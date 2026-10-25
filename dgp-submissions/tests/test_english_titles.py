"""The mechanism link and page heading are English; raw source is preserved."""
import json
import tempfile
import unittest
from pathlib import Path

from tools.dgp_registry.github_intake import ingest
from tools.dgp_registry.title_display import display_title


class EnglishTitleTests(unittest.TestCase):
    def test_existing_registry_titles_are_english(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "registry"
            result = ingest(Path("incoming"), root)
            self.assertGreaterEqual(result["mechanisms"], 20)
            for item in json.loads((root / "catalog.json").read_text(encoding="utf-8"))["records"]:
                self.assertFalse(any('\u3400' <= c <= '\u9fff' for c in item["mechanism"]),
                                 (item["record_id"], item["mechanism"]))
                content=(root / "drafts" / (item["record_id"]+".md")).read_text(encoding="utf-8")
                self.assertEqual(content.splitlines()[0], "# "+item["mechanism"])
            # Original student content is still retrievable in the source JSON.
            raw = json.loads((root/"drafts"/"proximal-dukes-2023-mediation-v1.json").read_text(encoding="utf-8"))
            self.assertEqual(raw["mechanism"]["name"], "潜在混杂下的自然直接效应")

    def test_new_zip_english_title_without_case_rules(self):
        r={"record_id":"novel-iv-test", "mechanism":{"name":"中文原始标题",
                                              "title_en":"Compliance under a New Design"}}
        self.assertEqual(display_title(r), "Compliance under a New Design")

    def test_fallback_does_not_mistranslate(self):
        r={"record_id":"new-cate-mechanism", "mechanism":{"name":"中文原始标题"}}
        self.assertEqual(display_title(r),
                         "DGP new-cate-mechanism (English title required)")


if __name__=="__main__":
    unittest.main()
