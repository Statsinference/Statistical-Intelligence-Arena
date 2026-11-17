# Sant'Anna--Zhao DGP1: two-period panel with covariate-specific trends

> **Unverified extraction — scientific review required.**

**Primary area:** DiD — Difference-in-Differences

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Sant'Anna, P. H. C. and Zhao, J. (2020). Doubly robust difference-in-differences estimators. Journal of Econometrics 219(1), 101–122. DOI: 10.1016/j.jeconom.2020.06.003.

**DOI:** — · **Source locator:** PDF page 20, Section 4.1, definitions of f_reg/f_ps/Z and DGP1, following paragraph for noise, observed panel, and ATT=0; page 19 for original n=1000.

## DGP / generation mechanism

**Sampling design:** Unit: individual with a two-period panel stored in one wide row; Dependence: iid between individuals; baseline and post-period outcomes within an individual share latent v and covariates

**Generator source:** [generator.py](../generators/did-santanna-zhao-2020-panel-dgp1-v1.py)

**Keywords (source-described):** Interactions · Nonlinearity · Panel data

**Observed variables**

Z1–Z4 (4 variables), D, Y_pre, Y_post

<details>
<summary>All observed variable names</summary>

Z1, Z2, Z3, Z4, D, Y_pre, Y_post

</details>

**Latent variables**

X, U, eta, v

**Latent-variable identification:** candidates from equations need review

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

**Raw covariates**

```math
X \sim \mathcal{N}(0,I_{4})
```

```math
Z_{j}=(\mathrm{Ztilde}_{j}-\mathbb{E}[\mathrm{Ztilde}_{j}])/\mathrm{sd}(\mathrm{Ztilde}_{j})
```

**Transformations**

```math
\mathrm{Ztilde}=(\exp(X_{1}/2),10+X_{2}/(1+\exp(X_{1})),(0.6+X_{1}\cdot X_{3}/25)^{3},(20+X_{2}+X_{4})^{2})
```

**Prognosis**

```math
f(Z)=210+27.4\cdot Z_{1}+13.7\cdot (Z_{2}+Z_{3}+Z_{4})
```

**Group assignment**

```math
g(Z)=0.75\cdot (-Z_{1}+0.5\cdot Z_{2}-0.25\cdot Z_{3}-0.1\cdot Z_{4})
```

```math
D=1\{U\leq \mathrm{sigmoid}(g(Z))\}
```

```math
U\sim U(0,1)
```

**Latent fixed effect**

```math
v=D\cdot f(Z)+\eta
```

```math
\eta\sim \mathcal{N}(0,1)
```

**Panel outcomes**

```math
Y_{\mathrm{pre}}=f(Z)+v+\varepsilon_{0}
```

```math
Y_{1}(d)=2\cdot f(Z)+v+\varepsilon_{1}(d)
```

```math
Y_{\mathrm{post}}=Y_{1}(D)
```

**Innovations**

eta,epsilon0,epsilon1(0),epsilon1(1) are independent N(0,1)

independent of X,U

<details>
<summary>Original source equations (verbatim)</summary>

<pre>
X ~ N(0,I4); Z_j=(Ztilde_j-E[Ztilde_j])/sd(Ztilde_j)
Ztilde=(exp(X1/2),10+X2/(1+exp(X1)),(0.6+X1*X3/25)^3,(20+X2+X4)^2)
f(Z)=210+27.4*Z1+13.7*(Z2+Z3+Z4)
g(Z)=0.75*(-Z1+0.5*Z2-0.25*Z3-0.1*Z4); D=1{U&lt;=sigmoid(g(Z))}; U~U(0,1)
v=D*f(Z)+eta; eta~N(0,1)
Y_pre=f(Z)+v+epsilon0; Y_1(d)=2*f(Z)+v+epsilon1(d); Y_post=Y_1(D)
eta,epsilon0,epsilon1(0),epsilon1(1) are independent N(0,1), independent of X,U
</pre>

</details>


## Parameter scenarios, estimands and truth

<table>
<thead><tr><th>Scenario</th><th>Estimand</th><th>Definition</th><th>Reported value</th></tr></thead>
<tbody>
<tr>
<td>original_panel_dgp1</td>
<td rowspan="1">ATT</td>
<td rowspan="1">

$`\mathbb{E}[Y_1(1)-Y_1(0)\mid D=1]`$

</td>
<td>0.0</td>
</tr>
</tbody>
</table>

**Definition notes**

- All scenarios: Post-period 1.

<details>
<summary>Submitted estimand definitions</summary>

Submitted English definitions appear below; other original-language definitions remain in the linked JSON. Concise formulas above are display interpretations and still require scientific review.

**Scenario(s):** original_panel_dgp1

Population ATT for the treated group at post-period 1. The realized group D and latent v are held fixed across treatment counterfactuals. Original value is zero; this is not the observed post-period group contrast or a sample-average effect.

[Open raw scientific record (JSON)](./did-santanna-zhao-2020-panel-dgp1-v1.json).

</details>


**Original submitted target notation:** ATT = E[Y_1(1)-Y_1(0) \| D=1]


## Identifiability assumptions

- Consistency and no interference across independent panel individuals.
- No anticipation: baseline observed outcome is Y_0(0).
- Conditional parallel trends given observed Z: E[Y_1(0)-Y_0(0)\|D,Z]=f_reg(Z) for either group.
- Pointwise overlap for finite Z through logistic assignment. No uniform bound away from zero or one is asserted on unbounded support.
- Independent normal innovations conditional on Z,D; latent time-invariant v is shared across both periods and counterfactual post-period states.

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Adaptations from the source (submitted, unverified):**

- Retain the original DGP1 distribution and population ATT=0. Only DGP1 is registered; the paper also presents DGP2-DGP4.
- Use Python/NumPy PCG64 instead of attempting identical draws from original estimator experiments; n=128 is an interface smoke check, not the original n=1000 experiment.
- Represent each iid individual as one wide row (Z1-Z4,D,Y_pre,Y_post), preserving shared latent v across periods; raw X and potential outcomes are not released.
- Compute source population normalization using analytic moments for Ztilde1,3,4 and a 120-node Gauss-Hermite constant for Var(Ztilde2). Do not standardize using the realized sample.
- Expose att_shift=0 for the original scenario; nonzero shifts are verification controls only, not paper scenarios or extra families.

**Warnings:**

- Latent-variable candidates inferred from source equations; confirm their roles and completeness against the original paper or generator.
- Catalog placement: Two-period panel for doubly robust difference-in-differences.
