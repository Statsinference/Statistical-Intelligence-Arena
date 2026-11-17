# Standard NIE1 adaptation: he song xu

> **Unverified extraction — scientific review required.**

**Primary area:** Mediation — Direct and Indirect Effects

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** He, Y., Song, P. X.-K. and Xu, G. (2024). Adaptive Bootstrap Tests for Composite Null Hypotheses in the Mediation Pathway Analysis. Journal of the Royal Statistical Society: Series B 86(2), 411–434. DOI: 10.1093/jrsssb/qkad129.

**DOI:** 10.1093/jrsssb/qkad129 · **Source locator:** Journal §4 Numerical Experiments, equation (11), fixed null scenarios (12), §4.2 fixed-product 0.04 alternative; arXiv:2310.11630v1 PDF pp.10–12 (zero-index 9–11). NIE definition equation (1), preprint PDF p.4.; adaptation: bundled SCIENTIFIC_SPEC.md and nie_standard_v1/generators.py::_draw

## DGP / generation mechanism

**Sampling design:** IID observations at a fixed structural configuration; separate mechanism and observation seeds.

**Generator source:** [generator.py](https://github.com/Statsinference/stats-inference-arena/blob/main/dgp-submissions/registry/generators/mediation-standard-nie1-he-song-xu-v1.py)

**Keywords (source-described):** Not specified

**Observed variables**

X1, X2, A, M1, Y

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

<pre>x=np.column_stack([c[&quot;x1_sd&quot;]*r.standard_normal(n),r.binomial(1,c[&quot;x2_probability&quot;],n)])
a=r.binomial(1,c[&quot;treatment_probability&quot;],n)
m=(c[&quot;mediator_intercept&quot;]+c[&quot;alpha_s&quot;]*a+c[&quot;mediator_x1&quot;]*x[:,0]+c[&quot;mediator_x2&quot;]*x[:,1]+c[&quot;mediator_noise_sd&quot;]*r.standard_normal(n))[:,None]
y=c[&quot;outcome_intercept&quot;]+c[&quot;beta_m&quot;]*m[:,0]+c[&quot;outcome_direct&quot;]*a+c[&quot;outcome_x1&quot;]*x[:,0]+c[&quot;outcome_x2&quot;]*x[:,1]+c[&quot;outcome_noise_sd&quot;]*r.standard_normal(n)
return x,a,m,y,[&quot;continuous&quot;],[&quot;continuous&quot;,&quot;binary&quot;],&quot;continuous&quot;</pre>

<details>
<summary>Original source equations (verbatim)</summary>

<pre>
NIE1 = E[Y(1,M(1))-Y(1,M(0))]
x=np.column_stack([c[&quot;x1_sd&quot;]*r.standard_normal(n),r.binomial(1,c[&quot;x2_probability&quot;],n)])
a=r.binomial(1,c[&quot;treatment_probability&quot;],n)
m=(c[&quot;mediator_intercept&quot;]+c[&quot;alpha_s&quot;]*a+c[&quot;mediator_x1&quot;]*x[:,0]+c[&quot;mediator_x2&quot;]*x[:,1]+c[&quot;mediator_noise_sd&quot;]*r.standard_normal(n))[:,None]
y=c[&quot;outcome_intercept&quot;]+c[&quot;beta_m&quot;]*m[:,0]+c[&quot;outcome_direct&quot;]*a+c[&quot;outcome_x1&quot;]*x[:,0]+c[&quot;outcome_x2&quot;]*x[:,1]+c[&quot;outcome_noise_sd&quot;]*r.standard_normal(n)
return x,a,m,y,[&quot;continuous&quot;],[&quot;continuous&quot;,&quot;binary&quot;],&quot;continuous&quot;
</pre>

</details>


## Parameter scenarios, estimands and truth

| Scenario | Estimand | Definition | Reported value | Evidence status |
|---|---|---|---|---|
| native | NIE | NIE = E[Y(1,M(1))-Y(1,M(0))] in the adapted fixed-SEM superpopulation, jointly intervening on the complete mediator vector. | 0.04000000000000001 | reported_numeric |

## Identifiability assumptions

- Independent exogenous structural errors and iid units conditional on fixed configuration.
- No treatment-induced mediator-outcome confounder remains in the adapted SEM.
- Causal identification additionally requires consistency, exchangeability/cross-world conditions and treatment/mediator support; treatment randomization alone is insufficient.

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Warnings:**

- Nothing automatically flagged; this does NOT equal scientific acceptance.
