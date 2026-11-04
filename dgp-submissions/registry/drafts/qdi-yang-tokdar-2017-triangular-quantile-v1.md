# Published Figure 1 triangular predictor DGP: conditional 0.95 quantile at the centroid

> **Unverified extraction — scientific review required.**

**Primary area:** Quantile Inference

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Yang, Yun and Tokdar, Surya T. (2017). Joint Estimation of Quantile Planes Over Arbitrary Predictor Spaces. Journal of the American Statistical Association 112(519), 1107-1120. DOI: 10.1080/01621459.2016.1192545.

**DOI:** 10.1080/01621459.2016.1192545 · **Source locator:** Published Figure 1 caption (unnumbered quantile equation), Sec.1.3 context: journal p.1108 / PDF p.3 including publisher cover; citation PDF p.1. Quantile definition and shared-rank inverse transform: journal p.1107/PDF p.2 Eqs.(1)–(3). Density/row likelihood: journal p.1110/PDF p.5 Sec.2.3. Independent stochastic design: journal p.1112/PDF p.7 Sec.4. Supplement p.1 and Sec.B.1 pp.9–11. Upstream repository/commit/file/function/line evidence is in source_records.json and card.md; it is provenance context, not executed DGP code. Published Sec.5.1 is a separate univariate design.

## DGP / generation mechanism

**Sampling design:** Unit: One fully observed synthetic vector (X1,X2,Y); n is row count. Published illustration n=1000.; Dependence: iid rows; within-row predictor covariance Cov(X1,X2)=-5/12 (derived). A single independent standard Gaussian rank generates each Y. No network, panel, cluster or interference structure.

**Generator source:** [generator.py](../generators/qdi-yang-tokdar-2017-triangular-quantile-v1.py)

**Keywords (source-described):** Linearity

**Observed variables**

X1, X2, Y

**Latent variables**

R_i, T_i, Z_i

**Latent-variable identification:** candidates from equations need review

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

**Generation step 0: n, seed, fixed constants**

$$
\mathrm{Published} \mathrm{illustration} n=1000
$$

Source notation retained without guessing:

<pre>check n=128, seed=1729 are collector choices. A=(-1,1)</pre>

$$
B=(-1,2)
$$

$$
C=(2,-1)
$$

normal means (0,1), standard deviations (1,1/5).

**Generation step 1: R_i,T_i; u_i,v_i (internal)**

$$
R_{i},T_{i}\overset{\mathrm{iid}}{\sim} \mathrm{Uniform}(0,1)
$$

$$
\text{ if } R_{i}+T_{i}>1 \text{ then } (u_{i},v_{i})=(1-R_{i},1-T_{i}), \mathrm{else} (R_{i},T_{i})
$$

$$
\mathrm{Density} \text{ of } (u_{i},v_{i}) \text{ is } 2 \text{ on } u\geq 0,v\geq 0,u+v\leq 1.
$$

**Generation step 2: X_i=(X1_i,X2_i) (observed)**

$$
X_{i}=A+u_{i}(B-A)+v_{i}(C-A)=(-1+3v_{i},1+u_{i}-2v_{i})
$$

$$
X_{i}\sim \mathrm{Uniform}_{\mathrm{area}}(D). D=\{x_{1}\geq -1,2x_{1}+3x_{2}\geq 1,x_{1}+x_{2}\leq 1\}
$$

$$
\mathrm{area}=3/2, \mathrm{density}=2/3.
$$

**Generation step 3: s_i,a_i,b_i (internal deterministic values)**

$$
s_{i}=\mathrm{X1}_{i}+\mathrm{X2}_{i} \in [0,1]
$$

$$
\text{ a }_{i}=(1-s_{i})/3 \in [0,1/3]
$$

$$
b_{i}=(2+s_{i})/3 \in [2/3,1]
$$

$$
\text{ a }_{i}+b_{i}=1.
$$

**Generation step 4: Z_i (internal common rank)**

$$
Z_{i}\sim \mathcal{N}(0,1)
$$

independent of (R_i,T_i), X_i and other rows

Source notation retained without guessing:

<pre>Equivalently U_i=Phi(Z_i)~Uniform(0,1). L0_i=Z_i and L1_i=1+(1/5)Z_i share this same Z_i, hence have correlation 1.</pre>

**Generation step 5: Y_i (observed)**

$$
Y_{i}=\text{ a }_{i} Z_{i}+b_{i}(1+Z_{i}/5)=\mu_{i}+\sigma_{i} Z_{i}
$$

$$
\mu_{i}=(2+s_{i})/3, \sigma_{i}=(7-4s_{i})/15 \in [1/5,7/15]. Y_{i}\mid X_{i}\sim \mathcal{N}(\mu_{i},\sigma_{i}^{2}). \varepsilon_{i}=Y_{i}-\mu_{i} \mathrm{has} \mathrm{conditional} \text{ variance } \sigma_{i}^{2}
$$

epsilon_i is not marginally

independent of X_i because its scale varies

**Generation step 6: Observed table and independent rows**

$$
\mathrm{Repeat} \text{ the } \mathrm{row} \mathrm{law} \text{ iid } \text{ for } i=1,\ldots ,n
$$

Return X1,X2,Y only

$$
\mathrm{Within}-\mathrm{row} X_{1}/X_{2} \mathrm{covariance}=-5/12
$$

Y depends on their sum. No treatment/mediator, assignment, label selection, missingness, censoring, measurement error, predictor training, cluster, panel or interference mechanism.

**Published quantile law**

$$
s=x_{1}+x_{2}
$$

