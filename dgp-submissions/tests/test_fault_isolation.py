"""One broken upload never suppresses unrelated DGPs or deletes last valid data."""
import json
import zipfile
from pathlib import Path
from unittest.mock import patch

from tools.dgp_registry.github_intake import ingest
from tools.dgp_registry.domains import DOMAINS, to_domain
from tools.dgp_registry.zip_reader import read_archive
from tools.dgp_registry.intake_safety import read_zip_report, refresh_navigation


def add_case(z, folder, rid, family='ate', *, valid=True, properties=None):
    z.writestr(folder+'/collection.json', json.dumps({
        'contribution_id':rid, 'family':family, 'title':'Synthetic parser test',
        'source':{'citation':'Test Author (2020). Test Paper. Test Journal.'},
        'equations':['X~N(0,I_p)', 'Y=f(X)+epsilon'],
        'estimand':{'definition':'m(x)=E[Y|X=x]'},
        'properties':properties or {}, 'sampling':'IID units',
    }))
    if valid:
        z.writestr(folder+'/config.json',json.dumps({'scenarios':{'fixed':{'p':1000,'n':50,'s':5}}}))
    z.writestr(folder+'/generator.py', 'raise RuntimeError("NEVER EXECUTE THIS SOURCE")\n')


def case(path, rid, family='ate', *, valid=True, properties=None):
    with zipfile.ZipFile(path,'w') as z:
        add_case(z,'case',rid,family,valid=valid,properties=properties)


def test_broken_early_zip_does_not_block_later_upload(tmp_path):
    inc=tmp_path/'incoming';inc.mkdir()
    (inc/'00-broken.zip').write_bytes(b'not a ZIP')
    case(inc/'99-good.zip','later-valid-1')
    out=tmp_path/'registry'
    r=ingest(inc,out)
    assert r['mechanisms']==1 and r['failure_count']==1
    assert (out/'drafts/later-valid-1.json').is_file()
    report=json.loads((out/'INTAKE_REPORT.json').read_text())
    assert report['status']=='partial_success_needs_attention'
    assert report['failures'][0]['source'].endswith('00-broken.zip')
    assert 'INTAKE_REPORT.md' in (out/'INDEX.md').read_text()


def test_one_invalid_dgp_does_not_block_siblings_in_same_zip(tmp_path):
    inc=tmp_path/'incoming';inc.mkdir()
    with zipfile.ZipFile(inc/'mixed.zip','w') as z:
        add_case(z,'bad','broken-case-1',valid=False)
        add_case(z,'good','working-case-1')
    out=tmp_path/'registry'
    r=ingest(inc,out)
    assert r['mechanisms']==1 and r['failure_count']==1
    assert (out/'drafts/working-case-1.json').exists()
    assert not (out/'drafts/broken-case-1.json').exists()
    import pytest
    with pytest.raises(ValueError):
        read_archive(inc/'mixed.zip')


def test_input_repair_clears_report_without_reuploading_other_zips(tmp_path):
    inc=tmp_path/'incoming';inc.mkdir();out=tmp_path/'registry'
    case(inc/'first.zip','first-case-1',valid=False)
    case(inc/'second.zip','second-case-1')
    assert ingest(inc,out)['failure_count']==1
    case(inc/'first.zip','first-case-1')
    r=ingest(inc,out)
    assert r['mechanisms']==2 and r['failure_count']==0


def test_last_valid_entry_and_generator_are_retained_and_marked(tmp_path):
    inc=tmp_path/'incoming';inc.mkdir();out=tmp_path/'registry'
    case(inc/'first.zip','first-case-1')
    ingest(inc,out)
    old_code=(out/'generators/first-case-1.py').read_bytes()
    (inc/'first.zip').write_bytes(b'broken replacement')
    case(inc/'next.zip','new-case-1')
    r=ingest(inc,out)
    assert r['mechanisms']==2 and r['stale_count']==1
    old=json.loads((out/'drafts/first-case-1.json').read_text())
    assert old['review_status']=='stale_last_valid_needs_review'
    assert (out/'generators/first-case-1.py').read_bytes()==old_code
    assert (out/'drafts/new-case-1.json').exists()


