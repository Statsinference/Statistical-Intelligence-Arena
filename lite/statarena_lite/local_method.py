"""Load a local estimator and produce predictions for a Lite split."""

import csv
import importlib.util
import math
import sys
from contextlib import contextmanager
from pathlib import Path

import numpy as np


PREDICTION_COLUMNS = ("table_id", "estimate", "ci_lower", "ci_upper")


@contextmanager
def _load_estimator(path: Path):
    path = path.resolve()
    if not path.is_file() or path.suffix != ".py":
        raise ValueError(f"Method must be a Python file: {path}")

    module_name = "_statarena_lite_local_method"
    spec = importlib.util.spec_from_file_location(module_name, path)
    module = importlib.util.module_from_spec(spec)
    previous_module = sys.modules.get(module_name)
    previous_path = sys.path.copy()
    sys.modules[module_name] = module
    sys.path.insert(0, str(path.parent))
    try:
        try:
            spec.loader.exec_module(module)
        except Exception as error:
            raise RuntimeError(f"Could not load method {path}: {error}") from error
        estimate = getattr(module, "estimate", None)
        if not callable(estimate):
            raise ValueError(f"Method must define a callable estimate(study): {path}")
        yield estimate
    finally:
        sys.path[:] = previous_path
        if previous_module is None:
            sys.modules.pop(module_name, None)
        else:
            sys.modules[module_name] = previous_module


def _observations(path: Path) -> dict:
    if path.suffix == ".npz":
        with np.load(path, allow_pickle=False) as arrays:
            return {name: arrays[name] for name in arrays.files}

    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        columns = {name: [] for name in reader.fieldnames or ()}
        for row in reader:
            for name, values in columns.items():
                values.append(float(row[name]))
    return {name: np.asarray(values) for name, values in columns.items()}


def _proximal_queries(split_dir: Path) -> dict:
    with (split_dir / "queries.csv").open(encoding="utf-8", newline="") as handle:
        return {
            row["table_id"]: {name: float(value) for name, value in row.items() if name != "table_id"}
            for row in csv.DictReader(handle)
        }


def _cate_query(split_dir: Path, table_id: str) -> dict:
    path = split_dir / "queries" / f"{table_id}.csv"
    with path.open(encoding="utf-8", newline="") as handle:
        row = next(csv.DictReader(handle))
    return {name: float(value) for name, value in row.items()}


def run_local_method(path: Path, domain: str, starter: Path, split: str, output: Path) -> None:
    """Call estimate(study) once for each observed table and write the predictions."""
    split_dir = starter / split
    extension = "npz" if domain in {"iv", "did"} else "csv"
    paths = sorted((split_dir / "tables").glob(f"*.{extension}"))
    if not paths:
        raise ValueError(f"No {domain} tables found for the {split} split: {split_dir}")

    queries = _proximal_queries(split_dir) if domain == "proximal" else {}
    predictions = []
    with _load_estimator(path) as estimate:
        for table in paths:
            table_id = table.stem
            try:
                study = _observations(table)
                study.update(table_id=table_id, domain=domain)
                if domain == "proximal":
                    study["query"] = queries[table_id]
                elif domain == "cate":
                    study["query"] = _cate_query(split_dir, table_id)
                point, lower, upper = (float(value) for value in estimate(study))
                if not all(map(math.isfinite, (point, lower, upper))):
                    raise ValueError("estimate(study) returned a non-finite value")
                if lower > upper:
                    raise ValueError("The lower confidence limit exceeds the upper limit")
            except Exception as error:
                raise RuntimeError(f"Could not estimate {domain} table {table_id}: {error}") from error
            predictions.append((table_id, point, lower, upper))

    with output.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(PREDICTION_COLUMNS)
        writer.writerows(predictions)
