# Pointwise conditional mean in the Wang-Yang (2007) d=30 additive heteroscedastic design

> **Unverified extraction — scientific review required.**

**Primary area:** Nonparametric Regression

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Wang, L. and Yang, L. (2007). Spline-backfitted kernel smoothing of nonlinear additive autoregression model. The Annals of Statistics 35(6), 2474-2503. DOI: 10.1214/009053607000000488.

**DOI:** — · **Source locator:** Section starts: Section 6 on PDF p.14, Section Example 6.2 on PDF p.18. Unnumbered paragraph on PDF p.18: "Consider the nonlinear additive heteroscedastic model" (Example6.2 mean, signed heteroscedastic scale, truncated-normal design and experiment parameters). All PDF pages are 1-based pages of the fixed reading file math/0612677v5. No printed journal page is inferred by adding an offset.

## DGP / generation mechanism

**Sampling design:** Unit: observation row (one simulated time index t together with its 30 covariate coordinates X1..X30); Dependence: Under the declared lag-window interpretation, rows at distance at least d=30 use disjoint innovations and covariate draws; adjacent rows share 29 coordinates. Consecutive length-30 blocks still overlap in their underlying covariate draws and are not independent. There is no statistic-independent effective sample size.

**Generator source:** [generator.py](../generators/nri-wangyang-2007-hdadditive-v1.py)

**Keywords (source-described):** Nonlinearity

**Observed variables**

X1–X30 (30 variables), Y

<details>
<summary>All observed variable names</summary>

X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, X11, X12, X13, X14, X15, X16, X17, X18, X19, X20, X21, X22, X23, X24, X25, X26, X27, X28, X29, X30, Y

</details>

**Latent variables**

Z_s

**Latent-variable identification:** candidates from equations need review

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

**1. Scalar stream**

$$
Z_{s}\overset{\mathrm{iid}}{\sim} \mathcal{N}(0,1) \mathrm{conditional} \text{ on } -2.5\leq Z_{s}\leq 2.5, s=0..n+29-1
$$

rejection sampling

$$
\mathrm{sd}=1 \mathrm{before} \mathrm{truncation}
$$

One scalar truncated-normal stream

$$
\text{ source } d=30, \mathrm{bound}=2.5.
$$

**2. Lag window**

$$
X_{t}=(Z_{t+29},Z_{t+28},\ldots ,Z_{t}), t=0..n-1
$$

X1 is the most recent lag

Deterministic window

no new noise

Adjacent rows share 29 stream values.

**3. Mean and scale**

$$
m(X)=\sum_{\text{ a }=1}^{30} \sin(\pi\cdot X_{a}/2.5)
$$

$$
L=\text{ mean }(\lvert X_{a}\rvert)
$$

$$
\sigma(X)=0.1\cdot (\sqrt{30}/2)\cdot (5-\exp(L))/(5+\exp(L))
$$

Deterministic

signed source multiplier retained

Divisor 2 is outside the radical.

**4. Innovation**

$$
\varepsilon_{t}\overset{\mathrm{iid}}{\sim} \mathcal{N}(0,1)
$$

independent of the scalar stream and other innovations

$$
\mathrm{Noise} \mathrm{sd}=1 \mathrm{before} \mathrm{multiplication} \text{ by } \sigma(X).
$$

**5. Outcome and columns**

$$
Y_{t}=m(X_{t})+\sigma(X_{t})\cdot \varepsilon_{t}
$$

return X1..X30,Y in chronological window order

$$
\mathrm{Conditional} \text{ variance }=\sigma(X_{t})^{2}
$$

no latent/noiseless column is exported.

<details>
<summary>Original source equations (verbatim)</summary>

<pre>
Z_s iid N(0,1) conditional on -2.5&lt;=Z_s&lt;=2.5, s=0..n+29-1; rejection sampling; sd=1 before truncation. One scalar truncated-normal stream; source d=30, bound=2.5.
X_t=(Z_(t+29),Z_(t+28),...,Z_t), t=0..n-1; X1 is the most recent lag. Deterministic window; no new noise. Adjacent rows share 29 stream values.
m(X)=sum_(a=1)^30 sin(pi*X_a/2.5); L=mean(abs(X_a)); sigma(X)=0.1*(sqrt(30)/2)*(5-exp(L))/(5+exp(L)). Deterministic; signed source multiplier retained. Divisor 2 is outside the radical.
epsilon_t iid N(0,1), independent of the scalar stream and other innovations. Noise sd=1 before multiplication by sigma(X).
Y_t=m(X_t)+sigma(X_t)*epsilon_t; return X1..X30,Y in chronological window order. Conditional variance=sigma(X_t)^2; no latent/noiseless column is exported.
</pre>

</details>


## Parameter scenarios, estimands and truth

| Scenario | Estimand | Definition | Reported value | Evidence status |
|---|---|---|---|---|
| original-sigma01 | Pointwise conditional mean | Scalar conditional mean of Y at a fixed 30-dimensional query point x0 in the superpopulation defined by the fixed Example 6.2 DGP. It is a pointwise regression functional, not a causal effect; the query is a parameter of each scenario and is read from config by truth(config). | 1.0 | reported_numeric |
| origin-query | Pointwise conditional mean | Scalar conditional mean of Y at a fixed 30-dimensional query point x0 in the superpopulation defined by the fixed Example 6.2 DGP. It is a pointwise regression functional, not a causal effect; the query is a parameter of each scenario and is read from config by truth(config). | 0.0 | reported_numeric |

**Original submitted target notation:** m(x0) = E[Y \| X = x0] = sum_{alpha=1}^{30} sin(pi * x0_alpha / 2.5)


## Identifiability assumptions

- The displayed lag subscripts are interpreted as one shared iid truncated-normal stream, independent of the iid N(0,1) innovations.
- The query is fixed inside the 30-dimensional truncated-normal support.
- The noise multiplier may have either sign; conditional variance is its square and conditional mean is zero.
- Pointwise truth does not imply an estimator or coverage result; the source's unspecified cross-row sampling algorithm remains an interpretation boundary.

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Adaptations from the source (submitted, unverified):**

- Read the displayed X_{t-alpha} subscripts consistently across rows as overlapping windows of one iid truncated-normal stream. This is the declared interpretation of the source notation; no claim is made that an author implementation has been recovered.
- Replace component-estimator comparisons by scalar m(x0)=E[Y\|X=x0]; x0=(1.25,0,...,0) and the zero vector are our choices.
- Implement truncation by rejection sampling; retain the source's signed noise multiplier without clipping.
- For the shared-stream interpretation, use exact overlap counts for signal variance of the whole-table mean and conditional noise variance; adjacent length-d blocks are dependent, and no universal n/d effective sample size is assumed.
- Use interface sample sizes and CPU checks without fitting the source estimators.

**Warnings:**

- Latent-variable candidates inferred from source equations; confirm their roles and completeness against the original paper or generator.
