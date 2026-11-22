"""Verify source-reported domain tables and the deployed website; never run DGPs."""
from pathlib import Path
import json
import math
import os
import re
import time
import urllib.request
from playwright.sync_api import sync_playwright

out = Path('verification')
out.mkdir(exist_ok=True)
expected = json.loads(Path('data/results.json').read_text())
html = Path('index.html').read_text()
assert 'Core Contributors' not in html and 'id="contributors"' not in html
assert 'href="#contributors"' not in html
assert '<title>Statistical Inference Arena</title>' in html
inline = re.search(r'<script id="results-data" type="application/json">(.*?)</script>', html, re.S)
assert inline and json.loads(inline.group(1))['suites'] == [], 'Public JSON is the sole result source'
suites = {s['id']: s for s in expected['suites']}
assert len(suites) == 7
assert {s['domain'] for s in suites.values()} == {'ate','cate','mediation','iv','proximal','did_sc'}
keys = ['bias','variance','rmse','length','coverage','time_s']
# Independent transcription checks: tuples follow the printed column order.
checks = {
 'iv-v0.2': [
  ('ID','PFN',[.003,.072,.267,.901,.951,2.28]),
  ('ID','RF',[.034,.160,.401,1.060,.957,7.91]),
  ('ID','RF trim',[.023,.092,.304,.969,.957,7.62]),
  ('OOD','PFN',[.001,.029,.170,.666,.957,2.24]),
  ('OOD','RF',[-6.12,150000,382,240000,.602,8.27]),
  ('OOD','RF trim',[-.011,.084,.290,1.278,.993,7.65])],
 'ate-collected-dgp-report': [
  ('ID','CausalPFN',[.0091,.1069**2,.1211,.2861,.7683,.836]),
  ('ID','RF',[-.0133,.1351**2,.1446,.6852,.9866,130.278]),
  ('OOD','CausalPFN',[.0207,.0629**2,.0700,.1719,.7861,.878]),
  ('OOD','RF',[-.0275,.1080**2,.1197,.6746,.9860,144.089])],
 'cate-collected-dgp-report': [
  ('ID','CausalPFN',[.0086,.2401**2,.3216,6.4158,1,.168]),
  ('ID','RF',[-.0342,.4750**2,.6314,1.7332,.9068,55.783]),
  ('OOD','CausalPFN',[.0322,.1261**2,.1940,3.9290,1,.215]),
  ('OOD','RF',[.0420,.3244**2,.3474,.9778,.8944,69.712])],
 'did-experiment3-2026-11-13': [
  ('ID','DirectATT S1',[-.0144,.0289,.1706,.7658,.971,.0475]),
  ('ID','DirectATT S2',[-.0224,.0646,.2550,1.0211,.927,.0471]),
  ('ID','PS/OR-DR S1',[-.0008,.0177,.1332,.4640,.953,.1397]),
  ('ID','PS/OR-DR S2',[-.0007,.0177,.1330,.4623,.955,.1390]),
  ('ID','RF-DR-DiD',[-.0335,.0907,.3028,.8708,.949,1.0596]),
  ('OOD','DirectATT S1',[-.0339,.0821,.2884,.5289,.749,.0478]),
  ('OOD','DirectATT S2',[-.0163,.1012,.3184,.5749,.751,.0478]),
  ('OOD','PS/OR-DR S1',[-.0067,.0295,.1718,.5332,.940,.1397]),
  ('OOD','PS/OR-DR S2',[-.0057,.0294,.1715,.5315,.938,.1398]),
  ('OOD','RF-DR-DiD',[.0025,.0385,.1962,.6255,.935,1.3292])]
}
for sid, entries in checks.items():
    actual = {(r['group'],r['method']): r for r in suites[sid]['rows']}
    assert len(actual) == len(entries)
    for group,method,values in entries:
        for key,value in zip(keys,values):
            assert math.isclose(actual[(group,method)][key],value,rel_tol=1e-12,abs_tol=1e-12),(sid,group,method,key)
for suite in suites.values():
    for r in suite['rows']:
        if r.get('variance_is_approximate'):
            assert math.isclose(r['variance'],r['reported_se']**2,abs_tol=1e-12)
        if r.get('status') == 'not_reported':
            assert all(r[k] is None for k in keys)
prox = suites['proximal-v3-normalized']
assert prox['metric_scale'] == 'per_table_y_sd'
for r in prox['rows']:
    if r['group'] == 'OOD':
        assert r['variance'] is None and r['time_s'] is None