$$
Q_{Y}(\tau|x)=(1-s)/3\cdot Q_{\mathcal{N}}(\tau|0,1)+(2+s)/3\cdot Q_{\mathcal{N}}(\tau|1,0.2^{2}), \text{ where } \mathrm{second} Q_{\mathrm{N}} \mathrm{parameter} \text{ is } \text{ variance }.
$$

**Derived coefficient functions**

$$
z_{\tau}=\Phi^{-1}(\tau)
$$

$$
\beta_{0}(\tau)=2/3+(7/15)z_{\tau}
$$

$$
\beta_{1}(\tau)=\beta_{2}(\tau)=1/3-(4/15)z_{\tau}
$$

Derived, not new parameters.

**Joint density and CDF**

$$
f_{X},Y(x,y)=(2/3)\cdot 1_{D}(x)\cdot \phi((y-\mu(x))/\sigma(x))/\sigma(x)
$$

$$
F_{Y}(y\mid x)=\Phi((y-\mu(x))/\sigma(x)).
$$

**Adapted fixed query**

$$
x^{\ast}=(0,2/3), \tau^{\ast}=19/20
$$

$$
\theta=8/9+(13/45)\cdot \Phi^{-1}(19/20).
$$

<details>
<summary>Original source equations (verbatim)</summary>

<pre>
Published illustration n=1000; check n=128, seed=1729 are collector choices. A=(-1,1), B=(-1,2), C=(2,-1); normal means (0,1), standard deviations (1,1/5).
R_i,T_i iid Uniform(0,1); if R_i+T_i&gt;1 then (u_i,v_i)=(1-R_i,1-T_i), else (R_i,T_i). Density of (u_i,v_i) is 2 on u&gt;=0,v&gt;=0,u+v&lt;=1.
X_i=A+u_i(B-A)+v_i(C-A)=(-1+3v_i,1+u_i-2v_i); X_i~Uniform_area(D). D={x1&gt;=-1,2x1+3x2&gt;=1,x1+x2&lt;=1}; area=3/2, density=2/3.
s_i=X1_i+X2_i in [0,1]; a_i=(1-s_i)/3 in [0,1/3]; b_i=(2+s_i)/3 in [2/3,1]; a_i+b_i=1.
Z_i~N(0,1), independent of (R_i,T_i), X_i and other rows. Equivalently U_i=Phi(Z_i)~Uniform(0,1). L0_i=Z_i and L1_i=1+(1/5)Z_i share this same Z_i, hence have correlation 1.
Y_i=a_i Z_i+b_i(1+Z_i/5)=mu_i+sigma_i Z_i; mu_i=(2+s_i)/3, sigma_i=(7-4s_i)/15 in [1/5,7/15]. Y_i|X_i~N(mu_i,sigma_i^2). epsilon_i=Y_i-mu_i has conditional variance sigma_i^2; epsilon_i is not marginally independent of X_i because its scale varies.
Repeat the row law iid for i=1,...,n. Return X1,X2,Y only. Within-row X1/X2 covariance=-5/12; Y depends on their sum. No treatment/mediator, assignment, label selection, missingness, censoring, measurement error, predictor training, cluster, panel or interference mechanism.
s=x1+x2; Q_Y(tau|x)=(1-s)/3*Q_N(tau|0,1)+(2+s)/3*Q_N(tau|1,0.2^2), where second Q_N parameter is variance.
z_tau=Phi^-1(tau); beta0(tau)=2/3+(7/15)z_tau; beta1(tau)=beta2(tau)=1/3-(4/15)z_tau. Derived, not new parameters.
f_X,Y(x,y)=(2/3)*1_D(x)*phi((y-mu(x))/sigma(x))/sigma(x); F_Y(y|x)=Phi((y-mu(x))/sigma(x)).
x*=(0,2/3), tau*=19/20; theta=8/9+(13/45)*Phi^-1(19/20).
</pre>

</details>


## Parameter scenarios, estimands and truth

| Scenario | Estimand | Definition | True value | Evidence status |
|---|---|---|---|---|
| published_triangle_centroid | theta = Q_Y(19/20 \| X=(0,2/3)) | inf{y:F_Y(y\|X=(0,2/3))&gt;=19/20} under the continuous conditional-law version specified by the published Figure 1 law. Exact centroid and quantile level are stored as rational metadata. One pointwise conditional quantile, not a marginal target or simultaneous band. | 1.3640688255637583 | reported_numeric |

## Identifiability assumptions

- iid observation rows (X1,X2,Y); X jointly uniform on conv{(-1,1),(-1,2),(2,-1)}. The two coordinates are dependent within rows.
- Complete observations: no censoring, missingness, selection or measurement error added. Latent Gaussian rank is independent of X and across rows and is never returned.
- Use the conditional distribution version continuous in x specified by the published equation. This makes the probability-zero fixed conditioning point meaningful.
- The centroid (0,2/3) is strictly interior; f_X=2/3 in a neighborhood. s=X1+X2 lies in [0,1]; sigma=(7-4s)/15 lies in [1/5,7/15]. The conditional CDF is continuous, strictly increasing, and has positive density at the target.
- The original coordinate origin is outside this triangle. The theory in Sec.2.1 allows translation to an interior origin, but this generator does not translate observed coordinates or alter the published law. No claim is made that the original origin satisfies that theoretical assumption.
- No causal intervention target; no unconfoundedness, cross-world, treatment-positivity or interference assumptions are imposed.

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Warnings:**

- Latent-variable candidates inferred from source equations; confirm their roles and completeness against the original paper or generator.
