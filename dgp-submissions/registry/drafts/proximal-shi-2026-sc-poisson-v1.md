# Poisson Synthetic Control with Truncated Normal Factors

> **Unverified extraction — scientific review required.**

**Primary area:** Proximal Causal Inference

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Shi, X., Li, K. Q., Yu, M., Miao, W., Kuchibhotla, A. K., Hu, M., &amp; Tchetgen Tchetgen, E. (2026). Theory for Identification and Inference with Synthetic Controls: A Proximal Causal Inference Framework. Journal of the American Statistical Association, online publication, 4 June 2026. DOI: 10.1080/01621459.2026.2639734.

**DOI:** 10.1080/01621459.2026.2639734 · **Source locator:** JASA 2026 publisher supplement J.8, PDF pp. 49–51, equation (S.25); r=1, N=2, no covariates.

## DGP / generation mechanism

**Sampling design:** Unit: one panel experiment; a row is a time point; Dependence: conditionally independent counts across units given a shared factor; independent time innovations

**Generator source:** [generator.py](../generators/proximal-shi-2026-sc-poisson-v1.py)

**Keywords (source-described):** Nonlinearity · Panel data

**Observed variables**

time, A, Y, W, Z

**Latent variables**

λ_t

**Latent-variable identification:** candidates from equations need review

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

**Original source equations (verbatim):** [Open raw scientific record (JSON)](./proximal-shi-2026-sc-poisson-v1.json).

```math
\begin{aligned}
\lambda_t&\overset{\mathrm{ind}}{\sim}\mathcal{N}(0.5,0.1^2)\ \text{truncated to }(0,1)\\
A_t&=\mathbf1\{t>T_0\},\quad T_0=\lfloor T/2\rfloor
\end{aligned}
```

```math
\begin{aligned}
Y_t\mid\lambda_t&\sim\mathrm{Poisson}(\exp\{\lambda_t+\beta A_t\})\\
W_t,Z_t\mid\lambda_t&\overset{\mathrm{cond.ind.}}{\sim}\mathrm{Poisson}(\lambda_t/(e-1))\\
\beta&=-2
\end{aligned}
```

```math
\begin{aligned}
r&=1\\
h(W)&=\exp(W),\qquad E[\exp(W)\mid\lambda]=\exp(\lambda)
\end{aligned}
```

All source loadings equal one in this configuration.


## Parameter scenarios, estimands and truth

<table>
<thead><tr><th>Scenario</th><th>Estimand</th><th>Definition</th><th>Reported value</th></tr></thead>
<tbody>
<tr>
<td>journal_r1_no_covariates</td>
<td rowspan="1">Causal log mean ratio</td>
<td rowspan="1">

$`\log\{\mathbb{E}[Y_t(1)]/\mathbb{E}[Y_t(0)]\}`$

</td>
<td>-2.0</td>
</tr>
</tbody>
</table>

**Definition notes**

- All scenarios: Treated unit; post-period marginal means.

<details>
<summary>Submitted estimand definitions</summary>

Submitted English definitions appear below; other original-language definitions remain in the linked JSON. Concise formulas above are display interpretations and still require scientific review.

**Scenario(s):** journal_r1_no_covariates

Original-language definition is available in the raw scientific record (JSON).

[Open raw scientific record (JSON)](./proximal-shi-2026-sc-poisson-v1.json).

</details>


**Original submitted target notation:** theta


## Identifiability assumptions

- No anticipation or interference on controls. Factor distributions and the exponential bridge remain stable before and after treatment. Unit counts are conditionally independent given the factors; proxies are informative and satisfy the source's bridge-identification conditions.

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Adaptations from the source (submitted, unverified):**

- English description pending; see [original scientific record](./proximal-shi-2026-sc-poisson-v1.json).

**Warnings:**

- Latent-variable candidates inferred from source equations; confirm their roles and completeness against the original paper or generator.
