"""Exercise the actual workflow shell with fake Git/GitHub; no commits or network."""
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import textwrap
import unittest

WORKFLOW = Path(__file__).resolve().parents[2] / '.github/workflows/simulated-dgp-catalog.yml'
PUBLISH = textwrap.dedent(WORKFLOW.read_text().rsplit('        run: |\n', 1)[1])
OUTPUT = 'website/data-submissions/simulated-dgp/by-domain/'
BRANCH = 'submissions/simulated-dgp-catalog'
PR = 'https://example.test/example/arena/pull/42'
FAKE = r'''
import json, os, sys
from pathlib import Path
args = sys.argv[1:]
tool = Path(sys.argv[0]).name
root = Path(os.environ['FAKE_ROOT'])
mode = os.environ['FAKE_MODE']
with (root / 'calls').open('a') as log:
    log.write(json.dumps([tool, *args]) + '\n')
existing = mode in ('existing', 'already_generated', 'branch_changed', 'unchanged_existing')
if tool == 'gh':
    if args[0] == 'api':
        if existing:
            print('https://example.test/example/arena/pull/42')
    elif args[:2] == ['pr', 'create']:
        if mode == 'create_denied':
            sys.exit('Actions cannot create PRs')
        body = Path(args[args.index('--body-file') + 1]).read_text()
        (root / 'body').write_text(body)
        print('https://example.test/example/arena/pull/42')
    elif args[:2] != ['pr', 'close']:
        sys.exit('Unexpected gh command: ' + repr(args))
    sys.exit(0)
if args[:3] == ['diff', '--cached', '--quiet']:
    sys.exit(0 if mode.startswith('unchanged') else 1)
if args[:3] == ['diff', '--cached', '--name-only']:
    path = 'outside.txt' if mode == 'outside' else 'website/data-submissions/simulated-dgp/by-domain/cate.md'
    sys.stdout.write(path + '\0')
elif args[0] == 'fetch':
    (root / 'fetched').write_text(args[-1])
elif args[0] == 'rev-parse':
    if args[1] == 'HEAD':
        print('base')
    elif args[1] == 'FETCH_HEAD':
        if (root / 'fetched').read_text() == 'refs/heads/main':
            print('new_base' if mode == 'main_changed' else 'base')
        else:
            print('unexpected_head' if mode == 'branch_changed' else 'previous')
    elif args[1] == 'previous^{tree}':
        print('tree' if mode == 'already_generated' else 'old_tree')
    else:
        sys.exit('Unexpected rev-parse: ' + repr(args))
elif args[0] == 'ls-remote':
    if existing and not mode.startswith('unchanged'):
        print('previous\trefs/heads/submissions/simulated-dgp-catalog')
elif args[0] == 'merge-base':
    sys.exit(1)
elif args[0] == 'write-tree':
    print('tree')
elif args[0] == 'commit-tree':
    print('generated_commit')
elif args[0] == 'push':
    if mode == 'push_denied':
        sys.exit('Push rejected')
elif args[0] not in ('add', 'config'):
    sys.exit('Unexpected git command: ' + repr(args))
'''


