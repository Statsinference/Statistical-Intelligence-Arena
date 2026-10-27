"""Isolate malformed submissions without executing code or bypassing ZIP limits."""
from __future__ import annotations

import csv
import hashlib
import io
import json
import re
import zipfile
from pathlib import Path

from .domains import DOMAINS
from .zip_reader import filehash, from_collection, safe_zip

INPUT_ERRORS = (ValueError, TypeError, AttributeError, KeyError, IndexError,
                UnicodeError, OSError, RuntimeError, NotImplementedError,
                RecursionError, OverflowError, csv.Error, zipfile.BadZipFile)


def failure(source, error, member=None):
    """Keep a short error and a source location, not arbitrary full file contents."""
    return {'source': str(source), 'member': member,
            'error_type': type(error).__name__,
            'message': ' '.join(str(error).split())[:700]}


def read_zip_report(path: Path):
    """Return valid records and individual failures; unsafe ZIPs fail as a whole.

    The original read_archive API remains strict for callers and security tests.
    Only this intake entrypoint supports partial success.
    """
    path = Path(path)
    digest = None
    try:
        if path.stat().st_size > 25 * 1024 * 1024:
            raise ValueError('ZIP exceeds 25 MiB upload limit')
        data = path.read_bytes()
        digest = filehash(data)
        with zipfile.ZipFile(io.BytesIO(data)) as archive:
            safe_zip(archive)
            names = archive.namelist()
            if len(names) != len(set(names)):
                raise ValueError('Duplicate ZIP member names are ambiguous')
            prefixes = sorted(n[:-len('collection.json')] for n in names
                              if n == 'collection.json' or n.endswith('/collection.json'))
            if not prefixes:
                raise ValueError('no structured collection.json found')
            records, errors = [], []
            for prefix in prefixes:
                try:
                    records.append(from_collection(archive, prefix, path.name, digest))
                except INPUT_ERRORS as error:
                    errors.append(failure(path.as_posix(), error, prefix+'collection.json'))
            return records, [], errors, digest
    except INPUT_ERRORS as error:
        return [], [], [failure(path.as_posix(), error)], digest


def _cell(value):
    return (str(value or '—').replace('&', '&amp;').replace('<', '&lt;')
            .replace('>', '&gt;').replace('|', '\\|').replace('\n', ' '))


def write_intake_report(output, errors, *, source_count, records, stale_ids):
    output = Path(output)
    report = {
        'status': 'partial_success_needs_attention' if errors else 'success',
        'zip_count': source_count, 'indexed_dgp_count': len(records),
        'failure_count': len(errors), 'stale_record_ids': sorted(stale_ids),
        'failures': errors,
        'scientific_validation': 'not_performed',
    }
    (output/'INTAKE_REPORT.json').write_text(
        json.dumps(report, indent=2, ensure_ascii=False)+'\n', encoding='utf-8')
    lines = ['# Submission processing report', '',
             '**Status:** '+report['status'], '',
             f'{source_count} ZIP(s); {len(records)} indexed DGP(s); '
             f'{len(errors)} processing failure(s).', '',
             'A failed ZIP or DGP does not block unrelated valid submissions. '
             'Processing success is not scientific approval.', '']
    if errors:
        lines += ['| ZIP | DGP source | Error |', '|---|---|---|']
        for error in errors:
            lines.append('| '+' | '.join(_cell(error.get(key)) for key in
                                        ('source', 'member', 'message'))+' |')
    else:
        lines.append('No input processing failures.')
    if stale_ids:
        lines += ['', '## Retained last-valid records', '',
                  'These records are retained from an earlier parse because their source '
                  'currently fails. They do not certify the latest ZIP.', '']
        lines += ['- '+_cell(rid) for rid in sorted(stale_ids)]
    (output/'INTAKE_REPORT.md').write_text('\n'.join(lines)+'\n', encoding='utf-8')
    for name in ('INDEX.md', 'PR_SUMMARY.md'):
        path = output/name
        text = path.read_text(encoding='utf-8').replace(
            '## Six research areas', '## Research areas')
        first, separator, body = text.partition('\n')
        notice = (f'**Input processing:** {len(errors)} failure(s), {len(stale_ids)} '
                  'last-valid record(s) retained. [Submission report](INTAKE_REPORT.md).')
        path.write_text(first+'\n\n'+notice+'\n'+body, encoding='utf-8')
    catalog_path = output/'catalog.json'
    catalog = json.loads(catalog_path.read_text(encoding='utf-8'))
    catalog['intake'] = {key: val for key, val in report.items() if key != 'failures'}
    catalog_path.write_text(json.dumps(catalog, indent=2, ensure_ascii=False)+'\n',
                            encoding='utf-8')
    return report


def refresh_navigation(path: Path):
    """Update only this subsystem's navigation, not the benchmark root README."""
    path = Path(path)
    if not path.is_file():
        return
    text = path.read_text(encoding='utf-8')
    text = text.replace('## Browse the six research areas', '## Browse research areas')
    text = text.replace('alt="Browse six areas"', 'alt="Browse research areas"')
    text = text.replace('Browse-Six_DGP_Areas-', 'Browse-DGP_Research_Areas-')
    pattern = r'(## Browse research areas)[ \t]*\n\s*\[ATE\][^\n]*'
    links = ' · '.join(f'[{label.split(" — ")[0]}](registry/by-domain/{key}.md)'
                       for key, label in DOMAINS.items())
    text = re.sub(pattern, lambda m: m.group(1)+'\n\n'+links, text, count=1)
    report_link = '[Submission processing report](registry/INTAKE_REPORT.md)'
    if report_link not in text:
        text = text.replace('## Browse research areas', report_link+
                            '\n\n## Browse research areas', 1)
    path.write_text(text, encoding='utf-8')
