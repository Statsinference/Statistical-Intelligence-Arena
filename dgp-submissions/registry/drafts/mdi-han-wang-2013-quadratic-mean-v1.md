# MAR response with quadratic conditional mean and heteroscedastic noise

> **Unverified extraction — scientific review required.**

**Primary area:** Missing Data

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Han, P. and Wang, L. (2013). Estimation with missing data: beyond double robustness. Biometrika 100(2), 417–430. DOI: 10.1093/biomet/ass087.

**DOI:** 10.1093/biomet/ass087 · **Source locator:** Section 6, first of four data-generating models, journal p. 426 (PDF p. 10); Table 1, journal p. 427 (PDF p. 11), gives n=300,1000 and 5000 replications.

## DGP / generation mechanism

**Sampling design:** Unit: individual; Dependence: iid

**Generator source:** [generator.py](../generators/mdi-han-wang-2013-quadratic-mean-v1.py)

**Keywords (source-described):** Nonlinearity

**Observed variables**

X, R, Y_observed

**Latent variables**

Not explicitly identified (review required)

**Latent-variable identification:** not explicitly specified

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

**Covariate**

$$
X \sim \mathrm{Uniform}(-2.5,2.5)
$$

**Full outcome**

$$
Y\mid X=x \sim \mathcal{N}(1+2x+3x^{2}, 4x^{2}+2), \text{ with } \mathrm{second} \mathrm{argument} \text{ variance }
$$

**Observation**

$$
R\mid X=x \sim \mathrm{Bernoulli}(1/[1+\exp(0.8+0.5x-0.3x^{2})])
$$

$$
R=1 \mathrm{means} \text{ observed }
$$

**Observed encoding**

$$
Y_{\mathrm{observed}}=Y \text{ when } R=1 \text{ and } 0 \text{ placeholder } \text{ when } R=0
$$

**Target**

$$
\theta=\mathbb{E}(Y)=7.25
$$

<details>
<summary>Original source equations (verbatim)</summary>

<pre>
X ~ Uniform(-2.5,2.5)
Y|X=x ~ Normal(1+2x+3x^2, 4x^2+2), with second argument variance
R|X=x ~ Bernoulli(1/[1+exp(0.8+0.5x-0.3x^2)]); R=1 means observed
Y_observed=Y when R=1 and 0 placeholder when R=0
theta=E(Y)=7.25
</pre>

</details>


## Parameter scenarios, estimands and truth

| Scenario | Estimand | Definition | True value | Evidence status |
|---|---|---|---|---|
| original | theta = E(Y) | Full-data superpopulation response mean before outcome masking. | 7.25 | reported_numeric |

## Identifiability assumptions

- X is fully observed Uniform(-2.5,2.5).
- Y\|X=x is normal with mean 1+2x+3x^2 and variance 4x^2+2.
- MAR: R is independent of Y conditional on X, and R=1 means Y is observed.
- Observation probability is strictly positive for all X in its compact support.

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Warnings:**

- No explicit latent-variable metadata or reliably identifiable latent declarations; absence from this list does not prove that no latent variables exist.
