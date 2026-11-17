# Nonparametric regression with two Gaussian peaks: CCF2018 Model 3 (homoscedastic)

> **Unverified extraction — scientific review required.**

**Primary area:** Nonparametric Regression

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Calonico, S., Cattaneo, M. D., and Farrell, M. H. (2018). On the Effect of Bias Estimation on Coverage Accuracy in Nonparametric Inference. Journal of the American Statistical Association 113(522), 767-779. DOI: 10.1080/01621459.2017.1285776.

**DOI:** 10.1080/01621459.2017.1285776 · **Source locator:** Supplement S.II.7 (Complete Simulation Results), printed p.80, PDF p.81: data-generating process Y=m(X)+eps, X~U[-1,1], eps~N(0,1) (homoscedastic), and Model 3 regression function m(x)=0.3*exp(-4*(2x+1)^2)+0.7*exp(-16*(2x-1)^2). Main text Section 4 (Simulation Results), printed p.776, PDF p.10: the five-point evaluation grid x in {-2/3,-1/3,0,1/3,2/3}.

## DGP / generation mechanism

**Sampling design:** Unit: individual; Dependence: iid

**Generator source:** [generator.py](../generators/nri-two-gaussian-peaks-v1.py)

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
\varepsilon\sim \mathcal{N}(0,1)  \mathrm{homoscedastic}
$$

independently of X

**Model 3 (two Gaussian peaks)**

$$
m(x) = 0.3\cdot \exp(-4\cdot (2x+1)^{2}) + 0.7\cdot \exp(-16\cdot (2x-1)^{2})
$$

**Peak locations**

$$
\mathrm{left} \mathrm{peak} \text{ at } x=-1/2 (\mathrm{amplitude} 0.3)
$$

$$
\mathrm{right} \mathrm{peak} \text{ at } x=1/2 (\mathrm{amplitude} 0.7)
$$

**Estimand (fixed query point)**

$$
m(x_{0}) = \mathbb{E}[Y \mid  X = x_{0}]  \text{ at }  x_{0} \in \{-2/3,-1/3,0,1/3,2/3\}
$$

**Five-point analytic forms**

$$
m_{3}(-2/3)=0.3\cdot e^{-4/9}+0.7\cdot e^{-784/9}
$$

$$
m_{3}(-1/3)=0.3\cdot e^{-4/9}+0.7\cdot e^{-400/9}
$$

$$
m_{3}(0)=0.3\cdot e^{-4}+0.7\cdot e^{-16}
$$

$$
m_{3}(1/3)=0.3\cdot e^{-100/9}+0.7\cdot e^{-16/9}
$$

$$
m_{3}(2/3)=0.3\cdot e^{-196/9}+0.7\cdot e^{-16/9}
$$

<details>
<summary>Original source equations (verbatim)</summary>

<pre>
Y = m(X) + eps,  X ~ U[-1,1],  eps ~ N(0,1)  homoscedastic, independently of X
m(x) = 0.3*exp(-4*(2x+1)^2) + 0.7*exp(-16*(2x-1)^2)
left peak at x=-1/2 (amplitude 0.3); right peak at x=1/2 (amplitude 0.7)
m(x0) = E[Y | X = x0]  at  x0 in {-2/3,-1/3,0,1/3,2/3}
m3(-2/3)=0.3*e^(-4/9)+0.7*e^(-784/9); m3(-1/3)=0.3*e^(-4/9)+0.7*e^(-400/9); m3(0)=0.3*e^(-4)+0.7*e^(-16); m3(1/3)=0.3*e^(-100/9)+0.7*e^(-16/9); m3(2/3)=0.3*e^(-196/9)+0.7*e^(-16/9)
</pre>

</details>


## Parameter scenarios, estimands and truth

