# StatsArena — submission extraction (needs review)

> Domain is provisionally inferred from the ZIP family field, not scientifically verified. Reviewers may correct classification.

## ATE — Average Treatment Effect

| Quasi-oracle estimation of heterogeneous treatment effects | [ATE under Nie--Wager Setup A: nonlinear confounding and heterogeneous effects](../drafts/ate-nie-wager-2021-a-v1.md) | original_d6_sigma1: theta_ATE = E[Y(1)-Y(0)] = 0.5 | Needs review | [generator.py](../generators/ate-nie-wager-2021-a-v1.py) |
| Estimation and Inference of Heterogeneous Treatment Effects using Random Forests | [Null Treatment Effect with Nonlinear Propensity Scores and Observed Confounding](../drafts/ate-wager-athey-2018-confounded-null-v1.md) | source_d5_sigma1: theta_ATE=E[Y(1)-Y(0)] = 0.0 | Needs review | [generator.py](../generators/ate-wager-athey-2018-confounded-null-v1.py) |

## CATE — Conditional Average Treatment Effect

| Generalized Random Forests | [Pointwise CATE with Confounding and Logistic Interaction Effects](../drafts/cate-athey-tibshirani-wager-2019-confounded-v1.md) | source_d10_sigma1_fixed_query: tau(x_star)=E[Y(1)-Y(0)\|X=x_star] = 2.25 | Needs review | [generator.py](../generators/cate-athey-tibshirani-wager-2019-confounded-v1.py) |
| Estimation and Inference of Heterogeneous Treatment Effects using Random Forests | [Pointwise CATE under Randomized Treatment with Logistic Interaction Effects](../drafts/cate-wager-athey-2018-logistic-v1.md) | source_d6_sigma1_fixed_query: tau(x_star)=E[Y(1)-Y(0)\|X=x_star] = 2.25 | Needs review | [generator.py](../generators/cate-wager-athey-2018-logistic-v1.py) |

## Mediation — Direct and Indirect Effects

| Semiparametric theory for causal mediation analysis: efficiency bounds, multiple robustness and sensitivity analysis | [Natural indirect effect in the Tchetgen Tchetgen–Shpitser mediation design](../drafts/nie-eric-original-v1.md) | original: theta_NIE = theta_11 - theta_10 = 0.2366199012683949 | Needs review | [generator.py](../generators/nie-eric-original-v1.py) |

## IV — Instrumental Variables

| Generalized random forests | [Endogenous Noncompliance and Local Treatment Effects](../drafts/iv-athey-tibshirani-wager-2019-compliance-v1.md) | source_additive_k2_omega0_mu0: tau_IV(x*) = 1.0; source_additive_k2_omega0_mu3: tau_IV(x*) = 1.0; source_additive_k2_omega1_mu0: tau_IV(x*) = 1.0; source_additive_k2_omega1_mu3: tau_IV(x*) = 1.0; source_additive_k4_omega0_mu0: tau_IV(x*) = 1.75; source_additive_k4_omega0_mu3: tau_IV(x*) = 1.75; source_additive_k4_omega1_mu0: tau_IV(x*) = 1.75; source_additive_k4_omega1_mu3: tau_IV(x*) = 1.75; source_nonadditive_k2_omega0_mu0: tau_IV(x*) = 0.5; source_nonadditive_k2_omega0_mu3: tau_IV(x*) = 0.5; source_nonadditive_k2_omega1_mu0: tau_IV(x*) = 0.5; source_nonadditive_k2_omega1_mu3: tau_IV(x*) = 0.5; source_nonadditive_k4_omega0_mu0: tau_IV(x*) = 1.0; source_nonadditive_k4_omega0_mu3: tau_IV(x*) = 1.0; source_nonadditive_k4_omega1_mu0: tau_IV(x*) = 1.0; source_nonadditive_k4_omega1_mu3: tau_IV(x*) = 1.0 | Needs review | [generator.py](../generators/iv-athey-tibshirani-wager-2019-compliance-v1.py) |
| Minimax Estimation of Conditional Moment Models | [IV: sine structural response with Gaussian confounding](../drafts/iv-dikkala-2020-sine-v1.md) | code_scale_alpha06_raw: theta_IV = h0(0.5)-h0(0) = 0.479425538604203 | Needs review | [generator.py](../generators/iv-dikkala-2020-sine-v1.py) |
| Instrumental variables as bias amplifiers with general outcome and confounding | [DGP iv-ding-2017-binary-bias-v1 (English title required)](../drafts/iv-ding-2017-binary-bias-v1.md) | source_table1_case1: LATE = 0.05545454545454545; source_table1_case2: LATE = 0.01; source_table1_case3: LATE = 0.022500000000000003 | Needs review | [generator.py](../generators/iv-ding-2017-binary-bias-v1.py) |
| Deep IV: A Flexible Approach for Counterfactual Prediction | [IV: DeepIV raw-unit demand with endogenous continuous price](../drafts/iv-hartford-2017-demand-v1.md) | paper_raw_rho08: theta_IV = E[Y(do(P=21))-Y(do(P=20))] = -11.624351792971128 | Needs review | [generator.py](../generators/iv-hartford-2017-demand-v1.py) |
| Instrumental Variables Estimation With Some Invalid Instruments and its Application to Mendelian Randomization | [Partially Invalid Instruments with Linear Endogenous Treatment](../drafts/iv-kang-2016-invalid-linear-v1.md) | author_readme_fixed: beta = 1.0 | Needs review | [generator.py](../generators/iv-kang-2016-invalid-linear-v1.py) |

