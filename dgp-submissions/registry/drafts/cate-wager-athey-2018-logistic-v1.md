# Pointwise CATE under Randomized Treatment with Logistic Interaction Effects

> **Unverified extraction — scientific review required.**

**Primary area:** CATE — Conditional Average Treatment Effect

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Wager, S. and Athey, S. (2018). Estimation and Inference of Heterogeneous Treatment Effects using Random Forests. Journal of the American Statistical Association 113(523), 1228-1242. DOI: 10.1080/01621459.2017.1319839.

**DOI:** — · **Source locator:** arXiv:1510.04342v4 PDF p.20, Section 5.1, common model and equation (28); p.22 Table 2 for d=6.

## DGP / generation mechanism

**Sampling design:** Unit: individual; Dependence: iid individuals with 6 mutually independent Uniform(0,1) baseline covariates

**Generator source:** [generator.py](../generators/cate-wager-athey-2018-logistic-v1.py)

**Keywords (source-described):** Interactions · Nonlinearity · Effect heterogeneity

**Observed variables**

X1, X2, X3, X4, X5, X6, A, Y

**Latent variables**

Not explicitly identified (review required)

**Latent-variable identification:** not explicitly specified

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

**Covariates**

$$
X_{j}\overset{\mathrm{iid}}{\sim} \mathrm{Uniform}(0,1), j=1,\ldots ,6
$$

**Treatment assignment**

$$
e(X)=0.5
$$

$$
A\mid X\sim \mathrm{Bernoulli}(e(X))
$$

**Centered baseline**

$$
m(X)=0
$$

**Conditional effect**

$$
\tau(X)=s(X_{1})\cdot s(X_{2}), s(u)=1+1/[1+\exp(-20\cdot (u-1/3))]
$$

**Outcome**

$$
Y=m(X)+(A-0.5)\cdot \tau(X)+\varepsilon
$$

$$
\varepsilon\sim \mathcal{N}(0,1)
$$

independent of X and assignment uniforms

<details>
<summary>Original source equations (verbatim)</summary>

<pre>
X_j iid Uniform(0,1), j=1,...,6
e(X)=0.5; A|X~Bernoulli(e(X))
m(X)=0
tau(X)=s(X1)*s(X2), s(u)=1+1/[1+exp(-20*(u-1/3))]
Y=m(X)+(A-0.5)*tau(X)+epsilon; epsilon~Normal(0,1), independent of X and assignment uniforms
</pre>

</details>


## Parameter scenarios, estimands and truth

| Scenario | Estimand | Definition | True value | Evidence status |
|---|---|---|---|---|
| source_d6_sigma1_fixed_query | tau(x_star)=E[Y(1)-Y(0)\|X=x_star] | Scalar pointwise CATE at x_star=[0.3333333333333333, 0.3333333333333333, 0.5, 0.5, 0.5, 0.5]. Continuous source response functions specify the conditional version at this point. This is not a population ATE or the full CATE vector/function interface. | 2.25 | reported_numeric |

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

**Warnings:**

- No explicit latent-variable metadata or reliably identifiable latent declarations; absence from this list does not prove that no latent variables exist.
