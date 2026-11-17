# MAR mean response with ten Gaussian covariates and two active coordinates

> **Unverified extraction — scientific review required.**

**Primary area:** Missing Data

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Hu, Z., Follmann, D. A. and Wang, N. (2014). Estimation of mean response via the effective balancing score. Biometrika 101(3), 613–624. DOI: 10.1093/biomet/asu022.

**DOI:** 10.1093/biomet/asu022 · **Source locator:** Section 4, Numerical Studies, simulation 1, paragraph beginning 'In simulation 1' (PMC section anchor S15, paragraph P49).

## DGP / generation mechanism

**Sampling design:** Unit: individual; Dependence: iid

**Generator source:** [generator.py](../generators/mdi-hu-follmann-wang-2014-linear-balance-v2.py)

**Keywords (source-described):** Not specified

**Observed variables**

X1–X10 (10 variables), R, Y_observed

<details>
<summary>All observed variable names</summary>

X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, R, Y_observed

</details>

**Latent variables**

Not explicitly identified (review required)

**Latent-variable identification:** not explicitly specified

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

**Covariates**

X1,...,X10 mutually independent N(0,1)

**Full outcome**

```math
Y=3X_{1}+5X_{2}+\varepsilon, \varepsilon\text{ independent } \mathcal{N}(0,1)
```

**Observation**

```math
R\mid X\sim \mathrm{Bernoulli}(\mathrm{expit}(X_{1}))
```

R

independent of Y given X

**Observed encoding**

```math
Y_{\mathrm{observed}}=Y \text{ if } R=1
```

otherwise finite placeholder 0

**Target**

```math
\theta=\mathbb{E}(Y)=0
```

<details>
<summary>Original source equations (verbatim)</summary>

<pre>
X1,...,X10 mutually independent N(0,1)
Y=3X1+5X2+epsilon, epsilon independent N(0,1)
R|X~Bernoulli(expit(X1)); R independent of Y given X
Y_observed=Y if R=1; otherwise finite placeholder 0
theta=E(Y)=0
</pre>

</details>


## Parameter scenarios, estimands and truth

| Scenario | Estimand | Definition | Reported value |
|---|---|---|---|
| original | Full-data population outcome mean | Marginal full-data mean response for the iid superpopulation before Y is masked. | 0.0 |

**Original submitted target notation:** theta = E(Y)


## Identifiability assumptions

- Individuals iid; ten mutually independent N(0,1) covariates.
- MAR: R is independent of Y conditional on fully observed X1,...,X10.
- Observation probability expit(X1) is strictly positive at every finite X1, but has no uniform lower bound over Gaussian support.
- Independent mean-zero N(0,1) outcome noise.

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Adaptations from the source (submitted, unverified):**

- One generator call produces one iid sample; the paper compares estimators over 200 datasets with n=200 or n=1000.
- R=0 and finite Y_observed=0 encode missing Y for the numeric-only interface; always mask using R.

**Warnings:**

- No explicit latent-variable metadata or reliably identifiable latent declarations; absence from this list does not prove that no latent variables exist.
