# Time-varying instrumental variables with confounding and censored survival

> **Unverified extraction — scientific review required.**

**Primary area:** IV — Instrumental Variables

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Cui, Y., Michael, H., Tanser, F. and Tchetgen Tchetgen, E. (2023). Instrumental variable estimation of the marginal structural Cox model for time-varying treatments. Biometrika 110(1),101-118. DOI:10.1093/biomet/asab062. Advance publication 2021.

**DOI:** 10.1093/biomet/asab062 · **Source locator:** Actual read: published full-text PMC9919489 HTML, Sections2-4; Section4.2 eq(8) [image Equation24.gif], unnumbered integral [image Equation25.gif], factorization [Equation26.gif]; Section4.3 ordered simulation list [ImEquation185-209.gif]. These GIF names are asset identifiers, NOT paper equation numbers. Source equations visually checked from the original assets.

## DGP / generation mechanism

**Sampling design:** Unit: individual longitudinal trajectory represented as a wide row; Dependence: iid persons; within-person observations at0 and1 depend through latent T00,U and treatment-confounder feedback

**Generator source:** [generator.py](../generators/iv-cui-2023-longitudinal-survival-v1.py)

**Keywords (source-described):** Interactions · Nonlinearity

**Observed variables**

L0, Z0, A0, R1, L1, Z1, A1, Y, event, T00, U0, U1

**Latent variables**

Not explicitly identified (review required)

**Latent-variable identification:** not explicitly specified

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

**Exogenous draws**

$$
T_{00}\sim \mathrm{Exponential}(\text{ rate }=1)
$$

$$
\text{ independent } \varepsilon_{1},\ldots ,\varepsilon_{4}\sim \mathcal{N}(0,0.5^{2})
$$

$$
\text{ independent } \mathrm{Ctilde}\sim \mathrm{Uniform}(0,4).
$$

**Baseline confounding**

$$
\begin{aligned}
L_{0} &= 1.5\cdot T_{00}+\varepsilon_{1} \\
U_{0} &= 1.5\cdot T_{00}+\varepsilon_{2}.
\end{aligned}
$$

**Baseline instrument**

$$
Z_{0}\mid L_{0}\sim \mathrm{Bernoulli}(\Phi(-0.5+0.2\cdot L_{0})).
$$

**Baseline treatment**

$$
\Delta_{0}=\Phi(0.2\cdot L_{0})
$$

$$
A_{0}\mid L_{0},U_{0},Z_{0}\sim \mathrm{Bernoulli}(\Phi(0.2\cdot L_{0}-0.8\cdot U_{0})\cdot (1-\Delta_{0})+Z_{0}\cdot \Delta_{0}).
$$

**Second-visit confounding**

$$
\begin{aligned}
L_{1} &= L_{0}-U_{0}+1.5\cdot A_{0}+T_{00}+\varepsilon_{3} \\
U_{1} &= 0.5\cdot L_{0}-U_{0}+A_{0}+T_{00}+\varepsilon_{4}.
\end{aligned}
$$

**Second instrument**

$$
Z_{1}\mid L_{1},A_{0},Z_{0}\sim \mathrm{Bernoulli}(\Phi(-1+0.2\cdot L_{1}+0.2\cdot A_{0}+0.2\cdot Z_{0})).
$$

**Second treatment**

$$
\Delta_{1}=\Phi(0.2\cdot L_{1})
$$

$$
A_{1}\mid L_{1},U_{1},Z_{1}\sim \mathrm{Bernoulli}(\Phi(0.2\cdot L_{1}-0.8\cdot U_{1})\cdot (1-\Delta_{1})+Z_{1}\cdot \Delta_{1}).
$$

**Causal failure time**

$$
T_{00}=\mathrm{int}_{0}^{T} \exp(\psi\cdot \text{ a }(s))\mathrm{ds} \text{ with } \text{ a }(s)=A_{0} \text{ for } s\leq 1 \text{ and } A_{1} \text{ for } s>1
$$

$$
\psi=-1 \mathrm{or0}
$$

$$
\mathrm{Let} q_{0}=\exp(\psi\cdot A_{0})
$$

$$
q_{1}=\exp(\psi\cdot A_{1}). T=T_{00}/q_{0} \text{ if } T_{00}\leq q_{0}
$$

$$
T=1+(T_{00}-q_{0})/q_{1} \text{ otherwise }.
$$

**Censoring**

$$
C=\min(\mathrm{Ctilde},2)
$$

