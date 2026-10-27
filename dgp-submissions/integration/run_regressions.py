"""Run parser regression tests on a frozen corpus, not on unreviewed new ZIPs.

Live submissions are handled separately by github_intake with per-input reports.
Synthetic tests exercise malformed, high-dimensional and interference inputs.
No submitted generator is executed.
"""
from __future__ import annotations

import io
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path, PurePosixPath

FIXTURE_COMMIT = '7585d6cd609a5948868d7d45351eb42fd258bbe0'
HOME = Path(__file__).resolve().parents[1]
ROOT = HOME.parent


def main():
    archive_bytes = subprocess.check_output([
        'git','archive','--format=zip',FIXTURE_COMMIT,
        'dgp-submissions/incoming','dgp-submissions/registry',
    ], cwd=ROOT)
    with tempfile.TemporaryDirectory(prefix='statsarena-regression-') as folder:
        work=Path(folder)
        for name in ('tools','tests','examples','docs','integration'):
            shutil.copytree(HOME/name,work/name,
                            ignore=shutil.ignore_patterns('__pycache__','*.pyc'))
        for name in ('README.md','CONTRIBUTING.md'):
            shutil.copyfile(HOME/name,work/name)
        with zipfile.ZipFile(io.BytesIO(archive_bytes)) as z:
            for item in z.infolist():
                parts=PurePosixPath(item.filename).parts
                if parts == ('dgp-submissions',) and item.is_dir():
                    continue
                if len(parts)<2 or parts[0]!='dgp-submissions' or '..' in parts:
                    raise ValueError('Unexpected fixture archive member')
                dest=work.joinpath(*parts[1:])
                if item.is_dir():
                    dest.mkdir(parents=True,exist_ok=True)
                else:
                    dest.parent.mkdir(parents=True,exist_ok=True)
                    dest.write_bytes(z.read(item))
        print('Regression corpus pinned to '+FIXTURE_COMMIT+'; live incoming ZIPs are not test fixtures.',flush=True)
        return subprocess.run([sys.executable,'-m','pytest','tests',
                               '--ignore=tests/test_integration.py','-q'],cwd=work).returncode


if __name__=='__main__':
    raise SystemExit(main())
