# Continuous-proxy double negative control test-negative design

> **Unverified extraction — scientific review required.**

**Primary area:** Proximal Causal Inference

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Kendrick Qijun Li, Xu Shi, Wang Miao, Eric Tchetgen Tchetgen (2024). Double Negative Control Inference in Test-Negative Design Studies of Vaccine Effectiveness. Journal of the American Statistical Association, 119(547), 1859-1870. DOI: 10.1080/01621459.2023.2220935.

**DOI:** 10.1080/01621459.2023.2220935 · **Source locator:** Author supplementary PDF at Git commit ba9dc3c581390fcefce0ca4cdabf65688a91a455; PDF p.25, Section I, Table S.1, binary and continuous blocks. Continuous block.

## DGP / generation mechanism

**Sampling design:** Unit: individual; Dependence: English description not yet supplied; consult the original scientific record (JSON).

**Generator source:** [generator.py](../generators/proximal-li-2023-07-10-continuous-tnd-v1.py)

**Keywords (source-described):** Interactions · Nonlinearity

**Observed variables**

X, A, Z, W, Y, U, D, S

**Latent variables**

Not explicitly identified (review required)

**Latent-variable identification:** not explicitly specified

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

**Original source equations (verbatim):** [Open raw scientific record (JSON)](./proximal-li-2023-07-10-continuous-tnd-v1.json).

English equation transcription pending; consult the linked original scientific record (JSON) for the complete source and context.

```math
\sigma(t)=1/(1+\exp(-t))
```

English equation transcription pending; consult the linked original scientific record (JSON) for the complete source and context.

```math
U \sim \mathrm{Uniform}(0,1)
```

```math
X \sim \mathrm{Uniform}(0,1)
```

**Step 2**

```math
A \mid  U,X \sim \mathrm{Bernoulli}(\sigma(-1 + U + 0.25X))
```

**Step 3**

```math
Z = 0.25A + 0.25X + 5U + \varepsilon_{Z}
```

**Step 4**

```math
W = 0.25X + 2U + \varepsilon_{W}
```

**Step 5**

```math
Y \mid  A,U,X \sim \mathrm{Bernoulli}(\exp(\eta_{0} + \beta A - 2U - 0.25X - 0.75UX))
```

```math
\eta_{0}=\ln(0.01)
```

**Step 6**

```math
D \mid  U,X \sim \mathrm{Bernoulli}(\exp(-4.605 + 0.25X - 0.2U))
```

**Step 7**

```math
S \mid  Y,D,U,X \sim \mathrm{Bernoulli}(\max(Y,D) \times  \sigma(-1.4 + 0.5X + 2U + UX))
```

English equation transcription pending; consult the linked original scientific record (JSON) for the complete source and context.

εZ

εW

```math
\mathcal{N}(0,0.25^{2})
```

U,X

```math
S=1
```

X,A,Z,W,Y

U,D,S

X

[0,1]

English equation transcription pending; consult the linked original scientific record (JSON) for the complete source and context.

```math
\eta_{0}=\log(0.01)
```

```math
\beta\in \{\log(0.2), \log(0.5), \log(0.7), 0\}
```


## Parameter scenarios, estimands and truth

<table>
<thead><tr><th>Scenario</th><th>Estimand</th><th>Definition</th><th>Reported value</th></tr></thead>
<tbody>
<tr>
<td>table-eta001-rr020</td>
<td rowspan="4">Causal log mean ratio</td>
<td rowspan="4">

$`\log\{\mathbb{E}[Y^{(1)}]/\mathbb{E}[Y^{(0)}]\}`$

</td>
<td>-1.6094379124341003</td>
</tr>
<tr>
<td>table-eta001-rr050</td>
<td>-0.6931471805599453</td>
</tr>
<tr>
<td>table-eta001-rr070</td>
<td>-0.35667494393873245</td>
</tr>
<tr>
<td>table-eta001-rr100</td>
<td>0.0</td>
</tr>
</tbody>
</table>

**Definition notes**

- All scenarios: Source population before selection S.

<details>
<summary>Submitted estimand definitions</summary>

Submitted English definitions appear below; other original-language definitions remain in the linked JSON. Concise formulas above are display interpretations and still require scientific review.

**Scenario(s):** table-eta001-rr020, table-eta001-rr050, table-eta001-rr070, table-eta001-rr100

log(E[Y(1)]/E[Y(0)]) in the source population before S selection; not selected-sample log odds ratio.

[Open raw scientific record (JSON)](./proximal-li-2023-07-10-continuous-tnd-v1.json).

</details>


**Original submitted target notation:** beta_log_RR


## Identifiability assumptions

- Consistency, no interference and IID source individuals
- Latent exchangeability given U,X and treatment positivity; negative-control exclusions and conditional proxy relevance/completeness
- The normal treatment bridge exists; common log-risk coefficient beta across U,X
- Among cases, S depends on U,X and not directly on A; case bridge weighting cancels the common selection factor in the risk ratio
- Estimating an unknown bridge from selected controls invokes the rare-disease approximation; no exact finite-sample estimator claim is made
- U and X, conditional proxy errors and Bernoulli draws use independent exogenous random numbers

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Adaptations from the source (submitted, unverified):**

- English description pending; see [original scientific record](./proximal-li-2023-07-10-continuous-tnd-v1.json).
- English description pending; see [original scientific record](./proximal-li-2023-07-10-continuous-tnd-v1.json).
- English description pending; see [original scientific record](./proximal-li-2023-07-10-continuous-tnd-v1.json).

**Warnings:**

- No explicit latent-variable metadata or reliably identifiable latent declarations; absence from this list does not prove that no latent variables exist.
