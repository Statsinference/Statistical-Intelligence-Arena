# DGP did-zhao-cui-2025-instrumented-v1 (English title required)

> **Unverified extraction — scientific review required.**

**Primary area:** DiD / Synthetic Control

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Zhao, P., &amp; Cui, Y. (2025). A semiparametric instrumented difference-in-differences approach to policy learning. Biometrika, 112(4), asaf043.

**DOI:** 10.1093/biomet/asaf043 · **Source locator:** English description not yet supplied; consult the original scientific record (JSON).

## DGP / generation mechanism

**Sampling design:** Unit: independent individual from one of two repeated cross-sections; Dependence: English description not yet supplied; consult the original scientific record (JSON).

**Generator source:** [generator.py](../generators/did-zhao-cui-2025-instrumented-v1.py)

**Keywords (source-described):** Interactions · Nonlinearity · Effect heterogeneity

**Observed variables**

X1, X2, Z, T, A, Y

**Latent variables**

Not explicitly identified (review required)

**Latent-variable identification:** not explicitly specified

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

**Original source equations (verbatim):** [Open raw scientific record (JSON)](./did-zhao-cui-2025-instrumented-v1.json).

$X_{1i}\sim N(0,1),\quad X_{2i}\sim N(0,1)$

$$
$Z_i\sim \mathrm{Bernoulli}(0.5),\quad T_i\sim \mathrm{Bernoulli}(0.5)$
$$

$$
$f_U(u)=\frac{1}{2\pi\cosh(u/2)},\quad E[U_{ti}]=0,\quad \mathrm{Var}(U_{ti})=\pi^2$
$$

$$
$V_{ti}\sim\mathrm{Uniform}(0,1),\quad U_{ti}=2\log\tan(\pi V_{ti}/2)$
$$

$$
$A_{0i}\mid X_i,Z_i,U_{0i}\sim\mathrm{Bernoulli}\left(\frac{1}{1+\exp[-(2-7Z_i+0.2U_{0i}+2X_{1i})]}\right)$
$$

$$
$A_{1i}\mid X_i,Z_i,U_{1i}\sim\mathrm{Bernoulli}\left(\frac{1}{1+\exp[-(-1.5+5Z_i-0.15U_{1i}+1.5X_{2i})]}\right)$
$$

$$
$h(X_i)=1.5X_\{1i\}+2X_\{2i\}-0.5$
$$

$\epsilon_{0i}\sim N(0,1),\quad\epsilon_{1i}\sim N(0,1)$

$$
$Y_{0i}=200+10[A_{0i}h(X_i)+0.5U_{0i}+2Z_i+1.5X_{1i}+2X_{2i}]+\epsilon_{0i}$
$$

$$
$Y_{1i}=240+10[A_{1i}h(X_i)+0.5U_{1i}+2Z_i+2X_{1i}+1.5X_{2i}]+\epsilon_{1i}$
$$

$$
$A_i=(1-T_i)A_{0i}+T_iA_{1i},\quad Y_i=(1-T_i)Y_{0i}+T_iY_{1i}$
$$

$$
$ATE=\mathbb{E}[10h(X_i)]=-5$
$$


## Parameter scenarios, estimands and truth

| Scenario | Estimand | Definition | True value | Evidence status |
|---|---|---|---|---|
| source_section6_ate_target | ATE | English description not yet supplied; consult the original scientific record (JSON). | -5.0 | reported_numeric |

## Identifiability assumptions

- English description not yet supplied; consult the original scientific record (JSON).
- English description not yet supplied; consult the original scientific record (JSON).
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
