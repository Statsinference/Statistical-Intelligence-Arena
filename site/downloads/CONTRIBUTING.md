# Contribute to Statistical Inference Arena

Discussion protocol v0.3, 18 October 2026. Output schema 0.2.0. No submission service, trained demo or benchmark runner is deployed.

## First milestone: source-grounded DGPs

Choose one of exactly six families: ate, cate, mediation, iv, proximal, did_sc. Follow demo/README.md for the planned mediation example. A real-data application is optional. A classical mechanism requires a verified primary source and exact source locator; a new toy example is allowed when labeled original/illustrative rather than attributed to a nonexistent paper.

Before implementing an estimator, complete a DGP card and catalog entry: original equations, adaptation, parameters, estimand/truth, independent sampling unit, license and version. Check truth through an independent derivation or implementation, not a second wrapper around the same code.

## DGP, training-distribution and evaluation sequence

1. **DGP catalog:** identify and review each mechanism; distinguish the source design from your adaptation.
2. **Hyperdistribution:** register task-conditional Pi_k with one target ID, role mapping and query contract, mechanism weights, parameter laws/constraints, truth/teacher construction and splits. The first demo is mediation only. Future joint training requires explicit task conditioning and compatible output heads, never six unlabeled scalar targets.
3. **Small PFN plan:** specify the reference demo architecture/checkpoint, supervision, losses, episode and context-size budget, seeds and stopping rule. configs/train.yaml is planned and not implemented. Mean/variance heads are optional method choices; no theorem is inherited merely by choosing them.
4. **Frozen evaluation plan:** select fixed mechanisms, independent paired repetitions, sample sizes, CI methods, MC uncertainty and validity gate before results. Held-out mechanisms and parameter regions are distinct from seed holdout.
5. **Implementation and execution:** implement the pipeline, review its DGP, truth rule and configurations, then begin training/evaluation under the frozen design. This release supplies specifications only.
6. **Evidence and review:** provide actual outputs, full failure/cost accounting, AI issue dispositions, scientific review and an independent clean rerun.

The project plans a small reference PFN demo. Contributors do not have to retrain a foundation model for each task. A suitable existing checkpoint may be reused with its provenance and support limits. An unsupported target needs an explicit unsupported adapter response, never substitution of ATE for NIE or CATE.

## Fixed package checklist

- task.yaml, task.md, scientific_spec.md: task identity, population, target, identifying assumptions, observed inputs, scope, truth, budgets and limits.
- dgps/catalog.csv, dgps/README.md, DGP cards: verified sources, exact equations, adaptations, parameterization, truth and versions.
- hyperdistribution.yaml: mixture, constraints, task conditioning, teacher, exposure and train/dev/evaluation separation.
- configs/train.yaml: planned or implemented status, model, supervision, episodes/n/seeds, offline budget, checkpoint metadata and stopping policy.
- configs/evaluate.yaml and evaluation/protocol.yaml: fixed-DGP plan, paired R/n/seeds, CI methods, MC intervals, coverage basis, denominator and availability/failure gate.
- demo/README.md: a reproducible student-facing workflow with honest implementation status and intended interfaces.
- data/, environment/: generator/access implementation, dictionary, rights, dependence, hashes and pinned execution environment.
- solution/: runnable classical/reference baseline and PFN interface registry with exact versions and support limits.
- reports/, review/, LICENSE.md, PROVENANCE.md: executed evidence when available, AI issue log, independent scientific/reproduction review and rights.

The supplied files describe a plan. Replace placeholders with verified artifacts before submission. Passing structural checks does not implement, execute or accept a contribution.

## Statistical rules

At each fixed DGP, repeat the full permitted method on independent experiments. For CATE, register fixed x or group definitions and query IDs; correlated queries from the same dataset are not independent MC repetitions. For panel/network/cluster designs, identify the independent experiment and the fixed versus redrawn quantities.

Register nominal level, tolerance, MC confidence method/level, coverage_basis, denominator, zero-valid-output policy and availability/failure gate. Keep all attempts. Conditional coverage among selectively returned intervals cannot alone establish validity. Compare length only among methods passing the same target/scope/budget gate. Report overcoverage, infinite lengths and availability. No universal R, cutoff or global ranking is imposed.

Match total observed labels and disclose allocations to context, calibration, tuning and other held-out labels. Separate offline training, load and warmed end-to-end deployment cost. Oracle effects/nuisances may construct offline training labels under a declared simulator, but are excluded from deployment inputs and hidden evaluation feedback.

## Family-specific boundaries

- ATE/CATE: specify the intervention and population; for CATE fix the conditioning set and query rather than silently averaging into ATE.
- Mediation: state treatment levels, NDE/NIE definitions, mediator timing and the assumptions needed by the chosen identification route.
- IV: distinguish LATE/its complier population from ATE or a structural coefficient. Weak identification may require unbounded or disconnected parameter confidence sets; the latter need an output extension.
- Proximal: declare proxy roles, bridge/existence/completeness conditions and sensitivity to weak proxies.
- DiD: declare panel or repeated-cross-section sampling, treatment timing, the parallel-trends statement and no-anticipation conditions.
- Synthetic control: separately declare donors, pre/post windows, contamination, counterfactual model and dependence. It does not automatically share DiD assumptions.

General prediction sets remain a schema compatibility capability, not a current family/track. Higher-order accuracy is not a Phase-1 acceptance condition.

## Review and checks

AI pre-review precedes human scientific review. Reviewers can be from the same team, with independence from evaluated-model development and conflicts documented. A second person independently reruns the frozen implementation before acceptance.

```sh
python validate_submission.py --mode scaffold
python evaluation/check_contract.py
python validate_submission.py --mode submission
```

Only structural checks are executable here. YAML scientific semantics, provenance, code, rights and statistical evidence require separate review. Submission mode rejects this template's planned methods, illustrative outputs and TODOs.
