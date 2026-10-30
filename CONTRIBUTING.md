# Contributing to Statistical Inference Arena

**100% GitHub-native · Structured ZIP → automatic DGP catalog · No Issue · No LLM API · No other website**

<p align="center">
  <a href="/../../upload/main/dgp-submissions/incoming"><img alt="Upload a DGP ZIP directly to this repository" src="https://img.shields.io/badge/Submit_DGP-Upload_ZIP-1677C8?style=for-the-badge" /></a>
  <a href="dgp-submissions/registry/INDEX.md"><img alt="Browse research areas" src="https://img.shields.io/badge/Browse-DGP_Research_Areas-444444?style=for-the-badge" /></a>
  <a href="dgp-submissions/CONTRIBUTING.md"><img alt="Contribution instructions" src="https://img.shields.io/badge/How_to_Contribute-Read_Guide-007F73?style=for-the-badge" /></a>
</p>

## For students — 3 steps, all on GitHub

1. **Outside collaborators (Read):** first fork the private repository into your own GitHub account. Open **your fork**, then click **Submit DGP**. The button opens GitHub's **file-upload page directly**, targeting `dgp-submissions/incoming/` on the `main` branch **of the repository you are viewing**. Check that the repository owner in the URL is your username, not `Statsinference`.
2. **Drag and drop your structured `.zip`, or click “choose your files”.** Click **Commit changes** to save it to your fork. Your fork's `main` is separate from the upstream repository's `main`; uploading here does not submit or merge anything upstream.
3. In your fork, choose **Contribute → Open pull request** and target `Statsinference/stats-inference-arena:main`. The **DGP ZIP-only** check runs before a maintainer reviews and merges; the catalog updates only after merging.

**Already have a fork?** Use **Sync fork → Update branch** to obtain this updated upload button, then reopen this page in your fork. The button follows the repository you are viewing; it does not automatically find your fork when clicked on the upstream page.

Maintainers with upstream Write permission may commit ZIPs directly to the upstream repository instead. **Outside collaborators do not need upstream Write permission.** Do not use an upstream upload URL from inside your fork.

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

[Submission processing report](dgp-submissions/registry/INTAKE_REPORT.md)

## Browse research areas

[ATE](dgp-submissions/registry/by-domain/ate.md) · [CATE](dgp-submissions/registry/by-domain/cate.md) · [Mediation](dgp-submissions/registry/by-domain/mediation.md) · [IV](dgp-submissions/registry/by-domain/iv.md) · [Proximal Causal Inference](dgp-submissions/registry/by-domain/proximal.md) · [DiD / Synthetic Control](dgp-submissions/registry/by-domain/did_sc.md) · [Nonparametric Regression](dgp-submissions/registry/by-domain/nonparametric_regression.md) · [Quantile Inference](dgp-submissions/registry/by-domain/quantile.md) · [Semi-Supervised Inference](dgp-submissions/registry/by-domain/semi_supervised.md) · [Missing Data](dgp-submissions/registry/by-domain/missing_data.md)

<!-- STATSARENA_PAPER_LIST_BEGIN -->

## Paper list by research area

Each paper is listed **once per area**. Generators are source files from the submitted ZIP, not executed or automatically validated.

**Keywords** describe each submitted DGP, not the whole paper. Missing tags do not prove absence; nonlinearity may occur in any part of the mechanism. Numbered entries match the DGP mechanisms and generators in the same row.

### [ATE — Average Treatment Effect](dgp-submissions/registry/by-domain/ate.md)

5 paper(s) · 12 DGP mechanism(s)

