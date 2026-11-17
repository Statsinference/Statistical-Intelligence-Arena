# DGP iv-ye-2024-genius-heteroskedastic-v1 (English title required)

> **Unverified extraction — scientific review required.**

**Primary area:** IV — Instrumental Variables

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Ye T, Liu Z, Sun B, Tchetgen Tchetgen E (2024). GENIUS-MAWII: For robust Mendelian randomization with many weak invalid instruments. JRSS-B 86(4):1045–1067. DOI:10.1093/jrsssb/qkae024.

**DOI:** — · **Source locator:** English description not yet supplied; consult the original scientific record (JSON).

## DGP / generation mechanism

**Sampling design:** Unit: English description not yet supplied; consult the original scientific record (JSON).; Dependence: iid individuals conditional on frozen coefficient vectors. One hundred independent Binomial(2,.5) SNPs and mutually independent U/epsilon_A/epsilon_Y; heteroskedastic exposure noise retained. No baseline covariates or LD data.

**Generator source:** [generator.py](../generators/iv-ye-2024-genius-heteroskedastic-v1.py)

**Keywords (source-described):** Interactions

**Observed variables**

Z1–Z100 (100 variables), A, Y

<details>
<summary>All observed variable names</summary>

Z1, Z2, Z3, Z4, Z5, Z6, Z7, Z8, Z9, Z10, Z11, Z12, Z13, Z14, Z15, Z16, Z17, Z18, Z19, Z20, Z21, Z22, Z23, Z24, Z25, Z26, Z27, Z28, Z29, Z30, Z31, Z32, Z33, Z34, Z35, Z36, Z37, Z38, Z39, Z40, Z41, Z42, Z43, Z44, Z45, Z46, Z47, Z48, Z49, Z50, Z51, Z52, Z53, Z54, Z55, Z56, Z57, Z58, Z59, Z60, Z61, Z62, Z63, Z64, Z65, Z66, Z67, Z68, Z69, Z70, Z71, Z72, Z73, Z74, Z75, Z76, Z77, Z78, Z79, Z80, Z81, Z82, Z83, Z84, Z85, Z86, Z87, Z88, Z89, Z90, Z91, Z92, Z93, Z94, Z95, Z96, Z97, Z98, Z99, Z100, A, Y

</details>

**Latent variables**

U

**Latent-variable identification:** candidates from equations need review

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

**Original source equations (verbatim):** [Open raw scientific record (JSON)](./iv-ye-2024-genius-heteroskedastic-v1.json).

**DGP equation 1**

```math
m=100, Z_{j}\overset{\mathrm{iid}}{\sim} \mathrm{Binomial}(2,0.5)
```

```math
U\sim \mathcal{N}(0,0.48), \varepsilon_{A},\varepsilon_{Y}\overset{\mathrm{iid}}{\sim} \mathcal{N}(0,0.32).
```

**DGP equation 2**

```math
A=\sum_{j}\gamma_{j}Z_{j}+U+(1+\sum_{j}\delta_{j}Z_{j})\varepsilon_{A}
```

**DGP equation 3**

```math
Y=0.4A+\sum_{j}\alpha_{j}Z_{j}+U+\varepsilon_{Y}.
```

**DGP equation 4**

```math
h^{2}=0.2, \kappa=1, s^{2}=h^{2}/(1.5m)
```

```math
\gamma_{j}=s\phi_{\gamma j}, \delta_{j}=\kappa s\phi_{\delta j}.
```

**DGP equation 5**

```math
\phi_{\gamma j},\phi_{\delta j}\overset{\mathrm{iid}}{\sim} \mathcal{N}(0,1)
```

```math
\alpha_{j}=0, \text{ or } \alpha_{j}\sim \mathcal{N}(s,s^{2}), \text{ or } \alpha_{j}=\gamma_{j}/2.
```


## Parameter scenarios, estimands and truth

<table>
<thead><tr><th>Scenario</th><th>Estimand</th><th>Definition</th><th>Reported value</th></tr></thead>
<tbody>
<tr>
<td>setting1_new_draw</td>
<td rowspan="4">Population unit-change structural mean effect ⚠ review</td>
<td rowspan="4">

$`\mathbb{E}[Y^{(a+1)}-Y^{(a)}]`$

</td>
<td>0.4</td>
</tr>
<tr>
<td>setting2_new_draw</td>
<td>0.4</td>
</tr>
<tr>
<td>setting3_new_draw</td>
<td>0.4</td>
</tr>
<tr>
<td>setting4_new_draw</td>
<td>0.4</td>
</tr>
</tbody>
</table>

**Definition notes**

- All scenarios: Unit exposure intervention; duplicate-ID conflict still needs review.

<details>
<summary>Submitted estimand definitions</summary>

Submitted English definitions appear below; other original-language definitions remain in the linked JSON. Concise formulas above are display interpretations and still require scientific review.

**Scenario(s):** setting1_new_draw, setting2_new_draw, setting3_new_draw, setting4_new_draw

Original-language definition is available in the raw scientific record (JSON).

[Open raw scientific record (JSON)](./iv-ye-2024-genius-heteroskedastic-v1.json).

</details>


**Original submitted target notation:** β0=.4


## Identifiability assumptions

- English description not yet supplied; consult the original scientific record (JSON).

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** duplicate_conflict_needs_review

**Adaptations from the source (submitted, unverified):**

- Original Section6.1 structural equations, noise variances and four SNP-type proportions retained. New, fully recorded one-time coefficient realization uses Python random.Random(104729); author frozen coefficient vectors/seed were not supplied in the read text. This does not reproduce published Monte Carlo tables.
- SNP type groups use fixed index blocks; SNPs are iid and this is a deterministic labelling of the source proportions. Coefficients fixed across repeated samples, never treated as a new family.
- All four settings are declared; small CPU samples n=128 are interface checks, not the original n=10000/100000 estimator experiment. No LD/UK-Biobank or covariate supplement scenarios are claimed.

**Warnings:**

- Latent-variable candidates inferred from source equations; confirm their roles and completeness against the original paper or generator.
- Conflicting submission with the same DGP ID in incoming/T08_checked_batch_20261029_r1.zip; review and reconcile before approval.
