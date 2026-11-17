# Standard NIE1 adaptation: jones lnl

> **Unverified extraction — scientific review required.**

**Primary area:** Mediation — Direct and Indirect Effects

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Jones, J., Ertefaie, A. and Strawderman, R. L. (2025). Causal mediation analysis: selection with asymptotically valid inference. Journal of the Royal Statistical Society Series B: Statistical Methodology 87(3), 678-700. DOI: 10.1093/jrsssb/qkae109.

**DOI:** 10.1093/jrsssb/qkae109 · **Source locator:** Section 5 'Simulation Studies', arXiv:2110.06127v2 PDF page 15 (the two forms of mu_D0, psi_M and psi_Y, and the three-letter scenario naming; this contribution registers LNL), and Appendix A 'Simulation Results', PDF page 26 (all variances, dimensions and the structural parameters alpha_0, beta_0, gamma_0, and the statement NIE = 2.4). Structural model (1) is on PDF page 4; Proposition 2.1 giving NDE = gamma_0 and NIE = alpha_0 . beta_0 is on PDF page 6.; adaptation: bundled SCIENTIFIC_SPEC.md and nie_standard_v1/generators.py::_draw

## DGP / generation mechanism

**Sampling design:** IID observations at a fixed structural configuration; separate mechanism and observation seeds.

**Generator source:** [generator.py](../generators/mediation-standard-nie1-jones-lnl-v1.py)

**Keywords (source-described):** Not specified

**Observed variables**

X1, X2, X3, A, M1–M10 (10 variables), Y

<details>
<summary>All observed variable names</summary>

X1, X2, X3, A, M1, M2, M3, M4, M5, M6, M7, M8, M9, M10, Y

</details>

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

<pre>x=np.sqrt(c[&quot;covariate_variance&quot;])*r.standard_normal((n,3))
q=c[&quot;mediator_count&quot;]
pa=expit(c[&quot;propensity_scale&quot;]*((x[:,0]+x[:,1]) if c[&quot;propensity_form&quot;]==&quot;linear&quot; else (x[:,0]*x[:,1]+x[:,1])))
a=r.binomial(1,pa)
xm=(x[:,0] if c[&quot;mediator_confounding_form&quot;]==&quot;linear&quot; else x[:,0]**2)+x[:,1]-x[:,2]
xy=2*((x[:,0]-.5) if c[&quot;outcome_confounding_form&quot;]==&quot;linear&quot; else (x[:,0]-.5)**2)+x[:,1]+2*x[:,2]
m=a[:,None]*np.asarray(c[&quot;alpha0&quot;])+xm[:,None]+c[&quot;mediator_noise_sd&quot;]*r.standard_normal((n,q))
y=c[&quot;gamma0&quot;]*a+m@c[&quot;beta0&quot;]+xy+c[&quot;outcome_noise_sd&quot;]*r.standard_normal(n)
return x,a,m,y,[&quot;continuous&quot;]*q,[&quot;continuous&quot;]*3,&quot;continuous&quot;</pre>

<details>
<summary>Original source equations (verbatim)</summary>

<pre>
NIE1 = E[Y(1,M(1))-Y(1,M(0))]
x=np.sqrt(c[&quot;covariate_variance&quot;])*r.standard_normal((n,3))
q=c[&quot;mediator_count&quot;]
pa=expit(c[&quot;propensity_scale&quot;]*((x[:,0]+x[:,1]) if c[&quot;propensity_form&quot;]==&quot;linear&quot; else (x[:,0]*x[:,1]+x[:,1])))
a=r.binomial(1,pa)
xm=(x[:,0] if c[&quot;mediator_confounding_form&quot;]==&quot;linear&quot; else x[:,0]**2)+x[:,1]-x[:,2]
xy=2*((x[:,0]-.5) if c[&quot;outcome_confounding_form&quot;]==&quot;linear&quot; else (x[:,0]-.5)**2)+x[:,1]+2*x[:,2]
m=a[:,None]*np.asarray(c[&quot;alpha0&quot;])+xm[:,None]+c[&quot;mediator_noise_sd&quot;]*r.standard_normal((n,q))
y=c[&quot;gamma0&quot;]*a+m@c[&quot;beta0&quot;]+xy+c[&quot;outcome_noise_sd&quot;]*r.standard_normal(n)
return x,a,m,y,[&quot;continuous&quot;]*q,[&quot;continuous&quot;]*3,&quot;continuous&quot;
</pre>

</details>


## Parameter scenarios, estimands and truth

| Scenario | Estimand | Definition | Reported value |
|---|---|---|---|
| native | NIE | NIE = E[Y(1,M(1))-Y(1,M(0))] in the adapted fixed-SEM superpopulation, jointly intervening on the complete mediator vector. | 2.4000000000000004 |

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

- Retain LNL propensity/mediator-confounding/outcome-confounding forms, vector mediators and active paths.
- New complete-data superpopulation NIE1 target; original records/estimands are retained separately.
- Standalone canonical generator core SHA256 443e04663970594a8ec2932dc0ee9718c10cc501314d133686dfd0e9acf1baa8

**Warnings:**

- Nothing automatically flagged; this does NOT equal scientific acceptance.
