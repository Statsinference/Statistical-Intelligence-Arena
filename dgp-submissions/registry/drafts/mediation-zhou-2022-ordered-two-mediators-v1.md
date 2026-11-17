# Cumulative path-specific effect through the second of two causally ordered mediators

> **Unverified extraction — scientific review required.**

**Primary area:** Mediation — Direct and Indirect Effects

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Zhou, X. (2022). Semiparametric estimation for causal mediation analysis with multiple causally ordered mediators. Journal of the Royal Statistical Society Series B: Statistical Methodology 84(3), 794-821. DOI: 10.1111/rssb.12487.

**DOI:** 10.1111/rssb.12487 · **Source locator:** Section 5 'A Simulation Study' (arXiv:2011.12751v2 PDF page 28) gives the structural model; Supplementary Material F (arXiv:2011.12751v2 PDF page 56) gives the numerical coefficients beta_X1..beta_X4, beta_A, beta_M1, beta_M2, beta_Y. Estimand cPSE defined in Section 4.4 and equation (19), PDF page 32.

## DGP / generation mechanism

**Sampling design:** Unit: individual; Dependence: iid individuals; all variables within an individual are generated jointly in temporal order

**Generator source:** [generator.py](../generators/mediation-zhou-2022-ordered-two-mediators-v1.py)

**Keywords (source-described):** Nonlinearity

**Observed variables**

X1–X4 (4 variables), A, M1, M2, Y

<details>
<summary>All observed variable names</summary>

X1, X2, X3, X4, A, M1, M2, Y

</details>

**Latent variables**

U1, U2, U3, UXY

**Latent-variable identification:** explicit structured metadata

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

**Latent errors**

```math
(U_{1},U_{2},U_{3},UXY) \sim \mathcal{N}(0, I_{4})
```

**Baseline covariates**

```math
\mathrm{Xj} \sim \mathcal{N}((U_{1},U_{2},U_{3},UXY) \beta_{\mathrm{Xj}}, 1), j = 1,2,3,4
```

**Treatment**

```math
A \sim \mathrm{Bernoulli}(\mathrm{logit}^{-1}[(1,X_{1},X_{2},X_{3},X_{4}) \beta_{A}])
```

**First mediator**

```math
M_{1} \sim \mathcal{N}((1,X_{1},X_{2},X_{3},X_{4},A) \beta_{\mathrm{M1}}, 1)
```

**Second mediator**

```math
M_{2} \sim \mathcal{N}((1,X_{1},X_{2},X_{3},X_{4},A,M_{1}) \beta_{\mathrm{M2}}, 1)
```

**Outcome**

```math
Y \sim \mathcal{N}((1,UXY,X_{1},X_{2},X_{3},X_{4},A,M_{1},M_{2}) \beta_{Y}, 1)
```

**Coefficients (Supplementary Material F)**

```math
\beta_{\mathrm{X1}}=(0.77,-0.86,0.35,0.88)
```

```math
\beta_{\mathrm{X2}}=(-0.99,-0.72,-0.1,0.54)
```

```math
\beta_{\mathrm{X3}}=(-0.74,0.1,0.91,0.46)
```

```math
\beta_{\mathrm{X4}}=(-0.21,-0.43,-0.21,-0.7)
```

```math
\beta_{A}=(-0.36,-0.08,-0.06,0.4,-0.14)
```

```math
\beta_{\mathrm{M1}}=(0,0.3,0.42,0.48,0.28,0.41)
```

```math
\beta_{\mathrm{M2}}=(0.04,0.2,0.09,0.12,0.39,0.34,0.24)
```

```math
\beta_{Y}=(-0.27,-0.1,0.25,0.2,-0.08,0.78,0.76,-0.4,0.96)
```

<details>
<summary>Original source equations (verbatim)</summary>

