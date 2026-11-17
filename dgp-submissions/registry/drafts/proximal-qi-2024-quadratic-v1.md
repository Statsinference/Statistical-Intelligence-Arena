# Quadratic Baseline Effects and Product Treatment Effect (N2)

> **Unverified extraction — scientific review required.**

**Primary area:** Proximal Causal Inference

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Qi, Z., Miao, R., &amp; Zhang, X. (2024). Proximal Learning for Individualized Treatment Regimes Under Unmeasured Confounding. Journal of the American Statistical Association, 119(546), 915–928. DOI: 10.1080/01621459.2022.2147841.

**DOI:** 10.1080/01621459.2022.2147841 · **Source locator:** Section 6.1, Table 4, model N2, PDF p. 25; nonlinear/X and h0_nonlinear_X_fun branches in the author's simu_setting.py.

## DGP / generation mechanism

**Sampling design:** Unit: individual; Dependence: iid individuals; all variables within an individual are jointly generated

**Generator source:** [generator.py](../generators/proximal-qi-2024-quadratic-v1.py)

**Keywords (source-described):** Interactions · Nonlinearity

**Observed variables**

X1, X2, A, Z, W, Y

**Latent variables**

U

**Latent-variable identification:** candidates from equations need review

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

**Original source equations (verbatim):** [Open raw scientific record (JSON)](./proximal-qi-2024-quadratic-v1.json).

$$
\begin{aligned}
X_1,X_2&\overset{\mathrm{iid}}{\sim}\mathcal{N}(0.25,0.25^2)\\
p(X)&=[1+\exp\{0.125(X_1+X_2)\}]^{-1}\\
A\mid X&\sim\mathrm{Bernoulli}(p(X))
\end{aligned}
$$

$$
\begin{aligned}
(Z,W,U)\mid A,X&\sim\mathcal{N}_{3}(m,\Sigma)\\
m&=(0.25+0.25A+0.25s,\ 0.25+0.125A+0.25s,\ 0.25+0.25A+0.25s)\\
s&=X_1+X_2
\end{aligned}
$$

$$
\begin{aligned}
\Sigma&=\begin{bmatrix}
1 & 0.25 & 0.5\\
0.25 & 1 & 0.5\\
0.5 & 0.5 & 1
\end{bmatrix}\\
m_W(U,X)&=0.125+0.125s+0.5U
\end{aligned}
$$

Covariance matrix: 3 × 3.

$$
\begin{aligned}
Y&=2+X_1^2+X_2^2+5m_W+2(W-m_W)\\
&\quad +A(0.25-6X_1X_2)+\varepsilon\\
\varepsilon&\sim\mathrm{Uniform}(-1,1)
\end{aligned}
$$


## Parameter scenarios, estimands and truth

| Scenario | Estimand | Definition | Reported value | Evidence status |
|---|---|---|---|---|
| N2 | ATE | ATE = E[0.25 - 6X1X2] = -0.125. | -0.125 | reported_numeric |

**Original submitted target notation:** ATE


## Identifiability assumptions

- Consistency, no interference, conditional exchangeability of potential outcomes given (U,X), and treatment positivity; exclusion of Z from the outcome, conditional independence of W from (A,Z) given the relevant latent state, and the source's proxy relevance, completeness, and bridge-existence conditions. The retrospective sampling factorization A → (Z,W,U) does not imply that A causally changes baseline U or W.

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Adaptations from the source (submitted, unverified):**

- English description pending; see [original scientific record](./proximal-qi-2024-quadratic-v1.json).

**Warnings:**

- Latent-variable candidates inferred from source equations; confirm their roles and completeness against the original paper or generator.
