"""Test dynamic reference paper lists generated for README and Registry index."""
import json
import tempfile
import unittest
from pathlib import Path

from tools.dgp_registry.github_intake import ingest
from tools.dgp_registry.paper_list import BEGIN, END, paper_list_tables, update_readme


class PaperListTests(unittest.TestCase):
    def test_current_collection_grouped_by_domain_and_paper(self):
        with tempfile.TemporaryDirectory() as work:
            folder = Path(work)
            root = folder / "registry"
            result = ingest(Path("incoming"), root)
            self.assertGreaterEqual(result["mechanisms"], 20)
            index = (root / "INDEX.md").read_text(encoding="utf-8")
            self.assertIn("## Paper list by research area", index)
            self.assertIn("### [Proximal Causal Inference]", index)
            self.assertIn("### [IV — Instrumental Variables]", index)
            self.assertIn("### [ATE — Average Treatment Effect]", index)
            self.assertIn("### [CATE — Conditional Average Treatment Effect]", index)
            records = json.loads((root / "catalog.json").read_text(encoding="utf-8"))["records"]
            lines = paper_list_tables(records, draft_prefix="registry/drafts/",
                                      domain_prefix="registry/by-domain/")
            self.assertEqual("\n".join(lines).count(
                "| [Proximal Learning for Individualized Treatment Regimes Under Unmeasured Confounding]"), 1)
            self.assertEqual("\n".join(lines).count(
                "(registry/drafts/proximal-qi-2024-quadratic-v1.md)"), 1)

    def test_readme_regeneration_is_idempotent(self):
        with tempfile.TemporaryDirectory() as work:
            folder = Path(work)
            registry = folder / "registry"
            ingest(Path("incoming"), registry)
            readme = folder / "README.md"
            readme.write_text("# Site\n\n" + BEGIN + "\nOld\n" + END +
                              "\n\n## Keep this unchanged\n", encoding="utf-8")
            update_readme(readme, registry / "catalog.json")
            rendered = readme.read_text(encoding="utf-8")
            self.assertIn("### [ATE — Average Treatment Effect]", rendered)
            self.assertIn("### [Proximal Causal Inference]", rendered)
            self.assertIn("(registry/drafts/proximal-dukes-2023-mediation-v1.md)", rendered)
            self.assertIn("## Keep this unchanged", rendered)
            update_readme(readme, registry / "catalog.json")
            self.assertEqual(rendered, readme.read_text(encoding="utf-8"))

    def test_single_paper_with_multiple_mechanisms_is_one_row(self):
        records = [
            {"record_id":"a-1","domain":"iv",
             "paper":"Example Research (2026), DOI: 10.1234/example.",
             "mechanism":"Method One"},
            {"record_id":"a-2","domain":"iv",
             "paper":"EXAMPLE RESEARCH, DOI: 10.1234/example",
             "mechanism":"Method Two"},
        ]
        output="\n".join(paper_list_tables(records))
        section=output.split("### [IV — Instrumental Variables]")[1].split("### [")[0]
        self.assertIn("1 paper(s) · 2 DGP mechanism(s)", section)
        self.assertIn(" | 2 | ", section)
        self.assertEqual(section.count("(drafts/a-1.md)"),1)
        self.assertEqual(section.count("(drafts/a-2.md)"),1)
        self.assertEqual(section.count("https://doi.org/10.1234/example"),1)

    def test_new_paper_auto_appears_and_missing_domain_not_invented(self):
        records=[
            {"record_id":"test-1","domain":"did_sc",
             "paper":{"citation":"New Synthetic Control Paper (2030)."},
             "mechanism":{"name":"Novel SCM"}},
        ]
        section="\n".join(paper_list_tables(records))
        self.assertIn("New Synthetic Control Paper", section)
        self.assertIn("[Novel SCM](drafts/test-1.md)", section)
        self.assertNotIn("Legacy DiD / Synthetic Control", section)
        self.assertIn("### [Needs classification]", section)
        self.assertIn("No submissions yet", section)


if __name__ == "__main__":
    unittest.main()

