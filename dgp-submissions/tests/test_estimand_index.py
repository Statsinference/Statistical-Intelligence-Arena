"""Regression tests for traceable target naming and categorical indexes."""
from pathlib import Path
from tools.dgp_registry.target_index import load_labels, target_name, render_target_indexes

def _record(record_id):
    item = load_labels()[record_id]
    return {
        'record_id': record_id,
        'domain': item['domain'],
        'estimand': {'name': item['original_name'], 'definition': item['source_definition']},
        'paper': {'citation': 'Example (2024). Target example.'},
        'mechanism': {'name': 'Example mechanism'},
    }

def test_standard_names_are_bound_to_submitted_definitions():
    labels = load_labels()
    ding = _record('ate-ding-dasgupta-2016-binary-rct-v1')
    assert target_name(ding, labels) == 'ATE'
    ding['estimand']['definition'] += ' changed'
    assert target_name(ding, labels) == 'Needs review'

def test_iv_slope_not_misidentified_as_population_late():
    labels = load_labels()
    slope = _record('iv-wang-2021-binary-late-v1')
    assert target_name(slope, labels) == 'Conditional LATE curve transformed-slope parameter'
    assert target_name(slope, labels) != 'LATE'
    ratio = _record('iv-athey-tibshirani-wager-2019-compliance-v1')
    assert target_name(ratio, labels) == 'Pointwise conditional Wald ratio'

def test_cdf_is_not_relabelled_conditional_quantile():
    labels = load_labels()
    cdf = _record('qdi-henzi-2021-poisson-clipped-rate-v1')
    assert target_name(cdf, labels) == 'Conditional cumulative distribution function'

def test_known_label_and_review_status_are_distinct():
    labels = load_labels()
    cate = _record('cate-athey-2019-heterogeneity-confounding-v1')
    assert target_name(cate, labels) == 'CATE ⚠ review'
    inconsistent = _record('proximal-shi-2026-sc-gaussian-v1')
    assert target_name(inconsistent, labels) == 'Needs review'

def test_target_index_preserves_all_input_records(tmp_path):
    labels = load_labels()
    nie = _record('nie-eric-original-v1')
    other = _record('mediation-miles-2019-toxicity-path-specific-v1')
    unknown = _record('mediation-luo-et-al-2025-dynamic-markov-v1')
    unknown['estimand']['definition'] += ' changed'
    render_target_indexes([nie, other, unknown], tmp_path, labels)
    result = (tmp_path / 'by-target' / 'mediation.md').read_text(encoding='utf-8')
    assert '**3 DGP mechanism(s).**' in result
    assert 'Natural indirect effect (NIE)' in result and '| NIE |' in result
    assert 'Other mediation targets' in result and 'Path-specific effect' in result
    assert '## Needs review' in result and unknown['record_id'] in result
