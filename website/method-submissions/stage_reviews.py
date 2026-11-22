"""Reconcile one upstream review branch per method issue."""
from __future__ import annotations

import json
import os
import subprocess

from sync import PRIVATE_SOURCE, fetch_issues, parse_issue, write_archive

BASE_BRANCH = 'main'
BRANCH_PREFIX = 'method-submissions/issue-'
ARCHIVE_PATHS = ('method-submissions/received', 'method-submissions/checks')


def git(*args: str) -> str:
    return subprocess.check_output(['git', *args], text=True).strip()


def gh(*args: str) -> str:
    return subprocess.check_output(['gh', *args], text=True).strip()


def review_branches() -> dict[str, str]:
    refs = git('ls-remote', '--heads', 'origin', f'refs/heads/{BRANCH_PREFIX}*')
    return {ref.removeprefix('refs/heads/'): sha for sha, ref in (line.split() for line in refs.splitlines())}


def latest_review_state(branch: str) -> str | None:
    owner = PRIVATE_SOURCE.split('/', 1)[0]
    pulls = json.loads(gh('api', '--method', 'GET', f'repos/{PRIVATE_SOURCE}/pulls', '-f', 'state=all',
                          '-f', f'base={BASE_BRANCH}', '-f', f'head={owner}:{branch}', '-f', 'per_page=100'))
    pull = next((pull for pull in pulls if (pull['head']['repo'] or {}).get('full_name') == PRIVATE_SOURCE), None)
    if pull:
        return 'merged' if pull['merged_at'] else pull['state']
    return None


def archive_matches(ref: str) -> bool:
    result = subprocess.run(['git', 'diff', '--cached', '--quiet', ref, '--', *ARCHIVE_PATHS])
    if result.returncode not in (0, 1):
        result.check_returncode()
    return result.returncode == 0


def push_snapshot(branch: str, base: str, previous: str | None, issue_number: int) -> None:
    # Parent the previous review snapshot as well as main. This fast-forwards
    # the review branch and uses main as a shared base for the generated index.
    parents = ['-p', base]
    if previous and previous != base:
        parents.extend(('-p', previous))
    commit = git('commit-tree', git('write-tree'), *parents, '-m', f'Stage method submission #{issue_number}')
    git('push', 'origin', f'{commit}:refs/heads/{branch}')


def stage_issue(issue: dict, base: str, branches: dict[str, str]) -> None:
    number = issue.get('number')
    if type(number) is not int or number < 1:
        return
    branch = f'{BRANCH_PREFIX}{number}'
    previous = branches.get(branch)
    record = parse_issue(issue)
    if not record and not previous:
        return

    git('reset', '--hard', '--quiet', base)
    if record:
        write_archive([issue])
        git('add', '--', *(path for path in ARCHIVE_PATHS if os.path.isdir(path)))
    changed = not archive_matches(base)
    if not changed and not previous:
        return

    review = latest_review_state(branch)
    if review == 'closed':
        # A reviewer can reopen a declined PR after requesting changes.
        return
    if not changed and review != 'open':
        return
    if previous:
        git('fetch', '--quiet', '--no-tags', '--depth=1', 'origin', f'refs/heads/{branch}')
        if git('rev-parse', 'FETCH_HEAD') != previous:
            raise RuntimeError(f'{branch} changed during reconciliation')
    if not previous or not archive_matches(previous):
        push_snapshot(branch, base, previous, number)
    if changed and review in (None, 'merged'):
        try:
            gh('pr', 'create', '--repo', PRIVATE_SOURCE, '--base', BASE_BRANCH, '--head', branch,
               '--title', f'Review method submission #{number}',
               '--body', f'Generated from issue #{number}. Review the archive changes before merging.')
        except subprocess.CalledProcessError:
            print(f'::error::Review branch {branch} was staged. Check Actions PR permissions or open its PR manually.')
            raise


def main() -> None:
    if os.environ.get('GITHUB_ACTIONS') != 'true' or os.environ.get('GITHUB_REPOSITORY') != PRIVATE_SOURCE:
        raise SystemExit('Run this script from the StatArena method submission workflow.')
    if git('status', '--porcelain'):
        raise SystemExit('The checkout must be clean before staging method reviews.')
    base = git('rev-parse', 'HEAD')
    branches = review_branches()
    failures = []
    for issue in fetch_issues():
        try:
            stage_issue(issue, base, branches)
        except (subprocess.CalledProcessError, RuntimeError) as error:
            number = issue['number']
            print(f'::error::Could not stage method submission #{number}: {error}')
            failures.append(number)
    git('reset', '--hard', '--quiet', base)
    if failures:
        raise SystemExit(f'Method submission reviews need attention: {failures}')


if __name__ == '__main__':
    main()
