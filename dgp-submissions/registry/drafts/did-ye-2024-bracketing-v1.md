# DGP did-ye-2024-bracketing-v1 (English title required)

> **Unverified extraction — scientific review required.**

**Primary area:** DiD — Difference-in-Differences

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Ye, T., Keele, L., Hasegawa, R. B., &amp; Small, D. S. (2024). A Negative Correlation Strategy for Bracketing in Difference-in-Differences. JASA, 119(547), 2256–2268.

**DOI:** 10.1080/01621459.2023.2252576 · **Source locator:** English description not yet supplied; consult the original scientific record (JSON).

## DGP / generation mechanism

**Sampling design:** Unit: individual panel, n individuals, 4 outcomes per row; Dependence: English description not yet supplied; consult the original scientific record (JSON).

**Generator source:** [generator.py](../generators/did-ye-2024-bracketing-v1.py)

**Keywords (source-described):** Panel data

**Observed variables**

G, Y1–Y4 (4 variables)

<details>
<summary>All observed variable names</summary>

G, Y1, Y2, Y3, Y4

</details>

**Latent variables**

Not explicitly identified (review required)

**Latent-variable identification:** not explicitly specified

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

**Original source equations (verbatim):** [Open raw scientific record (JSON)](./did-ye-2024-bracketing-v1.json).

**Fixed group design: a=0, b=1, trt=2; n=1000 in source**

```math
(p_a,p_b,p_{trt})=(0.2,0.5,0.3),\quad \sum_g n_g=n
```

**Group allocation; largest fractional remainders receive the remaining units**

```math
n_g=\lfloor np_g\rfloor+r_g,\quad r_g\in\{0,1\},\quad \sum_g r_g=n-\sum_g\lfloor np_g\rfloor
```

**Case I untreated means in group a**

```math
\mu_a^{I}=(10,11,9,8)
```

**Case I untreated means in group b**

```math
\mu_b^{I}=(4,5,3,2)
```

**Case I untreated means in treated group**

```math
\mu_{trt}^{I}=(3,4,2,1)
```

**Case II untreated means in group a**

```math
\mu_a^{II}=(10,11,10,11)
```

**Case II untreated means in group b**

```math
\mu_b^{II}=(4,6,2,3)
```

**Case II untreated means in treated group**

```math
\mu_{trt}^{II}=(3,4,0,1)
```

**Additive effects; no anticipation in period 1**

```math
(\theta_1,\theta_2,\theta_3,\theta_4)=(0,2,3,1)
```

**Independent errors across all individuals and periods**

```math
\epsilon_{it}\sim N(0,1),\quad i=1,\ldots,n,\quad t=1,2,3,4
```

**Observed outcome; effect added to treated group only**

```math
Y_{it}=\mu_{G_i,t}+\mathbf{1}\{G_i=trt\}\theta_t+\epsilon_{it}
```

**Fixed estimand**

```math
ATT_4=E[Y_{i4}^{(1)}-Y_{i4}^{(0)}\mid G_i=trt]=\theta_4=1
```


## Parameter scenarios, estimands and truth

<table>
<thead><tr><th>Scenario</th><th>Estimand</th><th>Definition</th><th>Reported value</th></tr></thead>
<tbody>
<tr>
<td>case1_parallel</td>
<td rowspan="2">ATT</td>
<td rowspan="2">

$`\mathbb{E}[Y_4^{(1)}-Y_4^{(0)}\mid G=\mathrm{trt}]`$

</td>
<td>1.0</td>
</tr>
<tr>
<td>case2_partial</td>
<td>1.0</td>
</tr>
</tbody>
</table>

**Definition notes**

- All scenarios: Final period, treated group.

<details>
<summary>Submitted estimand definitions</summary>

Submitted English definitions appear below; other original-language definitions remain in the linked JSON. Concise formulas above are display interpretations and still require scientific review.

**Scenario(s):** case1_parallel, case2_partial

Original-language definition is available in the raw scientific record (JSON).

[Open raw scientific record (JSON)](./did-ye-2024-bracketing-v1.json).

</details>


**Original submitted target notation:** ATT_4


## Identifiability assumptions

- English description not yet supplied; consult the original scientific record (JSON).
- English description not yet supplied; consult the original scientific record (JSON).
- English description not yet supplied; consult the original scientific record (JSON).

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Adaptations from the source (submitted, unverified):**

- English description pending; see [original scientific record](./did-ye-2024-bracketing-v1.json).
- English description pending; see [original scientific record](./did-ye-2024-bracketing-v1.json).
- English description pending; see [original scientific record](./did-ye-2024-bracketing-v1.json).
- English description pending; see [original scientific record](./did-ye-2024-bracketing-v1.json).
- English description pending; see [original scientific record](./did-ye-2024-bracketing-v1.json).

**Warnings:**

- No explicit latent-variable metadata or reliably identifiable latent declarations; absence from this list does not prove that no latent variables exist.
- Catalog placement: Three-group multi-period design for DiD bracketing.
