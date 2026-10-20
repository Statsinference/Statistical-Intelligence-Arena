# Scientific specification template — protocol v0.3

18 October 2026. Output schema remains 0.2.0. This is a planned original illustrative mediation task, not a sourced classical reproduction or implemented experiment.

## Target, population and sampling law

NIE = E[Y(1,M(1))-Y(1,M(0))]; complementary NDE = E[Y(1,M(0))-Y(0,M(0))]. This task evaluates NIE only. These are distinct targets, not interchangeable labels. Use target_object parameter_ci and coverage_scope marginal over repeated independent datasets at one fixed DGP.

TODO: population, treatment versions, baseline X, treatment A, mediator M, outcome Y, units, timing and independent sampling/assignment units. State what remains fixed and what is redrawn in each replicate. Do not call every baseline predictor a confounder.

## Identification

For the proposed route:
NIE = E_X[integral mu(1,m,X) {f(m|A=1,X)-f(m|A=0,X)} dm].

A sufficient assumption set must cover consistency, treatment exchangeability, mediator-outcome exchangeability, cross-world conditions, treatment positivity and mediator support. Exclude treatment-induced mediator-outcome confounding for this simple route. Treatment randomization alone does not identify the natural indirect effect. TODO: exact assumptions, graph/structural equations, derivation, supplied versus untestable knowledge and response to nonidentification.

## DGP-first specification and original illustrative mechanism

Register every source and adaptation in dgps/catalog.csv, with the field definitions in dgps/README.md. This release contains no curated catalog rows. The illustrative card is dgps/cards/mediation_illustrative.md and claims no external source.

X ~ N(0,1); A|X ~ Bernoulli(expit(c0+cX X)).
M = a0+aA A+aX X+eM.
Y = b0+bA A+bM M+bAM A M+bX X+eY.

Errors are independent, mean zero, and independent of X and assignment randomness. Then NIE = aA(bM+bAM), and NDE = bA+bAM a0 because E[X]=0. With another covariate population, NDE = bA+bAM(a0+aX E[X]). Parameters/noise distributions are not yet selected. A parameter draw in training is not the same experiment as repeated datasets at fixed parameters.

TODO: exact parameter ranges, constraints, noise distributions, sampling implementation, source/adaptation review and independent truth derivation/implementation. A semisynthetic replacement must state whether X is averaged over a fixed empirical pool or a superpopulation and modify truth accordingly. A published estimate is not exact truth; bound numerical truth error.

## Task-conditional hyperdistribution and supervision

hyperdistribution.yaml defines Pi_k conditional on one task_id, target_id, role mapping and query contract. The first planned demo uses mediation only. Future joint training across families must explicitly condition on tasks and provide compatible outputs; unrelated scalar labels must not be mixed without that information.

configs/train.yaml records a chosen label target: true parameter, FSP-style teacher, distillation or another justified rule. None is mandatory. A mediation FSP-style rule requires a derivation for this functional and its assumptions; an ATE EIF cannot simply be relabeled. Optional mean/variance heads must identify their targets, including whether variance means V(P), V(P)/n, posterior uncertainty or future-response noise, and specify the CI construction. An architecture or loss choice alone supplies no fixed-DGP coverage guarantee.

## Six-family extension requirements

| Family ID | Required scientific contract |
|---|---|
| ate | intervention, target population, treatment versions, identification and overlap/support |
| cate | causal contrast conditional on the declared X; fixed query x/grid or groups, target population, query weighting and coverage scope; within-table queries are dependent |
| mediation | precise NDE/NIE convention, mediator timing and the identification route above or a separately justified alternative |
| iv | structural coefficient versus LATE/complier target, instrument validity, exclusion and any monotonicity/relevance assumptions; weak identification changes valid uncertainty procedures |
| proximal | proxy roles, bridge existence/identification/completeness, support and weak-proxy behavior |
| did_sc | subdesign required: DiD specifies panel/repeated-cross-section sampling, timing, target contrast, parallel trends and no anticipation; synthetic control separately specifies donors, pre/post windows, contamination, counterfactual model and temporal dependence |

For panel/cluster designs, define an independent experiment and the fixed/redrawn time/design components. A linear data-generating equation is a mechanism inside a family, not a seventh family. Core scalar CI output accepts unbounded connected intervals; disconnected/empty parameter confidence sets require extension, never prediction_set or a silent convex hull.

## Fixed-DGP evaluation claim

configs/evaluate.yaml instantiates evaluation/protocol.yaml. Freeze DGP parameters, n/R, seed ledgers, queries, CI methods, budgets, nominal levels, MC method/level, tolerance and gate before evaluation. Pair methods on the same observed datasets. R counts independent experiments, not correlated CATE queries or panel rows.

Report valid-output coverage and all-attempt valid-and-covering rate with explicit denominators, availability and failures; predeclare the gating basis and availability/failure requirement. Selectively returning intervals cannot pass on conditional coverage alone. Compare length only after the same target/scope/budget validity gate; preserve infinite lengths and inconclusive MC results. A prior-mixture average cannot replace fixed-DGP results.

Separate public train/dev, held-out mechanisms/parameter regions and evaluation seeds; source age/fame does not establish unseen status. Generic future-Y prediction is not a current track, although schema compatibility remains. Simultaneous/vector regions need an extension. Higher-order accuracy is not required or implied.
