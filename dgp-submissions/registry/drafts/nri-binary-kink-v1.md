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

**Knot location**

```math
\text{ a }_{s} = 0.2 + 0.8s, s \in \{0,0.1,\ldots ,1\}
```

**Left linear segment for s&lt;1**

```math
p_{s}(x) = 0.2 x / \text{ a }_{s} \text{ for } 0\leq x\leq \text{ a }_{s}
```

**Right linear segment for s&lt;1**

```math
p_{s}(x) = 0.2 + 0.8 (x-\text{ a }_{s})/(1-\text{ a }_{s}) \text{ for } \text{ a }_{s}<x\leq 1
```

**Degenerate s=1 convention**

```math
\text{ a }_{1}=1
```

```math
p_{1}(x)=0.2x \text{ for } 0\leq x<1 \text{ and } p_{1}(1)=1 \text{ by } \mathrm{library} \mathrm{convention}
```

**Covariate and outcome**

```math
X_{i}\sim \mathrm{Uniform}[0,1] \text{ independently }
```

```math
Y_{i}\mid X_{i}=x\sim \mathrm{Bernoulli}(p_{s}(x)) \text{ independently }
```

**NRI scalar target**

```math
m_{s}(0.5)=\mathbb{E}[Y\mid X=0.5]=p_{s}(0.5)
```

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

<table>
<thead><tr><th>Scenario</th><th>Estimand</th><th>Definition</th><th>Reported value</th></tr></thead>
<tbody>
<tr>
<td>s00</td>
<td rowspan="11">Pointwise conditional mean</td>
<td rowspan="11">

$`\mathbb{E}[Y\mid X=0.5]`$

</td>
<td>0.5</td>
</tr>
<tr>
<td>s01</td>
<td>0.4444444444444444</td>
</tr>
<tr>
<td>s02</td>
<td>0.375</td>
</tr>
<tr>
<td>s03</td>
<td>0.2857142857142857</td>
</tr>
<tr>
<td>s04</td>
<td>0.19230769230769232</td>
</tr>
<tr>
<td>s05</td>
<td>0.16666666666666666</td>
</tr>
<tr>
<td>s06</td>
<td>0.1470588235294118</td>
</tr>
<tr>
<td>s07</td>
<td>0.13157894736842105</td>
</tr>
<tr>
<td>s08</td>
<td>0.11904761904761904</td>
</tr>
<tr>
<td>s09</td>
<td>0.10869565217391303</td>
</tr>
<tr>
<td>s10</td>
<td>0.1</td>
</tr>
</tbody>
</table>

**Definition notes**

- All scenarios: Under the scenario-specific data law.

<details>
<summary>Submitted estimand definitions</summary>

Submitted English definitions appear below; other original-language definitions remain in the linked JSON. Concise formulas above are display interpretations and still require scientific review.

**Scenario(s):** s00, s01, s02, s03, s04, s05, s06, s07, s08, s09, s10

Noncausal nonparametric regression function at the fixed query x*=0.5 for a selected source scenario s in {0,0.1,...,1}; p_s is the piecewise-linear interpolation through (0,0), (a_s,0.2), (1,1), with a_s=0.2+0.8s. This is a conditional Bernoulli probability, not an intervention effect or a prediction interval.

[Open raw scientific record (JSON)](./nri-binary-kink-v1.json).

</details>


**Original submitted target notation:** m_s(x*) = E[Y \| X=x*] = p_s(x*)


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

**Adaptations from the source (submitted, unverified):**

- Register the source shape grid s=0,0.1,...,1 as eleven named scenarios and use s=0.5 as the default; these are source parameter settings, not new mechanism families.
- Expose the scalar NRI target p_s(0.5)=E[Y\|X=0.5] required by the collection interface. The source studies simultaneous confidence bands over x, not this scalar truth hook.
- At the source-degenerate endpoint s=1 (a=1), define p_1(1)=1 as the library convention while retaining the first-segment value p_1(x)=0.2x for x&lt;1. This changes only the single endpoint value under continuous Uniform[0,1] sampling, but it changes an endpoint query truth.
- Run the collection smoke check instead of the source's 1000-replication coverage experiment; no confidence band, bootstrap, or coverage result is claimed.

**Warnings:**

- No explicit latent-variable metadata or reliably identifiable latent declarations; absence from this list does not prove that no latent variables exist.
