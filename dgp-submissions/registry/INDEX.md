# StatsArena — DGP Registry

> **Draft view:** all automatically extracted records still need human scientific review.

**23 DGP mechanisms**, **41 parameter scenarios**, **18 reference papers**

## Six research areas

| Research area | Papers | DGP mechanisms | Open catalog |
|---|---:|---:|---|
| ATE — Average Treatment Effect | 2 | 2 | [Browse](by-domain/ate.md) |
| CATE — Conditional Average Treatment Effect | 2 | 2 | [Browse](by-domain/cate.md) |
| Mediation — Direct and Indirect Effects | 1 | 1 | [Browse](by-domain/mediation.md) |
| IV — Instrumental Variables | 5 | 5 | [Browse](by-domain/iv.md) |
| Proximal Causal Inference | 7 | 10 | [Browse](by-domain/proximal.md) |
| DiD / Synthetic Control | 1 | 1 | [Browse](by-domain/did_sc.md) |

## Paper list by research area

Each paper is listed **once per area**. Generators are source files from the submitted ZIP, not executed or automatically validated.

### [ATE — Average Treatment Effect](by-domain/ate.md)

2 paper(s) · 2 DGP mechanism(s)

| Paper Title | DGPs | DGP Mechanisms | Generator.py |
|---|---:|---|---|
| [Estimation and Inference of Heterogeneous Treatment Effects using Random Forests](https://doi.org/10.1080/01621459.2017.1319839) | 1 | [Null Treatment Effect with Nonlinear Propensity Scores and Observed Confounding](drafts/ate-wager-athey-2018-confounded-null-v1.md) | [generator.py](generators/ate-wager-athey-2018-confounded-null-v1.py) |
| [Quasi-oracle estimation of heterogeneous treatment effects](https://doi.org/10.1093/biomet/asaa076) | 1 | [ATE under Nie--Wager Setup A: nonlinear confounding and heterogeneous effects](drafts/ate-nie-wager-2021-a-v1.md) | [generator.py](generators/ate-nie-wager-2021-a-v1.py) |

### [CATE — Conditional Average Treatment Effect](by-domain/cate.md)

2 paper(s) · 2 DGP mechanism(s)

| Paper Title | DGPs | DGP Mechanisms | Generator.py |
|---|---:|---|---|
| [Estimation and Inference of Heterogeneous Treatment Effects using Random Forests](https://doi.org/10.1080/01621459.2017.1319839) | 1 | [Pointwise CATE under Randomized Treatment with Logistic Interaction Effects](drafts/cate-wager-athey-2018-logistic-v1.md) | [generator.py](generators/cate-wager-athey-2018-logistic-v1.py) |
| [Generalized Random Forests](https://doi.org/10.1214/18-aos1709) | 1 | [Pointwise CATE with Confounding and Logistic Interaction Effects](drafts/cate-athey-tibshirani-wager-2019-confounded-v1.md) | [generator.py](generators/cate-athey-tibshirani-wager-2019-confounded-v1.py) |

### [Mediation — Direct and Indirect Effects](by-domain/mediation.md)

1 paper(s) · 1 DGP mechanism(s)

| Paper Title | DGPs | DGP Mechanisms | Generator.py |
|---|---:|---|---|
| [Semiparametric theory for causal mediation analysis: efficiency bounds, multiple robustness and sensitivity analysis](https://doi.org/10.1214/12-aos990) | 1 | [Natural indirect effect in the Tchetgen Tchetgen–Shpitser mediation design](drafts/nie-eric-original-v1.md) | [generator.py](generators/nie-eric-original-v1.py) |

### [IV — Instrumental Variables](by-domain/iv.md)

5 paper(s) · 5 DGP mechanism(s)

| Paper Title | DGPs | DGP Mechanisms | Generator.py |
|---|---:|---|---|
| Deep IV: A Flexible Approach for Counterfactual Prediction | 1 | [IV: DeepIV raw-unit demand with endogenous continuous price](drafts/iv-hartford-2017-demand-v1.md) | [generator.py](generators/iv-hartford-2017-demand-v1.py) |
| [Generalized random forests](https://doi.org/10.1214/18-aos1709) | 1 | [Endogenous Noncompliance and Local Treatment Effects](drafts/iv-athey-tibshirani-wager-2019-compliance-v1.md) | [generator.py](generators/iv-athey-tibshirani-wager-2019-compliance-v1.py) |
| [Instrumental variables as bias amplifiers with general outcome and confounding](https://doi.org/10.1093/biomet/asx009) | 1 | [DGP iv-ding-2017-binary-bias-v1 (English title required)](drafts/iv-ding-2017-binary-bias-v1.md) | [generator.py](generators/iv-ding-2017-binary-bias-v1.py) |
| [Instrumental Variables Estimation With Some Invalid Instruments and its Application to Mendelian Randomization](https://doi.org/10.1080/01621459.2014.994705) | 1 | [Partially Invalid Instruments with Linear Endogenous Treatment](drafts/iv-kang-2016-invalid-linear-v1.md) | [generator.py](generators/iv-kang-2016-invalid-linear-v1.py) |
| Minimax Estimation of Conditional Moment Models | 1 | [IV: sine structural response with Gaussian confounding](drafts/iv-dikkala-2020-sine-v1.md) | [generator.py](generators/iv-dikkala-2020-sine-v1.py) |

### [Proximal Causal Inference](by-domain/proximal.md)

7 paper(s) · 10 DGP mechanism(s)

| Paper Title | DGPs | DGP Mechanisms | Generator.py |
|---|---:|---|---|
| [Long-term causal inference under persistent confounding via data combination](https://doi.org/10.1093/jrsssb/qkae095) | 1 | [Sequential Proxies and Long-Term Causal Effects from Combined Data](drafts/proximal-imbens-2025-longterm-v1.md) | [generator.py](generators/proximal-imbens-2025-longterm-v1.py) |
| [Proximal causal inference for complex longitudinal studies](https://doi.org/10.1093/jrsssb/qkad020) | 1 | [Two-Period Treatment with Time-Varying Confounding and Feedback](drafts/proximal-ying-2023-longitudinal-v1.md) | [generator.py](generators/proximal-ying-2023-longitudinal-v1.py) |
| [Proximal indirect comparison](https://doi.org/10.1093/biomet/asaf044) | 1 | [Cross-Trial Transportability with Unmeasured Effect Modification](drafts/proximal-su-2026-transport-v1.md) | [generator.py](generators/proximal-su-2026-transport-v1.py) |
| [Proximal Learning for Individualized Treatment Regimes Under Unmeasured Confounding](https://doi.org/10.1080/01621459.2022.2147841) | 3 | [Absolute-Value and Trigonometric Proxy Interactions (N1)](drafts/proximal-qi-2024-trigonometric-v1.md), [Linear Heterogeneous Treatment Effect Bridge (L1/L2)](drafts/proximal-qi-2024-linear-itr-v1.md), [Quadratic Baseline Effects and Product Treatment Effect (N2)](drafts/proximal-qi-2024-quadratic-v1.md) | [1: generator.py](generators/proximal-qi-2024-trigonometric-v1.py), [2: generator.py](generators/proximal-qi-2024-linear-itr-v1.py), [3: generator.py](generators/proximal-qi-2024-quadratic-v1.py) |
| [Proximal mediation analysis](https://doi.org/10.1093/biomet/asad015) | 1 | [Natural Direct Effect under Unmeasured Confounding](drafts/proximal-dukes-2023-mediation-v1.md) | [generator.py](generators/proximal-dukes-2023-mediation-v1.py) |
| [Semiparametric Proximal Causal Inference](https://doi.org/10.1080/01621459.2023.2191817) | 1 | [Linear Bridge Model with Constant ATE](drafts/proximal-cui-2024-linear-v1.md) | [generator.py](generators/proximal-cui-2024-linear-v1.py) |
| [Theory for Identification and Inference with Synthetic Controls: A Proximal Causal Inference Framework](https://doi.org/10.1080/01621459.2026.2639734) | 2 | [Poisson Synthetic Control with Truncated Normal Factors](drafts/proximal-shi-2026-sc-poisson-v1.md), [Stationary Multifactor Gaussian Synthetic Control](drafts/proximal-shi-2026-sc-gaussian-v1.md) | [1: generator.py](generators/proximal-shi-2026-sc-poisson-v1.py), [2: generator.py](generators/proximal-shi-2026-sc-gaussian-v1.py) |

### [DiD / Synthetic Control](by-domain/did_sc.md)

1 paper(s) · 1 DGP mechanism(s)

| Paper Title | DGPs | DGP Mechanisms | Generator.py |
|---|---:|---|---|
| [Doubly robust difference-in-differences estimators](https://doi.org/10.1016/j.jeconom.2020.06.003) | 1 | [Sant'Anna--Zhao DGP1: two-period panel with covariate-specific trends](drafts/did-santanna-zhao-2020-panel-dgp1-v1.md) | [generator.py](generators/did-santanna-zhao-2020-panel-dgp1-v1.py) |

### [Needs classification](by-domain/unclassified.md)

1 paper(s) · 2 DGP mechanism(s)

| Paper Title | DGPs | DGP Mechanisms | Generator.py |
|---|---:|---|---|
| [Generalized random forests](https://doi.org/10.1214/18-aos1709) | 2 | [Conditional quantile under Athey-Tibshirani-Wager Figure 2 mean shift](drafts/qr-athey-tibshirani-wager-2019-mean-v1.md), [Conditional quantile under Athey-Tibshirani-Wager Figure 2 scale shift](drafts/qr-athey-tibshirani-wager-2019-scale-v1.md) | [1: generator.py](generators/qr-athey-tibshirani-wager-2019-mean-v1.py), [2: generator.py](generators/qr-athey-tibshirani-wager-2019-scale-v1.py) |


## Needs classification

[2 unclassified DGP(s)](by-domain/unclassified.md) require a reviewer.

## Extraction notes

- Equivalent DGP ate-nie-wager-2021-a-v1 in incoming/contributions.zip is already registered from incoming/ate-nie-wager-2021-a-v1.zip; merged duplicate source reference.
- Equivalent DGP cate-athey-tibshirani-wager-2019-confounded-v1 in incoming/contributions.zip is already registered from incoming/cate-athey-tibshirani-wager-2019-confounded-v1.zip; merged duplicate source reference.