def test_unsafe_archive_stays_rejected_entirely(tmp_path):
    inc=tmp_path/'incoming';inc.mkdir()
    with zipfile.ZipFile(inc/'unsafe.zip','w') as z:
        z.writestr('../outside.py','bad')
        add_case(z,'safe-looking','not-accepted-1')
    case(inc/'safe.zip','accepted-1')
    r=ingest(inc,tmp_path/'registry')
    assert r['mechanisms']==1 and r['failure_count']==1
    assert not (tmp_path/'outside.py').exists()


def test_all_four_new_domains_accept_high_dimensional_metadata(tmp_path):
    inc=tmp_path/'incoming';inc.mkdir()
    for i,family in enumerate(['nri','qdi','ssi','missing_data']):
        case(inc/(family+'.zip'),'new-domain-'+str(i),family,
             properties={'high_dimensional':True,'dimension':1000,'effective_dimension':5})
    out=tmp_path/'registry'
    r=ingest(inc,out)
    assert r['mechanisms']==4 and r['failure_count']==0
    for domain in ['nonparametric_regression','quantile','semi_supervised','missing_data']:
        assert (out/'by-domain'/(domain+'.md')).exists()
    for p in (out/'drafts').glob('*.json'):
        assert json.loads(p.read_text())['mechanism']['properties']['high_dimensional'] is True


def test_interference_flag_is_not_an_intake_ban(tmp_path):
    inc=tmp_path/'incoming';inc.mkdir()
    case(inc/'network.zip','network-case-1','ate',properties={'interference':True})
    r=ingest(inc,tmp_path/'registry')
    assert r['mechanisms']==1 and r['failure_count']==0


def test_unknown_family_is_not_guessed_and_all_areas_render(tmp_path):
    inc=tmp_path/'incoming';inc.mkdir()
    case(inc/'unknown.zip','unknown-case-1','novel-unclassified')
    ingest(inc,tmp_path/'registry')
    assert (tmp_path/'registry/by-domain/unclassified.md').exists()
    assert len(DOMAINS)==10
    assert to_domain('quantile_regression')=='quantile'
    assert to_domain('nonparametric regression')=='nonparametric_regression'
    assert to_domain('totally-unknown') is None


def test_bad_display_metadata_is_quarantined(tmp_path):
    inc=tmp_path/'incoming';inc.mkdir();out=tmp_path/'registry'
    with zipfile.ZipFile(inc/'bad.zip','w') as z:
        z.writestr('collection.json',json.dumps({
            'contribution_id':'bad-display-1','family':'ate','title':'Title',
            'source':{'citation':'Test paper'},'equations':['X~N(0,1)'],
            'estimand':{'definition':'E[X]'},
            'english_display':{'equations':[{'latex':'X=1'},{'latex':'X=2'}]},
        }))
        z.writestr('config.json','{"scenarios":{"test":{}}}')
    case(inc/'good.zip','good-display-1')
    r=ingest(inc,out)
    assert r['mechanisms']==1 and r['failure_count']==1


def test_program_failure_preserves_published_registry(tmp_path):
    inc=tmp_path/'incoming';inc.mkdir();out=tmp_path/'registry'
    case(inc/'good.zip','valid-case-1');ingest(inc,out)
    before={p.relative_to(out).as_posix():p.read_bytes() for p in out.rglob('*') if p.is_file()}
    import pytest
    with patch('tools.dgp_registry.github_intake.build',side_effect=RuntimeError('internal error')):
        with pytest.raises(RuntimeError):ingest(inc,out)
    after={p.relative_to(out).as_posix():p.read_bytes() for p in out.rglob('*') if p.is_file()}
    assert before==after


def test_navigation_updates_only_marked_section(tmp_path):
    p=tmp_path/'README.md'
    p.write_text('# Unchanged\n\n## Browse the six research areas\n\n[ATE](registry/by-domain/ate.md)\n\n## Tail\nunchanged\n')
    refresh_navigation(p)
    once=p.read_text();refresh_navigation(p)
    assert once==p.read_text()
    assert 'semi_supervised.md' in once and 'missing_data.md' in once
    assert 'six research' not in once
    assert once.endswith('## Tail\nunchanged\n')
