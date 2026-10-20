# Planned reference mediation demo — protocol v0.3

**PLANNED; NOT IMPLEMENTED.** This release supplies the specification for a future reference walkthrough. It includes no generator, trained checkpoint, training loop, estimator, statistical runner, benchmark results or runnable commands for them. The only working commands are the package format and contract checks.

## Purpose

A student should eventually be able to follow one small, complete mediation example, then replace its sourced DGP card, target and method under the same contribution contract. The first demo is single-family, single-target NIE, not an unconditioned mixture of six unrelated scalar targets. It illustrates the workflow; it is not proof that PFNs outperform classical inference.

## Intended inputs and outputs

| Stage | Intended input | Intended output | Current status |
|---|---|---|---|
| DGP specification | source/card, equations, fixed parameters, population and units | reviewed DGP ID and independently checked truth rule | illustrative card only |
| Hyperdistribution | reviewed mechanisms, weights, parameter support, constraints | task-conditional Pi_k and split/seed manifest | template only |
| Small PFN plan | Pi_k, target/roles, label/teacher rule, architecture, loss and budget | frozen training configuration | template only |
| Offline training | reviewed DGP, truth rule and training configuration | checkpoint, hash, exposure record, training costs | not implemented |
| Method adapters | observed table, declared target/roles/query, design and budget | schema 0.2.0 Layer B result | interface proposed |
| Fixed-DGP CI evaluation | frozen DGP/n/R grid, independent paired replicates, methods | per-attempt outputs and coverage/length/availability/MC/cost report | not implemented |

## Student walkthrough for subsequent implementation

1. Read ../scientific_spec.md and ../dgps/cards/mediation_illustrative.md. Record the NIE convention and its identification assumptions. This original illustrative card claims no classical paper source; a sourced alternative must include an exact primary-source locator and every adaptation.
2. Complete a catalog row, choose fixed parameters/noise distributions, implement observed-data generation and a separate truth oracle, and check the analytic NIE against an independent calculation. Do not expose oracle targets, latent errors or counterfactuals to evaluated methods.
3. Complete ../hyperdistribution.yaml for the mediation task. Register task identity, role mapping and query contract. Choose train/dev mechanisms, weights and parameter laws; seal held-out mechanisms/regions/seeds before comparisons. Changing a random seed alone is not mechanism generalization.
4. Complete ../configs/train.yaml. Select the label target deliberately: true parameter, an FSP-style teacher, distillation or another justified target. A mediation FSP-style teacher needs its own functional derivation; copying an ATE EIF is not valid. Optional mean/variance heads must state what they estimate and how a CI is constructed.
5. Once the implementation is ready and the DGP, truth rule and training configuration have passed scientific review, start training. Save the checkpoint hash, exact prior support, label/loss definitions, budgets and selection history. Reusing a suitable checkpoint is allowed; each contributor need not pretrain a model.
6. Implement a classical reference and PFN adapter in the registry. A regression plug-in plus fully rerun bootstrap is a possible baseline for the illustrated model, pending assumptions and interval justification. Unsupported PFN targets must remain explicit rather than silently changing the estimand.
7. Complete ../configs/evaluate.yaml. At each fixed DGP and n, generate R independent datasets, give each method the same observed dataset and permitted information, rerun all allowed refitting/adaptation/calibration, and preserve every attempted result. Keep context/calibration/tuning labels within the matched total budget.
8. Report coverage with Monte Carlo uncertainty, availability/failures and all-attempt denominators; compare interval length only after the predeclared validity and availability rules. Separate offline training, loading and end-to-end inference costs.
9. Request scientific review and independent reproduction. Structural checks passing is not scientific acceptance.

## Proposed adapter interface (design only)

Input: observed table, task_id, target_id, role mapping, query contract (if any), permitted design knowledge, nominal level and budget. Output: one Layer B record per method/DGP/replicate/target/query under ../evaluation/result.schema.json. These are interface requirements, not an implemented API. The evaluator alone may access truth.

For the current NIE card, target_object is parameter_ci and the repeated-sampling coverage scope is marginal at a fixed DGP. CATE extensions need fixed query values and query IDs where required. Disconnected parameter confidence sets require an explicit extension; generic future-response prediction is outside this round.

## Commands that are available now

```text
python validate_submission.py --mode scaffold
python evaluation/check_contract.py
python validate_submission.py --mode submission
```

The first two are format/contract checks. Strict submission is expected to fail because implementation, source registration, reviewer evidence and scientific choices remain incomplete. The checker does not parse YAML or execute the proposed scientific workflow.
