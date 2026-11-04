# Nie–Wager (2021) Setup B: randomised trial with a logarithmic treatment effect

> **Unverified extraction — scientific review required.**

**Primary area:** CATE — Conditional Average Treatment Effect

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Nie, X. and Wager, S. (2021). Quasi-oracle estimation of heterogeneous treatment effects. Biometrika 108(2), 299-319. DOI: 10.1093/biomet/asaa076.

**DOI:** — · **Source locator:** Section 6.1, arXiv:1712.04912v4 (6 Aug 2020) PDF p.16, unnumbered Setup B paragraph (no equation number in the source): 'Here, e*(x) = 1/2 for all x ... Xi ~ N(0, I_{d x d}), tau*(Xi) = Xi1 + log(1 + e^{Xi2}), and b*(Xi) = max{Xi1 + Xi2, Xi3, 0} + max{Xi4 + Xi5, 0}'.

## DGP / generation mechanism

**Sampling design:** Unit: individual; Dependence: independent and identically distributed

**Generator source:** [generator.py](../generators/cate-nie-2021-setup-b-v1.py)

**Keywords (source-described):** Interactions · Nonlinearity

**Observed variables**

X1, X2, X3, X4, X5, A, Y

**Latent variables**

Xj

**Latent-variable identification:** candidates from equations need review

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

**X1-X5**

$$
\mathrm{Xj} \sim \mathcal{N}(0,1) \text{ independently }, j = 1..5
$$

**Treatment**

$$
e(X) = 1/2
$$

**Baseline**

$$
b(X) = \max\{X_{1} + X_{2}, X_{3}, 0\} + \max\{X_{4} + X_{5}, 0\}
$$

**Heterogeneity**

$$
\tau(X) = X_{1} + \log(1 + \exp(X_{2}))
$$

**Outcome**

$$
Y = b(X) + A \tau(X) + \sigma\varepsilon, \varepsilon\sim \mathcal{N}(0,1)
$$

$$
\sigma= 1
$$

<details>
<summary>Original source equations (verbatim)</summary>

<pre>
Xj ~ Normal(0,1) independently, j = 1..5
e(X) = 1/2
b(X) = max{X1 + X2, X3, 0} + max{X4 + X5, 0}
tau(X) = X1 + log(1 + exp(X2))
Y = b(X) + A tau(X) + sigma eps, eps ~ Normal(0,1), sigma = 1
</pre>

</details>


## Parameter scenarios, estimands and truth

| Scenario | Estimand | Definition | True value | Evidence status |
|---|---|---|---|---|
| original | tau(x0) = E[Y(1) - Y(0) \| X = x0] | Conditional average treatment effect at the declared query points; linear in X1 plus a log-sum-exp transform of X2. | 1.4740769841801067 | reported_numeric |

## Identifiability assumptions

- SUTVA: one version of treatment, no interference
- Randomised assignment: e(x) = 1/2, so unconfoundedness holds by design and no propensity adjustment is needed
- Overlap: e(x) = 1/2 with margin 0.5
- Homoscedastic Gaussian noise with sigma = 1

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Warnings:**

- Latent-variable candidates inferred from source equations; confirm their roles and completeness against the original paper or generator.
