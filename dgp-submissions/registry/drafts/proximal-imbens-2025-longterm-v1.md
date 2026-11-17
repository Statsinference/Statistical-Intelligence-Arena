# Sequential Proxies and Long-Term Causal Effects from Combined Data

> **Unverified extraction — scientific review required.**

**Primary area:** Proximal Causal Inference

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Imbens, G., Kallus, N., Mao, X., &amp; Wang, Y. (2025). Long-term causal inference under persistent confounding via data combination. Journal of the Royal Statistical Society Series B: Statistical Methodology, 87(2), 362–388. DOI: 10.1093/jrsssb/qkae095.

**DOI:** 10.1093/jrsssb/qkae095 · **Source locator:** JRSS-B final publication, Section 7.2 and Table 2; author manuscript PDF p. 23, Example 2, Appendix B.2; dimensions and operation order checked against the author's minimax/data.R.

## DGP / generation mechanism

**Sampling design:** Unit: independent individuals from two samples; Dependence: independent rows conditional on fixed source membership; sequential dependence within each row

**Generator source:** [generator.py](../generators/proximal-imbens-2025-longterm-v1.py)

**Keywords (source-described):** Nonlinearity

**Observed variables**

X1–X5 (5 variables), S1_1–S1_5 (5 variables), S2, S3_1–S3_5 (5 variables), G, A, GY

<details>
<summary>All observed variable names</summary>

X1, X2, X3, X4, X5, S1_1, S1_2, S1_3, S1_4, S1_5, S2, S3_1, S3_2, S3_3, S3_4, S3_5, G, A, GY

</details>

**Latent variables**

X̃, U, S̃1, S̃2, S̃3

**Latent-variable identification:** candidates from equations need review

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

**Original source equations (verbatim):** [Open raw scientific record (JSON)](./proximal-imbens-2025-longterm-v1.json).

```math
\begin{aligned}
G=1&:\ \text{observational sample},\qquad G=0:\ \text{experimental sample}\\
\widetilde X,U&\overset{\mathrm{ind}}{\sim}\mathcal{N}_{5}(0,0.5I)
\end{aligned}
```

The two samples consist of independent individuals.

```math
\begin{aligned}
P(A=1\mid\widetilde X,U,G=1)&=[1+\exp(\kappa_x^\top\widetilde X+\kappa_u^\top U)]^{-1}\\
P(A=1\mid G=0)&=\tfrac12
\end{aligned}
```

```math
\begin{aligned}
\widetilde S_1&=\tau_1A+\beta_1\widetilde X+\gamma_1U+\varepsilon_1\\
\widetilde S_2&=\tau_2A+\alpha_2\widetilde S_1+\beta_2\widetilde X+\gamma_2U+\varepsilon_2
\end{aligned}
```

```math
\begin{aligned}
\widetilde S_3&=\tau_3A+\alpha_3\widetilde S_2+\beta_3\widetilde X+\gamma_3U+\varepsilon_3\\
Y&=\tau_yA+\alpha_y^\top\widetilde S_3+\beta_y^\top\widetilde X+\gamma_y^\top U+\varepsilon_{y}
\end{aligned}
```

```math
g(v)=\mathrm{sign}(v)|v|^2
```

The first and third short-term outcome groups are five-dimensional; the second group and Y are scalar. Error components are independent with source distribution N(0,0.5). The nonlinear transformation is applied componentwise to X and the short-term outcomes.

```math
\tau_2=\tau_y=0.5
```

Coefficient directions are sampled from Uniform(0,1) and vector/column norms scaled to 0.5. The registered frozen design uses seed 20261023; all coefficient values are retained in config.json.


## Parameter scenarios, estimands and truth

| Scenario | Estimand | Definition | Reported value |
|---|---|---|---|
| paper_q2_p5_fixed_design | Subpopulation average treatment effect | Tau = E[Y(1)-Y(0) \| G=0] under the registered fixed coefficient design. | 0.8797723708687131 |

**Original submitted target notation:** theta


## Identifiability assumptions

- Consistency and no interference; randomized treatment in the experimental sample; shared baseline and latent structures across the two samples; the specified sequential proxy conditions conditional on U and intermediate short-term outcomes; full-rank proxy loadings, bridge existence and support. The proxies may be affected by treatment in this source's proximal extension.

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Adaptations from the source (submitted, unverified):**

- English description pending; see [original scientific record](./proximal-imbens-2025-longterm-v1.json).

**Warnings:**

- Latent-variable candidates inferred from source equations; confirm their roles and completeness against the original paper or generator.
