# S-shaped binary regression functions from Dimitriadis et al. (2023)

> **Unverified extraction — scientific review required.**

**Primary area:** Nonparametric Regression

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Dimitriadis, T., Dümbgen, L., Henzi, A., Puke, M. and Ziegel, J. (2023). Honest calibration assessment for binary outcome predictions. Biometrika, 110(3), 663–680. DOI: 10.1093/biomet/asac068.

**DOI:** — · **Source locator:** DGP source actually checked in arXiv:2203.04065v2 (2022-11-02), PDF p.8, Section 5, item 2 (S-shaped); X~U[0,1] and Y~Bernoulli{p_s(X)} are specified on the same page. Supplementary Material PDF pp.17–20 covers rounding, application details, and proofs and does not state a changed S-shaped DGP. The paper gives replication URL https://github.com/marius-cp/replication_DDHPZ22 but no fixed code commit. Formal Biometrika DGP differences were not checked.

## DGP / generation mechanism

**Sampling design:** Unit: individual observation (X_i,Y_i); Dependence: iid across observations; no cluster, panel, network, or within-unit dependence

**Generator source:** [generator.py](../generators/nri-binary-s-shape-v1.py)

**Keywords (source-described):** Nonlinearity

**Observed variables**

X, Y

**Latent variables**

Not explicitly identified (review required)

**Latent-variable identification:** not explicitly specified

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

**Covariate**

```math
X_{i} \sim \mathrm{Uniform}[0,1] \text{ independently }
```

**S-shaped regression function (source form)**

```math
p_{s}(x) = [1 + ((1-x)/x)^{1+s}]^{-1}, s \in \{0,0.1,\ldots ,1\}, 0<x<1
```

```math
p_{s}(0)=0 \text{ and } p_{s}(1)=1 \text{ by } \mathrm{limits}
```

**S-shaped regression function (endpoint-safe equivalent)**

```math
p_{s}(x) = x^{1+s} / (x^{1+s} + (1-x)^{1+s}), \text{ with } \text{ endpoint } \mathrm{values} 0 \text{ and } 1
```

**Binary outcome**

```math
Y_{i} \mid  X_{i}=x \sim \mathrm{Bernoulli}(p_{s}(x)) \text{ independently }
```

**NRI scalar target**

```math
m_{s}(0.5) = \mathbb{E}[Y \mid  X=0.5] = p_{s}(0.5) = 0.5 \text{ for } \mathrm{every} \mathrm{declared} s
```

<details>
<summary>Original source equations (verbatim)</summary>

<pre>
X_i ~ Uniform[0,1] independently
p_s(x) = [1 + ((1-x)/x)^(1+s)]^(-1), s in {0,0.1,...,1}, 0&lt;x&lt;1; p_s(0)=0 and p_s(1)=1 by limits
p_s(x) = x^(1+s) / (x^(1+s) + (1-x)^(1+s)), with endpoint values 0 and 1
Y_i | X_i=x ~ Bernoulli(p_s(x)) independently
m_s(0.5) = E[Y | X=0.5] = p_s(0.5) = 0.5 for every declared s
</pre>

</details>


## Parameter scenarios, estimands and truth

