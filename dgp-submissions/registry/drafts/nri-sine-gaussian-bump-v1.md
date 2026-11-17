# Nonparametric regression with sine plus Gaussian bump: CCF2018 Model 1 (m(x)=sin(4x)+2*exp(-64x^2))

> **Unverified extraction — scientific review required.**

**Primary area:** Nonparametric Regression

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Calonico, S., Cattaneo, M. D., and Farrell, M. H. (2018). On the Effect of Bias Estimation on Coverage Accuracy in Nonparametric Inference. Journal of the American Statistical Association 113(522), 767-779. DOI: 10.1080/01621459.2017.1285776.

**DOI:** 10.1080/01621459.2017.1285776 · **Source locator:** Supplement S.II.7 (Complete Simulation Results), printed p.80, PDF p.81: data-generating process Y=m(X)+eps, X~U[-1,1], eps~N(0,1), and Model 1 regression function m(x)=sin(4x)+2*exp(-64*x^2). Main text Section 4 (Simulation Results), printed p.776, PDF p.10: the five-point evaluation grid x in {-2/3,-1/3,0,1/3,2/3}.

## DGP / generation mechanism

**Sampling design:** Unit: individual; Dependence: iid

**Generator source:** [generator.py](../generators/nri-sine-gaussian-bump-v1.py)

**Keywords (source-described):** Nonlinearity

**Observed variables**

X, Y

**Latent variables**

Not explicitly identified (review required)

**Latent-variable identification:** not explicitly specified

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

**DGP structure**

$$
Y = m(X) + \varepsilon,  X \sim U[-1,1]
$$

$$
\varepsilon\sim \mathcal{N}(0,1)
$$

independently of X

**Model 1 (sine plus Gaussian bump)**

$$
m(x) = \sin(4x) + 2\cdot \exp(-64\cdot x^{2})
$$

**Estimand (fixed query point)**

$$
m(x_{0}) = \mathbb{E}[Y \mid  X = x_{0}]  \text{ at }  x_{0} \in \{-2/3,-1/3,0,1/3,2/3\}
$$

**Truth at x0=0**

$$
m(0) = \sin(0) + 2\cdot \exp(0) = 0 + 2 = 2  (\mathrm{exact})
$$

**Even-part identity**

Source notation retained without guessing:

<pre>m(x) + m(-x) = 4*exp(-64*x^2)  (sin cancels as odd; bump doubles as even)</pre>

<details>
<summary>Original source equations (verbatim)</summary>

<pre>
Y = m(X) + eps,  X ~ U[-1,1],  eps ~ N(0,1)  independently of X
m(x) = sin(4x) + 2*exp(-64*x^2)
m(x0) = E[Y | X = x0]  at  x0 in {-2/3,-1/3,0,1/3,2/3}
m(0) = sin(0) + 2*exp(0) = 0 + 2 = 2  (exact)
m(x) + m(-x) = 4*exp(-64*x^2)  (sin cancels as odd; bump doubles as even)
</pre>

</details>


## Parameter scenarios, estimands and truth

| Scenario | Estimand | Definition | Reported value | Evidence status |
|---|---|---|---|---|
| m1_x0_neg2o3 | Pointwise conditional mean | Conditional mean of Y given X = x0 at a fixed query point x0 from the grid {-2/3,-1/3,0,1/3,2/3}, in the superpopulation defined by Y = m(X) + eps, X ~ U[-1,1], eps ~ N(0,1). Model 1: m(x)=sin(4x)+2*exp(-64*x^2), a sine oscillation plus a sharp Gaussian bump centered at x=0. Each query point is a separate pointwise inference target; the five points are not a simultaneous confidence band. | -0.4572726266349253 | reported_numeric |
| m1_x0_neg1o3 | Pointwise conditional mean | Conditional mean of Y given X = x0 at a fixed query point x0 from the grid {-2/3,-1/3,0,1/3,2/3}, in the superpopulation defined by Y = m(X) + eps, X ~ U[-1,1], eps ~ N(0,1). Model 1: m(x)=sin(4x)+2*exp(-64*x^2), a sine oscillation plus a sharp Gaussian bump centered at x=0. Each query point is a separate pointwise inference target; the five points are not a simultaneous confidence band. | -0.9703059256931684 | reported_numeric |
| m1_x0_0 | Pointwise conditional mean | Conditional mean of Y given X = x0 at a fixed query point x0 from the grid {-2/3,-1/3,0,1/3,2/3}, in the superpopulation defined by Y = m(X) + eps, X ~ U[-1,1], eps ~ N(0,1). Model 1: m(x)=sin(4x)+2*exp(-64*x^2), a sine oscillation plus a sharp Gaussian bump centered at x=0. Each query point is a separate pointwise inference target; the five points are not a simultaneous confidence band. | 2.0 | reported_numeric |
| m1_x0_1o3 | Pointwise conditional mean | Conditional mean of Y given X = x0 at a fixed query point x0 from the grid {-2/3,-1/3,0,1/3,2/3}, in the superpopulation defined by Y = m(X) + eps, X ~ U[-1,1], eps ~ N(0,1). Model 1: m(x)=sin(4x)+2*exp(-64*x^2), a sine oscillation plus a sharp Gaussian bump centered at x=0. Each query point is a separate pointwise inference target; the five points are not a simultaneous confidence band. | 0.973569877033457 | reported_numeric |
| m1_x0_2o3 | Pointwise conditional mean | Conditional mean of Y given X = x0 at a fixed query point x0 from the grid {-2/3,-1/3,0,1/3,2/3}, in the superpopulation defined by Y = m(X) + eps, X ~ U[-1,1], eps ~ N(0,1). Model 1: m(x)=sin(4x)+2*exp(-64*x^2), a sine oscillation plus a sharp Gaussian bump centered at x=0. Each query point is a separate pointwise inference target; the five points are not a simultaneous confidence band. | 0.45727262663669865 | reported_numeric |

**Original submitted target notation:** m(x0) = E[Y \| X = x0]


## Identifiability assumptions

- iid observations; X is independent of the noise eps
- eps ~ N(0,1) with mean zero, so E[Y\|X=x0] = m(x0) is deterministic and known in closed form
- m(x) is smooth (infinitely differentiable); the Gaussian bump 2*exp(-64*x^2) is centered at x=0 with effective width ~1/8 and creates high curvature near x=0
- Pointwise inference at each fixed query point; the five-point grid is NOT evaluated as a simultaneous confidence band by the current scalar truth interface
- No causal interpretation; this is a nonparametric regression inference (NRI) task with no treatment, mediator, or intervention

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Adaptations from the source (submitted, unverified):**

- Model 1 is a sine-plus-Gaussian-bump regression function newly constructed by CCF2018 (distinct from the Hall-Horowitz 2013 damped-sine family g2/g3); registered as an independent mean family as specified by the task.
- The five evaluation points {-2/3,-1/3,0,1/3,2/3} are registered as separate fixed-query-point scenarios because the current scalar truth interface returns one m(x0) per call; each is a pointwise 95% interval target, not a simultaneous confidence band.
- Population truth is computed by direct analytic/numerical evaluation (closed-form function); no coverage simulation, bootstrap, or PFN training is run in this collection.

**Warnings:**

- No explicit latent-variable metadata or reliably identifiable latent declarations; absence from this list does not prove that no latent variables exist.
