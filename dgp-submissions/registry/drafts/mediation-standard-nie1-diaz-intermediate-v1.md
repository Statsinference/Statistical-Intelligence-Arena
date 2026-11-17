# Standard NIE1 adaptation: diaz intermediate

> **Unverified extraction — scientific review required.**

**Primary area:** Mediation — Direct and Indirect Effects

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Díaz, I., Hejazi, N. S., Rudolph, K. E. and van der Laan, M. J. (2021). Non-parametric efficient causal mediation with intermediate confounders. Biometrika 108(3), 627–641. DOI: 10.1093/biomet/asaa085.

**DOI:** 10.1093/biomet/asaa085 · **Source locator:** Section 5 Numerical studies, displayed seven-equation DGP; checked against arXiv:1912.09936v2 PDF p.12 (zero-index p.11), lines 693–706. Interventional effect definition Eq. (2), PDF p.5 (zero-index p.4), and identification Eq. (3), PDF p.6.; adaptation: bundled SCIENTIFIC_SPEC.md and nie_standard_v1/generators.py::_draw

## DGP / generation mechanism

**Sampling design:** IID observations at a fixed structural configuration; separate mechanism and observation seeds.

**Generator source:** [generator.py](../generators/mediation-standard-nie1-diaz-intermediate-v1.py)

**Keywords (source-described):** Not specified

**Observed variables**

X1, X2, X3, A, M1, Y

**Latent variables**

Not explicitly identified (review required)

**Latent-variable identification:** explicit structured metadata

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

**target**

```math
\psi=\mathbb{E}[Y(1,M(1))-Y(1,M(0))]
```

**adapted structural equations**

Source notation retained without guessing:

<pre>if s == &quot;diaz_hejazi&quot;:
            x = r.binomial(1, c[&quot;baseline_probabilities&quot;], (n,3))
            a = r.binomial(1, x.sum(1)/c[&quot;treatment_denominator&quot;]+c[&quot;treatment_intercept&quot;])
            m = r.binomial(1, _dh_probs(c[&quot;mediation_path_scale&quot;]*a, x))
            y = m@c[&quot;outcome_mediator_coefficients&quot;]+c[&quot;outcome_treatment_coefficient&quot;]*a+c[&quot;outcome_baseline_quadratic_coefficient&quot;]*x.sum(1)**2+c[&quot;outcome_noise_sd&quot;]*r.standard_normal(n)
            return x,a,m,y,[&quot;binary&quot;]*3,[&quot;binary&quot;]*3,&quot;continuous&quot;
x = np.empty((n,3))
x[:,0]=r.binomial(1,c[&quot;p_w1&quot;],n)
x[:,1]=r.binomial(1,c[&quot;p_w2&quot;],n)
x[:,2]=r.binomial(1,c[&quot;p_w3_intercept&quot;]+c[&quot;p_w3_slope&quot;]*(x[:,0]+x[:,1]))
a=r.binomial(1,expit(c[&quot;treatment_intercept&quot;]+c[&quot;treatment_w_sum&quot;]*x.sum(1)+c[&quot;treatment_w1w2&quot;]*x[:,0]*x[:,1]))
m=r.binomial(1,expit(c[&quot;m_w1&quot;]*x[:,0]+c[&quot;m_w2&quot;]*x[:,1]+c[&quot;m_a&quot;]*a+c[&quot;m_aw2&quot;]*a*x[:,1]))[:,None]
y=r.binomial(1,expit((c[&quot;y_a&quot;]*a+c[&quot;y_m&quot;]*m[:,0])/(x.sum(1)+c[&quot;y_denominator_intercept&quot;])))
return x,a,m,y,[&quot;binary&quot;],[&quot;binary&quot;]*3,&quot;binary&quot;</pre>

<details>
<summary>Original source equations (verbatim)</summary>

<pre>
NIE1 = E[Y(1,M(1))-Y(1,M(0))]
if s == &quot;diaz_hejazi&quot;:
            x = r.binomial(1, c[&quot;baseline_probabilities&quot;], (n,3))
            a = r.binomial(1, x.sum(1)/c[&quot;treatment_denominator&quot;]+c[&quot;treatment_intercept&quot;])
            m = r.binomial(1, _dh_probs(c[&quot;mediation_path_scale&quot;]*a, x))
            y = m@c[&quot;outcome_mediator_coefficients&quot;]+c[&quot;outcome_treatment_coefficient&quot;]*a+c[&quot;outcome_baseline_quadratic_coefficient&quot;]*x.sum(1)**2+c[&quot;outcome_noise_sd&quot;]*r.standard_normal(n)
            return x,a,m,y,[&quot;binary&quot;]*3,[&quot;binary&quot;]*3,&quot;continuous&quot;
x = np.empty((n,3))
x[:,0]=r.binomial(1,c[&quot;p_w1&quot;],n)
x[:,1]=r.binomial(1,c[&quot;p_w2&quot;],n)
x[:,2]=r.binomial(1,c[&quot;p_w3_intercept&quot;]+c[&quot;p_w3_slope&quot;]*(x[:,0]+x[:,1]))
a=r.binomial(1,expit(c[&quot;treatment_intercept&quot;]+c[&quot;treatment_w_sum&quot;]*x.sum(1)+c[&quot;treatment_w1w2&quot;]*x[:,0]*x[:,1]))
m=r.binomial(1,expit(c[&quot;m_w1&quot;]*x[:,0]+c[&quot;m_w2&quot;]*x[:,1]+c[&quot;m_a&quot;]*a+c[&quot;m_aw2&quot;]*a*x[:,1]))[:,None]
y=r.binomial(1,expit((c[&quot;y_a&quot;]*a+c[&quot;y_m&quot;]*m[:,0])/(x.sum(1)+c[&quot;y_denominator_intercept&quot;])))
return x,a,m,y,[&quot;binary&quot;],[&quot;binary&quot;]*3,&quot;binary&quot;
</pre>

</details>


## Parameter scenarios, estimands and truth

| Scenario | Estimand | Definition | Reported value |
|---|---|---|---|
| native | NIE | NIE = E[Y(1,M(1))-Y(1,M(0))] in the adapted fixed-SEM superpopulation, jointly intervening on the complete mediator vector. | 0.01686828165920525 |

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

- Remove Z structurally: set m_z, m_az, y_z and y_az to zero. Recompute natural NIE1, replacing the source interventional indirect-effect target.
- New complete-data superpopulation NIE1 target; original records/estimands are retained separately.
- Standalone canonical generator core SHA256 443e04663970594a8ec2932dc0ee9718c10cc501314d133686dfd0e9acf1baa8

**Warnings:**

- Nothing automatically flagged; this does NOT equal scientific acceptance.
