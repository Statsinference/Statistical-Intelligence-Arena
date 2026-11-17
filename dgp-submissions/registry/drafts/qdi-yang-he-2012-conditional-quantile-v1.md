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

**Keywords (source-described):** Not specified

**Observed variables**

X, Z, Y

**Latent variables**

B, e

**Latent-variable identification:** candidates from equations need review

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

**Common covariate law, Section 4.2 p.1114**

```math
X \sim \chi-\mathrm{square}(\mathrm{df}=2)
```

```math
Z = 2B, B \sim \mathrm{Bernoulli}(0.5)
```

X, Z, e

mutually independent

**Model 1, p.1114**

```math
Y=X+Z+e
```

```math
e\sim \mathcal{N}(\text{ mean }=0, \text{ variance }=4).
```

**Model 2, p.1114**

```math
Y=X+Z+e
```

```math
\log(e)\sim \mathcal{N}(\text{ mean }=0, \text{ variance }=1)
```

e is not centered.

**Model 3, p.1114**

```math
Y=X+Z+(1+X/2)e
```

```math
e\sim \mathcal{N}(\text{ mean }=0, \text{ variance }=4).
```

**Model 4, p.1114**

```math
Y=X+Z+(1+X/2)e
```

```math
\log(e)\sim \mathcal{N}(\text{ mean }=0, \text{ variance }=1)
```

e is not centered.

**Derived target adaptation**

```math
\theta_{m}=2+s_{m}(2)q_{e}(0.95), \text{ with } s_{1}=s_{2}=1, s_{3}(x)=s_{4}(x)=1+x/2
```

```math
q_{\mathrm{normal}}(\tau)=2 \Phi^{-1}(\tau), q_{\mathrm{lognormal}}(\tau)=\exp(\Phi^{-1}(\tau)).
```

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

| Scenario | Estimand | Definition | Reported value |
|---|---|---|---|
| model1_normal_homoscedastic | Conditional quantile | inf{y: F_m(y\|X=2,Z=0)&gt;=0.95} in the model-specific synthetic superpopulation. Conditional, pointwise scalar; not a marginal quantile, regression slope, posterior quantile, sample-mean adjusted intercept or simultaneous band. | 5.289707253902943 |
| model2_lognormal_homoscedastic | Conditional quantile | inf{y: F_m(y\|X=2,Z=0)&gt;=0.95} in the model-specific synthetic superpopulation. Conditional, pointwise scalar; not a marginal quantile, regression slope, posterior quantile, sample-mean adjusted intercept or simultaneous band. | 7.18025160223301 |
| model3_normal_heteroscedastic | Conditional quantile | inf{y: F_m(y\|X=2,Z=0)&gt;=0.95} in the model-specific synthetic superpopulation. Conditional, pointwise scalar; not a marginal quantile, regression slope, posterior quantile, sample-mean adjusted intercept or simultaneous band. | 8.579414507805886 |
| model4_lognormal_heteroscedastic | Conditional quantile | inf{y: F_m(y\|X=2,Z=0)&gt;=0.95} in the model-specific synthetic superpopulation. Conditional, pointwise scalar; not a marginal quantile, regression slope, posterior quantile, sample-mean adjusted intercept or simultaneous band. | 12.36050320446602 |

**Original submitted target notation:** theta_m = Q_0.95(Y \| X=2,Z=0), m=1,2,3,4


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

**Adaptations from the source (submitted, unverified):**

- Retain the four published data-generating laws and all their parameters. Treat Models 1-4 as four scenarios in one mechanism family.
- Select only tau=0.95 from the original joint levels 0.9, 0.925, 0.95 and target a scalar conditional quantile, not the full vector of regression coefficients.
- Replace the original sample-dependent adjusted intercept at (sample mean X,0) with the fixed query (X,Z)=(2,0), where 2=E[X]. This is a target adaptation, not a reported source-paper truth.
- Use local Python RNG and CPU smoke n=128, seed=1729; original simulations use n=100 and 500 samples. No claim to replicate the original random stream, estimator MSE, priors or MCMC computations.

**Warnings:**

- Latent-variable candidates inferred from source equations; confirm their roles and completeness against the original paper or generator.
