"""Regression tests for general ZIP-to-GitHub LaTeX rendering."""
import tempfile
import unittest
from pathlib import Path

from tools.dgp_registry.github_intake import ingest
from tools.dgp_registry.math_format import equation_markdown, plain_math_to_latex
from tools.dgp_registry.zip_reader import read_archive


class MathRenderingTests(unittest.TestCase):
    def test_existing_proximal_zip_generates_latex_without_paper_specific_rules(self):
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "registry"
            result = ingest(Path("examples"), output)
            self.assertEqual(result["mechanisms"], 10)
            self.assertEqual(result["scenarios"], 11)
            md = (output / "drafts/proximal-dukes-2023-mediation-v1.md").read_text(encoding="utf-8")
            self.assertIn(r"\begin{bmatrix}", md)
            self.assertIn(r"\mathcal{N}_{3}", md)
            self.assertIn(r"\varepsilon_{z}", md)
            self.assertIn(r"\begin{aligned}", md)
            self.assertIn("Original source equations (verbatim)", md)
            self.assertIn("Open raw scientific record (JSON)", md)
            self.assertNotIn(r"X_\{1\}", md)
            self.assertEqual(md.count("$$") % 2, 0)

    def test_ate_plain_math_is_general(self):
        md = "\n".join(equation_markdown([
            "X1 ~ N(0,1)",
            "A~Bernoulli(.5)",
            "Y=2A+X1+ε",
        ]))
        self.assertIn(r"X_{1} \sim", md)
        self.assertIn(r"\mathrm{Bernoulli}", md)
        self.assertIn(r"Y=2A+X_{1}+\varepsilon", md)

    def test_explicit_latex_input_is_preserved(self):
        eq = {
            "expression": "NDE = E[Y(1,M(0)) - Y(0,M(0))]",
            "latex": r"\mathrm{NDE}=\mathbb{E}[Y(1,M(0))-Y(0,M(0))]",
        }
        md = "\n".join(equation_markdown([eq]))
        self.assertIn(eq["latex"], md)
        self.assertIn(eq["expression"], md)

    def test_unrecognized_prose_is_kept_without_inventing_math(self):
        original = "这里使用论文未完全定义的数据机制。"
        md = "\n".join(equation_markdown([original]))
        self.assertIn(original, md)
        self.assertNotIn("$$", md)
        self.assertIsNone(plain_math_to_latex("unknown true value"))

    def test_verbatim_appendix_is_html_escaped(self):
        md = "\n".join(equation_markdown(["</pre><script>alert(1)</script>"]))
        self.assertNotIn("<script>", md)
        self.assertIn("&lt;script&gt;", md)

    def test_real_iv_contribution_unicode_sums_and_prose(self):
        zip_path = Path("incoming/iv-athey-tibshirani-wager-2019-compliance-v1.zip")
        records, warnings = read_archive(zip_path)
        self.assertEqual(len(records), 1)
        content = "\n".join(equation_markdown(records[0]["mechanism"]["generation_equations"]))
        self.assertIn(r"I_{10}", content)
        self.assertIn(r"\varepsilon", content)
        self.assertIn(r"\mathrm{Bernoulli}", content)
        self.assertIn(r"\mathrm{expit}", content)
        self.assertIn(r"\sum_{j=1}^{k}", content)
        self.assertIn(r"\max(0,x_{j})", content)
        self.assertIn(r"\in \{2,4\}", content)
        self.assertIn("**Additive**", content)
        self.assertIn("**Nonadditive**", content)
        self.assertIn("mutually independent", content)
        self.assertNotIn(r"\operatorname", content)
        math_parts = content.split("$$")[1::2]
        math_only = "\n".join(math_parts)
        self.assertNotIn("I₁₀", math_only)
        self.assertNotIn("Σⱼ", math_only)
        self.assertTrue(all("mutually independent" not in block for block in math_parts))

    def test_all_existing_domains_generate_github_safe_math(self):
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "registry"
            result = ingest(Path("incoming"), output)
            self.assertGreaterEqual(result["mechanisms"], 20)
            for file in (output / "drafts").glob("*.md"):
                content = file.read_text(encoding="utf-8")
                math = "\n".join(content.split("$$")[1::2])
                self.assertNotIn(r"\operatorname", math, file.name)
                self.assertIn("Original source equations (verbatim)", content)

    def test_explicit_unsupported_operator_macro_is_sanitized(self):
        md = "\n".join(equation_markdown([
            {"expression": "A ~ Bernoulli(0.5)",
             "latex": r"A\sim\operatorname{Bernoulli}(0.5)"}
        ]))
        self.assertIn(r"\mathrm{Bernoulli}", md)
        self.assertNotIn(r"\operatorname", md)

    def test_plain_unicode_subscript_and_set_membership(self):
        converted = plain_math_to_latex("k ∈ {2,4}")
        self.assertIn(r"\in \{2,4\}", converted)
        self.assertEqual(plain_math_to_latex("X∼N(0,I₁₀)"),
                         r"X\sim \mathcal{N}(0,I_{10})")




    def test_no_double_subscripts_on_reported_examples(self):
        from tools.dgp_registry.math_format import DIAGNOSTIC_RX
        eqs = [
            'Y_t|λ_t ~ Poisson(exp{λ_t+βA_t})',
            'W_t,Z_t|λ_t 独立 ~ Poisson(λ_t/(e−1))',
            'e(X)=[1+20*X1*(1-X1)^3]/4',
            'b(X)=sin(pi*X1*X2)+2*(X3-0.5)^2+X4+0.5*X5',
            'X_j iid Uniform(0,1), j=1,...,6'
        ]
        rendered = '\n'.join(equation_markdown(eqs))
        blocks = rendered.split(chr(36)*2)[1::2]
        math = '\n'.join(blocks)
        self.assertIn(r'\beta A_{t}', math)
        self.assertNotIn(r'\beta_{A}_t', math)
        self.assertIn(r'\mathrm{Poisson}', math)
        self.assertIn(r'20\cdot X_{1}\cdot (1-X_{1})^{3}', math)
        self.assertIn(r'\sin(\pi\cdot X_{1}\cdot X_{2})', math)
        self.assertIn(r'\overset{\mathrm{iid}}{\sim}', math)
        self.assertFalse(DIAGNOSTIC_RX.search(math))
        self.assertNotIn(r'\_', math)

    def test_nested_commas_in_distributions_and_all_uploaded_equations(self):
        from tools.dgp_registry.math_format import DIAGNOSTIC_RX
        from tools.dgp_registry.zip_reader import read_archive
        example = ('Z~Normal(0,SD=2), U~Normal(0,SD=2), '
                   'delta,zeta~Normal(0,SD=0.1), mutually independent')
        parts = '\n'.join(equation_markdown([example])).split(chr(36)*2)[1::2]
        self.assertEqual(len(parts), 3)
        self.assertIn(r'\delta,\zeta\sim', parts[-1])
        self.assertTrue(all('mutually independent' not in p for p in parts))
        from tools.dgp_registry.intake_safety import read_zip_report
        # Five known uploads lack equations. They are rejected by intake and
        # must not prevent independent valid submissions from being checked.
        known_invalid = {
            'did-qin-zhang-2008-bounded-panel-v1.zip',
            'did-ye-2024-iid-common-trend-v1.zip',
            'did-zhou-2026-mixture-mean-v1.zip',
            'did-zhou-2026-network-weight-v1.zip',
            'did-zhou-2026-truncated-mean-v1.zip',
        }
        checked = 0
        for archive in Path('incoming').glob('*.zip'):
            records, _, errors, _ = read_zip_report(archive)
            if errors:
                self.assertIn(archive.name, known_invalid, str(errors))
                self.assertTrue(all('Missing generating equations' in e['message'] for e in errors))
            for rec in records:
                checked += 1
                markdown = '\n'.join(equation_markdown(rec['mechanism']['generation_equations']))
                for latex in markdown.split(chr(36)*2)[1::2]:
                    self.assertNotIn(r'\operatorname', latex, rec['record_id'])
                    # Literal underscores are valid inside textual labels;
                    # reject escaped underscores in mathematical notation.
                    import re
                    notation = re.sub(r'\\(?:mathrm|text)\{[^{}]*\}', '', latex)
                    self.assertNotIn(r'\_', notation, rec['record_id'])
                    self.assertFalse(DIAGNOSTIC_RX.search(latex), rec['record_id'])
                    self.assertEqual(latex.count('{'), latex.count('}'), rec['record_id'])
        self.assertGreaterEqual(checked, 20)


if __name__ == "__main__":
    unittest.main()
