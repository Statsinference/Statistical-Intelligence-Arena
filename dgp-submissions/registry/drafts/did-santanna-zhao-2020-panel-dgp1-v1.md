# Sant'Anna--Zhao DGP1: two-period panel with covariate-specific trends

> **Unverified extraction — scientific review required.**

**Primary area:** DiD / Synthetic Control

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Sant'Anna, P. H. C. and Zhao, J. (2020). Doubly robust difference-in-differences estimators. Journal of Econometrics 219(1), 101–122. DOI: 10.1016/j.jeconom.2020.06.003.

**DOI:** — · **Source locator:** PDF page 20, Section 4.1, definitions of f_reg/f_ps/Z and DGP1, following paragraph for noise, observed panel, and ATT=0; page 19 for original n=1000.

## DGP / generation mechanism

**Sampling design:** Unit: individual with a two-period panel stored in one wide row; Dependence: iid between individuals; baseline and post-period outcomes within an individual share latent v and covariates

**Generator source:** [generator.py](../generators/did-santanna-zhao-2020-panel-dgp1-v1.py)

**Observed variables**

Z1, Z2, Z3, Z4, D, Y_pre, Y_post

**Latent variables**

X, U, eta, v

**Latent-variable identification:** candidates from equations need review

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

$$
X \sim \mathcal{N}(0,I_{4})
$$

$$
Z_j=(Ztilde_j-\mathbb{E}[Ztilde_j])/sd(Ztilde_j)
$$

$$
Ztilde=(\exp(X_{1}/2),10+X_{2}/(1+\exp(X_{1})),(0.6+X_{1}\cdot X_{3}/25)^{3},(20+X_{2}+X_{4})^{2})
$$

$$
f(Z)=210+27.4\cdot Z_{1}+13.7\cdot (Z_{2}+Z_{3}+Z_{4})
$$

$$
g(Z)=0.75\cdot (-Z_{1}+0.5\cdot Z_{2}-0.25\cdot Z_{3}-0.1\cdot Z_{4})
$$

$$
D=1\{U<=sigmoid(g(Z))\}
$$

$$
U\sim U(0,1)
$$

$$
v=D\cdot f(Z)+eta
$$

$$
eta\sim \mathcal{N}(0,1)
$$

$$
Y_pre=f(Z)+v+\varepsilon_{0}
$$

$$
Y_1(d)=2\cdot f(Z)+v+\varepsilon_{1}(d)
$$

$$
Y_post=Y_1(D)
$$

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

| Scenario | Estimand | Definition | True value | Evidence status |
|---|---|---|---|---|
| original_panel_dgp1 | ATT = E[Y_1(1)-Y_1(0) \| D=1] | Population ATT for the treated group at post-period 1. The realized group D and latent v are held fixed across treatment counterfactuals. Original value is zero; this is not the observed post-period group contrast or a sample-average effect. | 0.0 | reported_numeric |

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

**Warnings:**

- Latent-variable candidates inferred from source equations; confirm their roles and completeness against the original paper or generator.
