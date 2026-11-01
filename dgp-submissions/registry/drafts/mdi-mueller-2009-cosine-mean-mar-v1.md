# Cosine response mean with logistic MAR

> **Unverified extraction — scientific review required.**

**Primary area:** Missing Data

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Müller, U. U. (2009). Estimating linear functionals in nonlinear regression with responses missing at random. The Annals of Statistics 37(5A), 2245-2277. DOI: 10.1214/08-AOS642.

**DOI:** 10.1214/08-aos642 · **Source locator:** Section 1 independence/MAR assumptions; Section 6.2, journal p. 2269 / local PDF p. 25, nonlinear regression with MAR; Table 1, journal p. 2270 / PDF p. 26 confirms mean-response target.

## DGP / generation mechanism

**Sampling design:** Unit: individual; Dependence: iid

**Generator source:** [generator.py](../generators/mdi-mueller-2009-cosine-mean-mar-v1.py)

**Keywords (source-described):** Nonlinearity

**Observed variables**

X, R, Y_observed

**Latent variables**

Not explicitly identified (review required)

**Latent-variable identification:** not explicitly specified

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

$$
X\sim \mathrm{Uniform}(-1,1)
$$

$$
\varepsilon\sim \mathcal{N}(0,1)
$$

independent of X

$$
Y=\cos(2X)+\varepsilon
$$

$$
R\mid X=x\sim \mathrm{Bernoulli}(\mathrm{expit}(x)).
$$

$$
Y_observed=Y if R=1, else finite zero placeholder.
$$

$$
\theta=\mathbb{E}(Y)=0.454648713412841
$$

<details>
<summary>Original source equations (verbatim)</summary>

<pre>
X~Uniform(-1,1); epsilon~N(0,1) independent of X; Y=cos(2X)+epsilon; R|X=x~Bernoulli(expit(x)).
Y_observed=Y if R=1, else finite zero placeholder.
theta=E(Y)=0.454648713412841
</pre>

</details>


## Parameter scenarios, estimands and truth

| Scenario | Estimand | Definition | True value | Evidence status |
|---|---|---|---|---|
| original | theta = E(Y) | Full-data superpopulation response mean before outcome masking. | 0.45464871341284085 | reported_numeric |

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
