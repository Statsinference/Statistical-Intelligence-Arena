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

$$
X_\{1\}\sim \mathrm{Uniform}(0,1), X_\{2\}\sim \mathrm{Bernoulli}(0.5), (p_\{CO\},p_\{AT\},p_\{NT\})=(2/3,1/6,1/6).
$$

$$
\varepsilon_\{V\}\sim \mathcal{N}(0,0.5^\{2\}), V\mid X,\varepsilon_\{V\}\sim Bernoulli[\mathrm{expit}(0.1X_\{2\}+X_\{1\}^\{2\}+X_\{1\}X_\{2\}+\varepsilon_\{V\})].
$$

$$
D=V (CO)
$$

$$
D=1 (AT)
$$

$$
D=0 (NT)
$$

$$
u\sim \mathrm{Uniform}(0,1).
$$

$$
G, CO: \log T=-0.2X_\{1\}-0.3X_\{2\}+0.5D+\log\{-\log(1-u)\}.
$$

$$
H, CO: \log T=-0.2X_\{1\}-0.3X_\{2\}+\log u+0.5exp(0.3u)D.
$$

$$
Non-CO: \log T=-0.1X_\{1\}-0.2X_\{2\}+0.2D+\varepsilon, \varepsilon\sim \mathcal{N}(0,0.5^\{2\}).
$$

$$
\begin{aligned}
C &= \mathrm{Uniform}(0,b)+X_\{2\} \\
b &= 2.2 (G), 1.4 (H) \\
W &= \min(T,C) \\
E &= 1\{T\leq C\}.
\end{aligned}
$$


## Parameter scenarios, estimands and truth

| Scenario | Estimand | Definition | True value | Evidence status |
|---|---|---|---|---|
| source_G | CQCE(.5) | English description not yet supplied; consult the original scientific record (JSON). | 0.5 | reported_numeric |
| source_H | CQCE(.5) | English description not yet supplied; consult the original scientific record (JSON). | 0.5809171213641415 | reported_numeric |

## Identifiability assumptions

- English description not yet supplied; consult the original scientific record (JSON).

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Warnings:**

- Latent-variable candidates inferred from source equations; confirm their roles and completeness against the original paper or generator.
