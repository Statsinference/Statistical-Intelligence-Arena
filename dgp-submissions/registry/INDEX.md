# StatsArena — DGP Registry

> **Draft view:** all automatically extracted records still need human scientific review.

**27 DGP mechanisms**, **51 parameter scenarios**, **22 reference papers**

## Six research areas

| Research area | Papers | DGP mechanisms | Open catalog |
|---|---:|---:|---|
| ATE — Average Treatment Effect | 2 | 2 | [Browse](by-domain/ate.md) |
| CATE — Conditional Average Treatment Effect | 2 | 2 | [Browse](by-domain/cate.md) |
| Mediation — Direct and Indirect Effects | 1 | 1 | [Browse](by-domain/mediation.md) |
| IV — Instrumental Variables | 5 | 5 | [Browse](by-domain/iv.md) |
| Proximal Causal Inference | 7 | 10 | [Browse](by-domain/proximal.md) |
| DiD / Synthetic Control | 3 | 3 | [Browse](by-domain/did_sc.md) |

## Paper list by research area

Each paper is listed **once per area**. Generators are source files from the submitted ZIP, not executed or automatically validated.

**Keywords** describe each submitted DGP, not the whole paper. Missing tags do not prove absence; nonlinearity may occur in any part of the mechanism. Numbered entries match the DGP mechanisms and generators in the same row.

### [ATE — Average Treatment Effect](by-domain/ate.md)

2 paper(s) · 2 DGP mechanism(s)

