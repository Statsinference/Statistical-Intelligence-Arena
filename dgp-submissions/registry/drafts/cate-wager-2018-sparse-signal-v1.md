# Wager–Athey (2018) appendix design: effect spread over q signal coordinates

> **Unverified extraction — scientific review required.**

**Primary area:** CATE — Conditional Average Treatment Effect

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Wager, S. and Athey, S. (2018). Estimation and Inference of Heterogeneous Treatment Effects using Random Forests. Journal of the American Statistical Association 113(523), 1228-1242. DOI: 10.1080/01621459.2017.1319839.

**DOI:** — · **Source locator:** Appendix A 'Additional Simulations', arXiv:1510.04342v4 (10 Jul 2017) PDF p.30, equation (30) for tau(x) and Table 5 (p.30) for the (q, d) grid; the preceding paragraph states 'we generate data with a treatment effect function (30)'.

## DGP / generation mechanism

**Sampling design:** Unit: individual; Dependence: independent and identically distributed

**Generator source:** [generator.py](../generators/cate-wager-2018-sparse-signal-v1.py)

**Keywords (source-described):** Nonlinearity

**Observed variables**

X1, X2, X3, X4, X5, X6, A, Y

**Latent variables**

Xj

**Latent-variable identification:** candidates from equations need review

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

$$
Xj \sim \mathrm{Uniform}(0,1) independently, j = 1..6
$$

$$
P(A=1\mid X) = 0.5
$$

$$
m(X) = 0
$$

$$
\tau(X) = (4/q) sum_\{j=1..q\} [1/(1+\exp(-12 (Xj - 1/2))) - 1/2]
$$

$$
q = 4
$$

$$
Y = m(X) + A \tau(X) + eps, eps \sim \mathcal{N}(0,1)
$$

<details>
<summary>Original source equations (verbatim)</summary>

<pre>
Xj ~ Uniform(0,1) independently, j = 1..6
P(A=1|X) = 0.5
m(X) = 0
tau(X) = (4/q) sum_{j=1..q} [1/(1+exp(-12 (Xj - 1/2))) - 1/2], q = 4
Y = m(X) + A tau(X) + eps, eps ~ Normal(0,1)
</pre>

</details>


## Parameter scenarios, estimands and truth

| Scenario | Estimand | Definition | True value | Evidence status |
|---|---|---|---|---|
| original | tau(x0) = E[Y(1) - Y(0) \| X = x0] | Conditional average treatment effect when the signal is spread additively over q = 4 of the 6 coordinates; the estimand at a query point is the sum of four sigmoid contributions minus 2. | 0.9836748576936802 | reported_numeric |

## Identifiability assumptions

- SUTVA: one version of treatment, no interference
- Randomised assignment: e(x) = 0.5, so unconfoundedness holds by design
- Overlap: e(x) = 0.5 with margin 0.5
- Homoscedastic Gaussian noise with unit variance

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Warnings:**

- Latent-variable candidates inferred from source equations; confirm their roles and completeness against the original paper or generator.
