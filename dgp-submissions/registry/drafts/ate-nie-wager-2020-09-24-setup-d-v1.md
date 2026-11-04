# Three-term assignment and unrelated positive-part outcomes

> **Unverified extraction — scientific review required.**

**Primary area:** ATE — Average Treatment Effect

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Xinkun Nie and Stefan Wager (2021). Quasi-oracle estimation of heterogeneous treatment effects. Biometrika, 108(2):299–319. DOI 10.1093/biomet/asaa076

**DOI:** 10.1093/biomet/asaa076 · **Source locator:** Section 6.1, PDF p.15 / journal p.313, unnumbered shared sampling equations and Set-ups A–D; Section 6.2 / Figure 3, PDF p.16 / journal p.314 for dimension and noise settings; collected paragraph: Set-up D

## DGP / generation mechanism

**Sampling design:** Unit: independent individual; Dependence: Five active covariates; disjoint nonlinear conditional means and treatment interactions. The three-term propensity denominator is retained; it is not expit(X1+X2). No uniform overlap bound is claimed. Independent treatment/noise random draws conditional on covariates; no clusters or panel structure.

**Generator source:** [generator.py](../generators/ate-nie-wager-2020-09-24-setup-d-v1.py)

**Keywords (source-described):** Interactions · Nonlinearity

**Observed variables**

X1, X2, X3, X4, X5, X6, A, Y

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
p(X)=1/(1+\exp(-X_{1})+\exp(-X_{2}))
$$

$$
A\mid X\sim \mathrm{Bernoulli}(p).
$$

$$
u=\max(X_{1}+X_{2}+X_{3},0)
$$

$$
v=\max(X_{4}+X_{5},0)
$$

$$
b=(u+v)/2
$$

$$
\tau=u-v.
$$

$$
Y=b(X)+(A-0.5)\cdot \tau(X)+\varepsilon, \varepsilon\sim \mathcal{N}(0,1)
$$

$$
\mathrm{equivalently} \mathbb{E}[Y|X,A=1]=u \text{ and } \mathbb{E}[Y|X,A=0]=v.
$$

<details>
<summary>Original source equations (verbatim)</summary>

<pre>
X~N_d(0,I); coordinates independent.
p(X)=1/(1+exp(-X1)+exp(-X2)); A|X~Bernoulli(p).
u=max(X1+X2+X3,0); v=max(X4+X5,0); b=(u+v)/2; tau=u-v.
Y=b(X)+(A-0.5)*tau(X)+epsilon, epsilon~N(0,1); equivalently E[Y|X,A=1]=u and E[Y|X,A=0]=v.
</pre>

</details>


## Parameter scenarios, estimands and truth

| Scenario | Estimand | Definition | True value | Evidence status |
|---|---|---|---|---|
| original | ATE | E[Y(1)-Y(0)] in the full declared covariate population; treatment 1 versus 0; population, not sample-conditional, target. | 0.1267987153949146 | reported_numeric |

## Identifiability assumptions

- Consistency and no interference across independent individuals.
- Conditional exchangeability given observed baseline X under the declared synthetic assignment.
- Pointwise positivity; no uniform overlap bound claimed for unbounded Gaussian logistic settings.

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Warnings:**

- Nothing automatically flagged; this does NOT equal scientific acceptance.
