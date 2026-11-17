# Nonparametric regression with linear mean and Gaussian bump: CCF2018 Models 2 and 4

> **Unverified extraction — scientific review required.**

**Primary area:** Nonparametric Regression

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Calonico, S., Cattaneo, M. D., and Farrell, M. H. (2018). On the Effect of Bias Estimation on Coverage Accuracy in Nonparametric Inference. Journal of the American Statistical Association 113(522), 767-779. DOI: 10.1080/01621459.2017.1285776.

**DOI:** 10.1080/01621459.2017.1285776 · **Source locator:** Supplement S.II.7 (Complete Simulation Results), printed p.80, PDF p.81: data-generating process Y=m(X)+eps, X~U[-1,1], eps~N(0,1), and Models 1-6 with regression functions. Main text Section 4 (Simulation Results), printed p.776, PDF p.10: representative Model 5 and the evaluation grid x in {-2/3,-1/3,0,1/3,2/3}.

## DGP / generation mechanism

**Sampling design:** Unit: individual; Dependence: iid

**Generator source:** [generator.py](../generators/nri-linear-gaussian-bump-v1.py)

**Keywords (source-described):** Nonlinearity

**Observed variables**

X, Y

**Latent variables**

Not explicitly identified (review required)

**Latent-variable identification:** not explicitly specified

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

**DGP structure**

```math
Y = m(X) + \varepsilon,  X \sim U[-1,1]
```

```math
\varepsilon\sim \mathcal{N}(0,1)
```

independently of X

**Model 2 (linear + Gaussian bump)**

```math
m(x) = 2x + 2\cdot \exp(-64\cdot x^{2})
```

**Model 4 (linear + scaled Gaussian density)**

```math
m(x) = x + 5\cdot \phi(10x),  \phi(z) = \exp(-z^{2}/2)/\sqrt{2\cdot \pi}
```

**Estimand (fixed query point)**

```math
m(x_{0}) = \mathbb{E}[Y \mid  X = x_{0}]  \text{ at }  x_{0} = 0
```

**Truth Model 2**

```math
m(0) = 2\cdot 0 + 2\cdot \exp(0) = 2
```

**Truth Model 4**

```math
m(0) = 0 + 5\cdot \phi(0) = 5/\sqrt{2\cdot \pi} \approx 1.994711
```

<details>
<summary>Original source equations (verbatim)</summary>

<pre>
Y = m(X) + eps,  X ~ U[-1,1],  eps ~ N(0,1)  independently of X
m(x) = 2x + 2*exp(-64*x^2)
m(x) = x + 5*phi(10x),  phi(z) = exp(-z^2/2)/sqrt(2*pi)
m(x0) = E[Y | X = x0]  at  x0 = 0
m(0) = 2*0 + 2*exp(0) = 2
m(0) = 0 + 5*phi(0) = 5/sqrt(2*pi) approx 1.994711
</pre>

</details>


## Parameter scenarios, estimands and truth

| Scenario | Estimand | Definition | Reported value |
|---|---|---|---|
| model2 | Pointwise conditional mean | Conditional mean of Y given X = x0 at the fixed query point x0 = 0, in the superpopulation defined by the DGP Y = m(X) + eps, X ~ U[-1,1], eps ~ N(0,1). Models 2 and 4 from supplement S.II.7 are collected as two scenarios of the same mechanism family; both are linear-plus-Gaussian-bump regression functions. | 2.0 |
| model4 | Pointwise conditional mean | Conditional mean of Y given X = x0 at the fixed query point x0 = 0, in the superpopulation defined by the DGP Y = m(X) + eps, X ~ U[-1,1], eps ~ N(0,1). Models 2 and 4 from supplement S.II.7 are collected as two scenarios of the same mechanism family; both are linear-plus-Gaussian-bump regression functions. | 1.9947114020071635 |

**Original submitted target notation:** m(x0) = E[Y \| X = x0]


## Identifiability assumptions

- iid observations; X is independent of the noise eps
- eps ~ N(0,1) with mean zero, so E[Y\|X=x0] = m(x0) is deterministic and known in closed form
- m(x) is smooth (infinitely differentiable) on [-1,1]; the Gaussian bump creates high curvature near x=0
- Pointwise inference at a single fixed query point x0=0; this is not a simultaneous confidence band over the paper's evaluation grid {-2/3,-1/3,0,1/3,2/3}
- No causal interpretation; this is a nonparametric regression inference (NRI) task with no treatment, mediator, or intervention

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** exact_reproduction

**Status:** needs_scientific_review

**Adaptations from the source (submitted, unverified):**

- None described in the submitted metadata; this does not establish exact reproduction.

**Warnings:**

- No explicit latent-variable metadata or reliably identifiable latent declarations; absence from this list does not prove that no latent variables exist.
