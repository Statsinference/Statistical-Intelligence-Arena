# Rare independent response mixture

> **Unverified extraction — scientific review required.**

**Primary area:** ATE — Average Treatment Effect

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Stefan Wager and Susan Athey (2018). Estimation and Inference of Heterogeneous Treatment Effects using Random Forests. Journal of the American Statistical Association, 113(523):1228–1242. DOI 10.1080/01621459.2017.1319839

**DOI:** 10.1080/01621459.2017.1319839 · **Source locator:** arXiv:1510.04342v4 Appendix B, PDF p.31, unnumbered paragraph beginning “We are in a randomized controlled trial”, equation Yi=2WiAi+epsilon_i and noise/Bernoulli definitions

## DGP / generation mechanism

**Sampling design:** Unit: independent individual; Dependence: All ten observed covariates are irrelevant; effective_dimension=0 and high_dimensional=false. Latent B is never returned. No observed covariate interaction/nonlinear mean is claimed; mixture non-Gaussianity is described separately. Independent treatment/noise random draws conditional on covariates; no clusters or panel structure.

**Generator source:** [generator.py](../generators/ate-wager-athey-2018-06-06-rare-response-v1.py)

**Keywords (source-described):** Linearity

**Observed variables**

X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, A, Y, B

**Latent variables**

B

**Latent-variable identification:** explicit structured metadata

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

$$
X\sim \mathrm{Uniform}([0,1]^{10})
$$

$$
A\sim \mathrm{Bernoulli}(0.5)
$$

independent of X

$$
B\sim \mathrm{Bernoulli}(0.05)
$$

$$
\varepsilon\sim \mathcal{N}(0,0.1\cdot \cdot 2)
$$

independent of X,A and each other

$$
Y=2\cdot A\cdot B+\varepsilon. Source W is treatment A here
$$

source A_i is the latent response indicator B, not a baseline covariate.

<details>
<summary>Original source equations (verbatim)</summary>

<pre>
X~Uniform([0,1]^10); A~Bernoulli(0.5), independent of X.
B~Bernoulli(0.05), epsilon~N(0,0.1**2), independent of X,A and each other.
Y=2*A*B+epsilon. Source W is treatment A here; source A_i is the latent response indicator B, not a baseline covariate.
</pre>

</details>


## Parameter scenarios, estimands and truth

| Scenario | Estimand | Definition | True value | Evidence status |
|---|---|---|---|---|
| original | ATE | E[Y(1)-Y(0)] in the full declared covariate population; treatment 1 versus 0; population, not sample-conditional, target. | 0.1 | reported_numeric |

## Identifiability assumptions

- Consistency and no interference across independent individuals.
- Conditional exchangeability given observed baseline X under the declared synthetic assignment.
- Pointwise positivity; no uniform overlap bound claimed for unbounded Gaussian logistic settings.

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Warnings:**

- Nothing automatically flagged; this does NOT equal scientific acceptance.
