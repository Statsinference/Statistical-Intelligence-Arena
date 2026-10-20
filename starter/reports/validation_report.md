# Validation and evidence report — protocol v0.3

**Scientific status: NOT RUN / NOT IMPLEMENTED.** The package contains templates, illustrative output records and structural checks only. No training, generator or benchmark experiment has been run by this release.

## Specification readiness

TODO: reviewed DGP catalog/cards and exact source locators; adaptations and independent truth checks; task-conditional Pi_k and split/exposure manifest; model/teacher/loss/head/budget plan; frozen fixed-DGP/n/R/query/method/CI plan; named reviewers and rights.

## Evidence required after implementation and execution

- Source, code, environment, DGP/configuration and checkpoint hashes.
- Full per-attempt result records, including unsupported/abstained/failed/not_identified cases and infrastructure retries.
- Coverage with MC uncertainty at each fixed DGP/n/target/scope; valid-output and all-attempt denominators; availability and predeclared failure gate.
- Length comparisons only after validity/availability gates, preserving infinite intervals and inconclusive results.
- Paired method differences with experiment-level uncertainty; correlated queries are not independent replicates.
- Training/teacher, load and warmed end-to-end costs; observed-label allocation and tuning/calibration budget.
- Baseline justification, source/truth controls, data leakage checks, reviewer dispositions and independent rerun.

## Current illustrative artifacts

result.json and analysis.json are illustrative contract examples, not execution evidence. prediction_set.json is a legacy compatibility example for the unchanged schema; general future-response prediction is outside the current six-family track. Never relabel these as benchmark_run without actual execution.

## Structural checks recorded on 18 October 2026

- validate_submission.py --mode scaffold --include-analysis: PASS.
- evaluation/check_contract.py: PASS, 47 positive/negative Python contract fixtures. Optional JSON Schema cross-check was skipped because jsonschema is not installed.
- validate_submission.py --mode submission: expected FAIL, 20 issues from illustrative records/registry and unfinished placeholders.

No generator, training, estimator or statistical benchmark was executed. Structural success cannot certify YAML semantics, identification, coverage, source fidelity or acceptance. TODO: replace the scientific-evidence sections with actual execution evidence and review findings when available.
