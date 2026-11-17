import copy
from tools.dgp_registry.concise_definitions import concise_definition, PENDING
from tools.dgp_registry import catalog
from tools.dgp_registry.presentation_en import has_cjk


def fixtures():
    rec = {'record_id': 'finite-test', 'domain': 'ate',
           'provenance': {'submitted_zip_sha256': 'digest'},
           'estimand': {'name': 'tau', 'definition': 'Finite population treatment effect.'},
           'paper': {}, 'mechanism': {},
           'scenarios': [{'id': 'one', 'truth': {'value': 0}},
                         {'id': 'two', 'truth': {'value': .2}}]}
    defs = {'finite-test': {'domain': 'ate', 'source_zip_sha256': 'digest',
            'default': {'source_name': 'tau', 'source_definition': 'Finite population treatment effect.',
                        'display_math': r'\frac{1}{N}\sum_{i=1}^{N}\{Y_i(1)-Y_i(0)\}'}}}
    return rec, defs


def test_finite_population_formula_and_preserved_original(monkeypatch):
    rec, defs = fixtures()
    monkeypatch.setattr(catalog, 'CONCISE_DEFINITIONS', defs)
    before = copy.deepcopy(rec)
    result = catalog.detail(rec)
    assert result.count(r'$`\frac{1}{N}\sum_{i=1}^{N}\{Y_i(1)-Y_i(0)\}`$') == 1
    assert result.count('rowspan="2"') == 2
    assert result.count(rec['estimand']['definition']) == 1
    assert '<summary>Submitted estimand definitions</summary>' in result
    assert '[Open raw scientific record (JSON)]' in result
    assert rec == before


def test_stale_unknown_and_changed_archive_never_get_guessed():
    rec, defs = fixtures()
    rec['estimand']['definition'] += ' changed'
    assert concise_definition(rec, rec['scenarios'][0], defs) == PENDING
    rec, defs = fixtures()
    rec['provenance']['submitted_zip_sha256'] = 'changed'
    assert concise_definition(rec, rec['scenarios'][0], defs) == PENDING
    rec['record_id'] = 'unknown'
    assert concise_definition(rec, rec['scenarios'][0], defs) == PENDING
    rec, defs = fixtures()
    del defs['finite-test']['source_zip_sha256']
    rec['provenance'] = {}
    assert concise_definition(rec, rec['scenarios'][0], defs) == PENDING
    defs['finite-test']['source_zip_sha256'] = None
    assert concise_definition(rec, rec['scenarios'][0], defs).startswith('$`')


def test_scenario_override_must_match_its_own_source():
    rec, defs = fixtures()
    scenario = rec['scenarios'][1]
    scenario['estimand'] = {'name': 'other', 'definition': 'A distinct target.'}
    assert concise_definition(rec, scenario, defs) == PENDING
    defs['finite-test']['scenarios'] = {'two': {'source_name': 'other',
        'source_definition': 'A distinct target.', 'display_math': r'\mathbb{E}[Y]'}}
    assert concise_definition(rec, scenario, defs) == r'$`\mathbb{E}[Y]`$'
    scenario['estimand']['definition'] += ' changed'
    assert concise_definition(rec, scenario, defs) == PENDING


def test_rejects_unsafe_table_delimiters():
    rec, defs = fixtures()
    for bad in ['X|Y', 'x`y', '$x$', 'X<Y', 'X>Y', 'x\ny']:
        defs['finite-test']['default']['display_math'] = bad
        assert concise_definition(rec, rec['scenarios'][0], defs) == PENDING


def test_notes_are_deduplicated_escaped_and_math_rendered(monkeypatch):
    rec, defs = fixtures()
    entry = defs['finite-test']['default']
    entry['display_note'] = 'at x < 3 | specified group'
    entry['display_note_math'] = r'x_\star=2'
    monkeypatch.setattr(catalog, 'CONCISE_DEFINITIONS', defs)
    result = catalog.detail(rec)
    assert result.count(r'at x &lt; 3 \| specified group') == 1
    assert '- All scenarios:' in result
    assert r'$`x_\star=2`$' in result
    assert result.index('**Definition notes**') > result.index('<td>two</td>')
    entry['display_note_math'] = 'X|Y'
    assert 'Definition note formula requires review.' in catalog.detail(rec)


def test_partial_note_lists_matching_scenarios(monkeypatch):
    rec, defs = fixtures()
    defs['finite-test']['scenarios'] = {'one': {'source_name': 'tau',
        'source_definition': 'Finite population treatment effect.',
        'display_math': 'x', 'display_note': 'Only the first.'}}
    monkeypatch.setattr(catalog, 'CONCISE_DEFINITIONS', defs)
    assert '- one: Only the first.' in catalog.detail(rec)


def test_chinese_source_definitions_are_linked_not_displayed(monkeypatch):
    rec, defs = fixtures()
    rec['estimand']['definition'] = '平均处理效应'
    rec['scenarios'][1]['estimand'] = {'name': 'local', 'definition': '条件平均处理效应'}
    monkeypatch.setattr(catalog, 'CONCISE_DEFINITIONS', defs)
    before = copy.deepcopy(rec)
    page = catalog.detail(rec)
    assert not has_cjk(page)
    assert page.count('Original-language definition is available') == 1
    assert '[Open raw scientific record (JSON)](./finite-test.json)' in page
    assert rec == before


def test_rowspans_split_for_distinct_formula_or_note(monkeypatch):
    rec, defs = fixtures()
    item = defs['finite-test']['default']
    defs['finite-test']['scenarios'] = {'two': dict(item, display_math='x')}
    monkeypatch.setattr(catalog, 'CONCISE_DEFINITIONS', defs)
    page = catalog.detail(rec)
    assert page.count('rowspan="1"') == 4
    assert '<td rowspan="1">\n\n$`x`$\n\n</td>' in page
    defs['finite-test']['scenarios']['two']['display_math'] = item['display_math']
    defs['finite-test']['scenarios']['two']['display_note'] = 'Distinct condition.'
    page = catalog.detail(rec)
    assert page.count('rowspan="1"') == 4
    assert 'Distinct condition.' in page


def test_html_cells_escape_untrusted_scenario_and_reported_value(monkeypatch):
    rec, defs = fixtures()
    rec['scenarios'][0]['id'] = '<script>alert("x")</script>'
    rec['scenarios'][0]['truth']['value'] = '<img src=x onerror=alert(1)>'
    monkeypatch.setattr(catalog, 'CONCISE_DEFINITIONS', defs)
    page = catalog.detail(rec)
    assert '<td>&lt;script&gt;alert(&quot;x&quot;)&lt;/script&gt;</td>' in page
    assert '<td>&lt;img src=x onerror=alert(1)&gt;</td>' in page
    assert '<script>alert' not in page and '<img src=' not in page
