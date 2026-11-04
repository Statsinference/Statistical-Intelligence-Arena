# Conditional quantile in the Bondell-Reich-Wang linear location-scale mechanism

> **Unverified extraction — scientific review required.**

**Primary area:** Quantile Inference

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Bondell, H. D., Reich, B. J. and Wang, H. (2010). Noncrossing quantile regression curve estimation. Biometrika 97(4), 825-838. DOI: 10.1093/biomet/asq048.

**DOI:** 10.1093/biomet/asq048 · **Source locator:** Section 4.1, unnumbered location-scale model on PDF page 7 = journal page 831; beta0=gamma0=1 in same paragraph; Example 1 parameters on PDF page 8 = journal page 832.

## DGP / generation mechanism

**Sampling design:** Unit: One fully observed independent row (X,Y); Dependence: IID rows; coordinate and noise independence as recorded in equations and source adaptations.

**Generator source:** [generator.py](../generators/qdi-bondell-reich-wang-2010-linear-scale-v2.py)

**Keywords (source-described):** Linearity · Heteroskedasticity

**Observed variables**

X1, X2, X3, X4, Y

**Latent variables**

Not explicitly identified (review required)

**Latent-variable identification:** explicit structured metadata

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

**Original source equations (verbatim):** [Open raw scientific record (JSON)](./qdi-bondell-reich-wang-2010-linear-scale-v2.json).

**E1**

$$
X_{ij}\overset{\mathrm{iid}}{\sim}U(0,1),\quad\varepsilon_i\sim\mathcal N(0,1),\quad\varepsilon_i\perp X_i
$$

The displayed marginals are source-supported; the independence/product-sampling part is a declared implementation convention. See source_recheck.json.

**E2**

$$
Y_i=1+\sum_{j=1}^4X_{ij}+\left(1+0.1\sum_{j=1}^4X_{ij}\right)\varepsilon_i
$$

**E3**

$$
Q_\tau(x)=1+\sum_{j=1}^4x_j+\left(1+0.1\sum_{j=1}^4x_j\right)\Phi^{-1}(\tau)
$$


## Parameter scenarios, estimands and truth

| Scenario | Estimand | Definition | True value | Evidence status |
|---|---|---|---|---|
| source_law_fixed_query | Q_{0.9}(x_query) | Conditional 0.9 quantile at X=(0.5,0.5,0.5,0.5) in source Example 1. | 4.537861878653521 | reported_numeric |

## Identifiability assumptions

- Independent, identically distributed fully observed rows from the stated synthetic population.
- All noise variables are independent of observed covariates; coordinate dependence is exactly as stated in equations and implementation conventions.
- Quantiles use the left generalized inverse inf{y:F(y)&gt;=tau}; the selected continuous law has positive density at the registered quantile.

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Warnings:**

- Nothing automatically flagged; this does NOT equal scientific acceptance.
