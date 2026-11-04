# Conditional quantile in the Li-Liu-Zhu sinc demonstration mechanism

> **Unverified extraction — scientific review required.**

**Primary area:** Quantile Inference

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Li, Y., Liu, Y. and Zhu, J. (2007). Quantile Regression in Reproducing Kernel Hilbert Spaces. Journal of the American Statistical Association 102(477), 255-268. DOI: 10.1198/016214506000000979.

**DOI:** 10.1198/016214506000000979 · **Source locator:** Section 1, illustrative solution-path example; PDF page 2 = journal page 256; unnumbered sinc model in left column, six training observations.

## DGP / generation mechanism

**Sampling design:** Unit: One fully observed independent row (X,Y); Dependence: IID rows; coordinate and noise independence as recorded in equations and source adaptations.

**Generator source:** [generator.py](../generators/qdi-li-liu-zhu-2007-sinc-v2.py)

**Keywords (source-described):** Nonlinearity

**Observed variables**

X1, Y

**Latent variables**

Not explicitly identified (review required)

**Latent-variable identification:** explicit structured metadata

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

**Original source equations (verbatim):** [Open raw scientific record (JSON)](./qdi-li-liu-zhu-2007-sinc-v2.json).

**E1**

$$
X_i\sim U(-2,2),\quad\varepsilon_i\sim\mathcal N(0,0.2^2),\quad X_i\perp\varepsilon_i
$$

The displayed marginals are source-supported; the independence/product-sampling part is a declared implementation convention. See source_recheck.json.

**E2**

$$
Y_i=\frac{\sin(\pi X_i)}{\pi X_i}+\varepsilon_i,\quad \operatorname{sinc}(0)=1
$$

**E3**

$$
Q_\tau(x)=\operatorname{sinc}(x)+0.2\Phi^{-1}(\tau)
$$


## Parameter scenarios, estimands and truth

| Scenario | Estimand | Definition | True value | Evidence status |
|---|---|---|---|---|
| source_law_fixed_query | Q_{0.9}(0.5) | Conditional 0.9 quantile at X=0.5, using the sinc data law of the Section 1 demonstration. | 0.8929300854765015 | reported_numeric |

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
