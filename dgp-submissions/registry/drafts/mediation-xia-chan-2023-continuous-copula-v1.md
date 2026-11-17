# Continuous Gaussian-copula mediator and treatment-induced confounder

> **Unverified extraction — scientific review required.**

**Primary area:** Mediation — Direct and Indirect Effects

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Xia, F. and Chan, K. C. G. (2023). Identification, Semiparametric Efficiency, and Quadruply Robust Estimation in Mediation Analysis with Treatment-Induced Confounding. Journal of the American Statistical Association 118(542), 1272–1281. DOI: 10.1080/01621459.2021.1990765.

**DOI:** 10.1080/01621459.2021.1990765 · **Source locator:** Accepted manuscript §4.1, continuous C and M paragraph, PDF p.17; https://par.nsf.gov/servlets/purl/10300663.

## DGP / generation mechanism

**Sampling design:** Unit: individual; Dependence: IID rows; within each row C and M residuals have Gaussian correlation 0.2

**Generator source:** [generator.py](../generators/mediation-xia-chan-2023-continuous-copula-v1.py)

**Keywords (source-described):** Interactions · Nonlinearity

**Observed variables**

X, A, C, M, Y

**Latent variables**

E_M, E_C

**Latent-variable identification:** candidates from equations need review

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

**X,A**

```math
X\sim \mathcal{N}(0,1)
```

```math
A\mid X\sim \mathrm{Bern}(\mathrm{expit}(-0.4+0.6X))
```

**Copula**

```math
(E_{M},E_{C})\sim \mathcal{N}_{2}(0,\begin{bmatrix}
1 & 0.2 \\
0.2 & 1
\end{bmatrix})
```

**Mediator**

```math
M=3+2A+4X+5E_{M}
```

**Confounder**

```math
C=1+2A+2X+4E_{C}
```

**Outcome**

```math
Y=1+2A+2M+3C+5X+4AC+2AM+\varepsilon_{Y}
```

```math
\varepsilon_{Y}\sim \mathcal{N}(0,16)
```

**Target**

```math
\mathrm{NDE}=2+3(2)+4\mathbb{E}[C^{(1)}]+2\mathbb{E}[M^{(0)}]=26
```

<details>
<summary>Original source equations (verbatim)</summary>

<pre>
X~N(0,1); A|X~Bern(expit(-0.4+0.6X))
(E_M,E_C)~N_2(0,[[1,0.2],[0.2,1]])
M=3+2A+4X+5E_M
C=1+2A+2X+4E_C
Y=1+2A+2M+3C+5X+4AC+2AM+epsilon_Y; epsilon_Y~N(0,16)
NDE=2+3(2)+4E[C(1)]+2E[M(0)]=26
</pre>

</details>


## Parameter scenarios, estimands and truth

<table>
<thead><tr><th>Scenario</th><th>Estimand</th><th>Definition</th><th>Reported value</th></tr></thead>
<tbody>
<tr>
<td>section_4_1_continuous</td>
<td rowspan="1">NDE</td>
<td rowspan="1">

$`\mathbb{E}\!\left[Y^{(1,M^{(0)})}-Y^{(0,M^{(0)})}\right]`$

</td>
<td>26.0</td>
</tr>
</tbody>
</table>

**Definition notes**

- All scenarios: The treatment-induced C follows its treatment-specific value in each outcome potential.

<details>
<summary>Submitted estimand definitions</summary>

Submitted English definitions appear below; other original-language definitions remain in the linked JSON. Concise formulas above are display interpretations and still require scientific review.

**Scenario(s):** section_4_1_continuous

E[Y(1,M(0))-Y(0,M(0))], with the treatment-induced C under its own treatment in each outcome potential.

[Open raw scientific record (JSON)](./mediation-xia-chan-2023-continuous-copula-v1.json).

</details>


**Original submitted target notation:** NDE


## Identifiability assumptions

- IID units, consistency, positivity
- Gaussian-copula joint potential construction with shared standardized errors
- Conditional treatment propensity as source
- Cross-world structure for natural direct effect follows the coupled structural equations; such effects require stronger assumptions than interventional effects

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Adaptations from the source (submitted, unverified):**

- Gaussian copula with normal marginals implemented as correlated standard normal errors; this is mathematically equivalent at each A,X.
- Use analytic NDE=26 derived from the displayed equations; the accepted manuscript reports 26.01, and the 0.01 discrepancy remains unresolved.
- n=1500 is source scenario metadata; generator interface permits arbitrary n.
- Ignore deliberate nuisance-model misspecification, which is an estimation setting and not another DGP.

**Warnings:**

- Latent-variable candidates inferred from source equations; confirm their roles and completeness against the original paper or generator.
