# DGP iv-wei-2021-censored-quantile-v1 (English title required)

> **Unverified extraction — scientific review required.**

**Primary area:** IV — Instrumental Variables

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Wei B, Peng L, Zhang MJ, Fine JP (2021). Estimation of causal quantile effects with a binary instrumental variable and censored data. JRSS-B 83(3):559–578. DOI:10.1111/rssb.12431.

**DOI:** — · **Source locator:** English description not yet supplied; consult the original scientific record (JSON).

## DGP / generation mechanism

**Sampling design:** Unit: English description not yet supplied; consult the original scientific record (JSON).; Dependence: iid individuals; latent compliance stratum independent of the IV-generation noise given X. Given X2, censoring is generated independently; observed W=min(T,C), E=1(T&lt;=C). No latent stratum, uncensored T or C exported.

**Generator source:** [generator.py](../generators/iv-wei-2021-censored-quantile-v1.py)

**Keywords (source-described):** Interactions · Nonlinearity

**Observed variables**

X1, X2, V, D, W, E

**Latent variables**

u

**Latent-variable identification:** candidates from equations need review

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

**Original source equations (verbatim):** [Open raw scientific record (JSON)](./iv-wei-2021-censored-quantile-v1.json).

**DGP equation 1**

```math
X_{1}\sim \mathrm{Uniform}(0,1), X_{2}\sim \mathrm{Bernoulli}(0.5), (p_{CO},p_{AT},p_{NT})=(2/3,1/6,1/6).
```

**DGP equation 2**

```math
\varepsilon_{V}\sim \mathcal{N}(0,0.5^{2}), V\mid X,\varepsilon_{V}\sim \mathrm{Bernoulli}[\mathrm{expit}(0.1X_{2}+X_{1}^{2}+X_{1}X_{2}+\varepsilon_{V})].
```

**DGP equation 3**

```math
D=V (CO)
```

```math
D=1 (AT)
```

```math
D=0 (NT)
```

```math
u\sim \mathrm{Uniform}(0,1).
```

**DGP equation 4**

```math
G, CO: \log T=-0.2X_{1}-0.3X_{2}+0.5D+\log\{-\log(1-u)\}.
```

**DGP equation 5**

```math
H, CO: \log T=-0.2X_{1}-0.3X_{2}+\log u+0.5\exp(0.3u)D.
```

**DGP equation 6**

```math
\mathrm{Non}-CO: \log T=-0.1X_{1}-0.2X_{2}+0.2D+\varepsilon, \varepsilon\sim \mathcal{N}(0,0.5^{2}).
```

**DGP equation 7**

```math
\begin{aligned}
C &= \mathrm{Uniform}(0,b)+X_{2} \\
b &= 2.2 (G), 1.4 (H) \\
W &= \min(T,C) \\
E &= 1\{T\leq C\}.
\end{aligned}
```


## Parameter scenarios, estimands and truth

<table>
<thead><tr><th>Scenario</th><th>Estimand</th><th>Definition</th><th>Reported value</th></tr></thead>
<tbody>
<tr>
<td>source_G</td>
<td rowspan="2">Conditional complier median causal effect</td>
<td rowspan="2">

Definition needs review; see the submitted definition below.

</td>
<td>0.5</td>
</tr>
<tr>
<td>source_H</td>
<td>0.5809171213641415</td>
</tr>
</tbody>
</table>

<details>
<summary>Submitted estimand definitions</summary>

Submitted English definitions appear below; other original-language definitions remain in the linked JSON. Concise formulas above are display interpretations and still require scientific review.

**Scenario(s):** source_G, source_H

Original-language definition is available in the raw scientific record (JSON).

[Open raw scientific record (JSON)](./iv-wei-2021-censored-quantile-v1.json).

</details>


**Original submitted target notation:** CQCE(.5)


## Identifiability assumptions

- English description not yet supplied; consult the original scientific record (JSON).

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Adaptations from the source (submitted, unverified):**

- Select original G/H scenarios because their censoring laws are explicitly supplied; A/B only state approximately30% without endpoints and are not claimed implemented.
- Scalar interface selects original CQCE at tau=.5; new local RNG; no quantile regression fitting/bootstrap or coverage experiments.

**Warnings:**

- Latent-variable candidates inferred from source equations; confirm their roles and completeness against the original paper or generator.
