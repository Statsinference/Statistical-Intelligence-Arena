"""Publication aliases and auditable DGP tags, not guesses from paper/domain names."""
import copy
import json
import re
from pathlib import Path

import pytest

from tools.dgp_registry.github_intake import ingest
from tools.dgp_registry.listing_metadata import venue_abbreviation, keyword_entries, keywords
from tools.dgp_registry.paper_list import paper_title, paper_list_tables


def record(props=None, name='A new mechanism', venue=None, domain='ate', notes=None):
    p=dict(props or {})
    if notes is not None:
        p['notes']=notes
    return {'record_id':'generic-example', 'domain':domain,
            'paper':{'citation':'Author (2026). An unrelated paper title. Venue.',
                     'title':'An unrelated paper title', 'venue':venue},
            'mechanism':{'name':name, 'properties':p}}


@pytest.mark.parametrize('source,wanted',[
    ('Journal of the American Statistical Association','JASA'),
    ('JASA','JASA'),
    ('Journal of the Royal Statistical Society Series B: Statistical Methodology','JRSSB'),
    ('JRSS-B','JRSSB'),
    ('The Annals of Statistics','AoS'),
    ('Biometrika','Biometrika'),
    ('Journal of Econometrics','JoE'),
    ('ICML (PMLR)','ICML'),
    ('NeurIPS','NeurIPS'),
])
def test_venue_aliases_use_submitted_venue(source,wanted):
    assert venue_abbreviation(record(venue=source))==wanted


def test_venue_unknown_is_not_promoted_to_known_journal():
    r=record(venue='Unlisted research workshop')
    assert venue_abbreviation(r)=='Unlisted research workshop'
    r['paper']['venue']=None
    assert venue_abbreviation(r)==''


def test_flags_are_source_properties_not_title_or_domain_inference():
    r=record({'dimension':10000}, name='CATE hypothetical nonlinear high-dimensional network',domain='cate')
    assert keywords(r)==[]
    r['mechanism']['properties'].update(interactions=True,nonlinear=True,high_dimensional=True,
                                       interference=True,effect_heterogeneity=True)
    assert keywords(r)==['Interactions','Nonlinearity','High-dimensionality','Interference','Effect heterogeneity']
    for entry in keyword_entries(r):
        assert entry['source'].startswith('mechanism.properties.')
        assert entry['method']=='explicit_boolean'


def test_no_interference_and_latent_confounding_are_never_interference():
    r=record({'nonlinear':True},notes='No interference; latent confounder U shared within an individual.')
    r['mechanism']['assumptions']=['There is no interference.']
    r['mechanism']['latent_variables']=[{'name':'U'}]
    assert 'Interference' not in keywords(r)
    assert 'Effect heterogeneity' not in keywords(r)


def test_false_flags_veto_conflicting_keywords_and_prose():
    r=record({'interference':False,'effect_heterogeneity':False,'high_dimensional':False,
              'keywords':['interference','heterogeneity','high-dimensionality']},
             name='Heterogeneous treatment effects')
    assert keywords(r)==[]


def test_boolean_strings_are_not_truthy():
    r=record({'nonlinear':'false','interactions':'true','high_dimensional':1})
    assert keywords(r)==[]


def test_effect_heterogeneity_requires_an_explicit_source_description():
    r=record({'interactions':True}, notes='Only X1 and X2 modify treatment effect.')
    assert keywords(r)==['Interactions','Effect heterogeneity']
    evidence=keyword_entries(r)[1]
    assert evidence['value']=='Only X1 and X2 modify treatment effect'
    assert evidence['source']=='mechanism.properties.notes'
    r['mechanism']['properties']['notes']='No effect heterogeneity; constant treatment effect.'
    assert keywords(r)==['Interactions']
    r['mechanism']['properties']['notes']='处理与基线交互构成效应异质性。'
    assert 'Effect heterogeneity' in keywords(r)


