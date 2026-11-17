"""Validate title-only paper tables and byte-identical ZIP generator links."""
import hashlib
import json
import tempfile
import unittest
import zipfile
from pathlib import Path

from tools.dgp_registry.github_intake import ingest
from tools.dgp_registry.paper_list import generator_file, generator_link, paper_list_tables, paper_title


class GeneratorPaperListTests(unittest.TestCase):
    def test_all_collected_generator_files_are_exact_zip_sources(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "registry"
            result = ingest(Path("incoming"), out)
            records = [json.loads(path.read_text(encoding="utf-8"))
                       for path in (out / "drafts").glob("*.json")]
            self.assertGreaterEqual(len(records), 20)
            self.assertEqual(len(records), result["mechanisms"])
            exports = 0
            for r in records:
                gen = generator_file(r)
                if not gen:
                    continue
                exports += 1
                source = Path(r["provenance"]["submission_file"])
                member = r["implementation"]["generator_reference"]
                with zipfile.ZipFile(source) as archive:
                    original = archive.read(member)
                generated = (out / gen).read_bytes()
                self.assertEqual(generated, original, r["record_id"])
                self.assertEqual(hashlib.sha256(generated).hexdigest(),
                                 r["implementation"]["exported_generator_sha256"])
                self.assertIn("generator.py", generator_link(r))
            self.assertEqual(exports, len(records),
                             "Existing submission ZIPs should all supply generator.py")
            sample=(out / "by-domain/proximal.md").read_text(encoding="utf-8")
            self.assertNotIn("| Generator.py |", sample)
            detail = (out / "drafts/proximal-dukes-2023-mediation-v1.md").read_text(encoding="utf-8")
            self.assertIn("../generators/proximal-dukes-2023-mediation-v1.py", detail)

    def test_current_paper_titles_are_titles_only(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "registry"
            ingest(Path("incoming"), out)
            records=json.loads((out / "catalog.json").read_text(encoding="utf-8"))["records"]
            for rec in records:
                title = paper_title(rec)
                self.assertTrue(len(title) >= 8, rec["record_id"])
                self.assertNotIn("DOI:", title, rec["record_id"])
                self.assertNotIn("Journal of ", title, rec["record_id"])
                self.assertEqual(rec["paper_title"], title)
            readme="\n".join(paper_list_tables(
                records, draft_prefix="registry/drafts/",
                generator_prefix="registry/generators/"
            ))
            self.assertIn("| Paper Title | DGPs | DGP Mechanisms | Keywords |", readme)
            self.assertNotIn("| Generator.py |", readme)
            self.assertIn("[Proximal mediation analysis]", readme)
            self.assertNotIn("registry/generators/proximal-dukes-2023-mediation-v1.py", readme)
            self.assertNotIn("[Dukes, O.,", readme)

    def test_missing_generator_never_creates_fake_link(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            incoming=root/"incoming"; incoming.mkdir()
            with zipfile.ZipFile(incoming/"no-code.zip", "w") as archive:
                archive.writestr("sample/collection.json", json.dumps({
                    "contribution_id":"no-code-1","family":"ate",
                    "title":"Simple randomized experiment",
                    "source":{"citation":"Sample, A. (2026). The causal test paper. Testing Journal."},
                    "equations":["A~Bernoulli(0.5)"],
                    "estimand":{"definition":"ATE=E[Y(1)-Y(0)]"}
                }))
                archive.writestr("sample/config.json", '{"scenarios":{"original":{"n":10}}}')
            out=root/"registry"
            ingest(incoming, out)
            rec=json.loads((out/"drafts/no-code-1.json").read_text(encoding="utf-8"))
            self.assertIsNone(generator_file(rec))
            self.assertEqual(generator_link(rec), "—")
            self.assertFalse((out/"generators/no-code-1.py").exists())
            self.assertIn("The causal test paper", "\n".join(
                paper_list_tables([rec], generator_prefix="generators/")))

    def test_grouped_paper_links_each_dgp_without_generator_column(self):
        records=[
            {"record_id":"demo-1","domain":"iv",
             "paper":{"citation":"A, B (2026). One paper two DGPs. Journal of Examples.",
                      "title":"One paper two DGPs"},
             "mechanism":{"name":"Alpha"},
             "implementation":{"exported_generator_path":"generators/demo-1.py"}},
            {"record_id":"demo-2","domain":"iv",
             "paper":{"citation":"A, B (2026). One paper two DGPs. Journal of Examples.",
                      "title":"One paper two DGPs"},
             "mechanism":{"name":"Beta"},
             "implementation":{"exported_generator_path":"generators/demo-2.py"}},
        ]
        txt="\n".join(paper_list_tables(records))
        iv=txt.split("### [IV — Instrumental Variables]")[1].split("### [")[0]
        self.assertEqual(iv.count("One paper two DGPs"),1)
        self.assertIn("drafts/demo-1.md",iv)
        self.assertIn("drafts/demo-2.md",iv)
        self.assertNotIn("generator.py",iv)
        self.assertNotIn("generators/demo-1.py",iv)
        self.assertNotIn("generators/demo-2.py",iv)


if __name__=="__main__":
    unittest.main()
