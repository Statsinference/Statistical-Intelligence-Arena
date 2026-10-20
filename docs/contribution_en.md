# Statistical Inference Arena: Contribution Requirements

**Protocol v0.3 · 2026-10-18 · Output schema 0.2.0 · Draft specification**

Working project name: Statistical Inference Arena. Legacy CausalTaskBench filenames are retained for compatibility. This is the complete English contribution protocol; the full student workflow is included in Chapter 8.

## 1. Purpose, first release and scope

The first release evaluates **confidence intervals for causal estimands**, with point estimation, availability and cost reported alongside them. The planned development sequence is: register classical data-generating processes (DGPs), define a training hyperdistribution, build a small prior-data fitted network (PFN) baseline, then evaluate its intervals on independent repetitions at fixed DGPs. This is a plan for constructing and evaluating methods; it does not presume that PFNs outperform classical estimators.

The six task categories are **ATE, CATE, mediation, instrumental variables, proximal causal inference, and DID/synthetic control**. DID and synthetic control share one collection category but require distinct scientific and uncertainty contracts. Start with one precisely specified task rather than assuming one model already supports every category.

Phase 1 prioritizes **Layer B: method evaluation**: roles, estimand, identification conditions, observed inputs and budgets are supplied. **Layer A: complete scientific analysis** is optional and may be added later with separate prompts, permissions, outputs and review. A method's numerical performance does not establish complete-analysis capability.

Current status: protocol and contributor scaffolding. The mediation reference demo, end-to-end training runner and statistical evaluator still require implementation and review. This document records no trained checkpoint, successful experiment or accepted contribution. No training is launched as part of this revision.

## 2. Scientific contract for the six task categories

Each task fixes its estimand, population, scale, intervention contrast, observation/assignment units, dependence, and identification assumptions before selecting a method. Record which roles and scientific facts are supplied; an observational table alone does not determine them. Pretreatment predictors are not automatically confounders.

| Category | Required target and design specification |
| --- | --- |
| ATE | Define `E[Y(1)-Y(0)]`, the target population and treatment versions. State consistency, relevant exchangeability, positivity and interference conditions; specify sampling weights or selection if applicable. |
| CATE | Define `tau(x)=E[Y(1)-Y(0) given X=x]`, the conditioning variables and a fixed query or prespecified query grid/distribution. Record support/overlap and smoothness or structural assumptions used by the estimator and its interval. A collection of pointwise intervals is not a simultaneous band. |
| Mediation | Define `NIE=E[Y(1,M(1))-Y(1,M(0))]` and complementary `NDE=E[Y(1,M(0))-Y(0,M(0))]`. State timing, consistency, treatment and mediator-outcome exchangeability, the required cross-world assumptions, treatment positivity and mediator support. The simple natural-effect route excludes treatment-induced mediator-outcome confounding. Treatment randomization alone is insufficient. |
| IV | Specify the instrument, treatment and outcome. Distinguish LATE for a declared complier population from ATE or a structural coefficient. State relevance, exclusion, instrument exogeneity and monotonicity where needed. Record instrument strength. Weak-IV-valid confidence sets can be unbounded or disconnected. |
| Proximal | Specify treatment-inducing and outcome-inducing proxy roles, latent-confounding assumptions, the bridge equation, existence/completeness and relevant positivity/integrability conditions. Define the effect functional recovered by the bridge; ordinary covariate adjustment is not a substitute. |
| DID / synthetic control | DID: define group-time or aggregate ATT, treatment timing, comparison group, no anticipation, parallel trends and any staggered-adoption restrictions. Synthetic control: define the treated-unit/time target, donor eligibility, counterfactual model and pre/post periods. Record within-unit and temporal dependence, spillovers and the assignment or sampling basis for inference. Do not reuse a generic iid interval without justification. |

The main track requests `target_object: parameter_ci` for causal effect parameters. The retained `mean_ci` format can describe an explicitly separated conditional-mean subtask. Future-response `prediction_set` outputs remain schema-compatible but are **outside this first CI comparison**.

Fix `coverage_scope` as `marginal`, `fixed_query`, `group`, `pointwise` or `simultaneous`, and write its probability statement. For a fixed-query CATE interval, the query is held fixed while datasets are repeated. A grid evaluation must specify each query and any aggregation weights; simultaneous coverage needs a versioned output/evaluator extension.

