#!/usr/bin/env python3
"""Contract fixtures only. Toy values below are not estimator runs or benchmark evidence."""
from copy import deepcopy
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.dont_write_bytecode = True
sys.path.insert(0, str(ROOT))
from validate_submission import read_json, loads_strict, validate_output, validate_methods

BASE = read_json(ROOT / "reports/result.json")
SCHEMA = read_json(ROOT / "evaluation/result.schema.json")
passed = 0

def check(name, data, valid, layer="B", schema_check=False):
    global passed
    try:
        validate_output(data, layer)
    except (ValueError, TypeError, KeyError, OverflowError):
        if valid:
            raise AssertionError("Valid fixture rejected: " + name)
    else:
        if not valid:
            raise AssertionError("Invalid fixture accepted: " + name)
    if schema_check:
        try:
            import jsonschema
        except ImportError:
            pass
        else:
            accepted = not list(jsonschema.Draft202012Validator(SCHEMA).iter_errors(data))
            assert accepted == valid, "JSON Schema differs on shape fixture: " + name
    passed += 1

def mutate(base, update):
    value = deepcopy(base)
    update(value)
    return value

def expect_error(name, fn):
    global passed
    try:
        fn()
    except (ValueError, TypeError, KeyError, OverflowError):
        passed += 1
        return
    raise AssertionError("Invalid fixture accepted: " + name)

