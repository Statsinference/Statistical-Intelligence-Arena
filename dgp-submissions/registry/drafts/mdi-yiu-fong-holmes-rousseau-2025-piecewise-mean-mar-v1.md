# Piecewise response mean with discontinuous MAR propensity

> **Unverified extraction — scientific review required.**

**Primary area:** Missing Data

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Yiu, S., Fong, E., Holmes, C. and Rousseau, J. (2025). Semiparametric posterior corrections. Journal of the Royal Statistical Society: Series B 87(4), 1025-1054. DOI: 10.1093/jrsssb/qkaf005.

**DOI:** 10.1093/jrsssb/qkaf005 · **Source locator:** Section 6.2, journal p. 1045 / local main-text PDF p. 21; Table 2 journal p. 1046 / PDF p. 22 labels outcome-mean estimation.

## DGP / generation mechanism

**Sampling design:** Unit: individual; Dependence: iid

**Generator source:** [generator.py](../generators/mdi-yiu-fong-holmes-rousseau-2025-piecewise-mean-mar-v1.py)

**Keywords (source-described):** Nonlinearity

**Observed variables**

X, R, Y_observed

**Latent variables**

Not explicitly identified (review required)

**Latent-variable identification:** not explicitly specified

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

**Full data and observation**

$$
X\sim \mathrm{Uniform}[-1,1]
$$

$$
m(x)=\begin{cases}
(x+2)^{2}/2 & x\in [-1,-0.5) \\
x/2+0.875 & x\in [-0.5,0) \\
-5(x-0.2)^{2}+1.075 & x\in [0,0.5) \\
x+0.125 & x\in [0.5,1]
\end{cases}
$$

$$
Y\mid X=x\sim \mathcal{N}(m(x), [0.2-0.1\cos(2\pi x)]^{2})
$$

$$
R\mid X=x\sim \mathrm{Bernoulli}(0.5+0.4\mathrm{sign}(x)).
$$

**Observed encoding**

$$
Y_{\mathrm{observed}}=Y \text{ if } R=1, \mathrm{else} \mathrm{finite} \mathrm{zero} \text{ placeholder }.
$$

**Target**

$$
\theta=\mathbb{E}(Y)=0.84375
$$

<details>
<summary>Original source equations (verbatim)</summary>

<pre>
X~Uniform[-1,1]; m(x)=(x+2)^2/2 on [-1,-0.5), x/2+0.875 on [-0.5,0), -5(x-0.2)^2+1.075 on [0,0.5), x+0.125 on [0.5,1]; Y|X=x~N(m(x), [0.2-0.1cos(2pi x)]^2); R|X=x~Bernoulli(0.5+0.4sign(x)).
Y_observed=Y if R=1, else finite zero placeholder.
theta=E(Y)=0.84375
</pre>

</details>


## Parameter scenarios, estimands and truth

| Scenario | Estimand | Definition | True value | Evidence status |
|---|---|---|---|---|
| original | theta = E(Y) | Full-data superpopulation response mean before outcome masking. | 0.84375 | reported_numeric |

## Identifiability assumptions

- Covariates are fully observed.
- R is conditionally independent of Y given fully observed covariates (MAR).
- R=1 means Y is observed.
- Observation probabilities are positive.

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Warnings:**

- No explicit latent-variable metadata or reliably identifiable latent declarations; absence from this list does not prove that no latent variables exist.
