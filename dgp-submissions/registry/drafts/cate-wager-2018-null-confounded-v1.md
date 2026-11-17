# Wager–Athey (2018) simulation 1: zero treatment effect with a beta-density propensity

> **Unverified extraction — scientific review required.**

**Primary area:** CATE — Conditional Average Treatment Effect

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Wager, S. and Athey, S. (2018). Estimation and Inference of Heterogeneous Treatment Effects using Random Forests. Journal of the American Statistical Association 113(523), 1228-1242. DOI: 10.1080/01621459.2017.1319839.

**DOI:** — · **Source locator:** Section 5.1 'Experimental Setup', arXiv:1510.04342v4 (10 Jul 2017) PDF p.20, equation (27); the sentence 'We used n = 500 samples and varied d between 2 and 30' follows the equation on the same page.

## DGP / generation mechanism

**Sampling design:** Unit: individual; Dependence: independent and identically distributed

**Generator source:** [generator.py](../generators/cate-wager-2018-null-confounded-v1.py)

**Keywords (source-described):** Nonlinearity

**Observed variables**

X1–X5 (5 variables), A, Y

<details>
<summary>All observed variable names</summary>

X1, X2, X3, X4, X5, A, Y

</details>

**Latent variables**

Xj

**Latent-variable identification:** candidates from equations need review

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

**X1-X5**

$$
\mathrm{Xj} \sim \mathrm{Uniform}(0,1) \text{ independently }, j = 1..5
$$

**Treatment**

$$
P(A=1\mid X) = 0.25 \cdot  (1 + 20 X_{1} (1-X_{1})^{3})
$$

**Baseline**

$$
m(X) = 2 X_{1} - 1
$$

**Heterogeneity**

$$
\tau(X) = 0
$$

**Outcome**

$$
Y = m(X) + A \tau(X) + \varepsilon, \varepsilon\sim \mathcal{N}(0,1)
$$

<details>
<summary>Original source equations (verbatim)</summary>

<pre>
Xj ~ Uniform(0,1) independently, j = 1..5
P(A=1|X) = 0.25 * (1 + 20 X1 (1-X1)^3)
m(X) = 2 X1 - 1
tau(X) = 0
Y = m(X) + A tau(X) + eps, eps ~ Normal(0,1)
</pre>

</details>


## Parameter scenarios, estimands and truth

| Scenario | Estimand | Definition | Reported value | Evidence status |
|---|---|---|---|---|
| original | CATE | Conditional average treatment effect at the declared query point; in this design it is identically zero for every x, which makes it a null-effect control for bias and interval coverage under confounding. | 0.0 | reported_numeric |

**Original submitted target notation:** tau(x0) = E[Y(1) - Y(0) \| X = x0]


## Identifiability assumptions

- SUTVA: one version of treatment, no interference between individuals
- Unconfoundedness: {Y(0), Y(1)} independent of A given X. In the source this is enforced by construction because the outcome depends on X only through m(X) and the effect is constant
- Overlap: 0.25 &lt;= e(X) &lt;= 0.777 on the whole support of X, since 20 u (1-u)^3 attains its maximum 2.109 at u = 0.25
- Homoscedastic Gaussian noise with unit variance, as in the source

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Adaptations from the source (submitted, unverified):**

- Dimension is fixed at d = 5 instead of the source's d in {2,...,30}; only X1 enters the propensity and the baseline, X2-X5 are irrelevant coordinates kept so the design still has ambient dimension.
- The source writes Y = m(X) + (W - 0.5) tau(X) + eps; this package uses the equivalent contrast form Y = m(X) + A tau(X) + eps with A in {0,1}. The CATE is unchanged, the marginal outcome law differs by the constant 0.5 tau(X) = 0.
- The source reports MSE and coverage over 500 replications at n = 500; this package fixes one scenario and is checked at n = 128 for interface purposes only. No estimator is re-run.
- beta_{2,4} is the Beta(2,4) *density* in the source; it is implemented as 20 u (1-u)^3 so that e(X) = 0.25 (1 + 20 X1 (1-X1)^3).

**Warnings:**

- Latent-variable candidates inferred from source equations; confirm their roles and completeness against the original paper or generator.