$$
Y=\min(T,C)
$$

$$
\mathrm{event}=I(T\leq C).
$$

**Observed representation**

$$
R_{1}=I(Y\geq 1)
$$

output second-visit L1,Z1,A1 multiplied by R1, together with R1

Never output T00,U0,U1,T,C or errors.

**Population target**

$$
\mathrm{For} \text{ fixed } \mathrm{treatment} \mathrm{regime} \text{ a }, \lambda_{\mathrm{Ta}}(t)=\exp(\psi\cdot \text{ a }(t))
$$

Source notation retained without guessing:

<pre>psi=log(hazard under a(t)=1 / hazard under a(t)=0), at a common time away from1</pre>

$$
\mathrm{Baseline} \mathrm{hazard}=1.
$$

<details>
<summary>Original source equations (verbatim)</summary>

<pre>
T00~Exponential(rate=1); independent epsilon1,...,epsilon4~N(0,0.5^2); independent Ctilde~Uniform(0,4).
L0=1.5*T00+epsilon1; U0=1.5*T00+epsilon2.
Z0|L0~Bernoulli(Phi(-0.5+0.2*L0)).
Delta0=Phi(0.2*L0); A0|L0,U0,Z0~Bernoulli(Phi(0.2*L0-0.8*U0)*(1-Delta0)+Z0*Delta0).
L1=L0-U0+1.5*A0+T00+epsilon3; U1=0.5*L0-U0+A0+T00+epsilon4.
Z1|L1,A0,Z0~Bernoulli(Phi(-1+0.2*L1+0.2*A0+0.2*Z0)).
Delta1=Phi(0.2*L1); A1|L1,U1,Z1~Bernoulli(Phi(0.2*L1-0.8*U1)*(1-Delta1)+Z1*Delta1).
T00=int_0^T exp(psi*a(s))ds with a(s)=A0 for s&lt;=1 and A1 for s&gt;1; psi=-1 or0. Let q0=exp(psi*A0),q1=exp(psi*A1). T=T00/q0 if T00&lt;=q0; T=1+(T00-q0)/q1 otherwise.
C=min(Ctilde,2); Y=min(T,C); event=I(T&lt;=C).
R1=I(Y&gt;=1); output second-visit L1,Z1,A1 multiplied by R1, together with R1. Never output T00,U0,U1,T,C or errors.
For fixed treatment regime a, lambda_Ta(t)=exp(psi*a(t)); psi=log(hazard under a(t)=1 / hazard under a(t)=0), at a common time away from1. Baseline hazard=1.
</pre>

</details>


## Parameter scenarios, estimands and truth

| Scenario | Estimand | Definition | True value | Evidence status |
|---|---|---|---|---|
| source_effect_minus1 | psi | Population marginal structural Cox log hazard ratio for the current binary treatment under fixed two-visit intervention regimes: lambda_Ta(t)=lambda0(t)*exp(psi*a(t)), lambda0(t)=1. Compare treatment1 versus0 at the same time t away from the visit1 switch. Target is psi=-1 or0, not a survival probability difference or LATE. | -1.0 | reported_numeric |
| source_null | psi | Population marginal structural Cox log hazard ratio for the current binary treatment under fixed two-visit intervention regimes: lambda_Ta(t)=lambda0(t)*exp(psi*a(t)), lambda0(t)=1. Compare treatment1 versus0 at the same time t away from the visit1 switch. Target is psi=-1 or0, not a survival probability difference or LATE. | 0.0 | reported_numeric |

## Identifiability assumptions

- iid individuals; consistency and no interference; potential treatments constant on (0,1] and after1.
- Time-varying Z generated conditional on observed pre-treatment history using independent Bernoulli draws; sequential instrument independence and exclusion given that history.
- Instrument positivity and relevance: at visit j, the treatment-probability contrast for Z=1 versus0 equals Delta_j=Phi(0.2 L_j)&gt;0 and is independent of unobserved U_j given L_j (independent compliance type, source Assumption6).
- Unmeasured time-varying confounding is present; ordinary sequential ignorability given L alone is not asserted.
- Independent censoring C=min(Uniform(0,4),2); estimation target is observed only up to administrative time2.
- Second-visit covariates/instrument/treatment only observed while at risk R1=1; use mask and survival endpoint jointly.

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Warnings:**

- No explicit latent-variable metadata or reliably identifiable latent declarations; absence from this list does not prove that no latent variables exist.
