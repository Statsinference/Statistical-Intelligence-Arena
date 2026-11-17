# Nonparametric regression with damped-sine mean: CCF2018 Models 5 and 6 (Hall-Horowitz g2/g3 family)

> **Unverified extraction — scientific review required.**

**Primary area:** Nonparametric Regression

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Calonico, S., Cattaneo, M. D., and Farrell, M. H. (2018). On the Effect of Bias Estimation on Coverage Accuracy in Nonparametric Inference. Journal of the American Statistical Association 113(522), 767-779. DOI: 10.1080/01621459.2017.1285776. Models 5 and 6 originate from Hall, P. G. and Horowitz, J. L. (2013), A simple bootstrap method for constructing nonparametric confidence bands for functions, Annals of Statistics 41(4), 1892-1921, where they appear as g2 and g3=g2(x/3).

**DOI:** 10.1080/01621459.2017.1285776 · **Source locator:** Supplement S.II.7 (Complete Simulation Results), printed p.80, PDF p.81: DGP structure Y=m(X)+eps, X~U[-1,1], eps~N(0,1), and Models 5-6 regression functions. Main text Section 4 (Simulation Results), printed p.776, PDF p.10: representative Model 5 example and the five-point evaluation grid x in {-2/3,-1/3,0,1/3,2/3}.

## DGP / generation mechanism

**Sampling design:** Unit: individual; Dependence: iid

**Generator source:** [generator.py](../generators/nri-damped-sine-v1.py)

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

**Model 5 (g2 of Hall-Horowitz)**

```math
m(x) = \sin(3\cdot \pi\cdot x/2) / (1 + 18\cdot x^{2}\cdot (\mathrm{sgn}(x)+1))
```

**Model 6 (g3 = g2(x/3))**

```math
m(x) = \sin(\pi\cdot x/2) / (1 + 2\cdot x^{2}\cdot (\mathrm{sgn}(x)+1))
```

**Estimand (fixed query point)**

```math
m(x_{0}) = \mathbb{E}[Y \mid  X = x_{0}]  \text{ at }  x_{0} \in \{-2/3,-1/3,0,1/3,2/3\}
```

**M5 five-point truth**

```math
m_{5}(-2/3)=0, m_{5}(-1/3)=-1, m_{5}(0)=0, m_{5}(1/3)=0.2, m_{5}(2/3)=0
```

<details>
<summary>Original source equations (verbatim)</summary>

<pre>
Y = m(X) + eps,  X ~ U[-1,1],  eps ~ N(0,1)  independently of X
m(x) = sin(3*pi*x/2) / (1 + 18*x^2*(sgn(x)+1))
m(x) = sin(pi*x/2) / (1 + 2*x^2*(sgn(x)+1))
m(x0) = E[Y | X = x0]  at  x0 in {-2/3,-1/3,0,1/3,2/3}
m5(-2/3)=0, m5(-1/3)=-1, m5(0)=0, m5(1/3)=0.2, m5(2/3)=0
</pre>

</details>


## Parameter scenarios, estimands and truth

<table>
<thead><tr><th>Scenario</th><th>Estimand</th><th>Definition</th><th>Reported value</th></tr></thead>
<tbody>
<tr>
<td>m5_x0_neg2o3</td>
<td rowspan="1">Pointwise conditional mean</td>
<td rowspan="1">

$`\mathbb{E}[Y\mid X=-2/3]`$

</td>
<td>-1.2246467991473532e-16</td>
</tr>
<tr>
<td>m5_x0_neg1o3</td>
<td rowspan="1">Pointwise conditional mean</td>
<td rowspan="1">

$`\mathbb{E}[Y\mid X=-1/3]`$

</td>
<td>-1.0</td>
</tr>
<tr>
<td>m5_x0_0</td>
<td rowspan="1">Pointwise conditional mean</td>
<td rowspan="1">

$`\mathbb{E}[Y\mid X=0]`$

</td>
<td>0.0</td>
</tr>
<tr>
<td>m5_x0_1o3</td>
<td rowspan="1">Pointwise conditional mean</td>
<td rowspan="1">

$`\mathbb{E}[Y\mid X=1/3]`$

