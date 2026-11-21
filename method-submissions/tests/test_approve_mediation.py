import json
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from approve_mediation import RELEASE, make_row, record_approval
from sync import submission_fields


class MediationApprovalTests(unittest.TestCase):
    submission = {
        "domain": "mediation", "schema_version": 2, "is_test": False, "issue_number": 5,
        "method_name": "Path product", "method_url": "https://example.org/method",
        "version": "1.2", "estimator": "OLS with bootstrap intervals"
    }
    scores = {
        "tables": 2000, "paired_mechanisms": 1000, "bias": -.1, "rmse": .2,
        "variance_within_mechanism": .03, "coverage_95": .95, "mean_interval_length": .7,
        "mean_inference_seconds": None
    }

    def test_mapping_and_retry(self):
        row = make_row(self.submission, {**self.scores, "private_note": "excluded"}, "other")
        self.assertEqual(row, {
            "issue_number": 5, "family": "other", "method": "Path product",
            "method_url": "https://example.org/method", "version": "1.2",
            "estimator": "OLS with bootstrap intervals", "tables": 2000, "bias": -.1,
            "rmse": .2, "variance": .03, "length": .7, "coverage": .95, "time_s": None,
        })
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp, "mediation-reviewed.json")
            path.write_text(json.dumps({"release": RELEASE, "rows": []}), encoding="utf-8")
            record_approval(path, {**row, "issue_number": 7})
            record_approval(path, row)
            stored = path.read_bytes()
            record_approval(path, row)
            self.assertEqual(stored, path.read_bytes())
            record_approval(path, {**row, "time_s": 1.5})
            rows = json.loads(path.read_bytes())["rows"]
            self.assertEqual([(r["issue_number"], r["time_s"]) for r in rows], [(5, 1.5), (7, None)])

    def test_invalid_submissions(self):
        for patch in ({"domain": "ate"}, {"is_test": True}, {"issue_number": False},
                      {"method_url": "javascript:alert(1)"}, {"version": ""}):
            with self.subTest(patch=patch), self.assertRaises(ValueError):
                make_row({**self.submission, **patch}, self.scores, "other")

    def test_general_form_mediation_submission_can_be_published(self):
        fields = submission_fields(
            "### Method link\n\nhttps://github.com/example/mediation\n\n"
            "### Research domain\n\nCausal Mediation Analysis\n\n"
            "### Completed checklist\n\n## Method name and version\n\n"
            "Method name: Path product\n\nVersion: v1.2\n\n"
            "## Method description\n\nOLS with bootstrap intervals\n\n## How to run\n\nRscript run.R"
        )
        row = make_row({**fields, "issue_number": 5, "is_test": False}, self.scores, "other")
        self.assertEqual((row["method"], row["version"], row["estimator"]),
                         ("Path product", "v1.2", "OLS with bootstrap intervals"))

    def test_invalid_scores(self):
        for patch in ({"release": "future"}, {"tables": 16}, {"paired_mechanisms": 8},
                      {"bias": float("nan")}, {"coverage_95": 95}, {"rmse": -.1},
                      {"mean_interval_length": None}, {"mean_inference_seconds": -2}):
            with self.subTest(patch=patch), self.assertRaises(ValueError):
                make_row(self.submission, {**self.scores, **patch}, "pfn")


if __name__ == "__main__":
    unittest.main()
