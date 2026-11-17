# IV: monotone threshold compliance with Poisson principal-stratum confounding

> **Unverified extraction — scientific review required.**

**Primary area:** IV — Instrumental Variables

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Qiu, Y., Tao, J., and Zhou, X.-H. (2021). Inference of Heterogeneous Treatment Effects using Observational Data with High-Dimensional Covariates. Journal of the Royal Statistical Society Series B 83(5), 1016-1043. DOI 10.1111/rssb.12469.

**DOI:** — · **Source locator:** Publisher full-text HTML Section 2 Eq. (1) LCSTE and Assumption 1; Section 6 DGP2 Eq. (38), preceding X,Z,D generation and following fixed constants and p grid. Equation (38) MathML inspected to confirm identical Poisson subgroup additions to both potential outcomes. No author code used; fixed commit not applicable.

## DGP / generation mechanism

**Sampling design:** Unit: individual; Dependence: iid individuals; X components correlated with AR(1) covariance; latent principal stratum confounds D and Y. Independent innovations given X as explicitly adapted.

**Generator source:** [generator.py](../generators/iv-qiu-2021-principal-stratum-poisson-v1.py)

**Keywords (source-described):** Nonlinearity · High-dimensionality

**Observed variables**

X1–X200 (200 variables), Z, D, Y

<details>
<summary>All observed variable names</summary>

X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, X11, X12, X13, X14, X15, X16, X17, X18, X19, X20, X21, X22, X23, X24, X25, X26, X27, X28, X29, X30, X31, X32, X33, X34, X35, X36, X37, X38, X39, X40, X41, X42, X43, X44, X45, X46, X47, X48, X49, X50, X51, X52, X53, X54, X55, X56, X57, X58, X59, X60, X61, X62, X63, X64, X65, X66, X67, X68, X69, X70, X71, X72, X73, X74, X75, X76, X77, X78, X79, X80, X81, X82, X83, X84, X85, X86, X87, X88, X89, X90, X91, X92, X93, X94, X95, X96, X97, X98, X99, X100, X101, X102, X103, X104, X105, X106, X107, X108, X109, X110, X111, X112, X113, X114, X115, X116, X117, X118, X119, X120, X121, X122, X123, X124, X125, X126, X127, X128, X129, X130, X131, X132, X133, X134, X135, X136, X137, X138, X139, X140, X141, X142, X143, X144, X145, X146, X147, X148, X149, X150, X151, X152, X153, X154, X155, X156, X157, X158, X159, X160, X161, X162, X163, X164, X165, X166, X167, X168, X169, X170, X171, X172, X173, X174, X175, X176, X177, X178, X179, X180, X181, X182, X183, X184, X185, X186, X187, X188, X189, X190, X191, X192, X193, X194, X195, X196, X197, X198, X199, X200, Z, D, Y

</details>

**Latent variables**

e_d0, e_d1, e0, K11, K00

**Latent-variable identification:** candidates from equations need review

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

**Covariates and instrument**

```math
X\sim \mathcal{N}_{p}(0,\Sigma)
```

```math
\Sigma_{jk}=1\cdot 0.5^{\lvert j-k\rvert}
```

```math
\mathrm{gamma1}_{j}=\mathrm{gamma2}_{j}=j^{-2}
```

```math
Z\mid X\sim \mathrm{Bernoulli}(\mathrm{expit}(X'\gamma_{1}))
```

```math
p=200.
```

**Potential treatment**

```math
e_{\mathrm{d0}},e_{\mathrm{d1}}\overset{\mathrm{iid}}{\sim} \mathcal{N}(0,1)
```

```math
D_{0}=I(X'\gamma_{2}-1+e_{\mathrm{d0}}\geq 0)
```

```math
D_{1}^{\ast}=I(X'\gamma_{2}+1+e_{\mathrm{d1}}\geq 0)
```

```math
D_{1}=\max(D_{1}^{\ast},D_{0})
```

```math
D=Z D_{1}+(1-Z)D_{0}.
```

**Potential outcomes**

```math
e_{0}\sim \mathcal{N}(0,1)
```

```math
\beta_{j}=2\cdot j^{-2}
```

```math
K_{11}\sim \mathrm{Poisson}(\lambda_{11})
```

```math
K_{00}\sim \mathrm{Poisson}(0.5)
```

