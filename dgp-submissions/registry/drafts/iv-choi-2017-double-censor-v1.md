# IV: left-censored continuous exposure and right-censored outcome

> **Unverified extraction — scientific review required.**

**Primary area:** IV — Instrumental Variables

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Choi, B. Y., Fine, J. P., and Brookhart, M. A. (2017). On two-stage estimation of structural instrumental variable models. Biometrika 104(4), 881-899. DOI 10.1093/biomet/asx056.

**DOI:** — · **Source locator:** PMC author manuscript Section 4 Case 1B, equations (12)-(13) (Equation35.gif/Equation36.gif) and simulation parameter/censoring paragraph; Section 3.2 observed outcome min/event indicator, Section 3.3 left censoring sign reversal. Original equation GIFs visually read and saved in local source audit. No author software used; commit not applicable.

## DGP / generation mechanism

**Sampling design:** Unit: individual; Dependence: iid individuals; two independent truncated-normal instruments, two independent measured confounders and latent U. Shared U induces D,Y dependence; independent censoring thresholds.

**Generator source:** [generator.py](../generators/iv-choi-2017-double-censor-v1.py)

**Keywords (source-described):** Nonlinearity

**Observed variables**

V1, V2, W1, W2, D_observed, D_exact, Y_observed, Y_event

**Latent variables**

U, delta, C_Y, C_D

**Latent-variable identification:** candidates from equations need review

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

$$
V_{1},V_{2},W_{1},W_{2},U\overset{\mathrm{iid}}{\sim} \mathcal{N}(0,1) conditional on [-2,2]
$$

$$
\varepsilon,\delta\overset{\mathrm{iid}}{\sim} \mathcal{N}(0,1), independent of all covariates.
$$

$$
D=1+V_{1}+V_{2}+W_{1}+W_{2}+U+\delta
$$

$$
Y=1+D+W_{1}+W_{2}+U+\varepsilon
$$

all source Eq12/13 parameters1.

$$
C_Y\sim \mathrm{Uniform}(0,13.249945942133955)
$$

$$
C_D\sim \mathrm{Uniform}(-7,2.629814945797971)
$$



independent of all other variables and each other. Endpoints numerically calibrated to20% population censoring as an explicit adaptation

$$
D_observed=\max(D,C_D)
$$

$$
D_exact=I(D>=C_D)
$$

$$
Y_observed=\min(Y,C_Y)
$$

$$
Y_event=I(Y<=C_Y). Return V_{1},V_{2},W_{1},W_{2},D_observed,D_exact,Y_observed,Y_event only.
$$

<details>
<summary>Original source equations (verbatim)</summary>

<pre>
V1,V2,W1,W2,U iid N(0,1) conditional on [-2,2]; epsilon,delta iid N(0,1), independent of all covariates.
D=1+V1+V2+W1+W2+U+delta; Y=1+D+W1+W2+U+epsilon; all source Eq12/13 parameters1.
C_Y~Uniform(0,13.249945942133955); C_D~Uniform(-7,2.629814945797971); independent of all other variables and each other. Endpoints numerically calibrated to20% population censoring as an explicit adaptation.
D_observed=max(D,C_D); D_exact=I(D&gt;=C_D); Y_observed=min(Y,C_Y); Y_event=I(Y&lt;=C_Y). Return V1,V2,W1,W2,D_observed,D_exact,Y_observed,Y_event only.
</pre>

</details>


## Parameter scenarios, estimands and truth

| Scenario | Estimand | Definition | True value | Evidence status |
|---|---|---|---|---|
| source_case1b_calibrated | alpha_YZ | Structural coefficient1 of the true, possibly unobserved continuous exposure D in Y(d)=1+d+W1+W2+U+epsilon. Thus E[Y(d+1)-Y(d)]=1 on source linear/log-time outcome scale, not effect on exp(Y) survival time or complier LATE. | 1.0 | reported_numeric |

## Identifiability assumptions

- iid individuals, consistency, no interference
- Independent instruments V1,V2, measured W1,W2 and latent U; instruments affect Y only through D
- Nonzero instrument relevance: both exposure coefficients1
- Independent normal structural innovations; unobserved U creates exposure/outcome confounding
- Censoring thresholds independently generated from uniforms; proper left-exposure and right-outcome indicators retained
- Uniform censoring support and AFT/rank identification require scientific review; machine checks establish generation/truth, not general missing-data identification

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Warnings:**

- Latent-variable candidates inferred from source equations; confirm their roles and completeness against the original paper or generator.