class CatalogWorkflowTests(unittest.TestCase):
    def run_publish(self, mode):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        root = Path(temp.name)
        for name in ('git', 'gh'):
            path = root / name
            path.write_text('#!' + sys.executable + '\n' + FAKE)
            path.chmod(0o755)
        (root / 'python').symlink_to(sys.executable)
        env = dict(os.environ, PATH=str(root) + os.pathsep + os.environ['PATH'],
                   FAKE_ROOT=str(root), FAKE_MODE=mode, GITHUB_REPOSITORY='example/arena',
                   GITHUB_REPOSITORY_OWNER='example', RUNNER_TEMP=str(root),
                   GITHUB_SERVER_URL='https://example.test', GITHUB_STEP_SUMMARY=str(root / 'summary'))
        result = subprocess.run(['bash', '-c', PUBLISH], cwd=root, env=env, capture_output=True, text=True)
        calls = [json.loads(line) for line in (root / 'calls').read_text().splitlines()]
        for call in calls:
            if call[:2] == ['git', 'push']:
                self.assertEqual(call[-1], 'generated_commit:refs/heads/' + BRANCH)
                self.assertFalse(any(arg.startswith('--force') for arg in call))
            self.assertNotIn('--admin', call)
            self.assertNotEqual(call[:3], ['gh', 'pr', 'review'])
            self.assertNotEqual(call[:3], ['gh', 'pr', 'merge'])
        return result, calls, root

    def test_shell_syntax(self):
        result = subprocess.run(['bash', '-n'], input=PUBLISH, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_unchanged_output_makes_no_commit_push_or_pr(self):
        result, calls, _ = self.run_publish('unchanged')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertFalse(any(c[:2] in (['git', 'commit-tree'], ['git', 'push'], ['gh', 'pr']) for c in calls))

    def test_obsolete_pr_is_closed_when_main_already_matches(self):
        result, calls, _ = self.run_publish('unchanged_existing')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn(['gh', 'pr', 'close', PR, '--repo', 'example/arena'], calls)
        self.assertFalse(any(c[:2] == ['git', 'push'] for c in calls))

    def test_new_pr_is_created_for_manual_review_and_merge(self):
        result, calls, root = self.run_publish('new')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue(any(c[:3] == ['gh', 'pr', 'create'] for c in calls))
        commit = next(c for c in calls if c[:2] == ['git', 'commit-tree'])
        self.assertEqual(commit[2:5], ['tree', '-p', 'base'])
        self.assertIn('merge it manually', (root / 'body').read_text())
        self.assertIn('manual merge', (root / 'summary').read_text())
        self.assertIn(PR, (root / 'summary').read_text())

    def test_existing_pr_updated_without_duplicate_and_preserves_history(self):
        result, calls, _ = self.run_publish('existing')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertFalse(any(c[:3] == ['gh', 'pr', 'create'] for c in calls))
        commit = next(c for c in calls if c[:2] == ['git', 'commit-tree'])
        self.assertEqual(commit[2:7], ['tree', '-p', 'base', '-p', 'previous'])

    def test_identical_review_branch_reuses_existing_pr(self):
        result, calls, _ = self.run_publish('already_generated')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertFalse(any(c[:2] in (['git', 'commit-tree'], ['git', 'push']) for c in calls))
        self.assertFalse(any(c[:3] == ['gh', 'pr', 'create'] for c in calls))

    def test_changed_main_or_review_branch_stops_before_mutation(self):
        for mode in ('main_changed', 'branch_changed', 'outside'):
            with self.subTest(mode=mode):
                result, calls, _ = self.run_publish(mode)
                self.assertNotEqual(result.returncode, 0)
                self.assertFalse(any(c[:2] in (['git', 'commit-tree'], ['git', 'push'], ['gh', 'pr']) for c in calls))

    def test_rejected_push_does_not_create_or_merge_pr(self):
        result, calls, _ = self.run_publish('push_denied')
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse(any(c[:2] == ['gh', 'pr'] for c in calls))

    def test_pr_creation_denial_fails_with_actionable_summary(self):
        result, calls, root = self.run_publish('create_denied')
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('create pull requests', (root / 'summary').read_text())
        self.assertFalse(any(c[:3] == ['gh', 'pr', 'merge'] for c in calls))

    def test_workflow_permissions_and_output_trigger_exclusion(self):
        text = WORKFLOW.read_text()
        self.assertIn('pull-requests: write', text)
        self.assertIn('GH_TOKEN: ${{ github.token }}', text)
        self.assertIn("'!website/data-submissions/simulated-dgp/by-domain/**'", text)
        self.assertNotIn('pull_request_target:', text)
        self.assertNotIn('gh pr merge', text)
        self.assertNotIn('--auto', text)
        self.assertIn("if: github.ref == 'refs/heads/main'", text)
