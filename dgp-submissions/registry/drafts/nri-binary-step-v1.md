# Upper step binary regression functions from Dimitriadis et al. (2023)

> **Unverified extraction — scientific review required.**

**Primary area:** Nonparametric Regression

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Dimitriadis, T., Dümbgen, L., Henzi, A., Puke, M. and Ziegel, J. (2023). Honest calibration assessment for binary outcome predictions. Biometrika, 110(3), 663-680. DOI: 10.1093/biomet/asac068.

**DOI:** — · **Source locator:** DGP source actually checked in arXiv:2203.04065v2 (2022-11-02), PDF p.8, Section 5, item 4 (Step): upper staircase p_s(x)=(floor(k*x)+1{x!=1})/k with k=15-10*s; X~U[0,1] and Y~Bernoulli{p_s(X)} are specified on the same page. Supplementary Material PDF pp.17-20 covers rounding, application details and proofs and does not state a changed step DGP. The paper gives replication URL https://github.com/marius-cp/replication_DDHPZ22 but no fixed code commit. Formal Biometrika DGP differences were not checked [*].

## DGP / generation mechanism

**Sampling design:** Unit: individual observation (X_i,Y_i); Dependence: iid across observations; no cluster, panel, network, or within-unit dependence

**Generator source:** [generator.py](../generators/nri-binary-step-v1.py)

**Keywords (source-described):** Nonlinearity

**Observed variables**

X, Y

**Latent variables**

Not explicitly identified (review required)

**Latent-variable identification:** not explicitly specified

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

**Covariate**

$$
X_{i} \sim \mathrm{Uniform}[0,1] \text{ independently }
$$

**Step regression function**

$$
p_{s}(x) = (\lfloor k\cdot x\rfloor + 1\{x \neq 1\}) / k, k = 15 - 10\cdot s, s \in \{0.1, 0.2, \ldots , 1.0\}, k \in \{14, 13, \ldots , 5\}
$$

**Special values**

$$
p_{s}(0) = 1/k
$$

$$
p_{s}(j/k) = (j+1)/k \text{ for } j=0,\ldots ,k-1
$$

$$
p_{s}(1) = 1
$$

**Binary outcome**

$$
Y_{i} \mid  X_{i}=x \sim \mathrm{Bernoulli}(p_{s}(x)) \text{ independently }
$$

**NRI scalar target (default)**

$$
m_{s}(0.5) = \mathbb{E}[Y \mid  X=0.5] = p_{s}(0.5) = (\lfloor k\cdot 0.5\rfloor+1)/k
$$

$$
\text{ for } s=0.5, k=10: \lfloor 5.0\rfloor=5, \mathrm{value}=6/10=0.6
$$

<details>
<summary>Original source equations (verbatim)</summary>

<pre>
X_i ~ Uniform[0,1] independently
p_s(x) = (floor(k*x) + 1{x != 1}) / k, k = 15 - 10*s, s in {0.1, 0.2, ..., 1.0}, k in {14, 13, ..., 5}
p_s(0) = 1/k; p_s(j/k) = (j+1)/k for j=0,...,k-1; p_s(1) = 1
Y_i | X_i=x ~ Bernoulli(p_s(x)) independently
m_s(0.5) = E[Y | X=0.5] = p_s(0.5) = (floor(k*0.5)+1)/k; for s=0.5, k=10: floor(5.0)=5, value=6/10=0.6
</pre>

</details>


## Parameter scenarios, estimands and truth

