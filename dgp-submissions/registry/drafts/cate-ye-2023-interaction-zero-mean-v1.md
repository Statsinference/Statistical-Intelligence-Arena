# Ye-Shao-Yi-Zhao (2023) setting 1: treatment-by-covariate interaction with zero average effect

> **Unverified extraction — scientific review required.**

**Primary area:** CATE — Conditional Average Treatment Effect

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Ye, T., Shao, J., Yi, Y. and Zhao, Q. (2023). Toward better practice of covariate adjustment in analyzing randomized clinical trials. Journal of the American Statistical Association 118(544), 2370-2382. DOI: 10.1080/01621459.2022.2049278.

**DOI:** — · **Source locator:** Section 4.1 'Simulation results', equation (20) on PDF p.23 ('Y (2) = Y (1) + zeta(U - muU), Y (3) = Y (2)'), with the following sentence on the same page defining theta1 = theta2 = theta3 and the allocation proportions. arXiv:2009.11828v2 (13 Jul 2021), 62-page author manuscript.

## DGP / generation mechanism

**Sampling design:** Unit: patient; Dependence: independent and identically distributed

**Generator source:** [generator.py](../generators/cate-ye-2023-interaction-zero-mean-v1.py)

**Keywords (source-described):** Interactions · Linearity

**Observed variables**

U, W, A, Y

**Latent variables**

Not explicitly identified (review required)

**Latent-variable identification:** not explicitly specified

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

$$
U, W \sim \mathcal{N}(0,1) independently (standardised surrogate for the trial's empirical distribution)
$$

$$
P(A=1) = 0.5 (simple randomisation, two arms at 1:1)
$$

$$
Y(1) = eps, Y(2) = Y(1) + \zeta (U - muU)
$$

$$
\zeta = 1, muU = 0
$$

$$
\tau(U) = \zeta (U - muU) = U, with \mathbb{E}[\tau(U)] = 0
$$

$$
Y = A Y(2) + (1-A) Y(1) = eps + A \tau(U)
$$

<details>
<summary>Original source equations (verbatim)</summary>

<pre>
U, W ~ Normal(0,1) independently (standardised surrogate for the trial&#x27;s empirical distribution)
P(A=1) = 0.5 (simple randomisation, two arms at 1:1)
Y(1) = eps, Y(2) = Y(1) + zeta (U - muU), zeta = 1, muU = 0
tau(U) = zeta (U - muU) = U, with E[tau(U)] = 0
Y = A Y(2) + (1-A) Y(1) = eps + A tau(U)
</pre>

</details>


## Parameter scenarios, estimands and truth

| Scenario | Estimand | Definition | True value | Evidence status |
|---|---|---|---|---|
| original | tau(u0) = E[Y(1) - Y(0) \| U = u0] | Conditional average treatment effect at the declared query points for the arm-2 versus arm-1 contrast; the surface is linear in U with slope zeta = 1 and has exactly zero mean over the covariate distribution, so there is heterogeneity but no average effect. | 0.5 | reported_numeric |

## Identifiability assumptions

- SUTVA: one version of treatment, no interference between patients
- Randomised assignment: e = 0.5, so the treatment is independent of the potential responses by design
- Overlap: e = 0.5 with margin 0.5
- The baseline response Y(1) is independent of (U,W) in this package, which is the declared surrogate for the source's near-zero R-squared

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Warnings:**

- No explicit latent-variable metadata or reliably identifiable latent declarations; absence from this list does not prove that no latent variables exist.
