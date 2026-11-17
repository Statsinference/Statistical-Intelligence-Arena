# Linear assignment and cross-product outcomes

> **Unverified extraction — scientific review required.**

**Primary area:** ATE — Average Treatment Effect

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Shujie Ma, Liping Zhu, Zhiwei Zhang, Chih-Ling Tsai and Raymond J. Carroll (2019). A robust and efficient approach to causal inference based on sparse sufficient dimension reduction. The Annals of Statistics 47(3):1505–1535. DOI 10.1214/18-AOS1722

**DOI:** 10.1214/18-aos1722 · **Source locator:** Section 7.2, PDF p.14 / journal p.1518, unnumbered Models 1 and 2 and shared X/noise paragraph; Section 7.3 PDF p.17 / journal p.1521 confirms ATE=1; collected Model 2

## DGP / generation mechanism

**Sampling design:** Unit: independent individual; Dependence: Independent individuals; AR(1) Gaussian covariance within each individual. Outcome errors and treatment randomization use independent local draws.

**Generator source:** [generator.py](../generators/ate-ma-zhu-zhang-tsai-carroll-2019-06-01-model-2-v1.py)

**Keywords (source-described):** Interactions · Nonlinearity

**Observed variables**

X1–X20 (20 variables), A, Y

<details>
<summary>All observed variable names</summary>

X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, X11, X12, X13, X14, X15, X16, X17, X18, X19, X20, A, Y

</details>

**Latent variables**

Not explicitly identified (review required)

**Latent-variable identification:** explicit structured metadata

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

$$
X\sim \mathcal{N}_{20}(0,\Sigma), \Sigma[j,k]=0.5^{\lvert j-k\rvert}
$$

independent individuals

$$
p(X)=\mathrm{expit}((X_{1}+X_{2}+X_{3})/2)
$$

$$
A\mid X\sim \mathrm{Bernoulli}(p).
$$

$$
Y=A+(X_{1}+2)\cdot (X_{2}+X_{3}+2)+\varepsilon
$$

$$
\varepsilon\sim \mathcal{N}(0,1)
$$

independent across individuals and of X/assignment randomness

<details>
<summary>Original source equations (verbatim)</summary>

<pre>
X~N_20(0,Sigma), Sigma[j,k]=0.5**abs(j-k); independent individuals.
p(X)=expit((X1+X2+X3)/2); A|X~Bernoulli(p).
Y=A+(X1+2)*(X2+X3+2)+epsilon; epsilon~N(0,1), independent across individuals and of X/assignment randomness.
</pre>

</details>


## Parameter scenarios, estimands and truth

| Scenario | Estimand | Definition | Reported value | Evidence status |
|---|---|---|---|---|
| original | ATE | ATE = E[Y(1)-Y(0)] in the full original covariate population; binary treatment 1 versus 0. | 1.0 | reported_numeric |

**Original submitted target notation:** ATE


## Identifiability assumptions

- Consistency and no interference across independent individuals.
- Treatment independent of outcome error conditional on observed X; source conditional exchangeability.
- Positive probability for each treatment at every finite X; no trimming or new clipping.

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Adaptations from the source (submitted, unverified):**

- Rename source treatment D or W to A; observed conditional law unchanged.
- Independent Python/NumPy implementation; no source estimator fitting or reported performance tables are reproduced.

**Warnings:**

- Nothing automatically flagged; this does NOT equal scientific acceptance.
