"""Render only independently reviewed, source-bound potential outcomes.

The scientific submission and verbatim original equations never change. Each
replacement matches a full rendered math block, a record ID and its ZIP hash.
"""
from functools import lru_cache
import json
from pathlib import Path


@lru_cache(maxsize=1)
def _replacements():
    path = Path(__file__).with_name('counterfactual_equation_overrides.json')
    doc = json.loads(path.read_text(encoding='utf-8'))
    if doc.get('schema_version') != 1:
        raise ValueError('Unsupported counterfactual display schema')
    indexed = {}
    for item in doc['replacements']:
        key = (item['record_id'], item['source_zip_sha256'], item['rendered_latex'])
        if key in indexed and indexed[key] != item['rewritten_latex']:
            raise ValueError('Conflicting counterfactual display overrides')
        indexed[key] = item['rewritten_latex']
    return indexed


def render_counterfactual_equations(lines, source_record):
    """Rewrite matching fenced math blocks; preserve all original-source text."""
    record_id = source_record.get('record_id')
    digest = (source_record.get('provenance') or {}).get('submitted_zip_sha256')
    if not record_id or not digest:
        return list(lines)
    result = list(lines)
    replacements = _replacements()
    for index in range(1, len(result) - 1):
        if result[index - 1] == '```math' and result[index + 1] == '```':
            result[index] = replacements.get((record_id, digest, result[index]), result[index])
    return result
