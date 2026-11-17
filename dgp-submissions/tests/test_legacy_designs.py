import json
import zipfile
from pathlib import Path

from tools.dgp_registry.catalog import build
from tools.dgp_registry.github_intake import ingest
from tools.dgp_registry.legacy_designs import LEGACY_DESIGNS, legacy_design
from tools.dgp_registry.target_index import load_labels, target_name
from tools.dgp_registry.concise_definitions import load_definitions, concise_definition


def test_classifications_require_exact_record_and_zip_digest():
    assert len(LEGACY_DESIGNS) == 11
    assert sum(item[1] == 'did' for item in LEGACY_DESIGNS.values()) == 6
    assert sum(item[1] == 'synthetic_control' for item in LEGACY_DESIGNS.values()) == 5
    for rid, (digest, domain, note) in LEGACY_DESIGNS.items():
        assert legacy_design(rid, digest) == (domain, note)
        assert legacy_design(rid, '0' * 64) is None
        assert legacy_design(rid + '-unknown', digest) is None
        assert legacy_design(rid, None) is None


def test_catalog_hides_legacy_bucket_and_keeps_old_links(tmp_path):
    records = [{'record_id':'new-did-sc', 'domain':'did_sc',
                'paper':{'citation':'Example.'}, 'mechanism':{'name':'Example'},
                'estimand':{'name':'tau', 'definition':'Unknown'}, 'scenarios':[]}]
    build(records, tmp_path)
    index = (tmp_path/'INDEX.md').read_text(encoding='utf8')
    assert 'Legacy DiD / Synthetic Control' not in index
    assert '[DiD' in index and '[Synthetic Control' in index
    assert '[Difference-in-Differences](did.md)' in (tmp_path/'by-domain/did_sc.md').read_text(encoding='utf8')
    assert '[Synthetic Control](synthetic_control.md)' in (tmp_path/'by-domain/did_sc.md').read_text(encoding='utf8')
    assert 'new-did-sc' in (tmp_path/'by-domain/unclassified.md').read_text(encoding='utf8')
    assert '[DiD targets](did.md)' in (tmp_path/'by-target/did_sc.md').read_text(encoding='utf8')


def test_real_legacy_submissions_preserve_targets_and_digest(tmp_path):
    # Actual records are read from the submitted ZIPs; no generator execution.
    incoming = Path('incoming')
    if not incoming.is_dir():
        return
    out = tmp_path/'registry'
    result = ingest(incoming, out)
    catalog = json.loads((out/'catalog.json').read_text(encoding='utf8'))
    available = {r['record_id']: r for r in catalog['records']}
    labels, definitions = load_labels(), load_definitions()
    checked = 0
    for rid, (digest, domain, _) in LEGACY_DESIGNS.items():
        if rid not in available:
            continue
        rec = json.loads((out/'drafts'/f'{rid}.json').read_text(encoding='utf8'))
        assert rec['domain'] == domain
        assert rec['provenance']['submitted_zip_sha256'] == digest
        assert rec['source_suggested_domain'] == 'did_sc'
        assert rec['review_status'] == 'needs_scientific_review'
        assert target_name(rec, labels) != 'Needs review'
        if definitions[rid].get('scenarios'):
            assert any(concise_definition(rec, scenario, definitions) != 'Definition needs review; see the submitted definition below.'
                       for scenario in rec.get('scenarios', [])), rid
        checked += 1
    # The frozen regression corpus predates most of the eleven submissions.
    # Validate every one present, without requiring newer ZIPs in that corpus.
    assert checked >= 1
    assert result['mechanisms'] >= checked


def test_changed_archive_is_not_guessed_from_old_classification(tmp_path):
    source = Path('incoming/did-cwz-2021-donor-ar-null-v1.zip')
    if not source.exists():
        return
    incoming = tmp_path/'incoming'
    incoming.mkdir()
    changed = incoming/source.name
    changed.write_bytes(source.read_bytes())
    with zipfile.ZipFile(changed, 'a') as z:
        z.writestr('source-changed.txt', 'This makes the source digest differ.')
    out = tmp_path/'registry'
    ingest(incoming, out)
    rec = json.loads((out/'drafts/did-cwz-2021-donor-ar-null-v1.json').read_text(encoding='utf8'))
    assert rec['domain'] == 'unclassified'
    assert rec['source_suggested_domain'] == 'did_sc'
    assert rec['classification_status'] == 'needs_manual_classification'
    assert 'does not match a source-bound classification' in ' '.join(rec['warnings'])
    assert 'did-cwz-2021-donor-ar-null-v1' in (out/'by-domain/unclassified.md').read_text(encoding='utf8')
