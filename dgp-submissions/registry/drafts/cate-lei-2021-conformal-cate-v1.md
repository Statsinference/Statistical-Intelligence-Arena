# Lei–Candès (2021) simulation: zero control outcome with a double-sigmoid effect

> **Unverified extraction — scientific review required.**

**Primary area:** CATE — Conditional Average Treatment Effect

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Lei, L. and Candes, E. J. (2021). Conformal inference of counterfactuals and individual treatment effects. Journal of the Royal Statistical Society: Series B (Statistical Methodology) 83(5), 911-938. DOI: 10.1111/rssb.12445.

**DOI:** — · **Source locator:** Section 3.6 'Numerical experiments', arXiv:2006.06138v2 (6 May 2021) PDF p.9 (covariate construction: 'Xj = Phi(X'_j) ... equicorrelated multivariate Gaussian') and PDF p.10 (second and third bullets: 'Y(0) = 0', 'E[Y(1)\|X] = f(X1) f(X2), f(x) = 2/(1+exp{-12(x-0.5)})', and 'e(x) = (1/4){1 + beta_{2,4}(x1)}'). The section uses unnumbered bullets, so the locator cites the bullets and page rather than an equation number.

## DGP / generation mechanism

**Sampling design:** Unit: individual; Dependence: independent and identically distributed at rho = 0

**Generator source:** [generator.py](../generators/cate-lei-2021-conformal-cate-v1.py)

**Keywords (source-described):** Interactions · Nonlinearity

**Observed variables**

X1–X10 (10 variables), A, Y

<details>
<summary>All observed variable names</summary>

X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, A, Y

</details>

**Latent variables**

Not explicitly identified (review required)

**Latent-variable identification:** not explicitly specified

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

**X1-X10**

```math
\mathrm{Xj} = \Phi(X'_{j}), X' \mathrm{equicorrelated} \mathrm{Gaussian} \text{ with } \rho= 0, \mathrm{so} \mathrm{Xj} \sim \mathrm{Uniform}(0,1) \text{ independently }, j = 1..10
```

**Treatment**

```math
e(X) = (1/4) \{1 + F_{2,4}(X_{1})\}, F_{2,4} \text{ the } \mathrm{Beta}(2,4) \mathrm{cdf}
```

**Control outcome**

```math
Y(0) = 0
```

**Treated outcome**

```math
\mathbb{E}[Y(1)\mid X] = f(X_{1}) f(X_{2}), f(u) = 2 / (1 + \exp(-12 (u - 1/2)))
```

```math
Y(1) = \mathbb{E}[Y(1)\mid X] + \sigma\varepsilon
```

**Heterogeneity**

```math
\tau(X) = f(X_{1}) f(X_{2})
```

**Observed**

```math
Y = A Y(1) + (1-A) Y(0)
```

```math
\sigma= 1
```

<details>
<summary>Original source equations (verbatim)</summary>

<pre>
Xj = Phi(X&#x27;_j), X&#x27; equicorrelated Gaussian with rho = 0, so Xj ~ Uniform(0,1) independently, j = 1..10
e(X) = (1/4) { 1 + F_{2,4}(X1) }, F_{2,4} the Beta(2,4) cdf
Y(0) = 0
E[Y(1)|X] = f(X1) f(X2), f(u) = 2 / (1 + exp(-12 (u - 1/2)));  Y(1) = E[Y(1)|X] + sigma eps
tau(X) = f(X1) f(X2)
Y = A Y(1) + (1-A) Y(0), sigma = 1
</pre>

</details>


## Parameter scenarios, estimands and truth

| Scenario | Estimand | Definition | Reported value |
|---|---|---|---|
| original | CATE | Conditional average treatment effect at the declared query points when the control potential outcome is identically zero, so the effect equals the treated conditional mean. | 1.0 |

**Original submitted target notation:** tau(x0) = E[Y(1) - Y(0) \| X = x0]


## Identifiability assumptions

- SUTVA: one version of treatment, no interference
- Unconfoundedness: the propensity depends on X1 only, and Y(1) depends on X1 and X2, so the assignment is confounded
- Overlap: e(X) in [0.25, 0.5] by construction, giving a uniform overlap margin of 0.25
- Homoscedastic Gaussian noise with sigma^2 = 1, added only under treatment because Y(0) = 0

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Adaptations from the source (submitted, unverified):**

- The source uses d = 10 or d = 100 covariates and an equicorrelation rho in {0, 0.9}; this package fixes d = 10 with rho = 0, so the covariates are independent uniforms and X3..X10 are inert.
- Only the homoscedastic scenario sigma^2 = 1 is used; the source also reports sigma^2(x) = -log(x1).
- Phi(Z) with Z standard normal is distributed as Uniform(0,1), so the covariates are drawn directly as uniforms; no numerical normal cdf is needed at rho = 0.
- The source evaluates interval coverage of CATE and ITE; this package only declares the mechanism and its population CATE. No conformal procedure is run.

**Warnings:**

- No explicit latent-variable metadata or reliably identifiable latent declarations; absence from this list does not prove that no latent variables exist.
