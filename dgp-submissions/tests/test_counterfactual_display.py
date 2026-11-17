"""Check curated counterfactual notation without rewriting source records."""
import re

from tools.dgp_registry.concise_definitions import load_definitions
from tools.dgp_registry.counterfactual_display import render_counterfactual_equations, _replacements


def test_curated_counterfactual_display_and_noncausal_formulas():
    definitions = load_definitions()
    entries = [entry for record in definitions.values()
               for entry in [record.get('default') or {}, *record.get('scenarios', {}).values()]
               if entry]
    formulas = {entry.get('display_math', '') for entry in entries}
    notes = {entry.get('display_note_math', '') for entry in entries}
    assert r'\mathbb{E}[Y^{(1)}-Y^{(0)}]' in formulas
    assert r'\frac{1}{N}\sum_{i=1}^{N}\{Y_i^{(1)}-Y_i^{(0)}\}' in formulas
    assert r'\mathbb{E}\!\left[Y^{(1,M^{(1)})}-Y^{(1,M^{(0)})}\right]' in formulas
    assert r'\mathbb{E}[Y^{(1)}-Y^{(0)}\mid D^{(1)}\gt D^{(0)}]' in formulas
    assert r'\theta_{a_1a_2a_3}=\mathbb{E}[Y^{(a_3,M_1^{(a_1)},M_2^{(a_2,M_1^{(a_1)})})}]' in notes
    assert any(r'\lambda_{T^{(\bar a)}}(t)' in formula for formula in formulas)
    assert any(r'-Y(\alpha+X^\top\beta)' in formula for formula in formulas)
    assert not any(re.search(r'\b(?:Y|M|D|A|Z)(?:_\{[^}]+\}|_[A-Za-z0-9]+)?\((?:0|1)\)', f)
                   for f in formulas | notes)


def test_source_definition_and_provenance_are_preserved():
    definitions = load_definitions()
    record = definitions['ate-athey-imbens-wager-2018-arb-v1']
    assert record['source_zip_sha256'] == 'f29ff168545fa811ed66400f5a557feaea35e6e19a36e41377f7fd136fa34021'
    entry = record['scenarios']['delta_dense_dense']
    assert 'Population average treatment effect E[Y(1)-Y(0)]' in entry['source_definition']
    assert entry['display_math'] == r'\mathbb{E}[Y^{(1)}-Y^{(0)}]'


def test_equation_display_is_exact_and_source_bound():
    replacements = _replacements()
    keys = [key for key in replacements if key[0] == 'ate-athey-imbens-wager-2018-arb-v1'
            and r'Y_{i}(w)' in key[2]]
    assert len(keys) == 1
    record_id, digest, original = keys[0]
    record = {'record_id': record_id, 'provenance': {'submitted_zip_sha256': digest}}
    lines = ['```math', original, '```', '<details>', original, '</details>']
    result = render_counterfactual_equations(lines, record)
    assert result[1] == replacements[keys[0]]
    assert result[4] == original  # source inside details is untouched
    assert lines[1] == original  # input not mutated
    wrong_hash = {'record_id': record_id, 'provenance': {'submitted_zip_sha256': 'different'}}
    assert render_counterfactual_equations(lines, wrong_hash) == lines
    assert render_counterfactual_equations(['```math', original + ' ', '```'], record)[1] == original + ' '


def test_equation_overrides_preserve_functions_and_multiplication():
    replacements = _replacements()
    assert len(replacements) == 72
    assert len({key[0] for key in replacements}) == 39
    assert any('Y^{(1, M^{(0)})}' in value for value in replacements.values())
    assert not any(r'A(0.5+3X_1-5X_2' in key[2] for key in replacements)
    assert not any('Q_Y(0.9)' in key[2] for key in replacements)
