# Statistical Inference Arena · DGP Submission

**100% GitHub-native · Structured ZIP → automatic DGP catalog · No Issue · No LLM API · No other website**

<p align="center">
  <a href="https://github.com/Statsinference/stats-inference-arena/upload/main/dgp-submissions/incoming"><img alt="Submit DGP ZIP" src="https://img.shields.io/badge/Submit_DGP-Upload_ZIP_on_GitHub-1677C8?style=for-the-badge" /></a>
  <a href="registry/INDEX.md"><img alt="Browse six areas" src="https://img.shields.io/badge/Browse-Six_DGP_Areas-444444?style=for-the-badge" /></a>
  <a href="CONTRIBUTING.md"><img alt="Contribution instructions" src="https://img.shields.io/badge/How_to_Contribute-Read_Guide-007F73?style=for-the-badge" /></a>
</p>

## For students — 3 steps, all on GitHub

1. Click **Submit DGP** to open GitHub's file-upload screen for `incoming/` directly.
2. Choose or drag in **one structured `.zip` file**.
3. Click **Commit changes** (to `main` when authorized, otherwise to a new branch and submit a pull request). If GitHub requires a new branch, create a PR; the extraction preview runs on the PR, and the catalog updates after it is merged.

The ZIP's `collection.json` already identifies its research family, so **students do not need a separate dropdown**. A missing or unknown family is flagged for human classification, never guessed.

> **Important:** This is a private research intake. Each contribution becomes an **unverified draft** until a researcher checks the original paper. This software does not prove true values or equations correct.

## What gets extracted

| Scientific information | Stored in DGP registry |
|---|---|
| Reference paper | Citation, DOI, publication, paper/section locator |
| DGP mechanism | Name, generating equations, distributions and coefficients |
| Variables | Observed columns and their roles; latent variables flagged for review |
| Scenario | Parameter settings and experiment variants |
| Estimand | Which quantity (e.g. ATE/NDE/LATE) and definition |
| True value | Scenario-specific value (or needs review), calculation notes |
| Provenance | Uploaded ZIP, hashes, original/adapted notes and validation status |

**Hierarchy:** Area → Paper → DGP → Scenario → Estimand & Truth. One paper may contribute multiple DGPs, and one DGP may contain multiple scenarios.

## Browse the six research areas

[ATE](registry/by-domain/ate.md) · [CATE](registry/by-domain/cate.md) · [Mediation](registry/by-domain/mediation.md) · [IV](registry/by-domain/iv.md) · [Proximal](registry/by-domain/proximal.md) · [DiD / Synthetic Control](registry/by-domain/did_sc.md)

<!-- STATSARENA_PAPER_LIST_BEGIN -->

## Paper list by research area

Each paper is listed **once per area**. Generators are source files from the submitted ZIP, not executed or automatically validated.

**Keywords** describe each submitted DGP, not the whole paper. Missing tags do not prove absence; nonlinearity may occur in any part of the mechanism. Numbered entries match the DGP mechanisms and generators in the same row.

### [ATE — Average Treatment Effect](registry/by-domain/ate.md)

2 paper(s) · 2 DGP mechanism(s)

