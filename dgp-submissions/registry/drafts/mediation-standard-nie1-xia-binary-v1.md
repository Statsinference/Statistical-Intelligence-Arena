# Standard NIE1 adaptation: xia binary

> **Unverified extraction — scientific review required.**

**Primary area:** Mediation — Direct and Indirect Effects

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Xia, F. and Chan, K. C. G. (2023). Identification, Semiparametric Efficiency, and Quadruply Robust Estimation in Mediation Analysis with Treatment-Induced Confounding. Journal of the American Statistical Association 118(542), 1272–1281. DOI: 10.1080/01621459.2021.1990765.

**DOI:** 10.1080/01621459.2021.1990765 · **Source locator:** Author accepted manuscript §4.1, “Binary C and M”, PDF p.17; https://par.nsf.gov/servlets/purl/10300663.; adaptation: bundled SCIENTIFIC_SPEC.md and nie_standard_v1/generators.py::_draw

## DGP / generation mechanism

**Sampling design:** IID observations at a fixed structural configuration; separate mechanism and observation seeds.

**Generator source:** [generator.py](../generators/mediation-standard-nie1-xia-binary-v1.py)

**Keywords (source-described):** Not specified

**Observed variables**

X1, A, M1, Y

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

<pre>x=c[&quot;x_sd&quot;]*r.standard_normal((n,1))
a=r.binomial(1,expit(c[&quot;a_logit_intercept&quot;]+c[&quot;a_logit_x&quot;]*x[:,0]))
if s==&quot;xia_binary&quot;: m=r.binomial(1,expit(c[&quot;m_logit_intercept&quot;]+c[&quot;m_logit_a&quot;]*a+c[&quot;m_logit_x&quot;]*x[:,0]))[:,None]
        else: m=(c[&quot;m_intercept&quot;]+c[&quot;m_a&quot;]*a+c[&quot;m_x&quot;]*x[:,0]+c[&quot;m_sd&quot;]*r.standard_normal(n))[:,None]
y=c[&quot;y_intercept&quot;]+c[&quot;y_a&quot;]*a+(c[&quot;y_m&quot;]+c[&quot;y_am&quot;]*a)*m[:,0]+c[&quot;y_x&quot;]*x[:,0]+c[&quot;y_sd&quot;]*r.standard_normal(n)
return x,a,m,y,[&quot;binary&quot; if s==&quot;xia_binary&quot; else &quot;continuous&quot;],[&quot;continuous&quot;],&quot;continuous&quot;</pre>

<details>
<summary>Original source equations (verbatim)</summary>

<pre>
NIE1 = E[Y(1,M(1))-Y(1,M(0))]
x=c[&quot;x_sd&quot;]*r.standard_normal((n,1))
a=r.binomial(1,expit(c[&quot;a_logit_intercept&quot;]+c[&quot;a_logit_x&quot;]*x[:,0]))
if s==&quot;xia_binary&quot;: m=r.binomial(1,expit(c[&quot;m_logit_intercept&quot;]+c[&quot;m_logit_a&quot;]*a+c[&quot;m_logit_x&quot;]*x[:,0]))[:,None]
        else: m=(c[&quot;m_intercept&quot;]+c[&quot;m_a&quot;]*a+c[&quot;m_x&quot;]*x[:,0]+c[&quot;m_sd&quot;]*r.standard_normal(n))[:,None]
y=c[&quot;y_intercept&quot;]+c[&quot;y_a&quot;]*a+(c[&quot;y_m&quot;]+c[&quot;y_am&quot;]*a)*m[:,0]+c[&quot;y_x&quot;]*x[:,0]+c[&quot;y_sd&quot;]*r.standard_normal(n)
return x,a,m,y,[&quot;binary&quot; if s==&quot;xia_binary&quot; else &quot;continuous&quot;],[&quot;continuous&quot;],&quot;continuous&quot;
</pre>

</details>


## Parameter scenarios, estimands and truth

| Scenario | Estimand | Definition | True value | Evidence status |
|---|---|---|---|---|
| native | NIE | NIE = E[Y(1,M(1))-Y(1,M(0))] in the adapted fixed-SEM superpopulation, jointly intervening on the complete mediator vector. | -0.36488213957756865 | reported_numeric |

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
