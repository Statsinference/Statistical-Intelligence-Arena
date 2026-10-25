# Cross-Trial Transportability with Unmeasured Effect Modification

> **Unverified extraction — scientific review required.**

**Primary area:** Proximal Causal Inference

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Su, Z., Rytgaard, H. C., Ravn, H., &amp; Eriksson, F. (2026). Proximal indirect comparison. Biometrika, 113(1), asaf044. DOI: 10.1093/biomet/asaf044.

**DOI:** 10.1093/biomet/asaf044 · **Source locator:** Section 5.1, arXiv v2 PDF pp. 10–11; Supplement Section S4.1, pp. 30–31.

## DGP / generation mechanism

**Sampling design:** Unit: individual; Dependence: iid individuals; all variables within an individual are jointly generated

**Generator source:** [generator.py](../generators/proximal-su-2026-transport-v1.py)

**Observed variables**

X1, X2, X3, W1, W2, W3, SZ1, SZ2, SZ3, S, SA, SY

**Latent variables**

V, Uj

**Latent-variable identification:** candidates from equations need review

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

**Original source equations (verbatim):** [Open raw scientific record (JSON)](./proximal-su-2026-transport-v1.json).

$$
\begin{aligned}
V&\sim\mathcal{N}_{3}(0,\Sigma_X)\\
\Sigma_X&=\begin{bmatrix}
1 & 0.25 & 0.25\\
0.25 & 1 & 0.25\\
0.25 & 0.25 & 1
\end{bmatrix}\\
X_j&=\Phi(V_j)
\\
U_j&\overset{\mathrm{iid}}{\sim}\mathrm{Uniform}(-1,0)
\end{aligned}
$$

The covariance matrix is 3 × 3, with unit diagonal and off-diagonal 0.25. U is independent of X.

$$
S\mid X,U\sim\mathrm{Bernoulli}(\mathrm{expit}\{-0.625+0.5\sum_jX_j+0.5\sum_jU_j\})
$$

S=1 denotes the source trial; S=0 denotes the target population.

$$
\begin{aligned}
A\mid S=1&\sim\mathrm{Bernoulli}(0.5)\\
Z\mid X,U,S=1&\sim\mathcal{N}_{3}(U+X,0.25I)\\
W\mid X,U&\sim\mathcal{N}_{3}(U+X,0.25I)
\end{aligned}
$$

$$
\begin{aligned}
Y\mid S=1&=0.5-A+\sum_j U_j+A\sum_j U_j+\sum_jX_j\\
&\quad+\sum_jW_j+A\sum_jW_j+\varepsilon\\
\varepsilon&\sim\mathcal{N}(0,0.5^2)
\end{aligned}
$$

$$
\mathrm{observed}\{X,W,S,SA,SZ,SY\}
$$

When S=0, SA/SZ/SY are coded as zero placeholders; the observed S indicator distinguishes unmeasured entries from genuine zero values.


## Parameter scenarios, estimands and truth

| Scenario | Estimand | Definition | True value | Evidence status |
|---|---|---|---|---|
| original | theta | Theta = E[E(Y \| A=1,X,U,S=1) - E(Y \| A=0,X,U,S=1) \| S=0]. | -2.6489954259019695 | reported_numeric |

## Identifiability assumptions

- Randomized treatment in the source trial; transportability of effects conditional on (X,U) and selection overlap. The distribution of W given (X,U) is stable across samples, Z satisfies the source-trial proxy exclusions, and the required bridge and completeness conditions hold. The target population is S=0, not the pooled population.

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Warnings:**

- Latent-variable candidates inferred from source equations; confirm their roles and completeness against the original paper or generator.