| Paper Title | DGPs | DGP Mechanisms | Keywords | Generator.py |
|---|---:|---|---|---|
| [Estimation and Inference of Heterogeneous Treatment Effects using Random Forests](https://doi.org/10.1080/01621459.2017.1319839) (JASA) | 1 | [Null Treatment Effect with Nonlinear Propensity Scores and Observed Confounding](registry/drafts/ate-wager-athey-2018-confounded-null-v1.md) | Nonlinearity | [generator.py](registry/generators/ate-wager-athey-2018-confounded-null-v1.py) |
| [Quasi-oracle estimation of heterogeneous treatment effects](https://doi.org/10.1093/biomet/asaa076) (Biometrika) | 1 | [ATE under Nie--Wager Setup A: nonlinear confounding and heterogeneous effects](registry/drafts/ate-nie-wager-2021-a-v1.md) | Interactions · Nonlinearity · Effect heterogeneity | [generator.py](registry/generators/ate-nie-wager-2021-a-v1.py) |

### [CATE — Conditional Average Treatment Effect](registry/by-domain/cate.md)

2 paper(s) · 2 DGP mechanism(s)

| Paper Title | DGPs | DGP Mechanisms | Keywords | Generator.py |
|---|---:|---|---|---|
| [Estimation and Inference of Heterogeneous Treatment Effects using Random Forests](https://doi.org/10.1080/01621459.2017.1319839) (JASA) | 1 | [Pointwise CATE under Randomized Treatment with Logistic Interaction Effects](registry/drafts/cate-wager-athey-2018-logistic-v1.md) | Interactions · Nonlinearity · Effect heterogeneity | [generator.py](registry/generators/cate-wager-athey-2018-logistic-v1.py) |
| [Generalized Random Forests](https://doi.org/10.1214/18-aos1709) (AoS) | 1 | [Pointwise CATE with Confounding and Logistic Interaction Effects](registry/drafts/cate-athey-tibshirani-wager-2019-confounded-v1.md) | Interactions · Nonlinearity · Effect heterogeneity | [generator.py](registry/generators/cate-athey-tibshirani-wager-2019-confounded-v1.py) |

### [Mediation — Direct and Indirect Effects](registry/by-domain/mediation.md)

1 paper(s) · 1 DGP mechanism(s)

| Paper Title | DGPs | DGP Mechanisms | Keywords | Generator.py |
|---|---:|---|---|---|
| [Semiparametric theory for causal mediation analysis: efficiency bounds, multiple robustness and sensitivity analysis](https://doi.org/10.1214/12-aos990) (AoS) | 1 | [Natural indirect effect in the Tchetgen Tchetgen–Shpitser mediation design](registry/drafts/nie-eric-original-v1.md) | Interactions · Nonlinearity | [generator.py](registry/generators/nie-eric-original-v1.py) |

### [IV — Instrumental Variables](registry/by-domain/iv.md)

5 paper(s) · 5 DGP mechanism(s)

| Paper Title | DGPs | DGP Mechanisms | Keywords | Generator.py |
|---|---:|---|---|---|
| Deep IV: A Flexible Approach for Counterfactual Prediction (ICML) | 1 | [IV: DeepIV raw-unit demand with endogenous continuous price](registry/drafts/iv-hartford-2017-demand-v1.md) | Interactions · Nonlinearity | [generator.py](registry/generators/iv-hartford-2017-demand-v1.py) |
| [Generalized random forests](https://doi.org/10.1214/18-aos1709) (AoS) | 1 | [Endogenous Noncompliance and Local Treatment Effects](registry/drafts/iv-athey-tibshirani-wager-2019-compliance-v1.md) | Interactions · Nonlinearity | [generator.py](registry/generators/iv-athey-tibshirani-wager-2019-compliance-v1.py) |
| [Instrumental variables as bias amplifiers with general outcome and confounding](https://doi.org/10.1093/biomet/asx009) (Biometrika) | 1 | [DGP iv-ding-2017-binary-bias-v1 (English title required)](registry/drafts/iv-ding-2017-binary-bias-v1.md) | Interactions · Nonlinearity | [generator.py](registry/generators/iv-ding-2017-binary-bias-v1.py) |
| [Instrumental Variables Estimation With Some Invalid Instruments and its Application to Mendelian Randomization](https://doi.org/10.1080/01621459.2014.994705) (JASA) | 1 | [Partially Invalid Instruments with Linear Endogenous Treatment](registry/drafts/iv-kang-2016-invalid-linear-v1.md) | Linearity | [generator.py](registry/generators/iv-kang-2016-invalid-linear-v1.py) |
| Minimax Estimation of Conditional Moment Models (NeurIPS) | 1 | [IV: sine structural response with Gaussian confounding](registry/drafts/iv-dikkala-2020-sine-v1.md) | Nonlinearity | [generator.py](registry/generators/iv-dikkala-2020-sine-v1.py) |

### [Proximal Causal Inference](registry/by-domain/proximal.md)

7 paper(s) · 10 DGP mechanism(s)

| Paper Title | DGPs | DGP Mechanisms | Keywords | Generator.py |
|---|---:|---|---|---|
| [Long-term causal inference under persistent confounding via data combination](https://doi.org/10.1093/jrsssb/qkae095) (JRSSB) | 1 | [Sequential Proxies and Long-Term Causal Effects from Combined Data](registry/drafts/proximal-imbens-2025-longterm-v1.md) | Nonlinearity | [generator.py](registry/generators/proximal-imbens-2025-longterm-v1.py) |
| [Proximal causal inference for complex longitudinal studies](https://doi.org/10.1093/jrsssb/qkad020) (JRSSB) | 1 | [Two-Period Treatment with Time-Varying Confounding and Feedback](registry/drafts/proximal-ying-2023-longitudinal-v1.md) | Nonlinearity | [generator.py](registry/generators/proximal-ying-2023-longitudinal-v1.py) |
| [Proximal indirect comparison](https://doi.org/10.1093/biomet/asaf044) (Biometrika) | 1 | [Cross-Trial Transportability with Unmeasured Effect Modification](registry/drafts/proximal-su-2026-transport-v1.md) | Interactions · Nonlinearity · Effect heterogeneity | [generator.py](registry/generators/proximal-su-2026-transport-v1.py) |
| [Proximal Learning for Individualized Treatment Regimes Under Unmeasured Confounding](https://doi.org/10.1080/01621459.2022.2147841) (JASA) | 3 | 1: [Absolute-Value and Trigonometric Proxy Interactions (N1)](registry/drafts/proximal-qi-2024-trigonometric-v1.md)<br/>2: [Linear Heterogeneous Treatment Effect Bridge (L1/L2)](registry/drafts/proximal-qi-2024-linear-itr-v1.md)<br/>3: [Quadratic Baseline Effects and Product Treatment Effect (N2)](registry/drafts/proximal-qi-2024-quadratic-v1.md) | 1: Interactions · Nonlinearity<br/>2: Interactions · Nonlinearity · Effect heterogeneity<br/>3: Interactions · Nonlinearity | [1: generator.py](registry/generators/proximal-qi-2024-trigonometric-v1.py)<br/>[2: generator.py](registry/generators/proximal-qi-2024-linear-itr-v1.py)<br/>[3: generator.py](registry/generators/proximal-qi-2024-quadratic-v1.py) |
| [Proximal mediation analysis](https://doi.org/10.1093/biomet/asad015) (Biometrika) | 1 | [Natural Direct Effect under Unmeasured Confounding](registry/drafts/proximal-dukes-2023-mediation-v1.md) | Nonlinearity | [generator.py](registry/generators/proximal-dukes-2023-mediation-v1.py) |
| [Semiparametric Proximal Causal Inference](https://doi.org/10.1080/01621459.2023.2191817) (JASA) | 1 | [Linear Bridge Model with Constant ATE](registry/drafts/proximal-cui-2024-linear-v1.md) | Nonlinearity | [generator.py](registry/generators/proximal-cui-2024-linear-v1.py) |
| [Theory for Identification and Inference with Synthetic Controls: A Proximal Causal Inference Framework](https://doi.org/10.1080/01621459.2026.2639734) (JASA) | 2 | 1: [Poisson Synthetic Control with Truncated Normal Factors](registry/drafts/proximal-shi-2026-sc-poisson-v1.md)<br/>2: [Stationary Multifactor Gaussian Synthetic Control](registry/drafts/proximal-shi-2026-sc-gaussian-v1.md) | 1: Nonlinearity · Panel data<br/>2: Linearity · Panel data | [1: generator.py](registry/generators/proximal-shi-2026-sc-poisson-v1.py)<br/>[2: generator.py](registry/generators/proximal-shi-2026-sc-gaussian-v1.py) |

### [DiD / Synthetic Control](registry/by-domain/did_sc.md)

3 paper(s) · 3 DGP mechanism(s)

| Paper Title | DGPs | DGP Mechanisms | Keywords | Generator.py |
|---|---:|---|---|---|
| A Negative Correlation Strategy for Bracketing in Difference-in-Differences (JASA) | 1 | [DGP did-ye-2024-bracketing-v1 (English title required)](registry/drafts/did-ye-2024-bracketing-v1.md) | Linearity · Panel data | [generator.py](registry/generators/did-ye-2024-bracketing-v1.py) |
| A semiparametric instrumented difference-in-differences approach to policy learning (Biometrika) | 1 | [DGP did-zhao-cui-2025-instrumented-v1 (English title required)](registry/drafts/did-zhao-cui-2025-instrumented-v1.md) | Interactions · Nonlinearity · Effect heterogeneity | [generator.py](registry/generators/did-zhao-cui-2025-instrumented-v1.py) |
| [Doubly robust difference-in-differences estimators](https://doi.org/10.1016/j.jeconom.2020.06.003) (JoE) | 1 | [Sant'Anna--Zhao DGP1: two-period panel with covariate-specific trends](registry/drafts/did-santanna-zhao-2020-panel-dgp1-v1.md) | Interactions · Nonlinearity · Panel data | [generator.py](registry/generators/did-santanna-zhao-2020-panel-dgp1-v1.py) |

### [Needs classification](registry/by-domain/unclassified.md)

2 paper(s) · 3 DGP mechanism(s)

| Paper Title | DGPs | DGP Mechanisms | Keywords | Generator.py |
|---|---:|---|---|---|
| [Generalized random forests](https://doi.org/10.1214/18-aos1709) (AoS) | 2 | 1: [Conditional quantile under Athey-Tibshirani-Wager Figure 2 mean shift](registry/drafts/qr-athey-tibshirani-wager-2019-mean-v1.md)<br/>2: [Conditional quantile under Athey-Tibshirani-Wager Figure 2 scale shift](registry/drafts/qr-athey-tibshirani-wager-2019-scale-v1.md) | 1: Nonlinearity<br/>2: Nonlinearity · Heteroskedasticity | [1: generator.py](registry/generators/qr-athey-tibshirani-wager-2019-mean-v1.py)<br/>[2: generator.py](registry/generators/qr-athey-tibshirani-wager-2019-scale-v1.py) |
| [On the Effect of Bias Estimation on Coverage Accuracy in Nonparametric Inference](https://doi.org/10.1080/01621459.2017.1285776) (JASA) | 1 | [DGP nri-calonico-2018-asymmetric-sine-v1 (English title required)](registry/drafts/nri-calonico-2018-asymmetric-sine-v1.md) | Nonlinearity | [generator.py](registry/generators/nri-calonico-2018-asymmetric-sine-v1.py) |

<!-- STATSARENA_PAPER_LIST_END -->

After the ZIP commit, see **Actions → DGP submissions**. The bot updates [`registry/INDEX.md`](registry/INDEX.md) and the six catalog pages on successful runs; no deployment or model key is involved.

## Example and format

The downloadable [`examples/proximal_10_dgps.zip`](examples/proximal_10_dgps.zip) is a structured test archive (10 DGPs, 11 scenarios from 7 papers). For required fields and limitations, see [ZIP format](docs/ZIP_FORMAT.md) and [Contributing](CONTRIBUTING.md).

### Safety and limitations

Submitted ZIPs are treated as **data only**, never executed. The catalog shows extracted text and submitted truth values with **Needs scientific review** labels. The archive format requires structured `collection.json` and `config.json`. If the ZIP only contains a raw PDF or random Python code, deterministic extraction is not possible without additional author-supplied structure.

**GitHub-native limitation:** This is GitHub's normal file-upload page, not a custom domain-selection form. DGP area comes from the ZIP's `collection.json` `family` field. Automatic indexing requires the checked-in `../.github/workflows/dgp-submissions.yml` workflow and Actions permission to write generated draft catalog files.
