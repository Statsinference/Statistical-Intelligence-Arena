# Two-type donor panel with stationary common AR(1) factors

> **Unverified extraction — scientific review required.**

**Primary area:** Legacy DiD / Synthetic Control — classification needed

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Ferman, B. (2021). On the Properties of the Synthetic Control Estimator with Many Periods and Many Controls. Journal of the American Statistical Association, 116(536), 1764–1772. DOI:10.1080/01621459.2021.1965613

**DOI:** 10.1080/01621459.2021.1965613 · **Source locator:** Publication-linked replication archive: Figshare10.6084/m9.figshare.15135426.v3, file31887422, MD5 5d0337c0f1da966466b54a2e35362456; Codes/Readme.rtf line10 links main.R and aux.R to Table1. main.R30,34–37,44–60,66–94; aux.R12–19. Auxiliary arXiv1906.06665v5 Section5 PDF17–18, Table1 PDF46; these are not journal page numbers.

## DGP / generation mechanism

**Sampling design:** Unit: One jointly generated panel: 11 units (one treated and ten donors), 20 pre periods and one post, represented by one wide row per unit.; Dependence: Two independent stationary Gaussian AR(1) common factors with rho=.5; five donors share the treated loading and five share the second loading. Unit/time idiosyncratic errors are iid standard normal and independent of factors.

**Generator source:** [generator.py](../generators/did-ferman-2021-two-factor-null-v1.py)

**Keywords (source-described):** Panel data

**Observed variables**

G, Y_pre_01, Y_pre_02, Y_pre_03, Y_pre_04, Y_pre_05, Y_pre_06, Y_pre_07, Y_pre_08, Y_pre_09, Y_pre_10–Y_pre_20 (11 variables), Y_post_01

<details>
<summary>All observed variable names</summary>

G, Y_pre_01, Y_pre_02, Y_pre_03, Y_pre_04, Y_pre_05, Y_pre_06, Y_pre_07, Y_pre_08, Y_pre_09, Y_pre_10, Y_pre_11, Y_pre_12, Y_pre_13, Y_pre_14, Y_pre_15, Y_pre_16, Y_pre_17, Y_pre_18, Y_pre_19, Y_pre_20, Y_post_01

</details>

**Latent variables**

F_k0, eta_ks, F_ks

**Latent-variable identification:** candidates from equations need review

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

**stationary common factors**

```math
k=1,2
```

```math
F_{k0}\overset{\mathrm{iid}}{\sim} \mathcal{N}(0,1)
```

```math
F_{ks}=0.5\cdot F_{k},s-1+\eta_{ks} \text{ for } s=1,\ldots ,21, \eta_{ks}\overset{\mathrm{iid}}{\sim} \mathcal{N}(0,0.75)
```

independent across k,s and of the initial states

```math
\mathrm{Omit} \text{ only } s=0
```

no extra burn-in.

**unit loadings and noise**

```math
\mathrm{N}=11,J=10
```

```math
\mu_{0}=\mu_{1}=\ldots =\mu_{5}=(1,0)
```

```math
\mu_{6}=\ldots =\mu_{10}=(0,1)
```

```math
\varepsilon_{is}\overset{\mathrm{iid}}{\sim} \mathcal{N}(0,1)
```

independent of both factor paths

**observed outcomes and treatment**

```math
Y_{is}=\mu_{i}^{T} F_{s}+\varepsilon_{is}+1\{i=0,s=21\}\cdot \mathrm{post}_{\mathrm{effect}}
```

```math
\mathrm{post}_{\mathrm{effect}}=0. G_{0}=1,G_{1}:10=0
```

```math
s=1,\ldots ,20 \mathrm{pre} \text{ and } s=21 \mathrm{post}. n \mathrm{must} \mathrm{equal11}.
```

**causal target**

```math
\tau_{01}=Y_{0},21(1)-Y_{0},21(0)=\mathrm{post}_{\mathrm{effect}}=0 \text{ with } \mathrm{common} \mathrm{exogenous} \mathrm{draws} \mathrm{held} \text{ fixed }
```

single-treated SATT and its design expectation are zero.

<details>
<summary>Original source equations (verbatim)</summary>

<pre>
k=1,2; F_k0 iid N(0,1); F_ks=0.5*F_k,s-1+eta_ks for s=1,...,21, eta_ks iid N(0,0.75), independent across k,s and of the initial states. Omit only s=0; no extra burn-in.
N=11,J=10; mu_0=mu_1=...=mu_5=(1,0); mu_6=...=mu_10=(0,1); epsilon_is iid N(0,1), independent of both factor paths.
Y_is=mu_i^T F_s+epsilon_is+1{i=0,s=21}*post_effect; post_effect=0. G_0=1,G_1:10=0; s=1,...,20 pre and s=21 post. n must equal11.
tau_01=Y_0,21(1)-Y_0,21(0)=post_effect=0 with common exogenous draws held fixed; single-treated SATT and its design expectation are zero.
</pre>

</details>


## Parameter scenarios, estimands and truth

| Scenario | Estimand | Definition | Reported value |
|---|---|---|---|
| table1_j10_t020_null | Treated-unit treatment effect | Specified treated unit i=0, first and only post period t=1: Y_01(1)-Y_01(0). Its design-population mean and single-treated-unit finite SATT both equal zero pointwise. | 0.0 |

**Original submitted target notation:** tau_01


## Identifiability assumptions

- Consistency, no interference and no anticipation; only i=0 is exposed in the single post period.
- Shared common factors with fixed two-type loadings and independent unit/time disturbances; null effect is a structural response restriction. SC estimation quality and identification claims are distinct from the analytic response truth.

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Adaptations from the source (submitted, unverified):**

- Preserve source Table1 cell J=10,T0=2J=20,T1=1, zero effect; unit-wide numerical representation and strict n=11 are approved collection-interface adaptations.
- Independent Python implementation with local random.Random preserves specified distributions and dependence, not R random-stream identity; no estimator-performance replication.
- Formal publication-linked archive supplies AR recursion and initialization; formal main article full-text version comparison remains incomplete and no unverified journal equation/page locator is claimed.

**Warnings:**

- Latent-variable candidates inferred from source equations; confirm their roles and completeness against the original paper or generator.
- Legacy combined DiD / Synthetic Control family: human classification required; not automatically reassigned.
