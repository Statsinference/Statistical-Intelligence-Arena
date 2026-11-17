"""Presentation regressions: mathematical notation must not rewrite the DGP."""
import copy
import json
from pathlib import Path
import re

import pytest

from tools.dgp_registry.catalog import detail
from tools.dgp_registry.math_format import equation_markdown, plain_math_to_latex


@pytest.mark.parametrize('source, expected', [
    ('Z_{j}~N(0,1)', r'Z_{j}\sim \mathcal{N}(0,1)'),
    ('X~N_800(0,Sigma)', r'\mathcal{N}_{800}(0,\Sigma)'),
    ('Sigma_ij=0.5^abs(i-j)', r'\Sigma_{ij}=0.5^{\lvert i-j\rvert}'),
    ('Y_obs=Y', r'Y_{\mathrm{obs}}=Y'),
    ('Y_observed=R*Y', r'Y_{\mathrm{observed}}=R\cdot Y'),
    ('M_(t-1)=0', r'M_{t-1}=0'),
    ('Y=X1**2+X2**3', r'Y=X_{1}^{2}+X_{2}^{3}'),
    ('Y=0.5**abs(i-j)', r'Y=0.5^{\lvert i-j\rvert}'),
    ('p_s(x)=x^(1-s)', r'x^{1-s}'),
    ('b=Phi^-1(0.5)', r'\Phi^{-1}(0.5)'),
    ('Sigma_jk=rho^|j-k|', r'\rho^{\lvert j-k\rvert}'),
    ('N11=#{i:Y_i=1}', r'\#\{i:Y_{i}=1\}'),
    (r'p_s(x)=x^(1-s), s in {0,0.1,1}\{1}', r'\setminus \{1\}'),
    ('I_{4x4}=I', r'I_{4\times 4}=I'),
    ('eta0=log(0.01)', r'\eta_{0}=\log(0.01)'),
    ('η0=ln(0.01)', r'\eta_{0}=\ln(0.01)'),
    ('Y=sum_{j=1}^{p} X_j', r'\sum_{j=1}^{p}'),
    ('Y=Σⱼ₌₁ᵏ Xⱼ', r'\sum_{j=1}^{k}'),
    ('q=Integral_5^infinity f(t) dt', r'\int_{5}^{\infty}'),
    ('Q*(u)=4(u-0.4)^3+0.2u', r'Q^{\ast}(u)'),
    ('P*=P', r'P^{\ast}=P'),
    ('Y=A*(X1+1)', r'A\cdot (X_{1}+1)'),
    ('kappa=1; κs=1', r'\kappa s=1'),
    ('A=ZQ', 'A=ZQ'),
    ('rate=5%', r'5\%'),
])
def test_source_notation_is_printed_without_operator_corruption(source, expected):
    # Semicolon-separated examples use the public block interface.
    text='\n'.join(equation_markdown([source],include_source=False))
    assert expected in text
    assert r'\cdot \cdot' not in text
    assert r'_\{' not in text
    assert r'^\{' not in text


def test_starred_function_context_is_shared_but_not_assumed_for_every_product():
    equations=['Q*(u)=4*u^3', 'theta=Q*(0.9)', 'Y=A*(X1+1)']
    md='\n'.join(equation_markdown(equations,include_source=False))
    assert r'Q^{\ast}(0.9)' in md
    assert r'A\cdot (X_{1}+1)' in md


def test_no_greedy_greek_suffix_rewrite():
    assert r'\kappa s' in plain_math_to_latex('y=κs')
    assert r'\kappa_{s}' not in plain_math_to_latex('y=κs')
    assert r'\beta A' in plain_math_to_latex('y=βA')
    assert plain_math_to_latex('y=εZ') is None  # not guessed to be epsilon times Z


def test_named_noise_symbols_require_source_evidence():
    equations=['Z=U+εZ', '`εZ` and `εW` are independent noise terms.']
    md='\n'.join(equation_markdown(equations,include_source=False))
    assert r'Z=U+\varepsilon_{Z}' in md
    assert r'\varepsilon Z' not in md


def test_ambiguous_compound_script_is_kept_verbatim():
    source='gamma_j=phi_gamma_j*sqrt(h2/(1.5*m))'
    md='\n'.join(equation_markdown([source],include_source=False))
    assert '<pre>'+source+'</pre>' in md
    assert '$$' not in md  # no plausible-looking but fabricated nesting


def test_chained_python_power_is_not_misrendered_as_double_superscript():
    assert plain_math_to_latex('Y=x**2**3') is None


@pytest.mark.parametrize('wrapper', [lambda s:'$'+s+'$',lambda s:'$$'+s+'$$',
                                     lambda s:r'\['+s+r'\]',lambda s:'`'+s+'`'])
