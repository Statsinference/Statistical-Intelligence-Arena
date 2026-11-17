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

```math
X_i\sim U(0,5),\quad E_i\sim\mathrm{Exp}(\mathrm{rate}=1),\quad X_i\perp E_i
```

**E2**

```math
Y_i=2+X_i+e^{-X_i}\{E_i-\log(2.6)\}
```

**E3**

```math
Q_\tau(x)=2+x+e^{-x}\{-\log(1-\tau)-\log(2.6)\}
```


## Parameter scenarios, estimands and truth

| Scenario | Estimand | Definition | Reported value |
|---|---|---|---|
| source_law_fixed_query | Conditional quantile | Conditional 0.9 quantile at X=2, according to the explicitly dated preprint model 4. | 4.182306593688138 |

**Original submitted target notation:** Q_{0.9}(2)


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

- The mechanism is transcribed from the dated 2007-05-08 preprint associated with the 2008 JRSS-B publication. The preprint attributes this model to Yu and Jones (1998). This lineage is recorded to prevent duplicate counting across papers.
- The 2008 typeset simulation formulas have not been compared line by line; no equality of all preprint and final-version formulas is asserted. Published bibliographic metadata and the actual read-version locator are kept separate.
- Fixed x=2 and tau=0.9 define a scalar query. Independent X and E and iid rows are explicit implementation conventions. The offset is exactly log(2.6), not log(2).
- Independent Python/NumPy implementation from mathematical formulas; no author code is redistributed. PCG64(seed) replaces unspecified/source software random-number generation. Sample size is the generate n argument; source_n only records the published sample sizes. No fitting, bootstrap, confidence-band coverage experiment or PFN training is included.

**Warnings:**

- Nothing automatically flagged; this does NOT equal scientific acceptance.
