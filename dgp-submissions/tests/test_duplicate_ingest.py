"""Verify content-based duplicate handling without a model or special-case DGP data."""
import json
import tempfile
import unittest
from pathlib import Path
from zipfile import ZipFile

from tools.dgp_registry.github_intake import ingest


def make_zip(path, *, family="ate", coef=2, extra=False):
    source = {
        "contribution_id": "generic-example-1",
        "family": family,
        "title": "Synthetic test of a general DGP",
        "source": {"citation": "Unit test only", "locator": "§1"},
        "equations": ["X~N(0,1)", "A~Bernoulli(.5)", f"Y={coef}*A+X+epsilon"],
        "estimand": {"definition": "ATE = E[Y(1)-Y(0)]"},
        "truth": {"reference_value": coef, "method": "intervention contrast"},
        "sampling": "IID"
    }
    with ZipFile(path, "w") as z:
        z.writestr("mechanism/collection.json", json.dumps(source))
        z.writestr("mechanism/config.json", json.dumps({"scenarios": {"original": {"n": 500}}}))
        if extra:
            z.writestr("mechanism/README.txt", "Same science; different ZIP packaging")


class DuplicateIntakeTests(unittest.TestCase):
    def test_equivalent_content_in_distinct_archives_is_merged(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d); incoming=root/"incoming"; incoming.mkdir()
            make_zip(incoming/"a.zip")
            make_zip(incoming/"b.zip", extra=True)
            out=root/"output"
            results=ingest(incoming,out)
            self.assertEqual(results["mechanisms"],1)
            record=json.loads((out/"drafts/generic-example-1.json").read_text())
            self.assertEqual(len(record["provenance"]["duplicate_submission_files"]),1)
            self.assertIn("Equivalent DGP", (out/"INDEX.md").read_text())

    def test_conflicting_content_kept_as_two_unverified_records(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d); incoming=root/"incoming"; incoming.mkdir()
            make_zip(incoming/"a.zip", family="ate", coef=2)
            make_zip(incoming/"b.zip", family="iv", coef=4)
            out=root/"output"
            results=ingest(incoming,out)
            self.assertEqual(results["mechanisms"],2)
            self.assertIn("CONFLICT", (out/"INDEX.md").read_text())
            originals=list((out/"drafts").glob("*.json"))
            self.assertEqual(len(originals),2)
            for p in originals:
                record=json.loads(p.read_text())
                self.assertEqual(record["review_status"],"duplicate_conflict_needs_review")

    def test_new_domain_works_without_hardcoded_paper(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d); incoming=root/"incoming"; incoming.mkdir()
            make_zip(incoming/"one.zip",family="cate")
            result=ingest(incoming,root/"output")
            self.assertEqual(result["mechanisms"],1)
            self.assertIn("Synthetic test", (root/"output/by-domain/cate.md").read_text())


if __name__ == "__main__":
    unittest.main()
