# DGP iv-henckel-2024-g1-sem-v1 (English title required)

> **Unverified extraction — scientific review required.**

**Primary area:** IV — Instrumental Variables

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Henckel L, Buttenschön M, Maathuis MH (2024). Graphical tools for selecting conditional instrumental sets. Biometrika 111(3):771–788. DOI:10.1093/biomet/asad066.

**DOI:** — · **Source locator:** English description not yet supplied; consult the original scientific record (JSON).

## DGP / generation mechanism

**Sampling design:** Unit: English description not yet supplied; consult the original scientific record (JSON).; Dependence: iid individuals conditional on one frozen SEM. Independent node noises include two hidden common causes; D-X and X-Y dependence is retained. M is posttreatment, C is the selected conditioning covariate.

**Generator source:** [generator.py](../generators/iv-henckel-2024-g1-sem-v1.py)

**Keywords (source-described):** Linearity

**Observed variables**

A, B, C, D, X, M, Y

**Latent variables**

Not explicitly identified (review required)

**Latent-variable identification:** not explicitly specified

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

**Original source equations (verbatim):** [Open raw scientific record (JSON)](./iv-henckel-2024-g1-sem-v1.json).

$$
\begin{aligned}
A &= \varepsilon_\{A\} \\
C &= \varepsilon_\{C\} \\
B &= b_\{CB\}C+\varepsilon_\{B\}
\end{aligned}
$$

$$
D=b_\{AD\}A+b_\{BD\}B+b_\{HD\}H_\{DX\}+\varepsilon_\{D\}
$$

$$
X=b_\{BX\}B+b_\{HX\}H_\{DX\}+b_\{GX\}H_\{XY\}+\varepsilon_\{X\}
$$

$$
M=b_\{XM\}X+\varepsilon_\{M\}
$$

$$
Y=b_\{XY\}X+b_\{MY\}M+b_\{CY\}C+b_\{GY\}H_\{XY\}+\varepsilon_\{Y\}.
$$

$$
\varepsilon_\{k\} \sim \mathcal{N}(0,v_\{k\})  or  \mathrm{Uniform}(-√(3v_\{k\}),√(3v_\{k\})).
$$


## Parameter scenarios, estimands and truth

| Scenario | Estimand | Definition | True value | Evidence status |
|---|---|---|---|---|
| G1_gaussian_new_draw | tau_YX | English description not yet supplied; consult the original scientific record (JSON). | 0.7324265699272281 | reported_numeric |
| G1_uniform_new_draw | tau_YX | English description not yet supplied; consult the original scientific record (JSON). | 0.7324265699272281 | reported_numeric |

## Identifiability assumptions

- English description not yet supplied; consult the original scientific record (JSON).

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Warnings:**

- No explicit latent-variable metadata or reliably identifiable latent declarations; absence from this list does not prove that no latent variables exist.
