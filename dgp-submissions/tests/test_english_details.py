"""English-only DGP detail pages and genuinely two-dimensional covariance matrices."""
import copy
import json
import re
import tempfile
import unittest
from pathlib import Path

from tools.dgp_registry.github_intake import ingest
from tools.dgp_registry.presentation_en import english_display, has_cjk
from tools.dgp_registry.math_format import equation_markdown

class EnglishDetailsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.folder=tempfile.TemporaryDirectory()
        cls.root=Path(cls.folder.name)/"registry"
        cls.result=ingest(Path("incoming"),cls.root)

    @classmethod
    def tearDownClass(cls):
        cls.folder.cleanup()

    def test_all_current_detail_pages_are_english(self):
        self.assertGreaterEqual(self.result["mechanisms"], 23)
        files=sorted((self.root/"drafts").glob("*.md"))
        self.assertEqual(len(files),self.result["mechanisms"])
        for f in files:
            content=f.read_text(encoding="utf-8")
            self.assertFalse(has_cjk(content),f.name)
            self.assertIn("Source locator:",content)
            self.assertIn("Identifiability assumptions",content)
            self.assertIn("Generator source",content)
            self.assertEqual(len(re.findall(r"^```math
(.*?)\n```$", content, re.M | re.S)),\n                             content.count("```math"), f.name)

    def test_raw_proximal_science_is_unchanged(self):
        filename="proximal-dukes-2023-mediation-v1"
        original=json.loads((self.root/"drafts"/(filename+".json")).read_text(encoding="utf-8"))
        self.assertIn("潜在",original["mechanism"]["name"])
        original_copy=copy.deepcopy(original)
        preview,translated=english_display(original)
        self.assertTrue(translated)
        self.assertEqual(original_copy,original)
        self.assertFalse(has_cjk(preview["paper"]["source_locator"]))
        self.assertFalse(has_cjk(str(preview["mechanism"]["assumptions"])))

        page=(self.root/"drafts"/(filename+".md")).read_text(encoding="utf-8")
        self.assertIn("[Open raw scientific record (JSON)](./"+filename+".json)",page)
        self.assertNotIn("(X1,X2,U)~N3(",page)
        self.assertIn(r"\begin{bmatrix}",page)

    def test_numeric_covariance_has_three_rows_and_three_columns(self):
        for filename in [
            "proximal-dukes-2023-mediation-v1",
            "proximal-cui-2024-linear-v1",
            "proximal-qi-2024-linear-itr-v1",
            "proximal-su-2026-transport-v1",
        ]:
            page=(self.root/"drafts"/(filename+".md")).read_text(encoding="utf-8")
            match=re.search(r"\\begin\{bmatrix\}\s*(.*?)\s*\\end\{bmatrix\}",page,re.S)
            self.assertIsNotNone(match,filename)
            rows=re.split(r"\\\\\s*\n",match.group(1).strip())
            self.assertEqual(len(rows),3,(filename,rows))
            for row in rows:
                self.assertEqual(len(row.split("&")),3,(filename,row))
                self.assertTrue(all(re.search(r"\d",token) for token in row.split("&")))

    def test_legacy_numeric_matrix_renders_multiline(self):
        md="\n".join(equation_markdown([
            "Sigma=[[1,0.25,0.5],[0.25,1,0.5],[0.5,0.5,1]]"
        ]))
        self.assertIn(r"\begin{bmatrix}",md)
        self.assertIn("1 & 0.25 & 0.5",md)
        self.assertEqual(md.count(" & "),6)
        self.assertIn(r"\end{bmatrix}",md)

    def test_missing_translation_is_explicit_not_invented(self):
        record={
            "record_id":"unseen-cate-1",
            "paper":{"citation":"Example Study","source_locator":"原文第二页"},
            "mechanism":{"generation_equations":["Y=X+ε；需要其他信息"],
                         "assumptions":["完全随机的条件"]},
            "estimand":{"definition":"直接效应"},
            "scenarios":[],
        }
        view,flag=english_display(record)
        self.assertTrue(flag)
        self.assertFalse(has_cjk(str(view)))
        self.assertEqual(record["paper"]["source_locator"],"原文第二页")


if __name__=="__main__":
    unittest.main()