| Paper Title | DGPs | DGP Mechanisms | Keywords | Generator.py |
|---|---:|---|---|---|
| [Estimation and Inference of Heterogeneous Treatment Effects using Random Forests](https://doi.org/10.1080/01621459.2017.1319839) (JASA) | 1 | [Null Treatment Effect with Nonlinear Propensity Scores and Observed Confounding](drafts/ate-wager-athey-2018-confounded-null-v1.md) | Nonlinearity | [generator.py](generators/ate-wager-athey-2018-confounded-null-v1.py) |
| [Quasi-oracle estimation of heterogeneous treatment effects](https://doi.org/10.1093/biomet/asaa076) (Biometrika) | 1 | [ATE under Nie--Wager Setup A: nonlinear confounding and heterogeneous effects](drafts/ate-nie-wager-2021-a-v1.md) | Interactions · Nonlinearity · Effect heterogeneity | [generator.py](generators/ate-nie-wager-2021-a-v1.py) |

### [CATE — Conditional Average Treatment Effect](by-domain/cate.md)

2 paper(s) · 2 DGP mechanism(s)

| Paper Title | DGPs | DGP Mechanisms | Keywords | Generator.py |
|---|---:|---|---|---|
| [Estimation and Inference of Heterogeneous Treatment Effects using Random Forests](https://doi.org/10.1080/01621459.2017.1319839) (JASA) | 1 | [Pointwise CATE under Randomized Treatment with Logistic Interaction Effects](drafts/cate-wager-athey-2018-logistic-v1.md) | Interactions · Nonlinearity · Effect heterogeneity | [generator.py](generators/cate-wager-athey-2018-logistic-v1.py) |
| [Generalized Random Forests](https://doi.org/10.1214/18-aos1709) (AoS) | 1 | [Pointwise CATE with Confounding and Logistic Interaction Effects](drafts/cate-athey-tibshirani-wager-2019-confounded-v1.md) | Interactions · Nonlinearity · Effect heterogeneity | [generator.py](generators/cate-athey-tibshirani-wager-2019-confounded-v1.py) |

### [Mediation — Direct and Indirect Effects](by-domain/mediation.md)

1 paper(s) · 1 DGP mechanism(s)

| Paper Title | DGPs | DGP Mechanisms | Keywords | Generator.py |
|---|---:|---|---|---|
| [Semiparametric theory for causal mediation analysis: efficiency bounds, multiple robustness and sensitivity analysis](https://doi.org/10.1214/12-aos990) (AoS) | 1 | [Natural indirect effect in the Tchetgen Tchetgen–Shpitser mediation design](drafts/nie-eric-original-v1.md) | Interactions · Nonlinearity | [generator.py](generators/nie-eric-original-v1.py) |

### [IV — Instrumental Variables](by-domain/iv.md)

5 paper(s) · 5 DGP mechanism(s)

| Paper Title | DGPs | DGP Mechanisms | Keywords | Generator.py |
|---|---:|---|---|---|
| Deep IV: A Flexible Approach for Counterfactual Prediction (ICML) | 1 | [IV: DeepIV raw-unit demand with endogenous continuous price](drafts/iv-hartford-2017-demand-v1.md) | Interactions · Nonlinearity | [generator.py](generators/iv-hartford-2017-demand-v1.py) |
| [Generalized random forests](https://doi.org/10.1214/18-aos1709) (AoS) | 1 | [Endogenous Noncompliance and Local Treatment Effects](drafts/iv-athey-tibshirani-wager-2019-compliance-v1.md) | Interactions · Nonlinearity | [generator.py](generators/iv-athey-tibshirani-wager-2019-compliance-v1.py) |
| [Instrumental variables as bias amplifiers with general outcome and confounding](https://doi.org/10.1093/biomet/asx009) (Biometrika) | 1 | [DGP iv-ding-2017-binary-bias-v1 (English title required)](drafts/iv-ding-2017-binary-bias-v1.md) | Interactions · Nonlinearity | [generator.py](generators/iv-ding-2017-binary-bias-v1.py) |
| [Instrumental Variables Estimation With Some Invalid Instruments and its Application to Mendelian Randomization](https://doi.org/10.1080/01621459.2014.994705) (JASA) | 1 | [Partially Invalid Instruments with Linear Endogenous Treatment](drafts/iv-kang-2016-invalid-linear-v1.md) | Linearity | [generator.py](generators/iv-kang-2016-invalid-linear-v1.py) |
| Minimax Estimation of Conditional Moment Models (NeurIPS) | 1 | [IV: sine structural response with Gaussian confounding](drafts/iv-dikkala-2020-sine-v1.md) | Nonlinearity | [generator.py](generators/iv-dikkala-2020-sine-v1.py) |

### [Proximal Causal Inference](by-domain/proximal.md)

7 paper(s) · 10 DGP mechanism(s)

| Paper Title | DGPs | DGP Mechanisms | Keywords | Generator.py |
|---|---:|---|---|---|
| [Long-term causal inference under persistent confounding via data combination](https://doi.org/10.1093/jrsssb/qkae095) (JRSSB) | 1 | [Sequential Proxies and Long-Term Causal Effects from Combined Data](drafts/proximal-imbens-2025-longterm-v1.md) | Nonlinearity | [generator.py](generators/proximal-imbens-2025-longterm-v1.py) |
| [Proximal causal inference for complex longitudinal studies](https://doi.org/10.1093/jrsssb/qkad020) (JRSSB) | 1 | [Two-Period Treatment with Time-Varying Confounding and Feedback](drafts/proximal-ying-2023-longitudinal-v1.md) | Nonlinearity | [generator.py](generators/proximal-ying-2023-longitudinal-v1.py) |
| [Proximal indirect comparison](https://doi.org/10.1093/biomet/asaf044) (Biometrika) | 1 | [Cross-Trial Transportability with Unmeasured Effect Modification](drafts/proximal-su-2026-transport-v1.md) | Interactions · Nonlinearity · Effect heterogeneity | [generator.py](generators/proximal-su-2026-transport-v1.py) |
| [Proximal Learning for Individualized Treatment Regimes Under Unmeasured Confounding](https://doi.org/10.1080/01621459.2022.2147841) (JASA) | 3 | 1: [Absolute-Value and Trigonometric Proxy Interactions (N1)](drafts/proximal-qi-2024-trigonometric-v1.md)<br/>2: [Linear Heterogeneous Treatment Effect Bridge (L1/L2)](drafts/proximal-qi-2024-linear-itr-v1.md)<br/>3: [Quadratic Baseline Effects and Product Treatment Effect (N2)](drafts/proximal-qi-2024-quadratic-v1.md) | 1: Interactions · Nonlinearity<br/>2: Interactions · Nonlinearity · Effect heterogeneity<br/>3: Interactions · Nonlinearity | [1: generator.py](generators/proximal-qi-2024-trigonometric-v1.py)<br/>[2: generator.py](generators/proximal-qi-2024-linear-itr-v1.py)<br/>[3: generator.py](generators/proximal-qi-2024-quadratic-v1.py) |
| [Proximal mediation analysis](https://doi.org/10.1093/biomet/asad015) (Biometrika) | 1 | [Natural Direct Effect under Unmeasured Confounding](drafts/proximal-dukes-2023-mediation-v1.md) | Nonlinearity | [generator.py](generators/proximal-dukes-2023-mediation-v1.py) |
| [Semiparametric Proximal Causal Inference](https://doi.org/10.1080/01621459.2023.2191817) (JASA) | 1 | [Linear Bridge Model with Constant ATE](drafts/proximal-cui-2024-linear-v1.md) | Nonlinearity | [generator.py](generators/proximal-cui-2024-linear-v1.py) |
| [Theory for Identification and Inference with Synthetic Controls: A Proximal Causal Inference Framework](https://doi.org/10.1080/01621459.2026.2639734) (JASA) | 2 | 1: [Poisson Synthetic Control with Truncated Normal Factors](drafts/proximal-shi-2026-sc-poisson-v1.md)<br/>2: [Stationary Multifactor Gaussian Synthetic Control](drafts/proximal-shi-2026-sc-gaussian-v1.md) | 1: Nonlinearity · Panel data<br/>2: Linearity · Panel data | [1: generator.py](generators/proximal-shi-2026-sc-poisson-v1.py)<br/>[2: generator.py](generators/proximal-shi-2026-sc-gaussian-v1.py) |

### [DiD / Synthetic Control](by-domain/did_sc.md)

3 paper(s) · 3 DGP mechanism(s)

| Paper Title | DGPs | DGP Mechanisms | Keywords | Generator.py |
|---|---:|---|---|---|
| [A Negative Correlation Strategy for Bracketing in Difference-in-Differences](https://doi.org/10.1080/01621459.2023.2252576) (JASA) | 1 | [DGP did-ye-2024-bracketing-v1 (English title required)](drafts/did-ye-2024-bracketing-v1.md) | Linearity · Panel data | [generator.py](generators/did-ye-2024-bracketing-v1.py) |
| [A semiparametric instrumented difference-in-differences approach to policy learning](https://doi.org/10.1093/biomet/asaf043) (Biometrika) | 1 | [DGP did-zhao-cui-2025-instrumented-v1 (English title required)](drafts/did-zhao-cui-2025-instrumented-v1.md) | Interactions · Nonlinearity · Effect heterogeneity | [generator.py](generators/did-zhao-cui-2025-instrumented-v1.py) |
| [Doubly robust difference-in-differences estimators](https://doi.org/10.1016/j.jeconom.2020.06.003) (JoE) | 1 | [Sant'Anna--Zhao DGP1: two-period panel with covariate-specific trends](drafts/did-santanna-zhao-2020-panel-dgp1-v1.md) | Interactions · Nonlinearity · Panel data | [generator.py](generators/did-santanna-zhao-2020-panel-dgp1-v1.py) |

### [Needs classification](by-domain/unclassified.md)

3 paper(s) · 4 DGP mechanism(s)

| Paper Title | DGPs | DGP Mechanisms | Keywords | Generator.py |
|---|---:|---|---|---|
| [Generalized random forests](https://doi.org/10.1214/18-aos1709) (AoS) | 2 | 1: [Conditional quantile under Athey-Tibshirani-Wager Figure 2 mean shift](drafts/qr-athey-tibshirani-wager-2019-mean-v1.md)<br/>2: [Conditional quantile under Athey-Tibshirani-Wager Figure 2 scale shift](drafts/qr-athey-tibshirani-wager-2019-scale-v1.md) | 1: Nonlinearity<br/>2: Nonlinearity · Heteroskedasticity | [1: generator.py](generators/qr-athey-tibshirani-wager-2019-mean-v1.py)<br/>[2: generator.py](generators/qr-athey-tibshirani-wager-2019-scale-v1.py) |
| [High-Dimensional Quantile Regression: Convolution Smoothing and Concave Regularization](https://doi.org/10.1111/rssb.12485) (JRSSB) | 1 | [QDI: active-coordinate Gaussian-mixture marginal of the Tan-Wang-Zhou design (10-dimensional adaptation)](drafts/qdi-tan-wang-zhou-20220201-active10-mixture-v2.md) | Linearity | [generator.py](generators/qdi-tan-wang-zhou-20220201-active10-mixture-v2.py) |
| [On the Effect of Bias Estimation on Coverage Accuracy in Nonparametric Inference](https://doi.org/10.1080/01621459.2017.1285776) (JASA) | 1 | [DGP nri-calonico-2018-asymmetric-sine-v1 (English title required)](drafts/nri-calonico-2018-asymmetric-sine-v1.md) | Nonlinearity | [generator.py](generators/nri-calonico-2018-asymmetric-sine-v1.py) |


## Needs classification

[4 unclassified DGP(s)](by-domain/unclassified.md) require a reviewer.

## Extraction notes

- Equivalent DGP ate-nie-wager-2021-a-v1 in incoming/contributions.zip is already registered from incoming/ate-nie-wager-2021-a-v1.zip; merged duplicate source reference.
- Equivalent DGP cate-athey-tibshirani-wager-2019-confounded-v1 in incoming/contributions.zip is already registered from incoming/cate-athey-tibshirani-wager-2019-confounded-v1.zip; merged duplicate source reference.
