# Random assignment and smooth sigmoid-difference effect

> **Unverified extraction — scientific review required.**

**Primary area:** ATE — Average Treatment Effect

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Xinkun Nie and Stefan Wager (2021). Quasi-oracle estimation of heterogeneous treatment effects. Biometrika 108(2):299–319. DOI 10.1093/biomet/asaa076

**DOI:** 10.1093/biomet/asaa076 · **Source locator:** Section 4.2, PDF p.9 / journal p.307, equation (9) and following smooth effect definition; Figure 2 PDF p.10 / journal p.308, sigma=1 noise setting

## DGP / generation mechanism

**Sampling design:** Unit: independent individual; Dependence: Independent individuals; Independent Gaussian coordinates within each individual. Outcome errors and treatment randomization use independent local draws.

**Generator source:** [generator.py](../generators/ate-nie-wager-2020-09-24-eq9-smooth-v1.py)

**Keywords (source-described):** Interactions · Nonlinearity

**Observed variables**

X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, A, Y

**Latent variables**

Not explicitly identified (review required)

**Latent-variable identification:** explicit structured metadata

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

$$
X\sim N_10(0,I)
$$

independent coordinates and individuals.

$$
A\sim \mathrm{Bernoulli}(0.5)
$$

independent of X

$$
b(X)=3/(1+\exp(X_{3}-X_{2}))
$$

$$
\tau(X)=1/(1+\exp(X_{1}-X_{2})).
$$

$$
Y\mid X,A\sim \mathcal{N}(b(X)+(A-0.5)\cdot \tau(X),\sigma\cdot \cdot 2)
$$

$$
\sigma=1, selected from Figure 2 noise levels.
$$

<details>
<summary>Original source equations (verbatim)</summary>

<pre>
X~N_10(0,I); independent coordinates and individuals.
A~Bernoulli(0.5), independent of X.
b(X)=3/(1+exp(X3-X2)); tau(X)=1/(1+exp(X1-X2)).
Y|X,A~N(b(X)+(A-0.5)*tau(X),sigma**2), sigma=1, selected from Figure 2 noise levels.
</pre>

</details>


## Parameter scenarios, estimands and truth

| Scenario | Estimand | Definition | True value | Evidence status |
|---|---|---|---|---|
| original | ATE | ATE = E[Y(1)-Y(0)] in the full original covariate population; binary treatment 1 versus 0. | 0.5 | reported_numeric |

## Identifiability assumptions

- Consistency and no interference across independent individuals.
- Treatment independent of outcome error conditional on observed X; source conditional exchangeability.
- Positive probability for each treatment at every finite X; no trimming or new clipping.

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Warnings:**

- Nothing automatically flagged; this does NOT equal scientific acceptance.
