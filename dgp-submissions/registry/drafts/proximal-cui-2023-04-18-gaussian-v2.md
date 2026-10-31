# Single-time Gaussian proximal ATE

> **Unverified extraction — scientific review required.**

**Primary area:** Proximal Causal Inference

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Yifan Cui, Hongming Pu, Xu Shi, Wang Miao, Eric Tchetgen Tchetgen (2024). Semiparametric Proximal Causal Inference. Journal of the American Statistical Association, 119(546), 1348-1359. DOI: 10.1080/01621459.2023.2191817.

**DOI:** 10.1080/01621459.2023.2191817 · **Source locator:** arXiv:2011.08411v4; PDF pp.21-22, Section 5.1, Eqs.(13)-(14)

## DGP / generation mechanism

**Sampling design:** Unit: individual; Dependence: English description not yet supplied; consult the original scientific record (JSON).

**Generator source:** [generator.py](../generators/proximal-cui-2023-04-18-gaussian-v2.py)

**Keywords (source-described):** Nonlinearity

**Observed variables**

X1, X2, A, Z, W, Y, U

**Latent variables**

Not explicitly identified (review required)

**Latent-variable identification:** not explicitly specified

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

**Original source equations (verbatim):** [Open raw scientific record (JSON)](./proximal-cui-2023-04-18-gaussian-v2.json).

English equation transcription pending

see the original record (JSON).

$$
1. `X \sim Normal_2((0.25,0.25), \begin{bmatrix}
0.0625 & 0 \\
0 & 0.0625
\end{bmatrix})`
$$

$$
2. `A \mid  X \sim \mathrm{Bernoulli}(\sigma(-0.125 X_{1} - 0.125 X_{2}))`
$$

English equation transcription pending

see the original record (JSON).

$$
`\mu(A,X) = (0.25,0.25,0.25)^T + A(0.25,0.125,0.25)^T + (0.25 X_{1} + 0.25 X_{2})(1,1,1)^T`
$$

English equation transcription pending

see the original record (JSON).

English equation transcription pending

see the original record (JSON).

$$
`Y = 2 + 2A + 0.25(X_{1}+X_{2}) + (4-2)g(U,X) + 2W + \varepsilon Y`
$$

English equation transcription pending

see the original record (JSON).


## Parameter scenarios, estimands and truth

| Scenario | Estimand | Definition | True value | Evidence status |
|---|---|---|---|---|
| original | psi_ATE | E[Y(1)-Y(0)] in the source population, same marginal U,W,X under both interventions. | 2.0 | reported_numeric |

## Identifiability assumptions

- Consistency, well-defined binary interventions, no interference and IID people
- Y independent of Z given U,A,X; W independent of (A,Z) given U,X
- Y(a) independent of A given U,X; positivity given U,X
- Outcome bridge existence and Gaussian completeness/rank conditions of Cui et al. Theorem 2.1; fixed nondegenerate covariance as specified; no uniform positivity bound on Gaussian tails
- The observational factorization X,A,(Z,W,U),Y does not imply a causal arrow A to baseline U

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** exact_reproduction

**Status:** needs_scientific_review

**Warnings:**

- No explicit latent-variable metadata or reliably identifiable latent declarations; absence from this list does not prove that no latent variables exist.
