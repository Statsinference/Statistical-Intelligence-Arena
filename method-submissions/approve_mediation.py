"""Add a maintainer-graded aggregate result to the public mediation leaderboard."""
import argparse
import json
import math
from pathlib import Path

from sync import public_web_link

RELEASE = "mediation-v1.0"
REGISTRY = Path(__file__).resolve().parents[1] / "data" / "mediation-reviewed.json"
METRICS = {
    "bias": "bias",
    "variance": "variance_within_mechanism",
    "rmse": "rmse",
    "length": "mean_interval_length",
    "coverage": "coverage_95",
    "time_s": "mean_inference_seconds",
}


def make_row(submission, scores, family):
    if not isinstance(submission, dict) or not isinstance(scores, dict):
        raise ValueError("Expected JSON objects for the archived submission and its official score")
    if (submission.get("domain") != "mediation" or submission.get("schema_version") not in (2, 3)
            or submission.get("is_test") is not False):
        raise ValueError("Expected an archived mediation submission from received/")
    number = submission.get("issue_number")
    if type(number) is not int or number < 1 or family not in ("pfn", "other"):
        raise ValueError("Invalid submission number or method family")
    if scores.get("release", RELEASE) != RELEASE or scores.get("tables") != 2000 or scores.get("paired_mechanisms") != 1000:
        raise ValueError("Expected the complete official mediation v1.0 score")
    row = {"issue_number": number, "family": family, "tables": 2000}
    for key, source in (("method", "method_name"), ("version", "version"), ("estimator", "estimator"),
                        ("method_url", "method_url")):
        value = submission.get(source)
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"Missing submission field {source}")
        row[key] = " ".join(value.split())
    if not public_web_link(row["method_url"]):
        raise ValueError("Expected a public HTTPS method URL")
    for key, source in METRICS.items():
        value = scores[source]
        if key == "time_s" and value is None:
            row[key] = None
            continue
        if type(value) not in (float, int) or not math.isfinite(value):
            raise ValueError(f"Invalid score {source}")
        if (key != "bias" and value < 0) or (key == "coverage" and value > 1):
            raise ValueError(f"Score out of range: {source}")
        row[key] = value
    return row


def record_approval(registry_path, row):
    # Exclusive staging serializes local approvals and keeps the original intact on failure.
    pending = registry_path.with_suffix(".json.pending")
    output = pending.open("x", encoding="utf-8", newline="\n")
    try:
        with output:
            registry = json.loads(registry_path.read_text(encoding="utf-8"))
            if registry.get("release") != RELEASE or not isinstance(registry.get("rows"), list):
                raise ValueError("Unexpected reviewed-results registry")
            rows = {entry["issue_number"]: entry for entry in registry["rows"]}
            if len(rows) != len(registry["rows"]):
                raise ValueError("Duplicate issue number in reviewed-results registry")
            rows[row["issue_number"]] = row
            registry["rows"] = [rows[number] for number in sorted(rows)]
            output.write(json.dumps(registry, ensure_ascii=False, allow_nan=False, indent=2) + "\n")
        pending.replace(registry_path)
    except BaseException:
        pending.unlink(missing_ok=True)
        raise


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("submission", type=Path, help="Archived issue JSON in method-submissions/received/")
    parser.add_argument("scores", type=Path, help="Aggregate JSON produced by the official private grader")
    parser.add_argument("--family", choices=("pfn", "other"), required=True)
    args = parser.parse_args()
    try:
        submission = json.loads(args.submission.read_text(encoding="utf-8-sig"))
        scores = json.loads(args.scores.read_text(encoding="utf-8-sig"))
        row = make_row(submission, scores, args.family)
        record_approval(REGISTRY, row)
        print(f"Staged reviewed result for issue #{row['issue_number']} in {REGISTRY.name}")
    except (OSError, ValueError, TypeError, KeyError, OverflowError) as exc:
        parser.exit(1, f"{exc}\n")