Use exact analytic truth or a numerical oracle with quantified approximation error for parameter-coverage evaluation. Real-data reference estimates are not exact truths. Semisynthetic tasks must distinguish a fixed empirical covariate pool from a superpopulation target. An assumption-violation probe must be labeled as such; a simulator's known causal target does not make it identifiable from the method's observed inputs.

**First pilot: an explicitly illustrative mediation mechanism**

The starter's `dgps/cards/mediation_illustrative.md` is a proposed teaching example, with no external-paper attribution and no implemented generator. It uses the temporal order X, A, M, Y:

```text
X ~ N(0,1)
A given X ~ Bernoulli(expit(c0 + cX*X))
M = a0 + aA*A + aX*X + eM
Y = b0 + bA*A + bM*M + bAM*A*M + bX*X + eY
NIE = aA*(bM + bAM)
NDE = bA + bAM*a0
```

These formulas assume independent mean-zero errors, the declared causal model and E[X]=0. For another population, the NDE is `bA + bAM*(a0 + aX*E[X])`. Specify noise distributions, coefficients, overlap and sampling units before implementation. The initial task targets NIE; NDE requires a separate target ID and evaluation. Independently verify these formulas and the identification assumptions before using this card as a reference demo. A mediation-specific sample-dependent teacher also needs its own derivation; renaming an ATE teacher is insufficient.

## 3. Register classical DGPs and verify their truth

Begin by collecting established simulation settings from original methodological papers and their official code. A real-data paper is optional; a canonical synthetic setting is a valid first contribution.

For every source, record the exact paper/version and stable URL or DOI, section/page/equation/table, code repository/commit where available, and license/access terms. Trace the simulated variable equations, assignment mechanism, noise laws, coefficient values, dependence, sample sizes and target definition. If the source leaves something ambiguous, record the ambiguity and proposed resolution for scientific review.

Create one `dgps/catalog.csv` row per registered mechanism or configuration family. Link detailed equations and parameters rather than hiding them in a short label. The source ledger must distinguish:

- faithful reproduction of a published mechanism;

- an explicit modification, with each changed equation, parameter or sampling choice;

- a new stress-test mechanism, with its own rationale and validity conditions.

Record variable roles, sampling/assignment units, parameter domains and restrictions, truth class, oracle implementation and its numerical error, and version/hash. Confirm the estimand with an independent derivation or numerical implementation. For mediation, test the treatment reference level and mediator contrast; for IV, check the target population and weak-instrument regime.

Keep nuisance functions, latent variables, potential outcomes and exact effects in the generator/oracle interface. Export only permitted observed variables to the learner. The training supervisor may use oracle information to construct labels; the evaluation service may use it to score outputs. It must not enter the deployed model's input by an unnoticed column or metadata field.

Direct reuse of a public classical mechanism is a transparent starting point, **not a solution to contamination or prior exposure**. Preserve public provenance and disclose possible model exposure; the split policy in Section 4 determines what generalization claim is supportable.

## 4. From the DGP registry to a training hyperdistribution

Define the hyperdistribution **conditional on a task/estimand k**. Let F identify a registered mechanism family for that task and eta its admissible configuration:
```text
(F, eta) given k ~ Pi_k
P = P_(k,F,eta)
n ~ pi_n(. given k,F,eta)
D_n ~ SamplingDesign(P,n)
```
For iid individual sampling, the final step is `D_n ~ P^n`; panel, cluster and network designs require their declared sampler. Pi_k is a distribution over mechanisms/configurations, not the empirical distribution of rows in one table.

In `hyperdistribution.yaml`, specify task/target ID, mechanism mixture weights, parameter ranges and distribution shapes, dependence among parameters, validity constraints/rejection rules, n distribution, unit of sampling, output roles and the label-oracle reference. Mixture weights must sum to one over included mechanism families. A first mediation pilot may use a single task and mechanism family. If constraints reject sampled configurations, record how rejection changes the effective distribution.

For each sampled P, draw one or more datasets and obtain supervision `T_k(P,D_n)`. State whether labels are the fixed target `theta_k(P)`, a sample-dependent estimator/teacher, a variance quantity or an error-distribution target. Record how labels are computed and what randomness they include. Repeated datasets from the same P and draws of new P have separate IDs/seeds. An eventual joint model may add a task mixture, but must condition on task/target and roles or use explicit heads/adapters. Do not mix six estimands into an unlabelled scalar output or assume the table tells the model which effect to estimate.

