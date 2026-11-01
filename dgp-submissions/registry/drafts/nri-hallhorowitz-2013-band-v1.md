# Pointwise conditional-mean query at a fixed interior design point in the Hall and Horowitz (2013) univariate smooth regression design

> **Unverified extraction — scientific review required.**

**Primary area:** Nonparametric Regression

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Hall, P. and Horowitz, J. L. (2013). A simple bootstrap method for constructing nonparametric confidence bands for functions. The Annals of Statistics 41(4), 1892-1921. DOI: 10.1214/13-AOS1137.

**DOI:** — · **Source locator:** Formula bodies: (2.1) on PDF p.4. Section starts: Section 2.1 on PDF p.4, Section 3 on PDF p.13, Section 3.1 on PDF p.13, Section 3.2 on PDF p.14. Unnumbered paragraph on PDF p.13: "For n = 100, 200 or 400" (three g functions, n, sigma, distribution and repetition parameters). Unnumbered paragraph on PDF p.14: "a proportion of values" (evaluation interval [-0.9,0.9]). All PDF pages are 1-based pages of the fixed reading file 1309.4864v1. No printed journal page is inferred by adding an offset.

## DGP / generation mechanism

**Sampling design:** Unit: One scalar covariate/outcome pair (X_i, Y_i), one observation per independent unit; Dependence: iid across i with no within-cluster correlation; X_i is drawn independently of epsilon_i, so observations share nothing beyond the fixed DGP parameters

**Generator source:** [generator.py](../generators/nri-hallhorowitz-2013-band-v1.py)

**Keywords (source-described):** Nonlinearity

**Observed variables**

X, Y

**Latent variables**

Not explicitly identified (review required)

**Latent-variable identification:** not explicitly specified

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

$$
X_i\overset{\mathrm{iid}}{\sim} \mathrm{Uniform}(-1,1). Source support -1..1
$$

one scalar covariate per row.

$$
g_{1}(x)=x+5\cdot \exp(-50\cdot x^{2})/sqrt(2\cdot \pi)
$$

$$
g_{2}(x)=\sin(3\cdot \pi\cdot x/2)/(1+18\cdot x^{2}\cdot (sgn(x)+1))
$$

$$
g_{3}(x)=\sin(\pi\cdot x/2)/(1+2\cdot x^{2}\cdot (sgn(x)+1)). Deterministic
$$

$$
sgn(x)=-1/0/1 for x<0/=0/>0. All coefficients are from the source unnumbered functions.
$$

$$
\varepsilon_i\overset{\mathrm{iid}}{\sim} \mathcal{N}(0,\sigma^{2}), independent of X
$$

$$
registered pairs are (g_{1},\sigma=1),(g_{2},0.5),(g_{3},0.2). \sigma is a standard deviation, not a variance
$$

the source has a full 3-by-3 design.

$$
Y_i=g_j(X_i)+\varepsilon_i
$$

return X,Y. No extra noise, latent mean or oracle column.

<details>
<summary>Original source equations (verbatim)</summary>

<pre>
X_i iid Uniform(-1,1). Source support -1..1; one scalar covariate per row.
g1(x)=x+5*exp(-50*x^2)/sqrt(2*pi); g2(x)=sin(3*pi*x/2)/(1+18*x^2*(sgn(x)+1)); g3(x)=sin(pi*x/2)/(1+2*x^2*(sgn(x)+1)). Deterministic; sgn(x)=-1/0/1 for x&lt;0/=0/&gt;0. All coefficients are from the source unnumbered functions.
epsilon_i iid N(0,sigma^2), independent of X; registered pairs are (g1,sigma=1),(g2,0.5),(g3,0.2). sigma is a standard deviation, not a variance; the source has a full 3-by-3 design.
Y_i=g_j(X_i)+epsilon_i; return X,Y. No extra noise, latent mean or oracle column.
</pre>

</details>


## Parameter scenarios, estimands and truth

| Scenario | Estimand | Definition | True value | Evidence status |
|---|---|---|---|---|
| g1-sigma1 | m(x0) = E[Y \| X = x0] = g_j(x0) | The value of the conditional mean function at one fixed interior design point x0 specified per scenario, in the superpopulation defined by the declared regression model with X uniform on [-1,1] and additive N(0, sigma^2) noise. This is a pointwise scalar query, not a simultaneous confidence band and not a coverage claim over any interval. | 1.9947114020071635 | reported_numeric |
| g2-sigma05 | m(x0) = E[Y \| X = x0] = g_j(x0) | The value of the conditional mean function at one fixed interior design point x0 specified per scenario, in the superpopulation defined by the declared regression model with X uniform on [-1,1] and additive N(0, sigma^2) noise. This is a pointwise scalar query, not a simultaneous confidence band and not a coverage claim over any interval. | 0.23294536334790983 | reported_numeric |
| g3-sigma02 | m(x0) = E[Y \| X = x0] = g_j(x0) | The value of the conditional mean function at one fixed interior design point x0 specified per scenario, in the superpopulation defined by the declared regression model with X uniform on [-1,1] and additive N(0, sigma^2) noise. This is a pointwise scalar query, not a simultaneous confidence band and not a coverage claim over any interval. | 0.3535533905932738 | reported_numeric |

## Identifiability assumptions

- Independent and identically distributed pairs (X_i, Y_i); no clustering, serial dependence, spatial or network interference is present.
- X_i is drawn uniformly on [-1,1], so its density is bounded away from zero at every interior query point used here and local smoothing has design points on both sides of x0.
- epsilon_i ~ N(0, sigma^2) is independent of X_i and additive, so no correction for heteroskedasticity, measurement error or endogenous regressors is required to identify E[Y \| X = x0].
- g_j is bounded on [-1,1] and smooth enough for the local-polynomial regularity assumed in Section 2 of the source; g2 and g3 are continuous at x = 0 where the sign convention switches.
- The query point x0 is fixed interior to the support and chosen before seeing data; pointwise verification at one or several x0 does not establish simultaneous coverage over the source evaluation interval [-0.9, 0.9].
- This is a non-causal regression target: no intervention, exposure, exchangeability or counterfactual consistency assumption is claimed.

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Warnings:**

- No explicit latent-variable metadata or reliably identifiable latent declarations; absence from this list does not prove that no latent variables exist.
