# Single linear mediator with independent mixed-type baseline covariates

> **Unverified extraction — scientific review required.**

**Primary area:** Mediation — Direct and Indirect Effects

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** He, Y., Song, P. X.-K. and Xu, G. (2024). Adaptive Bootstrap Tests for Composite Null Hypotheses in the Mediation Pathway Analysis. Journal of the Royal Statistical Society: Series B 86(2), 411–434. DOI: 10.1093/jrsssb/qkad129.

**DOI:** 10.1093/jrsssb/qkad129 · **Source locator:** Journal §4 Numerical Experiments, equation (11), fixed null scenarios (12), §4.2 fixed-product 0.04 alternative; arXiv:2310.11630v1 PDF pp.10–12 (zero-index 9–11). NIE definition equation (1), preprint PDF p.4.

## DGP / generation mechanism

**Sampling design:** Unit: individual; Dependence: iid

**Generator source:** [generator.py](../generators/mediation-he-song-xu-2024-single-linear-v1.py)

**Keywords (source-described):** Not specified

**Observed variables**

X1, X2, A, M, Y

**Latent variables**

Not explicitly identified (review required)

**Latent-variable identification:** not explicitly specified

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

**Baseline**

```math
A\sim \mathrm{Bern}(0.5)
```

```math
X_{1}\sim \mathcal{N}(0,1)
```

```math
X_{2}\sim \mathrm{Bern}(0.5), \text{ independently }
```

**Mediator**

```math
M=\alpha_{S} A+1+X_{1}+X_{2}+\varepsilon_{M}, \varepsilon_{M}\sim \mathcal{N}(0,0.5^{2})
```

**Outcome**

```math
Y=\beta_{M} M+1+X_{1}+X_{2}+A+\varepsilon_{Y}, \varepsilon_{Y}\sim \mathcal{N}(0,0.5^{2})
```

independent of epsilon_M

<details>
<summary>Original source equations (verbatim)</summary>

<pre>
A~Bern(0.5), X1~N(0,1), X2~Bern(0.5), independently
M=alpha_S A+1+X1+X2+epsilon_M, epsilon_M~N(0,0.5^2)
Y=beta_M M+1+X1+X2+A+epsilon_Y, epsilon_Y~N(0,0.5^2), independent of epsilon_M
</pre>

</details>


## Parameter scenarios, estimands and truth

<table>
<thead><tr><th>Scenario</th><th>Estimand</th><th>Definition</th><th>Reported value</th></tr></thead>
<tbody>
<tr>
<td>fixed_product_004_ratio_1</td>
<td rowspan="4">NIE</td>
<td rowspan="4">

$`\mathbb{E}\!\left[Y^{(1,M^{(1)})}-Y^{(1,M^{(0)})}\right]`$

</td>
<td>0.04000000000000001</td>
</tr>
<tr>
<td>fixed_null_h01</td>
<td>0.0</td>
</tr>
<tr>
<td>fixed_null_h02</td>
<td>0.0</td>
</tr>
<tr>
<td>fixed_null_h03</td>
<td>0.0</td>
</tr>
</tbody>
</table>

<details>
<summary>Submitted estimand definitions</summary>

Submitted English definitions appear below; other original-language definitions remain in the linked JSON. Concise formulas above are display interpretations and still require scientific review.

**Scenario(s):** fixed_product_004_ratio_1, fixed_null_h01, fixed_null_h02, fixed_null_h03

E[Y(1,M(1))-Y(1,M(0))] in the source SEM superpopulation; exposure S is named A in data columns.

[Open raw scientific record (JSON)](./mediation-he-song-xu-2024-single-linear-v1.json).

</details>


**Original submitted target notation:** NIE_1


## Identifiability assumptions

- Consistency and no interference
- IID individuals
- Independent exposure and baseline covariates
- Independent mediator and outcome errors
- No unmeasured mediator-outcome confounding
- Positivity for binary exposure

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Adaptations from the source (submitted, unverified):**

- Retain the published linear SEM and baseline/noise constants. Register the three fixed null configurations from equation (12) as scenarios of one family.
- Choose alpha_S=beta_M=0.2 from the §4.2 fixed-product 0.04 alternative at ratio one; this particular point is a disclosed selection from the paper's continuous power setting, not a new family.
- Report the population natural NIE alpha_S*beta_M rather than the paper's bootstrap test performance.

**Warnings:**

- No explicit latent-variable metadata or reliably identifiable latent declarations; absence from this list does not prove that no latent variables exist.
