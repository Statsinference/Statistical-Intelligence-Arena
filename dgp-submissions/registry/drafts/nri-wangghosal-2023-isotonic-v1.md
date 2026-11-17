# Pointwise conditional mean in the bivariate isotonic regression design of Wang and Ghosal (2023), Section 5.2

> **Unverified extraction — scientific review required.**

**Primary area:** Nonparametric Regression

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Wang, K. and Ghosal, S. (2023). Coverage of credible intervals in Bayesian multivariate isotonic regression. The Annals of Statistics 51(3), 1376-1400. DOI: 10.1214/23-AOS2298. Author preprint arXiv:2211.12566.

**DOI:** — · **Source locator:** Formula bodies: (3.1) on PDF p.6, (5.2) on PDF p.19. Section starts: Section 3.2 on PDF p.6, Section 3.5 on PDF p.9, Section 5.2 on PDF p.18. Unnumbered paragraph on PDF p.9: "To see the effect" (separate small experiment query (.5,.5) and sd=.1). Unnumbered paragraph on PDF p.19: "We propose five regression functions" (five unnumbered main-experiment functions). Unnumbered paragraph on PDF p.19: "Set epsilon_i" (standard-normal errors and mutually independent uniform covariates; anchor is a plaintext rendering of the displayed symbol). All PDF pages are 1-based pages of the fixed reading file 2211.12566v1. No printed journal page is inferred by adding an offset.

## DGP / generation mechanism

**Sampling design:** Unit: individual observation, i.e. one independent (X1, X2, Y) triple; Dependence: iid across observations; the two covariates are independent of each other and of the additive noise

**Generator source:** [generator.py](../generators/nri-wangghosal-2023-isotonic-v1.py)

**Keywords (source-described):** Interactions · Nonlinearity

**Observed variables**

X1, X2, Y

**Latent variables**

Not explicitly identified (review required)

**Latent-variable identification:** not explicitly specified

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

**1. First covariate**

```math
\mathrm{X1}_{i}\overset{\mathrm{iid}}{\sim} \mathrm{Uniform}(0,1)
```

Source main simulation, Section 5.2.

**2. Second covariate**

```math
\mathrm{X2}_{i}\overset{\mathrm{iid}}{\sim} \mathrm{Uniform}(0,1)
```

independent of X1

Independent rows and independent within-row coordinates.

**3. Innovation**

```math
\varepsilon_{i}\overset{\mathrm{iid}}{\sim} \mathcal{N}(0,1)
```

independent of X1,X2

```math
\mathrm{Main} \mathrm{simulation} \mathrm{error} \mathrm{sd}=1
```

not the separate Section 3.5 small-example noise.

**4. Mean surface**

```math
f_{1}=(X_{1}+X_{2})^{2}
```

```math
f_{2}=\sqrt{X_{1}+X_{2}}
```

```math
f_{3}=X_{1}\cdot X_{2}
```

```math
f_{4}=\exp(X_{1}+X_{2})
```

```math
f_{5}=\exp(X_{1}\cdot X_{2})
```

Deterministic source functions

the radical in f2 covers the whole sum.

**5. Observed response**

```math
Y_{i}=f_{k}(\mathrm{X1}_{i},\mathrm{X2}_{i})+\varepsilon_{i}
```

return X1,X2,Y. No latent surface or oracle column

One selected surface per scenario.

<details>
<summary>Original source equations (verbatim)</summary>

<pre>
X1_i iid Uniform(0,1). Source main simulation, Section 5.2.
X2_i iid Uniform(0,1), independent of X1. Independent rows and independent within-row coordinates.
epsilon_i iid N(0,1), independent of X1,X2. Main simulation error sd=1; not the separate Section 3.5 small-example noise.
f1=(X1+X2)^2; f2=sqrt(X1+X2); f3=X1*X2; f4=exp(X1+X2); f5=exp(X1*X2). Deterministic source functions; the radical in f2 covers the whole sum.
Y_i=f_k(X1_i,X2_i)+epsilon_i; return X1,X2,Y. No latent surface or oracle column. One selected surface per scenario.
</pre>

</details>


## Parameter scenarios, estimands and truth

<table>
<thead><tr><th>Scenario</th><th>Estimand</th><th>Definition</th><th>Reported value</th></tr></thead>
<tbody>
<tr>
<td>original-f1</td>
<td rowspan="5">Pointwise conditional mean</td>
<td rowspan="5">

$`\mathbb{E}[Y\mid X=(0.5,0.5)]`$

</td>
<td>1.0</td>
</tr>
<tr>
<td>original-f2</td>
<td>1.0</td>
</tr>
<tr>
<td>original-f3</td>
<td>0.25</td>
</tr>
<tr>
<td>original-f4</td>
<td>2.718281828459045</td>
</tr>
<tr>
<td>original-f5</td>
<td>1.2840254166877414</td>
</tr>
</tbody>
</table>

**Definition notes**

- All scenarios: Under the scenario-specific data law.

<details>
<summary>Submitted estimand definitions</summary>

Submitted English definitions appear below; other original-language definitions remain in the linked JSON. Concise formulas above are display interpretations and still require scientific review.

**Scenario(s):** original-f1, original-f2, original-f3, original-f4, original-f5

Pointwise conditional mean of Y at the fixed query point x0 = (query_x1, query_x2) = (0.5, 0.5) under the declared Section 5.2 law, for the regression function f_k selected by the scenario. This is a scalar pointwise query, not a simultaneous confidence band and not a coverage probability.

[Open raw scientific record (JSON)](./nri-wangghosal-2023-isotonic-v1.json).

</details>


**Original submitted target notation:** f_k(x0) = E[Y \| X = x0]


## Identifiability assumptions

- Observations (X1, X2, Y) are independent and identically distributed; there is no clustering, Markov, panel or network dependence.
- The design is Uniform on the unit square with independent coordinates, so the design density is bounded away from zero in a neighbourhood of the query point.
- The query point x0 = (0.5, 0.5) lies in the interior of the support [0, 1]^2, away from the boundary where isotonic estimators behave differently.
- The noise epsilon is Normal(0, sigma^2) with the declared sigma = 1 and is independent of X; the regression function is continuous at x0.
- Each f_k is non-decreasing in both coordinates on [0, 1]^2; this shape property is a feature of the declared DGP and is checked numerically, not assumed away.
- No missingness, censoring, measurement error, label-selection or sampling-weight mechanism is present; the observed table is the full sample.
- Pointwise evaluation at a single query point is not a simultaneous-band guarantee, and no credible-interval coverage claim for the source method is made here.

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Adaptations from the source (submitted, unverified):**

- Keep all five Section 5.2 functions as scenarios of one mechanism.
- Use x0=(0.5,0.5) from the separate Section 3.5 example as a declared transferred query, not as a Section 5.2 setting.
- Use scalar conditional-mean checks and requested n; do not reproduce posterior computation or confidence-band coverage.

**Warnings:**

- No explicit latent-variable metadata or reliably identifiable latent declarations; absence from this list does not prove that no latent variables exist.
