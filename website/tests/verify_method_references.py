"""Check method-specific references without changing or executing evaluations."""
import hashlib
import json
import os
import re
import base64
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'verification'
OUT.mkdir(exist_ok=True)
expected = json.loads((ROOT / 'data/results.json').read_text())
base = os.environ.get('ARENA_TEST_URL', '')
def load_page(page):
    if base:
        page.goto(base + '#domain=ate', wait_until='networkidle')
    else:
        # In-memory browser rendering: no network or local-server access required.
        html = (ROOT / 'index.html').read_text()
        html = re.sub(r'<script id="results-data" type="application/json">.*?</script>',
                      lambda m: '<script id="results-data" type="application/json">' + json.dumps(expected) + '</script>', html, flags=re.S)
        html = re.sub(r'<link rel="stylesheet" href="(assets/[^"?]+)(?:[^"]*)">',
                      lambda m: '<style>' + (ROOT / m.group(1)).read_text() + '</style>', html)
        html = re.sub(r'<script src="(assets/[^"?]+)(?:[^"]*)"></script>',
                      lambda m: '<script>' + (ROOT / m.group(1)).read_text() + '</script>', html)
        logo = base64.b64encode((ROOT / 'assets/statsarena-logo.webp').read_bytes()).decode()
        html = html.replace('assets/statsarena-logo.webp', 'data:image/webp;base64,' + logo)
        page.set_content(html, wait_until='load')
    page.wait_for_function('DATA.suites.length === 7')
    page.evaluate("chooseTask('ate')")
errors = []
checks = []
with sync_playwright() as p:
    executable = os.environ.get('CHROMIUM_EXECUTABLE')
    browser = p.chromium.launch(**({'executable_path': executable} if executable else {}))
    page = browser.new_page(viewport={'width': 1440, 'height': 1000})
    page.route('https://fonts.googleapis.com/**', lambda route: route.abort())
    page.route('https://fonts.gstatic.com/**', lambda route: route.abort())
    page.on('pageerror', lambda error: errors.append(str(error)))
    load_page(page)
    assert json.loads(page.evaluate('JSON.stringify(DATA)')) == expected
    for domain in ['ate','cate','proximal']:
        page.locator(f'[data-t="{domain}"]').click()
        expected_url = ('https://arxiv.org/abs/2610.08078v2' if domain == 'proximal' else 'https://proceedings.neurips.cc/paper_files/paper/2025/hash/e3d3db07c1bfb63e1d0b998996de1d12-Abstract-Conference.html')
        assert page.locator('#tbody a.method-ref-label').count() == 2
        assert all(u == expected_url for u in page.locator('#tbody a.method-ref-label').evaluate_all('(els)=>els.map(e=>e.href)'))
        assert page.locator('#tbody a.method-ref-name').count() == 2
        page.locator('#method-references').evaluate('(el)=>el.open=true')
        assert page.locator('#method-references .reference-title').get_attribute('href') == expected_url
        assert page.locator('#method-references .reference-entry').count() == 1
        if domain in ['ate','cate']:
            assert page.locator('#method-references .reference-secondary').get_attribute('href') == 'https://huggingface.co/vdblm/causalpfn'
        page.locator('[data-sort="rmse"]').click()
        assert page.locator('#tbody a.method-ref-label').count() == 2
        page.locator('[data-fam="classical"]').click()
        assert page.locator('#tbody .method-ref-label').count() == 0
        assert page.locator('#method-references').is_hidden()
        page.locator('[data-fam="all"]').click()
        page.locator('#q').fill('causalpfn' if domain != 'proximal' else 'proximalfm')
        assert page.locator('#tbody a.method-ref-label').count() == 2
        page.locator('#q').fill('')
        page.locator('#method-references').evaluate('(el)=>el.open=true')
        page.locator('#table').screenshot(path=str(OUT / f'{domain}-references.png'))
        checks.append(domain + ': paper links, unique citation, sorting, filters')
    for domain in ['mediation','iv','did_sc']:
        page.locator(f'[data-t="{domain}"]').click()
        assert page.locator('#tbody a.method-ref-label').count() == 0
        assert page.locator('#tbody .reference-pending').count() > 0
        assert page.locator('#method-references a').count() == 0
        checks.append(domain + ': no invented reference')
    for domain in ['nonparametric_regression','quantile','semi_supervised','missing_data']:
        page.locator(f'[data-t="{domain}"]').click()
        assert page.locator('#method-references').is_hidden()
    fallback = page.evaluate('''() => {
      const api=window.ArenaMethodReferences;
      const hf={url:'https://huggingface.co/vdblm/causalpfn',title:'Test fixture'};
      const paper={url:'https://arxiv.org/abs/2506.07918',title:'Test fixture'};
      return [api.primary({huggingface:hf}).kind,
              api.primary({paper,huggingface:hf}).kind,
              api.primary({paper:{url:'javascript:alert(1)'}}),
              api.primary({huggingface:{url:'https://example.com/model'}}),
              api.lookup('iv',{method:'CausalPFN',family:'pfn'})];
    }''')
    assert fallback == ['huggingface', 'paper', None, None, None]
    checks.append('HF-only fallback; paper priority; safe URLs; domain-specific matching')
    page.locator('[data-t="ate"]').click()
    page.locator('#theme-btn').click()
    assert page.locator('#tbody a.method-ref-name').count() == 2
    mobile = browser.new_page(viewport={'width':390,'height':844}, is_mobile=True, has_touch=True)
    mobile.route('https://fonts.googleapis.com/**', lambda route: route.abort())
    mobile.route('https://fonts.gstatic.com/**', lambda route: route.abort())
    mobile.on('pageerror', lambda error: errors.append(str(error)))
    load_page(mobile)
    assert mobile.evaluate('document.documentElement.scrollWidth <= window.innerWidth')
    assert mobile.locator('#tbody a.method-ref-name').count() == 2
    mobile.locator('#method-references').evaluate('(el)=>el.open=true')
    mobile.locator('#table').screenshot(path=str(OUT/'mobile-references.png'))
    assert not errors, errors
    assert json.loads(page.evaluate('JSON.stringify(DATA)')) == expected
    checks.append('mobile viewport, dark theme, data unchanged, no JavaScript errors')
    report={'status':'passed','url':base or 'in-memory local render','checks':checks,'results_sha256':hashlib.sha256((ROOT/'data/results.json').read_bytes()).hexdigest(),'javascript_errors':errors}
    (OUT/'method-references.json').write_text(json.dumps(report,indent=2))
    print(json.dumps(report,indent=2))
    browser.close()