Freeze three uses: **training** for shared weights, **development** for selecting the hyperdistribution, architecture, teacher and CI rules, and **evaluation** for final comparisons. State permitted public access and model-pretraining exposure. Distinguish held-out seeds, parameter regions, functional mechanisms, source-DGP families and entire task categories. Seed holdout tests new datasets; it does not establish mechanism or task transfer. Specify which sources remain public even when configurations or labels are restricted.

Classic DGPs used in training may also define an explicitly labeled in-distribution evaluation on fresh datasets. Stronger transfer claims require an appropriate holdout and exposure audit. Repeated evaluation feedback must not silently become development data; changing choices after evaluation requires a documented new development cycle and fresh evaluation assets.

## 5. Small-PFN baseline and interval construction

A small-PFN baseline is a planned, budgeted prototype, not an already trained model. Start from a shared architecture/adapter where appropriate, then document the changes required by the task: variable-role encoding, table/context structure, treatment or query specification, target normalization, output head, teacher and loss. Distinct targets need not require distinct backbones, but a shared backbone does not automatically support new estimands. Do not turn a mediator into an ordinary adjustment covariate and call the result NIE.

The training configuration and checkpoint metadata must record: architecture and parameter count; depth, width, attention and input masking where relevant; output/teacher/loss definition; code and DGP registry versions; hyperdistribution hash; model and data seeds; fresh-versus-cached task sampling; number of distinct tasks and presentations; sample-size distribution; optimizer, updates/epochs, batch size, stopping/selection rule; hardware, precision, budget and checkpoint hash. A numerical training-task count is a declared budget, not a universal scientific requirement.

The model receives observed data, explicit task/target ID, role mapping and permitted query metadata, including x for CATE. Oracle quantities can supervise offline training or serve the evaluator, but cannot appear as inference inputs. Freeze the checkpoint and method-selection rule before final evaluation. Shared weights can then be reused across new datasets; per-table nuisance fitting or calibration is an additional online step and must be recorded.

Declare exactly how an interval is produced. Options may include a native model uncertainty output, calibrated estimation-error quantiles, a bootstrap that reruns the relevant procedure, or an influence-function/one-step correction with a variance estimator. Each requires target- and design-specific justification. No particular teacher, FSP objective or EIF construction is mandatory. For nonregular or weakly identified targets, ordinary Wald or bootstrap intervals may be inadequate.

If a variance head is used, define its exact target: the estimator's sampling variance, an asymptotic variance coefficient to be divided by n, a conditional teacher-label variance, or a predictive variance are different objects. State any n scaling and how the point and variance outputs form an interval. A variance head and a positive output transform do not establish coverage.

A learned distribution over training labels is not automatically the frequentist sampling law of the deployed estimator at fixed P. Native credible intervals retain their label; their repeated-sampling coverage is evaluated rather than assumed. Record `native_frozen`, `adapted` or `refit`, and list calibration, correction, resampling or fine-tuning steps. Frozen weights alone do not imply a single forward pass.

Every task supplies a runnable classical/reference baseline and at least one PFN adapter entry. If an existing PFN cannot support the task, return `unsupported` with model/version and a concrete reason. Contributors need not independently pretrain a model for every method; team training can follow a reviewed training plan. Classical-best or PFN-better claims must be limited to the observed regime, budgets and metrics.

## 6. Required package and interface boundaries

Keep the legacy starter paths compatible and add the scientific/training specification files below. A path in this table is a required template or eventual contribution artifact, not evidence that an executable runner already exists.

