# Zhao and Cui (2025): repeated-cross-sectional instrumented DiD with bridge confounding

> **Unverified extraction — scientific review required.**

**Primary area:** DiD / Synthetic Control

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Pan Zhao and Yifan Cui (2025). A semiparametric instrumented difference-in-differences approach to policy learning. Biometrika 112(4), asaf043. DOI:10.1093/biomet/asaf043

**DOI:** 10.1093/biomet/asaf043 · **Source locator:** Formal published 16-page PDF, Section6, PDF/printed pp11-12 (unnumbered generation equations); Section2 PDF4-5 CATE and policy value; Section4 PDF8 population E[deltaY(X)/deltaA(X)]. Official supplementary ZIP, 2.pdf, SectionL pp21-22 says same DGP. Author repository panzhaooo/policy-learning-instrumented-DiD commit11f92f2c29316810531935985a981b567b8abab5, simulation/main.R6-28, main.R6-28, source n driver near file end; bridgedist0.1.2 CRAN Archive R/Bridge.R rbridge and qbridge defaults phi1/2 (cross-check only, author package version not pinned).

## DGP / generation mechanism

**Sampling design:** Unit: One independent cross-sectional individual observed at exactly one time T in{0,1}. External n is total row count, not n per period and not a paired panel.; Dependence: Rows iid; independent X1,X2 standard normals; independent U0,U1 bridge(phi=.5); independent Z,T Bernoulli(.5); conditionally independent treatment draws and N(0,1) outcome errors. No serial initialization, common factors or donor construction.

**Generator source:** [generator.py](../generators/did-zhao-cui-2025-bridge-iv-v1.py)

**Keywords (source-described):** Interactions · Nonlinearity · Panel data

**Observed variables**

X1, X2, Z, T, A, Y

**Latent variables**

U0, U1, e0, e1

**Latent-variable identification:** candidates from equations need review

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

$$
X_{1},X_{2}\overset{\mathrm{iid}}{\sim} \mathcal{N}(0,1)
$$

$$
Z,T\overset{\mathrm{iid}}{\sim} \mathrm{Bernoulli}(0.5)
$$

$$
U_{0},U_{1} iid bridge(phi=0.5), density f(u)=1/[2\cdot \pi\cdot cosh(u/2)]. Baseline/exogenous draws independent across rows and variables. U=2\cdot \log(tan(\pi\cdot V/2)), V \mathrm{Uniform}(0,1)
$$

exact machine endpoint0 is redrawn.

$$
p_{0}=\mathrm{expit}(2-7Z+0.2U_{0}+2X_{1})
$$

$$
p_{1}=\mathrm{expit}(-1.5+5Z-0.15U_{1}+1.5X_{2})
$$

$$
A_{0}\sim \mathrm{Bernoulli}(p_{0})
$$

$$
A_{1}\sim \mathrm{Bernoulli}(p_{1}), conditionally independent.
$$

$$
s(X)=1.5X_{1}+2X_{2}-0.5
$$

$$
Y_{0}=200+10\cdot [A_{0}\cdot s(X)+0.5U_{0}+2Z+1.5X_{1}+2X_{2}]+e_{0}
$$

$$
Y_{1}=240+10\cdot [A_{1}\cdot s(X)+0.5U_{1}+2Z+2X_{1}+1.5X_{2}]+e_{1}
$$

$$
e_{0},e_{1}\overset{\mathrm{iid}}{\sim} \mathcal{N}(0,1), independent of all other primitive draws.
$$

$$
A=(1-T)\cdot A_{0}+T\cdot A_{1}
$$

$$
Y=(1-T)\cdot Y_{0}+T\cdot Y_{1}
$$

return X1,X2,Z,T,A,Y only. n is total individuals

$$
paper baseline n=5000 independently tested
$$

$$
official n=32 smoke is a sample-size extension due to unmodified tool cap2048, not an official n_{5000} pass.
$$

$$
\tau_t(x)=\mathbb{E}[Y_t(1)-Y_t(0)\mid X=x]=10\cdot s(x)
$$

$$
ATE=\mathbb{E}[\tau_t(X)]=-5. This is not ATT, finite-sample SATT, PCD or a policy-performance estimand.
$$

<details>
<summary>Original source equations (verbatim)</summary>

<pre>
X1,X2 iid N(0,1); Z,T iid Bernoulli(0.5); U0,U1 iid bridge(phi=0.5), density f(u)=1/[2*pi*cosh(u/2)]. Baseline/exogenous draws independent across rows and variables. U=2*log(tan(pi*V/2)), V Uniform(0,1); exact machine endpoint0 is redrawn.
p0=expit(2-7Z+0.2U0+2X1); p1=expit(-1.5+5Z-0.15U1+1.5X2); A0~Bernoulli(p0),A1~Bernoulli(p1), conditionally independent.
s(X)=1.5X1+2X2-0.5; Y0=200+10*[A0*s(X)+0.5U0+2Z+1.5X1+2X2]+e0; Y1=240+10*[A1*s(X)+0.5U1+2Z+2X1+1.5X2]+e1; e0,e1 iid N(0,1), independent of all other primitive draws.
A=(1-T)*A0+T*A1; Y=(1-T)*Y0+T*Y1; return X1,X2,Z,T,A,Y only. n is total individuals; paper baseline n=5000 independently tested; official n=32 smoke is a sample-size extension due to unmodified tool cap2048, not an official n5000 pass.
tau_t(x)=E[Y_t(1)-Y_t(0)|X=x]=10*s(x); ATE=E[tau_t(X)]=-5. This is not ATT, finite-sample SATT, PCD or a policy-performance estimand.
</pre>

</details>


## Parameter scenarios, estimands and truth

| Scenario | Estimand | Definition | True value | Evidence status |
|---|---|---|---|---|
| section6_main | ATE | Population average causal effect E[Y_t(1)-Y_t(0)]=E[10(1.5X1+2X2-0.5)]=-5 for either t=0 or1, over X~N(0,I2), and original natural Z,U. Not ATT, a finite-sample SATT, optimal-policy value or PCD. | -5.0 | reported_numeric |

## Identifiability assumptions

- Source instrumented-DiD consistency/random sampling, random Z and T, no instrument effect on the untreated trend, stable CATE and no shared unmeasured effect modifier.
- All normal/bridge/Bernoulli innovations are independent as in author simulation/main.R; treatment depends on latent U and observed X, so ordinary unconfoundedness and ordinary unconditional parallel trends are not asserted.
- The scalar truth uses specified intervention conditional means and the standard-normal population, not a finite sample average of heterogenous individual effects.

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Warnings:**

- Latent-variable candidates inferred from source equations; confirm their roles and completeness against the original paper or generator.
