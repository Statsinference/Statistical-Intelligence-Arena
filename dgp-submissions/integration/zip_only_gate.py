"""Trusted-base PR gate. Inspect Git blobs; NEVER check out or execute PR code.

The workflow must use pull_request_target and check out the base SHA. The only
repository write permission needed is statuses:write, to attach the result to
exactly the reviewed PR head. No file writes or merges occur on GitHub here.
"""
from __future__ import annotations

import base64
import io
import json
import os
from pathlib import Path
import re
import subprocess
import sys
from urllib.request import Request, urlopen
import zipfile

CONTEXT = 'DGP ZIP-only'
PREFIX = 'dgp-submissions/incoming/'
PATH_RE = re.compile(re.escape(PREFIX) + r'[A-Za-z0-9][A-Za-z0-9._-]{0,199}\.[zZ][iI][pP]')
SHA_RE = re.compile(r'[0-9a-f]{40}')
MAX_BYTES = 25 * 1024 * 1024
STATE_NAME = 'dgp-zip-only-state.json'


def git(root: Path, *args: str) -> bytes:
    return subprocess.check_output(['git', *args], cwd=root, stderr=subprocess.PIPE)


def changes(root: Path, base: str, head: str) -> list[dict]:
    if not SHA_RE.fullmatch(base) or not SHA_RE.fullmatch(head):
        raise ValueError('Invalid immutable commit SHA')
    ancestor = git(root, 'merge-base', base, head).decode().strip()
    raw = git(root, 'diff', '--raw', '-z', '--no-renames', '--no-ext-diff',
              '--no-textconv', '--no-abbrev', ancestor, head, '--')
    parts = raw.split(b'\0')
    if parts[-1] == b'':
        parts.pop()
    if len(parts) % 2:
        raise ValueError('Cannot read complete Git diff')
    result = []
    for i in range(0, len(parts), 2):
        fields = parts[i].decode('ascii').split()
        if len(fields) != 5 or not fields[0].startswith(':'):
            raise ValueError('Unexpected Git diff metadata')
        result.append(dict(path=parts[i+1].decode('utf-8', errors='strict'),
                           old_mode=fields[0][1:], mode=fields[1],
                           blob=fields[3], status=fields[4]))
    return result


def validate_diff(items: list[dict]) -> list[dict]:
    if not items:
        raise ValueError('No changed ZIP files to review')
    problems = []
    for item in items:
        path = item['path']
        if not PATH_RE.fullmatch(path):
            problems.append(f'{path!r}: only ZIP files directly under {PREFIX} are allowed')
        if item['status'] not in ('A', 'M'):
            problems.append(f'{path!r}: deletions/renames/type changes are not allowed')
        if item['mode'] != '100644' or item['old_mode'] not in ('000000', '100644'):
            problems.append(f'{path!r}: must be a regular, non-executable file; no symlinks/submodules')
        if not SHA_RE.fullmatch(item['blob']):
            problems.append(f'{path!r}: invalid blob identifier')
    if problems:
        raise ValueError('\n'.join(problems[:50]))
    return items


def zip_blob(root: Path, item: dict) -> bytes:
    size = int(git(root, 'cat-file', '-s', item['blob']))
    if size <= 0 or size > MAX_BYTES:
        raise ValueError(f"{item['path']}: ZIP must be nonempty and at most 25 MiB")
    payload = git(root, 'cat-file', 'blob', item['blob'])
    if len(payload) != size or not zipfile.is_zipfile(io.BytesIO(payload)):
        raise ValueError(f"{item['path']}: not a readable ZIP archive")
    return payload


def api(repo: str, endpoint: str, payload=None):
    if not re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+', repo):
        raise ValueError('Invalid base repository')
    token = os.environ['GH_TOKEN']
    request = Request('https://api.github.com/repos/' + repo + endpoint,
                      data=None if payload is None else json.dumps(payload).encode(),
                      headers={'Authorization': 'Bearer ' + token,
                               'Accept': 'application/vnd.github+json',
                               'X-GitHub-Api-Version': '2022-11-28',
                               'Content-Type': 'application/json'})
    with urlopen(request, timeout=30) as response:
        return json.load(response)


def report(text: str):
    # Prevent untrusted filenames from becoming Actions workflow commands/HTML.
    safe = text.replace('::', ': :').replace('<', '&lt;').replace('>', '&gt;')
    print(safe, flush=True)
    summary = os.environ.get('GITHUB_STEP_SUMMARY')
    if summary:
        with open(summary, 'a', encoding='utf-8') as stream:
            stream.write('\n' + safe + '\n')


def status(state: dict, verdict: str, description: str):
    run_id = os.environ['GITHUB_RUN_ID']
    api(state['repo'], '/statuses/' + state['head'], {
        'state': verdict, 'context': CONTEXT, 'description': description[:140],
        'target_url': f"https://github.com/{state['repo']}/actions/runs/{run_id}"})