| Path | Required content |
| --- | --- |
| `task.yaml`, `task.md`, `scientific_spec.md` | Protocol/task version, owners, selected category, target/object/scope, identification, units, permitted inputs and budgets; optional Layer A separately. |
| `dgps/catalog.csv` and linked mechanism specifications | Exact source/page/equation/code version, reproduction differences, rights, parameters, roles, sampling, target/oracle and truth checks. |
| `hyperdistribution.yaml` | Task-conditioned Pi_k hierarchy, mechanism weights, configuration distributions/constraints, n, sampling units, label oracle and train/development/evaluation splits. |
| `configs/train.yaml` | Planned architecture, role/query mapping, teacher/head/loss, seeds, task sampling, optimizer, compute and checkpoint-selection budget. |
| `data/`, `environment/` | Observed-input dictionary, generator/access and hashes; pinned execution environment and bounded commands once implemented. |
| `solution/methods.json`, `methods/` or declared implementation paths | Classical reference, PFN adapter, support status, interval construction, execution mode and actual entrypoints when implemented. |
| `configs/evaluate.yaml`, `evaluation/protocol.yaml`, `evaluation/result.schema.json`, seed ledger | Fixed-DGP/n/query grid, R, paired seeds, CI evaluator, truth join, coverage gate, failure policy and positive/incorrect controls. |
| `reports/`, `review/`, `PROVENANCE.md`, `LICENSE.md` | Actual run outputs/logs/costs when available; AI findings, scientific review, independent rerun, exposure audit, rights and versions. |

Each catalog entry needs stable IDs and links to details; blank fields require an explicit unresolved item. New configuration files do not execute training by themselves. A proposed training interface takes a train config and produces weights plus metadata; a proposed evaluation interface takes frozen methods, fixed DGP configs and a seed ledger and produces per-replicate outputs plus summaries. **Those are interface requirements, not runnable commands supplied by this protocol.**

The existing output schema remains **0.2.0**; protocol version **0.3** does not rename the JSON schema. Each result identifies task/version, mechanism, replicate, method, target, query/group when applicable, status, estimate, uncertainty, diagnostics, evidence, cost and provenance. `uncertainty.coverage_scope` is mandatory, including for point-only or unsupported outputs, and describes the requested scope rather than proving coverage.

The core CI format contains one connected interval, possibly unbounded through `-inf`/`+inf` string endpoints. Empty/disconnected parameter confidence sets, simultaneous bands, vector effects and identified sets require explicit extensions; do not relabel them `prediction_set` or silently take a convex hull. The compatible `prediction_set` type can use disjoint `intervals`, but is outside the main CI track.

An `ok` scalar parameter output needs a finite estimate; point-only outputs use uncertainty `none` and do not enter interval-length comparisons. Non-ok statuses `unsupported`, `abstained`, `failed`, `not_identified` retain reason and IDs with null estimate and uncertainty `none`. JSON NaN/Infinity are rejected. Structure validation is distinct from execution and scientific validation.

## 7. CI evaluation at fixed DGPs

Freeze an evaluation grid of mechanism configurations, n and targets/queries. Within each cell, hold P and its true parameter fixed, generate R independent datasets using the declared sampling/assignment design, and rerun the complete allowed method. Pair methods on the same dataset/seed and, when relevant, the same query grid. A different random P in every repetition measures a mixture-average property, not coverage at a fixed DGP; report that separately.

Prespecify R, seeds, nominal levels, tolerances, tuning rules, timeouts and checkpoint status. Respect the independent unit: clusters, panels or networks may require whole-unit resampling, dependence-aware procedures, or a specified assignment experiment. Do not bootstrap rows merely because the input is tabular. Separate variation from dataset sampling, model-training seeds and numerical truth approximation.

Match **total observed-label budgets** across methods. Disclose context, calibration, tuning and any other held-out allocation; calibration labels are not free extra data. A different-budget comparison must be separately labeled. Classical reference tuning and PFN adaptation need explicit access and compute rules.

Report bias/RMSE, empirical estimator variance, reported variance/SE calibration when supplied, CI coverage and length, availability, failures and cost. A narrow interval with poor coverage is not an improvement. Before results, register `coverage_basis` (`valid_output` or `all_attempt_valid_covering`), its denominator, availability/failure requirements, nominal level, allowed undercoverage tolerance, confidence-bound method/level and gate. Selective abstention cannot pass solely through coverage among successes. No universal cutoff or minimum R is prescribed.

Compare interval lengths only among methods passing the same target/scope coverage gate; show overcoverage and availability alongside length. Insufficient Monte Carlo precision is inconclusive. Report every scheduled attempt, including unsupported, abstained, failed, timeout, nonfinite and infrastructure errors; predeclare retry rules. Retain unbounded intervals in length summaries. No global combined score is defined.

For independent binary repetition indicators, coverage MCSE is approximately `sqrt(p*(1-p)/R)`; p=0.95 and R=1000 gives about 0.0069, a planning example only. Report a prespecified binomial interval or a design-appropriate alternative. For CATE, query-specific coverage can use independent datasets at each fixed query; pooled query indicators within a dataset are dependent. Use independent-replicate/design-aware uncertainty for grid summaries and paired method differences, not an artificial binomial denominator of R times the number of queries.

