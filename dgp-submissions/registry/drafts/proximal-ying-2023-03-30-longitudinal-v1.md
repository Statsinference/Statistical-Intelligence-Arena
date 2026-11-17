# Longitudinal two-time proximal MSM coefficient

> **Unverified extraction — scientific review required.**

**Primary area:** Proximal Causal Inference

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Andrew Ying, Wang Miao, Xu Shi, Eric J. Tchetgen Tchetgen (2023). Proximal causal inference for complex longitudinal studies. Journal of the Royal Statistical Society Series B: Statistical Methodology, 85(3), 684-704. DOI: 10.1093/jrsssb/qkad020.

**DOI:** 10.1093/jrsssb/qkad020 · **Source locator:** arXiv:2109.07030v5; PDF pp.47-48, Appendix F.1 (printed appendix pp.22-23), Eqs.(F.1)-(F.3)

## DGP / generation mechanism

**Sampling design:** Unit: individual subject (one wide row); Dependence: English description not yet supplied; consult the original scientific record (JSON).

**Generator source:** [generator.py](../generators/proximal-ying-2023-03-30-longitudinal-v1.py)

**Keywords (source-described):** Nonlinearity

**Observed variables**

X0, A0, Z0, W0, X1, A1, Z1, W1, Y, U0, U1

**Latent variables**

Not explicitly identified (review required)

**Latent-variable identification:** not explicitly specified

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

**Original source equations (verbatim):** [Open raw scientific record (JSON)](./proximal-ying-2023-03-30-longitudinal-v1.json).

English equation transcription pending; consult the linked original scientific record (JSON) for the complete source and context.

```math
\sigma(t)=1/(1+\exp(-t))
```

```math
\mathcal{N}(0,0.5^{2})
```

English equation transcription pending; consult the linked original scientific record (JSON) for the complete source and context.

```math
X_{0} \sim \mathcal{N}(-0.35,0.5^{2})
```

```math
U_{0} \sim \mathcal{N}(0.35,0.5^{2})
```

**Step 2**

```math
A_{0} \mid  X_{0},U_{0} \sim \mathrm{Bernoulli}(\sigma(-0.5 + 0.35X_{0} - 0.35U_{0}))
```

**Step 3**

```math
Z_{0} = 0.2 + 0.5A_{0} + 0.5X_{0} + 0.75U_{0} + \varepsilon_{Z0}
```

**Step 4**

```math
W_{0} = 0.2 + 0.5X_{0} - 0.95U_{0} + \varepsilon_{W0}
```

**Step 5**

```math
X_{1} = 0.2 + 0.7A_{0} + 0.7X_{0} + \varepsilon_{X1}
```

**Step 6**

```math
U_{1} = 0.2 + 0.7A_{0} + 0.7U_{0} + \varepsilon_{U1}
```

**Step 7**

```math
A_{1} \mid  A_{0},X_{0},X_{1},U_{0},U_{1} \sim \mathrm{Bernoulli}(\sigma(-0.5 + 0.5A_{0} + 0.35(X_{0}+X_{1}) + 0.35(U_{0}+U_{1})))
```

**Step 8**

```math
Z_{1} = 0.2 + 0.5(A_{0}+A_{1}) + 0.5(X_{0}+X_{1}) - 0.75(U_{0}+U_{1}) + \varepsilon_{Z1}
```

**Step 9**

```math
W_{1} = 0.35 + 0.45(X_{0}+X_{1}) - 0.85(U_{0}+U_{1}) + \varepsilon_{W1}
```

**Step 10**

```math
Y = -1.3 + A_{1} + 1.14A_{0} + 0.5X_{1} - 0.7U_{1} + 0.2X_{0} - 0.7U_{0} + \varepsilon_{Y}
```

English equation transcription pending; consult the linked original scientific record (JSON) for the complete source and context.

X0,U0

X0,A0,Z0,W0,X1,A1,Z1,W1,Y

U0,U1


## Parameter scenarios, estimands and truth

<table>
<thead><tr><th>Scenario</th><th>Estimand</th><th>Definition</th><th>Reported value</th></tr></thead>
<tbody>
<tr>
<td>original</td>
<td rowspan="1">Marginal structural mean model slope</td>
<td rowspan="1">

$`\beta_1=\mathbb{E}[Y^{(1,0)}-Y^{(0,0)}]`$

</td>
<td>1.0</td>
</tr>
</tbody>
</table>

**Definition notes**

- All scenarios: Common slope beta_1 in E[Y(a_0,a_1)]=beta_0+beta_1(a_0+a_1); the 11-vs-00 contrast is 2 beta_1.

<details>
<summary>Submitted estimand definitions</summary>

Submitted English definitions appear below; other original-language definitions remain in the linked JSON. Concise formulas above are display interpretations and still require scientific review.

**Scenario(s):** original

Common slope beta1 in E[Y(a0,a1)]=beta0+beta1*(a0+a1). The 11-vs-00 contrast is separately 2*beta1.

[Open raw scientific record (JSON)](./proximal-ying-2023-03-30-longitudinal-v1.json).

</details>


**Original submitted target notation:** beta1


## Identifiability assumptions

- Consistency, no interference; IID subjects with explicitly dependent observations within subject
- Sequential latent exchangeability for treatment histories given latent U and observed X histories
- Z and W satisfy sequential proxy exclusion restrictions at each time given the relevant treatment/confounder history
- Sequential outcome bridges exist; proxy relevance/completeness conditions are those of the longitudinal proximal identification result
- Sequential positivity; Gaussian tails do not imply uniform overlap
- Independent initial X0,U0 and independent structural errors are an explicit joint-generation completion, separately disclosed as an implementation assumption

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Adaptations from the source (submitted, unverified):**

- English description pending; see [original scientific record](./proximal-ying-2023-03-30-longitudinal-v1.json).

**Warnings:**

- No explicit latent-variable metadata or reliably identifiable latent declarations; absence from this list does not prove that no latent variables exist.
