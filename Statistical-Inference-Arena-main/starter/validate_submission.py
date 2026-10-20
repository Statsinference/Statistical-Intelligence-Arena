#!/usr/bin/env python3
"""Protocol v0.3 structural checks, output schema 0.2.0; no estimator, YAML parser or scientific approval."""
import argparse
import csv
import json
import math
from pathlib import Path
import re
import sys

VERSION = "0.2.0"
REQUIRED_FILES = (
    "dgps/catalog.csv", "dgps/README.md", "dgps/cards/mediation_illustrative.md",
    "hyperdistribution.yaml", "configs/train.yaml", "configs/evaluate.yaml", "demo/README.md",
    "README.md", "CONTRIBUTING.md", "task.yaml", "task.md", "scientific_spec.md",
    "data/README.md", "data/schema.csv", "environment/README.md", "solution/README.md",
    "solution/methods.json", "evaluation/protocol.yaml", "evaluation/result.schema.json",
    "evaluation/check_contract.py", "reports/validation_report.md", "reports/result.json",
    "review/ai_review.md", "LICENSE.md", "PROVENANCE.md", "validate_submission.py",
)
COMMON_FIELDS = (
    "schema_version", "artifact_kind", "task_id", "task_version", "layer", "run_id",
    "mechanism_id", "replicate_id", "method_id", "target_id", "target_object",
    "query_id", "group_id", "status", "status_reason", "estimate", "uncertainty",
    "diagnostics", "evidence", "runtime", "provenance",
)
STATUSES = {"ok", "not_identified", "unsupported", "abstained", "failed"}
TARGETS = {"parameter_ci", "mean_ci", "prediction_set"}
SCOPES = {"marginal", "fixed_query", "group", "pointwise", "simultaneous"}
UQ_TYPES = {"none", "standard_error", "confidence_interval", "credible_interval", "prediction_set"}
MODES = {"native_frozen", "adapted", "refit"}
ROLES = {"classical_reference", "pfn_adapter", "other"}
SCHEMA_COLUMNS = ("column", "role", "dtype", "required", "unit", "allowed_values", "missingness_policy", "description")

def require(condition, message):
    if not condition:
        raise ValueError(message)

def fields(value, names, label):
    require(isinstance(value, dict), label + " must be an object")
    missing = [k for k in names if k not in value]
    require(not missing, label + " missing: " + ", ".join(missing))

def text(value, label, nullable=False):
    if nullable and value is None:
        return
    require(isinstance(value, str) and bool(value.strip()), label + " must be a nonempty string")

def finite_number(value, label, nullable=False, nonnegative=False):
    if nullable and value is None:
        return
    require(isinstance(value, (int, float)) and not isinstance(value, bool), label + " must be numeric")
    require(math.isfinite(value), label + " must be finite")
    if nonnegative:
        require(value >= 0, label + " must be nonnegative")

def string_list(value, label):
    require(isinstance(value, list), label + " must be a list")
    for item in value:
        text(item, label + " item")

def evidence_list(value, label):
    string_list(value, label)
    for item in value:
        path = item.replace("\\", "/")
        require(not path.startswith("/") and ":" not in path and ".." not in path.split("/"),
                label + " must contain relative bundle paths without traversal")

def endpoint(value, label):
    if isinstance(value, str) and value in ("-inf", "+inf"):
        return float("-inf") if value == "-inf" else float("inf")
    finite_number(value, label)
    return float(value)

def interval_pair(lower, upper, label):
    lo, hi = endpoint(lower, label + ".lower"), endpoint(upper, label + ".upper")
    require(lo != float("inf") and hi != float("-inf"), label + ": invalid infinity direction")
    require(lo <= hi, label + ": reversed endpoints")
    return lo, hi