Separate offline pretraining/development cost, loading and warmed end-to-end per-dataset cost. Warmed time includes preprocessing, fitting, calibration/correction, all model calls, interval construction and output. Record hardware, precision, threads, batching, warmup, repetitions and memory; pure forward time is supplementary. Optional later diagnostics include size distortion, skewness, tail behavior and coverage error versus n. Higher-order rate claims require a target-specific argument and adequate empirical precision.

## 8. Complete student contribution walkthrough

Follow these steps for one selected task. This chapter contains the complete workflow; the separate student walkthrough is a convenient copy. Record planned work as planned, and attach execution evidence only after the relevant implementation exists.

**8.1 Copy the template and claim one task**

Copy the current contributor starter into a separate task directory. Select `ate`, `cate`, `mediation`, `iv`, `proximal` or `did_sc`; choose a specific estimand and scientific owner. The current starter is scaffolding. **A runnable mediation reference demo is still to be implemented**; once reviewed, it can become the worked example for later students. Do not describe copying the template as reproducing a successful experiment. Deliver a short proposal with target, population, available source and planned evidence.

**8.2 Read the original source and register the mechanism**

Read the original method paper and official simulation code, not only a summary. Fill the catalog's source version, page/equation, code commit, rights and reproduction differences. Transcribe the variable equations, parameters, assignment and noise laws, sampling unit and target into a reviewable specification. Mark unresolved details rather than guessing a paper's implementation. If starting from a new canonical example, label it as newly specified rather than falsely attributing it to a paper.

**8.3 Implement observed data and independently check truth**

Implement the registered DGP and a separate truth calculation. Check units, signs, intervention levels and sampling dependence on small deterministic inputs or analytically tractable configurations. Verify source-faithful and modified versions separately. Export only observed variables; keep oracle labels in separate artifacts. Record approximation error and what the independent check shares with the primary implementation. Deliver generator/oracle code plus evidence; this step is not yet a PFN experiment.

**8.4 Configure Pi_k and freeze data-use splits**

Fill `hyperdistribution.yaml` for the selected task: registered mechanism IDs, normalized weights, admissible parameter distributions, constraints, n and sampling design, and label-oracle path. Define separate training, development and evaluation registries/seeds. Declare whether evaluation is in-distribution, parameter-held-out, mechanism-held-out or task-held-out. A small single-family mediation pilot is sufficient as a first plan. Deliver a sampling specification with examples of valid and rejected configurations; no training command is implied.

**8.5 Update roles, target, teacher, head and CI rule**

Map observed columns to the selected causal roles and make task/target ID explicit; add the fixed x or grid for CATE. Specify the teacher in `configs/train.yaml`: true target, reviewed sample-dependent teacher or estimator distillation are different choices. Update the output head/loss and interval construction to match it. Record architecture and masking changes. Check that oracle information is used only for supervision/evaluation. A new target requires a justified adapter, not a renamed output field.

**8.6 Implement the classical reference and PFN adapter**

Register both in `solution/methods.json`. Implement a suitable classical estimator and interval before comparing the PFN. Give both the same target and observed-label budget; disclose calibration/tuning splits and fitting rules. An existing unsupported PFN returns its precise limitation. Specify native-frozen, adapted or refit operation and record every correction or resampling step. Deliver real entrypoints and a pinned environment once implemented; do not fill them with invented commands or results.

**8.7 Run available structural checks, then an implemented smoke test**

The following commands are currently available from the starter directory:
```sh
python validate_submission.py --mode scaffold
python evaluation/check_contract.py
python validate_submission.py --mode submission
```
The unfinished starter should pass the first two and fail submission mode. These checks do not execute estimators or validate new YAML scientific content. Once generator, methods and evaluator are implemented, add an explicitly documented bounded smoke run and positive/incorrect controls. A smoke pass establishes plumbing, not CI coverage. Preserve actual logs and unresolved errors.

**8.8 Prepare small-scale training for a later execution stage**

