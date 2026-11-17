# Proximal mediation natural direct effect

> **Unverified extraction — scientific review required.**

**Primary area:** Proximal Causal Inference

**Suggested cross-tags (unverified):** mediation

## Reference paper

**Citation:** Oliver Dukes, Ilya Shpitser, Eric J. Tchetgen Tchetgen (2023). Proximal mediation analysis. Biometrika, 110(4), 973-987. DOI: 10.1093/biomet/asad015.

**DOI:** 10.1093/biomet/asad015 · **Source locator:** arXiv:2109.11904v2; PDF pp.13-14, Section 4

## DGP / generation mechanism

**Sampling design:** Unit: individual; Dependence: English description not yet supplied; consult the original scientific record (JSON).

**Generator source:** [generator.py](../generators/proximal-dukes-2023-03-03-mediation-v1.py)

**Keywords (source-described):** Nonlinearity

**Observed variables**

X1, X2, A, Z, W, M, Y, U

**Latent variables**

Not explicitly identified (review required)

**Latent-variable identification:** not explicitly specified

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

**Original source equations (verbatim):** [Open raw scientific record (JSON)](./proximal-dukes-2023-03-03-mediation-v1.json).

English equation transcription pending; consult the linked original scientific record (JSON) for the complete source and context.

```math
T=X_{1}+X_{2}
```

```math
\sigma(t)=1/(1+\exp(-t))
```

**Step 1**

```math
(X_{1},X_{2},U)^{T} \sim \mathcal{N}_{3}((0.25,0.25,0)^{T}, \begin{bmatrix}
0.25 & 0 & 0.05 \\
0 & 0.25 & 0.05 \\
0.05 & 0.05 & 1
\end{bmatrix})
```

**Step 2**

```math
A \mid  T,U \sim \mathrm{Bernoulli}(\sigma(-0.5T - 0.4U))
```

**Step 3**

```math
Z = 0.2 - 0.52A + 0.2T - U + \varepsilon_{Z}
```

**Step 4**

```math
W = 0.3 + 0.2T - 0.6U + \varepsilon_{W}
```

**Step 5**

```math
M = -0.3A - 0.5T + 0.4U + \varepsilon_{M}
```

**Step 6**

```math
Y = 2 + 2A + M + 2W - T - U + \varepsilon_{Y}
```

English equation transcription pending; consult the linked original scientific record (JSON) for the complete source and context.

εZ,εW,εM

```math
\mathcal{N}(0,1)
```

```math
\varepsilon_{Y} \sim \mathcal{N}(0,2^{2})
```

X1,X2,A,Z,W,M,Y

U


## Parameter scenarios, estimands and truth

<table>
<thead><tr><th>Scenario</th><th>Estimand</th><th>Definition</th><th>Reported value</th></tr></thead>
<tbody>
<tr>
<td>original</td>
<td rowspan="1">NDE</td>
<td rowspan="1">

$`\mathbb{E}[Y^{(1,M^{(0)})}-Y^{(0,M^{(0)})}]`$

</td>
<td>2.0</td>
</tr>
</tbody>
</table>

**Definition notes**

- All scenarios: Natural direct effect.

<details>
<summary>Submitted estimand definitions</summary>

Submitted English definitions appear below; other original-language definitions remain in the linked JSON. Concise formulas above are display interpretations and still require scientific review.

**Scenario(s):** original

E[Y(1,M(0))-Y(0,M(0))] in the source population; NIE and total effect are auxiliary only.

[Open raw scientific record (JSON)](./proximal-dukes-2023-03-03-mediation-v1.json).

</details>


**Original submitted target notation:** NDE


## Identifiability assumptions

- Consistency for treatment and mediator interventions, no interference and IID people
- Proxy exclusions and latent confounding/cross-world conditions for Y(1,M(0)) in the proximal mediation model
- Outcome bridge and nested bridge existence with completeness and treatment/mediator positivity
- Baseline W is not causally affected by A; M(a) and Y(a,m) use the structural equations with shared baseline and exogenous errors
- Independent exogenous errors conditional on the declared correlated baseline form the joint-generation completion, separately disclosed

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Adaptations from the source (submitted, unverified):**

- English description pending; see [original scientific record](./proximal-dukes-2023-03-03-mediation-v1.json).

**Warnings:**

- No explicit latent-variable metadata or reliably identifiable latent declarations; absence from this list does not prove that no latent variables exist.
