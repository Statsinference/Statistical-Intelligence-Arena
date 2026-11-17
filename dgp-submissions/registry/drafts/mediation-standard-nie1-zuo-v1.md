# Standard NIE1 adaptation: zuo

> **Unverified extraction — scientific review required.**

**Primary area:** Mediation — Direct and Indirect Effects

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Zuo, S., Ghosh, D., Ding, P. and Yang, F. (2025). Mediation Analysis with the Mediator and Outcome Missing Not at Random. Journal of the American Statistical Association 120(550), 794–804. DOI: 10.1080/01621459.2024.2359132.

**DOI:** 10.1080/01621459.2024.2359132 · **Source locator:** Published paper §5.1, Setting C and Assumption III; numeric coefficients in author arXiv:2212.05577v3 supplemental Table S1, PDF p.72 (zero-index 71), lines 3984–4006.; adaptation: bundled SCIENTIFIC_SPEC.md and nie_standard_v1/generators.py::_draw

## DGP / generation mechanism

**Sampling design:** IID observations at a fixed structural configuration; separate mechanism and observation seeds.

**Generator source:** [generator.py](../generators/mediation-standard-nie1-zuo-v1.py)

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

<pre>x=c[&quot;x_mean&quot;]+c[&quot;x_sd&quot;]*r.standard_normal((n,1))
a=r.binomial(1,c[&quot;p_t&quot;],n)
m=(c[&quot;alpha_0&quot;]+c[&quot;alpha_t&quot;]*a+c[&quot;alpha_x&quot;]*x[:,0]+c[&quot;m_sd&quot;]*r.standard_normal(n))[:,None]
y=c[&quot;beta_0&quot;]+c[&quot;beta_t&quot;]*a+(c[&quot;beta_m&quot;]+c[&quot;beta_mt&quot;]*a)*m[:,0]+c[&quot;beta_x&quot;]*x[:,0]+c[&quot;y_sd&quot;]*r.standard_normal(n)
return x,a,m,y,[&quot;continuous&quot;],[&quot;continuous&quot;],&quot;continuous&quot;</pre>

<details>
<summary>Original source equations (verbatim)</summary>

<pre>
NIE1 = E[Y(1,M(1))-Y(1,M(0))]
x=c[&quot;x_mean&quot;]+c[&quot;x_sd&quot;]*r.standard_normal((n,1))
a=r.binomial(1,c[&quot;p_t&quot;],n)
m=(c[&quot;alpha_0&quot;]+c[&quot;alpha_t&quot;]*a+c[&quot;alpha_x&quot;]*x[:,0]+c[&quot;m_sd&quot;]*r.standard_normal(n))[:,None]
y=c[&quot;beta_0&quot;]+c[&quot;beta_t&quot;]*a+(c[&quot;beta_m&quot;]+c[&quot;beta_mt&quot;]*a)*m[:,0]+c[&quot;beta_x&quot;]*x[:,0]+c[&quot;y_sd&quot;]*r.standard_normal(n)
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
<td>2.0</td>
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

[Open raw scientific record (JSON)](./mediation-standard-nie1-zuo-v1.json).

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

- Export complete M and Y before MNAR masks; omit missingness indicators. Preserve the full-data A-M interaction and natural NIE1.
- New complete-data superpopulation NIE1 target; original records/estimands are retained separately.
- Standalone canonical generator core SHA256 443e04663970594a8ec2932dc0ee9718c10cc501314d133686dfd0e9acf1baa8

**Warnings:**

- Nothing automatically flagged; this does NOT equal scientific acceptance.