def validate_output(data, expected_layer, require_run=False):
    fields(data, COMMON_FIELDS, "output")
    allowed = set(COMMON_FIELDS) | ({"estimand", "identifiability", "assumptions"} if expected_layer == "A" else set())
    require(set(data) <= allowed, "unknown output field(s): " + ", ".join(sorted(set(data)-allowed)))
    require(data["schema_version"] == VERSION, "unsupported schema_version")
    require(data["layer"] == expected_layer, "incorrect layer")
    require(data["artifact_kind"] in ("illustrative_example", "benchmark_run"), "invalid artifact_kind")
    example = data["artifact_kind"] == "illustrative_example"
    if require_run:
        require(not example, "illustrative examples are not submission runs")
    for key in ("task_id", "task_version", "method_id", "target_id"):
        text(data[key], key)
    for key in ("run_id", "mechanism_id", "replicate_id"):
        text(data[key], key, nullable=example)
    require(data["target_object"] in TARGETS, "invalid target_object")
    require(data["status"] in STATUSES, "invalid status")
    text(data["status_reason"], "status_reason", nullable=data["status"] == "ok")
    for key in ("query_id", "group_id"):
        text(data[key], key, nullable=True)
    ok = data["status"] == "ok"
    uq = data["uncertainty"]
    base_uq = {"type", "coverage_scope", "level", "interval", "standard_error", "method"}
    fields(uq, base_uq, "uncertainty")
    require(set(uq) <= base_uq | {"intervals"}, "unknown uncertainty field")
    require(uq["type"] in UQ_TYPES, "invalid uncertainty.type")
    require(uq["coverage_scope"] in SCOPES, "invalid coverage_scope")
    scope = uq["coverage_scope"]
    if scope in ("fixed_query", "pointwise"):
        text(data["query_id"], "query_id for query-specific coverage")
    if scope == "group":
        text(data["group_id"], "group_id for group coverage")
    require(not (ok and scope == "simultaneous"), "simultaneous outputs need a versioned extension")
    if ok:
        finite_number(data["estimate"], "estimate", nullable=uq["type"] == "prediction_set")
    else:
        require(data["estimate"] is None and uq["type"] == "none", "non-ok outputs require null estimate and type none")
    if uq["type"] == "prediction_set":
        require(data["target_object"] == "prediction_set", "prediction set cannot stand in for parameter/mean CI")
        fields(uq, ("intervals",), "uncertainty")
        require(uq["interval"] is None and uq["standard_error"] is None, "prediction set uses intervals only")
        require(isinstance(uq["intervals"], list), "intervals must be a list")
        previous_upper = None
        for i, component in enumerate(uq["intervals"]):
            require(isinstance(component, list) and len(component) == 2, "each set component must be [lower, upper]")
            lo, hi = interval_pair(component[0], component[1], "intervals[{}]".format(i))
            if previous_upper is not None:
                require(lo > previous_upper, "set components must be sorted, disjoint and non-touching")
            previous_upper = hi
    else:
        require("intervals" not in uq, "intervals field is only for prediction_set")
        if uq["type"] != "none":
            require(data["target_object"] != "prediction_set", "prediction target requires prediction_set or point-only none")
    if uq["type"] == "none":
        require(all(uq[k] is None for k in ("level", "interval", "standard_error", "method")), "type none requires null numerical uncertainty")
    elif uq["type"] == "standard_error":
        require(uq["level"] is None and uq["interval"] is None, "SE alone has no level/interval")
        finite_number(uq["standard_error"], "standard_error", nonnegative=True)
        text(uq["method"], "uncertainty.method")
    else:
        finite_number(uq["level"], "level")
        require(0 < uq["level"] < 1, "level must be between zero and one")
        text(uq["method"], "uncertainty.method")
        if uq["type"] != "prediction_set":
            fields(uq["interval"], ("lower", "upper"), "interval")
            require(set(uq["interval"]) == {"lower", "upper"}, "unknown interval field")
            interval_pair(uq["interval"]["lower"], uq["interval"]["upper"], "interval")
            finite_number(uq["standard_error"], "standard_error", nullable=True, nonnegative=True)
    evidence_list(data["evidence"], "evidence")
    require(isinstance(data["diagnostics"], list), "diagnostics must be a list")
    for item in data["diagnostics"]:
        fields(item, ("code", "status", "summary", "evidence"), "diagnostic")
        text(item["code"], "diagnostic.code")
        text(item["summary"], "diagnostic.summary")
        require(item["status"] in ("pass", "warn", "fail", "not_checked"), "invalid diagnostic status")
        evidence_list(item["evidence"], "diagnostic.evidence")
    runtime = data["runtime"]
    fields(runtime, ("wall_seconds", "offline_training_seconds", "load_seconds", "warm_end_to_end_seconds",
                     "device", "peak_memory_mb", "includes", "notes"), "runtime")
    finite_number(runtime["wall_seconds"], "runtime.wall_seconds", nullable=example, nonnegative=True)
    for k in ("offline_training_seconds", "load_seconds", "warm_end_to_end_seconds", "peak_memory_mb"):
        finite_number(runtime[k], "runtime."+k, nullable=True, nonnegative=True)
    text(runtime["device"], "runtime.device", nullable=example)
    text(runtime["notes"], "runtime.notes")
    string_list(runtime["includes"], "runtime.includes")
    if not example:
        require(bool(runtime["includes"]), "benchmark_run must declare timed stages")
    prov = data["provenance"]
    fields(prov, ("method_name", "method_version", "method_role", "execution_mode", "adaptation_steps",
                  "code_commit", "checkpoint_sha256", "input_sha256", "seed"), "provenance")
    require(prov["method_role"] in ROLES, "invalid method_role")
    require(prov["execution_mode"] in MODES, "invalid execution_mode")
    string_list(prov["adaptation_steps"], "adaptation_steps")
    if prov["execution_mode"] == "native_frozen":
        require(not prov["adaptation_steps"], "native_frozen cannot claim calibration/correction/adaptation")
    if prov["execution_mode"] == "adapted":
        require(bool(prov["adaptation_steps"]), "adapted requires declared steps")
    for k in ("method_name", "method_version"):
        text(prov[k], "provenance."+k, nullable=example)
    text(prov["code_commit"], "code_commit", nullable=True)
    for k in ("checkpoint_sha256", "input_sha256"):
        value = prov[k]
        require(value is None or (isinstance(value, str) and re.fullmatch(r"[0-9a-fA-F]{64}", value)), k+" must be a SHA-256 digest or null")
    if not example:
        require(prov["input_sha256"] is not None, "benchmark_run requires input_sha256")
    require(prov["seed"] is None or (isinstance(prov["seed"], int) and not isinstance(prov["seed"], bool)), "seed must be integer/null")
    if expected_layer == "A":
        fields(data, ("estimand", "identifiability", "assumptions"), "analysis")
        est = data["estimand"]
        fields(est, ("id", "definition", "population", "scale", "units"), "estimand")
        for k in ("id", "definition", "population", "scale"):
            text(est[k], "estimand."+k)
        text(est["units"], "estimand.units", nullable=True)
        require(est["id"] == data["target_id"], "estimand.id differs from target_id")
        ident = data["identifiability"]
        fields(ident, ("status", "justification", "identification_formula"), "identifiability")
        require(ident["status"] in ("identified", "partially_identified", "not_identified", "not_assessed"), "invalid identification status")
        text(ident["justification"], "identifiability.justification")
        text(ident["identification_formula"], "identification_formula", nullable=True)
        if ok:
            require(ident["status"] == "identified", "ok A output requires identified target")
        if data["status"] == "not_identified":
            require(ident["status"] in ("not_identified", "partially_identified"), "conflicting identification status")
        require(isinstance(data["assumptions"], list) and bool(data["assumptions"]), "A assumptions must be nonempty")
        for item in data["assumptions"]:
            fields(item, ("id", "statement", "assessment", "evidence"), "assumption")
            text(item["id"], "assumption.id")
            text(item["statement"], "assumption.statement")
            require(item["assessment"] in ("supplied", "supported", "uncertain", "violated", "not_assessed"), "invalid assumption assessment")
            evidence_list(item["evidence"], "assumption.evidence")