def test_heteroskedasticity_is_not_effect_heterogeneity():
    r=record(notes='The scale model has heteroskedasticity.')
    assert keywords(r)==['Heteroskedasticity']


def test_metadata_never_changes_the_scientific_record():
    r=record({'nonlinear':True,'high_dimensional':False},venue='JASA')
    before=copy.deepcopy(r)
    venue_abbreviation(r);keyword_entries(r);keywords(r)
    assert r==before


def test_explicit_custom_keywords_and_unknown_data():
    r=record({'keywords':['Invalid instruments','interactions','<script>','no interference']})
    assert keywords(r)==['Interactions','Invalid instruments']
    assert keywords(record())==[]


def test_panel_data_is_not_interference():
    r=record({'nonlinear':False})
    r['mechanism']['sampling']={'unit':'one panel experiment; a row is a time point'}
    assert keywords(r)==['Panel data']



def test_linearity_requires_explicit_evidence():
    assert 'Linearity' not in keywords(record({'nonlinear': False}))
    assert 'Linearity' not in keywords(record({'linear': False}))
    assert 'Linearity' not in keywords(record({}))
    assert keywords(record({'linear': True})) == ['Linearity']
    assert keywords(record({'keywords': ['linear']})) == ['Linearity']
    assert keywords(record({'keywords': ['linearity']})) == ['Linearity']
    assert 'Linearity' not in keywords(record({'linear': True, 'nonlinear': True}))
    assert 'Linearity' not in keywords(record({'linear': False, 'keywords': ['linear']}))


def test_title_only_plus_venue_and_keywords_remain_separate():
    a=record({'interactions':True,'nonlinear':True},name='Alpha',venue='JASA')
    b=record({'linear':True},name='Beta',venue='JASA')
    a['record_id']='alpha';b['record_id']='beta'
    assert paper_title(a)=='An unrelated paper title'
    page='\n'.join(paper_list_tables([a,b]))
    assert 'An unrelated paper title (JASA)' in page
    assert '| DGP Mechanisms | Estimand | Keywords |' in page
    assert '1: Interactions · Nonlinearity<br/>2: Linearity' in page
    assert '1: [Alpha]' in page and '2: [Beta]' in page
    assert page.count('An unrelated paper title')==1


def test_full_collection_keywords_and_flat_summary_agree(tmp_path):
    original={p.stem:json.loads(p.read_text(encoding='utf-8'))
              for p in Path('registry/drafts').glob('*.json')}
    out=tmp_path/'registry'
    result=ingest(Path('incoming'),out)
    data=json.loads((out/'catalog.json').read_text(encoding='utf-8'))
    assert result['mechanisms']>=23
    for summary in data['records']:
        r=json.loads((out/'drafts'/(summary['record_id']+'.json')).read_text(encoding='utf-8'))
        assert summary['keywords']==keywords(r)==keywords(summary)
        assert summary['venue_abbreviation']==venue_abbreviation(r)==venue_abbreviation(summary)
        for entry in summary['keyword_evidence']:
            assert entry['source'].startswith('mechanism.')
        # Verify declarations, never require every future DGP to be low-dimensional
        # or have no interference. Collection supports both positive properties.
        props=r['mechanism'].get('properties') or {}
        for key,label in [('high_dimensional','High-dimensionality'),('interference','Interference')]:
            if props.get(key) is True:
                assert label in keywords(r)
            elif props.get(key) is False:
                assert label not in keywords(r)
        if r['record_id'] in original:
            for field in ('paper','mechanism','scenarios','estimand'):
                assert r[field]==original[r['record_id']][field]
    page=(out/'by-domain/proximal.md').read_text(encoding='utf-8')
    assert ' (JRSSB)' in page and ' (JASA)' in page
    assert '| DGP mechanism | Keywords |' in page
    assert '| Generator.py |' not in page
    flat='\n'.join(paper_list_tables(data['records']))
    assert ' (AoS)' in flat and ' (JASA)' in flat
    assert '| Keywords |' in flat
