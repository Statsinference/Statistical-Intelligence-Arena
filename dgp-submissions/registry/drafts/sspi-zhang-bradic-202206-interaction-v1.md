# Interaction and Shifted Quadratic Semi-Supervised Mean

> **Unverified extraction — scientific review required.**

**Primary area:** Semi-Supervised Inference

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Zhang, Y. and Bradic, J. (2022). High-dimensional semi-supervised learning: in search of optimal inference of the mean. Biometrika 109(2), 387-403. DOI: 10.1093/biomet/asab042.

**DOI:** 10.1093/biomet/asab042 · **Source locator:** Section 5.1, Model 6, journal p. 399 = PDF p. 13; Model 1 covariates/noise on PDF p. 11; sampling PDF p. 1.

## DGP / generation mechanism

**Sampling design:** Unit: individual; Dependence: Independent complete-data units; fixed labeled/unlabeled group indicators, not independent Bernoulli indicators. Coordinate dependence is specified in equations.; N Semantics: n is combined table row count; Labeled Reference: 100; Unlabeled Reference: 1000; Predictor Source: No external or oracle predictor supplied. Downstream nuisance regressors must be trained on labeled training folds only; cross-fitting and tuning belong to the later estimator benchmark. No prediction is substituted for Y_obs.

**Generator source:** [generator.py](../generators/sspi-zhang-bradic-202206-interaction-v1.py)

**Keywords (source-described):** Interactions · Nonlinearity

**Observed variables**

X1, X2, X3, R, Y_obs

**Latent variables**

epsilon

**Latent-variable identification:** explicit structured metadata

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

**Covariates**

$$
X \sim \mathcal{N}_{3}(0,I)
$$

independent standard Gaussian coordinates

Paper notation p includes intercept: input dimension is p-1.

**Response**

$$
Y = X_{1} X_{2} + 0.5 (X_{3} + 0.5)^{2} + \varepsilon
$$

$$
\varepsilon\sim \mathcal{N}(0,0.25)
$$

**Sampling and observed data**

Independent units and independent outcome noise

$$
\mathrm{Two} \text{ iid } \mathrm{samples} \text{ from } \text{ the } \mathrm{same} \text{ population }
$$

fixed group sizes, R indicates observed Y

$$
\mathrm{Export} X,R,Y_{\mathrm{obs}} \text{ where } Y_{\mathrm{obs}}=Y \text{ when } R=1 \text{ and } 0 \text{ otherwise }
$$

$$
n_{\mathrm{total}}=\mathrm{nL}+\mathrm{nU}.
$$

<details>
<summary>Original source equations (verbatim)</summary>

<pre>
X ~ N_3(0,I); independent standard Gaussian coordinates. Paper notation p includes intercept: input dimension is p-1.
Y = X_1 X_2 + 0.5 (X_3 + 0.5)^2 + epsilon; epsilon ~ N(0,0.25)
Independent units and independent outcome noise. Two iid samples from the same population; fixed group sizes, R indicates observed Y. Export X,R,Y_obs where Y_obs=Y when R=1 and 0 otherwise; n_total=nL+nU.
</pre>

</details>


## Parameter scenarios, estimands and truth

| Scenario | Estimand | Definition | Reported value | Evidence status |
|---|---|---|---|---|
| source_fixed | Population outcome mean | Superpopulation mean theta=E[Y] under the declared fixed mechanism, shared by labeled and unlabeled samples. | 0.625 | reported_numeric |

**Original submitted target notation:** theta = E[Y]


## Identifiability assumptions

- Independent individuals; labeled and unlabeled observations have the same covariate law and common complete-data population.
- Fixed-size labeling independent of X,Y (two-sample/MCAR design); no MAR selection or distribution shift.
- Independent noise as specified; finite second moments; R must mask all uses of Y_obs.

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Adaptations from the source (submitted, unverified):**

- Map the two-sample SS design to one numeric table. API n is total rows, not the paper labeled n; R=1 for labeled rows; Y_obs=0 for R=0 is a sentinel, never a label. Source reference sample sizes are stored separately.
- For arbitrary CPU test n, labeled_count=max(1,min(n-1,floor(n*nL_ref/(nL_ref+nU_ref)))); first labeled_count rows form the independent labeled sample. At n=nL_ref+nU_ref the source counts are exact.
- Independent NumPy PCG64 implementation; no author code copied; original estimator tuning, fitted predictions, repeated CI experiments and PFN training are outside this DGP collection.

**Warnings:**

- Nothing automatically flagged; this does NOT equal scientific acceptance.
