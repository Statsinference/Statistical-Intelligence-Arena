# ATE under Nie--Wager Setup A: nonlinear confounding and heterogeneous effects

> **Unverified extraction — scientific review required.**

**Primary area:** ATE — Average Treatment Effect

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Nie, X. and Wager, S. (2021). Quasi-oracle estimation of heterogeneous treatment effects. Biometrika 108(2), 299-319. DOI: 10.1093/biomet/asaa076.

**DOI:** — · **Source locator:** arXiv v4 PDF pp. 15-16, Section 6.1, unnumbered common generation equations and Setup A; p. 18 Figure 3 caption for d=6 and sigma=1. Author repository experiments_for_paper/run_simu.R lines 25-32, 75-77 and start.sh lines 3-6 at commit 6806396960e672214e2ef36e16c76bbb58ef9114

## DGP / generation mechanism

**Sampling design:** Unit: individual; Dependence: iid across individuals; six independent Uniform(0,1) covariates within each individual

**Generator source:** [generator.py](../generators/ate-nie-wager-2021-a-v1.py)

**Keywords (source-described):** Interactions · Nonlinearity · Effect heterogeneity

**Observed variables**

X1–X6 (6 variables), A, Y

<details>
<summary>All observed variable names</summary>

X1, X2, X3, X4, X5, X6, A, Y

</details>

**Latent variables**

Not explicitly identified (review required)

**Latent-variable identification:** not explicitly specified

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

**Covariates**

```math
X_{j}\overset{\mathrm{iid}}{\sim} \mathrm{Uniform}(0,1), j=1,\ldots ,6
```

**Baseline**

```math
b(X)=\sin(\pi\cdot X_{1}\cdot X_{2})+2\cdot (X_{3}-0.5)^{2}+X_{4}+0.5\cdot X_{5}
```

**Treatment**

```math
e(X)=\max(0.1,\min(\sin(\pi\cdot X_{1}\cdot X_{2}),0.9))
```

```math
A\mid X\sim \mathrm{Bernoulli}(e(X))
```

**Conditional effect**

```math
\tau(X)=(X_{1}+X_{2})/2
```

**Outcome**

```math
Y=b(X)+(A-0.5)\cdot \tau(X)+\varepsilon
```

```math
\varepsilon\sim \mathcal{N}(0,1)
```

independent of X and treatment randomization

<details>
<summary>Original source equations (verbatim)</summary>

<pre>
X_j iid Uniform(0,1), j=1,...,6
b(X)=sin(pi*X1*X2)+2*(X3-0.5)^2+X4+0.5*X5
e(X)=max(0.1,min(sin(pi*X1*X2),0.9)); A|X~Bernoulli(e(X))
tau(X)=(X1+X2)/2
Y=b(X)+(A-0.5)*tau(X)+epsilon; epsilon~Normal(0,1), independent of X and treatment randomization
</pre>

</details>


## Parameter scenarios, estimands and truth

| Scenario | Estimand | Definition | Reported value |
|---|---|---|---|
| original_d6_sigma1 | ATE | Superpopulation average effect of A=1 versus A=0, under X~Uniform([0,1]^6). Not the realized-sample average effect, ATT, CATE output, or unadjusted observed group difference. | 0.5 |

**Original submitted target notation:** theta_ATE = E[Y(1)-Y(0)]


## Identifiability assumptions

- Consistency Y=Y(A) and well-defined binary treatment interventions.
- Independent identically distributed individuals; no interference.
- Conditional exchangeability (Y(0),Y(1)) independent of A given X; independent assignment uniforms and outcome noise implement it.
- Positivity 0.1 &lt;= P(A=1\|X) &lt;= 0.9 on the registered support.
- All required pretreatment confounders X1,X2 are observed; complete data and finite first moments.

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Adaptations from the source (submitted, unverified):**

- Retain Setup A equations and the d=6, sigma=1 parameter cell; rename source treatment W as A.
- Collect the scalar population ATE E[Y(1)-Y(0)] instead of the source CATE function. The value 0.5 is derived here, not presented as a paper-reported ATE estimate.
- Use Python/NumPy PCG64 and row-major X draws with independent uniform-threshold Bernoulli assignment; distributional reconstruction, not identical R random draws.
- Use n=128, seed=1729 for a CPU interface check instead of the source estimator experiments. No estimator is fitted.
- effect_scale=1 preserves the original treatment effect; zero and reversed values appear only in verification controls, not as additional registered families or scenarios.

**Warnings:**

- No explicit latent-variable metadata or reliably identifiable latent declarations; absence from this list does not prove that no latent variables exist.
