# Pointwise CATE with Confounding and Logistic Interaction Effects

> **Unverified extraction — scientific review required.**

**Primary area:** CATE — Conditional Average Treatment Effect

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Athey, S., Tibshirani, J. and Wager, S. (2019). Generalized Random Forests. The Annals of Statistics 47(2), 1148-1178. DOI: 10.1214/18-AOS1709.

**DOI:** — · **Source locator:** arXiv:1610.01271v4 PDF pp.22-23, Section 6.2, third simulation setting (both confounding and heterogeneity); p.23 Table 1, p=10, n=800.

## DGP / generation mechanism

**Sampling design:** Unit: individual; Dependence: iid individuals with 10 mutually independent Uniform(0,1) baseline covariates

**Generator source:** [generator.py](../generators/cate-athey-tibshirani-wager-2019-confounded-v1.py)

**Keywords (source-described):** Interactions · Nonlinearity · Effect heterogeneity

**Observed variables**

X1–X10 (10 variables), A, Y

<details>
<summary>All observed variable names</summary>

X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, A, Y

</details>

**Latent variables**

Not explicitly identified (review required)

**Latent-variable identification:** not explicitly specified

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

**Covariates**

```math
X_{j}\overset{\mathrm{iid}}{\sim} \mathrm{Uniform}(0,1), j=1,\ldots ,10
```

**Treatment assignment**

```math
e(X)=[1+20\cdot X_{3}\cdot (1-X_{3})^{3}]/4
```

```math
A\mid X\sim \mathrm{Bernoulli}(e(X))
```

**Centered baseline**

```math
m(X)=2\cdot X_{3}-1
```

**Conditional effect**

```math
\tau(X)=s(X_{1})\cdot s(X_{2}), s(u)=1+1/[1+\exp(-20\cdot (u-1/3))]
```

**Outcome**

```math
Y=m(X)+(A-0.5)\cdot \tau(X)+\varepsilon
```

```math
\varepsilon\sim \mathcal{N}(0,1)
```

independent of X and assignment uniforms

<details>
<summary>Original source equations (verbatim)</summary>

<pre>
X_j iid Uniform(0,1), j=1,...,10
e(X)=[1+20*X3*(1-X3)^3]/4; A|X~Bernoulli(e(X))
m(X)=2*X3-1
tau(X)=s(X1)*s(X2), s(u)=1+1/[1+exp(-20*(u-1/3))]
Y=m(X)+(A-0.5)*tau(X)+epsilon; epsilon~Normal(0,1), independent of X and assignment uniforms
</pre>

</details>


## Parameter scenarios, estimands and truth

<table>
<thead><tr><th>Scenario</th><th>Estimand</th><th>Definition</th><th>Reported value</th></tr></thead>
<tbody>
<tr>
<td>source_d10_sigma1_fixed_query</td>
<td rowspan="1">CATE</td>
<td rowspan="1">

$`\mathbb{E}[Y^{(1)}-Y^{(0)}\mid X=x_\star]`$

</td>
<td>2.25</td>
</tr>
</tbody>
</table>

**Definition notes**

- All scenarios: $`x_\star=(1/3,1/3,1/4,1/2,1/2,1/2,1/2,1/2,1/2,1/2)`$ The conditional target is evaluated at this covariate vector.

<details>
<summary>Submitted estimand definitions</summary>

Submitted English definitions appear below; other original-language definitions remain in the linked JSON. Concise formulas above are display interpretations and still require scientific review.

**Scenario(s):** source_d10_sigma1_fixed_query

Scalar pointwise CATE at x_star=[0.3333333333333333, 0.3333333333333333, 0.25, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]. Continuous source response functions specify the conditional version at this point. This is not a population ATE or the full CATE vector/function interface.

[Open raw scientific record (JSON)](./cate-athey-tibshirani-wager-2019-confounded-v1.json).

</details>


**Original submitted target notation:** tau(x_star)=E[Y(1)-Y(0)\|X=x_star]


## Identifiability assumptions

- Consistency and well-defined binary interventions; no interference.
- Independent identically distributed individuals.
- Conditional exchangeability (Y(0),Y(1)) independent of A given X, implemented by independent assignment uniforms and noise.
- Positivity: e=1/2 for randomized data; 1/4 &lt;= e(X) &lt;= 199/256 for the Beta-density assignment.
- All confounders observed, finite moments, and the specified continuous regression functions identify the pointwise conditional target where applicable.

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Adaptations from the source (submitted, unverified):**

- Preserve the source mechanism with dimension=10, noise variance=1; rename source W as A.
- The collection interface requires a scalar. Target tau(x_star) at the fixed query [0.3333333333333333, 0.3333333333333333, 0.25, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]; retain the full source tau(x) in the generator. This query and its value 2.25 are defined here, not a scalar result reported by the paper.
- Use Python/NumPy PCG64, row-major X, independent uniform-threshold assignment and normal noise; distributional reconstruction, not identical R random samples.
- Use n=128, seed=1729 for a CPU interface check instead of the source estimator study (source n=800). No estimator is fitted.
- effect_scale=1 is the source mechanism; 0 and -1 only serve internal verification controls, not additional contributions.
- The source fixes marginal Gaussian potential-outcome laws but does not require a cross-world coupling. A single independent noise produces the observed law; a shared-error potential-outcome representation is only a mathematical completion, not an asserted original coupling.

**Warnings:**

- No explicit latent-variable metadata or reliably identifiable latent declarations; absence from this list does not prove that no latent variables exist.