| Scenario | Estimand | Definition | Reported value | Evidence status |
|---|---|---|---|---|
| m3_x0_neg2o3 | Pointwise conditional mean | Conditional mean of Y given X = x0 at a fixed query point x0 from the grid {-2/3,-1/3,0,1/3,2/3}, in the superpopulation defined by Y = m(X) + eps, X ~ U[-1,1], eps ~ N(0,1) (homoscedastic). Model 3: m(x) = 0.3*exp(-4*(2x+1)^2) + 0.7*exp(-16*(2x-1)^2), a mixture of two Gaussian peaks with the left peak (amplitude 0.3, narrower width) centered at x=-1/2 and the right peak (amplitude 0.7, sharper width) centered at x=1/2. Each query point is a separate pointwise inference target; the five points are not a simultaneous confidence band. This contribution collects only the CCF M3 homoscedastic scenario; the Chen-Qin (2000) two-peak structure m_CQ(x) = m_CCF_M3(2x-1) with heteroscedastic noise, support [0,1], and query points {0,0.5} is a separate contribution because its complete observation law differs. | 0.1923541165289864 | reported_numeric |
| m3_x0_neg1o3 | Pointwise conditional mean | Conditional mean of Y given X = x0 at a fixed query point x0 from the grid {-2/3,-1/3,0,1/3,2/3}, in the superpopulation defined by Y = m(X) + eps, X ~ U[-1,1], eps ~ N(0,1) (homoscedastic). Model 3: m(x) = 0.3*exp(-4*(2x+1)^2) + 0.7*exp(-16*(2x-1)^2), a mixture of two Gaussian peaks with the left peak (amplitude 0.3, narrower width) centered at x=-1/2 and the right peak (amplitude 0.7, sharper width) centered at x=1/2. Each query point is a separate pointwise inference target; the five points are not a simultaneous confidence band. This contribution collects only the CCF M3 homoscedastic scenario; the Chen-Qin (2000) two-peak structure m_CQ(x) = m_CCF_M3(2x-1) with heteroscedastic noise, support [0,1], and query points {0,0.5} is a separate contribution because its complete observation law differs. | 0.19235411652898635 | reported_numeric |
| m3_x0_0 | Pointwise conditional mean | Conditional mean of Y given X = x0 at a fixed query point x0 from the grid {-2/3,-1/3,0,1/3,2/3}, in the superpopulation defined by Y = m(X) + eps, X ~ U[-1,1], eps ~ N(0,1) (homoscedastic). Model 3: m(x) = 0.3*exp(-4*(2x+1)^2) + 0.7*exp(-16*(2x-1)^2), a mixture of two Gaussian peaks with the left peak (amplitude 0.3, narrower width) centered at x=-1/2 and the right peak (amplitude 0.7, sharper width) centered at x=1/2. Each query point is a separate pointwise inference target; the five points are not a simultaneous confidence band. This contribution collects only the CCF M3 homoscedastic scenario; the Chen-Qin (2000) two-peak structure m_CQ(x) = m_CCF_M3(2x-1) with heteroscedastic noise, support [0,1], and query points {0,0.5} is a separate contribution because its complete observation law differs. | 0.005494770441242557 | reported_numeric |
| m3_x0_1o3 | Pointwise conditional mean | Conditional mean of Y given X = x0 at a fixed query point x0 from the grid {-2/3,-1/3,0,1/3,2/3}, in the superpopulation defined by Y = m(X) + eps, X ~ U[-1,1], eps ~ N(0,1) (homoscedastic). Model 3: m(x) = 0.3*exp(-4*(2x+1)^2) + 0.7*exp(-16*(2x-1)^2), a mixture of two Gaussian peaks with the left peak (amplitude 0.3, narrower width) centered at x=-1/2 and the right peak (amplitude 0.7, sharper width) centered at x=1/2. Each query point is a separate pointwise inference target; the five points are not a simultaneous confidence band. This contribution collects only the CCF M3 homoscedastic scenario; the Chen-Qin (2000) two-peak structure m_CQ(x) = m_CCF_M3(2x-1) with heteroscedastic noise, support [0,1], and query points {0,0.5} is a separate contribution because its complete observation law differs. | 0.11831380438580363 | reported_numeric |
| m3_x0_2o3 | Pointwise conditional mean | Conditional mean of Y given X = x0 at a fixed query point x0 from the grid {-2/3,-1/3,0,1/3,2/3}, in the superpopulation defined by Y = m(X) + eps, X ~ U[-1,1], eps ~ N(0,1) (homoscedastic). Model 3: m(x) = 0.3*exp(-4*(2x+1)^2) + 0.7*exp(-16*(2x-1)^2), a mixture of two Gaussian peaks with the left peak (amplitude 0.3, narrower width) centered at x=-1/2 and the right peak (amplitude 0.7, sharper width) centered at x=1/2. Each query point is a separate pointwise inference target; the five points are not a simultaneous confidence band. This contribution collects only the CCF M3 homoscedastic scenario; the Chen-Qin (2000) two-peak structure m_CQ(x) = m_CCF_M3(2x-1) with heteroscedastic noise, support [0,1], and query points {0,0.5} is a separate contribution because its complete observation law differs. | 0.11830932088875505 | reported_numeric |

**Original submitted target notation:** m(x0) = E[Y \| X = x0]


## Identifiability assumptions

- iid observations; X is independent of the noise eps
- eps ~ N(0,1) with mean zero and constant variance (homoscedastic), so E[Y\|X=x0] = m(x0) is deterministic and known in closed form
- m(x) is smooth (infinitely differentiable); each Gaussian peak is C-infinity; the two peaks are well separated (left at x=-1/2, right at x=1/2)
- Pointwise inference at each fixed query point; the five-point grid is NOT evaluated as a simultaneous confidence band by the current scalar truth interface
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
