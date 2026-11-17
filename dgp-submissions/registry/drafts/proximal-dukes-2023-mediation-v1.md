# Natural Direct Effect under Unmeasured Confounding

> **Unverified extraction — scientific review required.**

**Primary area:** Proximal Causal Inference

**Suggested cross-tags (unverified):** mediation

## Reference paper

**Citation:** Dukes, O., Shpitser, I., &amp; Tchetgen Tchetgen, E. J. (2023). Proximal mediation analysis. Biometrika, 110(4), 973–987. DOI: 10.1093/biomet/asad015.

**DOI:** 10.1093/biomet/asad015 · **Source locator:** Section 4, Simulation Studies, advance-access PDF pp. 10–11; data-generating mechanism for Experiment 1.

## DGP / generation mechanism

**Sampling design:** Unit: individual; Dependence: iid individuals; all variables within an individual are jointly generated

**Generator source:** [generator.py](../generators/proximal-dukes-2023-mediation-v1.py)

**Keywords (source-described):** Nonlinearity

**Observed variables**

X1, X2, A, Z, W, M, Y

**Latent variables**

U

**Latent-variable identification:** candidates from equations need review

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

**Original source equations (verbatim):** [Open raw scientific record (JSON)](./proximal-dukes-2023-mediation-v1.json).

```math
\begin{aligned}
(X_1,X_2,U)&\sim\mathcal{N}_{3}((0.25,0.25,0),\Sigma)\\
\Sigma&=\begin{bmatrix}
0.25 & 0 & 0.05\\
0 & 0.25 & 0.05\\
0.05 & 0.05 & 1
\end{bmatrix}
\end{aligned}
```

The covariance matrix is 3 × 3, with rows and columns displayed explicitly.

```math
A\mid X,U\sim\mathrm{Bernoulli}(\mathrm{expit}[-0.5(X_1+X_2)-0.4U])
```

```math
\begin{aligned}
Z&=0.2-0.52A+0.2(X_1+X_2)-U+\varepsilon_{z}\\
W&=0.3+0.2(X_1+X_2)-0.6U+\varepsilon_{w}
\end{aligned}
```

```math
\begin{aligned}
M&=-0.3A-0.5(X_1+X_2)+0.4U+\varepsilon_{m}\\
Y&=2+2A+M+2W-X_1-X_2-U+2\varepsilon_{y}
\end{aligned}
```

```math
\varepsilon_{z},\varepsilon_{w},\varepsilon_{m},\varepsilon_{y}\overset{\mathrm{ind}}{\sim}\mathcal{N}(0,1)
```

The errors are also independent of baseline variables and treatment randomization.


## Parameter scenarios, estimands and truth

| Scenario | Estimand | Definition | Reported value |
|---|---|---|---|
| original | NDE | NDE = E[Y(1,M(0)) - Y(0,M(0))] = 2. | 2.0 |

**Original submitted target notation:** NDE


## Identifiability assumptions

- Consistency, no interference, treatment/mediator support, treatment and mediator exchangeability conditional on (U,X), and the specified cross-world conditions. The treatment/outcome proxies Z and W obey the source's proximal-mediation exclusions; the required bridge exists and the proxies are relevant. Independent exogenous errors underlie the structural interpretation.

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Adaptations from the source (submitted, unverified):**

- English description pending; see [original scientific record](./proximal-dukes-2023-mediation-v1.json).

**Warnings:**

- Latent-variable candidates inferred from source equations; confirm their roles and completeness against the original paper or generator.
