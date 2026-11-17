# DGP iv-li-2026-aux-population-v1 (English title required)

> **Unverified extraction — scientific review required.**

**Primary area:** IV — Instrumental Variables

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Li W, Liu J, Ding P, Geng Z (2026). Identification and Multiply Robust Estimation of Causal Effects via Instrumental Variables from An Auxiliary Population. JASA 121(554):1372–1383. DOI:10.1080/01621459.2025.2576797. Read version has title ending auxiliary heterogeneous population.

**DOI:** — · **Source locator:** English description not yet supplied; consult the original scientific record (JSON).

## DGP / generation mechanism

**Sampling design:** Unit: English description not yet supplied; consult the original scientific record (JSON).; Dependence: iid individuals from the merged population; R selects the target or auxiliary population. Z is observed only when R=1; Z_obs=0 is a masked slot when R=0, not an observed target-population instrument. U is latent.

**Generator source:** [generator.py](../generators/iv-li-2026-aux-population-v1.py)

**Keywords (source-described):** Interactions · Nonlinearity

**Observed variables**

V1–V4 (4 variables), R, Z_obs, X, Y

<details>
<summary>All observed variable names</summary>

V1, V2, V3, V4, R, Z_obs, X, Y

</details>

**Latent variables**

U

**Latent-variable identification:** candidates from equations need review

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

**Original source equations (verbatim):** [Open raw scientific record (JSON)](./iv-li-2026-aux-population-v1.json).

**DGP equation 1**

```math
V_{k}\overset{\mathrm{iid}}{\sim} \mathcal{N}(0,1), v_{k}=\mathrm{expit}(2V_{k}-1), k=1,\ldots ,4.
```

**DGP equation 2**

```math
\rho^{2}=0.75+1.5v_{1}+1.5v_{2}-0.3v_{3}-0.3v_{4}
```

```math
U\mid V \sim \mathrm{Uniform}(-\rho,\rho).
```

**DGP equation 3**

```math
p_{R}=\mathrm{expit}(0.8+3v_{1}-2v_{2}-v_{3}-v_{4}), R\mid V \sim \mathrm{Bernoulli}(p_{R}).
```

**DGP equation 4**

```math
Z\mid V,R=1 \sim \mathrm{Bernoulli}[\mathrm{expit}(-0.5-v_{1}+1.5v_{2}+2v_{3}-v_{4})].
```

**DGP equation 5**

```math
\text{ a }_{1}=\mathrm{expit}(1.3-2.4Z), \text{ a }_{0}=\mathrm{expit}(v_{1}-v_{2}+0.8v_{3}-0.6v_{4}).
```

**DGP equation 6**

```math
X\mid V,U,R,Z \sim \mathrm{Bernoulli}[\mathrm{Ra}_{1}+(1-R)\text{ a }_{0}+0.1U].
```

**DGP equation 7**

```math
Y=(2-R+2v_{1}-v_{2}+v_{3}-0.5v_{4})(1+X)+U+\varepsilon, \varepsilon\sim \mathcal{N}(0,0.5^{2}).
```

**DGP equation 8**

```math
\tau=\mathbb{E}[(1-p_{R})(2+2v_{1}-v_{2}+v_{3}-0.5v_{4})] / \mathbb{E}[1-p_{R}].
```


## Parameter scenarios, estimands and truth

<table>
<thead><tr><th>Scenario</th><th>Estimand</th><th>Definition</th><th>Reported value</th></tr></thead>
<tbody>
<tr>
<td>source_v1</td>
<td rowspan="1">ATE</td>
<td rowspan="1">

$`\mathbb{E}[Y(1)-Y(0)\mid R=0]`$

</td>
<td>2.224373475244555</td>
</tr>
</tbody>
</table>

**Definition notes**

- All scenarios: Target population R=0.

<details>
<summary>Submitted estimand definitions</summary>

Submitted English definitions appear below; other original-language definitions remain in the linked JSON. Concise formulas above are display interpretations and still require scientific review.

**Scenario(s):** source_v1

Original-language definition is available in the raw scientific record (JSON).

[Open raw scientific record (JSON)](./iv-li-2026-aux-population-v1.json).

</details>


**Original submitted target notation:** tau


## Identifiability assumptions

- English description not yet supplied; consult the original scientific record (JSON).

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Adaptations from the source (submitted, unverified):**

- Use explicitly read v1 DGP; 2026 journal bibliographic status does not imply line-by-line matching with version of record.
- Encode missing IV as Z_obs=0 when R=0 and supply R as the observation mask; never output the true unobserved IV.
- Numerically integrate the exact population target instead of using source rounded value2.22 as exact truth; fit misspecification variants are not new DGPs.

**Warnings:**

- Latent-variable candidates inferred from source equations; confirm their roles and completeness against the original paper or generator.
