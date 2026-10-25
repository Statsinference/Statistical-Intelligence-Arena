# Null Treatment Effect with Nonlinear Propensity Scores and Observed Confounding

> **Unverified extraction — scientific review required.**

**Primary area:** ATE — Average Treatment Effect

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Wager, S. and Athey, S. (2018). Estimation and Inference of Heterogeneous Treatment Effects using Random Forests. Journal of the American Statistical Association 113(523), 1228-1242. DOI: 10.1080/01621459.2017.1319839.

**DOI:** — · **Source locator:** arXiv:1510.04342v4 PDF p.20, Section 5.1, common model and equation (27); p.21 Table 1 for d=5.

## DGP / generation mechanism

**Sampling design:** Unit: individual; Dependence: iid individuals with 5 mutually independent Uniform(0,1) baseline covariates

**Generator source:** [generator.py](../generators/ate-wager-athey-2018-confounded-null-v1.py)

**Observed variables**

X1, X2, X3, X4, X5, A, Y

**Latent variables**

Not explicitly identified (review required)

**Latent-variable identification:** not explicitly specified

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

$$
X_j\overset{\mathrm{iid}}{\sim} \mathrm{Uniform}(0,1), j=1,\ldots ,5
$$

$$
e(X)=[1+20\cdot X_{1}\cdot (1-X_{1})^{3}]/4
$$

$$
A\mid X\sim \mathrm{Bernoulli}(e(X))
$$

$$
m(X)=2\cdot X_{1}-1
$$

$$
\tau(X)=0
$$

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
X_j iid Uniform(0,1), j=1,...,5
e(X)=[1+20*X1*(1-X1)^3]/4; A|X~Bernoulli(e(X))
m(X)=2*X1-1
tau(X)=0
Y=m(X)+(A-0.5)*tau(X)+epsilon; epsilon~Normal(0,1), independent of X and assignment uniforms
</pre>

</details>


## Parameter scenarios, estimands and truth

| Scenario | Estimand | Definition | True value | Evidence status |
|---|---|---|---|---|
| source_d5_sigma1 | theta_ATE=E[Y(1)-Y(0)] | Superpopulation average effect of A=1 versus A=0, integrating over iid Uniform covariates; not a sample average or observed treated-control mean difference. | 0.0 | reported_numeric |

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
