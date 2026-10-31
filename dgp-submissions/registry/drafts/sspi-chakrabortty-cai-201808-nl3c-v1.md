# Three-Component Quadratic Semi-Supervised Projection Intercept

> **Unverified extraction — scientific review required.**

**Primary area:** Semi-Supervised Inference

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Chakrabortty, A. and Cai, T. (2018). Efficient and adaptive linear regression in semi-supervised settings. The Annals of Statistics 46(4), 1541-1572. DOI: 10.1214/17-AOS1594.

**DOI:** 10.1214/17-aos1594 · **Source locator:** Section 6.1, model (iv), journal p. 1559 = PDF p. 19; n=500 and N=10000 on journal p. 1558 = PDF p. 18; regression target in Section 2.

## DGP / generation mechanism

**Sampling design:** Unit: individual; Dependence: Independent complete-data units; fixed labeled/unlabeled group indicators, not independent Bernoulli indicators. Coordinate dependence is specified in equations.; N Semantics: n is combined table row count; Labeled Reference: 500; Unlabeled Reference: 10000; Predictor Source: No external or oracle predictor supplied. Downstream nuisance regressors must be trained on labeled training folds only; cross-fitting and tuning belong to the later estimator benchmark. No prediction is substituted for Y_obs.

**Generator source:** [generator.py](../generators/sspi-chakrabortty-cai-201808-nl3c-v1.py)

**Keywords (source-described):** Interactions · Nonlinearity

**Observed variables**

X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, R, Y_obs

**Latent variables**

epsilon

**Latent-variable identification:** explicit structured metadata

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

$$
Coordinates independent \mathcal{N}(0,1) conditional on -5 <= X_j <= 5
$$

implemented by rejection, not clipping. This makes the source restriction explicit.

$$
p=10
$$

$$
b_{1}=(1,1,1,1,1,0,0,0,0,0)
$$

$$
b_{2}=(1,1,1,1,1,1,1,1,1,1)
$$

$$
\delta=(0,0,0,0,0,1,1,1,1,1)
$$

$$
omega=(1,0,1,0,1,0,1,0,1,0).
$$

$$
Y = (X^T b)(1 + X^T \delta) + (X^T omega)^{2} + \varepsilon
$$

$$
\varepsilon \sim \mathcal{N}(0,1)
$$

$$
Independent units and independent outcome noise. Two iid samples from the same population
$$

$$
fixed group sizes, R indicates observed Y. Export X,R,Y_obs where Y_obs=Y when R=1 and 0 otherwise
$$

$$
n_total=nL+nU.
$$

<details>
<summary>Original source equations (verbatim)</summary>

<pre>
Coordinates independent N(0,1) conditional on -5 &lt;= X_j &lt;= 5; implemented by rejection, not clipping. This makes the source restriction explicit.
p=10; b1=(1,1,1,1,1,0,0,0,0,0), b2=(1,1,1,1,1,1,1,1,1,1); delta=(0,0,0,0,0,1,1,1,1,1); omega=(1,0,1,0,1,0,1,0,1,0).
Y = (X^T b)(1 + X^T delta) + (X^T omega)^2 + epsilon; epsilon ~ N(0,1)
Independent units and independent outcome noise. Two iid samples from the same population; fixed group sizes, R indicates observed Y. Export X,R,Y_obs where Y_obs=Y when R=1 and 0 otherwise; n_total=nL+nU.
</pre>

</details>


## Parameter scenarios, estimands and truth

| Scenario | Estimand | Definition | True value | Evidence status |
|---|---|---|---|---|
| source_b1_conditional_truncation | alpha_projection = E[Y] | Intercept alpha of argmin_(alpha,beta) E[(Y-alpha-X^T beta)^2]; since E[X]=0 and Cov(X) is positive definite, alpha=E[Y]. | 4.999925663981647 | reported_numeric |
| source_b2_conditional_truncation | alpha_projection = E[Y] | Intercept alpha of argmin_(alpha,beta) E[(Y-alpha-X^T beta)^2]; since E[X]=0 and Cov(X) is positive definite, alpha=E[Y]. | 9.999851327963293 | reported_numeric |

## Identifiability assumptions

- Independent individuals; labeled and unlabeled observations have the same covariate law and common complete-data population.
- Fixed-size labeling independent of X,Y (two-sample/MCAR design); no MAR selection or distribution shift.
- Independent noise as specified; finite second moments; R must mask all uses of Y_obs.

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Warnings:**

- Nothing automatically flagged; this does NOT equal scientific acceptance.
