# Conditional quantile in the Bondell-Reich-Wang sine-location mechanism

> **Unverified extraction — scientific review required.**

**Primary area:** Quantile Inference

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Bondell, H. D., Reich, B. J. and Wang, H. (2010). Noncrossing quantile regression curve estimation. Biometrika 97(4), 825-838. DOI: 10.1093/biomet/asq048.

**DOI:** 10.1093/biomet/asq048 · **Source locator:** Section 4.2, Example 4; PDF page 9 = journal page 833; unnumbered Y=f(X)+g(X)*epsilon model and immediately following example.

## DGP / generation mechanism

**Sampling design:** Unit: One fully observed independent row (X,Y); Dependence: IID rows; coordinate and noise independence as recorded in equations and source adaptations.

**Generator source:** [generator.py](../generators/qdi-bondell-reich-wang-2010-sine-location-v2.py)

**Keywords (source-described):** Nonlinearity

**Observed variables**

X1, Y

**Latent variables**

Not explicitly identified (review required)

**Latent-variable identification:** explicit structured metadata

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

**Original source equations (verbatim):** [Open raw scientific record (JSON)](./qdi-bondell-reich-wang-2010-sine-location-v2.json).

**E1**

$$
X_i\sim U(0,1),\quad\varepsilon_i\sim\mathcal N(0,1),\quad X_i\perp\varepsilon_i
$$

The displayed marginals are source-supported; the independence/product-sampling part is a declared implementation convention. See source_recheck.json.

**E2**

$$
Y_i=0.5+2X_i+\sin(2\pi X_i-0.5)+\varepsilon_i
$$

**E3**

$$
Q_\tau(x)=m(x)+s(x)\Phi^{-1}(\tau)
$$


## Parameter scenarios, estimands and truth

| Scenario | Estimand | Definition | Reported value | Evidence status |
|---|---|---|---|---|
| source_law_fixed_query | Conditional quantile | Conditional 0.9 quantile at X=0.5 in source Example 4. | 3.260977104148804 | reported_numeric |

**Original submitted target notation:** Q_{0.9}(0.5)


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

- Fixed x=0.5 and tau=0.9 select one scalar query from source curves; the data-generating coefficients are retained.
- The source calls g a variance function but multiplies epsilon by g. This implementation follows the displayed equation: g is the conditional standard deviation and Var(Y\|X)=g^2. Independence of X and epsilon and iid rows are explicit implementation conventions.
- Independent Python/NumPy implementation from mathematical formulas; no author code is redistributed. PCG64(seed) replaces unspecified/source software random-number generation. Sample size is the generate n argument; source_n only records the published sample sizes. No fitting, bootstrap, confidence-band coverage experiment or PFN training is included.
- Clarified that generation constants are specified jointly in the displayed equations and config.json; not every fixed source constant is exposed as a configurable parameter.
- Source recheck did not turn the disclosed independence completion into a source fact. Marginal laws and equations match the read source, while the implementation product law still needs a maintainer decision before claiming a fully source-verified joint DGP.

**Warnings:**

- Nothing automatically flagged; this does NOT equal scientific acceptance.
