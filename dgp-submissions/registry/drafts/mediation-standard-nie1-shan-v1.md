# Standard NIE1 adaptation: shan

> **Unverified extraction — scientific review required.**

**Primary area:** Mediation — Direct and Indirect Effects

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Shan, J., Li, W. and Ai, C. (2026). Efficient Nonparametric Inference for Mediation Analysis with Nonignorable Missing Confounders. Journal of the American Statistical Association, published online 25 June 2026, pages 1-12. DOI: 10.1080/01621459.2026.2654218.

**DOI:** 10.1080/01621459.2026.2654218 · **Source locator:** Section 5 'Numerical studies', the displayed data-generating process and the DGP1 branch; arXiv:2402.05384 PDF page 14. Estimand definitions: Section 2.1, PDF page 4 (NIE xi(t), NDE zeta(t), ATE tau) and the mediation functional theta = E[Y(1, M(0))] with its identification formula (1) on PDF page 5. Figure 2 and its printed axis ranges: PDF page 15. Reported missingness split of about 58/14/14/14 per cent: PDF page 14. Page numbers are preprint PDF pages; the article is online first and carries no journal page numbers beyond 1-12.; adaptation: bundled SCIENTIFIC_SPEC.md and nie_standard_v1/generators.py::_draw

## DGP / generation mechanism

**Sampling design:** IID observations at a fixed structural configuration; separate mechanism and observation seeds.

**Generator source:** [generator.py](https://github.com/Statsinference/stats-inference-arena/blob/main/dgp-submissions/registry/generators/mediation-standard-nie1-shan-v1.py)

**Keywords (source-described):** Not specified

**Observed variables**

X1, X2, X3, A, M1, Y

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

<pre>x=np.column_stack([r.random((n,2)),r.binomial(1,c[&quot;x3_probability&quot;],n)])
a=r.binomial(1,expit(c[&quot;propensity_intercept&quot;]+c[&quot;propensity_x1_squared&quot;]*x[:,0]**2+c[&quot;propensity_x2&quot;]*x[:,1]+c[&quot;propensity_x3&quot;]*x[:,2]))
m=(c[&quot;mediator_intercept&quot;]+c[&quot;mediator_treatment&quot;]*a+c[&quot;mediator_treatment_x1_squared&quot;]*a*x[:,0]**2+c[&quot;mediator_x1_squared&quot;]*x[:,0]**2+c[&quot;mediator_sin_x2&quot;]*np.sin(x[:,1])+c[&quot;mediator_x3&quot;]*x[:,2]+c[&quot;mediator_noise_sd&quot;]*r.standard_normal(n))[:,None]
y=c[&quot;outcome_intercept&quot;]+c[&quot;outcome_treatment&quot;]*a+(c[&quot;outcome_mediator&quot;]+c[&quot;outcome_treatment_mediator&quot;]*a)*m[:,0]+c[&quot;outcome_treatment_x1&quot;]*a*x[:,0]+c[&quot;outcome_sin_x1&quot;]*np.sin(x[:,0])+c[&quot;outcome_x2_squared&quot;]*x[:,1]**2+c[&quot;outcome_x3&quot;]*x[:,2]+c[&quot;outcome_noise_sd&quot;]*r.standard_normal(n)
return x,a,m,y,[&quot;continuous&quot;],[&quot;continuous&quot;,&quot;continuous&quot;,&quot;binary&quot;],&quot;continuous&quot;</pre>

<details>
<summary>Original source equations (verbatim)</summary>

<pre>
NIE1 = E[Y(1,M(1))-Y(1,M(0))]
x=np.column_stack([r.random((n,2)),r.binomial(1,c[&quot;x3_probability&quot;],n)])
a=r.binomial(1,expit(c[&quot;propensity_intercept&quot;]+c[&quot;propensity_x1_squared&quot;]*x[:,0]**2+c[&quot;propensity_x2&quot;]*x[:,1]+c[&quot;propensity_x3&quot;]*x[:,2]))
m=(c[&quot;mediator_intercept&quot;]+c[&quot;mediator_treatment&quot;]*a+c[&quot;mediator_treatment_x1_squared&quot;]*a*x[:,0]**2+c[&quot;mediator_x1_squared&quot;]*x[:,0]**2+c[&quot;mediator_sin_x2&quot;]*np.sin(x[:,1])+c[&quot;mediator_x3&quot;]*x[:,2]+c[&quot;mediator_noise_sd&quot;]*r.standard_normal(n))[:,None]
y=c[&quot;outcome_intercept&quot;]+c[&quot;outcome_treatment&quot;]*a+(c[&quot;outcome_mediator&quot;]+c[&quot;outcome_treatment_mediator&quot;]*a)*m[:,0]+c[&quot;outcome_treatment_x1&quot;]*a*x[:,0]+c[&quot;outcome_sin_x1&quot;]*np.sin(x[:,0])+c[&quot;outcome_x2_squared&quot;]*x[:,1]**2+c[&quot;outcome_x3&quot;]*x[:,2]+c[&quot;outcome_noise_sd&quot;]*r.standard_normal(n)
return x,a,m,y,[&quot;continuous&quot;],[&quot;continuous&quot;,&quot;continuous&quot;,&quot;binary&quot;],&quot;continuous&quot;
</pre>

</details>


## Parameter scenarios, estimands and truth

| Scenario | Estimand | Definition | Reported value | Evidence status |
|---|---|---|---|---|
| native | NIE | NIE = E[Y(1,M(1))-Y(1,M(0))] in the adapted fixed-SEM superpopulation, jointly intervening on the complete mediator vector. | 1 | reported_numeric |

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