After scientific and implementation review, freeze the pilot architecture, task sampling, teacher, optimizer, seeds, task/update budget and checkpoint-selection rule. The future training interface is: reviewed train configuration to checkpoint plus metadata and logs; **an executable training entrypoint is not supplied here**. This revision starts no training. Once that later stage is implemented and training-ready, record actual unique tasks, presentations, elapsed cost, failures and selected checkpoint. Do not infer training success from a completed configuration.

**8.9 Evaluate CI procedures on paired independent repetitions**

Freeze the checkpoint/methods and evaluation registry. For each fixed DGP and n, independently generate the registered R datasets and run both full procedures on each dataset; keep CATE queries fixed as declared. The future evaluator must produce per-replicate results, truth joins and design-aware summaries; **no statistical evaluation runner is supplied here**. Report gate basis/denominators, coverage MC intervals, length after the gate, point/variance calibration, every failure and separated costs. Do not average over changing P and call it fixed-DGP coverage.

**8.10 Complete AI pre-review and scientific/independent review**

Record the AI tool/version/date, reviewed artifacts, findings, fixes and unresolved issues. Ask a scientific reviewer to check the source reconstruction, target/identification, oracle, hyperdistribution and CI design. Have a person independent of evaluated-model development rerun the implemented workflow in a clean environment; same-team reviewers are allowed with documented independence and conflicts. AI agreement or a structural pass is not scientific acceptance.

**8.11 Freeze the contribution and state its actual milestone**

Package the specifications, code, rights, version/hashes, seed/split ledger, model exposure, actual checkpoint metadata if any, run evidence and review disposition. Use the milestones below and list remaining work. A proposal may be submitted for review before training; an unsupported PFN remains a documented capability limit. Submission format and scientific readiness are distinct, and no live acceptance service is asserted.

## 9. Completion, review and staged milestones

Use a staged contribution process so students can submit a rigorous proposal before training. Reviewers assess the evidence for the declared milestone rather than treating a completed template as an implemented method.

| Milestone | Evidence required |
| --- | --- |
| Proposal | A selected task/estimand, source ledger, assumptions, truth plan, Pi_k, proposed baseline/PFN adapter, CI design, split policy and budget. Unresolved items and implementation owners are explicit. |
| Reference-demo-ready | An implemented generator and checked truth oracle; a runnable classical reference and declared PFN support/adapter; an implemented output/evaluation path; reproducible public smoke evidence and an environment. An unsupported PFN is recorded as a limit. |
| Training-ready | Reviewed input/teacher/head/loss definitions, executable training plumbing with bounded checks, frozen architecture/hyperdistribution, train/development splits, seeds, budget and checkpoint-selection plan. This status does not claim completed training. |
| Statistically validated | Actual frozen methods/checkpoints where used, paired fixed-DGP repetitions, target-appropriate coverage uncertainty and gates, lengths, failures/availability and costs, together with scientific review and independent rerun evidence. Claims are limited to the evaluated domain. |

The current protocol and starter are **draft specifications**. The mediation demo, training and statistical evaluation have not attained these implementation/validation milestones merely because templates are provided.

The final review package must answer the following checklist:

- Is the task/target/role/query contract explicit, with the required identification and sampling conditions?

- Can each DGP, source version, reproduction change and oracle be traced and independently checked?

- Are Pi_k, teacher labels and model inputs distinguished, with oracle information excluded from deployment inputs?

- Are train/development/evaluation uses, holdouts, model exposure and seed ledgers frozen and disclosed?

- Are the classical reference and PFN support/adapter documented with real entrypoints where implemented, environment and method mode?

- Are interval construction, observed-label budgets, fixed-DGP repetitions, MC uncertainty, coverage denominator/gate and every failure prespecified?

- Are actual outputs, costs, hashes and logs separated from illustrative examples and unexecuted plans?

- Are AI findings, scientific decisions, independent rerun evidence, remaining limitations and the claimed milestone recorded?

AI pre-review checks format, traceability, inconsistencies and obvious scientific mismatches. Scientific review checks estimand/identification, DGP/oracle, training design and uncertainty validity. An independent rerun checks the implemented workflow and reported numbers. Reviewers may come from the same team, but must be independent of the evaluated model's development and disclose conflicts. Unresolved scientific issues remain visible; any revision after frozen evaluation is versioned and re-evaluated as needed.

The contributor submits the selected milestone and evidence for review. Acceptance requires a recorded review decision. A structural validation pass alone does not establish statistical validity, and a successful result for one task does not establish support for all six categories.
