# Yang-He (2012) Section 4.2 Models 1-4: fixed-query conditional 0.95 quantile

> **Unverified extraction — scientific review required.**

**Primary area:** Quantile Inference

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Yang, Yunwen and He, Xuming (2012). Bayesian Empirical Likelihood for Quantile Regression. The Annals of Statistics 40(2), 1102-1131. DOI: 10.1214/12-AOS1005.

**DOI:** 10.1214/12-aos1005 · **Source locator:** Section 4.2, Efficiency of BEL under various priors, main PDF p.13 / printed p.1114, unnumbered Models 1-4; priors main PDF pp.13-14 / printed pp.1114-1115; Table 3 main PDF p.15 / printed p.1116 and Table 4 main PDF p.16 / printed p.1117. Quantile definition Eq.(1.1), main PDF p.1 / printed p.1102; random sampling Eq.(2.1), main PDF p.4 / printed p.1105; Section 3.1 Assumptions 3.1-3.5, main PDF p.7 / printed p.1108. Supplement PDF pages are counted separately.

## DGP / generation mechanism

**Sampling design:** Unit: One synthetic observation (X,Z,Y); n is the number of rows.; Dependence: iid across rows; X, Z, e mutually independent before constructing Y; Y depends on X and Z through the declared law.; Within Unit Dependence: Primitive X,Z,e independent; Z=2B deterministic; G=log(e) for Models2/4; Y depends on X,Z,e. Heteroscedastic scaled noise s(X)e is not independent of X.; Between Unit Dependence: iid synthetic rows; no shared random effects, clusters, panels or network structure.

**Generator source:** [generator.py](../generators/qdi-yang-he-2012-conditional-quantile-v1.py)

**Keywords (source-described):** Linearity

**Observed variables**

X, Z, Y

**Latent variables**

B, e

**Latent-variable identification:** candidates from equations need review

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

$$
X \sim chi-square(df=2)
$$

$$
Z = 2B, B \sim \mathrm{Bernoulli}(0.5)
$$

X, Z, e

mutually independent

$$
Y=X+Z+e
$$

$$
e\sim \mathcal{N}(mean=0, variance=4).
$$

$$
Y=X+Z+e
$$

$$
\log(e)\sim \mathcal{N}(mean=0, variance=1)
$$

e is not centered.

$$
Y=X+Z+(1+X/2)e
$$

$$
e\sim \mathcal{N}(mean=0, variance=4).
$$

$$
Y=X+Z+(1+X/2)e
$$

$$
\log(e)\sim \mathcal{N}(mean=0, variance=1)
$$

e is not centered.

$$
\theta_m=2+s_m(2)q_e(0.95), with s_1=s_2=1, s_3(x)=s_4(x)=1+x/2
$$

$$
q_normal(\tau)=2 Phi^\{-1\}(\tau), q_lognormal(\tau)=\exp(Phi^\{-1\}(\tau)).
$$

<details>
<summary>Original source equations (verbatim)</summary>

<pre>
X ~ chi-square(df=2); Z = 2B, B ~ Bernoulli(0.5); X, Z, e mutually independent.
Y=X+Z+e; e~Normal(mean=0, variance=4).
Y=X+Z+e; log(e)~Normal(mean=0, variance=1); e is not centered.
Y=X+Z+(1+X/2)e; e~Normal(mean=0, variance=4).
Y=X+Z+(1+X/2)e; log(e)~Normal(mean=0, variance=1); e is not centered.
theta_m=2+s_m(2)q_e(0.95), with s_1=s_2=1, s_3(x)=s_4(x)=1+x/2; q_normal(tau)=2 Phi^{-1}(tau), q_lognormal(tau)=exp(Phi^{-1}(tau)).
</pre>

</details>


## Parameter scenarios, estimands and truth

| Scenario | Estimand | Definition | True value | Evidence status |
|---|---|---|---|---|
| model1_normal_homoscedastic | theta_m = Q_0.95(Y \| X=2,Z=0), m=1,2,3,4 | inf{y: F_m(y\|X=2,Z=0)&gt;=0.95} in the model-specific synthetic superpopulation. Conditional, pointwise scalar; not a marginal quantile, regression slope, posterior quantile, sample-mean adjusted intercept or simultaneous band. | 5.289707253902943 | reported_numeric |
| model2_lognormal_homoscedastic | theta_m = Q_0.95(Y \| X=2,Z=0), m=1,2,3,4 | inf{y: F_m(y\|X=2,Z=0)&gt;=0.95} in the model-specific synthetic superpopulation. Conditional, pointwise scalar; not a marginal quantile, regression slope, posterior quantile, sample-mean adjusted intercept or simultaneous band. | 7.18025160223301 | reported_numeric |
| model3_normal_heteroscedastic | theta_m = Q_0.95(Y \| X=2,Z=0), m=1,2,3,4 | inf{y: F_m(y\|X=2,Z=0)&gt;=0.95} in the model-specific synthetic superpopulation. Conditional, pointwise scalar; not a marginal quantile, regression slope, posterior quantile, sample-mean adjusted intercept or simultaneous band. | 8.579414507805886 | reported_numeric |
| model4_lognormal_heteroscedastic | theta_m = Q_0.95(Y \| X=2,Z=0), m=1,2,3,4 | inf{y: F_m(y\|X=2,Z=0)&gt;=0.95} in the model-specific synthetic superpopulation. Conditional, pointwise scalar; not a marginal quantile, regression slope, posterior quantile, sample-mean adjusted intercept or simultaneous band. | 12.36050320446602 | reported_numeric |

## Identifiability assumptions

- Independent identically distributed observed rows (X,Z,Y), as in the random-sample framework of Section 2; within each row X, Z and e are mutually independent as explicitly stated on p.1114.
- Complete observation of X,Z,Y; n denotes the number of iid rows. No missingness, clustering, panel or network dependence is introduced.
- The declared conditional location-scale law defines a continuous version at X=2 despite P(X=2)=0; the query lies inside the continuous X support and Z=0 has probability 0.5.
- The source scale is 1 or 1+X/2, strictly positive on X&gt;=0. Conditional density is continuous and positive at the queried 0.95 quantile, so this quantile is unique.
- For inference using a quantile-regression estimator, correct conditional-quantile specification and a nondegenerate design are relevant. Both covariates are active and E[(1,X,Z)(1,X,Z)^T] is positive definite.
- The source Assumption 3.2 requires bounded covariate support, but the simulation X~chi-square(2) is unbounded. Preserve the simulation law, do not assert all BEL theorem conditions or finite-sample coverage. Prior and EL feasibility assumptions are method-specific and are not certified here.
- Noncausal QDI functional: no intervention, treatment exchangeability, mediation, cross-world or interference assumptions are imposed.

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Warnings:**

- Latent-variable candidates inferred from source equations; confirm their roles and completeness against the original paper or generator.
