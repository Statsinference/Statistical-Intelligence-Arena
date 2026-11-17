# Athey-Tibshirani-Wager (2019) third setting: heterogeneity and confounding combined

> **Unverified extraction — scientific review required.**

**Primary area:** CATE — Conditional Average Treatment Effect

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Athey, S., Tibshirani, J. and Wager, S. (2019). Generalized random forests. The Annals of Statistics 47(2), 1148-1178. DOI: 10.1214/18-AOS1709.

**DOI:** — · **Source locator:** Section 6.2 'Example: Causal Forests', arXiv:1610.01271v4 (5 Apr 2018) PDF pp.22-23: the section opens on p.22; the working equations tau(x) and e(x) = (1/4)(1 + beta_{2,4}(x3)), m(x) = 2 x3 - 1, the sentence defining the third setting ('We also consider a third setting with both heterogeneity and confounding, that combines tau(.) from the first setting with m(.) and e(.) from the second') and Table 1 all appear on p.23. The settings are unnumbered prose, so the locator gives page + paragraph instead of an equation number.

## DGP / generation mechanism

**Sampling design:** Unit: individual; Dependence: independent and identically distributed

**Generator source:** [generator.py](../generators/cate-athey-2019-heterogeneity-confounding-v1.py)

**Keywords (source-described):** Interactions · Nonlinearity

**Observed variables**

X1–X5 (5 variables), A, Y

<details>
<summary>All observed variable names</summary>

X1, X2, X3, X4, X5, A, Y

</details>

**Latent variables**

Xj

**Latent-variable identification:** candidates from equations need review

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

**X1-X5**

```math
\mathrm{Xj} \sim \mathrm{Uniform}(0,1) \text{ independently }, j = 1..5
```

**Treatment**

```math
P(A=1\mid X) = 0.25 (1 + 20 X_{3} (1-X_{3})^{3})
```

**Baseline**

```math
m(X) = 2 X_{3} - 1
```

**Heterogeneity**

```math
\tau(X) = s(X_{1}) s(X_{2}), s(u) = 1 + 1/(1 + \exp(-20 (u - 1/3)))
```

**Outcome**

```math
Y = m(X) + A \tau(X) + \varepsilon, \varepsilon\sim \mathcal{N}(0,1)
```

<details>
<summary>Original source equations (verbatim)</summary>

<pre>
Xj ~ Uniform(0,1) independently, j = 1..5
P(A=1|X) = 0.25 (1 + 20 X3 (1-X3)^3)
m(X) = 2 X3 - 1
tau(X) = s(X1) s(X2), s(u) = 1 + 1/(1 + exp(-20 (u - 1/3)))
Y = m(X) + A tau(X) + eps, eps ~ Normal(0,1)
</pre>

</details>


## Parameter scenarios, estimands and truth

| Scenario | Estimand | Definition | Reported value |
|---|---|---|---|
| original | CATE ⚠ review | Conditional average treatment effect at the declared query points for the combined setting: sigmoid-product heterogeneity on X1, X2 together with a beta-density propensity and a linear baseline on X3. | 2.25 |

**Original submitted target notation:** tau(x0) = E[Y(1) - Y(0) \| X = x0]


## Identifiability assumptions

- SUTVA: one version of treatment, no interference
- Unconfoundedness: treatment depends on X3, which also enters the baseline m(X) = 2 X3 - 1, so the design is observational
- Overlap: 0.25 &lt;= e(X) &lt;= 0.777 because 20 u (1-u)^3 peaks at u = 1/4
- Homoscedastic Gaussian noise with unit variance

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Adaptations from the source (submitted, unverified):**

- Ambient dimension fixed at p = 5 instead of the source's p in {10, 20}; the third setting needs only X1, X2 (effect) and X3 (confounding).
- The source writes Y ~ N(m(X) + (W - 0.5) tau(X), 1); this package uses A in {0,1} and Y = m(X) + A tau(X) + eps with eps ~ N(0,1). The CATE is unchanged.
- The effect surface is identical to cate-wager-2018-sigmoid-product-v1 because the source builds the third setting by reusing tau from its first setting; the difference between the two contributions is the confounding structure, which is the point of this row of Table 1.
- The source aggregates over 60 replications with B = 2000 trees; no forest is fitted here.

**Warnings:**

- Latent-variable candidates inferred from source equations; confirm their roles and completeness against the original paper or generator.
