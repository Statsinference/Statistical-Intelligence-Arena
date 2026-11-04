# Engression official supplementary pre-additive noise: four scenarios, interior conditional medians

> **Unverified extraction — scientific review required.**

**Primary area:** Quantile Inference

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Shen, Xinwei and Meinshausen, Nicolai (2025). Engression: extrapolation through the lens of distributional regression. Journal of the Royal Statistical Society Series B: Statistical Methodology 87(3):653–677. DOI:10.1093/jrsssb/qkae108.

**DOI:** 10.1093/jrsssb/qkae108 · **Source locator:** Published main PDF (25 pages, no cover): equation (2), journal p.655/PDF p.3; Section 2.1 equation (4), journal p.656/PDF p.4; Section 3.2, journal pp.662–663/PDF pp.10–11; Section 6, journal p.671/PDF p.19, defers simulations to supplementary C.1. Official supplement: C.1/Table C.1 PDF p.2, H.1 PDF p.29. Relevant pages personally read as text and rendered images. Official code fixed snapshot eb6b83b1613458b5b3547e4e44a81da4712ab581: engression-python/engression/data/simulator.py, preanm_simulator lines 6–57, transforms 22–30, Log 30, noise 35–40, training 42–46. See source_record.json.

## DGP / generation mechanism

**Sampling design:** Unit: One simulated complete observation (X_i,Y_i); Dependence: iid across rows; within each row Y is a deterministic nonlinear function of X plus an independent latent Gaussian noise before transformation.; N Semantics: n is the number of observed training-distribution rows, not the source neural-network training sample size and not the number of conditional draws at the query.

**Generator source:** [generator.py](../generators/qdi-shen-meinshausen-2025-preadditive-noise-v1.py)

**Keywords (source-described):** Nonlinearity

**Observed variables**

X, Y

**Latent variables**

eta_i

**Latent-variable identification:** candidates from equations need review

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

**Source pre-ANM (4)**

$$
Y=g(WX+\eta)+\beta^{T} X
$$

$$
\mathrm{collected} \mathrm{simulation} \mathrm{specializes} \text{ to } d=k=1,W=1,\beta=0, \mathrm{so} Y=g_{s}(X+\eta).
$$

**Independent noise and rows**

eta_i

independent of X_i

$$
(X_{i},\eta_{i}) \text{ iid } \text{ across } i
$$

$$
\eta_{i}\sim \mathcal{N}(0,\sigma_{s}^{2})
$$

$$
\sigma_{\mathrm{cubic}}=1.1, \text{ all } \mathrm{others}=1.
$$

**Covariate laws**

$$
X_{i}\sim \mathrm{Unif}[-2,2] \text{ for } \mathrm{softplus},\mathrm{cubic}
$$

$$
X_{i}\sim \mathrm{Unif}[0,2] \text{ for } \mathrm{square},\log.
$$

**Softplus**

$$
g_{\mathrm{softplus}}(u)=\ln(1+\exp(u)).
$$

**Square**

$$
g_{\mathrm{square}}(u)=\max(u,0)^{2}/2.
$$

**Cubic**

$$
g_{\mathrm{cubic}}(u)=u^{3}/3.
$$

**Log, literal table**

$$
g_{\log}(u)=(u-2)/3+\ln(3) \text{ if } u\leq 2
$$

$$
\ln(u) \text{ if } u>2
$$

Literal official supplementary Table C.1, explicitly selected by user

inspected author fixed-snapshot simulator.py line 30 differs.

**Scalar QDI target**

$$
q_{s}=\inf\{y:P_{\eta}(g_{s}(0.5+\eta)\leq y)\geq 0.5\}
$$

Source notation retained without guessing:

<pre>(q_softplus,q_square,q_cubic,q_log)=(ln(1+exp(0.5)),1/8,1/24,ln(3)-1/2).</pre>

<details>
<summary>Original source equations (verbatim)</summary>

