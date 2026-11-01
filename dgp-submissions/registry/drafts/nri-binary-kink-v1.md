# Kink binary regression functions from Dimitriadis et al. (2023)

> **Unverified extraction — scientific review required.**

**Primary area:** Nonparametric Regression

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Dimitriadis, T., Dümbgen, L., Henzi, A., Puke, M. and Ziegel, J. (2023). Honest calibration assessment for binary outcome predictions. Biometrika, 110(3), 663–680. DOI: 10.1093/biomet/asac068.

**DOI:** — · **Source locator:** DGP source actually checked in arXiv:2203.04065v2 (2022-11-02), PDF p.8, Section 5, item 3 (Kink): linear interpolation through (0,0), (0.2+0.8s,0.2), and (1,1); X~U[0,1] and Y~Bernoulli{p_s(X)} are specified on the same page. Supplementary Material PDF pp.17–20 covers rounding, application details, and proofs and does not state a changed kink DGP. The paper gives replication URL https://github.com/marius-cp/replication_DDHPZ22 but no fixed code commit. Formal Biometrika DGP differences were not checked.

## DGP / generation mechanism

**Sampling design:** Unit: individual observation (X_i,Y_i); Dependence: iid across observations; no cluster, panel, network, or within-unit dependence

**Generator source:** [generator.py](../generators/nri-binary-kink-v1.py)

**Keywords (source-described):** Nonlinearity

**Observed variables**

X, Y

**Latent variables**

Not explicitly identified (review required)

**Latent-variable identification:** not explicitly specified

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

$$
a_s = 0.2 + 0.8s, s in \{0,0.1,\ldots ,1\}
$$

$$
p_s(x) = 0.2 x / a_s for 0<=x<=a_s
$$

$$
p_s(x) = 0.2 + 0.8 (x-a_s)/(1-a_s) for a_s<x<=1
$$

$$
a_1=1
$$

$$
p_1(x)=0.2x for 0<=x<1 and p_1(1)=1 by library convention
$$

$$
X_i\sim Uniform[0,1] independently
$$

$$
Y_i\mid X_i=x\sim \mathrm{Bernoulli}(p_s(x)) independently
$$

$$
m_s(0.5)=\mathbb{E}[Y\mid X=0.5]=p_s(0.5)
$$

<details>
<summary>Original source equations (verbatim)</summary>

<pre>
a_s = 0.2 + 0.8s, s in {0,0.1,...,1}
p_s(x) = 0.2 x / a_s for 0&lt;=x&lt;=a_s
p_s(x) = 0.2 + 0.8 (x-a_s)/(1-a_s) for a_s&lt;x&lt;=1
a_1=1; p_1(x)=0.2x for 0&lt;=x&lt;1 and p_1(1)=1 by library convention
X_i~Uniform[0,1] independently; Y_i|X_i=x~Bernoulli(p_s(x)) independently
m_s(0.5)=E[Y|X=0.5]=p_s(0.5)
</pre>

</details>


## Parameter scenarios, estimands and truth

