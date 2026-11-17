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

X1–X10 (10 variables), A, Y

<details>
<summary>All observed variable names</summary>

X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, A, Y

</details>

**Latent variables**

Not explicitly identified (review required)

**Latent-variable identification:** explicit structured metadata

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

```math
X\sim \mathcal{N}_{10}(0,I)
```

independent coordinates and individuals.

```math
A\sim \mathrm{Bernoulli}(0.5)
```

independent of X

```math
b(X)=3/(1+\exp(X_{3}-X_{2}))
```

```math
\tau(X)=1/(1+\exp(X_{1}-X_{2})).
```

```math
Y\mid X,A\sim \mathcal{N}(b(X)+(A-0.5)\cdot \tau(X),\sigma^{2})
```

```math
\sigma=1, \mathrm{selected} \text{ from } \mathrm{Figure} 2 \text{ noise } \mathrm{levels}.
```

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

<table>
<thead><tr><th>Scenario</th><th>Estimand</th><th>Definition</th><th>Reported value</th></tr></thead>
<tbody>
<tr>
<td>original</td>
<td rowspan="1">ATE</td>
<td rowspan="1">

$`\mathbb{E}[Y(1)-Y(0)]`$

</td>
<td>0.5</td>
</tr>
</tbody>
</table>

**Definition notes**

- All scenarios: Population ATE; expectation is over the DGP's full population.

<details>
<summary>Submitted estimand definitions</summary>

Submitted English definitions appear below; other original-language definitions remain in the linked JSON. Concise formulas above are display interpretations and still require scientific review.

**Scenario(s):** original

ATE = E[Y(1)-Y(0)] in the full original covariate population; binary treatment 1 versus 0.

[Open raw scientific record (JSON)](./ate-nie-wager-2020-09-24-eq9-smooth-v1.json).

</details>


**Original submitted target notation:** ATE


## Identifiability assumptions

- Consistency and no interference across independent individuals.
- Treatment independent of outcome error conditional on observed X; source conditional exchangeability.
- Positive probability for each treatment at every finite X; no trimming or new clipping.

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Adaptations from the source (submitted, unverified):**

- Explicit target adaptation: integrate source conditional effect over the original covariate distribution to obtain population ATE; data-generating equations unchanged.
- Rename source treatment D or W to A; observed conditional law unchanged.
- Independent Python/NumPy implementation; no source estimator fitting or reported performance tables are reproduced.

**Warnings:**

- Nothing automatically flagged; this does NOT equal scientific acceptance.
