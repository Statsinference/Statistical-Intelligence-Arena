# Statistical Inference Arena: contributor starter

Discussion protocol **v0.3**, 18 October 2026. Output JSON schema remains **0.2.0**.
The working name is temporary; legacy CausalTaskBench paths remain compatible.

**Current delivery: documentation, planned configurations, illustrative output records and format checkers only. No generator, trained model, training runner, statistical evaluator or measured benchmark result is supplied. Training and evaluation remain subsequent implementation work.**

## Current scope

Exactly six task families are in the current protocol: **ate, cate, mediation, iv, proximal, did_sc**. The last family contains two distinct design branches with separate identification and uncertainty contracts. General future-response prediction is not a current track. The schema retains prediction_set solely for compatibility.

Layer B (method-level numerical evaluation) comes first. Layer A (complete analysis) remains optional and separately reviewed. A linear mechanism can be an illustrative DGP within one of these six families; it does not create a seventh family.

## Student workflow

1. Read [CONTRIBUTING.md](CONTRIBUTING.md) and the planned [mediation demo guide](demo/README.md).
2. Register source-grounded DGPs in [dgps/catalog.csv](dgps/catalog.csv), using [dgps/README.md](dgps/README.md). Record exact equations, original versus adapted choices, truth and provenance.
3. Define task-conditional Pi_k in [hyperdistribution.yaml](hyperdistribution.yaml): one target ID, role mapping and query contract, mechanism mixture, parameter ranges, constraints, teacher and public/held-out partitions. The first demo is single-family mediation; future joint training requires explicit task conditioning and compatible output heads.
4. Specify a small PFN experiment in [configs/train.yaml](configs/train.yaml). It is a plan, not runnable training. A contributor may reuse a suitable frozen checkpoint instead of retraining; disclose the same target and information limits.
5. Prespecify fixed-DGP confidence-interval evaluation in [configs/evaluate.yaml](configs/evaluate.yaml), using [evaluation/protocol.yaml](evaluation/protocol.yaml) as the scientific policy contract.
6. Implement the reviewed design, then supply the actual baseline, PFN interface, execution evidence, scientific review and independent rerun.

A classical published DGP is a source, not evidence that a test mechanism was unseen by pretraining. New random seeds mean new samples, not new mechanisms. This release contains an empty catalog and a clearly uncited illustrative mediation card; it does not claim to have curated classical sources.

## Available commands

With Python 3.9+ from this directory:

```sh
python validate_submission.py --mode scaffold
python evaluation/check_contract.py
python validate_submission.py --mode submission
```

The first two should pass. Submission mode must reject this unfinished package. Add --include-analysis only when Layer A is included. The checker uses the standard library and checks required-file presence, the data dictionary, registry and JSON consistency. It does not parse YAML, evaluate its semantics, run a model, verify DGP equations or grant acceptance.

## Output compatibility

The unchanged schema-0.2.0 contract separates target_object from uncertainty.type and uncertainty.coverage_scope.

- target_object: parameter_ci / mean_ci / prediction_set. In current causal tasks, CATE at a fixed x is a causal parameter_ci query unless an explicitly justified extension changes that contract; it is not automatically an ordinary regression mean.
- uncertainty.coverage_scope: marginal / fixed_query / group / pointwise / simultaneous. The scalar core rejects ok simultaneous outputs.
- uncertainty.type: none / standard_error / confidence_interval / credible_interval / prediction_set. Credible intervals retain their label when frequentist coverage is evaluated.
- Parameter/mean intervals use interval: {lower, upper}. One connected interval may be unbounded. Empty or disconnected parameter confidence sets, including weak-IV inversions, need an extension. Never relabel them prediction sets or silently take a convex hull.
- The legacy prediction_set contract uses intervals: [[lower, upper], ...], including empty/disconnected sets. This does not add a prediction track to v0.3.
- Endpoints are finite numbers or strings -inf/+inf. JSON NaN/Infinity are invalid. Query/group identifiers are required when the declared scope needs them.
- Statuses remain ok / unsupported / abstained / failed / not_identified. Non-ok outputs retain IDs and reasons with null numerical outputs.
- Illustrative records in reports/ are not runs. Only actual execution produces artifact_kind: benchmark_run.

Native frozen output, adapted procedures and per-dataset refitting remain separate. Match total observed-label budgets, disclose context/calibration/tuning allocations, retain all attempted runs, and specify the coverage denominator and availability/failure gate before examining results.
