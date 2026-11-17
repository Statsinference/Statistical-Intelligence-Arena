# Donor-outcome-weighted panel with stationary AR(1) residuals

> **Unverified extraction — scientific review required.**

**Primary area:** Synthetic Control

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Chernozhukov, V., Wüthrich, K., and Zhu, Y. (2021). An Exact and Robust Conformal Inference Method for Counterfactual and Synthetic Controls. Journal of the American Statistical Association, 116(536), 1849–1864. DOI:10.1080/01621459.2021.1920957

**DOI:** 10.1080/01621459.2021.1920957 · **Source locator:** Official supplemental appendix (2021-04-05), Appendix G PDF pp.14–15, Table I.2 PDF p.57. Official Figshare 10.6084/m9.figshare.14473870.v1, file ID27702607, archive MD5 45cd06497fcc35dcd7b30f5340565fc2. replication_package_final/simulations_conformal_final.R:31–39 (AR start and recursion),43–73 (factors/donors/weights/treated),98 (one post),149–150,164 (source baseline grid).

## DGP / generation mechanism

**Sampling design:** Unit: One joint 21-unit panel with20 pre and1 post periods, returned in unit-wide rows; one fixed treated unit and20 untreated donors.; Dependence: Shared iid Gaussian factors across units, stationary independent AR(1) donor residuals, and extra independent AR(1) u. Total treated residual inherits weighted donor residuals and is not independent of them.

**Generator source:** [generator.py](../generators/did-cwz-2021-donor-ar-null-v1.py)

**Keywords (source-described):** Panel data

**Observed variables**

G, Y_pre_01, Y_pre_02, Y_pre_03, Y_pre_04, Y_pre_05, Y_pre_06, Y_pre_07, Y_pre_08, Y_pre_09, Y_pre_10–Y_pre_20 (11 variables), Y_post_01

<details>
<summary>All observed variable names</summary>

G, Y_pre_01, Y_pre_02, Y_pre_03, Y_pre_04, Y_pre_05, Y_pre_06, Y_pre_07, Y_pre_08, Y_pre_09, Y_pre_10, Y_pre_11, Y_pre_12, Y_pre_13, Y_pre_14, Y_pre_15, Y_pre_16, Y_pre_17, Y_pre_18, Y_pre_19, Y_pre_20, Y_post_01

</details>

**Latent variables**

F_1t, F_2t, eta_dt, xi_t

**Latent-variable identification:** candidates from equations need review

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

**factors and stationary residuals**

```math
t=1,\ldots ,21
```

```math
F_{1t},F_{2t}\overset{\mathrm{iid}}{\sim} \mathcal{N}(0,1)
```

independent across factors and times. epsilon_d0,u_0 iid N(0,1)

```math
\varepsilon_{\mathrm{dt}}=0.6\cdot \varepsilon_{d,t-1}+\eta_{\mathrm{dt}}
```

```math
u_{t}=0.6\cdot u_{t}-1+\xi_{t}
```

```math
\eta_{\mathrm{dt}},\xi_{t}\overset{\mathrm{iid}}{\sim} \mathcal{N}(0,0.64)
```

Initial states and innovations mutually independent and

independent of factors

**donor observations**

```math
J=20
```

```math
\mathrm{reindex} \mathrm{donors} d=1,\ldots ,20 (\text{ source } j=d+1)
```

```math
\text{ a }_{d}=b_{d}=d/20. Y_{\mathrm{dt}}=\text{ a }_{d}+F_{1t}+b_{d}\cdot F_{2t}+\varepsilon_{\mathrm{dt}}.
```

**source weight scenarios**

```math
W_{1}: w_{d}=1/20 (\mathrm{default})
```

```math
W_{2}: w_{1}=w_{2}=w_{3}=1/3, \mathrm{others0}
```

```math
W_{3}: w_{d}=-1/20
```

```math
W_{4}: w_{1}=1,w_{2}=-1,\mathrm{others0}
```

These are four scenarios of one family.

**treated observation**

Source notation retained without guessing:

<pre>Y_0t(0)=sum_(d=1)^20 w_d*Y_dt+u_t, using actual donor outcomes including donor errors</pre>

