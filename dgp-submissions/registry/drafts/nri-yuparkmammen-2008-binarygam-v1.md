# Pointwise binary-response and count-response mean in the Yu-Park-Mammen smooth-backfitting GAM design

> **Unverified extraction — scientific review required.**

**Primary area:** Nonparametric Regression

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Yu, K., Park, B. U. and Mammen, E. (2008). Smooth backfitting in generalized additive models. The Annals of Statistics 36(1), 228-260. DOI: 10.1214/009053607000000596.

**DOI:** — · **Source locator:** Formula bodies: (5) on PDF p.7. Section starts: Section 2.2 on PDF p.6, Section 5 on PDF p.20. Unnumbered paragraph on PDF p.20: "The simulation was done under the following two models" (two conditional-response laws and following design/normalisation paragraphs). All PDF pages are 1-based pages of the fixed reading file 0803.1922v1. No printed journal page is inferred by adding an offset.

## DGP / generation mechanism

**Sampling design:** Unit: independent observation (X, Y) pair; Dependence: iid across observations; the two covariate components are independent within an observation (no Markov, cluster or repeated-measure structure)

**Generator source:** [generator.py](../generators/nri-yuparkmammen-2008-binarygam-v1.py)

**Keywords (source-described):** Nonlinearity

**Observed variables**

X1, X2, Y

**Latent variables**

Not explicitly identified (review required)

**Latent-variable identification:** not explicitly specified

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

**1. First covariate**

$$
X_{1}\sim \mathcal{N}(0,1) \mathrm{conditional} \text{ on } -1\leq X_{1}\leq 1, \mathrm{using} \mathrm{rejection} \mathrm{resampling}
$$

$$
\mathrm{Source} \mathrm{design} j=1
$$

$$
\mathrm{pre}-\mathrm{truncation} \text{ mean }=0, \mathrm{sd}=1.
$$

**2. Second covariate**

$$
X_{2}\sim \mathcal{N}(0,1) \mathrm{conditional} \text{ on } -1\leq X_{2}\leq 1
$$

independently of X1

$$
\mathrm{Source} j=1 \mathrm{correlation}=0
$$

$$
\text{ the } \mathrm{correlated} j=2 \mathrm{design} \text{ is } \text{ not } \mathrm{generated}.
$$

**3. Predictor**

$$
\eta=\sin(\pi\cdot X_{1})+0.5\cdot (X_{2}+\sin(\pi\cdot X_{2}))
$$

Deterministic source predictor

no extra noise.

**4. Response mean**

$$
m=1/(1+\exp(-\eta)) \text{ for } \mathrm{Bernoulli}
$$

$$
m=\exp(\eta) \text{ for } \mathrm{Poisson}
$$

Stable logistic evaluation

finite eta on [-1,1]^2.

**5. Observed response**

$$
Y\mid X\sim \mathrm{Bernoulli}(m) \text{ or } \mathrm{Poisson}(m)
$$

$$
\mathrm{Bernoulli} \mathrm{inversion} \text{ or } \mathrm{Knuth} \mathrm{product} \mathrm{sampler}
$$

return X1,X2,Y

$$
\mathrm{Conditional} \text{ variance }=m\cdot (1-m) \text{ or } m, \text{ respectively }
$$

no independent additive error is used.

<details>
<summary>Original source equations (verbatim)</summary>

<pre>
X1~N(0,1) conditional on -1&lt;=X1&lt;=1, using rejection resampling. Source design j=1; pre-truncation mean=0, sd=1.
X2~N(0,1) conditional on -1&lt;=X2&lt;=1, independently of X1. Source j=1 correlation=0; the correlated j=2 design is not generated.
eta=sin(pi*X1)+0.5*(X2+sin(pi*X2)). Deterministic source predictor; no extra noise.
m=1/(1+exp(-eta)) for Bernoulli; m=exp(eta) for Poisson. Stable logistic evaluation; finite eta on [-1,1]^2.
Y|X~Bernoulli(m) or Poisson(m); Bernoulli inversion or Knuth product sampler; return X1,X2,Y. Conditional variance=m*(1-m) or m, respectively; no independent additive error is used.
</pre>

</details>


## Parameter scenarios, estimands and truth

| Scenario | Estimand | Definition | True value | Evidence status |
|---|---|---|---|---|
| original-bernoulli | m(x0) = E[Y \| X = x0] | Conditional mean of the response at the fixed query point x0 = (0.5, 0.5) in the superpopulation defined by the fixed DGP: m(x0) = expit(eta(x0)) in scenario original-bernoulli (a classification probability) and m(x0) = exp(eta(x0)) in scenario original-poisson (a conditional count mean), with eta(x) = sin(pi x1) + 0.5 [x2 + sin(pi x2)]. A pointwise scalar query only; it is not a simultaneous confidence band over the covariate region. | 0.8519528019683106 | reported_numeric |
| original-poisson | m(x0) = E[Y \| X = x0] | Conditional mean of the response at the fixed query point x0 = (0.5, 0.5) in the superpopulation defined by the fixed DGP: m(x0) = expit(eta(x0)) in scenario original-bernoulli (a classification probability) and m(x0) = exp(eta(x0)) in scenario original-poisson (a conditional count mean), with eta(x) = sin(pi x1) + 0.5 [x2 + sin(pi x2)]. A pointwise scalar query only; it is not a simultaneous confidence band over the covariate region. | 5.754602676005731 | reported_numeric |

## Identifiability assumptions

- Observations (X_i, Y_i) are independent and identically distributed; there is no clustering, serial, spatial or network dependence.
- Covariates follow the source distribution j=1: two independent standard normal components, each truncated to [-1, 1], so the joint support is the box [-1, 1]^2.
- The conditional response law is exactly the source model: Y \| X = x ~ Bernoulli(expit(eta(x))) in scenario original-bernoulli and Y \| X = x ~ Poisson(exp(eta(x))) in scenario original-poisson; no link misspecification and no extra noise component.
- The query point (0.5, 0.5) is interior to the covariate support, so the target is determined by the sampling law evaluated at a point of positive density; no extrapolation is involved.
- The target is a pointwise scalar, not a simultaneous band, not a coverage claim, and not the source's ISB/IV/MISE criterion; a correct pointwise check does not license any band or coverage statement.

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Warnings:**

- No explicit latent-variable metadata or reliably identifiable latent declarations; absence from this list does not prove that no latent variables exist.