def test_delimiters_are_not_nested(wrapper):
    expression=r'\mu_a^{I}=(10,11,9,8)'
    md='\n'.join(equation_markdown([wrapper(expression)],include_source=False))
    assert md.count('$$')==2
    assert md.split('$$')[1].strip()==expression


def test_native_latex_keeps_its_structure_and_matrix_rows():
    expression=r'\begin{aligned}X_1&=1\\X_2&=2\end{aligned}'
    assert expression in '\n'.join(equation_markdown([{'latex':expression}]))
    expr=r'\operatorname*{argmin}_{x\in S} f(x)'
    assert expr in '\n'.join(equation_markdown([{'latex':expr}]))


def test_model_labels_remain_attached_to_their_own_formulas():
    entries=[{'label':'Model 2','expression':'m(0)=2'},
             {'label':'Model 4','expression':'m(0)=5/sqrt(2*pi)'}]
    snapshot=copy.deepcopy(entries)
    md='\n'.join(equation_markdown(entries))
    assert entries==snapshot
    assert md.index('**Model 2**')<md.index('m(0)=2')<md.index('**Model 4**')<md.index(r'm(0)=5/\sqrt')


def test_missing_english_transcription_does_not_delete_math_or_source_notes():
    original=['1. `U ~ Uniform(0,1)`，`X ~ Uniform(0,1)`；两者独立。']
    display=['English equation transcription pending; see the original record (JSON).']
    before=copy.deepcopy(original)
    md='\n'.join(equation_markdown(display,source_entries=original))
    assert r'U \sim \mathrm{Uniform}(0,1)' in md
    assert r'X \sim \mathrm{Uniform}(0,1)' in md
    assert '两者独立' in md  # verbatim original source remains available
    assert 'transcription pending' in md  # untranslated context is disclosed
    assert 'original scientific record (JSON)' in md
    assert original==before


def test_all_registered_scientific_records_are_unchanged_by_presentation():
    files=sorted(Path('registry/drafts').glob('*.json'))
    assert files
    for path in files:
        raw=path.read_bytes()
        record=json.loads(raw)
        before=copy.deepcopy(record)
        rendered=detail(record)
        assert record==before, path.name
        assert path.read_bytes()==raw, path.name
        assert 'Parameter scenarios, estimands and truth' in rendered
        for block in re.findall(r'^\$\$\n(.*?)\n\$\$$',rendered,re.M|re.S):
            assert r'_\{' not in block, (path.name,block)
            assert r'^\{' not in block, (path.name,block)
            assert r'\cdot \cdot' not in block, (path.name,block)
            assert not re.search(r'(?<!\\)\$',block), (path.name,block)


@pytest.mark.parametrize('source,expected', [
    ('Y_0t=0',r'Y_{0t}=0'),
    ('X_i,j-1=0',r'X_{i,j-1}=0'),
    ('Y=p0Y(X)+Z',r'\mathrm{p0Y}(X)+Z'),
    ('Y=x^2x',r'x^{2}x'),
])
def test_index_boundaries_and_named_probabilities(source,expected):
    assert expected in plain_math_to_latex(source)


def test_piecewise_intervals_keep_both_values_and_open_closed_endpoints():
    source='m(x)=(x+2)^2/2 on [-1,-0.5), x/2+0.875 on [-0.5,0), -5(x-0.2)^2+1.075 on [0,0.5), x+0.125 on [0.5,1]'
    latex=plain_math_to_latex(source)
    assert r'\begin{cases}' in latex
    for interval in ('[-1,-0.5)','[-0.5,0)','[0,0.5)','[0.5,1]'):
        assert interval in latex
    for expr in ('(x+2)^{2}/2','x/2+0.875','-5(x-0.2)^{2}+1.075','x+0.125'):
        assert expr in latex


def test_reviewed_scalar_sum_transcription_keeps_the_source_untouched():
    source='A=Σ_{j}γ_{j}Z_{j}+U+(1+Σ_{j}δ_{j}Z_{j})ε_{A},'
    md='\n'.join(equation_markdown([source]))
    assert md.count(r'\sum_{j}')==2
    assert source in md
    changed=source.replace('A=', 'B=',1)
    md_changed='\n'.join(equation_markdown([changed],include_source=False))
    assert r'\sum_{j}' not in md_changed  # no stale source-specific mapping


def test_reviewed_network_sum_is_not_a_covariance_matrix():
    source='θ=Σ_{i}β_{1i}w_{i} / Σ_{i}w_{i}.'
    md='\n'.join(equation_markdown([source]))
    assert md.count(r'\sum_{i}')==2
    assert source in md
    assert r'\Sigma_{ij}' in plain_math_to_latex('Sigma_ij=0.5^abs(i-j)')