<pre>
Y=g(WX+eta)+beta^T X; collected simulation specializes to d=k=1,W=1,beta=0, so Y=g_s(X+eta).
eta_i independent of X_i; (X_i,eta_i) iid across i; eta_i~N(0,sigma_s^2), sigma_cubic=1.1, all others=1.
X_i~Unif[-2,2] for softplus,cubic; X_i~Unif[0,2] for square,log.
g_softplus(u)=ln(1+exp(u)).
g_square(u)=max(u,0)^2/2.
g_cubic(u)=u^3/3.
g_log(u)=(u-2)/3+ln(3) if u&lt;=2; ln(u) if u&gt;2. Literal official supplementary Table C.1, explicitly selected by user; inspected author fixed-snapshot simulator.py line 30 differs.
q_s=inf{y:P_eta(g_s(0.5+eta)&lt;=y)&gt;=0.5}; (q_softplus,q_square,q_cubic,q_log)=(ln(1+exp(0.5)),1/8,1/24,ln(3)-1/2).
</pre>

</details>


## Parameter scenarios, estimands and truth

| Scenario | Estimand | Definition | True value | Evidence status |
|---|---|---|---|---|
| softplus | q_s(0.5;0.5) | For each scenario s, q_s(0.5;0.5)=inf{y:F_s(y;0.5)&gt;=0.5}, F_s(y;x)=P_eta[g_s(x+eta)&lt;=y], eta~N(0,sigma_s^2). A scalar conditional median at an interior covariate point; not a marginal quantile, causal effect, prediction interval or simultaneous band. | 0.9740769841801067 | reported_numeric |
| square | q_s(0.5;0.5) | For each scenario s, q_s(0.5;0.5)=inf{y:F_s(y;0.5)&gt;=0.5}, F_s(y;x)=P_eta[g_s(x+eta)&lt;=y], eta~N(0,sigma_s^2). A scalar conditional median at an interior covariate point; not a marginal quantile, causal effect, prediction interval or simultaneous band. | 0.125 | reported_numeric |
| cubic | q_s(0.5;0.5) | For each scenario s, q_s(0.5;0.5)=inf{y:F_s(y;0.5)&gt;=0.5}, F_s(y;x)=P_eta[g_s(x+eta)&lt;=y], eta~N(0,sigma_s^2). A scalar conditional median at an interior covariate point; not a marginal quantile, causal effect, prediction interval or simultaneous band. | 0.041666666666666664 | reported_numeric |
| log | q_s(0.5;0.5) | For each scenario s, q_s(0.5;0.5)=inf{y:F_s(y;0.5)&gt;=0.5}, F_s(y;x)=P_eta[g_s(x+eta)&lt;=y], eta~N(0,sigma_s^2). A scalar conditional median at an interior covariate point; not a marginal quantile, causal effect, prediction interval or simultaneous band. | 0.5986122886681097 | reported_numeric |

## Identifiability assumptions

- Rows (X_i,eta_i) are iid; eta independent of X; all X,Y fully observed; no clustering, panel or network dependence.
- The declared original Table C.1 transforms and nontruncated Gaussian laws are fixed. Cubic SD=1.1; other SDs=1.
- query_x=0.5 lies strictly inside every original uniform X support, with positive design density. The DGP provides a conditional-CDF version continuous in x near the query; pointwise conditional inference requires local smoothness/design assumptions, not causal exchangeability.
- Softplus/cubic are strictly increasing. Square has an atom Phi(-0.5)=0.30853753872598694 at zero for this query, below 0.5; its selected median 1/8 is in the continuous part.
- Literal Log is not globally monotone and jumps at u=2, but its selected median ln3-1/2 is below ln2. Locally only the left affine branch contributes, with continuous positive target density 3*phi(0). No current-target CDF kink or out-of-support identification problem is asserted.
- The supplement statement median=g(x) is not globally true for literal Log; at x=2, F(g(2);2)=Phi(1). Do not apply the paper global monotone extrapolation theorem blindly to square/log.
- No estimator-specific inference theory, interval coverage or named scientific acceptance is established by executable checks.

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Warnings:**

- Latent-variable candidates inferred from source equations; confirm their roles and completeness against the original paper or generator.
