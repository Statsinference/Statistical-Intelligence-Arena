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

$$
X_{i1},X_{i2}\overset{\mathrm{iid}}{\sim}U(0,1),\quad\varepsilon_i\perp X_i
$$

**E2**

$$
m(x)=\frac{40e^{8\{(x_1-0.5)^2+(x_2-0.5)^2\}}}{e^{8\{(x_1-0.2)^2+(x_2-0.7)^2\}}+e^{8\{(x_1-0.7)^2+(x_2-0.2)^2\}}}
$$

**E3**

$$
Y_i=m(X_i)+\varepsilon_i,\quad\varepsilon_i\sim\mathcal N(0,1)\;\text{or}\;t_3\;\text{or}\;0.1\mathcal N(0,25)+0.9\mathcal N(0,1)
$$

**E4**

$$
Q_\tau(x)=m(x)+F_\varepsilon^{-1}(\tau)
$$


## Parameter scenarios, estimands and truth

| Scenario | Estimand | Definition | True value | Evidence status |
|---|---|---|---|---|
| source_normal | Q_{0.1}(0.5,0.5) | Conditional 0.1 quantile at X=(0.5,0.5); normal, t3, and specified normal-mixture errors are scenarios within ONE mechanism family. | 5.787542073631004 | reported_numeric |
| source_t3 | Q_{0.1}(0.5,0.5) | Conditional 0.1 quantile at X=(0.5,0.5); normal, t3, and specified normal-mixture errors are scenarios within ONE mechanism family. | 5.431349285479395 | reported_numeric |
| source_normal_mixture | Q_{0.1}(0.5,0.5) | Conditional 0.1 quantile at X=(0.5,0.5); normal, t3, and specified normal-mixture errors are scenarios within ONE mechanism family. | 5.582372494783503 | reported_numeric |

## Identifiability assumptions

- Independent, identically distributed fully observed rows from the stated synthetic population.
- All noise variables are independent of observed covariates; coordinate dependence is exactly as stated in equations and implementation conventions.
- Quantiles use the left generalized inverse inf{y:F(y)&gt;=tau}; the selected continuous law has positive density at the registered quantile.

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Warnings:**

- Nothing automatically flagged; this does NOT equal scientific acceptance.
