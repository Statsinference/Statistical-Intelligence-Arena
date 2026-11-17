# Linear Bridge Model with Constant ATE

> **Unverified extraction — scientific review required.**

**Primary area:** Proximal Causal Inference

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Cui, Y., Pu, H., Shi, X., Miao, W., &amp; Tchetgen Tchetgen, E. (2024). Semiparametric Proximal Causal Inference. Journal of the American Statistical Association, 119(546), 1348–1359. DOI: 10.1080/01621459.2023.2191817.

**DOI:** 10.1080/01621459.2023.2191817 · **Source locator:** Section 5.1, arXiv v4 PDF pp. 21–22; bridge equations (13)–(14); Appendix H.

## DGP / generation mechanism

**Sampling design:** Unit: individual; Dependence: iid individuals; all variables within an individual are jointly generated

**Generator source:** [generator.py](../generators/proximal-cui-2024-linear-v1.py)

**Keywords (source-described):** Nonlinearity

**Observed variables**

X1, X2, A, Z, W, Y

**Latent variables**

U

**Latent-variable identification:** candidates from equations need review

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

**Original source equations (verbatim):** [Open raw scientific record (JSON)](./proximal-cui-2024-linear-v1.json).

```math
\begin{aligned}
X_1,X_2&\overset{\mathrm{iid}}{\sim}\mathcal{N}(0.25,0.25^2)\\
p(X)&=[1+\exp\{0.125(X_1+X_2)\}]^{-1}\\
A\mid X&\sim\mathrm{Bernoulli}(p(X))
\end{aligned}
```

```math
\begin{aligned}
(Z,W,U)\mid A,X&\sim\mathcal{N}_{3}(m,\Sigma)\\
m&=(0.25+0.25A+0.25s,\ 0.25+0.125A+0.25s,\ 0.25+0.25A+0.25s)\\
s&=X_1+X_2
\end{aligned}
```

```math
\begin{aligned}
\Sigma&=\begin{bmatrix}
1 & 0.25 & 0.5\\
0.25 & 1 & 0.5\\
0.5 & 0.5 & 1
\end{bmatrix}\\
m_W(U,X)&=0.125+0.125s+0.5U
\end{aligned}
```

Covariance matrix: 3 rows and 3 columns.

```math
\begin{aligned}
Y&=2+2A+0.25s+4m_W+2(W-m_W)+\varepsilon\\
\varepsilon&\sim\mathcal{N}(0,0.25^2)
\end{aligned}
```

```math
h(W,A,X)=2+2A+4W+0.25s
```


## Parameter scenarios, estimands and truth

<table>
<thead><tr><th>Scenario</th><th>Estimand</th><th>Definition</th><th>Reported value</th></tr></thead>
<tbody>
<tr>
<td>original</td>
<td rowspan="1">ATE</td>
<td rowspan="1">

$`\mathbb{E}[Y(1)-Y(0)]`$

</td>
<td>2.0</td>
</tr>
</tbody>
</table>

**Definition notes**

- All scenarios: Source population; original bridge-function derivation remains available.

<details>
<summary>Submitted estimand definitions</summary>

Submitted English definitions appear below; other original-language definitions remain in the linked JSON. Concise formulas above are display interpretations and still require scientific review.

**Scenario(s):** original

ATE = E[Y(1)−Y(0)] = 2。

[Open raw scientific record (JSON)](./proximal-cui-2024-linear-v1.json).

</details>


**Original submitted target notation:** ATE


## Identifiability assumptions

- Consistency, no interference, conditional exchangeability of potential outcomes given (U,X), and treatment positivity; exclusion of Z from the outcome, conditional independence of W from (A,Z) given the relevant latent state, and the source's proxy relevance, completeness, and bridge-existence conditions. The retrospective sampling factorization A → (Z,W,U) does not imply that A causally changes baseline U or W.

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Adaptations from the source (submitted, unverified):**

- English description pending; see [original scientific record](./proximal-cui-2024-linear-v1.json).

**Warnings:**

- Latent-variable candidates inferred from source equations; confirm their roles and completeness against the original paper or generator.
