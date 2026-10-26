# Conditional quantile under Athey-Tibshirani-Wager Figure 2 scale shift

> **Unverified extraction — scientific review required.**

**Primary area:** unclassified

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Athey, S., Tibshirani, J. and Wager, S. (2019). Generalized random forests. The Annals of Statistics 47(2), 1148-1178. DOI: 10.1214/18-AOS1709.

**DOI:** — · **Source locator:** arXiv v4 PDF p.19, Section 5, Figure 2 caption, right (scale shift) panel. Section 5 begins on p.18.

## DGP / generation mechanism

**Sampling design:** Unit: individual response and covariate vector; Dependence: iid rows; independent covariates; independent Gaussian response noise

**Generator source:** [generator.py](../generators/qr-athey-tibshirani-wager-2019-scale-v1.py)

**Keywords (source-described):** Nonlinearity · Heteroskedasticity

**Observed variables**

X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, X11, X12, X13, X14, X15, X16, X17, X18, X19, X20, X21, X22, X23, X24, X25, X26, X27, X28, X29, X30, X31, X32, X33, X34, X35, X36, X37, X38, X39, X40, Y

**Latent variables**

Not explicitly identified (review required)

**Latent-variable identification:** not explicitly specified

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

$$
X_j\overset{\mathrm{iid}}{\sim} \mathrm{Uniform}(-1,1), j=1,\ldots ,40
$$

$$
\varepsilon\sim \mathcal{N}(0,1)
$$

independent of all X_j

$$
Y=(1+I(X_{1}>0))\cdot \varepsilon
$$

$$
Q_q(Y\mid X=x)=(1+I(x_{1}>0))\cdot Phi_inverse(q)
$$

<details>
<summary>Original source equations (verbatim)</summary>

<pre>
X_j iid Uniform(-1,1), j=1,...,40
epsilon~Normal(0,1), independent of all X_j
Y=(1+I(X1&gt;0))*epsilon
Q_q(Y|X=x)=(1+I(x1&gt;0))*Phi_inverse(q)
</pre>

</details>


## Parameter scenarios, estimands and truth

| Scenario | Estimand | Definition | True value | Evidence status |
|---|---|---|---|---|
| source_p40_q90_positive_query | theta = Q_0.9(Y \| X=x_query) | Conditional 90th percentile of the observed response at x_query=(0.5,0,...,0) in the 40-dimensional covariate support; inf{y:P(Y&lt;=y\|X=x_query)&gt;=0.9}. A conditional quantile regression target, not a quantile treatment effect, population marginal quantile or causal estimand. | 2.5631031310892016 | reported_numeric |

## Identifiability assumptions

- Independent identically distributed rows with 40 independent Uniform(-1,1) features.
- Gaussian noise is independent of every covariate; conditional scale is strictly positive.
- The stated regular conditional distribution defines the pointwise target, with a continuous positive outcome density there.
- The query lies inside the covariate support and away from the x1=0 jump. No treatment identification or causal exchangeability assumption is invoked.

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Warnings:**

- No explicit latent-variable metadata or reliably identifiable latent declarations; absence from this list does not prove that no latent variables exist.
- Unrecognized or missing family in collection.json: human classification required.
