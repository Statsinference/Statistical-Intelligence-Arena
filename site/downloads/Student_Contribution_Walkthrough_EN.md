# Statistical Inference Arena: Student Contribution Walkthrough

**Protocol v0.3 · 2026-10-18 · Output schema 0.2.0 · Draft specification**

Start with one causal estimand and follow the eleven steps below. The first release evaluates causal-parameter confidence intervals. The six categories are ATE, CATE, mediation, IV, proximal inference and DID/synthetic control. Layer B method evaluation comes first; Layer A complete analysis is optional.

The intended sequence is **classical DGP registration → task-conditioned Pi_k → small-PFN plan → independent fixed-DGP CI evaluation**. The current mediation card is a proposed teaching mechanism; its runnable generator, reference demo, training runner and statistical evaluator remain to be implemented. This revision starts no training.

The [complete contribution requirements](CausalTaskBench_Contribution_Requirements_EN.md) define the scientific contracts, file specifications, coverage gates and review milestones. These steps also appear in full in Chapter 8 of that document.

## 1. Copy the template and claim one task

Copy the current contributor starter into a separate task directory. Select `ate`, `cate`, `mediation`, `iv`, `proximal` or `did_sc`; choose a specific estimand and scientific owner. The current starter is scaffolding. **A runnable mediation reference demo is still to be implemented**; once reviewed, it can become the worked example for later students. Do not describe copying the template as reproducing a successful experiment. Deliver a short proposal with target, population, available source and planned evidence.

## 2. Read the original source and register the mechanism

Read the original method paper and official simulation code, not only a summary. Fill the catalog's source version, page/equation, code commit, rights and reproduction differences. Transcribe the variable equations, parameters, assignment and noise laws, sampling unit and target into a reviewable specification. Mark unresolved details rather than guessing a paper's implementation. If starting from a new canonical example, label it as newly specified rather than falsely attributing it to a paper.

## 3. Implement observed data and independently check truth

Implement the registered DGP and a separate truth calculation. Check units, signs, intervention levels and sampling dependence on small deterministic inputs or analytically tractable configurations. Verify source-faithful and modified versions separately. Export only observed variables; keep oracle labels in separate artifacts. Record approximation error and what the independent check shares with the primary implementation. Deliver generator/oracle code plus evidence; this step is not yet a PFN experiment.

## 4. Configure Pi_k and freeze data-use splits

Fill `hyperdistribution.yaml` for the selected task: registered mechanism IDs, normalized weights, admissible parameter distributions, constraints, n and sampling design, and label-oracle path. Define separate training, development and evaluation registries/seeds. Declare whether evaluation is in-distribution, parameter-held-out, mechanism-held-out or task-held-out. A small single-family mediation pilot is sufficient as a first plan. Deliver a sampling specification with examples of valid and rejected configurations; no training command is implied.

## 5. Update roles, target, teacher, head and CI rule

Map observed columns to the selected causal roles and make task/target ID explicit; add the fixed x or grid for CATE. Specify the teacher in `configs/train.yaml`: true target, reviewed sample-dependent teacher or estimator distillation are different choices. Update the output head/loss and interval construction to match it. Record architecture and masking changes. Check that oracle information is used only for supervision/evaluation. A new target requires a justified adapter, not a renamed output field.

## 6. Implement the classical reference and PFN adapter

Register both in `solution/methods.json`. Implement a suitable classical estimator and interval before comparing the PFN. Give both the same target and observed-label budget; disclose calibration/tuning splits and fitting rules. An existing unsupported PFN returns its precise limitation. Specify native-frozen, adapted or refit operation and record every correction or resampling step. Deliver real entrypoints and a pinned environment once implemented; do not fill them with invented commands or results.

## 7. Run available structural checks, then an implemented smoke test

The following commands are currently available from the starter directory:
```sh
python validate_submission.py --mode scaffold
python evaluation/check_contract.py
python validate_submission.py --mode submission
```
The unfinished starter should pass the first two and fail submission mode. These checks do not execute estimators or validate new YAML scientific content. Once generator, methods and evaluator are implemented, add an explicitly documented bounded smoke run and positive/incorrect controls. A smoke pass establishes plumbing, not CI coverage. Preserve actual logs and unresolved errors.

## 8. Prepare small-scale training for a later execution stage

After scientific and implementation review, freeze the pilot architecture, task sampling, teacher, optimizer, seeds, task/update budget and checkpoint-selection rule. The future training interface is: reviewed train configuration to checkpoint plus metadata and logs; **an executable training entrypoint is not supplied here**. This revision starts no training. Once that later stage is implemented and training-ready, record actual unique tasks, presentations, elapsed cost, failures and selected checkpoint. Do not infer training success from a completed configuration.

## 9. Evaluate CI procedures on paired independent repetitions

Freeze the checkpoint/methods and evaluation registry. For each fixed DGP and n, independently generate the registered R datasets and run both full procedures on each dataset; keep CATE queries fixed as declared. The future evaluator must produce per-replicate results, truth joins and design-aware summaries; **no statistical evaluation runner is supplied here**. Report gate basis/denominators, coverage MC intervals, length after the gate, point/variance calibration, every failure and separated costs. Do not average over changing P and call it fixed-DGP coverage.

## 10. Complete AI pre-review and scientific/independent review

Record the AI tool/version/date, reviewed artifacts, findings, fixes and unresolved issues. Ask a scientific reviewer to check the source reconstruction, target/identification, oracle, hyperdistribution and CI design. Have a person independent of evaluated-model development rerun the implemented workflow in a clean environment; same-team reviewers are allowed with documented independence and conflicts. AI agreement or a structural pass is not scientific acceptance.

## 11. Freeze the contribution and state its actual milestone

Package the specifications, code, rights, version/hashes, seed/split ledger, model exposure, actual checkpoint metadata if any, run evidence and review disposition. Use the milestones below and list remaining work. A proposal may be submitted for review before training; an unsupported PFN remains a documented capability limit. Submission format and scientific readiness are distinct, and no live acceptance service is asserted.

## Before claiming completion

Record one actual milestone: **proposal**, **reference-demo-ready**, **training-ready** or **statistically validated**. A filled configuration is not a trained checkpoint. The current package is a draft scaffold.

For the first mediation pilot, `dgps/cards/mediation_illustrative.md` provides equations and proposed analytic NIE/NDE formulas to verify. It is an original teaching example, not a reproduction of a cited paper. The initial target is NIE; NDE is a separate target. The same distinctions apply to all families: explicit roles/target, justified teacher and CI, declared support, and fixed-DGP evidence.

Before evaluation, freeze total observed-label allocation across context/calibration/tuning, the independent sampling unit, n/R/seeds and query design, coverage basis/denominator and availability gate. Report every attempt. Compare length only after the common coverage gate, with Monte Carlo uncertainty; preserve unbounded intervals and all failures. Store actual evidence separately from illustrative outputs.
