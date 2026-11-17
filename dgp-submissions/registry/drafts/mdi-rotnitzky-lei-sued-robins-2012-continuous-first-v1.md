# MAR continuous response, first Kang-Schafer experiment in Rotnitzky et al. 2012

> **Unverified extraction — scientific review required.**

**Primary area:** Missing Data

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Rotnitzky, A., Lei, Q., Sued, M. and Robins, J. M. (2012). Improved double-robust estimation in missing data and causal inference models. Biometrika 99(2), 439–456. DOI: 10.1093/biomet/ass013.

**DOI:** — · **Source locator:** Section 5, first continuous-outcome experiment, journal pp. 451–452; Table 1 journal p. 453. The authors explicitly credit the Kang and Schafer (2007) design.

## DGP / generation mechanism

**Sampling design:** Unit: individual; Dependence: iid

**Generator source:** [generator.py](../generators/mdi-rotnitzky-lei-sued-robins-2012-continuous-first-v1.py)

**Keywords (source-described):** Nonlinearity

**Observed variables**

L1–L4 (4 variables), A, Y_observed

<details>
<summary>All observed variable names</summary>

L1, L2, L3, L4, A, Y_observed

</details>

**Latent variables**

Not explicitly identified (review required)

**Latent-variable identification:** not explicitly specified

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

**Covariates and noise**

```math
(L_{1},L_{2},L_{3},L_{4},\varepsilon) \sim \mathcal{N}(0,I_{5})
```

**Full outcome**

```math
Y=210+27.4L_{1}+13.7(L_{2}+L_{3}+L_{4})+\varepsilon
```

**Observation**

```math
A\mid L\sim \mathrm{Bernoulli}(\mathrm{expit}(-L_{1}+0.5L_{2}-0.25L_{3}-0.1L_{4}))
```

```math
A=1 \mathrm{means} Y \text{ observed }
```

**Observed encoding**

```math
Y_{\mathrm{observed}}=Y \text{ if } A=1, \text{ otherwise } \mathrm{finite} \mathrm{zero} \text{ placeholder }
```

**Target**

```math
\beta_{0}=\mathbb{E}(Y)=210
```

<details>
<summary>Original source equations (verbatim)</summary>

<pre>
(L1,L2,L3,L4,epsilon) ~ N(0,I5)
Y=210+27.4L1+13.7(L2+L3+L4)+epsilon
A|L~Bernoulli(expit(-L1+0.5L2-0.25L3-0.1L4)); A=1 means Y observed
Y_observed=Y if A=1, otherwise finite zero placeholder
beta_0=E(Y)=210
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
<td>210.0</td>
</tr>
</tbody>
</table>

**Definition notes**

- All scenarios: Full-data superpopulation mean before outcome masking.

<details>
<summary>Submitted estimand definitions</summary>

Submitted English definitions appear below; other original-language definitions remain in the linked JSON. Concise formulas above are display interpretations and still require scientific review.

**Scenario(s):** original

Full-data superpopulation mean of continuous Y before missingness.

[Open raw scientific record (JSON)](./mdi-rotnitzky-lei-sued-robins-2012-continuous-first-v1.json).

</details>


**Original submitted target notation:** beta_0 = E(Y)


## Identifiability assumptions

- (L1,L2,L3,L4,epsilon) have independent standard-normal components.
- Y=210+27.4 L1+13.7(L2+L3+L4)+epsilon.
- A is the observation indicator and A\|L~Bernoulli(expit(-L1+0.5L2-0.25L3-0.1L4)); conditional on L, A is independent of epsilon and Y.
- MAR given fully observed L; selection probability positive for every finite L, without a uniform lower bound on Gaussian support.

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Adaptations from the source (submitted, unverified):**

- One generate call produces one sample instead of paper n=200 or 1000 with 1000 Monte Carlo datasets.
- Finite zero placeholder encodes missing Y; use A as its mask.
- Auxiliary transformed X variables used only to fit intentionally misspecified working estimators are not output; fully observed L and the outcome/missingness mechanism are preserved.

**Warnings:**

- No explicit latent-variable metadata or reliably identifiable latent declarations; absence from this list does not prove that no latent variables exist.