assert len(prox['dgp_results']) == 26
assert len(suites['proximal-v3-original']['dgp_results']) == 6
med = suites['mediation-nie1-meeting-2026-11-12']
assert 'dgp_results' not in med
assert med['timing_comparisons'][0]['scope'] == 'previous_model_and_test_set'
assert sum(len(s['rows']) for s in suites.values()) == 36

base = 'https://statsinference.github.io/'
for attempt in range(36):
    token = f"{os.environ.get('GITHUB_SHA','')}-{attempt}"
    try:
        req = urllib.request.Request(base+'?verify='+token,headers={'Cache-Control':'no-cache'})
        live_html = urllib.request.urlopen(req,timeout=15).read().decode()
        req = urllib.request.Request(base+'data/results.json?verify='+token,headers={'Cache-Control':'no-cache'})
        live_data = json.load(urllib.request.urlopen(req,timeout=15))
        if 'id="contributors"' not in live_html and live_data == expected:
            break
    except Exception:
        pass
    time.sleep(5)
else:
    raise AssertionError('New HTML and result JSON did not become publicly available')

with sync_playwright() as pw:
    browser = pw.chromium.launch()
    page = browser.new_page(viewport={'width':1440,'height':1100})
    errors=[]
    page.on('pageerror',lambda e:errors.append(str(e)))
    response=page.goto(base+'?verify='+token,wait_until='domcontentloaded',timeout=60000)
    assert response.status == 200
    page.wait_for_function('DATA.suites.length===7',timeout=30000)
    assert page.title() == 'Statistical Inference Arena'
    assert page.locator('#contributors').count() == 0
    assert page.locator('#tabs [data-t]').count() == 10
    for domain,count in {'mediation':4,'ate':4,'cate':4,'iv':6,'proximal':4,'did_sc':10}.items():
        page.locator(f'[data-t="{domain}"]').click()
        assert page.locator('#tbody tr').count() == count
        if domain == 'iv':
            table=page.locator('#tbody').inner_text()
            for token_text in ['1.5×10⁵','2.4×10⁵','382','95.1%','99.3%']:
                assert token_text in table
            page.locator('#table').screenshot(path=str(out/'iv-table.png'))
        if domain == 'proximal':
            assert 'Norm. Bias' in page.locator('#thead').inner_text()
            page.locator('#table').screenshot(path=str(out/'proximal-table.png'))
            page.locator('#suite-select').select_option('proximal-v3-original')
            assert 'Norm.' not in page.locator('#thead').inner_text()
            assert '29.272' in page.locator('#tbody').inner_text()
        if domain == 'did_sc':
            assert '0.0475' in page.locator('#tbody').inner_text()
        page.locator('[data-split="OOD"]').click()
        assert page.locator('#tbody tr').count() == count//2
        page.locator('[data-split="both"]').click()
        page.locator('[data-sort="bias"]').click()
    page.locator('[data-t="ate"]').click()
    page.locator('[data-fam="classical"]').click()
    assert page.locator('#tbody tr').count() == 2
    page.locator('[data-fam="all"]').click()
    page.locator('#q').fill('CausalPFN')
    assert page.locator('#tbody tr').count() == 2
    page.locator('#q').fill('')
    with page.expect_download() as info:
        page.locator('#export-btn').click()
    csv=Path(info.value.path()).read_text()
    assert 'metric_scale' in csv and 'variance_definition' in csv
    for domain in ['nonparametric_regression','quantile','semi_supervised','missing_data']:
        page.locator(f'[data-t="{domain}"]').click()
        assert 'Results not yet published' in page.locator('#tbody').inner_text()
    page.locator('[data-t="iv"]').click()
    page.screenshot(path=str(out/'desktop.png'))
    page.set_viewport_size({'width':390,'height':844})
    page.locator('#menu-btn').click()
    page.locator('[data-t="ate"]').click()
    assert page.locator('#hero-title').inner_text() == 'ATE'
    assert page.evaluate('document.documentElement.scrollWidth<=innerWidth+1')
    page.screenshot(path=str(out/'mobile.png'),full_page=True)
    assert not errors,errors
    report={'status':'passed','url':base,'commit':os.environ.get('GITHUB_SHA'),'domains_with_results':6,'suites':7,'main_rows':36,'contributors_visible':False,'javascript_errors':errors}
    (out/'report.json').write_text(json.dumps(report,indent=2))
    print(json.dumps(report,indent=2))
    browser.close()
