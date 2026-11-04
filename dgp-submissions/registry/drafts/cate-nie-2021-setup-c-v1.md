# Nie–Wager (2021) Setup C: constant effect under a logistic propensity

> **Unverified extraction — scientific review required.**

**Primary area:** CATE — Conditional Average Treatment Effect

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Nie, X. and Wager, S. (2021). Quasi-oracle estimation of heterogeneous treatment effects. Biometrika 108(2), 299-319. DOI: 10.1093/biomet/asaa076.

**DOI:** — · **Source locator:** Section 6.1, arXiv:1712.04912v4 (6 Aug 2020) PDF p.16, unnumbered Setup C paragraph (no equation number in the source): 'e*(Xi) = 1/(1 + e^{Xi2+Xi3}), b*(Xi) = 2 log(1 + e^{Xi1+Xi2+Xi3}), and the treatment effect is constant, tau*(Xi) = 1'.

## DGP / generation mechanism

**Sampling design:** Unit: individual; Dependence: independent and identically distributed

**Generator source:** [generator.py](../generators/cate-nie-2021-setup-c-v1.py)

**Keywords (source-described):** Nonlinearity

**Observed variables**

X1, X2, X3, A, Y

**Latent variables**

Xj

**Latent-variable identification:** candidates from equations need review

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

**X1-X3**

$$
\mathrm{Xj} \sim \mathcal{N}(0,1) \text{ independently }, j = 1..3
$$

**Treatment**

$$
e(X) = 1 / (1 + \exp(X_{2} + X_{3}))
$$

**Baseline**

$$
b(X) = 2 \log(1 + \exp(X_{1} + X_{2} + X_{3}))
$$

**Heterogeneity**

$$
\tau(X) = 1
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
Xj ~ Normal(0,1) independently, j = 1..3
e(X) = 1 / (1 + exp(X2 + X3))
b(X) = 2 log(1 + exp(X1 + X2 + X3))
tau(X) = 1
Y = b(X) + A tau(X) + sigma eps, eps ~ Normal(0,1), sigma = 1
</pre>

</details>


## Parameter scenarios, estimands and truth

| Scenario | Estimand | Definition | True value | Evidence status |
|---|---|---|---|---|
| original | tau(x0) = E[Y(1) - Y(0) \| X = x0] | Conditional average treatment effect at the declared query points; constant equal to 1 for every x, so the whole difficulty is the strongly confounded nuisance structure. | 1.0 | reported_numeric |

## Identifiability assumptions

- SUTVA: one version of treatment, no interference
- Unconfoundedness: treatment depends on X2 + X3, which also enters the baseline; the design is observational
- Overlap: e(x) = 1/(1+e^{x2+x3}) is strictly inside (0,1) for every finite x, but the tails are thin; no uniform bound is claimed
- Homoscedastic Gaussian noise with sigma = 1

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Warnings:**

- Latent-variable candidates inferred from source equations; confirm their roles and completeness against the original paper or generator.
