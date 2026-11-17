# Two-period nonlinear-covariate panel with a zero treatment effect

> **Unverified extraction — scientific review required.**

**Primary area:** Legacy DiD / Synthetic Control — classification needed

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Abadie, A., and L’Hour, J. (2021). A Penalized Synthetic Control Estimator for Disaggregated Data. Journal of the American Statistical Association, 116(536), 1817–1834. DOI:10.1080/01621459.2021.1971535

**DOI:** 10.1080/01621459.2021.1971535 · **Source locator:** Published PDF: Section 5, PDF p.8/journal p.1824 (unnumbered DGP), PDF p.9/journal p.1825 (sample sizes), Table 4 PDF p.13/journal p.1829. Author simulations/Main_MonteCarlo_v3.m commit 3f2ad93a96acd558841275d07cd70576c78d451f, lines 33–37,69–81,205–219.

## DGP / generation mechanism

**Sampling design:** Unit: Independent units in fixed treated/control strata; two observations per unit represented by one wide row.; Dependence: Shared four baseline covariates within unit; independent standard-normal period disturbances. Covariates iid within strata and across dimensions; no missingness or attrition.

**Generator source:** [generator.py](../generators/did-abadie-lhour-2021-nonlinear-null-v1.py)

**Keywords (source-described):** Nonlinearity

**Observed variables**

G, X1–X4 (4 variables), Y_pre, Y_post

<details>
<summary>All observed variable names</summary>

G, X1, X2, X3, X4, Y_pre, Y_post

</details>

**Latent variables**

Not explicitly identified (review required)

**Latent-variable identification:** not explicitly specified

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

**fixed strata and sample-size interface**

n is units

```math
n_{1}=\min(n-1,\max(1,\lfloor n/5+0.5\rfloor))
```

```math
n_{0}=n-n_{1}
```

```math
\mathrm{baseline} n=500 \mathrm{gives} n_{1}=100,n_{0}=400
```

Source notation retained without guessing:

<pre>Other n are sample_size_extension_not_paper_table4. G_i=1 for first n1 units and 0 otherwise.</pre>

**covariates**

```math
p=4,r=2,\text{ a }=0.1,b=0.9,h=0.1
```

```math
X_{ij}\mid G_{i}=1\overset{\mathrm{iid}}{\sim} \mathrm{Uniform}(\text{ a },b)
```

```math
X_{ij}\mid G_{i}=0=\sqrt{U_{ij}}, U_{ij}\overset{\mathrm{iid}}{\sim} \mathrm{Uniform}(0,1)
```

Independent across units and covariate coordinates

**population normalization**

```math
v=\sqrt{p\cdot \mathrm{Var}(X^{r}\mid G=1)}
```

```math
\mathbb{E}[X^{k}\mid G=1]=(b^{k+1}-\text{ a }^{k+1})/((k+1)\cdot (b-\text{ a }))
```

```math
v^{2}=6256/28125
```

```math
\mu_{i}=\sum_{j=1}^{4} X_{ij}^{2}/v.
```

**observed two-period outcomes**

Source notation retained without guessing:

<pre>Y_pre_i=mu_i+epsilon_pre_i</pre>

Source notation retained without guessing:

<pre>Y_post_i=mu_i+epsilon_post_i</pre>

```math
\text{ all } \mathrm{period}/\mathrm{unit} \mathrm{errors}\overset{\mathrm{iid}}{\sim} \mathcal{N}(0,1)
```

independent of X

```math
\mathrm{The} \mathrm{same} X \text{ is } \mathrm{shared} \text{ across } \mathrm{periods}. A_{\mathrm{pre}}=0,A_{\mathrm{post}}=G
```

```math
\mathrm{treatment}_{\mathrm{effect}}=0.
```

**causal target**

```math
\mathrm{ATT}_{\mathrm{post}}=\mathbb{E}[Y_{2}(1)-Y_{2}(0)\mid G=1]=0
```

Source notation retained without guessing:

<pre>holding the same post error fixed across intervention states gives finite-sample SATT=0.</pre>

<details>
<summary>Original source equations (verbatim)</summary>

<pre>
n is units; n1=min(n-1,max(1,floor(n/5+0.5))), n0=n-n1; baseline n=500 gives n1=100,n0=400. Other n are sample_size_extension_not_paper_table4. G_i=1 for first n1 units and 0 otherwise.
p=4,r=2,a=0.1,b=0.9,h=0.1; X_ij|G_i=1 iid Uniform(a,b); X_ij|G_i=0=sqrt(U_ij), U_ij iid Uniform(0,1). Independent across units and covariate coordinates.
v=sqrt(p*Var(X^r|G=1)); E[X^k|G=1]=(b^(k+1)-a^(k+1))/((k+1)*(b-a)); v^2=6256/28125; mu_i=sum_(j=1)^4 X_ij^2/v.
Y_pre_i=mu_i+epsilon_pre_i; Y_post_i=mu_i+epsilon_post_i; all period/unit errors iid N(0,1), independent of X. The same X is shared across periods. A_pre=0,A_post=G; treatment_effect=0.
ATT_post=E[Y_2(1)-Y_2(0)|G=1]=0; holding the same post error fixed across intervention states gives finite-sample SATT=0.
</pre>

</details>


## Parameter scenarios, estimands and truth

<table>
<thead><tr><th>Scenario</th><th>Estimand</th><th>Definition</th><th>Reported value</th></tr></thead>
<tbody>
<tr>
<td>paper_table4_p4_r2_with_declared_n_extension</td>
<td rowspan="1">ATT</td>
<td rowspan="1">

$`\mathbb{E}[Y_2(1)-Y_2(0)\mid G=1]`$

</td>
<td>0.0</td>
</tr>
</tbody>
</table>

**Definition notes**

- All scenarios: Treated covariate population.

<details>
<summary>Submitted estimand definitions</summary>

Submitted English definitions appear below; other original-language definitions remain in the linked JSON. Concise formulas above are display interpretations and still require scientific review.

**Scenario(s):** paper_table4_p4_r2_with_declared_n_extension

E[Y_2(1)-Y_2(0)\|G=1] in the treated covariate population. Equal-weight finite-sample treated SATT also equals zero pointwise.

[Open raw scientific record (JSON)](./did-abadie-lhour-2021-nonlinear-null-v1.json).

</details>


**Original submitted target notation:** ATT_post


## Identifiability assumptions

- Consistency, no interference and no anticipation; A_pre=0 and A_post=G.
- Shared time-invariant unit signal and independent mean-zero period disturbances imply parallel untreated mean trends; zero treatment response is a structural DGP restriction.

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Adaptations from the source (submitted, unverified):**

- Baseline follows published Table 4 (100 treated/400 controls); author v3 default is 100/1000 and is not claimed as the baseline.
- External n counts units; other n follow the explicitly documented deterministic approximately 1:4 allocation and are sample-size extensions.
- Seven observed columns in a unit-wide representation; Python local RNG preserves the specified distributions, not MATLAB random-stream identity. No estimator or Table 4 performance replication.

**Warnings:**

- No explicit latent-variable metadata or reliably identifiable latent declarations; absence from this list does not prove that no latent variables exist.
- Legacy combined DiD / Synthetic Control family: human classification required; not automatically reassigned.
