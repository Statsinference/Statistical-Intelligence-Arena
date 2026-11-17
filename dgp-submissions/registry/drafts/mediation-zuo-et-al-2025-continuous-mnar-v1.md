# Continuous mediation with MNAR mediator and outcome

> **Unverified extraction — scientific review required.**

**Primary area:** Mediation — Direct and Indirect Effects

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Zuo, S., Ghosh, D., Ding, P. and Yang, F. (2025). Mediation Analysis with the Mediator and Outcome Missing Not at Random. Journal of the American Statistical Association 120(550), 794–804. DOI: 10.1080/01621459.2024.2359132.

**DOI:** 10.1080/01621459.2024.2359132 · **Source locator:** Published paper §5.1, Setting C and Assumption III; numeric coefficients in author arXiv:2212.05577v3 supplemental Table S1, PDF p.72 (zero-index 71), lines 3984–4006.

## DGP / generation mechanism

**Sampling design:** Unit: individual; Dependence: IID X,T,error terms and missingness uniforms; within unit M-&gt;Y and M-&gt;R_M, Y-&gt;R_Y

**Generator source:** [generator.py](../generators/mediation-zuo-et-al-2025-continuous-mnar-v1.py)

**Keywords (source-described):** Interactions · Nonlinearity

**Observed variables**

X, T, R_M, M_obs0, R_Y, Y_obs0

**Latent variables**

Not explicitly identified (review required)

**Latent-variable identification:** not explicitly specified

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

**X,T**

```math
X\sim \mathcal{N}(0,1)
```

```math
T\sim \mathrm{Bern}(0.5), \text{ independent }
```

**M**

```math
M\mid T,X\sim \mathcal{N}(T+X,1)
```

**Y**

```math
Y\mid M,T,X\sim \mathcal{N}(M+T+MT+X,1)
```

**R_M**

```math
R_{M}\mid M,T,X\sim \mathrm{Bern}(\mathrm{expit}(1.4+M+T+X))
```

**R_Y**

```math
R_{Y}\mid Y,T,X\sim \mathrm{Bern}(\mathrm{expit}(1.8+Y+T+X))
```

**Observed export**

```math
M_{\mathrm{obs0}}=R_{M}\cdot M
```

```math
Y_{\mathrm{obs0}}=R_{Y}\cdot Y
```

include R_M,R_Y to distinguish missing from genuine zero

<details>
<summary>Original source equations (verbatim)</summary>

<pre>
X~N(0,1), T~Bern(0.5), independent
M|T,X~N(T+X,1)
Y|M,T,X~N(M+T+MT+X,1)
R_M|M,T,X~Bern(expit(1.4+M+T+X))
R_Y|Y,T,X~Bern(expit(1.8+Y+T+X))
M_obs0=R_M*M; Y_obs0=R_Y*Y; include R_M,R_Y to distinguish missing from genuine zero
</pre>

</details>


## Parameter scenarios, estimands and truth

<table>
<thead><tr><th>Scenario</th><th>Estimand</th><th>Definition</th><th>Reported value</th></tr></thead>
<tbody>
<tr>
<td>setting_C_III</td>
<td rowspan="1">NIE</td>
<td rowspan="1">

$`\mathbb{E}\!\left[Y\{1,M(1)\}-Y\{1,M(0)\}\right]`$

</td>
<td>2.0</td>
</tr>
</tbody>
</table>

**Definition notes**

- All scenarios: Full-data estimand before MNAR masking.

<details>
<summary>Submitted estimand definitions</summary>

Submitted English definitions appear below; other original-language definitions remain in the linked JSON. Concise formulas above are display interpretations and still require scientific review.

**Scenario(s):** setting_C_III

E[Y(1,M(1))-Y(1,M(0))] in the full-data law before MNAR masking.

[Open raw scientific record (JSON)](./mediation-zuo-et-al-2025-continuous-mnar-v1.json).

</details>


**Original submitted target notation:** NIE_1


## Identifiability assumptions

- Randomized treatment and independent structural errors
- Consistency and no interference
- Sequential ignorability for full-data potential outcomes conditional on X
- Missingness depends on unobserved M and Y as specified; observed-only identification depends on the paper's extra conditions

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Adaptations from the source (submitted, unverified):**

- Choose the published Setting C / Assumption III and the non-null column of Table S1; the other support and missingness settings are separate scenarios, not counted here.
- Export only observed, numeric columns: M_obs0=R_M*M and Y_obs0=R_Y*Y, together with response flags; zero is a transport fill value, not an imputed datum. Full latent M,Y are never returned.
- Target full-data natural indirect effect at treatment 1, derived analytically as alpha_t(beta_m+beta_mt)=2; source simulation reports effects but this exact truth is independently computed here.

**Warnings:**

- No explicit latent-variable metadata or reliably identifiable latent declarations; absence from this list does not prove that no latent variables exist.
