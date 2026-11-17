"""Regressions for catalog math rendering without changing source records."""
from tools.dgp_registry.math_format import equation_markdown, formatted_blocks, plain_math_to_latex


def test_author_latex_cardinality_hash_and_set_are_escaped():
    entry = {'latex': r'\mathrm{N}_{11}=#{i:Y_{i}(1)=1,Y_{i}(0)=1}'}
    assert formatted_blocks(entry) == [
        ('math', r'\mathrm{N}_{11}=\#\{i:Y_{i}(1)=1,Y_{i}(0)=1\}')]
    assert entry['latex'] == r'\mathrm{N}_{11}=#{i:Y_{i}(1)=1,Y_{i}(0)=1}'


def test_text_hash_and_existing_escaped_hash():
    assert formatted_blocks({'latex': r'\text{#1}'}) == [('math', r'\text{\#1}')]
    assert formatted_blocks({'latex': r'\#\{1,2\}'}) == [('math', r'\#\{1,2\}')]


def test_macro_parameters_are_not_silently_rewritten():
    raw = r'\newcommand{\foo}[1]{#1}'
    assert formatted_blocks({'latex': raw}) == [('source', raw)]
    assert plain_math_to_latex(raw + '=0') is None


def test_wang_iv_declared_product_is_not_a_single_identifier():
    raw = 'p_{0}=(n(1−φ_{3})+c(1−q_{0}), nφ_{3}+cq_{0}, a(1−φ_{4}), aφ_{4}),'
    blocks = formatted_blocks({'expression': raw})
    assert blocks[0][0] == 'math'
    assert r'c q_{0}' in blocks[0][1]
    assert r'\mathrm{cq}' not in blocks[0][1]
    assert r'\text{ a }' not in blocks[0][1]
    changed = raw.replace('cq_{0}', 'cq_{1}')
    assert changed != raw
    # Only the exact reviewed source expression receives the transcription.
    assert formatted_blocks({'expression': changed}) != blocks


def test_pending_transcription_keeps_delimited_math_and_points_to_source():
    original = "设定 `X1~N(0,1)`，后面还有未翻译的上下文。"
    rendered = "\n".join(equation_markdown(
        ["English equation transcription pending; see JSON."],
        include_source=False, source_entries=[original]))
    assert "English equation transcription pending" in rendered
    assert "original scientific record (JSON)" in rendered
    assert r"X_{1}" in rendered
    assert r"\mathcal{N}" in rendered
    assert "设定" not in rendered
    assert original == "设定 `X1~N(0,1)`，后面还有未翻译的上下文。"


def test_pending_transcription_without_safe_fragment_discloses_missing_context():
    original = "未给出英文方程，应核对原文。"
    rendered = "\n".join(equation_markdown(
        ["English equation transcription pending; see JSON."],
        include_source=False, source_entries=[original]))
    assert "English equation transcription pending" in rendered
    assert "original scientific record (JSON)" in rendered
    assert "未给出" not in rendered
