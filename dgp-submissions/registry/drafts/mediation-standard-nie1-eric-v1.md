# Standard NIE1 adaptation: eric

> **Unverified extraction — scientific review required.**

**Primary area:** Mediation — Direct and Indirect Effects

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Tchetgen Tchetgen, E. J. and Shpitser, I. (2012). Semiparametric theory for causal mediation analysis: efficiency bounds, multiple robustness and sensitivity analysis. The Annals of Statistics 40(3), 1816–1845. DOI: 10.1214/12-AOS990.

**DOI:** — · **Source locator:** Section 3, electronic-reprint PDF page 13: Model.X, Model.E, Model.M, Model.Y. NIE definition: equation (1), PDF page 2.; adaptation: bundled SCIENTIFIC_SPEC.md and nie_standard_v1/generators.py::_draw

## DGP / generation mechanism

**Sampling design:** IID observations at a fixed structural configuration; separate mechanism and observation seeds.

**Generator source:** [generator.py](../generators/mediation-standard-nie1-eric-v1.py)

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

<pre>x=np.empty((n,3))
x[:,0]=r.binomial(1,c[&quot;x1_probability&quot;],n)
x[:,1]=r.binomial(1,c[&quot;x2_coefficients&quot;][0]+c[&quot;x2_coefficients&quot;][1]*x[:,0])
xc=c[&quot;x3_coefficients&quot;]
x[:,2]=xc[0]+xc[1]*x[:,0]+xc[2]*x[:,1]+c[&quot;x3_sd&quot;]*r.standard_normal(n)
f=np.column_stack([np.ones(n),x,x[:,0]*x[:,2]])
a=r.binomial(1,expit(f@c[&quot;treatment_coefficients&quot;]))
m=r.binomial(1,expit(f@c[&quot;mediator_coefficients&quot;]+c[&quot;mediator_treatment_coefficient&quot;]*a))[:,None]
y=np.column_stack([np.ones(n),x,a,m[:,0],a*m[:,0]])@c[&quot;outcome_coefficients&quot;]+c[&quot;outcome_noise_sd&quot;]*r.standard_normal(n)
return x,a,m,y,[&quot;binary&quot;],[&quot;binary&quot;,&quot;binary&quot;,&quot;continuous&quot;],&quot;continuous&quot;</pre>

<details>
<summary>Original source equations (verbatim)</summary>

<pre>
NIE1 = E[Y(1,M(1))-Y(1,M(0))]
x=np.empty((n,3))
x[:,0]=r.binomial(1,c[&quot;x1_probability&quot;],n)
x[:,1]=r.binomial(1,c[&quot;x2_coefficients&quot;][0]+c[&quot;x2_coefficients&quot;][1]*x[:,0])
xc=c[&quot;x3_coefficients&quot;]
x[:,2]=xc[0]+xc[1]*x[:,0]+xc[2]*x[:,1]+c[&quot;x3_sd&quot;]*r.standard_normal(n)
f=np.column_stack([np.ones(n),x,x[:,0]*x[:,2]])
a=r.binomial(1,expit(f@c[&quot;treatment_coefficients&quot;]))
m=r.binomial(1,expit(f@c[&quot;mediator_coefficients&quot;]+c[&quot;mediator_treatment_coefficient&quot;]*a))[:,None]
y=np.column_stack([np.ones(n),x,a,m[:,0],a*m[:,0]])@c[&quot;outcome_coefficients&quot;]+c[&quot;outcome_noise_sd&quot;]*r.standard_normal(n)
return x,a,m,y,[&quot;binary&quot;],[&quot;binary&quot;,&quot;binary&quot;,&quot;continuous&quot;],&quot;continuous&quot;
</pre>

</details>


## Parameter scenarios, estimands and truth

| Scenario | Estimand | Definition | Reported value | Evidence status |
|---|---|---|---|---|
| native | NIE | NIE = E[Y(1,M(1))-Y(1,M(0))] in the adapted fixed-SEM superpopulation, jointly intervening on the complete mediator vector. | 0.23661990123343668 | reported_numeric |

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

- Retain the scalar discrete-mediator SEM and superpopulation target; do not replace population X integration by the realized empirical-X average.
- New complete-data superpopulation NIE1 target; original records/estimands are retained separately.
- Standalone canonical generator core SHA256 443e04663970594a8ec2932dc0ee9718c10cc501314d133686dfd0e9acf1baa8

**Warnings:**

- Nothing automatically flagged; this does NOT equal scientific acceptance.
