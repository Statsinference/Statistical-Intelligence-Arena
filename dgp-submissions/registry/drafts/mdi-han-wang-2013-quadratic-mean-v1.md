# MAR response with quadratic conditional mean and heteroscedastic noise

> **Unverified extraction — scientific review required.**

**Primary area:** Missing Data

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Han, P. and Wang, L. (2013). Estimation with missing data: beyond double robustness. Biometrika 100(2), 417–430. DOI: 10.1093/biomet/ass087.

**DOI:** 10.1093/biomet/ass087 · **Source locator:** Section 6, first of four data-generating models, journal p. 426 (PDF p. 10); Table 1, journal p. 427 (PDF p. 11), gives n=300,1000 and 5000 replications.

## DGP / generation mechanism

**Sampling design:** Unit: individual; Dependence: iid

**Generator source:** [generator.py](../generators/mdi-han-wang-2013-quadratic-mean-v1.py)

**Keywords (source-described):** Nonlinearity

**Observed variables**

X, R, Y_observed

**Latent variables**

Not explicitly identified (review required)

**Latent-variable identification:** not explicitly specified

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

**Covariate**

```math
X \sim \mathrm{Uniform}(-2.5,2.5)
```

**Full outcome**

```math
Y\mid X=x \sim \mathcal{N}(1+2x+3x^{2}, 4x^{2}+2), \text{ with } \mathrm{second} \mathrm{argument} \text{ variance }
```

**Observation**

```math
R\mid X=x \sim \mathrm{Bernoulli}(1/[1+\exp(0.8+0.5x-0.3x^{2})])
```

```math
R=1 \mathrm{means} \text{ observed }
```

**Observed encoding**

```math
Y_{\mathrm{observed}}=Y \text{ when } R=1 \text{ and } 0 \text{ placeholder } \text{ when } R=0
```

**Target**

```math
\theta=\mathbb{E}(Y)=7.25
```

<details>
<summary>Original source equations (verbatim)</summary>

<pre>
X ~ Uniform(-2.5,2.5)
Y|X=x ~ Normal(1+2x+3x^2, 4x^2+2), with second argument variance
R|X=x ~ Bernoulli(1/[1+exp(0.8+0.5x-0.3x^2)]); R=1 means observed
Y_observed=Y when R=1 and 0 placeholder when R=0
theta=E(Y)=7.25
</pre>

</details>


## Parameter scenarios, estimands and truth

<table>
<thead><tr><th>Scenario</th><th>Estimand</th><th>Definition</th><th>Reported value</th></tr></thead>
<tbody>
<tr>
<td>original</td>
<td rowspan="1">Full-data population outcome mean</td>
<td rowspan="1">

$`\mathbb{E}[Y]`$

</td>
<td>7.25</td>
</tr>
</tbody>
</table>

**Definition notes**

- All scenarios: Full-data superpopulation mean before outcome masking.

<details>
<summary>Submitted estimand definitions</summary>

Submitted English definitions appear below; other original-language definitions remain in the linked JSON. Concise formulas above are display interpretations and still require scientific review.

**Scenario(s):** original

Full-data superpopulation response mean before outcome masking.

[Open raw scientific record (JSON)](./mdi-han-wang-2013-quadratic-mean-v1.json).

</details>


**Original submitted target notation:** theta = E(Y)


## Identifiability assumptions

- X is fully observed Uniform(-2.5,2.5).
- Y\|X=x is normal with mean 1+2x+3x^2 and variance 4x^2+2.
- MAR: R is independent of Y conditional on X, and R=1 means Y is observed.
- Observation probability is strictly positive for all X in its compact support.

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Adaptations from the source (submitted, unverified):**

- One generate call returns one sample rather than all paper Monte Carlo repetitions.
- A finite zero placeholder encodes missing Y in the numeric-only interface; mask with the observation indicator.

**Warnings:**

- No explicit latent-variable metadata or reliably identifiable latent declarations; absence from this list does not prove that no latent variables exist.
