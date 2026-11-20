"""Run and score StatArena's public starter releases."""

import argparse
import json
import os
from pathlib import Path
import subprocess
import sys
from tempfile import TemporaryDirectory

from .datasets import DATASETS, prepare
from .local_method import run_local_method


SPLITS = ("train", "dev", "test")
ATE_CATE = ("ate", "cate")
POSITIONAL_SCRIPTS = ("iv", "did")


def starter_command(starter: Path, *arguments: str) -> str:
    result = subprocess.run(
        [sys.executable, *arguments],
        cwd=starter,
        capture_output=True,
        text=True,
    )
    if result.returncode:
        detail = result.stderr.strip() or result.stdout.strip()
        raise RuntimeError(f"{arguments[0]} exited with code {result.returncode}. {detail}")
    return result.stdout


def run_baseline(domain: str, starter: Path, split: str, output: Path) -> None:
    tables = f"{split}/tables"
    if domain in POSITIONAL_SCRIPTS:
        output.write_text(starter_command(starter, "baseline.py", tables), encoding="utf-8")
        return

    arguments = ["baseline.py", "--tables", tables, "--output", str(output)]
    if domain in ATE_CATE:
        arguments.extend(["--task", domain.upper()])
    elif domain == "proximal":
        arguments.extend(["--queries", f"{split}/queries.csv"])
    starter_command(starter, *arguments)


def score_predictions(
    domain: str,
    starter: Path,
    split: str,
    predictions: Path,
    timings: Path | None = None,
) -> dict:
    if domain in POSITIONAL_SCRIPTS:
        arguments = ["score.py", f"{split}/truth.csv", str(predictions)]
    else:
        truth_name = f"truth_{domain}.csv" if domain in ATE_CATE else "truth.csv"
        arguments = ["score.py", "--truth", f"{split}/{truth_name}", "--predictions", str(predictions)]
        if timings is not None and timings.is_file() and domain in ATE_CATE:
            arguments.extend(["--timings", str(timings)])
    results = json.loads(starter_command(starter, *arguments))
    if domain in ATE_CATE:
        return {
            "bias": results["Bias"],
            "rmse": results["RMSE"],
            "coverage": results["Coverage"],
            "mean_interval_length": results["Length"],
            "variance": results["Variance"],
            "variance_definition": "Within-configuration replicate variance",
            **({"mean_time_seconds": results["Time"]} if results.get("Time") is not None else {}),
        }
    if domain == "mediation":
        results["coverage"] = results.pop("coverage_95")
    return results


def run(args: argparse.Namespace, starter: Path) -> tuple[Path, dict]:
    if args.method == "baseline":
        method = None
        name = "baseline"
    else:
        method = Path(args.method).expanduser().resolve()
        if method.suffix != ".py" or not method.is_file():
            raise ValueError("--method expects 'baseline' or the path to a Python file.")
        name = method.stem

    destination = args.output or Path("lite-results") / f"{args.domain}-{args.split}-{name}.csv"
    destination = destination.expanduser().resolve()
    if destination == method or destination.is_relative_to(starter):
        raise ValueError("Write predictions outside the cached starter and the method source.")
    destination.parent.mkdir(parents=True, exist_ok=True)
    with TemporaryDirectory(dir=destination.parent) as temp:
        predictions = Path(temp) / "predictions.csv"
        if method is None:
            run_baseline(args.domain, starter, args.split, predictions)
        else:
            run_local_method(method, args.domain, starter, args.split, predictions)
        timings = predictions.with_suffix(".csv.timings.json") if method is None else None
        metrics = score_predictions(args.domain, starter, args.split, predictions, timings)
        predictions.replace(destination)
    return destination, metrics


def main() -> int:
    parser = argparse.ArgumentParser(prog="statarena-lite", description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("list", help="List supported domains")
    locate = commands.add_parser("prepare", help="Download a public starter and print its directory")
    runner = commands.add_parser("run", help="Run a baseline or local Python method, then score its predictions")
    scorer = commands.add_parser("score", help="Score a predictions CSV")
    for command in (locate, runner, scorer):
        command.add_argument("--domain", required=True, choices=DATASETS)
    for command in (runner, scorer):
        command.add_argument("--split", choices=SPLITS, default="dev")
    runner.add_argument("--method", default="baseline", help="baseline or path to a local Python file")
    runner.add_argument("--output", type=Path, help="Destination CSV (default: lite-results/<domain>-<split>-<method>.csv)")
    scorer.add_argument("--predictions", type=Path, required=True)
    args = parser.parse_args()

    if args.command == "list":
        print("\n".join(DATASETS))
        return 0

    dataset = DATASETS[args.domain]
    cache = Path(os.environ.get("STATARENA_LITE_CACHE", Path.home() / ".cache" / "statarena-lite"))
    try:
        starter = prepare(dataset, cache).resolve()
        if args.command == "prepare":
            print(starter)
            return 0
        if args.command == "run":
            predictions, metrics = run(args, starter)
        else:
            predictions = args.predictions.expanduser().resolve()
            if not predictions.is_file():
                raise ValueError(f"Predictions CSV does not exist: {predictions}")
            metrics = score_predictions(args.domain, starter, args.split, predictions)
        print(json.dumps({
            "domain": args.domain,
            "split": args.split,
            "dataset_sha256": dataset.sha256,
            "predictions": str(predictions),
            "metrics": metrics,
        }, indent=2, allow_nan=False))
    except (OSError, ValueError, RuntimeError) as exc:
        parser.exit(1, f"statarena-lite: {exc}\n")
    return 0
