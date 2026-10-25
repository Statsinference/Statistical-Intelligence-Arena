# Two-Period Treatment with Time-Varying Confounding and Feedback

> **Unverified extraction — scientific review required.**

**Primary area:** Proximal Causal Inference

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Ying, A., Miao, W., Shi, X., &amp; Tchetgen Tchetgen, E. J. (2023). Proximal causal inference for complex longitudinal studies. Journal of the Royal Statistical Society Series B, 85(3), 684–704. DOI: 10.1093/jrsssb/qkad020.

**DOI:** 10.1093/jrsssb/qkad020 · **Source locator:** Supplement F.1, combined PDF pp. 47–48, equations (F.1)–(F.3); consistency proof in F.2.

## DGP / generation mechanism

**Sampling design:** Unit: individual; Dependence: iid individuals; longitudinal dependence within each row

**Generator source:** [generator.py](../generators/proximal-ying-2023-longitudinal-v1.py)

**Observed variables**

X0, A0, Z0, W0, X1, A1, Z1, W1, Y

**Latent variables**

U0, U1

**Latent-variable identification:** candidates from equations need review

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

**Original source equations (verbatim):** [Open raw scientific record (JSON)](./proximal-ying-2023-longitudinal-v1.json).

$$
\begin{aligned}
X_0&\sim\mathcal{N}(-0.35,0.5^2)\\
U_0&\sim\mathcal{N}(0.35,0.5^2)\\
p_0&=[1+\exp(0.5-0.35X_0+0.35U_0)]^{-1}
\end{aligned}
$$

X0 and U0 are independent.

$$
\begin{aligned}
A_0&\sim\mathrm{Bernoulli}(p_0)\\
Z_0&=0.2+0.5A_0+0.5X_0+0.75U_0+\varepsilon_{z0}\\
W_0&=0.2+0.5X_0-0.95U_0+\varepsilon_{w0}
\end{aligned}
$$

$$
\begin{aligned}
X_1&=0.2+0.7A_0+0.7X_0+\varepsilon_{x1}\\
U_1&=0.2+0.7A_0+0.7U_0+\varepsilon_{u1}
\end{aligned}
$$

$$
\begin{aligned}
p_1&=[1+\exp\{0.5-0.5A_0-0.35(X_0+X_1)-0.35(U_0+U_1)\}]^{-1}\\
A_1&\sim\mathrm{Bernoulli}(p_1)
\end{aligned}
$$

$$
Z_1=0.2+0.5(A_0+A_1)+0.5(X_0+X_1)-0.75(U_0+U_1)+\varepsilon_{z1}
$$

$$
W_1=0.35+0.45(X_0+X_1)-0.85(U_0+U_1)+\varepsilon_{w1}
$$

$$
Y=-1.3+A_1+1.14A_0+0.5X_1-0.7U_1+0.2X_0-0.7U_0+\varepsilon_{y}
$$

The newly introduced error terms are mutually independent N(0,0.5²).


## Parameter scenarios, estimands and truth

| Scenario | Estimand | Definition | True value | Evidence status |
|---|---|---|---|---|
| original | theta | E[Y(1,1)-Y(0,0)] = 2. | 1.9999999999999998 | reported_numeric |

## Identifiability assumptions

- Sequential consistency and no interference; sequential exchangeability and positivity conditional on the latent history; period-specific proxy exclusion and independence conditions, proxy relevance, and existence of sequential bridge functions as specified in Supplement F.2.

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Warnings:**

- Latent-variable candidates inferred from source equations; confirm their roles and completeness against the original paper or generator.