```math
B=X'\beta+e_{0}+K_{11}\cdot I(D_{0}=1)+K_{00}\cdot I(D_{1}=0)
```

```math
Y_{0}=B
```

```math
Y_{1}=1+B
```

```math
Y=D Y_{1}+(1-D)Y_{0}.
```

**Source scenarios**

lambda11 in {0.5,0.75,1,1.25}

no interactions

```math
\text{ source } \alpha_{0}=1.
```

<details>
<summary>Original source equations (verbatim)</summary>

<pre>
X~N_p(0,Sigma), Sigma_jk=1*0.5^|j-k|; gamma1_j=gamma2_j=j^-2; Z|X~Bernoulli(expit(X&#x27;gamma1)); p=200.
e_d0,e_d1 iid N(0,1); D0=I(X&#x27;gamma2-1+e_d0&gt;=0); D1*=I(X&#x27;gamma2+1+e_d1&gt;=0); D1=max(D1*,D0); D=Z D1+(1-Z)D0.
e0~N(0,1), beta_j=2*j^-2; K11~Poisson(lambda11), K00~Poisson(0.5); B=X&#x27;beta+e0+K11*I(D0=1)+K00*I(D1=0); Y0=B; Y1=1+B; Y=D Y1+(1-D)Y0.
lambda11 in {0.5,0.75,1,1.25}; no interactions; source alpha0=1.
</pre>

</details>


## Parameter scenarios, estimands and truth

<table>
<thead><tr><th>Scenario</th><th>Estimand</th><th>Definition</th><th>Reported value</th></tr></thead>
<tbody>
<tr>
<td>source_lambda11_0p5</td>
<td rowspan="4">LATE</td>
<td rowspan="4">

$`\mathbb{E}[Y(1)-Y(0)\mid D(1)\gt D(0)]`$

</td>
<td>1.0</td>
</tr>
<tr>
<td>source_lambda11_0p75</td>
<td>1.0</td>
</tr>
<tr>
<td>source_lambda11_1</td>
<td>1.0</td>
</tr>
<tr>
<td>source_lambda11_1p25</td>
<td>1.0</td>
</tr>
</tbody>
</table>

**Definition notes**

- All scenarios: Population complier effect.

<details>
<summary>Submitted estimand definitions</summary>

Submitted English definitions appear below; other original-language definitions remain in the linked JSON. Concise formulas above are display interpretations and still require scientific review.

**Scenario(s):** source_lambda11_0p5, source_lambda11_0p75, source_lambda11_1, source_lambda11_1p25

E[Y(1)-Y(0)\|D(1)&gt;D(0)]=1 in source DGP2 without treatment-covariate interactions. LCSTE(x)=1 for every x; alpha0 is the treatment coefficient directly evaluated in source Section 6. This is an IV complier estimand despite the paper's heterogeneous-effects title.

[Open raw scientific record (JSON)](./iv-qiu-2021-principal-stratum-poisson-v1.json).

</details>


**Original submitted target notation:** alpha0 = LATE


## Identifiability assumptions

- iid individuals, consistency and no interference
- Z independent of treatment and potential outcome innovations conditional on X; exclusion
- D(1)=max(D*(1),D(0)) ensures monotonicity
- Conditional instrument probability expit(X'gamma) strictly between 0 and 1 and complier probability positive for finite X
- No uniform lower-overlap bound claimed for unbounded Gaussian X; finite-sample estimators may face extreme scores

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Adaptations from the source (submitted, unverified):**

- Select source DGP2 without interaction and p=200 from source p=50,100,200,300,400,500; retain all four lambda11 source scenarios as one family.
- Return source alpha0=1, equal to constant complier local treatment effect and LATE without interaction; no new fixed-x or policy target is introduced.
- Implement Gaussian AR(1) covariance and iid threshold/noise/Poisson innovations using independently written NumPy, without author seed equivalence.
- Draw the generated Poisson innovations independently of X, treatment errors, outcome noise, instrument randomization and each other, spelling out the standard independent-draw reading of Section 6; no author software was available to check unreported coupling. Contrast truth is invariant to coupling because subgroup shifts are identical in both potentials.
- Omit estimation, penalty selection, 1000 replications and CIs; n and seed supplied by caller.

**Warnings:**

- Latent-variable candidates inferred from source equations; confirm their roles and completeness against the original paper or generator.
