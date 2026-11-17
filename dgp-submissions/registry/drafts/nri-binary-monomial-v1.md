# Monomial binary regression functions from Dimitriadis et al. (2023)

> **Unverified extraction — scientific review required.**

**Primary area:** Nonparametric Regression

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Dimitriadis, T., Dümbgen, L., Henzi, A., Puke, M. and Ziegel, J. (2023). Honest calibration assessment for binary outcome predictions. Biometrika, 110(3), 663–680. DOI: 10.1093/biomet/asac068.

**DOI:** — · **Source locator:** DGP source actually checked in arXiv:2203.04065v2 (2022-11-02), PDF p.8, Section 5, item 1 (Monomial); X~U[0,1] and Y~Bernoulli{p_s(X)} on the same page. The paper gives replication URL https://github.com/marius-cp/replication_DDHPZ22 but no fixed code commit. Formal Biometrika DGP differences were not checked.

## DGP / generation mechanism

**Sampling design:** Unit: individual observation (X_i,Y_i); Dependence: iid across observations; no cluster, panel, network, or within-unit dependence

**Generator source:** [generator.py](../generators/nri-binary-monomial-v1.py)

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

**Monomial regression function**

```math
p_{s}(x) = x^{1-s}, s \in \{0,0.1,\ldots ,1\}\setminus \{1\}
```

**Binary outcome**

```math
Y_{i} \mid  X_{i}=x \sim \mathrm{Bernoulli}(p_{s}(x)) \text{ independently }
```

**NRI scalar target**

```math
m_{s}(0.5) = \mathbb{E}[Y \mid  X=0.5] = p_{s}(0.5) = 0.5^{1-s}
```

<details>
<summary>Original source equations (verbatim)</summary>

<pre>
X_i ~ Uniform[0,1] independently
p_s(x) = x^(1-s), s in {0,0.1,...,1}\{1}
Y_i | X_i=x ~ Bernoulli(p_s(x)) independently
m_s(0.5) = E[Y | X=0.5] = p_s(0.5) = 0.5^(1-s)
</pre>

</details>


## Parameter scenarios, estimands and truth

<table>
<thead><tr><th>Scenario</th><th>Estimand</th><th>Definition</th><th>Reported value</th></tr></thead>
<tbody>
<tr>
<td>s00</td>
<td rowspan="10">Pointwise conditional mean</td>
<td rowspan="10">

$`\mathbb{E}[Y\mid X=0.5]`$

</td>
<td>0.5</td>
</tr>
<tr>
<td>s01</td>
<td>0.5358867312681466</td>
</tr>
<tr>
<td>s02</td>
<td>0.5743491774985174</td>
</tr>
<tr>
<td>s03</td>
<td>0.6155722066724582</td>
</tr>
<tr>
<td>s04</td>
<td>0.6597539553864471</td>
</tr>
<tr>
<td>s05</td>
<td>0.7071067811865476</td>
</tr>
<tr>
<td>s06</td>
<td>0.757858283255199</td>
</tr>
<tr>
<td>s07</td>
<td>0.8122523963562355</td>
</tr>
<tr>
<td>s08</td>
<td>0.8705505632961241</td>
</tr>
<tr>
<td>s09</td>
<td>0.9330329915368074</td>
</tr>
</tbody>
</table>

**Definition notes**

- All scenarios: Under the scenario-specific data law.

<details>
<summary>Submitted estimand definitions</summary>

Submitted English definitions appear below; other original-language definitions remain in the linked JSON. Concise formulas above are display interpretations and still require scientific review.

**Scenario(s):** s00, s01, s02, s03, s04, s05, s06, s07, s08, s09

Noncausal nonparametric regression function at the fixed query x*=0.5 for a selected source scenario s in {0,0.1,...,0.9}; with p_s(x)=x^(1-s), the target is p_s(0.5). This is a conditional Bernoulli probability, not an intervention effect or a prediction interval.

[Open raw scientific record (JSON)](./nri-binary-monomial-v1.json).

</details>


**Original submitted target notation:** m_s(x*) = E[Y \| X=x*] = p_s(x*)


## Identifiability assumptions

- Independent and identically distributed individual observations (X_i,Y_i).
- X has the source distribution Uniform[0,1] and the fixed query x*=0.5 lies in its support interior.
- Given X=x, Y is Bernoulli with success probability p_s(x)=x^(1-s); s&lt;1 ensures the declared source scenarios are defined.
- For every declared scenario s&lt;=0.9, p_s is nondecreasing on [0,1], matching the monotonicity condition used for the source simultaneous-band method.
- The scalar truth is evaluated under the known DGP; no causal exchangeability, treatment, mediator, or interference assumption is relevant.

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Adaptations from the source (submitted, unverified):**

- Register s=0,0.1,...,0.9 as named scenarios and use s=0.5 as the default scenario; these are source parameter settings, not new mechanism families.
- Expose the scalar NRI target p_s(0.5)=E[Y\|X=0.5] required by the collection interface. The source studies simultaneous confidence bands over x, not this scalar truth hook.
- Run the collection smoke check instead of the source's 1000-replication coverage experiment; no confidence band, bootstrap, or coverage result is claimed.

**Warnings:**

- No explicit latent-variable metadata or reliably identifiable latent declarations; absence from this list does not prove that no latent variables exist.
