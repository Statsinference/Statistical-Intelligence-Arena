# Conditional quantiles on the Li-Liu-Zhu exponential surface with non-Gaussian noise scenarios

> **Unverified extraction — scientific review required.**

**Primary area:** Quantile Inference

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Li, Y., Liu, Y. and Zhu, J. (2007). Quantile Regression in Reproducing Kernel Hilbert Spaces. Journal of the American Statistical Association 102(477), 255-268. DOI: 10.1198/016214506000000979.

**DOI:** 10.1198/016214506000000979 · **Source locator:** Section 5.1, equation (40) and following error-distribution paragraph; PDF page 8 = journal page 262. Section 5.2 on PDF page 9 = journal page 263 reuses this law.

## DGP / generation mechanism

**Sampling design:** Unit: One fully observed independent row (X,Y); Dependence: IID rows; coordinate and noise independence as recorded in equations and source adaptations.

**Generator source:** [generator.py](../generators/qdi-li-liu-zhu-2007-exponential-surface-v1.py)

**Keywords (source-described):** Interactions · Nonlinearity

**Observed variables**

X1, X2, Y

**Latent variables**

Not explicitly identified (review required)

**Latent-variable identification:** explicit structured metadata

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

**Original source equations (verbatim):** [Open raw scientific record (JSON)](./qdi-li-liu-zhu-2007-exponential-surface-v1.json).

**E1**

```math
X_{i1},X_{i2}\overset{\mathrm{iid}}{\sim}U(0,1),\quad\varepsilon_i\perp X_i
```

**E2**

```math
m(x)=\frac{40e^{8\{(x_1-0.5)^2+(x_2-0.5)^2\}}}{e^{8\{(x_1-0.2)^2+(x_2-0.7)^2\}}+e^{8\{(x_1-0.7)^2+(x_2-0.2)^2\}}}
```

**E3**

```math
Y_i=m(X_i)+\varepsilon_i,\quad\varepsilon_i\sim\mathcal N(0,1)\;\text{or}\;t_3\;\text{or}\;0.1\mathcal N(0,25)+0.9\mathcal N(0,1)
```

**E4**

```math
Q_\tau(x)=m(x)+F_\varepsilon^{-1}(\tau)
```


## Parameter scenarios, estimands and truth

<table>
<thead><tr><th>Scenario</th><th>Estimand</th><th>Definition</th><th>Reported value</th></tr></thead>
<tbody>
<tr>
<td>source_normal</td>
<td rowspan="3">Conditional quantile</td>
<td rowspan="3">

$`Q_{0.1}(Y\mid X=(0.5,0.5))`$

</td>
<td>5.787542073631004</td>
</tr>
<tr>
<td>source_t3</td>
<td>5.431349285479395</td>
</tr>
<tr>
<td>source_normal_mixture</td>
<td>5.582372494783503</td>
</tr>
</tbody>
</table>

<details>
<summary>Submitted estimand definitions</summary>

Submitted English definitions appear below; other original-language definitions remain in the linked JSON. Concise formulas above are display interpretations and still require scientific review.

**Scenario(s):** source_normal, source_t3, source_normal_mixture

Conditional 0.1 quantile at X=(0.5,0.5); normal, t3, and specified normal-mixture errors are scenarios within ONE mechanism family.

[Open raw scientific record (JSON)](./qdi-li-liu-zhu-2007-exponential-surface-v1.json).

</details>


**Original submitted target notation:** Q_{0.1}(0.5,0.5)


## Identifiability assumptions

- Independent, identically distributed fully observed rows from the stated synthetic population.
- All noise variables are independent of observed covariates; coordinate dependence is exactly as stated in equations and implementation conventions.
- Quantiles use the left generalized inverse inf{y:F(y)&gt;=tau}; the selected continuous law has positive density at the registered quantile.

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Adaptations from the source (submitted, unverified):**

- Fixed x=(0.5,0.5) and tau=0.1 select a scalar query. Normal, unscaled Student t3 and the stated normal mixture are three source noise scenarios, not three different families.
- The unspecified scale of the source double-exponential error is not guessed; that fourth noise case is excluded. Independent X1,X2, noise and rows are explicit implementation conventions because the paragraph states marginal distributions only.
- The computationally equivalent log-sum-exp form avoids unnecessary exponential overflow; no negative signs are inserted in the positive exponents in equation (40).
- Independent Python/NumPy implementation from mathematical formulas; no author code is redistributed. PCG64(seed) replaces unspecified/source software random-number generation. Sample size is the generate n argument; source_n only records the published sample sizes. No fitting, bootstrap, confidence-band coverage experiment or PFN training is included.

**Warnings:**

- Nothing automatically flagged; this does NOT equal scientific acceptance.
