# Stationary Multifactor Gaussian Synthetic Control

> **Unverified extraction — scientific review required.**

**Primary area:** Proximal Causal Inference

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Shi, X., Li, K. Q., Yu, M., Miao, W., Kuchibhotla, A. K., Hu, M., &amp; Tchetgen Tchetgen, E. (2026). Theory for Identification and Inference with Synthetic Controls: A Proximal Causal Inference Framework. Journal of the American Statistical Association, online publication, 4 June 2026. DOI: 10.1080/01621459.2026.2639734.

**DOI:** 10.1080/01621459.2026.2639734 · **Source locator:** JASA 2026 final publication, Section 4 (linear factor model and loadings); fixed r=5 without covariates and with independent errors; stationary/constrained/addcov=FALSE configuration in the author's run_sim_linear_est.R.

## DGP / generation mechanism

**Sampling design:** Unit: one panel experiment; a row is a time point; Dependence: shared factors across units; independent time innovations; deterministic pre/post indicator

**Generator source:** [generator.py](../generators/proximal-shi-2026-sc-gaussian-v1.py)

**Keywords (source-described):** Panel data

**Observed variables**

time, A, Y, W1–W5 (5 variables), Z1–Z5 (5 variables)

<details>
<summary>All observed variable names</summary>

time, A, Y, W1, W2, W3, W4, W5, Z1, Z2, Z3, Z4, Z5

</details>

**Latent variables**

λ_tk

**Latent-variable identification:** candidates from equations need review

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

**Original source equations (verbatim):** [Open raw scientific record (JSON)](./proximal-shi-2026-sc-gaussian-v1.json).

```math
\begin{aligned}
t&=1,\ldots,T\\
A_t&=\mathbf1\{t>T_0\},\quad T_0=\lfloor T/2\rfloor\\
\lambda_{tk}&\overset{\mathrm{ind}}{\sim}\mathcal{N}(0.5,0.5^2),\quad k=1,\ldots,5
\end{aligned}
```

```math
\begin{aligned}
\mu_0&=(1,1,1,1,1)\\
D&=\mathrm{diag}(3,6,6,6,6)\\
Y_t&=2A_t+\sum_{k=1}^5\lambda_{tk}+\varepsilon_{0t}
\end{aligned}
```

```math
\begin{aligned}
W_t&=D\lambda_t+\varepsilon_{Wt}\\
Z_t&=D\lambda_t+\varepsilon_{Zt}
\end{aligned}
```

The errors for all 11 units are independently N(0,1.5²), also independent across time.

```math
\begin{aligned}
h(W)&=W_1/3+(W_2+W_3+W_4+W_5)/6\\
\alpha^\top D&=\mu_0^\top,\qquad\sum_j\alpha_j=1
\end{aligned}
```


## Parameter scenarios, estimands and truth

| Scenario | Estimand | Definition | Reported value |
|---|---|---|---|
| journal_r5_stationary | Needs review | ETT = E[Y_t(1)-Y_t(0)] = 2, also when averaged over post-treatment periods. | 2.0 |

**Original submitted target notation:** ETT


## Identifiability assumptions

- No anticipation and no interference on control units. Shared factor loadings and bridge functions remain stable across periods. Errors are conditionally independent across units given the common factors; proxies are relevant to factors and the loading matrix has full rank.

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Adaptations from the source (submitted, unverified):**

- English description pending; see [original scientific record](./proximal-shi-2026-sc-gaussian-v1.json).

**Warnings:**

- Latent-variable candidates inferred from source equations; confirm their roles and completeness against the original paper or generator.