```math
Y_{0t}=Y_{0t}^{(0)}+1\{t=21\}\cdot \theta_{T}, \theta_{T}=0. G_{0}=1,\mathrm{donors} G=0
```

20pre+1post

```math
n=21 \text{ only }.
```

**causal target**

```math
Y_{0},21(1)-Y_{0},21(0)=\theta_{T}=0 \text{ for } \mathrm{every} \mathrm{realization}
```

design expectation and single-treated finite SATT are zero for every weight scenario.

<details>
<summary>Original source equations (verbatim)</summary>

<pre>
t=1,...,21; F_1t,F_2t iid N(0,1), independent across factors and times. epsilon_d0,u_0 iid N(0,1); epsilon_dt=0.6*epsilon_d,t-1+eta_dt; u_t=0.6*u_t-1+xi_t; eta_dt,xi_t iid N(0,0.64). Initial states and innovations mutually independent and independent of factors.
J=20; reindex donors d=1,...,20 (source j=d+1); a_d=b_d=d/20. Y_dt=a_d+F_1t+b_d*F_2t+epsilon_dt.
W1: w_d=1/20 (default); W2: w_1=w_2=w_3=1/3, others0; W3: w_d=-1/20; W4: w_1=1,w_2=-1,others0. These are four scenarios of one family.
Y_0t(0)=sum_(d=1)^20 w_d*Y_dt+u_t, using actual donor outcomes including donor errors; Y_0t=Y_0t(0)+1{t=21}*theta_T, theta_T=0. G_0=1,donors G=0; 20pre+1post; n=21 only.
Y_0,21(1)-Y_0,21(0)=theta_T=0 for every realization; design expectation and single-treated finite SATT are zero for every weight scenario.
</pre>

</details>


## Parameter scenarios, estimands and truth

<table>
<thead><tr><th>Scenario</th><th>Estimand</th><th>Definition</th><th>Reported value</th></tr></thead>
<tbody>
<tr>
<td>W1</td>
<td rowspan="4">Treated-unit treatment effect</td>
<td rowspan="4">

$`Y_{1,T}^{(1)}-Y_{1,T}^{(0)},\quad T=T_0+1=21`$

</td>
<td>0.0</td>
</tr>
<tr>
<td>W2</td>
<td>0.0</td>
</tr>
<tr>
<td>W3</td>
<td>0.0</td>
</tr>
<tr>
<td>W4</td>
<td>0.0</td>
</tr>
</tbody>
</table>

**Definition notes**

- All scenarios: Fixed treated unit.

<details>
<summary>Submitted estimand definitions</summary>

Submitted English definitions appear below; other original-language definitions remain in the linked JSON. Concise formulas above are display interpretations and still require scientific review.

**Scenario(s):** W1, W2, W3, W4

Y_1,T(1)-Y_1,T(0) at the fixed treated unit and T=T0+1=21. Its design-population expectation and the finite single-treated-unit SATT equal theta_T=0.

[Open raw scientific record (JSON)](./did-cwz-2021-donor-ar-null-v1.json).

</details>


**Original submitted target notation:** tau_T


## Identifiability assumptions

- Consistency and no anticipation: only the designated treated unit at the last period receives the additive response; treatment changes neither donor outcomes nor exogenous processes.
- The same donor panel and extra residual are held fixed across potential treatment states. Stable source untreated relationships and Gaussian processes are explicit DGP restrictions.
- SC nonnegative sum-one weight restrictions hold for W1/W2, not for W3/W4. These are intentional source misspecification scenarios; causal truth does not require an estimator to be correctly specified.

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Adaptations from the source (submitted, unverified):**

- Select the published supplemental Table I.2 cell J=20,T0=20,T_post=1,rho_epsilon=rho_u=0.6,theta_T=0. All four official weights are scenarios of one mechanism family; W1 is default.
- Represent the single jointly generated panel as 21 unit rows and 22 observed columns; n must equal21. No sample-size extensions or latent labels are exported.
- Use independently written standard-library Python with a local random stream. Preserve source distributions and generation equations, without claiming R bitwise replay or estimator-performance replication.

**Warnings:**

- Latent-variable candidates inferred from source equations; confirm their roles and completeness against the original paper or generator.
- Catalog placement: Treated-unit and donor panel for counterfactual/synthetic controls.
