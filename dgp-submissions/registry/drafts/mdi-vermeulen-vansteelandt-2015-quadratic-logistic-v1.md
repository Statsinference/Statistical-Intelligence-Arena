# Quadratic mean response with logistic MAR selection

> **Unverified extraction — scientific review required.**

**Primary area:** Missing Data

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Vermeulen, K. and Vansteelandt, S. (2015). Bias-reduced doubly robust estimation. Journal of the American Statistical Association 110(511), 1024-1036. DOI: 10.1080/01621459.2014.958155.

**DOI:** 10.1080/01621459.2014.958155 · **Source locator:** Section 4.1, Scenario 1, journal pp. 1029-1030 / PDF pp. 7-8; quadratic mean and logistic propensity with xi=1.

## DGP / generation mechanism

**Sampling design:** Unit: individual; Dependence: iid

**Generator source:** [generator.py](../generators/mdi-vermeulen-vansteelandt-2015-quadratic-logistic-v1.py)

**Keywords (source-described):** Nonlinearity

**Observed variables**

X, R, Y_observed

**Latent variables**

Not explicitly identified (review required)

**Latent-variable identification:** not explicitly specified

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

**Full data and observation**

```math
X\sim \mathcal{N}(0,1)
```

```math
Y\mid X=x\sim \mathcal{N}(x^{2},1)
```

```math
R\mid X=x\sim \mathrm{Bernoulli}(\mathrm{expit}(x)).
```

**Observed encoding**

```math
Y_{\mathrm{observed}}=Y \text{ when } R=1, \text{ and } \mathrm{finite} 0 \text{ placeholder } \text{ when } R=0.
```

**Target**

```math
\theta=\mathbb{E}(Y)=1
```

<details>
<summary>Original source equations (verbatim)</summary>

<pre>
X~N(0,1); Y|X=x~N(x^2,1); R|X=x~Bernoulli(expit(x)).
Y_observed=Y when R=1, and finite 0 placeholder when R=0.
theta=E(Y)=1
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
<td>1.0</td>
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

[Open raw scientific record (JSON)](./mdi-vermeulen-vansteelandt-2015-quadratic-logistic-v1.json).

</details>


**Original submitted target notation:** theta = E(Y)


## Identifiability assumptions

- Covariates are fully observed.
- R is conditionally independent of Y given fully observed covariates (MAR).
- R=1 means Y is observed.
- Observation probabilities are positive.

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Adaptations from the source (submitted, unverified):**

- One generate call returns one iid sample instead of the paper's 1000 Monte Carlo runs.
- R=0 uses a finite zero placeholder in the numeric interface; mask it by R.

**Warnings:**

- No explicit latent-variable metadata or reliably identifiable latent declarations; absence from this list does not prove that no latent variables exist.
