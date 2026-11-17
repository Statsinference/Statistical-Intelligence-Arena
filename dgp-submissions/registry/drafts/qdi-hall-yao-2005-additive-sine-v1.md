# Conditional CDF in the Hall-Yao additive sine mechanism

> **Unverified extraction — scientific review required.**

**Primary area:** Quantile Inference

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Hall, P. and Yao, Q. (2005). Approximating conditional distribution functions using dimension reduction. The Annals of Statistics 33(3), 1404-1421. DOI: 10.1214/009053604000001282.

**DOI:** 10.1214/009053604000001282 · **Source locator:** Section 4, Example 2; PDF page 12 = journal page 1415; unnumbered model. Distribution and total independence of X_ij and epsilon_i specified on PDF page 10 = journal page 1413.

## DGP / generation mechanism

**Sampling design:** Unit: One fully observed independent row (X,Y); Dependence: IID rows; coordinate and noise independence as recorded in equations and source adaptations.

**Generator source:** [generator.py](../generators/qdi-hall-yao-2005-additive-sine-v1.py)

**Keywords (source-described):** Nonlinearity

**Observed variables**

X1–X4 (4 variables), Y

<details>
<summary>All observed variable names</summary>

X1, X2, X3, X4, Y

</details>

**Latent variables**

Not explicitly identified (review required)

**Latent-variable identification:** explicit structured metadata

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

**Original source equations (verbatim):** [Open raw scientific record (JSON)](./qdi-hall-yao-2005-additive-sine-v1.json).

**E1**

```math
X_{ij},\varepsilon_i\overset{\mathrm{ind}}{\sim}\mathcal N(0,1),\quad j=1,\ldots,4
```

**E2**

```math
Y_i=\frac12\sum_{j=1}^4\sin(X_{ij})+\varepsilon_i
```

**E3**

```math
F_{Y\mid X}(y\mid x)=\Phi\!\left(y-\frac12\sum_{j=1}^4\sin x_j\right)
```


## Parameter scenarios, estimands and truth

| Scenario | Estimand | Definition | Reported value |
|---|---|---|---|
| source_law_fixed_query | Conditional cumulative distribution function | Conditional CDF P(Y&lt;=0.5 \| X=(0.5,0.25,-0.5,1)); conditioning is on the full four-dimensional X, not on the fitted index. | 0.4822778463878529 |

**Original submitted target notation:** F_{Y\|X}(0.5\|x_query)


## Identifiability assumptions

- Independent, identically distributed fully observed rows from the stated synthetic population.
- All noise variables are independent of observed covariates; coordinate dependence is exactly as stated in equations and implementation conventions.
- The conditional CDF conditions on all four covariates and uses the finite threshold stated in config; no single-index approximation is treated as the exact CDF.

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Adaptations from the source (submitted, unverified):**

- The full-X conditional CDF at a fixed query is used instead of the source least-squares single-index approximation; source data law is retained.
- Independent Python/NumPy implementation from mathematical formulas; no author code is redistributed. PCG64(seed) replaces unspecified/source software random-number generation. Sample size is the generate n argument; source_n only records the published sample sizes. No fitting, bootstrap, confidence-band coverage experiment or PFN training is included.

**Warnings:**

- Nothing automatically flagged; this does NOT equal scientific acceptance.
