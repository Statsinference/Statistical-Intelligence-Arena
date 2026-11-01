# Nie–Wager (2021) Setup A: Friedman baseline with a sinusoidal propensity

> **Unverified extraction — scientific review required.**

**Primary area:** CATE — Conditional Average Treatment Effect

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Nie, X. and Wager, S. (2021). Quasi-oracle estimation of heterogeneous treatment effects. Biometrika 108(2), 299-319. DOI: 10.1093/biomet/asaa076.

**DOI:** — · **Source locator:** Section 6.1 'Baseline methods and simulation setups', arXiv:1712.04912v4 (6 Aug 2020) PDF p.15 (general data-generating law) and PDF p.16 (unnumbered Setup A paragraph, since the setups carry no equation numbers: 'We use the scaled Friedman (1991) function ... e*(Xi) = trim0.1{sin(pi Xi1 Xi2)} and tau*(Xi) = (Xi1 + Xi2)/2').

## DGP / generation mechanism

**Sampling design:** Unit: individual; Dependence: independent and identically distributed

**Generator source:** [generator.py](../generators/cate-nie-2021-setup-a-v1.py)

**Keywords (source-described):** Interactions · Nonlinearity

**Observed variables**

X1, X2, X3, X4, X5, A, Y

**Latent variables**

Xj

**Latent-variable identification:** candidates from equations need review

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

$$
Xj \sim \mathrm{Uniform}(0,1) independently, j = 1..5
$$

$$
e(X) = trim_\{0.1\}\{ \sin(\pi X_{1} X_{2}) \}, trim_eta(u) = max\{eta, \min(u, 1-eta)\}
$$

$$
b(X) = \sin(\pi X_{1} X_{2}) + 2 (X_{3} - 1/2)^{2} + X_{4} + 0.5 X_{5}
$$

$$
\tau(X) = (X_{1} + X_{2}) / 2
$$

$$
Y = b(X) + A \tau(X) + \sigma eps, eps \sim \mathcal{N}(0,1)
$$

$$
\sigma = 1
$$

<details>
<summary>Original source equations (verbatim)</summary>

<pre>
Xj ~ Uniform(0,1) independently, j = 1..5
e(X) = trim_{0.1}{ sin(pi X1 X2) }, trim_eta(u) = max{eta, min(u, 1-eta)}
b(X) = sin(pi X1 X2) + 2 (X3 - 1/2)^2 + X4 + 0.5 X5
tau(X) = (X1 + X2) / 2
Y = b(X) + A tau(X) + sigma eps, eps ~ Normal(0,1), sigma = 1
</pre>

</details>


## Parameter scenarios, estimands and truth

| Scenario | Estimand | Definition | True value | Evidence status |
|---|---|---|---|---|
| original | tau(x0) = E[Y(1) - Y(0) \| X = x0] | Conditional average treatment effect at the declared query points; a simple linear surface in the first two coordinates, embedded in a deliberately difficult nuisance structure. | 0.25 | reported_numeric |

## Identifiability assumptions

- SUTVA: one version of treatment, no interference
- Unconfoundedness: treatment depends on X only through sin(pi X1 X2), which is also part of the baseline; the design is observational by construction
- Overlap: e(X) is trimmed to [0.1, 0.9], so positivity holds with margin 0.1
- Homoscedastic Gaussian noise; sigma = 1 in this scenario

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Warnings:**

- Latent-variable candidates inferred from source equations; confirm their roles and completeness against the original paper or generator.
