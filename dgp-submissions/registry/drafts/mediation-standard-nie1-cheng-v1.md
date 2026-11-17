# Standard NIE1 adaptation: cheng

> **Unverified extraction — scientific review required.**

**Primary area:** Mediation — Direct and Indirect Effects

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Cheng, C. and Li, F. (2025). Identification and multiply robust estimation in causal mediation analysis across principal strata. Journal of the Royal Statistical Society Series B: Statistical Methodology 88(1), 1-22. DOI: 10.1093/jrsssb/qkaf037.

**DOI:** 10.1093/jrsssb/qkaf037 · **Source locator:** Section 5 'A simulation study', arXiv:2304.10025v4 PDF page 23: the displayed data-generating process for (X, Z, D, M, Y). ITT-NIE and ITT-NDE are defined on PDF page 23 just above that display (ratio scale shown there; the paper states it primarily works on the mean-difference scale).; adaptation: bundled SCIENTIFIC_SPEC.md and nie_standard_v1/generators.py::_draw

## DGP / generation mechanism

**Sampling design:** IID observations at a fixed structural configuration; separate mechanism and observation seeds.

**Generator source:** [generator.py](../generators/mediation-standard-nie1-cheng-v1.py)

**Keywords (source-described):** Not specified

**Observed variables**

X1–X4 (4 variables), A, M1, Y

<details>
<summary>All observed variable names</summary>

X1, X2, X3, X4, A, M1, Y

</details>

**Latent variables**

Not explicitly identified (review required)

**Latent-variable identification:** explicit structured metadata

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

**target**

$$
\psi=\mathbb{E}[Y(1,M(1))-Y(1,M(0))]
$$

**adapted structural equations**

Source notation retained without guessing:

<pre>x = c[&quot;covariate_sd&quot;]*r.standard_normal((n, 4))
a = r.binomial(1, expit(x@c[&quot;treatment_coefficients&quot;]))
m = r.binomial(1, expit(c[&quot;mediator_intercept&quot;]+c[&quot;mediator_treatment_coefficient&quot;]*a+x@c[&quot;mediator_coefficients&quot;]))[:, None]
y = c[&quot;outcome_intercept&quot;]+c[&quot;outcome_treatment_coefficient&quot;]*a+c[&quot;outcome_mediator_coefficient&quot;]*m[:, 0]+x@c[&quot;outcome_coefficients&quot;]+c[&quot;outcome_noise_sd&quot;]*r.standard_normal(n)
return x,a,m,y,[&quot;binary&quot;],[&quot;continuous&quot;]*4,&quot;continuous&quot;</pre>

<details>
<summary>Original source equations (verbatim)</summary>

<pre>
NIE1 = E[Y(1,M(1))-Y(1,M(0))]
x = c[&quot;covariate_sd&quot;]*r.standard_normal((n, 4))
a = r.binomial(1, expit(x@c[&quot;treatment_coefficients&quot;]))
m = r.binomial(1, expit(c[&quot;mediator_intercept&quot;]+c[&quot;mediator_treatment_coefficient&quot;]*a+x@c[&quot;mediator_coefficients&quot;]))[:, None]
y = c[&quot;outcome_intercept&quot;]+c[&quot;outcome_treatment_coefficient&quot;]*a+c[&quot;outcome_mediator_coefficient&quot;]*m[:, 0]+x@c[&quot;outcome_coefficients&quot;]+c[&quot;outcome_noise_sd&quot;]*r.standard_normal(n)
return x,a,m,y,[&quot;binary&quot;],[&quot;continuous&quot;]*4,&quot;continuous&quot;
</pre>

</details>


## Parameter scenarios, estimands and truth

| Scenario | Estimand | Definition | Reported value | Evidence status |
|---|---|---|---|---|
| native | NIE | NIE = E[Y(1,M(1))-Y(1,M(0))] in the adapted fixed-SEM superpopulation, jointly intervening on the complete mediator vector. | 0.30114731040193965 | reported_numeric |

**Original submitted target notation:** NIE


## Identifiability assumptions

- Independent exogenous structural errors and iid units conditional on fixed configuration.
- No treatment-induced mediator-outcome confounder remains in the adapted SEM.
- Causal identification additionally requires consistency, exchangeability/cross-world conditions and treatment/mediator support; treatment randomization alone is insufficient.

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Adaptations from the source (submitted, unverified):**

- Set mediator_event_coefficient and outcome_event_coefficient to zero and remove D structurally; map source Z to A. The former principal-stratum/direct-effect target is not reused.
- New complete-data superpopulation NIE1 target; original records/estimands are retained separately.
- Standalone canonical generator core SHA256 443e04663970594a8ec2932dc0ee9718c10cc501314d133686dfd0e9acf1baa8

**Warnings:**

- Nothing automatically flagged; this does NOT equal scientific acceptance.