def reject_constant(value):
    raise ValueError("non-standard JSON constant: "+value)

def finite_float(value):
    parsed = float(value)
    require(math.isfinite(parsed), "non-finite JSON number: "+value)
    return parsed

def unique_keys(pairs):
    out = {}
    for key, value in pairs:
        require(key not in out, "duplicate JSON key: "+key)
        out[key] = value
    return out

def loads_strict(raw):
    return json.loads(raw, parse_constant=reject_constant, parse_float=finite_float, object_pairs_hook=unique_keys)

def read_json(path):
    return loads_strict(path.read_text(encoding="utf-8-sig"))

def check_csv(path):
    with path.open(encoding="utf-8-sig", newline="") as stream:
        reader = csv.DictReader(stream)
        require(reader.fieldnames == list(SCHEMA_COLUMNS), "unexpected CSV header")
        rows, names = list(reader), set()
        require(bool(rows), "empty data dictionary")
        for row in rows:
            require(None not in row and all(v is not None for v in row.values()), "malformed CSV row")
            text(row["column"], "column")
            require(row["column"] not in names, "duplicate column")
            names.add(row["column"])
            require(row["required"] in ("true", "false"), "required must be true/false")
            for key in ("role", "dtype", "description"):
                text(row[key], key)

def validate_methods(data, submission=False):
    fields(data, ("schema_version", "artifact_kind", "methods"), "methods registry")
    require(data["schema_version"] == VERSION, "unsupported registry version")
    require(data["artifact_kind"] in ("illustrative_example", "contribution_registry"), "invalid registry artifact_kind")
    if submission:
        require(data["artifact_kind"] == "contribution_registry", "illustrative method registry is not a submission")
    require(isinstance(data["methods"], list), "methods must be a list")
    roles, ids = set(), set()
    for method in data["methods"]:
        fields(method, ("method_id", "method_role", "model_version", "support_status", "execution_mode", "adaptation_steps", "entrypoint", "reason"), "method")
        for k in ("method_id", "model_version"):
            text(method[k], k)
        require(method["method_id"] not in ids, "duplicate method_id")
        ids.add(method["method_id"])
        require(method["method_role"] in ROLES, "invalid method_role")
        roles.add(method["method_role"])
        require(method["support_status"] in ("planned", "implemented", "unsupported"), "invalid support_status")
        require(method["execution_mode"] in MODES, "invalid execution_mode")
        string_list(method["adaptation_steps"], "adaptation_steps")
        if method["execution_mode"] == "native_frozen":
            require(not method["adaptation_steps"], "native_frozen registry cannot include adaptation")
        if method["execution_mode"] == "adapted":
            require(bool(method["adaptation_steps"]), "adapted registry requires steps")
        text(method["entrypoint"], "entrypoint", nullable=method["support_status"] == "planned")
        text(method["reason"], "reason", nullable=method["support_status"] == "implemented")
        if submission:
            require(method["support_status"] != "planned", "planned method is not complete")
            if method["method_role"] == "classical_reference":
                require(method["support_status"] == "implemented", "classical baseline must be implemented")
    require({"classical_reference", "pfn_adapter"} <= roles, "classical reference and PFN adapter are both required")

