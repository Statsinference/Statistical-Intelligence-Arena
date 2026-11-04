# Binary IV: congenial complier risk difference and odds-product model

> **Unverified extraction — scientific review required.**

**Primary area:** IV — Instrumental Variables

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Wang, L., Zhang, Y., Richardson, T. S., and Robins, J. M. (2021). Estimation of local treatment effects under the binary instrumental variable model. Biometrika 108(4), 881-894. DOI 10.1093/biomet/asab003.

**DOI:** — · **Source locator:** Read version: arXiv:2007.14458v2, 22 March 2022; Section 3 Theorem 1 definitions, Section 5 numerical DGP and Table 2 alpha1 target; Supplement S1 equations S4-S5 inverse observed law. Published DOI metadata checked separately; no author code used or commit applicable.

## DGP / generation mechanism

**Sampling design:** Unit: individual; Dependence: iid individuals; principal stratum and outcome depend on X; Z independent of stratum and potential outcomes conditional on X

**Generator source:** [generator.py](../generators/iv-wang-2021-binary-complier-odds-v1.py)

**Keywords (source-described):** Nonlinearity

**Observed variables**

X, Z, D, Y

**Latent variables**

Not explicitly identified (review required)

**Latent-variable identification:** not explicitly specified

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

**Covariate and instrument**

$$
X\sim \mathrm{Uniform}(-1,1)
$$

$$
Z\mid X=x\sim \mathrm{Bernoulli}(\mathrm{expit}(0.1-x)).
$$

**Principal strata**

$$
q=\mathrm{expit}(-0.4+0.8\cdot x)
$$

$$
P(CO\mid x)=q
$$

$$
P(AT\mid x)=(1-q)\cdot q
$$

$$
P(NT\mid x)=(1-q)^{2}
$$

$$
D=Z \text{ on } CO, D=1 \text{ on } AT, D=0 \text{ on } NT.
$$

**Complier outcome probabilities**

$$
\delta=\tanh(-x)
$$

$$
OP=\exp(-0.4+x)
$$

$$
f_{1}=f_{0}+\delta
$$

$$
f_{0}\cdot f_{1}/((1-f_{0})\cdot (1-f_{1}))=OP
$$

f0 in [max(0,-delta),min(1,1-delta)].

**Observed outcome**

$$
Y\mid CO,D,x\sim \mathrm{Bernoulli}(\mathrm{fD})
$$

$$
Y\mid AT,x\sim \mathrm{Bernoulli}(q)
$$

$$
Y\mid NT,x\sim \mathrm{Bernoulli}(q)
$$

Only X,Z,D,Y are returned.

<details>
<summary>Original source equations (verbatim)</summary>

<pre>
X~Uniform(-1,1); Z|X=x~Bernoulli(expit(0.1-x)).
q=expit(-0.4+0.8*x); P(CO|x)=q; P(AT|x)=(1-q)*q; P(NT|x)=(1-q)^2; D=Z on CO, D=1 on AT, D=0 on NT.
delta=tanh(-x); OP=exp(-0.4+x); f1=f0+delta; f0*f1/((1-f0)*(1-f1))=OP; f0 in [max(0,-delta),min(1,1-delta)].
Y|CO,D,x~Bernoulli(fD); Y|AT,x~Bernoulli(q); Y|NT,x~Bernoulli(q). Only X,Z,D,Y are returned.
</pre>

</details>


## Parameter scenarios, estimands and truth

| Scenario | Estimand | Definition | True value | Evidence status |
|---|---|---|---|---|
| source_additive | alpha1 | Slope coefficient alpha1 in E[Y(1)-Y(0)\|D(1)&gt;D(0),X=x]=tanh(alpha0+alpha1*x). Target population is the complier stratum conditional on x; scalar alpha1=-1 is explicitly reported in source Table 2. It is a curve coefficient, not marginal LATE or ATE. | -1.0 | reported_numeric |

## Identifiability assumptions

- iid individuals, consistency and no interference
- Binary Z conditionally independent of potential treatments and outcomes given observed X; exclusion
- Monotonicity D(1)&gt;=D(0); source principal-stratum model includes no defiers
- Instrument overlap and positive complier probability for all x in [-1,1]
- Correct conditional LATE tanh model identifies its coefficient over nondegenerate X support

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Warnings:**

- No explicit latent-variable metadata or reliably identifiable latent declarations; absence from this list does not prove that no latent variables exist.
