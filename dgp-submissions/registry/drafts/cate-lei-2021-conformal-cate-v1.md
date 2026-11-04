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

X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, A, Y

**Latent variables**

Not explicitly identified (review required)

**Latent-variable identification:** not explicitly specified

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

**X1-X10**

$$
\mathrm{Xj} = \Phi(X'_{j}), X' \mathrm{equicorrelated} \mathrm{Gaussian} \text{ with } \rho= 0, \mathrm{so} \mathrm{Xj} \sim \mathrm{Uniform}(0,1) \text{ independently }, j = 1..10
$$

**Treatment**

$$
e(X) = (1/4) \{1 + F_{2,4}(X_{1})\}, F_{2,4} \text{ the } \mathrm{Beta}(2,4) \mathrm{cdf}
$$

**Control outcome**

$$
Y(0) = 0
$$

**Treated outcome**

$$
\mathbb{E}[Y(1)\mid X] = f(X_{1}) f(X_{2}), f(u) = 2 / (1 + \exp(-12 (u - 1/2)))
$$

$$
Y(1) = \mathbb{E}[Y(1)\mid X] + \sigma\varepsilon
$$

**Heterogeneity**

$$
\tau(X) = f(X_{1}) f(X_{2})
$$

**Observed**

$$
Y = A Y(1) + (1-A) Y(0)
$$

$$
\sigma= 1
$$

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

| Scenario | Estimand | Definition | True value | Evidence status |
|---|---|---|---|---|
| original | tau(x0) = E[Y(1) - Y(0) \| X = x0] | Conditional average treatment effect at the declared query points when the control potential outcome is identically zero, so the effect equals the treated conditional mean. | 1.0 | reported_numeric |

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

**Warnings:**

- No explicit latent-variable metadata or reliably identifiable latent declarations; absence from this list does not prove that no latent variables exist.
