# Task brief: illustrative mediation NIE

Discussion protocol v0.3, 18 October 2026; output schema 0.2.0.

**Status: specification scaffold.** No generator, training/evaluation implementation, model or measured result exists in this package. The immediate work is to register and review DGPs, then complete a task-conditional hyperdistribution and small PFN / fixed-DGP CI evaluation plan.

## What this task asks

Given an observed table with baseline X_1, treatment A, mediator M and outcome Y, estimate the population natural indirect effect
NIE = E[Y(1,M(1)) - Y(1,M(0))]
and report a confidence interval under the declared identification assumptions. The target, role mapping, population, design knowledge and budget are supplied for Layer B. General analysis/identification decisions belong to optional Layer A and are scored separately.

The illustrative original mechanism is in dgps/cards/mediation_illustrative.md. It has no external classical-source claim. The DGP catalog is header-only pending verified sources. A real-data paper is optional; an attributed classical DGP needs an exact primary source and locator.

## Contribution sequence

1. Complete a sourced or explicitly original DGP card and catalog row, including independent truth verification.
2. Define Pi_k in hyperdistribution.yaml conditional on this task, NIE convention, role mapping and query contract.
3. Specify configs/train.yaml: model, label/teacher choice, optional heads, loss, episodes/n/seeds and offline budget. A suitable existing checkpoint may be reused.
4. Freeze configs/evaluate.yaml: fixed DGPs, paired independent repetitions, CI methods, nominal level, Monte Carlo uncertainty, coverage denominator, availability/failure gate and budgets.
5. Implement the reviewed design, then provide actual reference and PFN adapters, execution evidence, scientific review and independent reproduction. Follow demo/README.md.

## Permitted inputs and outputs

Observed table, supplied role/target/design information, nominal level, permitted checkpoint and budget. Oracle parameters, latent errors, hidden truth, counterfactual outcomes and oracle nuisance functions are evaluator-only unless explicitly declared as offline teacher inputs.

Use target_object parameter_ci, the registered fixed-DGP sampling scope, and one schema-0.2.0 Layer B record per attempted method/replicate/target. Keep unsupported, abstained, failed and not_identified attempts. Core parameter intervals may be unbounded but cannot encode empty/disconnected confidence sets; those require an extension.

## Scope and unfinished decisions

The protocol has six family IDs: ate, cate, mediation, iv, proximal, did_sc. DiD and synthetic control require different subdesign contracts. Future-response prediction is retained only for schema compatibility. This NIE template is not an implemented example of every family.

TODO: named owners/reviewers, selected source mechanisms, parameters, population/units, teacher choice, actual adapters and all statistical budgets/thresholds. No performance or acceptance claim is made.
