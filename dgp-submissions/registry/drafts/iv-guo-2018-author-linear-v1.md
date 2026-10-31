# DGP iv-guo-2018-author-linear-v1 (English title required)

> **Unverified extraction — scientific review required.**

**Primary area:** IV — Instrumental Variables

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Guo Z, Kang H, Cai TT, Small DS (2018). Confidence intervals for causal effects with invalid instruments by using two-stage hard thresholding with voting. JRSS-B 80(4):793–815. DOI:10.1111/rssb.12275.

**DOI:** — · **Source locator:** English description not yet supplied; consult the original scientific record (JSON).

## DGP / generation mechanism

**Sampling design:** Unit: English description not yet supplied; consult the original scientific record (JSON).; Dependence: iid individuals. Ten independent standard-normal candidate instruments are independent of the jointly normal structural errors; within-individual error variances are 1 and covariance is 0.8.

**Generator source:** [generator.py](../generators/iv-guo-2018-author-linear-v1.py)

**Keywords (source-described):** Linearity

**Observed variables**

Z1, Z2, Z3, Z4, Z5, Z6, Z7, Z8, Z9, Z10, D, Y

**Latent variables**

e, v

**Latent-variable identification:** candidates from equations need review

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

**Original source equations (verbatim):** [Open raw scientific record (JSON)](./iv-guo-2018-author-linear-v1.json).

$$
Z_\{j\} iid \sim \mathcal{N}(0,1), j=1,\ldots ,10
$$

$$
e,v iid \sim \mathcal{N}(0,1)
$$

Z ⟂ (e,v).

$$
\varepsilon_\{D\}=e,   \varepsilon_\{Y\}=0.8e+√(1-0.8^\{2\})v.
$$

$$
D=0.5+\Sigma_\{j=1\}^\{10\} \gamma_\{j\}Z_\{j\}+\varepsilon_\{D\}
$$

$$
Y=-0.5+\beta D+\Sigma_\{j=1\}^\{10\} \pi_\{j\}Z_\{j\}+\varepsilon_\{Y\}
$$

$$
\beta=1,   \gamma=(1,\ldots ,1)
$$

$$
\pi=(3,3,3,0,0,0,0,0,0,0).
$$


## Parameter scenarios, estimands and truth

| Scenario | Estimand | Definition | True value | Evidence status |
|---|---|---|---|---|
| author_lowdim | beta | English description not yet supplied; consult the original scientific record (JSON). | 1.0 | reported_numeric |

## Identifiability assumptions

- English description not yet supplied; consult the original scientific record (JSON).

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Warnings:**

- Latent-variable candidates inferred from source equations; confirm their roles and completeness against the original paper or generator.
