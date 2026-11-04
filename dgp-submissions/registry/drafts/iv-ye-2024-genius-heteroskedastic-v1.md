# DGP iv-ye-2024-genius-heteroskedastic-v1 (English title required)

> **Unverified extraction — scientific review required.**

**Primary area:** IV — Instrumental Variables

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Ye T, Liu Z, Sun B, Tchetgen Tchetgen E (2024). GENIUS-MAWII: For robust Mendelian randomization with many weak invalid instruments. JRSS-B 86(4):1045–1067. DOI:10.1093/jrsssb/qkae024.

**DOI:** — · **Source locator:** English description not yet supplied; consult the original scientific record (JSON).

## DGP / generation mechanism

**Sampling design:** Unit: English description not yet supplied; consult the original scientific record (JSON).; Dependence: iid individuals conditional on frozen coefficient vectors. One hundred independent Binomial(2,.5) SNPs and mutually independent U/epsilon_A/epsilon_Y; heteroskedastic exposure noise retained. No baseline covariates or LD data.

**Generator source:** [generator.py](../generators/iv-ye-2024-genius-heteroskedastic-v1.py)

**Keywords (source-described):** Interactions · Linearity

**Observed variables**

Z1, Z2, Z3, Z4, Z5, Z6, Z7, Z8, Z9, Z10, Z11, Z12, Z13, Z14, Z15, Z16, Z17, Z18, Z19, Z20, Z21, Z22, Z23, Z24, Z25, Z26, Z27, Z28, Z29, Z30, Z31, Z32, Z33, Z34, Z35, Z36, Z37, Z38, Z39, Z40, Z41, Z42, Z43, Z44, Z45, Z46, Z47, Z48, Z49, Z50, Z51, Z52, Z53, Z54, Z55, Z56, Z57, Z58, Z59, Z60, Z61, Z62, Z63, Z64, Z65, Z66, Z67, Z68, Z69, Z70, Z71, Z72, Z73, Z74, Z75, Z76, Z77, Z78, Z79, Z80, Z81, Z82, Z83, Z84, Z85, Z86, Z87, Z88, Z89, Z90, Z91, Z92, Z93, Z94, Z95, Z96, Z97, Z98, Z99, Z100, A, Y

**Latent variables**

U

**Latent-variable identification:** candidates from equations need review

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

**Original source equations (verbatim):** [Open raw scientific record (JSON)](./iv-ye-2024-genius-heteroskedastic-v1.json).

**DGP equation 1**

$$
m=100, Z_{j}\overset{\mathrm{iid}}{\sim} \mathrm{Binomial}(2,0.5)
$$

$$
U\sim \mathcal{N}(0,0.48), \varepsilon_{A},\varepsilon_{Y}\overset{\mathrm{iid}}{\sim} \mathcal{N}(0,0.32).
$$

**DGP equation 2**

$$
A=\sum_{j}\gamma_{j}Z_{j}+U+(1+\sum_{j}\delta_{j}Z_{j})\varepsilon_{A}
$$

**DGP equation 3**

$$
Y=0.4A+\sum_{j}\alpha_{j}Z_{j}+U+\varepsilon_{Y}.
$$

**DGP equation 4**

$$
h^{2}=0.2, \kappa=1, s^{2}=h^{2}/(1.5m)
$$

$$
\gamma_{j}=s\phi_{\gamma j}, \delta_{j}=\kappa s\phi_{\delta j}.
$$

**DGP equation 5**

$$
\phi_{\gamma j},\phi_{\delta j}\overset{\mathrm{iid}}{\sim} \mathcal{N}(0,1)
$$

$$
\alpha_{j}=0, \text{ or } \alpha_{j}\sim \mathcal{N}(s,s^{2}), \text{ or } \alpha_{j}=\gamma_{j}/2.
$$


## Parameter scenarios, estimands and truth

| Scenario | Estimand | Definition | True value | Evidence status |
|---|---|---|---|---|
| setting1_new_draw | β0=.4 | English description not yet supplied; consult the original scientific record (JSON). | 0.4 | reported_numeric |
| setting2_new_draw | β0=.4 | English description not yet supplied; consult the original scientific record (JSON). | 0.4 | reported_numeric |
| setting3_new_draw | β0=.4 | English description not yet supplied; consult the original scientific record (JSON). | 0.4 | reported_numeric |
| setting4_new_draw | β0=.4 | English description not yet supplied; consult the original scientific record (JSON). | 0.4 | reported_numeric |

## Identifiability assumptions

- English description not yet supplied; consult the original scientific record (JSON).

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** duplicate_conflict_needs_review

**Warnings:**

- Latent-variable candidates inferred from source equations; confirm their roles and completeness against the original paper or generator.
- Conflicting submission with the same DGP ID in incoming/T08_checked_batch_20261029_r1.zip; review and reconcile before approval.
