# GENIUS heteroskedastic exposure with many weak pleiotropic genetic instruments

> **Unverified extraction — scientific review required.**

**Primary area:** IV — Instrumental Variables

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Ye, T., Liu, Z., Sun, B. and Tchetgen Tchetgen, E. (2024). GENIUS-MAWII: for robust Mendelian randomization with many weak invalid instruments. Journal of the Royal Statistical Society Series B 86(4), 1045-1067. DOI:10.1093/jrsssb/qkae024.

**DOI:** 10.1093/jrsssb/qkae024 · **Source locator:** Published full article PMC11398887 Section 6.1, unnumbered A/Y equations and four settings before Table 1; arXiv:2107.06238 main+supplement downloaded 2026-10-29 PDF pp 22-23, supplement Section 2 PDF pp 48-50. Author mr.genius fixed commit f4b2335ec107b1de29f1ef3d747585b8e3e82665 R/mr.genius.R lines 21-37 audited but NOT used: differs from the published simulation.

## DGP / generation mechanism

**Sampling design:** Unit: individual; Dependence: iid conditional on frozen coefficient arrays; 100 independent SNP dosages per person

**Generator source:** [generator.py](../generators/iv-ye-2024-genius-heteroskedastic-v1-conflict-8dd1770580.py)

**Keywords (source-described):** Interactions · Nonlinearity

**Observed variables**

Z1, Z2, Z3, Z4, Z5, Z6, Z7, Z8, Z9, Z10, Z11, Z12, Z13, Z14, Z15, Z16, Z17, Z18, Z19, Z20, Z21, Z22, Z23, Z24, Z25, Z26, Z27, Z28, Z29, Z30, Z31, Z32, Z33, Z34, Z35, Z36, Z37, Z38, Z39, Z40, Z41, Z42, Z43, Z44, Z45, Z46, Z47, Z48, Z49, Z50, Z51, Z52, Z53, Z54, Z55, Z56, Z57, Z58, Z59, Z60, Z61, Z62, Z63, Z64, Z65, Z66, Z67, Z68, Z69, Z70, Z71, Z72, Z73, Z74, Z75, Z76, Z77, Z78, Z79, Z80, Z81, Z82, Z83, Z84, Z85, Z86, Z87, Z88, Z89, Z90, Z91, Z92, Z93, Z94, Z95, Z96, Z97, Z98, Z99, Z100, A, Y, U

**Latent variables**

phi_gamma_j

**Latent-variable identification:** candidates from equations need review

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

$$
Z_j independently \sim Binomial(2,0.5), j=1,\ldots ,100.
$$

$$
phi_\gamma_j,phi_\delta_j independently drawn once \sim \mathcal{N}(0,1)
$$

$$
\gamma_j=phi_\gamma_j\cdot sqrt(h_{2}/(1.5\cdot m))
$$

$$
\delta_j=phi_\delta_j\cdot kappa\cdot sqrt(h_{2}/(1.5\cdot m))
$$

$$
h_{2}=0.2,kappa=1.
$$

$$
U\sim \mathcal{N}(0,0.6\cdot (1-h_{2}))
$$

$$
\varepsilon_A,\varepsilon_Y independently \sim \mathcal{N}(0,0.4\cdot (1-h_{2}))
$$



independent of Z and each other

$$
A=sum_j \gamma_j Z_j + U + (1+sum_j \delta_j Z_j)\cdot \varepsilon_A.
$$

$$
Y=0.4\cdot A+sum_j \alpha_j Z_j+U+\varepsilon_Y.
$$

$$
S_{1}:\alpha_j=0
$$

S2:alpha_j~N(sqrt(tau0_squared),tau0_squared) where tau0_squared=h2/(1.5*m)

$$
S_{3}:\alpha_j=\gamma_j/2.
$$

Settings S1/S2/S3 counts are 100/0/0,60/20/20,10/90/0,10/0/90. Frozen realized coefficients are explicit in config.json.

<details>
<summary>Original source equations (verbatim)</summary>

<pre>
Z_j independently ~ Binomial(2,0.5), j=1,...,100.
phi_gamma_j,phi_delta_j independently drawn once ~ N(0,1); gamma_j=phi_gamma_j*sqrt(h2/(1.5*m)); delta_j=phi_delta_j*kappa*sqrt(h2/(1.5*m)); h2=0.2,kappa=1.
U~N(0,0.6*(1-h2)); epsilon_A,epsilon_Y independently ~N(0,0.4*(1-h2)); independent of Z and each other.
A=sum_j gamma_j Z_j + U + (1+sum_j delta_j Z_j)*epsilon_A.
Y=0.4*A+sum_j alpha_j Z_j+U+epsilon_Y.
S1:alpha_j=0; S2:alpha_j~N(sqrt(tau0_squared),tau0_squared) where tau0_squared=h2/(1.5*m); S3:alpha_j=gamma_j/2.
Settings S1/S2/S3 counts are 100/0/0,60/20/20,10/90/0,10/0/90. Frozen realized coefficients are explicit in config.json.
</pre>

</details>


## Parameter scenarios, estimands and truth

| Scenario | Estimand | Definition | True value | Evidence status |
|---|---|---|---|---|
| setting1_valid | beta | Population constant causal slope dE[Y\|do(A=a)]/da=0.4, equivalently unit contrast E[Y\|do(A=1)]-E[Y\|do(A=0)], in the frozen SNP coefficient population. | 0.4 | reported_numeric |
| setting2_mixed40 | beta | Population constant causal slope dE[Y\|do(A=a)]/da=0.4, equivalently unit contrast E[Y\|do(A=1)]-E[Y\|do(A=0)], in the frozen SNP coefficient population. | 0.4 | reported_numeric |
| setting3_inside90 | beta | Population constant causal slope dE[Y\|do(A=a)]/da=0.4, equivalently unit contrast E[Y\|do(A=1)]-E[Y\|do(A=0)], in the frozen SNP coefficient population. | 0.4 | reported_numeric |
| setting4_correlated90 | beta | Population constant causal slope dE[Y\|do(A=a)]/da=0.4, equivalently unit contrast E[Y\|do(A=1)]-E[Y\|do(A=0)], in the frozen SNP coefficient population. | 0.4 | reported_numeric |

## Identifiability assumptions

- iid units, consistency and no interference; all SNPs and structural disturbances independent; U is unobserved.
- Constant additive exposure effect; no Z-by-U interactions in the conditional means for A or Y, matching source models (4),(5).
- Classical exclusion holds only in S1; S2/S3 have direct pleiotropy and intentionally violate standard-IV exclusion.
- GENIUS identifies beta from Cov(Z,R_A*(R_Y-beta*R_A))=0 with nonzero Cov(Z,R_A^2), where R variables are residualized on Z. Heteroskedastic relevance must be nonzero; no LATE or monotonicity claim.

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** duplicate_conflict_needs_review

**Warnings:**

- Latent-variable candidates inferred from source equations; confirm their roles and completeness against the original paper or generator.
- DGP ID iv-ye-2024-genius-heteroskedastic-v1 is already used by incoming/T07_IV.zip, but scientific content differs; kept separately for reviewer resolution.
