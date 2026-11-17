"""Regression tests for compact catalog views and truthful missing values."""
import copy
import tempfile
import unittest
from pathlib import Path

from tools.dgp_registry.catalog import build, detail, truth_pairs


def record():
    return {
        'record_id': 'test-entry', 'domain': 'mediation',
        'paper': {'citation': 'Researcher (2020). Test Paper.'},
        'mechanism': {'name': 'Example mechanism', 'generation_equations': []},
        'estimand': {'name': 'An intentionally long target | ' + 'x' * 100,
                     'definition': 'Expected response difference'},
        'scenarios': [
            {'id': 'missing', 'truth': {'value': None,
                                        'expression': 'Expected response difference',
                                        'status': 'unknown'}},
            {'id': 'zero', 'truth': {'value': 0, 'status': 'reported_numeric'}},
        ],
    }


class DomainPresentationTests(unittest.TestCase):
    def test_missing_value_is_not_misrepresented_as_a_numeric_truth(self):
        r = record()
        before = copy.deepcopy(r)
        output = detail(r)
        self.assertIn('| missing |', output)
        self.assertIn('| Not reported | unknown |', output)
        self.assertIn('Stored expression (meaning requires review)', output)
        self.assertIn('missing: Expected response difference', output)
        self.assertIn('| 0 | reported_numeric |', output)
        self.assertIn('missing:', truth_pairs(r))
        self.assertIn('not reported', truth_pairs(r))
        self.assertEqual(r, before)

    def test_domain_listing_is_compact_and_links_to_complete_details(self):
        r = record()
        before = copy.deepcopy(r)
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp)
            build([r], output)
            page = (output / 'by-domain' / 'mediation.md').read_text(encoding='utf-8')
            detail_page = (output / 'drafts' / 'test-entry.md').read_text(encoding='utf-8')
        self.assertIn('Target (submitted name)', page)
        self.assertIn('../drafts/test-entry.md', page)
        self.assertIn('An intentionally long target \\|', page)
        self.assertIn('…', page)
        self.assertNotIn('Expected response difference', page)
        self.assertIn('Expected response difference', detail_page)
        self.assertIn('| 2 | Needs review |', page)
        self.assertEqual(r, before)


if __name__ == '__main__':
    unittest.main()