def main():
    check("unsupported illustrative shape", BASE, True, schema_check=True)
    check("optional analysis example", read_json(ROOT/"reports/analysis.json"), True, "A", True)
    check("prediction task unsupported shape", read_json(ROOT/"reports/prediction_set.json"), True, schema_check=True)
    ci = deepcopy(BASE)
    ci.update(status="ok", status_reason=None, estimate=0.2)
    ci["uncertainty"].update(type="confidence_interval", level=0.95, interval={"lower":-0.1,"upper":0.5}, standard_error=0.15, method="toy contract fixture")
    check("finite parameter CI", ci, True, schema_check=True)
    check("unbounded weak-identification-compatible CI", mutate(ci,lambda d:d["uncertainty"].update(interval={"lower":"-inf","upper":"+inf"})), True, schema_check=True)
    mean = deepcopy(ci)
    mean.update(target_object="mean_ci", target_id="mean_at_x0", query_id="x0")
    mean["uncertainty"]["coverage_scope"]="fixed_query"
    check("mean at fixed query", mean, True, schema_check=True)
    point = deepcopy(ci)
    point["uncertainty"] = deepcopy(BASE["uncertainty"])
    check("point-only under requested CI task", point, True, schema_check=True)
    se = deepcopy(point)
    se["uncertainty"].update(type="standard_error",standard_error=0.1,method="toy SE")
    check("standard error without interval", se, True, schema_check=True)
    pred = deepcopy(ci)
    pred.update(target_object="prediction_set",target_id="future_y",estimate=None)
    pred["uncertainty"].update(type="prediction_set",interval=None,standard_error=None,intervals=[[-2,-1],[1,2]])
    check("disjoint response set without point estimate", pred, True, schema_check=True)
    check("empty set retained", mutate(pred,lambda d:d["uncertainty"].update(intervals=[])), True, schema_check=True)
    check("unbounded set components", mutate(pred,lambda d:d["uncertainty"].update(intervals=[["-inf",-1],[1,"+inf"]])), True, schema_check=True)
    check("group set",mutate(pred,lambda d:(d.update(group_id="g1"),d["uncertainty"].update(coverage_scope="group"))),True,schema_check=True)
    check("simultaneous explicitly unsupported",mutate(BASE,lambda d:d["uncertainty"].update(coverage_scope="simultaneous")),True,schema_check=True)
    bad = [
        ("missing target object",lambda d:d.pop("target_object")),
        ("missing coverage scope",lambda d:d["uncertainty"].pop("coverage_scope")),
        ("old schema version",lambda d:d.update(schema_version="0.1.0")),
        ("unknown scope",lambda d:d["uncertainty"].update(coverage_scope="conditional")),
        ("future Y set mislabeled as parameter CI",lambda d:d.update(target_object="parameter_ci")),
        ("missing set intervals",lambda d:d["uncertainty"].pop("intervals")),
        ("CI field in prediction set",lambda d:d["uncertainty"].update(interval={"lower":0,"upper":1})),
        ("simultaneous without extension",lambda d:d["uncertainty"].update(coverage_scope="simultaneous")),
        ("missing fixed query ID",lambda d:d["uncertainty"].update(coverage_scope="fixed_query")),
        ("missing group ID",lambda d:d["uncertainty"].update(coverage_scope="group")),
        ("non-ok claims output",lambda d:d.update(status="failed",status_reason="toy failure")),
        ("wrong level",lambda d:d["uncertainty"].update(level=1)),
    ]
    for name, fn in bad:
        check(name,mutate(pred,fn),False,schema_check=True)
    check("set field in CI",mutate(ci,lambda d:d["uncertainty"].update(intervals=[[0,1]])),False,schema_check=True)
    check("null parameter estimate",mutate(ci,lambda d:d.update(estimate=None)),False,schema_check=True)
    check("native frozen has adaptation",mutate(ci,lambda d:d["provenance"].update(execution_mode="native_frozen")),False,schema_check=True)
    for name, intervals in [
        ("reversed component",[[2,1]]),("overlap",[[0,2],[1,3]]),("touching components",[[0,1],[1,2]]),
        ("unordered components",[[2,3],[0,1]]),("wrong infinity direction",[["+inf","+inf"]]),
        ("boolean endpoint",[[False,1]]),("nonfinite numeric endpoint",[[0,float("inf")]])
    ]:
        check(name,mutate(pred,lambda d,iv=intervals:d["uncertainty"].update(intervals=iv)),False)
    check("reversed CI",mutate(ci,lambda d:d["uncertainty"].update(interval={"lower":2,"upper":1})),False)
    check("unsafe evidence path",mutate(ci,lambda d:d.update(evidence=["../truth.json"])),False)
    check("nonfinite estimate",mutate(ci,lambda d:d.update(estimate=float("nan"))),False)
    check("negative cost",mutate(ci,lambda d:d["runtime"].update(load_seconds=-1)),False,schema_check=True)
    for name, raw in [("JSON NaN",'{"x":NaN}'),("JSON Infinity",'{"x":Infinity}'),("overflow number",'{"x":1e309}'),("duplicate key",'{"x":1,"x":2}')]:
        expect_error(name,lambda raw=raw:loads_strict(raw))
    registry=read_json(ROOT/"solution/methods.json")
    validate_methods(registry)
    expect_error("missing PFN adapter",lambda:validate_methods({**registry,"methods":registry["methods"][:1]}))
    expect_error("planned registry submission",lambda:validate_methods(registry,True))
    ready=deepcopy(registry)
    ready["artifact_kind"]="contribution_registry"
    for method in ready["methods"]:
        method["model_version"]="toy-contract-version"
        method["entrypoint"]="toy-contract-command-not-executed"
        method["reason"]="toy unsupported capability" if method["method_role"]=="pfn_adapter" else None
        method["support_status"]="unsupported" if method["method_role"]=="pfn_adapter" else "implemented"
    validate_methods(ready,True)
    global passed
    passed += 2
    try:
        import jsonschema
    except ImportError:
        print("Optional JSON Schema cross-check skipped (jsonschema not installed); Python fixtures all executed.")
    else:
        jsonschema.Draft202012Validator.check_schema(SCHEMA)
        print("JSON Schema 2020-12 syntax and selected shape fixtures also checked.")
    print("PASS: {} positive/negative contract checks; no estimator or statistical experiment executed.".format(passed))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
