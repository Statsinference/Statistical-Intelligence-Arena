"""Source-bound concise display definitions; no mathematical inference.

The raw and scenario-level name and definition must match an entry exactly.
Explicit scenario overrides take precedence; a changed source cannot silently
inherit a formula intended for another target. All values are display-only.
"""
import json
from pathlib import Path

OVERRIDES_PATH = Path(__file__).with_name('definition_overrides.json')
PENDING = 'Definition needs review; see the submitted definition below.'


def _safe_math(expression):
    return (isinstance(expression, str) and bool(expression.strip())
            and not any(ch in expression for ch in ('|', '`', '$', '<', '>', '\n', '\r')))


def load_definitions(path=OVERRIDES_PATH):
    doc = json.loads(Path(path).read_text(encoding='utf-8'))
    if doc.get('schema_version') != 1 or not isinstance(doc.get('records'), dict):
        raise ValueError('Unsupported concise definitions schema')
    return doc['records']


def concise_definition(record, scenario, definitions):
    """Return trusted inline GitHub math or a plain review message.

    Only hand-curated formulas bound to the exact source are used. An explicit
    scenario target does not fall back to a record-level entry when different.
    """
    item = definitions.get(record.get('record_id')) or {}
    if (item.get('domain') != record.get('domain')
            or 'source_zip_sha256' not in item
            or item['source_zip_sha256'] != (record.get('provenance') or {}).get('submitted_zip_sha256')):
        return PENDING
    source = scenario.get('estimand') or record.get('estimand') or {}
    target = (item.get('scenarios') or {}).get(str(scenario.get('id')))
    if target is None:
        target = item.get('default') or {}
    if (target.get('source_name') != source.get('name')
            or target.get('source_definition') != source.get('definition')):
        return PENDING
    expression = target.get('display_math')
    # GitHub supports $`...`$ for inline mathematical text in tables. Prevent
    # untrusted delimiters, literal table separators, and embedded HTML. Use
    # TeX commands such as \\mid, \\lt, and \\gt in curated expressions.
    if not _safe_math(expression):
        return PENDING
    return '$`' + expression.strip() + '`$'


def definition_note(record, scenario, definitions):
    """Return the verified entry's optional plain-text note, if any."""
    if concise_definition(record, scenario, definitions) == PENDING:
        return None
    item = definitions[record['record_id']]
    target = (item.get('scenarios') or {}).get(str(scenario.get('id')))
    if target is None:
        target = item.get('default') or {}
    note = target.get('display_note')
    note = note.strip() if isinstance(note, str) and note.strip() else ''
    math = target.get('display_note_math')
    if math is not None and not _safe_math(math):
        return ('Definition note formula requires review.', '')
    math = math.strip() if isinstance(math, str) else ''
    return (note, math) if note or math else None
