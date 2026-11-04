# Poisson Covariates and Poisson Response Semi-Supervised Mean

> **Unverified extraction — scientific review required.**

**Primary area:** Semi-Supervised Inference

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Zhang, A., Brown, L. D. and Cai, T. T. (2019). Semi-supervised inference: General theory and estimation of means. The Annals of Statistics 47(5), 2538-2566. DOI: 10.1214/18-AOS1756.

**DOI:** 10.1214/18-aos1756 · **Source locator:** Pinned arXiv v2 Section 4, setting 3, PDF p. 19 (unnumbered display); Table 1 on PDF p. 20 supplies (p,n,m)=(10,100,1000); sampling equations (1.1)-(1.2), PDF p. 2. These are preprint PDF page numbers, not journal pages.

## DGP / generation mechanism

**Sampling design:** Unit: individual; Dependence: Independent complete-data units; fixed labeled/unlabeled group indicators, not independent Bernoulli indicators. Coordinate dependence is specified in equations.; N Semantics: n is combined table row count; Labeled Reference: 100; Unlabeled Reference: 1000; Predictor Source: No external or oracle predictor supplied. Downstream nuisance regressors must be trained on labeled training folds only; cross-fitting and tuning belong to the later estimator benchmark. No prediction is substituted for Y_obs.

**Generator source:** [generator.py](../generators/sspi-zhang-brown-cai-201910-poisson-v1.py)

**Keywords (source-described):** Linearity

**Observed variables**

X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, R, Y_obs

**Latent variables**

Not explicitly identified (review required)

**Latent-variable identification:** explicit structured metadata

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

**Covariates**

$$
X_{1},\ldots ,X_{10} \text{ independent } \mathrm{Poisson}(10)
$$

**Response**

$$
X_{j}\overset{\mathrm{iid}}{\sim} \mathrm{Poisson}(10)
$$

$$
Y \mid  X \sim \mathrm{Poisson}(10 X_{1})
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
X_1,...,X_10 independent Poisson(10)
X_j iid ~ Poisson(10); Y | X ~ Poisson(10 X_1)
Independent units and independent outcome noise. Two iid samples from the same population; fixed group sizes, R indicates observed Y. Export X,R,Y_obs where Y_obs=Y when R=1 and 0 otherwise; n_total=nL+nU.
</pre>

</details>


## Parameter scenarios, estimands and truth

| Scenario | Estimand | Definition | True value | Evidence status |
|---|---|---|---|---|
| source_fixed | theta = E[Y] | Superpopulation mean theta=E[Y] under the declared fixed mechanism, shared by labeled and unlabeled samples. | 100.0 | reported_numeric |

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