def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent)
    parser.add_argument("--mode", choices=("scaffold", "submission"), default="scaffold")
    parser.add_argument("--result", type=Path)
    parser.add_argument("--analysis", type=Path)
    parser.add_argument("--include-analysis", action="store_true", help="Validate optional Layer A as well")
    args = parser.parse_args(argv)
    root, errors = args.root.resolve(), []
    for relative in REQUIRED_FILES:
        p = root/relative
        if not p.is_file() or p.stat().st_size == 0:
            errors.append("missing/empty required file: "+relative)
    checks = [
        ("data/schema.csv", lambda: check_csv(root/"data/schema.csv")),
        ("solution/methods.json", lambda: validate_methods(read_json(root/"solution/methods.json"), args.mode == "submission")),
        ("result schema", lambda: require(read_json(root/"evaluation/result.schema.json")["properties"]["schema_version"]["const"] == VERSION, "schema/checker version mismatch")),
    ]
    outputs = [("B", args.result or root/"reports/result.json")]
    if args.include_analysis or args.analysis:
        outputs.append(("A", args.analysis or root/"reports/analysis.json"))
    for layer, path in outputs:
        checks.append((str(path), lambda layer=layer, path=path: validate_output(read_json(path), layer, args.mode == "submission")))
    for label, check in checks:
        try:
            check()
        except (OSError, ValueError, TypeError, KeyError, OverflowError, csv.Error) as exc:
            errors.append(label+": "+str(exc))
    if args.mode == "submission":
        excluded = {"README.md", "CONTRIBUTING.md", "validate_submission.py", "evaluation/check_contract.py", "evaluation/result.schema.json"}
        paths = [root/p for p in REQUIRED_FILES if p not in excluded]
        if args.include_analysis or args.analysis:
            paths.append(args.analysis or root/"reports/analysis.json")
        for path in paths:
            if path.is_file() and re.search(r"\bTODO\b", path.read_text(encoding="utf-8-sig")):
                errors.append("unresolved placeholder: "+str(path.relative_to(root) if path.is_relative_to(root) else path))
    print("STRUCTURAL CHECK ONLY: no execution, YAML semantics, science or acceptance.")
    if errors:
        print("FAIL ({} issue(s))".format(len(errors)))
        for error in errors:
            print("- "+error)
        return 1
    print("PASS: required files, registry, CSV and requested scalar output contracts (0.2.0).")
    if args.mode == "scaffold":
        print("Illustrative outputs and unfinished templates are permitted in scaffold mode.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