| Scenario | Estimand | Definition | Reported value | Evidence status |
|---|---|---|---|---|
| s01 | Pointwise conditional mean | Noncausal nonparametric regression function at the fixed query x*=0.5 for a selected source scenario s in {0.1,0.2,...,1.0}; the step function is p_s(x)=(floor(k*x)+1{x!=1})/k with k=15-10*s, yielding a piecewise-constant right-continuous function with k equal steps of height 1/k. The target is a conditional Bernoulli probability, not an intervention effect or a prediction interval. | 0.5714285714285714 | reported_numeric |
| s02 | Pointwise conditional mean | Noncausal nonparametric regression function at the fixed query x*=0.5 for a selected source scenario s in {0.1,0.2,...,1.0}; the step function is p_s(x)=(floor(k*x)+1{x!=1})/k with k=15-10*s, yielding a piecewise-constant right-continuous function with k equal steps of height 1/k. The target is a conditional Bernoulli probability, not an intervention effect or a prediction interval. | 0.5384615384615384 | reported_numeric |
| s03 | Pointwise conditional mean | Noncausal nonparametric regression function at the fixed query x*=0.5 for a selected source scenario s in {0.1,0.2,...,1.0}; the step function is p_s(x)=(floor(k*x)+1{x!=1})/k with k=15-10*s, yielding a piecewise-constant right-continuous function with k equal steps of height 1/k. The target is a conditional Bernoulli probability, not an intervention effect or a prediction interval. | 0.5833333333333334 | reported_numeric |
| s04 | Pointwise conditional mean | Noncausal nonparametric regression function at the fixed query x*=0.5 for a selected source scenario s in {0.1,0.2,...,1.0}; the step function is p_s(x)=(floor(k*x)+1{x!=1})/k with k=15-10*s, yielding a piecewise-constant right-continuous function with k equal steps of height 1/k. The target is a conditional Bernoulli probability, not an intervention effect or a prediction interval. | 0.5454545454545454 | reported_numeric |
| s05 | Pointwise conditional mean | Noncausal nonparametric regression function at the fixed query x*=0.5 for a selected source scenario s in {0.1,0.2,...,1.0}; the step function is p_s(x)=(floor(k*x)+1{x!=1})/k with k=15-10*s, yielding a piecewise-constant right-continuous function with k equal steps of height 1/k. The target is a conditional Bernoulli probability, not an intervention effect or a prediction interval. | 0.6 | reported_numeric |
| s06 | Pointwise conditional mean | Noncausal nonparametric regression function at the fixed query x*=0.5 for a selected source scenario s in {0.1,0.2,...,1.0}; the step function is p_s(x)=(floor(k*x)+1{x!=1})/k with k=15-10*s, yielding a piecewise-constant right-continuous function with k equal steps of height 1/k. The target is a conditional Bernoulli probability, not an intervention effect or a prediction interval. | 0.5555555555555556 | reported_numeric |
| s07 | Pointwise conditional mean | Noncausal nonparametric regression function at the fixed query x*=0.5 for a selected source scenario s in {0.1,0.2,...,1.0}; the step function is p_s(x)=(floor(k*x)+1{x!=1})/k with k=15-10*s, yielding a piecewise-constant right-continuous function with k equal steps of height 1/k. The target is a conditional Bernoulli probability, not an intervention effect or a prediction interval. | 0.625 | reported_numeric |
| s08 | Pointwise conditional mean | Noncausal nonparametric regression function at the fixed query x*=0.5 for a selected source scenario s in {0.1,0.2,...,1.0}; the step function is p_s(x)=(floor(k*x)+1{x!=1})/k with k=15-10*s, yielding a piecewise-constant right-continuous function with k equal steps of height 1/k. The target is a conditional Bernoulli probability, not an intervention effect or a prediction interval. | 0.5714285714285714 | reported_numeric |
| s09 | Pointwise conditional mean | Noncausal nonparametric regression function at the fixed query x*=0.5 for a selected source scenario s in {0.1,0.2,...,1.0}; the step function is p_s(x)=(floor(k*x)+1{x!=1})/k with k=15-10*s, yielding a piecewise-constant right-continuous function with k equal steps of height 1/k. The target is a conditional Bernoulli probability, not an intervention effect or a prediction interval. | 0.6666666666666666 | reported_numeric |
| s10 | Pointwise conditional mean | Noncausal nonparametric regression function at the fixed query x*=0.5 for a selected source scenario s in {0.1,0.2,...,1.0}; the step function is p_s(x)=(floor(k*x)+1{x!=1})/k with k=15-10*s, yielding a piecewise-constant right-continuous function with k equal steps of height 1/k. The target is a conditional Bernoulli probability, not an intervention effect or a prediction interval. | 0.6 | reported_numeric |

**Original submitted target notation:** m_s(x*) = E[Y \| X=x*] = p_s(x*)


## Identifiability assumptions

- Independent and identically distributed individual observations (X_i,Y_i).
- X has the source distribution Uniform[0,1] and the fixed query x*=0.5 lies in its support interior.
- Given X=x, Y is Bernoulli with success probability p_s(x)=(floor(k*x)+1{x!=1})/k; k=15-10*s is a positive integer in {5,...,14} for the declared scenarios.
- For every declared scenario s in {0.1,...,1.0}, p_s is nondecreasing and right-continuous on [0,1] with p_s(0)=1/k&gt;0 and p_s(1)=1, satisfying the monotonicity condition used for the source simultaneous-band method.
- The scalar truth is evaluated under the known DGP; no causal exchangeability, treatment, mediator, or interference assumption is relevant.

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Adaptations from the source (submitted, unverified):**

- Register s=0.1,0.2,...,1.0 as named scenarios (s=0 excluded per the source upper-step definition k=15-10*s in {5,...,14}); these are source parameter settings, not new mechanism families.
- Expose the scalar NRI target p_s(0.5)=E[Y\|X=0.5] required by the collection interface. The source studies simultaneous confidence bands under monotonicity, not this scalar truth hook.
- Run the collection smoke check instead of the source's 1000-replication coverage experiment; no confidence band, bootstrap, or coverage result is claimed.

**Warnings:**

- No explicit latent-variable metadata or reliably identifiable latent declarations; absence from this list does not prove that no latent variables exist.
