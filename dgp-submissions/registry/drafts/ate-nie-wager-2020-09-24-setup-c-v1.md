# Confounded constant effect with softplus baseline

> **Unverified extraction — scientific review required.**

**Primary area:** ATE — Average Treatment Effect

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Xinkun Nie and Stefan Wager (2021). Quasi-oracle estimation of heterogeneous treatment effects. Biometrika, 108(2):299–319. DOI 10.1093/biomet/asaa076

**DOI:** 10.1093/biomet/asaa076 · **Source locator:** Section 6.1, PDF p.15 / journal p.313, unnumbered shared sampling equations and Set-ups A–D; Section 6.2 / Figure 3, PDF p.16 / journal p.314 for dimension and noise settings; collected paragraph: Set-up C

## DGP / generation mechanism

**Sampling design:** Unit: independent individual; Dependence: Three active covariates, nonlinear softplus baseline and logistic propensity. No explicit product term is tagged as an interaction. Propensity is pointwise positive but not uniformly bounded away from 0/1 on Gaussian support. Independent treatment/noise random draws conditional on covariates; no clusters or panel structure.

**Generator source:** [generator.py](../generators/ate-nie-wager-2020-09-24-setup-c-v1.py)

**Keywords (source-described):** Nonlinearity

**Observed variables**

X1–X6 (6 variables), A, Y

<details>
<summary>All observed variable names</summary>

X1, X2, X3, X4, X5, X6, A, Y

</details>

**Latent variables**

Not explicitly identified (review required)

**Latent-variable identification:** explicit structured metadata

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

$$
X\sim \mathcal{N}_{d}(0,I)
$$

coordinates independent.

$$
p(X)=1/(1+\exp(X_{2}+X_{3}))
$$

$$
A\mid X\sim \mathrm{Bernoulli}(p).
$$

$$
b(X)=2\cdot \log(1+\exp(X_{1}+X_{2}+X_{3}))
$$

$$
\tau(X)=1.
$$

$$
Y=b(X)+(A-0.5)\cdot \tau(X)+\varepsilon
$$

$$
\varepsilon\sim \mathcal{N}(0,1).
$$

<details>
<summary>Original source equations (verbatim)</summary>

<pre>
X~N_d(0,I); coordinates independent.
p(X)=1/(1+exp(X2+X3)); A|X~Bernoulli(p).
b(X)=2*log(1+exp(X1+X2+X3)); tau(X)=1.
Y=b(X)+(A-0.5)*tau(X)+epsilon; epsilon~N(0,1).
</pre>

</details>


## Parameter scenarios, estimands and truth

| Scenario | Estimand | Definition | Reported value | Evidence status |
|---|---|---|---|---|
| original | ATE | E[Y(1)-Y(0)] in the full declared covariate population; treatment 1 versus 0; population, not sample-conditional, target. | 1.0 | reported_numeric |

**Original submitted target notation:** ATE


## Identifiability assumptions

- Consistency and no interference across independent individuals.
- Conditional exchangeability given observed baseline X under the declared synthetic assignment.
- Pointwise positivity; no uniform overlap bound claimed for unbounded Gaussian logistic settings.

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Adaptations from the source (submitted, unverified):**

- Target explicitly changed from conditional effect tau(x) to population ATE E[tau(X)]; original data-generating law retained. No claim that the source reports this ATE numerical value.
- Source treatment indicator is named A in the observed output; no scientific change.
- Independently implemented Python/NumPy sampler; source estimator fitting and large simulation replications are outside this collection task.

**Warnings:**

- Nothing automatically flagged; this does NOT equal scientific acceptance.