| Paper Title | DGPs | DGP Mechanisms | Keywords | Generator.py |
|---|---:|---|---|---|
| [A robust and efficient approach to causal inference based on sparse sufficient dimension reduction](https://doi.org/10.1214/18-aos1722) (AoS) | 2 | 1: [Interaction assignment and quadratic outcomes](dgp-submissions/registry/drafts/ate-ma-zhu-zhang-tsai-carroll-2019-06-01-model-1-v1.md)<br/>2: [Linear assignment and cross-product outcomes](dgp-submissions/registry/drafts/ate-ma-zhu-zhang-tsai-carroll-2019-06-01-model-2-v1.md) | 1: Interactions · Nonlinearity<br/>2: Interactions · Nonlinearity | [1: generator.py](dgp-submissions/registry/generators/ate-ma-zhu-zhang-tsai-carroll-2019-06-01-model-1-v1.py)<br/>[2: generator.py](dgp-submissions/registry/generators/ate-ma-zhu-zhang-tsai-carroll-2019-06-01-model-2-v1.py) |
| [Estimation and Inference of Heterogeneous Treatment Effects using Random Forests](https://doi.org/10.1080/01621459.2017.1319839) (JASA) | 2 | 1: [Null Treatment Effect with Nonlinear Propensity Scores and Observed Confounding](dgp-submissions/registry/drafts/ate-wager-athey-2018-confounded-null-v1.md)<br/>2: [Rare independent response mixture](dgp-submissions/registry/drafts/ate-wager-athey-2018-06-06-rare-response-v1.md) | 1: Nonlinearity<br/>2: Linearity | [1: generator.py](dgp-submissions/registry/generators/ate-wager-athey-2018-confounded-null-v1.py)<br/>[2: generator.py](dgp-submissions/registry/generators/ate-wager-athey-2018-06-06-rare-response-v1.py) |
| [Joint sufficient dimension reduction and estimation of conditional and average treatment effects](https://doi.org/10.1093/biomet/asx028) (Biometrika) | 1 | [Transformed Gaussian covariates and latent-linear outcomes](dgp-submissions/registry/drafts/ate-huang-chan-2017-05-19-setting-2-v1.md) | Interactions · Nonlinearity | [generator.py](dgp-submissions/registry/generators/ate-huang-chan-2017-05-19-setting-2-v1.py) |
| [Quasi-oracle estimation of heterogeneous treatment effects](https://doi.org/10.1093/biomet/asaa076) (Biometrika) | 6 | 1: [ATE under Nie--Wager Setup A: nonlinear confounding and heterogeneous effects](dgp-submissions/registry/drafts/ate-nie-wager-2021-a-v1.md)<br/>2: [Confounded constant effect with softplus baseline](dgp-submissions/registry/drafts/ate-nie-wager-2020-09-24-setup-c-v1.md)<br/>3: [Random assignment and discontinuous threshold effect](dgp-submissions/registry/drafts/ate-nie-wager-2020-09-24-eq9-discontinuous-v1.md)<br/>4: [Random assignment and smooth sigmoid-difference effect](dgp-submissions/registry/drafts/ate-nie-wager-2020-09-24-eq9-smooth-v1.md)<br/>5: [Random assignment and softplus heterogeneous effects](dgp-submissions/registry/drafts/ate-nie-wager-2020-09-24-setup-b-v1.md)<br/>6: [Three-term assignment and unrelated positive-part outcomes](dgp-submissions/registry/drafts/ate-nie-wager-2020-09-24-setup-d-v1.md) | 1: Interactions · Nonlinearity · Effect heterogeneity<br/>2: Nonlinearity<br/>3: Interactions · Nonlinearity · Effect heterogeneity<br/>4: Interactions · Nonlinearity<br/>5: Interactions · Nonlinearity · Effect heterogeneity<br/>6: Interactions · Nonlinearity | [1: generator.py](dgp-submissions/registry/generators/ate-nie-wager-2021-a-v1.py)<br/>[2: generator.py](dgp-submissions/registry/generators/ate-nie-wager-2020-09-24-setup-c-v1.py)<br/>[3: generator.py](dgp-submissions/registry/generators/ate-nie-wager-2020-09-24-eq9-discontinuous-v1.py)<br/>[4: generator.py](dgp-submissions/registry/generators/ate-nie-wager-2020-09-24-eq9-smooth-v1.py)<br/>[5: generator.py](dgp-submissions/registry/generators/ate-nie-wager-2020-09-24-setup-b-v1.py)<br/>[6: generator.py](dgp-submissions/registry/generators/ate-nie-wager-2020-09-24-setup-d-v1.py) |
| [Robust estimation of causal effects via a high-dimensional covariate balancing propensity score](https://doi.org/10.1093/biomet/asaa020) (Biometrika) | 1 | [Correlated high-dimensional Gaussian linear outcomes](dgp-submissions/registry/drafts/ate-ning-peng-imai-2020-06-03-ar1-linear-v1.md) | Interactions · Nonlinearity · High-dimensionality | [generator.py](dgp-submissions/registry/generators/ate-ning-peng-imai-2020-06-03-ar1-linear-v1.py) |

### [CATE — Conditional Average Treatment Effect](dgp-submissions/registry/by-domain/cate.md)

2 paper(s) · 2 DGP mechanism(s)

| Paper Title | DGPs | DGP Mechanisms | Keywords | Generator.py |
|---|---:|---|---|---|
| [Estimation and Inference of Heterogeneous Treatment Effects using Random Forests](https://doi.org/10.1080/01621459.2017.1319839) (JASA) | 1 | [Pointwise CATE under Randomized Treatment with Logistic Interaction Effects](dgp-submissions/registry/drafts/cate-wager-athey-2018-logistic-v1.md) | Interactions · Nonlinearity · Effect heterogeneity | [generator.py](dgp-submissions/registry/generators/cate-wager-athey-2018-logistic-v1.py) |
| [Generalized Random Forests](https://doi.org/10.1214/18-aos1709) (AoS) | 1 | [Pointwise CATE with Confounding and Logistic Interaction Effects](dgp-submissions/registry/drafts/cate-athey-tibshirani-wager-2019-confounded-v1.md) | Interactions · Nonlinearity · Effect heterogeneity | [generator.py](dgp-submissions/registry/generators/cate-athey-tibshirani-wager-2019-confounded-v1.py) |

### [Mediation — Direct and Indirect Effects](dgp-submissions/registry/by-domain/mediation.md)

1 paper(s) · 1 DGP mechanism(s)

| Paper Title | DGPs | DGP Mechanisms | Keywords | Generator.py |
|---|---:|---|---|---|
| [Semiparametric theory for causal mediation analysis: efficiency bounds, multiple robustness and sensitivity analysis](https://doi.org/10.1214/12-aos990) (AoS) | 1 | [Natural indirect effect in the Tchetgen Tchetgen–Shpitser mediation design](dgp-submissions/registry/drafts/nie-eric-original-v1.md) | Interactions · Nonlinearity | [generator.py](dgp-submissions/registry/generators/nie-eric-original-v1.py) |

### [IV — Instrumental Variables](dgp-submissions/registry/by-domain/iv.md)

5 paper(s) · 5 DGP mechanism(s)

| Paper Title | DGPs | DGP Mechanisms | Keywords | Generator.py |
|---|---:|---|---|---|
| Deep IV: A Flexible Approach for Counterfactual Prediction (ICML) | 1 | [IV: DeepIV raw-unit demand with endogenous continuous price](dgp-submissions/registry/drafts/iv-hartford-2017-demand-v1.md) | Interactions · Nonlinearity | [generator.py](dgp-submissions/registry/generators/iv-hartford-2017-demand-v1.py) |
| [Generalized random forests](https://doi.org/10.1214/18-aos1709) (AoS) | 1 | [Endogenous Noncompliance and Local Treatment Effects](dgp-submissions/registry/drafts/iv-athey-tibshirani-wager-2019-compliance-v1.md) | Interactions · Nonlinearity | [generator.py](dgp-submissions/registry/generators/iv-athey-tibshirani-wager-2019-compliance-v1.py) |
| [Instrumental variables as bias amplifiers with general outcome and confounding](https://doi.org/10.1093/biomet/asx009) (Biometrika) | 1 | [DGP iv-ding-2017-binary-bias-v1 (English title required)](dgp-submissions/registry/drafts/iv-ding-2017-binary-bias-v1.md) | Interactions · Nonlinearity | [generator.py](dgp-submissions/registry/generators/iv-ding-2017-binary-bias-v1.py) |
| [Instrumental Variables Estimation With Some Invalid Instruments and its Application to Mendelian Randomization](https://doi.org/10.1080/01621459.2014.994705) (JASA) | 1 | [Partially Invalid Instruments with Linear Endogenous Treatment](dgp-submissions/registry/drafts/iv-kang-2016-invalid-linear-v1.md) | Linearity | [generator.py](dgp-submissions/registry/generators/iv-kang-2016-invalid-linear-v1.py) |
| Minimax Estimation of Conditional Moment Models (NeurIPS) | 1 | [IV: sine structural response with Gaussian confounding](dgp-submissions/registry/drafts/iv-dikkala-2020-sine-v1.md) | Nonlinearity | [generator.py](dgp-submissions/registry/generators/iv-dikkala-2020-sine-v1.py) |

### [Proximal Causal Inference](dgp-submissions/registry/by-domain/proximal.md)

7 paper(s) · 10 DGP mechanism(s)

| Paper Title | DGPs | DGP Mechanisms | Keywords | Generator.py |
|---|---:|---|---|---|
| [Long-term causal inference under persistent confounding via data combination](https://doi.org/10.1093/jrsssb/qkae095) (JRSSB) | 1 | [Sequential Proxies and Long-Term Causal Effects from Combined Data](dgp-submissions/registry/drafts/proximal-imbens-2025-longterm-v1.md) | Nonlinearity | [generator.py](dgp-submissions/registry/generators/proximal-imbens-2025-longterm-v1.py) |
| [Proximal causal inference for complex longitudinal studies](https://doi.org/10.1093/jrsssb/qkad020) (JRSSB) | 1 | [Two-Period Treatment with Time-Varying Confounding and Feedback](dgp-submissions/registry/drafts/proximal-ying-2023-longitudinal-v1.md) | Nonlinearity | [generator.py](dgp-submissions/registry/generators/proximal-ying-2023-longitudinal-v1.py) |
| [Proximal indirect comparison](https://doi.org/10.1093/biomet/asaf044) (Biometrika) | 1 | [Cross-Trial Transportability with Unmeasured Effect Modification](dgp-submissions/registry/drafts/proximal-su-2026-transport-v1.md) | Interactions · Nonlinearity · Effect heterogeneity | [generator.py](dgp-submissions/registry/generators/proximal-su-2026-transport-v1.py) |
| [Proximal Learning for Individualized Treatment Regimes Under Unmeasured Confounding](https://doi.org/10.1080/01621459.2022.2147841) (JASA) | 3 | 1: [Absolute-Value and Trigonometric Proxy Interactions (N1)](dgp-submissions/registry/drafts/proximal-qi-2024-trigonometric-v1.md)<br/>2: [Linear Heterogeneous Treatment Effect Bridge (L1/L2)](dgp-submissions/registry/drafts/proximal-qi-2024-linear-itr-v1.md)<br/>3: [Quadratic Baseline Effects and Product Treatment Effect (N2)](dgp-submissions/registry/drafts/proximal-qi-2024-quadratic-v1.md) | 1: Interactions · Nonlinearity<br/>2: Interactions · Nonlinearity · Effect heterogeneity<br/>3: Interactions · Nonlinearity | [1: generator.py](dgp-submissions/registry/generators/proximal-qi-2024-trigonometric-v1.py)<br/>[2: generator.py](dgp-submissions/registry/generators/proximal-qi-2024-linear-itr-v1.py)<br/>[3: generator.py](dgp-submissions/registry/generators/proximal-qi-2024-quadratic-v1.py) |
| [Proximal mediation analysis](https://doi.org/10.1093/biomet/asad015) (Biometrika) | 1 | [Natural Direct Effect under Unmeasured Confounding](dgp-submissions/registry/drafts/proximal-dukes-2023-mediation-v1.md) | Nonlinearity | [generator.py](dgp-submissions/registry/generators/proximal-dukes-2023-mediation-v1.py) |
| [Semiparametric Proximal Causal Inference](https://doi.org/10.1080/01621459.2023.2191817) (JASA) | 1 | [Linear Bridge Model with Constant ATE](dgp-submissions/registry/drafts/proximal-cui-2024-linear-v1.md) | Nonlinearity | [generator.py](dgp-submissions/registry/generators/proximal-cui-2024-linear-v1.py) |
| [Theory for Identification and Inference with Synthetic Controls: A Proximal Causal Inference Framework](https://doi.org/10.1080/01621459.2026.2639734) (JASA) | 2 | 1: [Poisson Synthetic Control with Truncated Normal Factors](dgp-submissions/registry/drafts/proximal-shi-2026-sc-poisson-v1.md)<br/>2: [Stationary Multifactor Gaussian Synthetic Control](dgp-submissions/registry/drafts/proximal-shi-2026-sc-gaussian-v1.md) | 1: Nonlinearity · Panel data<br/>2: Linearity · Panel data | [1: generator.py](dgp-submissions/registry/generators/proximal-shi-2026-sc-poisson-v1.py)<br/>[2: generator.py](dgp-submissions/registry/generators/proximal-shi-2026-sc-gaussian-v1.py) |

### [DiD / Synthetic Control](dgp-submissions/registry/by-domain/did_sc.md)

3 paper(s) · 3 DGP mechanism(s)

| Paper Title | DGPs | DGP Mechanisms | Keywords | Generator.py |
|---|---:|---|---|---|
| A Negative Correlation Strategy for Bracketing in Difference-in-Differences (JASA) | 1 | [DGP did-ye-2024-bracketing-v1 (English title required)](dgp-submissions/registry/drafts/did-ye-2024-bracketing-v1.md) | Linearity · Panel data | [generator.py](dgp-submissions/registry/generators/did-ye-2024-bracketing-v1.py) |
| A semiparametric instrumented difference-in-differences approach to policy learning (Biometrika) | 1 | [DGP did-zhao-cui-2025-instrumented-v1 (English title required)](dgp-submissions/registry/drafts/did-zhao-cui-2025-instrumented-v1.md) | Interactions · Nonlinearity · Effect heterogeneity | [generator.py](dgp-submissions/registry/generators/did-zhao-cui-2025-instrumented-v1.py) |
| [Doubly robust difference-in-differences estimators](https://doi.org/10.1016/j.jeconom.2020.06.003) (JoE) | 1 | [Sant'Anna--Zhao DGP1: two-period panel with covariate-specific trends](dgp-submissions/registry/drafts/did-santanna-zhao-2020-panel-dgp1-v1.md) | Interactions · Nonlinearity · Panel data | [generator.py](dgp-submissions/registry/generators/did-santanna-zhao-2020-panel-dgp1-v1.py) |

### [Nonparametric Regression](dgp-submissions/registry/by-domain/nonparametric_regression.md)

2 paper(s) · 2 DGP mechanism(s)

| Paper Title | DGPs | DGP Mechanisms | Keywords | Generator.py |
|---|---:|---|---|---|
| [A simple bootstrap method for constructing nonparametric confidence bands for functions](https://doi.org/10.1214/13-aos1137) (AoS) | 1 | [Hall--Horowitz Gaussian bump on a linear trend: pointwise regression-mean inference](dgp-submissions/registry/drafts/nri-hall-horowitz-2013-gaussian-bump-v1.md) | Nonlinearity | [generator.py](dgp-submissions/registry/generators/nri-hall-horowitz-2013-gaussian-bump-v1.py) |
| [On the Effect of Bias Estimation on Coverage Accuracy in Nonparametric Inference](https://doi.org/10.1080/01621459.2017.1285776) (JASA) | 1 | [DGP nri-calonico-2018-asymmetric-sine-v1 (English title required)](dgp-submissions/registry/drafts/nri-calonico-2018-asymmetric-sine-v1.md) | Nonlinearity | [generator.py](dgp-submissions/registry/generators/nri-calonico-2018-asymmetric-sine-v1.py) |

### [Quantile Inference](dgp-submissions/registry/by-domain/quantile.md)

2 paper(s) · 3 DGP mechanism(s)

| Paper Title | DGPs | DGP Mechanisms | Keywords | Generator.py |
|---|---:|---|---|---|
| [Generalized random forests](https://doi.org/10.1214/18-aos1709) (AoS) | 2 | 1: [Conditional quantile under Athey-Tibshirani-Wager Figure 2 mean shift](dgp-submissions/registry/drafts/qr-athey-tibshirani-wager-2019-mean-v1.md)<br/>2: [Conditional quantile under Athey-Tibshirani-Wager Figure 2 scale shift](dgp-submissions/registry/drafts/qr-athey-tibshirani-wager-2019-scale-v1.md) | 1: Nonlinearity<br/>2: Nonlinearity · Heteroskedasticity | [1: generator.py](dgp-submissions/registry/generators/qr-athey-tibshirani-wager-2019-mean-v1.py)<br/>[2: generator.py](dgp-submissions/registry/generators/qr-athey-tibshirani-wager-2019-scale-v1.py) |
| [High-Dimensional Quantile Regression: Convolution Smoothing and Concave Regularization](https://doi.org/10.1111/rssb.12485) (JRSSB) | 1 | [QDI: active-coordinate Gaussian-mixture marginal of the Tan-Wang-Zhou design (10-dimensional adaptation)](dgp-submissions/registry/drafts/qdi-tan-wang-zhou-20220201-active10-mixture-v2.md) | Linearity | [generator.py](dgp-submissions/registry/generators/qdi-tan-wang-zhou-20220201-active10-mixture-v2.py) |

### [Semi-Supervised Inference](dgp-submissions/registry/by-domain/semi_supervised.md)

7 paper(s) · 8 DGP mechanism(s)

| Paper Title | DGPs | DGP Mechanisms | Keywords | Generator.py |
|---|---:|---|---|---|
| A General M-estimation Theory in Semi-Supervised Framework (JASA) | 2 | 1: [Linear projection under correlated nonlinear regression with shared noise](dgp-submissions/registry/drafts/sspi-song-2024-nonlinear-noise-projection-v1.md)<br/>2: [Logistic projection under an even nonlinear Gaussian-mixture response](dgp-submissions/registry/drafts/sspi-song-2024-even-mixture-logistic-projection-v1.md) | 1: Nonlinearity · Heteroskedasticity<br/>2: Interactions · Nonlinearity · Heteroskedasticity | [1: generator.py](dgp-submissions/registry/generators/sspi-song-2024-nonlinear-noise-projection-v1.py)<br/>[2: generator.py](dgp-submissions/registry/generators/sspi-song-2024-even-mixture-logistic-projection-v1.py) |
| Extreme Value Statistics in Semi-Supervised Models (JASA) | 1 | [Extreme quantile with a tail-dependent Cauchy auxiliary variable](dgp-submissions/registry/drafts/sspi-ahmed-2025-cauchy-tail-quantile-v1.md) | Nonlinearity | [generator.py](dgp-submissions/registry/generators/sspi-ahmed-2025-cauchy-tail-quantile-v1.py) |
| High-dimensional semi-supervised learning: in search of optimal inference of the mean (Biometrika) | 1 | [Cosine single-index mean with Gaussian covariates](dgp-submissions/registry/drafts/sspi-zhang-bradic-2022-cosine-index-v1.md) | Interactions · Nonlinearity | [generator.py](dgp-submissions/registry/generators/sspi-zhang-bradic-2022-cosine-index-v1.py) |
| Predictions as Surrogates: Revisiting Surrogate Outcomes in the Age of AI (Biometrika) | 1 | [Population mean with a miscalibrated three-level surrogate](dgp-submissions/registry/drafts/sspi-ji-2026-discrete-surrogate-mean-v1.md) | Nonlinearity | [generator.py](dgp-submissions/registry/generators/sspi-ji-2026-discrete-surrogate-mean-v1.py) |
| Semi-supervised distribution learning (Biometrika) | 1 | [Marginal distribution inference with sparse Gaussian linear signal](dgp-submissions/registry/drafts/sspi-wen-2025-gaussian-cdf-v1.md) | Linearity | [generator.py](dgp-submissions/registry/generators/sspi-wen-2025-gaussian-cdf-v1.py) |
| Semi-Supervised Linear Regression (JASA) | 1 | [Best linear slope under a quadratic Gaussian response](dgp-submissions/registry/drafts/sspi-azriel-2022-quadratic-projection-v1.md) | Nonlinearity | [generator.py](dgp-submissions/registry/generators/sspi-azriel-2022-quadratic-projection-v1.py) |
| Semisupervised inference for explained variance in high dimensional linear regression and its applications (JRSSB) | 1 | [Explained variance for dense decaying regression with AR covariance](dgp-submissions/registry/drafts/sspi-cai-guo-2020-dense-explained-variance-v1.md) | Linearity · High-dimensionality | [generator.py](dgp-submissions/registry/generators/sspi-cai-guo-2020-dense-explained-variance-v1.py) |

### [Missing Data](dgp-submissions/registry/by-domain/missing_data.md)

0 paper(s) · 0 DGP mechanism(s)

| Paper Title | DGPs | DGP Mechanisms | Keywords | Generator.py |
|---|---:|---|---|---|
| — | 0 | No submissions yet | — | — |

<!-- STATSARENA_PAPER_LIST_END -->

After the ZIP commit, see **Actions → DGP submissions**. The bot updates [`registry/INDEX.md`](dgp-submissions/registry/INDEX.md) and the six catalog pages on successful runs; no deployment or model key is involved.

## Example and format

The downloadable [`examples/proximal_10_dgps.zip`](dgp-submissions/examples/proximal_10_dgps.zip) is a structured test archive (10 DGPs, 11 scenarios from 7 papers). For required fields and limitations, see [ZIP format](dgp-submissions/docs/ZIP_FORMAT.md) and [Contributing](dgp-submissions/CONTRIBUTING.md).

### Safety and limitations

Submitted ZIPs are treated as **data only**, never executed. The catalog shows extracted text and submitted truth values with **Needs scientific review** labels. The archive format requires structured `collection.json` and `config.json`. If the ZIP only contains a raw PDF or random Python code, deterministic extraction is not possible without additional author-supplied structure.

**GitHub-native limitation:** This is GitHub's normal file-upload page, not a custom domain-selection form. DGP area comes from the ZIP's `collection.json` `family` field. Automatic indexing requires the checked-in `.github/workflows/dgp-submissions.yml` workflow and Actions permission to write generated draft catalog files.

## Existing benchmark documentation

The DGP collection service does not change the benchmark protocol, website, or starter code. See the [project README](README.md), [student guide](docs/student_guide_en.md), [scientific requirements](docs/contribution_en.md), and [starter](starter/README.md).