<pre>
(U1,U2,U3,UXY) ~ N(0, I_4)
Xj ~ N((U1,U2,U3,UXY) beta_Xj, 1), j = 1,2,3,4
A ~ Bernoulli(logit^{-1}[(1,X1,X2,X3,X4) beta_A])
M1 ~ N((1,X1,X2,X3,X4,A) beta_M1, 1)
M2 ~ N((1,X1,X2,X3,X4,A,M1) beta_M2, 1)
Y ~ N((1,UXY,X1,X2,X3,X4,A,M1,M2) beta_Y, 1)
beta_X1=(0.77,-0.86,0.35,0.88); beta_X2=(-0.99,-0.72,-0.1,0.54); beta_X3=(-0.74,0.1,0.91,0.46); beta_X4=(-0.21,-0.43,-0.21,-0.7); beta_A=(-0.36,-0.08,-0.06,0.4,-0.14); beta_M1=(0,0.3,0.42,0.48,0.28,0.41); beta_M2=(0.04,0.2,0.09,0.12,0.39,0.34,0.24); beta_Y=(-0.27,-0.1,0.25,0.2,-0.08,0.78,0.76,-0.4,0.96)
</pre>

</details>


## Parameter scenarios, estimands and truth

| Scenario | Estimand | Definition | Reported value |
|---|---|---|---|
| original | Cumulative path-specific effect | Cumulative path-specific effect through the second mediator: theta_{a1,a2,a3} = E[Y(a3, M1(a1), M2(a2, M1(a1)))], and cPSE_M2 = theta_011 - theta_001 holds the Y-argument at A=1 and the M1-argument at A=0 while moving only the M2-argument from A=0 to A=1. This is NOT the natural indirect effect, NOT the natural direct effect and NOT the total effect. | 0.3264 |

**Original submitted target notation:** cPSE_M2 = theta_011 - theta_001


## Identifiability assumptions

- Consistency and well-defined joint interventions on A, M1 and M2
- Independent individuals; no interference
- Pearl NPSEM with mutually independent errors, as assumed by the source (its Assumptions 1-3)
- Causal ordering A -&gt; M1 -&gt; M2 -&gt; Y with no M2 -&gt; M1 arrow
- Cross-world independence implied by the mutually independent-error NPSEM; cPSEs are not identified by conditional-exchangeability assumptions alone
- Treatment positivity on the declared support; the logistic propensity is bounded away from 0 and 1 for finite covariates but no uniform overlap bound is claimed on unbounded Gaussian support
- The latent variable UXY confounds X and Y but, as the source states, does not threaten identification of theta_{a1,a2,a3} because it is a pre-treatment common cause

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Adaptations from the source (submitted, unverified):**

- Version used: arXiv:2011.12751v2 (2021-11-10) preprint of the JRSS-B 2022 article; the journal version was not accessible to the collector, so section/page locators refer to the preprint PDF and the coefficient values are taken from its Supplementary Material F. Any numbering difference between preprint and journal version is unverified.
- The source draws beta_X1..beta_X4 and beta_Y from Uniform[-1,1], beta_A from Uniform[-0.5,0.5], and beta_M1, beta_M2 from Uniform[0,0.5]; Supplementary Material F reports the realised values, which are registered here as FIXED parameters of one mechanism. The uniform draw itself is not re-sampled, so this is a single fixed mechanism, not a hyperdistribution.
- Registered target is the cumulative path-specific effect cPSE_M2 = theta_011 - theta_001 that the source analyses in Section 5. The source reports no numerical value for it (its Figure 3 only re-centres estimators at the truth); the value 0.3264 registered here is derived analytically by the collector from the registered coefficients and must be checked by a reviewer.
- The source generates 1000 Monte Carlo samples of size 2000 and compares eight estimators under five misspecification cases; none of that estimation work is reproduced. The 'false covariates' Z = (X1, exp(X2/2), (X3/X1)^(1/3), X4/(exp(X1/2)+1)) used there are an estimation device applied to the same data, not a different data-generating mechanism, so they are not registered as a separate DGP.
- Sampling is re-implemented with NumPy Generator(PCG64); no attempt is made to match the source software draw-for-draw.
- Only the eight observed columns are exported. The latent errors U1,U2,U3 and the latent X-Y confounder UXY are generated internally and never returned.

**Warnings:**

- Nothing automatically flagged; this does NOT equal scientific acceptance.
