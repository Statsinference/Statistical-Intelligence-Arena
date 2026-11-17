import io
import json
import zipfile
from pathlib import Path
import pytest
from tools.dgp_registry.github_intake import ingest
from tools.dgp_registry.domains import DOMAINS

def make_zip(p: Path, *, family='ate', rid='example-ate-1'):
    with zipfile.ZipFile(p,'w') as z:
        z.writestr('case/collection.json', json.dumps({
            'contribution_id':rid,'family':family,'title':'Minimal ATE DGP',
            'source':{'citation':'Sample Author 2024','locator':'Section 4'},
            'equations':['X ~ N(0,1)','A ~ Bernoulli(.5)','Y = 2*A + X + eps'],
            'estimand':{'definition':'ATE = E[Y(1)-Y(0)]'},
            'truth':{'reference_value':2.0,'method':'intervention contrast'},
            'sampling':'IID'
        }))
        z.writestr('case/config.json',json.dumps({'scenarios':{'original':{'n':500}}}))

def test_research_area_catalog_from_one_zip(tmp_path):
    d=tmp_path/'incoming';d.mkdir();make_zip(d/'submission.zip')
    result=ingest(d,tmp_path/'registry')
    assert result['mechanisms']==1 and result['scenarios']==1 and result['papers']==1
    text=(tmp_path/'registry/by-domain/ate.md').read_text()
    assert 'Minimal ATE' in text and 'ATE' in text
    assert 'Target (submitted name)' in text and 'Scenarios' in text
    assert '| 1 | Needs review |' in text
    detail=(tmp_path/'registry/drafts/example-ate-1.md').read_text(encoding='utf-8')
    assert '| original |' in detail and '| 2.0 |' in detail
    assert (tmp_path/'registry/drafts/example-ate-1.json').exists()
    assert 'Unverified' in (tmp_path/'registry/drafts/example-ate-1.md').read_text()
    assert len(list((tmp_path/'registry/by-domain').glob('*.md'))) == len(DOMAINS)

def test_unknown_family_is_not_guessed(tmp_path):
    d=tmp_path/'incoming';d.mkdir();make_zip(d/'submission.zip',family='strange')
    ingest(d,tmp_path/'registry')
    assert 'Needs classification' in (tmp_path/'registry/INDEX.md').read_text()
    assert (tmp_path/'registry/by-domain/unclassified.md').exists()

def test_duplicate_dgp_id_with_conflicting_science_is_quarantined(tmp_path):
    d=tmp_path/'incoming';d.mkdir();make_zip(d/'a.zip');make_zip(d/'b.zip',family='iv')
    result=ingest(d,tmp_path/'registry')
    assert result['mechanisms']==2
    assert (tmp_path/'registry/by-domain/ate.md').exists()
    assert (tmp_path/'registry/by-domain/iv.md').exists()
    assert 'CONFLICT' in (tmp_path/'registry/INDEX.md').read_text()

def test_identical_zip_skipped(tmp_path):
    d=tmp_path/'incoming';d.mkdir();make_zip(d/'a.zip');(d/'b.zip').write_bytes((d/'a.zip').read_bytes())
    result=ingest(d,tmp_path/'registry')
    assert result['mechanisms']==1

def test_unstructured_zip_is_reported_without_global_failure(tmp_path):
    d=tmp_path/'incoming';d.mkdir()
    with zipfile.ZipFile(d/'raw.zip','w') as z:z.writestr('random.txt','hi')
    result=ingest(d,tmp_path/'registry')
    assert result['mechanisms']==0 and result['failure_count']==1
    assert 'no structured collection.json' in (tmp_path/'registry/INTAKE_REPORT.md').read_text()
