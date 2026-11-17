# ATE with one confounder subject to nonrandom missingness

> **Unverified extraction — scientific review required.**

**Primary area:** ATE — Average Treatment Effect

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Yang, S., Wang, L. and Ding, P. (2019). Causal inference with confounders missing not at random. Biometrika, 106(4), 875-888. DOI: 10.1093/biomet/asz048.

**DOI:** 10.1093/biomet/asz048 · **Source locator:** Section 5.2, One confounder subject to missingness; journal pages 884-885; electronic PDF reader pages 10-11 of 27. DGP equations are unnumbered prose. Section 2.1 defines ATE and Assumptions 1-2; Section 2.3 defines Assumption 6 (outcome-independent missingness). Supplementary material: 13-page PDF, S1 diagrams, S2 proofs, S3 estimator details, S4 Bayesian estimation; no additional parameter values for Section 5.2 were identified.

## DGP / generation mechanism

**Sampling design:** Unit: Individual; Dependence: Independent and identically distributed full-data individuals. Within an individual, X1 and X2 affect treatment, potential outcomes and the missingness indicator. R1 is generated conditional on A and the complete X; observed X1 is masked according to R1. No interference or clustering.

**Generator source:** [generator.py](../generators/ate-yang-wang-ding-2019-mnar-confounder-v1.py)

**Keywords (source-described):** Interactions · Nonlinearity

**Observed variables**

X1, X2, A, Y, R1

**Latent variables**

Not explicitly identified (review required)

**Latent-variable identification:** not explicitly specified

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

**Baseline continuous confounder**

$$
X_{1} \sim \mathcal{N}(\text{ mean }=1, \text{ variance }=1)
$$

**Baseline binary confounder**

$$
X_{2} \sim \mathrm{Bernoulli}(0.5)
$$

**Potential outcome under control**

$$
Y(0) = 0.5 + 2\cdot X_{1} + X_{2} + \varepsilon(0), \varepsilon(0) \sim \mathcal{N}(0,1)
$$

**Potential outcome under treatment**

$$
Y(1) = 3\cdot X_{1} + 2\cdot X_{2} + \varepsilon(1), \varepsilon(1) \sim \mathcal{N}(0,1)
$$

**Treatment assignment**

$$
A \mid  X_{1},X_{2} \sim \mathrm{Bernoulli}(\pi)
$$

$$
\mathrm{logit}(\pi) = 1.25 - 0.5\cdot X_{1} - 0.5\cdot X_{2}
$$

**Missingness indicator**

$$
R_{1} \mid  X_{1},X_{2},A \sim \mathrm{Bernoulli}(p)
$$

$$
\mathrm{logit}(p) = -2 + 2\cdot X_{1} + A\cdot (1.5 + X_{2})
$$

$$
R_{1}=1 \mathrm{means} X_{1} \text{ observed }
$$

**Observed outcome**

$$
Y = A\cdot Y(1) + (1-A)\cdot Y(0)
$$

**Target truth**

$$
\mathrm{ATE}=\mathbb{E}[Y(1)-Y(0)]=-0.5 + 1\cdot \mathbb{E}[X_{1}] + 1\cdot \mathbb{E}[X_{2}] = -0.5+1+0.5=1
$$

<details>
<summary>Original source equations (verbatim)</summary>

<pre>
X1 ~ Normal(mean=1, variance=1)
X2 ~ Bernoulli(0.5)
Y(0) = 0.5 + 2*X1 + X2 + epsilon(0), epsilon(0) ~ Normal(0,1)
Y(1) = 3*X1 + 2*X2 + epsilon(1), epsilon(1) ~ Normal(0,1)
A | X1,X2 ~ Bernoulli(pi); logit(pi) = 1.25 - 0.5*X1 - 0.5*X2
R1 | X1,X2,A ~ Bernoulli(p); logit(p) = -2 + 2*X1 + A*(1.5 + X2); R1=1 means X1 observed
Y = A*Y(1) + (1-A)*Y(0)
ATE=E[Y(1)-Y(0)]=-0.5 + 1*E[X1] + 1*E[X2] = -0.5+1+0.5=1
</pre>

</details>


## Parameter scenarios, estimands and truth

| Scenario | Estimand | Definition | Reported value | Evidence status |
|---|---|---|---|---|
| paper_section_5_2 | ATE | Population average effect of intervening to set treatment A from 0 (control) to 1 (active), averaged over the full pre-treatment covariate distribution before missingness: E[Y(1)-Y(0)]. | 1.0 | reported_numeric |

**Original submitted target notation:** ATE = E[Y(1)-Y(0)]


## Identifiability assumptions

- Consistency: observed outcome Y = A Y(1) + (1-A)Y(0).
- Conditional exchangeability in the full data: {Y(0),Y(1)} independent of A conditional on X=(X1,X2), as Assumption 1 in Section 2.1 states; this follows from the declared simulator convention of independent potential-outcome errors conditional on X and the treatment law depending only on X.
- Pointwise treatment positivity from the logistic assignment law. With the stated unbounded Gaussian support, a uniform bound c1 &lt;= P(A=1\|X) &lt;= c2 as in Assumption 2 is not established and in fact cannot hold globally for this logistic form.
- Outcome-independent missingness: R1 is independent of Y conditional on (A,X), consistent with Assumption 6. R1 may depend on the missing confounder X1 itself, so the missingness is not at random.
- Full-data individuals are iid as described in Section 2.2. X1-X2 joint independence and cross-independence of potential-outcome errors are implementation conventions, not fully specified in the Section 5.2 paragraph, and require scientific confirmation.
- Assumption 7 in Section 2.3 requires a uniform positive lower bound on the probability of complete observation. With unbounded X1 and the stated missingness logit, no such uniform lower bound is guaranteed. Assumption 8 (bounded completeness) also needs separate mathematical review. The known analytic oracle does not by itself establish identification assumptions for estimators.

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Adaptations from the source (submitted, unverified):**

- Section 5.2 specifies the marginal laws X1 ~ Normal(1,1) and X2 ~ Bernoulli(0.5), but does not explicitly state their joint dependence. For the executable candidate, X1 and X2 are generated independently; the paper's approximate 67% response-rate report is consistent with this convention but does not uniquely prove it. Maintainer/scientific confirmation is requested.
- The paper specifies marginal laws epsilon(0) ~ Normal(0,1) and epsilon(1) ~ Normal(0,1), but Section 5.2 does not state all cross-independence relations. The executable implementation draws the errors independently of each other and X; this extra joint-law convention remains pending scientific confirmation.
- The collection worker accepts only finite numeric observed columns. To preserve the missingness pattern without NaN/Inf output, the exported X1 column uses 0.0 as a sentinel when R1=0 and exports R1 explicitly; when R1=1, X1 retains its generated value. This is an interface encoding, not an imputation, and must be interpreted jointly with R1.
- Use analytic ATE truth and CPU smoke checks instead of reproducing the paper's full 2,000-replicate simulation study, 100 imputed datasets, or 500-replicate bootstrap variance calculations.

**Warnings:**

- No explicit latent-variable metadata or reliably identifiable latent declarations; absence from this list does not prove that no latent variables exist.