</td>
<td>0.2</td>
</tr>
<tr>
<td>m5_x0_2o3</td>
<td rowspan="1">Pointwise conditional mean</td>
<td rowspan="1">

$`\mathbb{E}[Y\mid X=2/3]`$

</td>
<td>7.203804700866784e-18</td>
</tr>
<tr>
<td>m6_x0_neg2o3</td>
<td rowspan="1">Pointwise conditional mean</td>
<td rowspan="1">

$`\mathbb{E}[Y\mid X=-2/3]`$

</td>
<td>-0.8660254037844386</td>
</tr>
<tr>
<td>m6_x0_neg1o3</td>
<td rowspan="1">Pointwise conditional mean</td>
<td rowspan="1">

$`\mathbb{E}[Y\mid X=-1/3]`$

</td>
<td>-0.49999999999999994</td>
</tr>
<tr>
<td>m6_x0_0</td>
<td rowspan="1">Pointwise conditional mean</td>
<td rowspan="1">

$`\mathbb{E}[Y\mid X=0]`$

</td>
<td>0.0</td>
</tr>
<tr>
<td>m6_x0_1o3</td>
<td rowspan="1">Pointwise conditional mean</td>
<td rowspan="1">

$`\mathbb{E}[Y\mid X=1/3]`$

</td>
<td>0.34615384615384615</td>
</tr>
<tr>
<td>m6_x0_2o3</td>
<td rowspan="1">Pointwise conditional mean</td>
<td rowspan="1">

$`\mathbb{E}[Y\mid X=2/3]`$

</td>
<td>0.3117691453623979</td>
</tr>
</tbody>
</table>

**Definition notes**

- All scenarios: Under the scenario-specific data law.

<details>
<summary>Submitted estimand definitions</summary>

Submitted English definitions appear below; other original-language definitions remain in the linked JSON. Concise formulas above are display interpretations and still require scientific review.

**Scenario(s):** m5_x0_neg2o3, m5_x0_neg1o3, m5_x0_0, m5_x0_1o3, m5_x0_2o3, m6_x0_neg2o3, m6_x0_neg1o3, m6_x0_0, m6_x0_1o3, m6_x0_2o3

Conditional mean of Y given X = x0 at a fixed query point x0 from the grid {-2/3,-1/3,0,1/3,2/3}, in the superpopulation defined by Y = m(X) + eps, X ~ U[-1,1], eps ~ N(0,1). Model 5: m(x)=sin(3*pi*x/2)/(1+18*x^2*(sgn(x)+1)). Model 6: m(x)=sin(pi*x/2)/(1+2*x^2*(sgn(x)+1)) = g3(x) = g2(x/3) of the Hall-Horowitz family. Each (model, query point) is a separate pointwise inference target; the five points are not a simultaneous confidence band.

[Open raw scientific record (JSON)](./nri-damped-sine-v1.json).

</details>


**Original submitted target notation:** m(x0) = E[Y \| X = x0]


## Identifiability assumptions

- iid observations; X is independent of the noise eps
- eps ~ N(0,1) with mean zero, so E[Y\|X=x0] = m(x0) is deterministic and known in closed form
- m(x) is smooth away from x=0; at x=0 the sgn(x) factor makes the damping denominator piecewise, but m(0)=0 by continuity (sin(0)=0 and x^2=0 removes the sgn dependence)
- Pointwise inference at each fixed query point; the five-point grid is NOT evaluated as a simultaneous confidence band by the current scalar truth interface
- No causal interpretation; this is a nonparametric regression inference (NRI) task with no treatment, mediator, or intervention

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Adaptations from the source (submitted, unverified):**

- Models 5 and 6 are registered as scenarios of the Hall-Horowitz (2013) damped-sine mechanism family (g2 and g3=g2(x/3)), not as a new independent family, per the cross-paper no-double-counting rule.
- The five evaluation points {-2/3,-1/3,0,1/3,2/3} are registered as separate fixed-query-point scenarios because the current scalar truth interface returns one m(x0) per call; each is a pointwise 95% interval target, not a simultaneous confidence band.
- Population truth is computed analytically (closed form); no coverage simulation, bootstrap, or PFN training is run in this collection.

**Warnings:**

- No explicit latent-variable metadata or reliably identifiable latent declarations; absence from this list does not prove that no latent variables exist.
