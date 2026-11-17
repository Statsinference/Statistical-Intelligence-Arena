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
        self.assertIn('<td>missing</td>', output)
        self.assertIn('<td>Not reported</td>', output)
        self.assertNotIn('Evidence status', output)
        self.assertNotIn('| unknown |', output)
        self.assertIn('Stored expression (meaning requires review)', output)
        self.assertIn('missing: Expected response difference', output)
        self.assertIn('<td>0</td>', output)
        self.assertNotIn('| reported_numeric |', output)
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
        self.assertIn('| Estimand | Scenarios | Review status |', page)
        self.assertIn('../drafts/test-entry.md', page)
        self.assertIn('| Needs review | 2 | Needs scientific review |', page)
        self.assertNotIn('An intentionally long target', page)
        self.assertIn('An intentionally long target \\|', detail_page)
        self.assertNotIn('Expected response difference', page)
        self.assertIn('Expected response difference', detail_page)
        self.assertIn('| 2 | Needs scientific review |', page)
        self.assertEqual(r, before)


    def test_large_variable_lists_are_condensed_without_changing_record(self):
        r = record()
        r['mechanism']['observed_variables'] = [
            {'name': 'X' + str(i)} for i in range(1, 1001)
        ] + [{'name': 'A'}, {'name': 'Y'}]
        before = copy.deepcopy(r)
        text = detail(r)
        self.assertIn('X1-X1000 (1000 variables), A, Y', text)
        self.assertIn('All observed variable names', text)
        self.assertIn('X1, X2, X3, X4', text)
        self.assertEqual(r, before)

    def test_no_false_compression_of_noncontiguous_or_padded_variables(self):
        from tools.dgp_registry.catalog import observed_variables_display
        values = [{'name': s} for s in ['X01', 'X02', 'X03', 'X04',
                                         'Z1', 'Z2', 'Z4', 'Z5']]
        text, names = observed_variables_display(values)
        self.assertEqual(text, ', '.join(names))

    def test_detail_keeps_generator_and_adaptations_but_tables_do_not(self):
        r = record()
        r['implementation'] = {'exported_generator_path': 'generators/test-entry.py'}
        r['adaptations'] = ['Changed the treatment assignment.']
        r['review_status'] = 'duplicate_conflict_needs_review'
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp)
            build([r], output)
            page = (output / 'by-domain' / 'mediation.md').read_text(encoding='utf-8')
            index = (output / 'INDEX.md').read_text(encoding='utf-8')
            summary = (output / 'PR_SUMMARY.md').read_text(encoding='utf-8')
            detail_page = (output / 'drafts' / 'test-entry.md').read_text(encoding='utf-8')
        self.assertNotIn('Generator.py', page)
        self.assertNotIn('Generator.py', index)
        self.assertNotIn('Generator.py', summary)
        self.assertIn('../generators/test-entry.py', detail_page)
        self.assertIn('Changed the treatment assignment.', detail_page)
        self.assertIn('Duplicate conflict - review required', page)


    def test_original_language_adaptations_link_to_raw_record(self):
        r = record()
        r['adaptations'] = ['????????']
        before = copy.deepcopy(r)
        page = detail(r)
        self.assertNotIn('????????', page)
        self.assertIn('English description pending', page)
        self.assertIn('./test-entry.json', page)
        self.assertEqual(r, before)


    def test_structured_doi_survives_catalog_summary_grouping(self):
        import json
        from tools.dgp_registry.paper_list import _domain_papers
        a = record()
        a['record_id'] = 'doi-test-1'
        a['paper'] = {'citation': 'A. Example (2020). Matching Paper. DOI: 10.1234/example',
                      'doi': '10.1234/example', 'title': 'Matching Paper'}
        b = copy.deepcopy(a)
        b['record_id'] = 'doi-test-2'
        b['paper']['citation'] = 'A. Example (2020). Matching Paper.'
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp)
            build([a, b], output)
            records = json.loads((output / 'catalog.json').read_text(encoding='utf-8'))['records']
        self.assertEqual([r['paper_doi'] for r in records], ['10.1234/example'] * 2)
        self.assertEqual(len(_domain_papers(records)), 1)



if __name__ == '__main__':
    unittest.main()