## Proximal Causal Inference

| Semiparametric Proximal Causal Inference | [Linear Bridge Model with Constant ATE](../drafts/proximal-cui-2024-linear-v1.md) | original: ATE = 2.0 | Needs review | [generator.py](../generators/proximal-cui-2024-linear-v1.py) |
| Proximal mediation analysis | [Natural Direct Effect under Unmeasured Confounding](../drafts/proximal-dukes-2023-mediation-v1.md) | original: NDE = 2.0 | Needs review | [generator.py](../generators/proximal-dukes-2023-mediation-v1.py) |
| Long-term causal inference under persistent confounding via data combination | [Sequential Proxies and Long-Term Causal Effects from Combined Data](../drafts/proximal-imbens-2025-longterm-v1.md) | paper_q2_p5_fixed_design: theta = 0.8797723708687131 | Needs review | [generator.py](../generators/proximal-imbens-2025-longterm-v1.py) |
| Proximal Learning for Individualized Treatment Regimes Under Unmeasured Confounding | [Linear Heterogeneous Treatment Effect Bridge (L1/L2)](../drafts/proximal-qi-2024-linear-itr-v1.md) | L1: ATE = 0.10888711551018415; L2: ATE = 0.0 | Needs review | [generator.py](../generators/proximal-qi-2024-linear-itr-v1.py) |
| Proximal Learning for Individualized Treatment Regimes Under Unmeasured Confounding | [Quadratic Baseline Effects and Product Treatment Effect (N2)](../drafts/proximal-qi-2024-quadratic-v1.md) | N2: ATE = -0.125 | Needs review | [generator.py](../generators/proximal-qi-2024-quadratic-v1.py) |
| Proximal Learning for Individualized Treatment Regimes Under Unmeasured Confounding | [Absolute-Value and Trigonometric Proxy Interactions (N1)](../drafts/proximal-qi-2024-trigonometric-v1.md) | N1: ATE = 0.019533193713670016 | Needs review | [generator.py](../generators/proximal-qi-2024-trigonometric-v1.py) |
| Theory for Identification and Inference with Synthetic Controls: A Proximal Causal Inference Framework | [Stationary Multifactor Gaussian Synthetic Control](../drafts/proximal-shi-2026-sc-gaussian-v1.md) | journal_r5_stationary: ETT = 2.0 | Needs review | [generator.py](../generators/proximal-shi-2026-sc-gaussian-v1.py) |
| Theory for Identification and Inference with Synthetic Controls: A Proximal Causal Inference Framework | [Poisson Synthetic Control with Truncated Normal Factors](../drafts/proximal-shi-2026-sc-poisson-v1.md) | journal_r1_no_covariates: theta = -2.0 | Needs review | [generator.py](../generators/proximal-shi-2026-sc-poisson-v1.py) |
| Proximal indirect comparison | [Cross-Trial Transportability with Unmeasured Effect Modification](../drafts/proximal-su-2026-transport-v1.md) | original: theta = -2.6489954259019695 | Needs review | [generator.py](../generators/proximal-su-2026-transport-v1.py) |
| Proximal causal inference for complex longitudinal studies | [Two-Period Treatment with Time-Varying Confounding and Feedback](../drafts/proximal-ying-2023-longitudinal-v1.md) | original: theta = 1.9999999999999998 | Needs review | [generator.py](../generators/proximal-ying-2023-longitudinal-v1.py) |

## DiD / Synthetic Control

| Doubly robust difference-in-differences estimators | [Sant'Anna--Zhao DGP1: two-period panel with covariate-specific trends](../drafts/did-santanna-zhao-2020-panel-dgp1-v1.md) | original_panel_dgp1: ATT = E[Y_1(1)-Y_1(0) \| D=1] = 0.0 | Needs review | [generator.py](../generators/did-santanna-zhao-2020-panel-dgp1-v1.py) |


## Extraction notes

- Equivalent DGP ate-nie-wager-2021-a-v1 in incoming/contributions.zip is already registered from incoming/ate-nie-wager-2021-a-v1.zip; merged duplicate source reference.
- Equivalent DGP cate-athey-tibshirani-wager-2019-confounded-v1 in incoming/contributions.zip is already registered from incoming/cate-athey-tibshirani-wager-2019-confounded-v1.zip; merged duplicate source reference.
