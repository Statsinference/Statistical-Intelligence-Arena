# Three-term assignment and unrelated positive-part outcomes

> **Unverified extraction — scientific review required.**

**Primary area:** ATE — Average Treatment Effect

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Xinkun Nie and Stefan Wager (2021). Quasi-oracle estimation of heterogeneous treatment effects. Biometrika, 108(2):299–319. DOI 10.1093/biomet/asaa076

**DOI:** 10.1093/biomet/asaa076 · **Source locator:** Section 6.1, PDF p.15 / journal p.313, unnumbered shared sampling equations and Set-ups A–D; Section 6.2 / Figure 3, PDF p.16 / journal p.314 for dimension and noise settings; collected paragraph: Set-up D

## DGP / generation mechanism

**Sampling design:** Unit: independent individual; Dependence: Five active covariates; disjoint nonlinear conditional means and treatment interactions. The three-term propensity denominator is retained; it is not expit(X1+X2). No uniform overlap bound is claimed. Independent treatment/noise random draws conditional on covariates; no clusters or panel structure.

**Generator source:** [generator.py](../generators/ate-nie-wager-2020-09-24-setup-d-v1.py)

**Keywords (source-described):** Interactions · Nonlinearity

**Observed variables**

X1–X6 (6 variables), A, Y

<details>
<summary>All observed variable names</summary>

X1, X2, X3, X4, X5, X6, A, Y

</details>

**Latent variables**

Not explicitly identified (review required)

**Latent-variable identification:** explicit structured metadata

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

```math
X\sim \mathcal{N}_{d}(0,I)
```

coordinates independent.

```math
p(X)=1/(1+\exp(-X_{1})+\exp(-X_{2}))
```

```math
A\mid X\sim \mathrm{Bernoulli}(p).
```

```math
u=\max(X_{1}+X_{2}+X_{3},0)
```

```math
v=\max(X_{4}+X_{5},0)
```

```math
b=(u+v)/2
```

```math
\tau=u-v.
```

```math
Y=b(X)+(A-0.5)\cdot \tau(X)+\varepsilon, \varepsilon\sim \mathcal{N}(0,1)
```

```math
\mathrm{equivalently} \mathbb{E}[Y|X,A=1]=u \text{ and } \mathbb{E}[Y|X,A=0]=v.
```

<details>
<summary>Original source equations (verbatim)</summary>

<pre>
X~N_d(0,I); coordinates independent.
p(X)=1/(1+exp(-X1)+exp(-X2)); A|X~Bernoulli(p).
u=max(X1+X2+X3,0); v=max(X4+X5,0); b=(u+v)/2; tau=u-v.
Y=b(X)+(A-0.5)*tau(X)+epsilon, epsilon~N(0,1); equivalently E[Y|X,A=1]=u and E[Y|X,A=0]=v.
</pre>

</details>


## Parameter scenarios, estimands and truth

<table>
<thead><tr><th>Scenario</th><th>Estimand</th><th>Definition</th><th>Reported value</th></tr></thead>
<tbody>
<tr>
<td>original</td>
<td rowspan="1">ATE</td>
<td rowspan="1">

$`\mathbb{E}[Y^{(1)}-Y^{(0)}]`$

</td>
<td>0.1267987153949146</td>
</tr>
</tbody>
</table>

**Definition notes**

- All scenarios: Population ATE; expectation is over the DGP's full population.

<details>
<summary>Submitted estimand definitions</summary>

Submitted English definitions appear below; other original-language definitions remain in the linked JSON. Concise formulas above are display interpretations and still require scientific review.

**Scenario(s):** original

E[Y(1)-Y(0)] in the full declared covariate population; treatment 1 versus 0; population, not sample-conditional, target.

[Open raw scientific record (JSON)](./ate-nie-wager-2020-09-24-setup-d-v1.json).

</details>


**Original submitted target notation:** ATE


## Identifiability assumptions

- Consistency and no interference across independent individuals.
- Conditional exchangeability given observed baseline X under the declared synthetic assignment.
- Pointwise positivity; no uniform overlap bound claimed for unbounded Gaussian logistic settings.

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Adaptations from the source (submitted, unverified):**

- Target explicitly changed from conditional effect tau(x) to population ATE E[tau(X)]; original data-generating law retained. No claim that the source reports this ATE numerical value.
- Source treatment indicator is named A in the observed output; no scientific change.
- Independently implemented Python/NumPy sampler; source estimator fitting and large simulation replications are outside this collection task.

**Warnings:**

- Nothing automatically flagged; this does NOT equal scientific acceptance.
