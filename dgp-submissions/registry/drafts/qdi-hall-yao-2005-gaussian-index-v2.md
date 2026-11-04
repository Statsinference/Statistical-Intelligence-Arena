# Marginal quantile in the Hall-Yao Gaussian single-index mechanism

> **Unverified extraction — scientific review required.**

**Primary area:** Quantile Inference

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Hall, P. and Yao, Q. (2005). Approximating conditional distribution functions using dimension reduction. The Annals of Statistics 33(3), 1404-1421. DOI: 10.1214/009053604000001282.

**DOI:** 10.1214/009053604000001282 · **Source locator:** Section 4, Example 1; PDF page 10 = journal page 1413; unnumbered model immediately below Example 1. Independence specified in preceding paragraph.

## DGP / generation mechanism

**Sampling design:** Unit: One fully observed independent row (X,Y); Dependence: IID rows; coordinate and noise independence as recorded in equations and source adaptations.

**Generator source:** [generator.py](../generators/qdi-hall-yao-2005-gaussian-index-v2.py)

**Keywords (source-described):** Linearity

**Observed variables**

X1, X2, X3, X4, Y

**Latent variables**

Not explicitly identified (review required)

**Latent-variable identification:** explicit structured metadata

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

**Original source equations (verbatim):** [Open raw scientific record (JSON)](./qdi-hall-yao-2005-gaussian-index-v2.json).

**E1**

$$
X_{ij},\varepsilon_i\overset{\mathrm{ind}}{\sim}\mathcal N(0,1),\quad j=1,\ldots,4
$$

**E2**

$$
Y_i=\frac{X_{i1}+2X_{i2}+3X_{i4}}{\sqrt{14}}+\varepsilon_i
$$

**E3**

$$
Q_Y(0.9)=\sqrt 2\,\Phi^{-1}(0.9)
$$


## Parameter scenarios, estimands and truth

| Scenario | Estimand | Definition | True value | Evidence status |
|---|---|---|---|---|
| source_law_fixed_query | Q_Y(0.9) | Marginal population quantile Q_Y(tau)=inf{y:P(Y&lt;=y)&gt;=tau}, tau=0.9; X is integrated over its N(0,I4) population, not fixed at zero. | 1.8123876048736471 | reported_numeric |

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
