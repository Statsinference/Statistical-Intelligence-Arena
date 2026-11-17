# DID_SC: target categories

> Labels are based on submitted estimand definitions and require scientific review.
> Original definitions, formulas, and values remain in each record.

**11 DGP mechanism(s).**

## Average treatment effect on the treated (ATT)

**5 DGP mechanism(s).**

| Paper | DGP mechanism | Standardized target | Original submitted name |
|---|---|---|---|
| A Penalized Synthetic Control Estimator for Disaggregated Data (JASA) | [Two-period nonlinear-covariate panel with a zero treatment effect](../drafts/did-abadie-lhour-2021-nonlinear-null-v1.md) | ATT | ATT_post |
| Using Penalized Synthetic Controls on Truncated Data: A Case Study on Effect of Marijuana Legalization on Direct Payments to Physicians by Opioid Manufacturers (JASA) | [History-selected cluster panel with renewal damping and zero-censored outcomes](../drafts/did-karmakar-2025-code-truncated-cluster-null-v1.md) | ATT | ATT |
| Doubly robust difference-in-differences estimators (JoE) | [Sant'Anna--Zhao DGP1: two-period panel with covariate-specific trends](../drafts/did-santanna-zhao-2020-panel-dgp1-v1.md) | ATT | ATT = E[Y_1(1)-Y_1(0) \| D=1] |
| A Negative Correlation Strategy for Bracketing in Difference-in-Differences (JASA) | [DGP did-ye-2024-bracketing-v1 (English title required)](../drafts/did-ye-2024-bracketing-v1.md) | ATT | ATT_4 |
| A Negative Correlation Strategy for Bracketing in Difference-in-Differences (JASA) | [Three-group Gaussian outcomes with nonparallel untreated trends](../drafts/did-ye-2024-code-case2-gaussian-bracketing-v1.md) | ATT | ATT_4 |

## Other mixed-category targets

**6 DGP mechanism(s).**

| Paper | DGP mechanism | Standardized target | Original submitted name |
|---|---|---|---|
| An Exact and Robust Conformal Inference Method for Counterfactual and Synthetic Controls (JASA) | [Donor-outcome-weighted panel with stationary AR(1) residuals](../drafts/did-cwz-2021-donor-ar-null-v1.md) | Treated-unit treatment effect | tau_T |
| On the Properties of the Synthetic Control Estimator with Many Periods and Many Controls (JASA) | [Two-type donor panel with stationary common AR(1) factors](../drafts/did-ferman-2021-two-factor-null-v1.md) | Treated-unit treatment effect | tau_01 |
| Randomization Tests in Observational Studies With Staggered Adoption of Treatment (JASA) | [First-adopter Cox adoption with AR(1) outcomes conditional on whole-experiment success](../drafts/did-shaikh-toulis-2021-conditional-first-adopter-null-v1.md) | Conditional first-adopter average treatment effect | ATT_cond |
| Theory for Identification and Inference with Synthetic Controls: A Proximal Causal Inference Framework (JASA) | [Truncated-normal-factor Poisson donor-and-proxy panel](../drafts/did-shi-2026-poisson-proxy-logrr-v1.md) | Treated-unit population log mean ratio | log_RR_pop |
| A semiparametric instrumented difference-in-differences approach to policy learning (Biometrika) | [Repeated-cross-sectional instrumented DiD with bridge confounding](../drafts/did-zhao-cui-2025-bridge-iv-v1.md) | ATE | ATE |
| A semiparametric instrumented difference-in-differences approach to policy learning (Biometrika) | [DGP did-zhao-cui-2025-instrumented-v1 (English title required)](../drafts/did-zhao-cui-2025-instrumented-v1.md) | ATE | ATE |

## Needs review

**0 DGP mechanism(s).**

No records currently assigned.

