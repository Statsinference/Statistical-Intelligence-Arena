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

**Keywords (source-described):** Interactions

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

```math
P(A=1) = 0.5 (\mathrm{simple} \mathrm{randomisation}, \mathrm{two} \mathrm{arms} \text{ at } 1:1)
```

**Potential responses**

```math
Y^{(1)} = \varepsilon, Y^{(2)} = Y^{(1)} + \zeta(U - \mathrm{muU})
```

```math
\zeta= 1, \mathrm{muU} = 0
```

**Heterogeneity**

```math
\tau(U) = \zeta(U - \mathrm{muU}) = U, \text{ with } \mathbb{E}[\tau(U)] = 0
```

**Observed**

```math
Y = A Y^{(2)} + (1-A) Y^{(1)} = \varepsilon+ A \tau(U)
```

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

<table>
<thead><tr><th>Scenario</th><th>Estimand</th><th>Definition</th><th>Reported value</th></tr></thead>
<tbody>
<tr>
<td>original</td>
<td rowspan="1">CATE</td>
<td rowspan="1">

$`\mathbb{E}[Y^{(2)}-Y^{(1)}\mid U=u_0]`$

</td>
<td>0.5</td>
</tr>
</tbody>
</table>

**Definition notes**

- All scenarios: Primary query u_0=0.5; original truth.py. Potential-outcome arms are numbered 1 and 2 in the generation equations; observed A=1 selects arm 2.

<details>
<summary>Submitted estimand definitions</summary>

Submitted English definitions appear below; other original-language definitions remain in the linked JSON. Concise formulas above are display interpretations and still require scientific review.

**Scenario(s):** original

Conditional average treatment effect at the declared query points for the arm-2 versus arm-1 contrast; the surface is linear in U with slope zeta = 1 and has exactly zero mean over the covariate distribution, so there is heterogeneity but no average effect.

[Open raw scientific record (JSON)](./cate-ye-2023-interaction-zero-mean-v1.json).

</details>


**Original submitted target notation:** tau(u0) = E[Y(1) - Y(0) \| U = u0]


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

**Adaptations from the source (submitted, unverified):**

- Three arms reduced to two: only the arm-2 versus arm-1 contrast is kept, because the registered target family is the binary-treatment CATE. The contrast surface is exactly the increment in equation (20).
- Y(1) in the source is the observed placebo-arm response of 481 real patients and is not distributed with the paper; this package replaces it with independent N(0,1) noise. The source reports R-squared &lt;= 0.05 for a linear fit of Y(1) on (U,W), so the replacement preserves the near-independence of the baseline response from the covariates; it does change the paper's beta1 = -0.255 to 0 and this is a declared deviation.
- (U,W) in the source follow the empirical distribution of the same 481 patients; this package uses U, W ~ N(0,1) with muU = muW = 0 and E[U^2] = 1, i.e. the paper's centring constants are set to their standardised values.
- The source uses allocation 1:2:2 or 1:1:1 over three arms; this package uses simple randomisation with two arms at 1:1, so e = 0.5.
- The source varies zeta over [-1, 1]; this package fixes zeta = 1 as the single declared scenario.

**Warnings:**

- No explicit latent-variable metadata or reliably identifiable latent declarations; absence from this list does not prove that no latent variables exist.
