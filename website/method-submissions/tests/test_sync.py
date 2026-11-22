import copy
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
spec = importlib.util.spec_from_file_location('submission_sync', Path(__file__).parents[1] / 'sync.py')
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
URL = 'https://huggingface.co/Brownight/tabpfn-iv-adapter-v0.3'

def issue(n=1):
    return {'number': n, 'title': '[Method submission] Brownight/tabpfn-iv-adapter-v0.3', 'body': f'### Hugging Face model link\n{URL}\n\n### Research domain\niv\n\n{m.MARKER}', 'user': {'login': 'brownight'}, 'state': 'open', 'created_at': '2026-11-17T03:00:00Z', 'updated_at': '2026-11-17T03:00:00Z'}

class ArchiveTests(unittest.TestCase):
    def test_general_method_form_archives_completed_markdown(self):
        checklist = (
            '# StatArena method checklist\n\n'
            '## Method name and version\n\nMethod name: Wald | IV\n\nVersion: v1.0\n\n'
            '## Method description\n\nWald ratio with a bootstrap interval.\n\n'
            '## How to run\n\n```sh\npython run.py\n```\n\n'
            '## Inputs and outputs\n\nObserved study tables in, predictions CSV out.\n\n'
            '## Training and data exposure\n\nNone.'
        )
        link = 'https://github.com/example/wald'
        entry = issue(2)
        entry['title'] = '[Method submission] Method'
        entry['body'] = (
            f'### Method link\n\n{link}\n\n### Research domain\n\n'
            f'Instrumental Variables\n\n### Completed checklist\n\n{checklist}'
        ).replace('\n', '\r\n')
        record = m.parse_issue(entry)
        self.assertEqual(record['schema_version'], 3)
        self.assertEqual(record['domain'], 'iv')
        self.assertEqual(record['method_url'], link)
        self.assertEqual(record['method_name'], 'Wald | IV')
        self.assertEqual(record['version'], 'v1.0')
        self.assertEqual(record['estimator'], 'Wald ratio with a bootstrap interval.')
        self.assertEqual(record['checklist_markdown'], checklist)
        hf_entry = {**entry, 'body': entry['body'].replace(link, URL)}
        self.assertEqual(m.parse_issue(hf_entry)['huggingface_url'], URL)
        for old, new in (
            (link, 'javascript:alert(1)'),
            ('Instrumental Variables', 'Unknown'),
            (checklist.replace('\n', '\r\n'), '_No response_'),
        ):
            with self.subTest(new=new):
                self.assertIsNone(m.parse_issue({**entry, 'body': entry['body'].replace(old, new)}))
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.assertEqual(m.write_archive([issue(), entry], root), 2)
            index = (root / 'received/README.md').read_text()
            self.assertIn(r'[Wald \| IV](' + link + ')', index)
            self.assertIn(URL, index)

    def test_mediation_form_and_legacy_records_share_archive(self):
        fields = {
            'Method name': 'OLS product', 'Mediation method link': 'https://github.com/example/r-mediation/',
            'Release or commit': 'v1.2', 'Run instructions or analysis procedure': 'Rscript run.R',
            'Estimator and interval': 'Coefficient product with a percentile bootstrap.',
            'Training and data exposure': 'No pretraining. Development kit used for testing.',
            'Public development results': '_No response_',
        }
        entry = issue(2)
        entry['title'] = '[Method submission] Mediation'
        entry['body'] = '\r\n\r\n'.join(f'### {label}\r\n\r\n{value}' for label, value in fields.items())
        parsed = m.parse_issue(entry)
        self.assertEqual((parsed['schema_version'], parsed['domain'], parsed['method_url']),
                         (2, 'mediation', 'https://github.com/example/r-mediation'))
        self.assertNotIn('public_dev_results', parsed)
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            m.write_archive([issue(), entry], root)
            index = (root / 'received/README.md').read_text()
            self.assertIn(URL, index)
            self.assertIn('https://github.com/example/r-mediation', index)
        fields['Mediation method link'] = URL
        fields['Public development results'] = 'https://example.org/public-dev.csv'
        entry['body'] = '\n\n'.join(f'### {k}\n\n{v}' for k,v in fields.items())
        self.assertEqual(m.parse_issue(entry)['public_dev_results'], fields['Public development results'])
        self.assertEqual(m.parse_issue(entry)['huggingface_url'], URL)
        self.assertIsNone(m.parse_issue({**entry, 'body': entry['body'].replace(URL, 'https://github.com.evil.test/org/model')}))
        self.assertIsNone(m.parse_issue({**entry, 'body': entry['body'].replace('### Run instructions', '### Missing field')}))
        entry['body'] = entry['body'].replace(URL, 'https://example.org/method-card') + '\n\n### Official predictions\n\nhttps://example.org/predictions.csv'
        self.assertEqual(m.parse_issue(entry)['official_predictions_url'], 'https://example.org/predictions.csv')
        self.assertIsNone(m.parse_issue({**entry, 'body': entry['body'].replace('https://example.org/predictions.csv', 'javascript:alert(1)')}))
    def test_valid_link(self):
        self.assertEqual(m.parse_issue(issue())['huggingface_url'], URL)
        self.assertEqual(m.canonical_url(URL+'/'), URL)
        self.assertEqual(m.canonical_url(URL+'/tree/v0.3'), URL+'/tree/v0.3')
    def test_reject_unsafe_urls(self):
        for url in ['http://huggingface.co/a/b','https://huggingface.co.evil.test/a/b','https://huggingface.co@evil.test/a/b',URL+'?token=secret',URL+'#x',URL+'/../evil','https://huggingface.co/datasets/a','https://huggingface.co/spaces/a',URL+'\n$(bad)', 'javascript:alert(1)', URL+'/tree/../../main']:
            self.assertIsNone(m.canonical_url(url), url)
    def test_non_submission_ignored(self):
        for key,value in [('title','Other issue'),('body','unstructured'),('pull_request',{'url':'x'}),('number','../../main'),('user',{'login':'evil|cell'}),('created_at','unknown')]:
            i=issue();i[key]=value;self.assertIsNone(m.parse_issue(i),key)
    def test_unknown_domain_safe(self):
        i=issue();i['body']=i['body'].replace('\niv\n','\nevil\n');self.assertEqual(m.parse_issue(i)['domain'],'unspecified')
    def test_archive_idempotency_and_edit(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d);i=issue();m.write_archive([i],root)
            before={p.name:p.read_bytes() for p in (root/'received').iterdir()}
            m.write_archive([i],root);self.assertEqual(before,{p.name:p.read_bytes() for p in (root/'received').iterdir()})
            i['state']='closed';m.write_archive([i],root)
            self.assertEqual(json.loads((root/'received/issue-000001.json').read_text())['status'],'closed')
            m.write_archive([],root);self.assertIn('Brownight/tabpfn', (root/'received/README.md').read_text())
    def test_test_record_separate(self):
        with tempfile.TemporaryDirectory() as d:
            i=issue();i['title']='[Method submission] [TEST] Brownight/tabpfn-iv-adapter-v0.3';root=Path(d);m.write_archive([i],root)
            self.assertTrue((root/'checks/issue-000001.json').exists())
            self.assertNotIn('Brownight/tabpfn', (root/'received/README.md').read_text())

if __name__ == '__main__': unittest.main()
