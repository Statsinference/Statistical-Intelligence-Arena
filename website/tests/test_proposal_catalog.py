import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from build_proposal_catalog import (DOMAINS, MARKER, build_catalog, estimand_name,
                                    normalize_domain, parse_proposal, source_links)


def proposal(domain='cate', source='[A study](https://doi.org/10.1234/study)',
             target='Conditional average treatment effect (CATE). $2x$', keywords='Nonlinear; nonlinear; Limited overlap'):
    return f'''# A mechanism | with punctuation

## Research question
- **Primary domain.** `{domain}`
- **Keywords.** {keywords}
- **Question and intended use.** A CATE task, not ATE.

## Study design and data source
- **Motivation and references.** {source}
- **Population and sampling.** Independent units.

## Data-generating process and estimand
- **Estimand.** {target}
- **Truth check.** The formula is known.
'''


class CatalogTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.inputs = self.root / 'submissions'
        self.inputs.mkdir()
        self.output = self.root / 'by-domain'

    def write(self, text, name='case.md'):
        path = self.inputs / name
        path.write_text(text)
        return path

    def test_full_record_and_output_links(self):
        path = self.write(proposal())
        before = path.read_bytes()
        records = build_catalog(self.inputs, self.output)
        self.assertEqual(records[0]['domain'], 'cate')
        self.assertEqual(records[0]['estimand'], 'CATE')
        self.assertEqual(records[0]['keywords'], 'Nonlinearity · Weak overlap')
        result = (self.output / 'cate.md').read_text()
        self.assertIn('[A study](https://doi.org/10.1234/study)', result)
        self.assertIn('(../submissions/case.md)', result)
        self.assertIn('mechanism &#124;', result)
        self.assertIn('| Source | DGP mechanism | Keywords | Estimand |', result)
        self.assertNotIn('$2x$', result)
        self.assertNotIn('Review status', result)
        self.assertNotIn('Scenarios', result)
        self.assertEqual(path.read_bytes(), before)

    def test_domains_and_aliases(self):
        for domain, name in DOMAINS.items():
            for value in (domain, name, name.upper()):
                self.assertEqual(normalize_domain(value), domain)
        for value in ('NR', 'NRI', 'Nonparametric   Regression', 'nonparametric-regression'):
            self.assertEqual(normalize_domain(value), 'nonparametric_regression')
        for value in ('did_sc', 'cate/ate', 'unknown', ''):
            self.assertIsNone(normalize_domain(value))

    def test_missing_unknown_conflicting_domains_are_listed(self):
        for index, value in enumerate(('', 'unrecognized', 'cate, ate')):
            self.write(proposal(domain=value), f'case-{index}.md')
        self.write(proposal().replace('- **Keywords.**', '- **Domain.** ate\n- **Keywords.**'), 'conflict.md')
        records = build_catalog(self.inputs, self.output)
        self.assertEqual(len(records), 4)
        self.assertTrue(all(r['domain'] == 'unclassified' for r in records))
        self.assertIn('4 proposal(s)', (self.output / 'unclassified.md').read_text())

    def test_title_comments_and_code_cannot_assign_domain(self):
        text = proposal().replace('- **Primary domain.** `cate`', '')
        text += '\n<!-- - **Primary domain.** cate -->\n```markdown\n## Research question\n- **Primary domain.** cate\n```\n'
        self.assertEqual(parse_proposal(self.write(text, 'cate-prefix.md'))['domain'], 'unclassified')

    def test_source_link_forms_and_distinct_sources(self):
        text = '[First](https://doi.org/10.1234/a)\n[Second][b]; https://example.org/paper; DOI 10.1234/c'
        found = source_links(text, {'b': 'https://example.org/second'})
        self.assertEqual(len(found), 4)
        self.assertIn(('Second', 'https://example.org/second'), found)
        self.assertIn(('DOI', 'https://doi.org/10.1234/c'), found)
        self.assertEqual(source_links('[One](https://doi.org/10.1234/a(b))', {}),
                         [('One', 'https://doi.org/10.1234/a(b)')])

    def test_multiline_reference_links_and_duplicate_links(self):
        text = proposal(source='A reference:\n  [Study][ref]\n  [Study][ref]')
        text += '\n[ref]: https://example.org/paper\n'
        record = parse_proposal(self.write(text))
        self.assertEqual(record['source'], '[Study](https://example.org/paper)')

    def test_citation_title_and_fallback_text(self):
        text = 'Author (2020), *A paper title*, [DOI](https://doi.org/10.1234/x).'
        self.assertEqual(source_links(text, {}), [('A paper title', 'https://doi.org/10.1234/x')])
        record = parse_proposal(self.write(proposal(source='Author, A paper without URL.')))
        self.assertEqual(record['source'], 'Author, A paper without URL.')
        self.assertIn('No source link identified.', record['warnings'])

    def test_public_materials_does_not_promote_arbitrary_code_link(self):
        text = proposal(source='') + '\n## Materials and access\n- **Public materials.** [Code](https://github.com/example/repo)'
        self.assertEqual(parse_proposal(self.write(text))['source'], 'Source not specified')

    def test_named_estimands_and_no_formula_or_domain_guessing(self):
        cases = {'CATE. $2x$': 'CATE', 'average treatment effect on the treated (ATT).': 'ATT',
                 'Natural indirect effect (NIE).': 'NIE', 'Conditional quantile.': 'Conditional quantile',
                 '$E[Y(1)-Y(0)]$. Not a CATE.': 'Name pending', 'Not an ATE.': 'Name pending',
                 'CATE and ATE': 'Name pending', 'Unfamiliar target.': 'Name pending'}
        for raw, expected in cases.items():
            with self.subTest(raw=raw):
                self.assertEqual(estimand_name(raw), expected)
        record = parse_proposal(self.write(proposal(domain='iv', target='$formula$', keywords='')))
        self.assertEqual(record['estimand'], 'Name pending')
        self.assertEqual(record['keywords'], 'Not specified')

    def test_display_formula_cannot_expose_following_negated_name(self):
        record = parse_proposal(self.write(proposal(target='\n$$\nformula\n$$\nNot ATE.')))
        self.assertEqual(record['estimand'], 'Name pending')

    def test_rebuild_is_deterministic_and_handles_moves_and_deletions(self):
        path = self.write(proposal())
        build_catalog(self.inputs, self.output)
        first = {p.name: p.read_bytes() for p in self.output.glob('*.md')}
        build_catalog(self.inputs, self.output)
        self.assertEqual(first, {p.name: p.read_bytes() for p in self.output.glob('*.md')})
        path.write_text(proposal(domain='ate', target='ATE.'))
        build_catalog(self.inputs, self.output)
        self.assertNotIn('../submissions/case.md', (self.output / 'cate.md').read_text())
        self.assertIn('../submissions/case.md', (self.output / 'ate.md').read_text())
        path.unlink()
        build_catalog(self.inputs, self.output)
        self.assertNotIn('../submissions/case.md', (self.output / 'ate.md').read_text())

    def test_only_generated_files_are_replaced(self):
        self.output.mkdir()
        (self.output / 'notes.md').write_text('Keep my notes')
        (self.output / 'old.md').write_text(MARKER + '\nOld catalog')
        build_catalog(self.inputs, self.output)
        self.assertFalse((self.output / 'old.md').exists())
        self.assertEqual((self.output / 'notes.md').read_text(), 'Keep my notes')
        (self.output / 'cate.md').write_text('Manual page')
        with self.assertRaises(ValueError):
            build_catalog(self.inputs, self.output)
        self.assertEqual((self.output / 'cate.md').read_text(), 'Manual page')

    def test_read_failure_leaves_existing_catalog_intact(self):
        self.write(proposal())
        build_catalog(self.inputs, self.output)
        before = (self.output / 'cate.md').read_bytes()
        self.write('```unclosed', 'broken.md')
        with self.assertRaises(ValueError):
            build_catalog(self.inputs, self.output)
        self.assertEqual(before, (self.output / 'cate.md').read_bytes())

    def test_guide_documents_catalog_domains(self):
        root = Path(__file__).resolve().parents[1] / 'data-submissions/simulated-dgp'
        for domain in DOMAINS:
            self.assertIn(f'| `{domain}` |', (root / 'README.md').read_text())


if __name__ == '__main__':
    unittest.main()
