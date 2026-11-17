"""Check curated counterfactual notation without rewriting source records."""
import re

from tools.dgp_registry.concise_definitions import load_definitions


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
