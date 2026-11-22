from contextlib import ExitStack
import functools
import json
import os
from pathlib import Path
import sys
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import stage_reviews as review
from sync import write_archive
from test_sync import issue


class StageReviewsTests(unittest.TestCase):
    def setUp(self):
        context = ExitStack()
        self.addCleanup(context.close)
        scratch = context.enter_context(TemporaryDirectory())
        work = Path(scratch) / 'work'
        work.mkdir()
        context.callback(os.chdir, Path.cwd())
        os.chdir(work)
        self.repo = review.git
        remote = str(Path(scratch) / 'remote.git')
        self.repo('init', '-q', '--bare', '-b', 'main', remote)
        self.repo('init', '-q', '-b', 'main')
        self.repo('config', 'user.name', 'Submission test')
        self.repo('config', 'user.email', 'submission-test@example.com')
        self.repo('remote', 'add', 'origin', remote)
        self.archive = work / 'method-submissions'
        write_archive([issue(34)], self.archive)
        self.repo('add', 'method-submissions')
        self.repo('commit', '-qm', 'Previous approved archive')
        self.repo('push', 'origin', 'main')
        self.reviews = {}
        self.calls = []
        context.enter_context(patch.object(review, 'write_archive', functools.partial(write_archive, root=self.archive)))
        context.enter_context(patch.object(review, 'gh', side_effect=self.gh))

    def gh(self, command, *args):
        if command == 'api':
            branch = next(arg for arg in args if arg.startswith('head=')).split(':', 1)[1]
            return json.dumps(self.reviews.get(branch, []))
        self.assertEqual((command, args[0]), ('pr', 'create'))
        branch = args[args.index('--head') + 1]
        self.calls.append(branch)
        self.reviews.setdefault(branch, []).insert(0, {
            'state': 'open', 'merged_at': None, 'head': {'repo': {'full_name': review.PRIVATE_SOURCE}},
        })
        return ''

    def stage(self, *issues):
        main = self.repo('rev-parse', 'main')
        branches = review.review_branches()
        for item in issues:
            review.stage_issue(item, main, branches)
        self.repo('reset', '--hard', '-q', main)
        self.assertEqual(main, self.repo('rev-parse', 'main'))
        self.assertEqual(main, self.repo('ls-remote', 'origin', 'refs/heads/main').split()[0])

    def get_branch(self, number):
        return review.review_branches()[f'{review.BRANCH_PREFIX}{number}']

    def test_multiple_issues_edits_merges_and_invalid_updates(self):
        first, second = issue(1), issue(2)
        self.stage(first, second, issue(34))
        first_head = self.get_branch(1)
        second_head = self.get_branch(2)
        self.assertEqual(self.calls, ['method-submissions/issue-1', 'method-submissions/issue-2'])
        self.assertEqual(len(review.review_branches()), 2)
        self.assertEqual(self.repo('diff', '--name-only', 'main', first_head).splitlines(), [
            'method-submissions/received/README.md',
            'method-submissions/received/issue-000001.json',
            'method-submissions/received/iv/ISSUES.md',
        ])

        self.stage(first, second)
        self.assertEqual(self.get_branch(1), first_head)
        self.assertEqual(self.get_branch(2), second_head)

        first = {**first, 'state': 'closed'}
        self.stage(first, second)
        edited_head = self.get_branch(1)
        self.assertNotEqual(first_head, edited_head)
        self.assertEqual(self.repo('merge-base', first_head, edited_head), first_head)
        self.assertEqual(len(self.calls), 2)

        self.repo('merge', '--no-ff', '-qm', 'Approve issue 1', edited_head)
        self.repo('push', 'origin', 'main')
        self.reviews['method-submissions/issue-1'][0].update(state='closed', merged_at='2026-11-22T14:00:00Z')
        self.stage(first, second)
        rebased_second = self.get_branch(2)
        self.assertEqual(self.repo('merge-base', 'main', rebased_second), self.repo('rev-parse', 'main'))
        self.assertIn('issue-000001.json', self.repo('ls-tree', '-r', '--name-only', rebased_second))
        self.assertEqual(len(self.calls), 2)

        self.stage(first, {**second, 'body': 'Invalid after edit'})
        self.assertEqual(self.repo('diff', '--name-only', 'main', self.get_branch(2)), '')
        self.assertEqual(len(self.calls), 2)
        self.stage(first, second)
        self.assertIn('issue-000002.json', self.repo('diff', '--name-only', 'main', self.get_branch(2)))
        self.assertEqual(len(self.calls), 2)


if __name__ == '__main__':
    unittest.main()
