# Ye-Shao-Yi-Zhao (2023) setting 2: quadratic-in-U effect with a misspecified working model

> **Unverified extraction — scientific review required.**

**Primary area:** CATE — Conditional Average Treatment Effect

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Ye, T., Shao, J., Yi, Y. and Zhao, Q. (2023). Toward better practice of covariate adjustment in analyzing randomized clinical trials. Journal of the American Statistical Association 118(544), 2370-2382. DOI: 10.1080/01621459.2022.2049278.

**DOI:** — · **Source locator:** Section 4.1 'Simulation results', equation (21) on PDF p.24 ('Y (2) = -1.3 + Y (1) - 0.5(U - muU) - 0.01(U^2 - muU2) + 0.3(W - muW)'), with the sentence 'a quadratic term U^2 - muU2 appears in the data generating process (21) but is not adjusted by ANCOVA or ANHECOVA' on the same page. arXiv:2009.11828v2 (13 Jul 2021), 62-page author manuscript.

## DGP / generation mechanism

**Sampling design:** Unit: patient; Dependence: independent and identically distributed

**Generator source:** [generator.py](../generators/cate-ye-2023-quadratic-misspecified-v1.py)

**Keywords (source-described):** Interactions · Nonlinearity

**Observed variables**

U, W, A, Y

**Latent variables**

Not explicitly identified (review required)

**Latent-variable identification:** not explicitly specified

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

**U, W**

Source notation retained without guessing:

<pre>U, W ~ Normal(0,1) independently (standardised surrogate for the trial&#x27;s empirical distribution)</pre>

**Treatment**

$$
P(A=1) = 0.5 (\mathrm{simple} \mathrm{randomisation}, \mathrm{two} \mathrm{arms} \text{ at } 1:1)
$$

**Potential responses**

$$
Y(1) = \varepsilon, Y(2) = -1.3 + Y(1) - 0.5(U - \mathrm{muU}) - 0.01(U^{2} - \mathrm{muU2}) + 0.3(W - \mathrm{muW})
$$

**Heterogeneity**

$$
\tau(U, W) = -1.3 - 0.5 U - 0.01(U^{2} - 1) + 0.3 W
$$

**Observed**

$$
Y = \varepsilon+ A \tau(U, W)
$$

<details>
<summary>Original source equations (verbatim)</summary>

<pre>
U, W ~ Normal(0,1) independently (standardised surrogate for the trial&#x27;s empirical distribution)
P(A=1) = 0.5 (simple randomisation, two arms at 1:1)
Y(1) = eps, Y(2) = -1.3 + Y(1) - 0.5(U - muU) - 0.01(U^2 - muU2) + 0.3(W - muW)
tau(U, W) = -1.3 - 0.5 U - 0.01(U^2 - 1) + 0.3 W
Y = eps + A tau(U, W)
</pre>

</details>


## Parameter scenarios, estimands and truth

| Scenario | Estimand | Definition | True value | Evidence status |
|---|---|---|---|---|
| original | tau(u0, w0) = E[Y(1) - Y(0) \| U = u0, W = w0] | Conditional average treatment effect at the declared query points for the arm-2 versus arm-1 contrast; affine in U and W with a small negative quadratic term in U, so the surface is curved but close to linear over the bulk of the covariate law. | -1.3925 | reported_numeric |

## Identifiability assumptions

- SUTVA: one version of treatment, no interference between patients
- Randomised assignment: e = 0.5, so treatment is independent of the potential responses by design
- Overlap: e = 0.5 with margin 0.5
- The baseline response Y(1) is independent of (U,W) in this package, the declared surrogate for the source's low R-squared

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Warnings:**

- No explicit latent-variable metadata or reliably identifiable latent declarations; absence from this list does not prove that no latent variables exist.
