# Three-group Gaussian outcomes with nonparallel untreated trends

> **Unverified extraction — scientific review required.**

**Primary area:** DiD / Synthetic Control

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Ye, T., Keele, L., Hasegawa, R., and Small, D. S. (2024). A Negative Correlation Strategy for Bracketing in Difference-in-Differences. Journal of the American Statistical Association, 119(547), 2256–2268. DOI:10.1080/01621459.2023.2252576

**DOI:** 10.1080/01621459.2023.2252576 · **Source locator:** data_gen case2 and default att; table_summary t4 coverage target; DOI10.1080/01621459.2023.2252576; current author https://ting-ye.com/publication links same paper and repository

## DGP / generation mechanism

**Sampling design:** Unit: 1000 unit rows,4 observed periods; fixed300trt500b200a; n strictly1000; Dependence: All observed Gaussian cell innovations independent; fixed deterministic group/time means, no persistent latent state.

**Generator source:** [generator.py](../generators/did-ye-2024-code-case2-gaussian-bracketing-v1.py)

**Keywords (source-described):** Linearity

**Observed variables**

G, C, Y_pre001, Y_post001, Y_post002, Y_post003

**Latent variables**

Not explicitly identified (review required)

**Latent-variable identification:** not explicitly specified

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

$$
Y_gtj\sim \mathcal{N}(\mu_gt+I(g=trt)att_t,1), independent all cells
$$

$$
\mu_trt=(3,4,0,1)
$$

$$
\mu_a=(10,11,10,11)
$$

$$
\mu_b=(4,6,2,3)
$$

$$
att=(0,2,3,1)
$$

$$
Population ATT4=1
$$

finite-sample cross-world coupling unspecified

<details>
<summary>Original source equations (verbatim)</summary>

<pre>
Y_gtj~N(mu_gt+I(g=trt)att_t,1), independent all cells; mu_trt=(3,4,0,1),mu_a=(10,11,10,11),mu_b=(4,6,2,3),att=(0,2,3,1)
Population ATT4=1; finite-sample cross-world coupling unspecified
</pre>

</details>


## Parameter scenarios, estimands and truth

| Scenario | Estimand | Definition | True value | Evidence status |
|---|---|---|---|---|
| baseline | ATT_4 | Population mean treatment effect at final period4 conditional on treated group, source-declared att[4]=1; not finite-sample SATT. | 1.0 | reported_numeric |

## Identifiability assumptions

- Source additive treatment shift in treated-group marginal means; no interference and consistency.

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Warnings:**

- No explicit latent-variable metadata or reliably identifiable latent declarations; absence from this list does not prove that no latent variables exist.
