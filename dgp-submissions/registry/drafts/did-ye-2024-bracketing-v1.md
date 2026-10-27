# DGP did-ye-2024-bracketing-v1 (English title required)

> **Unverified extraction — scientific review required.**

**Primary area:** DiD / Synthetic Control

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Ye, T., Keele, L., Hasegawa, R. B., &amp; Small, D. S. (2024). A Negative Correlation Strategy for Bracketing in Difference-in-Differences. JASA, 119(547), 2256–2268.

**DOI:** 10.1080/01621459.2023.2252576 · **Source locator:** English description not yet supplied; consult the original scientific record (JSON).

## DGP / generation mechanism

**Sampling design:** Unit: individual panel, n individuals, 4 outcomes per row; Dependence: English description not yet supplied; consult the original scientific record (JSON).

**Generator source:** [generator.py](../generators/did-ye-2024-bracketing-v1.py)

**Keywords (source-described):** Linearity · Panel data

**Observed variables**

G, Y1, Y2, Y3, Y4

**Latent variables**

Not explicitly identified (review required)

**Latent-variable identification:** not explicitly specified

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

**Original source equations (verbatim):** [Open raw scientific record (JSON)](./did-ye-2024-bracketing-v1.json).

$$
$(p_a,p_b,p_{trt})=(0.2,0.5,0.3),\quad \sum_g n_g=n$
$$

$$
$n_g=\lfloor np_g\rfloor+r_g,\quad r_g\in\{0,1\},\quad \sum_g r_g=n-\sum_g\lfloor np_g\rfloor$
$$

$$
$\mu_a^{I}=(10,11,9,8)$
$$

$$
$\mu_b^{I}=(4,5,3,2)$
$$

$$
$\mu_{trt}^{I}=(3,4,2,1)$
$$

$$
$\mu_a^{II}=(10,11,10,11)$
$$

$$
$\mu_b^{II}=(4,6,2,3)$
$$

$$
$\mu_{trt}^{II}=(3,4,0,1)$
$$

$$
$(\theta_1,\theta_2,\theta_3,\theta_4)=(0,2,3,1)$
$$

$$
$\epsilon_{it}\sim N(0,1),\quad i=1,\ldots,n,\quad t=1,2,3,4$
$$

$$
$Y_{it}=\mu_{G_i,t}+\mathbf{1}\{G_i=trt\}\theta_t+\epsilon_{it}$
$$

$$
$ATT_4=E[Y_{i4}(1)-Y_{i4}(0)\mid G_i=trt]=\theta_4=1$
$$


## Parameter scenarios, estimands and truth

| Scenario | Estimand | Definition | True value | Evidence status |
|---|---|---|---|---|
| case1_parallel | ATT_4 | English description not yet supplied; consult the original scientific record (JSON). | 1.0 | reported_numeric |
| case2_partial | ATT_4 | English description not yet supplied; consult the original scientific record (JSON). | 1.0 | reported_numeric |

## Identifiability assumptions

- English description not yet supplied; consult the original scientific record (JSON).
- English description not yet supplied; consult the original scientific record (JSON).
- English description not yet supplied; consult the original scientific record (JSON).

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Warnings:**

- No explicit latent-variable metadata or reliably identifiable latent declarations; absence from this list does not prove that no latent variables exist.
