# Standard NIE1 adaptation: miles

> **Unverified extraction — scientific review required.**

**Primary area:** Mediation — Direct and Indirect Effects

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Miles, C. H., Shpitser, I., Kanki, P., Meloni, S. and Tchetgen Tchetgen, E. J. (2019). On semiparametric estimation of a path-specific effect in the presence of mediator-outcome confounding. Biometrika 107(1), 159-172. DOI: 10.1093/biomet/asz063.

**DOI:** 10.1093/biomet/asz063 · **Source locator:** Section 5 'Simulation study', arXiv:1710.02011v1 PDF pages 12-13: the displayed data-generating mechanism for (C0, A, C1, M, Y). Estimand beta_0 and the path-specific effect P_AMY are defined in Section 2, PDF pages 4-5; the identification formula is equation (1), PDF page 5.; adaptation: bundled SCIENTIFIC_SPEC.md and nie_standard_v1/generators.py::_draw

## DGP / generation mechanism

**Sampling design:** IID observations at a fixed structural configuration; separate mechanism and observation seeds.

**Generator source:** [generator.py](../generators/mediation-standard-nie1-miles-v1.py)

**Keywords (source-described):** Not specified

**Observed variables**

X1, A, M1, Y

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

<pre>x=r.uniform(*c[&quot;baseline_support&quot;],size=(n,1))
a=r.binomial(1,expit(c[&quot;exposure_coefficients&quot;][0]+c[&quot;exposure_coefficients&quot;][1]*x[:,0]))
m=(c[&quot;mediator_intercept&quot;]+c[&quot;mediator_baseline&quot;]*x[:,0]+c[&quot;mediator_exposure&quot;]*a+c[&quot;mediator_sd&quot;]*r.standard_normal(n))[:,None]
y=c[&quot;outcome_intercept&quot;]+c[&quot;outcome_baseline&quot;]*x[:,0]+c[&quot;outcome_exposure&quot;]*a+(c[&quot;outcome_mediator&quot;]+c[&quot;outcome_exposure_mediator&quot;]*a)*m[:,0]+c[&quot;outcome_sd&quot;]*r.standard_normal(n)
return x,a,m,y,[&quot;continuous&quot;],[&quot;continuous&quot;],&quot;continuous&quot;</pre>

<details>
<summary>Original source equations (verbatim)</summary>

<pre>
NIE1 = E[Y(1,M(1))-Y(1,M(0))]
x=r.uniform(*c[&quot;baseline_support&quot;],size=(n,1))
a=r.binomial(1,expit(c[&quot;exposure_coefficients&quot;][0]+c[&quot;exposure_coefficients&quot;][1]*x[:,0]))
m=(c[&quot;mediator_intercept&quot;]+c[&quot;mediator_baseline&quot;]*x[:,0]+c[&quot;mediator_exposure&quot;]*a+c[&quot;mediator_sd&quot;]*r.standard_normal(n))[:,None]
y=c[&quot;outcome_intercept&quot;]+c[&quot;outcome_baseline&quot;]*x[:,0]+c[&quot;outcome_exposure&quot;]*a+(c[&quot;outcome_mediator&quot;]+c[&quot;outcome_exposure_mediator&quot;]*a)*m[:,0]+c[&quot;outcome_sd&quot;]*r.standard_normal(n)
return x,a,m,y,[&quot;continuous&quot;],[&quot;continuous&quot;],&quot;continuous&quot;
</pre>

</details>


## Parameter scenarios, estimands and truth

<table>
<thead><tr><th>Scenario</th><th>Estimand</th><th>Definition</th><th>Reported value</th></tr></thead>
<tbody>
<tr>
<td>native</td>
<td rowspan="1">NIE</td>
<td rowspan="1">

$`\mathbb{E}\!\left[Y\{1,M(1)\}-Y\{1,M(0)\}\right]`$

</td>
<td>-0.51</td>
</tr>
</tbody>
</table>

**Definition notes**

- All scenarios: The intervention applies jointly to the complete mediator vector when M is multivariate; the DGP is an adaptation.

<details>
<summary>Submitted estimand definitions</summary>

Submitted English definitions appear below; other original-language definitions remain in the linked JSON. Concise formulas above are display interpretations and still require scientific review.

**Scenario(s):** native

NIE = E[Y(1,M(1))-Y(1,M(0))] in the adapted fixed-SEM superpopulation, jointly intervening on the complete mediator vector.

[Open raw scientific record (JSON)](./mediation-standard-nie1-miles-v1.json).

</details>


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

- Remove all three induced C1 variables and their M/Y interactions structurally by zeroing mediator_confounder, mediator_exposure_confounder and outcome_confounder. Retain A-M interaction and use treatment-1 natural NIE, not the source reference-level path-specific effect.
- New complete-data superpopulation NIE1 target; original records/estimands are retained separately.
- Standalone canonical generator core SHA256 443e04663970594a8ec2932dc0ee9718c10cc501314d133686dfd0e9acf1baa8

**Warnings:**

- Nothing automatically flagged; this does NOT equal scientific acceptance.
