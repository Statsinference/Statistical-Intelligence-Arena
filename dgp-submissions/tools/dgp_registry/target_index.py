"""Provisional, source-bound estimand names and target indexes.

Matching is exact on domain, submitted name, and complete submitted definition:
if any input changed, classification falls back to Needs review. The curated
labels describe the submitted definitions and do not independently validate
the paper, the generator, the estimand, or its numerical truth.
"""
from __future__ import annotations
import json
from collections import defaultdict
from pathlib import Path

LABELS_PATH = Path(__file__).with_name('estimand_labels.json')
TARGET_GROUPS = {
    'mediation': {
        'natural_indirect_effect': 'Natural indirect effect (NIE)',
        'natural_direct_effect': 'Natural direct effect (NDE)',
        'interventional_indirect_effect': 'Interventional indirect effect',
        'dynamic_mediation_effect': 'Dynamic mediation effect',
        'other': 'Other mediation targets',
    },
    'iv': {'population_late': 'Population local average treatment effect (LATE)',
           'other': 'Other IV targets'},
    'proximal': {'ate': 'Average treatment effect (ATE)',
                 'cate': 'Conditional average treatment effect (CATE)',
                 'other': 'Other proximal targets'},
    'did': {'att': 'Average treatment effect on the treated (ATT)',
            'other': 'Other DiD targets'},
    'did_sc': {'att': 'Average treatment effect on the treated (ATT)',
               'other': 'Other mixed-category targets'},
    'quantile': {'conditional_quantile': 'Conditional quantile',
                 'other': 'Other quantile or distribution targets'},
}

def load_labels(path=LABELS_PATH):
    return json.loads(Path(path).read_text(encoding='utf-8')).get('records', {})

def classification(record, labels):
    """Return a matching curated entry, or None if stale or unnamed."""
    item = labels.get(record.get('record_id')) or {}
    estimand = record.get('estimand') or {}
    if (item.get('status') not in ('provisional_submitted_definition_only', 'needs_review')
            or item.get('domain') != record.get('domain')
            or item.get('original_name') != estimand.get('name')
            or item.get('source_definition') != estimand.get('definition')
            or not item.get('standard_name')):
        return None
    return item

def target_name(record, labels):
    item = classification(record, labels)
    return (item['standard_name'] + (' ⚠ review' if item.get('status') == 'needs_review' else '')) if item else 'Needs review'

def _cell(value):
    return str(value or '—').replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('|', r'\|').replace('\n', ' ')

def render_target_indexes(records, output_root, labels):
    """Write browsable target indexes without mutating any input record."""
    from .paper_list import paper_title_with_venue
    from .title_display import display_title

    out = Path(output_root) / 'by-target'
    out.mkdir(parents=True, exist_ok=True)
    for domain, choices in TARGET_GROUPS.items():
        groups = defaultdict(list)
        selected = [rec for rec in records if rec.get('domain') == domain]
        for rec in selected:
            item = classification(rec, labels)
            key = item.get('target_type') if item else 'unclassified'
            if key not in choices:
                key = 'unclassified'
            groups[key].append((rec, item))
        lines = [
            f'# {domain.upper()}: target categories', '',
            '> Labels are based on submitted estimand definitions and require scientific review.',
            '> Original definitions, formulas, and values remain in each record.', '',
            f'**{len(selected)} DGP mechanism(s).**', '',
        ]
        for key, label in [*choices.items(), ('unclassified', 'Needs review')]:
            group = groups.get(key, [])
            lines += [f'## {label}', '', f'**{len(group)} DGP mechanism(s).**', '']
            if not group:
                lines += ['No records currently assigned.', '']
                continue
            lines += ['| Paper | DGP mechanism | Standardized target | Original submitted name |',
                      '|---|---|---|---|']
            for rec, item in sorted(group, key=lambda pair: pair[0]['record_id']):
                rid = rec['record_id']
                raw = (rec.get('estimand') or {}).get('name')
                target = target_name(rec, labels)
                lines.append(f'| {_cell(paper_title_with_venue(rec))} | '
                             f'[{_cell(display_title(rec))}](../drafts/{rid}.md) | '
                             f'{_cell(target)} | {_cell(raw)} |')
            lines.append('')
        (out / f'{domain}.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')