| Scenario | Estimand | Definition | Reported value |
|---|---|---|---|
| s00 | Pointwise conditional mean | Noncausal nonparametric regression function at the fixed query x*=0.5 for a selected source scenario s in {0,0.1,...,1}; with p_s(x)=[1+{(1-x)/x}^(1+s)]^(-1), the target is p_s(0.5). This is a conditional Bernoulli probability, not an intervention effect or a prediction interval. | 0.5 |
| s01 | Pointwise conditional mean | Noncausal nonparametric regression function at the fixed query x*=0.5 for a selected source scenario s in {0,0.1,...,1}; with p_s(x)=[1+{(1-x)/x}^(1+s)]^(-1), the target is p_s(0.5). This is a conditional Bernoulli probability, not an intervention effect or a prediction interval. | 0.5 |
| s02 | Pointwise conditional mean | Noncausal nonparametric regression function at the fixed query x*=0.5 for a selected source scenario s in {0,0.1,...,1}; with p_s(x)=[1+{(1-x)/x}^(1+s)]^(-1), the target is p_s(0.5). This is a conditional Bernoulli probability, not an intervention effect or a prediction interval. | 0.5 |
| s03 | Pointwise conditional mean | Noncausal nonparametric regression function at the fixed query x*=0.5 for a selected source scenario s in {0,0.1,...,1}; with p_s(x)=[1+{(1-x)/x}^(1+s)]^(-1), the target is p_s(0.5). This is a conditional Bernoulli probability, not an intervention effect or a prediction interval. | 0.5 |
| s04 | Pointwise conditional mean | Noncausal nonparametric regression function at the fixed query x*=0.5 for a selected source scenario s in {0,0.1,...,1}; with p_s(x)=[1+{(1-x)/x}^(1+s)]^(-1), the target is p_s(0.5). This is a conditional Bernoulli probability, not an intervention effect or a prediction interval. | 0.5 |
| s05 | Pointwise conditional mean | Noncausal nonparametric regression function at the fixed query x*=0.5 for a selected source scenario s in {0,0.1,...,1}; with p_s(x)=[1+{(1-x)/x}^(1+s)]^(-1), the target is p_s(0.5). This is a conditional Bernoulli probability, not an intervention effect or a prediction interval. | 0.5 |
| s06 | Pointwise conditional mean | Noncausal nonparametric regression function at the fixed query x*=0.5 for a selected source scenario s in {0,0.1,...,1}; with p_s(x)=[1+{(1-x)/x}^(1+s)]^(-1), the target is p_s(0.5). This is a conditional Bernoulli probability, not an intervention effect or a prediction interval. | 0.5 |
| s07 | Pointwise conditional mean | Noncausal nonparametric regression function at the fixed query x*=0.5 for a selected source scenario s in {0,0.1,...,1}; with p_s(x)=[1+{(1-x)/x}^(1+s)]^(-1), the target is p_s(0.5). This is a conditional Bernoulli probability, not an intervention effect or a prediction interval. | 0.5 |
| s08 | Pointwise conditional mean | Noncausal nonparametric regression function at the fixed query x*=0.5 for a selected source scenario s in {0,0.1,...,1}; with p_s(x)=[1+{(1-x)/x}^(1+s)]^(-1), the target is p_s(0.5). This is a conditional Bernoulli probability, not an intervention effect or a prediction interval. | 0.5 |
| s09 | Pointwise conditional mean | Noncausal nonparametric regression function at the fixed query x*=0.5 for a selected source scenario s in {0,0.1,...,1}; with p_s(x)=[1+{(1-x)/x}^(1+s)]^(-1), the target is p_s(0.5). This is a conditional Bernoulli probability, not an intervention effect or a prediction interval. | 0.5 |
| s10 | Pointwise conditional mean | Noncausal nonparametric regression function at the fixed query x*=0.5 for a selected source scenario s in {0,0.1,...,1}; with p_s(x)=[1+{(1-x)/x}^(1+s)]^(-1), the target is p_s(0.5). This is a conditional Bernoulli probability, not an intervention effect or a prediction interval. | 0.5 |

**Original submitted target notation:** m_s(x*) = E[Y \| X=x*] = p_s(x*)


## Identifiability assumptions

- Independent and identically distributed individual observations (X_i,Y_i).
- X has the source distribution Uniform[0,1] and the fixed query x*=0.5 lies in its support interior.
- Given X=x, Y is Bernoulli with success probability p_s(x); at x=0 and x=1 the regression function is defined by the continuous endpoint limits 0 and 1.
- For every declared scenario s&gt;=0, p_s is nondecreasing on [0,1] and smooth on (0,1), matching the monotonicity condition used for the source simultaneous-band method.
- The scalar truth is evaluated under the known DGP; no causal exchangeability, treatment, mediator, or interference assumption is relevant.

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Adaptations from the source (submitted, unverified):**

- Register the source shape grid s=0,0.1,...,1 as eleven named scenarios and use s=0.5 as the default; these are source parameter settings, not new mechanism families.
- Expose the scalar NRI target p_s(0.5)=E[Y\|X=0.5] required by the collection interface. The source studies simultaneous confidence bands over x, not this scalar truth hook.
- Implement the algebraically equivalent endpoint-safe formula x^(1+s)/(x^(1+s)+(1-x)^(1+s)) and run the collection smoke check instead of the source's 1000-replication coverage experiment; no confidence band, bootstrap, or coverage result is claimed.

**Warnings:**

- No explicit latent-variable metadata or reliably identifiable latent declarations; absence from this list does not prove that no latent variables exist.