| Scenario | Estimand | Definition | True value | Evidence status |
|---|---|---|---|---|
| s00 | m_s(x*) = E[Y \| X=x*] = p_s(x*) | Noncausal nonparametric regression function at the fixed query x*=0.5 for a selected source scenario s in {0,0.1,...,1}; p_s is the piecewise-linear interpolation through (0,0), (a_s,0.2), (1,1), with a_s=0.2+0.8s. This is a conditional Bernoulli probability, not an intervention effect or a prediction interval. | 0.5 | reported_numeric |
| s01 | m_s(x*) = E[Y \| X=x*] = p_s(x*) | Noncausal nonparametric regression function at the fixed query x*=0.5 for a selected source scenario s in {0,0.1,...,1}; p_s is the piecewise-linear interpolation through (0,0), (a_s,0.2), (1,1), with a_s=0.2+0.8s. This is a conditional Bernoulli probability, not an intervention effect or a prediction interval. | 0.4444444444444444 | reported_numeric |
| s02 | m_s(x*) = E[Y \| X=x*] = p_s(x*) | Noncausal nonparametric regression function at the fixed query x*=0.5 for a selected source scenario s in {0,0.1,...,1}; p_s is the piecewise-linear interpolation through (0,0), (a_s,0.2), (1,1), with a_s=0.2+0.8s. This is a conditional Bernoulli probability, not an intervention effect or a prediction interval. | 0.375 | reported_numeric |
| s03 | m_s(x*) = E[Y \| X=x*] = p_s(x*) | Noncausal nonparametric regression function at the fixed query x*=0.5 for a selected source scenario s in {0,0.1,...,1}; p_s is the piecewise-linear interpolation through (0,0), (a_s,0.2), (1,1), with a_s=0.2+0.8s. This is a conditional Bernoulli probability, not an intervention effect or a prediction interval. | 0.2857142857142857 | reported_numeric |
| s04 | m_s(x*) = E[Y \| X=x*] = p_s(x*) | Noncausal nonparametric regression function at the fixed query x*=0.5 for a selected source scenario s in {0,0.1,...,1}; p_s is the piecewise-linear interpolation through (0,0), (a_s,0.2), (1,1), with a_s=0.2+0.8s. This is a conditional Bernoulli probability, not an intervention effect or a prediction interval. | 0.19230769230769232 | reported_numeric |
| s05 | m_s(x*) = E[Y \| X=x*] = p_s(x*) | Noncausal nonparametric regression function at the fixed query x*=0.5 for a selected source scenario s in {0,0.1,...,1}; p_s is the piecewise-linear interpolation through (0,0), (a_s,0.2), (1,1), with a_s=0.2+0.8s. This is a conditional Bernoulli probability, not an intervention effect or a prediction interval. | 0.16666666666666666 | reported_numeric |
| s06 | m_s(x*) = E[Y \| X=x*] = p_s(x*) | Noncausal nonparametric regression function at the fixed query x*=0.5 for a selected source scenario s in {0,0.1,...,1}; p_s is the piecewise-linear interpolation through (0,0), (a_s,0.2), (1,1), with a_s=0.2+0.8s. This is a conditional Bernoulli probability, not an intervention effect or a prediction interval. | 0.1470588235294118 | reported_numeric |
| s07 | m_s(x*) = E[Y \| X=x*] = p_s(x*) | Noncausal nonparametric regression function at the fixed query x*=0.5 for a selected source scenario s in {0,0.1,...,1}; p_s is the piecewise-linear interpolation through (0,0), (a_s,0.2), (1,1), with a_s=0.2+0.8s. This is a conditional Bernoulli probability, not an intervention effect or a prediction interval. | 0.13157894736842105 | reported_numeric |
| s08 | m_s(x*) = E[Y \| X=x*] = p_s(x*) | Noncausal nonparametric regression function at the fixed query x*=0.5 for a selected source scenario s in {0,0.1,...,1}; p_s is the piecewise-linear interpolation through (0,0), (a_s,0.2), (1,1), with a_s=0.2+0.8s. This is a conditional Bernoulli probability, not an intervention effect or a prediction interval. | 0.11904761904761904 | reported_numeric |
| s09 | m_s(x*) = E[Y \| X=x*] = p_s(x*) | Noncausal nonparametric regression function at the fixed query x*=0.5 for a selected source scenario s in {0,0.1,...,1}; p_s is the piecewise-linear interpolation through (0,0), (a_s,0.2), (1,1), with a_s=0.2+0.8s. This is a conditional Bernoulli probability, not an intervention effect or a prediction interval. | 0.10869565217391303 | reported_numeric |
| s10 | m_s(x*) = E[Y \| X=x*] = p_s(x*) | Noncausal nonparametric regression function at the fixed query x*=0.5 for a selected source scenario s in {0,0.1,...,1}; p_s is the piecewise-linear interpolation through (0,0), (a_s,0.2), (1,1), with a_s=0.2+0.8s. This is a conditional Bernoulli probability, not an intervention effect or a prediction interval. | 0.1 | reported_numeric |

## Identifiability assumptions

- Independent and identically distributed individual observations (X_i,Y_i).
- X has the source distribution Uniform[0,1] and the fixed query x*=0.5 lies in its support.
- Given X=x, Y is Bernoulli with success probability p_s(x); for s&lt;1 the two linear pieces meet at a_s and have endpoint values 0 and 1.
- At s=1, the source anchors have coincident x-coordinate a_1=1; this contribution uses the declared library convention p_1(1)=1 and p_1(x)=0.2x for x&lt;1.
- For every declared scenario s in [0,1], p_s is nondecreasing on [0,1] under the stated endpoint convention, matching the monotonicity condition used for the source simultaneous-band method.
- The scalar truth is evaluated under the known DGP; no causal exchangeability, treatment, mediator, or interference assumption is relevant.

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Warnings:**

- No explicit latent-variable metadata or reliably identifiable latent declarations; absence from this list does not prove that no latent variables exist.
