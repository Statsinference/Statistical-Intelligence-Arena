"""Exercise real Git diffs, including symlink and code-change bypass attempts."""
import copy
import importlib.util
import io
import os
from pathlib import Path
import subprocess
import tempfile
import unittest
import zipfile

SCRIPT = Path(__file__).resolve().parents[1]/'integration/zip_only_gate.py'
spec = importlib.util.spec_from_file_location('zip_only_gate', SCRIPT)
gate = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gate)


def archive():
    data = io.BytesIO()
    with zipfile.ZipFile(data, 'w') as z:
        z.writestr('hello.txt', 'Data, not executed code')
    return data.getvalue()


class ZipOnlyGateTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.git('init', '-q')
        self.git('config', 'user.name', 'ZIP gate test')
        self.git('config', 'user.email', 'zip-gate@example.invalid')
        self.git('config', 'core.filemode', 'true')
        (self.root/'README.md').write_text('Trusted project README\n')
        (self.root/'dgp-submissions/incoming').mkdir(parents=True)
        (self.root/'dgp-submissions/incoming/old.zip').write_bytes(archive())
        self.commit()
        self.base = self.git('rev-parse', 'HEAD').decode().strip()

    def tearDown(self):
        self.tmp.cleanup()

    def git(self, *args):
        return subprocess.check_output(['git', *args], cwd=self.root, stderr=subprocess.PIPE)

    def commit(self):
        self.git('add', '-A')
        self.git('commit', '-qm', 'test change')
        return self.git('rev-parse', 'HEAD').decode().strip()

    def diff(self):
        return gate.changes(self.root, self.base, self.commit())

    def add(self, path='dgp-submissions/incoming/new.zip', data=None):
        p=self.root/path
        p.parent.mkdir(parents=True,exist_ok=True)
        p.write_bytes(archive() if data is None else data)
        return p

    def test_all_zip_additions_pass(self):
        self.add()
        self.add('dgp-submissions/incoming/two.ZIP')
        items=gate.validate_diff(self.diff())
        self.assertEqual(len(items),2)
        for item in items:
            self.assertEqual(gate.zip_blob(self.root,item),archive())

    def test_zip_replacement_passes(self):
        self.add('dgp-submissions/incoming/old.zip',archive()+b'updated')
        items=gate.validate_diff(self.diff())
        self.assertEqual(items[0]['status'],'M')

    def test_zip_plus_readme_rejected(self):
        self.add()
        (self.root/'README.md').write_text('untrusted change')
        with self.assertRaises(ValueError):gate.validate_diff(self.diff())

    def test_code_only_pr_rejected(self):
        self.add('dgp-submissions/tools/new.py',b'print("attack")')
        with self.assertRaises(ValueError):gate.validate_diff(self.diff())

    def test_workflow_modification_rejected(self):
        self.add('.github/workflows/dgp-submissions.yml',b'name: untrusted')
        with self.assertRaises(ValueError):gate.validate_diff(self.diff())

    def test_file_disguised_with_zip_extension(self):
        self.add(data=b'not really a zip')
        item=gate.validate_diff(self.diff())[0]
        with self.assertRaises(ValueError):gate.zip_blob(self.root,item)

    def test_zip_inside_wrong_directory_rejected(self):
        self.add('site/new.zip')
        with self.assertRaises(ValueError):gate.validate_diff(self.diff())

    def test_zip_subdirectories_not_allowed(self):
        self.add('dgp-submissions/incoming/nested/new.zip')
        with self.assertRaises(ValueError):gate.validate_diff(self.diff())

    def test_deleted_zip_rejected(self):
        (self.root/'dgp-submissions/incoming/old.zip').unlink()
        with self.assertRaises(ValueError):gate.validate_diff(self.diff())

    def test_renamed_zip_rejected(self):
        (self.root/'dgp-submissions/incoming/old.zip').rename(self.root/'dgp-submissions/incoming/moved.zip')
        with self.assertRaises(ValueError):gate.validate_diff(self.diff())

    def test_symlink_disguised_as_zip_rejected(self):
        (self.root/'dgp-submissions/incoming/evil.zip').symlink_to('../../README.md')
        with self.assertRaises(ValueError):gate.validate_diff(self.diff())

    def test_executable_zip_rejected(self):
        self.add().chmod(0o755)
        with self.assertRaises(ValueError):gate.validate_diff(self.diff())

    def test_empty_diff_rejected(self):
        self.assertEqual(gate.changes(self.root,self.base,self.base),[])
        with self.assertRaises(ValueError):gate.validate_diff([])

    def test_submodule_and_mode_changes_rejected(self):
        item={'path':'dgp-submissions/incoming/new.zip','status':'A',
              'mode':'160000','old_mode':'000000','blob':self.base}
        with self.assertRaises(ValueError):gate.validate_diff([item])

    def test_latest_main_changes_are_not_mistaken_for_pr_changes(self):
        self.add(); head=self.commit()
        self.git('checkout','-q',self.base)
        (self.root/'README.md').write_text('main maintainer update')
        newer_base=self.commit()
        items=gate.validate_diff(gate.changes(self.root,newer_base,head))
        self.assertEqual([x['path'] for x in items],['dgp-submissions/incoming/new.zip'])

    def test_stale_failed_replacement_is_not_approved(self):
        state=self.root/'state.json'
        state.write_text('{"paths":["dgp-submissions/incoming/new.zip"]}')
        folder=self.root/'dgp-submissions/registry';folder.mkdir()
        (folder/'INTAKE_REPORT.json').write_text('{"failures":[{"source":"incoming/new.zip","message":"invalid"}]}')
        with self.assertRaises(ValueError):gate.verify_report(self.root,state)

    def test_other_old_bad_zip_does_not_block_this_pr(self):
        state=self.root/'state.json'
        state.write_text('{"paths":["dgp-submissions/incoming/new.zip"]}')
        folder=self.root/'dgp-submissions/registry';folder.mkdir()
        (folder/'INTAKE_REPORT.json').write_text('{"failures":[{"source":"incoming/other.zip","message":"invalid"}]}')
        gate.verify_report(self.root,state)


if __name__=='__main__':
    unittest.main()