def check(root: Path, state_path: Path):
    event = json.loads(Path(os.environ['GITHUB_EVENT_PATH']).read_text())
    number = event.get('number')
    if type(number) is not int or number <= 0:
        raise ValueError('This gate requires a pull_request_target event')
    repo = os.environ['GITHUB_REPOSITORY']
    pr = api(repo, f'/pulls/{number}')
    head = pr['head']['sha']
    base = git(root, 'rev-parse', 'HEAD').decode().strip()
    state = dict(repo=repo, number=number, head=head, base=base, passed=False)
    state_path.write_text(json.dumps(state))
    status(state, 'pending', 'Reviewing all changed paths and ZIP inputs')
    if pr['state'] != 'open' or pr['base']['ref'] != 'main':
        raise ValueError('Only open PRs targeting main are accepted')
    if pr['base']['repo']['full_name'].lower() != repo.lower() or pr['base']['sha'] != base:
        raise ValueError('Base changed or checkout is not the trusted PR base; rerun the check')
    if not SHA_RE.fullmatch(head):
        raise ValueError('Invalid PR head SHA')
    auth = base64.b64encode(('x-access-token:' + os.environ['GH_TOKEN']).encode()).decode()
    # Fetch the public PR ref from the BASE repository. Never checkout its files.
    # Arguments are passed without a shell; credentials are not persisted/logged.
    git(root, '-c', 'http.https://github.com/.extraheader=AUTHORIZATION: basic ' + auth,
        'fetch', '--no-tags', '--no-recurse-submodules', 'origin',
        f'+refs/pull/{number}/head:refs/remotes/dgp-intake/review')
    fetched = git(root, 'rev-parse', 'refs/remotes/dgp-intake/review').decode().strip()
    if fetched != head:
        raise ValueError('PR changed during fetch; rerun on the latest commit')
    items = validate_diff(changes(root, base, head))
    # Validate every blob BEFORE changing the preview workspace.
    for item in items:
        zip_blob(root, item)  # Bounded per-file memory; do not accumulate ZIP payloads.
    latest = api(repo, f'/pulls/{number}')
    if latest['head']['sha'] != head or latest['base']['sha'] != base:
        raise ValueError('PR changed during review; rerun on the latest commit')
    for item in items:
        payload = zip_blob(root, item)
        destination = root / item['path']
        if destination.is_symlink() or destination.parent.resolve() != (root/PREFIX).resolve():
            raise ValueError('Unsafe ZIP destination')
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes(payload)
    state.update(passed=True, paths=[i['path'] for i in items])
    state_path.write_text(json.dumps(state))
    report('## ZIP-only diff: PASS\n\n' + '\n'.join('- `' + i['path'] + '` (' + i['status'] + ')' for i in items)
           + '\n\nOnly these ZIP blobs were loaded into the trusted preview. No PR code was executed.')


def verify_report(root: Path, state_path: Path):
    state = json.loads(state_path.read_text())
    report_path = root/'dgp-submissions/registry/INTAKE_REPORT.json'
    data = json.loads(report_path.read_text())
    changed = {path.removeprefix('dgp-submissions/') for path in state['paths']}
    failures = [f for f in data.get('failures', []) if f.get('source') in changed]
    if failures:
        raise ValueError('Changed ZIP failed parsing: ' + json.dumps(failures, ensure_ascii=True))
    report('## Structured ZIP validation: PASS\n\nScientific review and maintainer merge are still required.')


def finish(root: Path, state_path: Path):
    state = json.loads(state_path.read_text())
    pr = api(state['repo'], f"/pulls/{state['number']}")
    current = (pr['head']['sha'] == state['head'] and pr['base']['sha'] == state['base']
               and pr['base']['ref'] == 'main' and pr['state'] == 'open')
    good = current and state.get('passed') and os.environ.get('JOB_STATUS') == 'success'
    status(state, 'success' if good else 'failure',
           'ZIP-only and parser checks passed; maintainer review required' if good else
           'ZIP-only/validation failed or PR changed; inspect this run before merging')
    if not good:
        raise ValueError('PR did not pass the ZIP-only submission checks')


def main():
    root = Path(subprocess.check_output(['git', 'rev-parse', '--show-toplevel']).decode().strip())
    state_path = Path(git(root, 'rev-parse', '--absolute-git-dir').decode().strip())/STATE_NAME
    action = sys.argv[1]
    try:
        {'check': check, 'verify-report': verify_report, 'finish': finish}[action](root, state_path)
    except subprocess.CalledProcessError:
        report('ZIP-only check failed: could not inspect the complete Git history. No changes approved.')
        return 1
    except Exception as error:
        # Never echo a command line or token into logs.
        report('ZIP-only check failed: ' + type(error).__name__ + ': ' + str(error)[:4000])
        return 1
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
