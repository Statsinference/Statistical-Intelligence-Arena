# Conditional quantile in the Dette-Volgushev exponentially scaled exponential-error mechanism

> **Unverified extraction — scientific review required.**

**Primary area:** Quantile Inference

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Dette, H. and Volgushev, S. (2008). Non-crossing non-parametric estimates of quantile curves. Journal of the Royal Statistical Society Series B 70(3), 609-627. DOI: 10.1111/j.1467-9868.2008.00651.x.

**DOI:** 10.1111/j.1467-9868.2008.00651.x · **Source locator:** Read version: discussion paper dated 2007-05-08, Section 4.2, equation (4.5), model 4; PDF page 13 including EconStor cover = printed preprint page 12. The later journal pagination 609-627 is NOT the locator for this read version.

## DGP / generation mechanism

**Sampling design:** Unit: One fully observed independent row (X,Y); Dependence: IID rows; coordinate and noise independence as recorded in equations and source adaptations.

**Generator source:** [generator.py](../generators/qdi-dette-volgushev-2008-exponential-scale-v1.py)

**Keywords (source-described):** Nonlinearity · Heteroskedasticity

**Observed variables**

X1, Y

**Latent variables**

Not explicitly identified (review required)

**Latent-variable identification:** explicit structured metadata

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

**Original source equations (verbatim):** [Open raw scientific record (JSON)](./qdi-dette-volgushev-2008-exponential-scale-v1.json).

**E1**

$$
X_i\sim U(0,5),\quad E_i\sim\operatorname{Exp}(\mathrm{rate}=1),\quad X_i\perp E_i
$$

**E2**

$$
Y_i=2+X_i+e^{-X_i}\{E_i-\log(2.6)\}
$$

**E3**

$$
Q_\tau(x)=2+x+e^{-x}\{-\log(1-\tau)-\log(2.6)\}
$$


## Parameter scenarios, estimands and truth

| Scenario | Estimand | Definition | True value | Evidence status |
|---|---|---|---|---|
| source_law_fixed_query | Q_{0.9}(2) | Conditional 0.9 quantile at X=2, according to the explicitly dated preprint model 4. | 4.182306593688138 | reported_numeric |

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
