# Conditional CDF in Hall-Wolff-Yao sine regression with triangular noise

> **Unverified extraction — scientific review required.**

**Primary area:** Quantile Inference

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Hall, Peter; Wolff, Rodney C. L.; Yao, Qiwei (1999). Methods for Estimating a Conditional Distribution Function. Journal of the American Statistical Association 94(445), 154-163. DOI: 10.1080/01621459.1999.10473832.

**DOI:** 10.1080/01621459.1999.10473832 · **Source locator:** Version of record, supplied 11-page PDF (publisher cover is PDF p.1): Section 3.1 Simulation Studies, Example 1 first paragraph and unnumbered DGP equation, PDF p.4 / journal p.156. Equation (4) on that page is a bandwidth criterion, not this DGP. Example 1 continuation and Figure 1: PDF p.5 / journal p.157. Figure 2(d), x=0.1: PDF p.6 / journal p.158. Section 4 C1-C4 and Remark 1: PDF p.7 / journal p.159. Accepted-manuscript comparison locators are separately recorded below.

## DGP / generation mechanism

**Sampling design:** Unit: one observed pair (X_i,Y_i); Dependence: iid across rows; X_i independent of epsilon_i, while Y_i depends nonlinearly on X_i; no time-series or clustering structure in Example 1; Source Sample Size: 600; Source Replications: {'optimal_bandwidth_stage': 400, 'bootstrap_bandwidth_stage': 200}; N Semantics: n is the number of observed iid pairs requested by generate; seed is an implementation choice, not an original-paper seed

**Generator source:** [generator.py](../generators/qdi-hall-wolff-yao-1999-sine-triangular-v1.py)

**Keywords (source-described):** Nonlinearity

**Observed variables**

X, Y

**Latent variables**

U_i4

**Latent-variable identification:** candidates from equations need review

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

$$
X_i iid \sim f_T
$$

$$
\varepsilon_i iid \sim f_T
$$

{X_i}

independent of {epsilon_i}

$$
f_T(u)=(1-|u|)1\{-1<=u<=1\}.
$$

$$
Y_i = 2\cdot \sin(3.1416\cdot X_i) + \varepsilon_i.
$$

For independent U_i1,...,U_i4 ~ Uniform(0,1): X_i=U_i1-U_i2

epsilon_i=U_i3-U_i4. Only X_i,Y_i are exported.

$$
F(y\mid x)=G(z)
$$

$$
z=y-2\cdot \sin(3.1416\cdot x)
$$

$$
G(z)=0 for z<=-1
$$

$$
(1+z)^{2}/2 for -1<z<=0
$$

$$
1-(1-z)^{2}/2 for 0<z<1
$$

$$
1 for z>=1.
$$

$$
\theta=F(1\mid 0.1)=1-2\cdot \sin(0.31416)^{2}=0.8090161307517588 (binary64 evaluation).
$$

<details>
<summary>Original source equations (verbatim)</summary>

<pre>
X_i iid ~ f_T; epsilon_i iid ~ f_T; {X_i} independent of {epsilon_i}; f_T(u)=(1-|u|)1{-1&lt;=u&lt;=1}.
Y_i = 2*sin(3.1416*X_i) + epsilon_i.
For independent U_i1,...,U_i4 ~ Uniform(0,1): X_i=U_i1-U_i2; epsilon_i=U_i3-U_i4. Only X_i,Y_i are exported.
F(y|x)=G(z), z=y-2*sin(3.1416*x); G(z)=0 for z&lt;=-1; (1+z)^2/2 for -1&lt;z&lt;=0; 1-(1-z)^2/2 for 0&lt;z&lt;1; 1 for z&gt;=1.
theta=F(1|0.1)=1-2*sin(0.31416)^2=0.8090161307517588 (binary64 evaluation).
</pre>

</details>


## Parameter scenarios, estimands and truth

| Scenario | Estimand | Definition | True value | Evidence status |
|---|---|---|---|---|
| original_mechanism_fixed_cdf | theta = F_{Y\|X=0.1}(1) | P(Y&lt;=1 \| X=0.1) in the Example 1 superpopulation, using the continuous version F(y\|x)=G(y-2*sin(3.1416*x)) induced by independent triangular noise. Conditional CDF, not a marginal CDF, quantile, conditional mean, causal contrast, or prediction interval. Query x=0.1 and CDF threshold y=1 are fixed in config. | 0.8090161307517588 | reported_numeric |

## Identifiability assumptions

- Sampling: {(X_i,epsilon_i)} are iid across rows; the X and epsilon sequences are mutually independent, exactly as Example 1 specifies.
- Observation: X and Y are fully observed numeric variables; there is no missingness, label selection, censoring or measurement-error mechanism.
- Conditional-law identification: independent additive noise gives F(y\|x)=G(y-m(x)). As P(X=0.1)=0, the target uses the continuous conditional-distribution version determined by this model; continuity and positive design density near the query select its point value.
- Local regularity: f_X(0.1)=0.9&gt;0 and z=1-m(0.1) lies strictly inside (0,1), away from the triangular mode and support knots. Thus 0&lt;F&lt;1 and F(1\|x) is smooth in a neighborhood of x=0.1. No global smoothness at the triangular knots or uniform density lower bound near support endpoints is asserted.
- Source Section 4 C1-C4 are estimator-specific regularity/kernel/bandwidth/dependence conditions. iid rows satisfy its absolute-regularity component; no fitted estimator, bandwidth asymptotics, or confidence-band result is validated here. No causal exchangeability or intervention assumptions apply.

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Warnings:**

- Latent-variable candidates inferred from source equations; confirm their roles and completeness against the original paper or generator.
