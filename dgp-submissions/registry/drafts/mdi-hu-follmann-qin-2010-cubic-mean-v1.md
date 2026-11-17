# MAR mean response with a cubic outcome regression

> **Unverified extraction — scientific review required.**

**Primary area:** Missing Data

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Hu, Z., Follmann, D. A. and Qin, J. (2010). Semiparametric dimension reduction estimation for mean response with missing data. Biometrika 97(2), 305–319. DOI: 10.1093/biomet/asq005.

**DOI:** — · **Source locator:** Section 4, Simulation studies, first simulation, paragraph beginning 'In the first simulation'; journal p. 311, PDF p. 7 of the 15-page PMC article PDF (asq005.pdf).

## DGP / generation mechanism

**Sampling design:** Unit: individual; Dependence: iid

**Generator source:** [generator.py](../generators/mdi-hu-follmann-qin-2010-cubic-mean-v1.py)

**Keywords (source-described):** Interactions · Nonlinearity

**Observed variables**

X1, X2, R, Y_observed

**Latent variables**

Not explicitly identified (review required)

**Latent-variable identification:** not explicitly specified

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

**Covariates**

```math
X_{1},X_{2} \text{ independently } \sim \mathcal{N}(0,1)
```

**Full outcome**

```math
Y\mid X \sim \mathcal{N}((X_{1}+X_{2})^{3},1)
```

**Observation**

```math
R\mid X \sim \mathrm{Bernoulli}(\pi(X)), \pi(X)=1-1/[1+\exp(1-3X_{1}+2X_{2}^{2})]=\mathrm{expit}(1-3X_{1}+2X_{2}^{2})
```

R

independent of Y given X

**Observed encoding**

```math
Y_{\mathrm{observed}}=Y \text{ if } R=1, \text{ otherwise } 0 \text{ placeholder }
```

**Target**

```math
\theta=\mathbb{E}(Y)=\mathbb{E}[(X_{1}+X_{2})^{3}]=0
```

<details>
<summary>Original source equations (verbatim)</summary>

<pre>
X1,X2 independently ~ N(0,1)
Y|X ~ N((X1+X2)^3,1)
R|X ~ Bernoulli(pi(X)), pi(X)=1-1/[1+exp(1-3X1+2X2^2)]=expit(1-3X1+2X2^2); R independent of Y given X
Y_observed=Y if R=1, otherwise 0 placeholder
theta=E(Y)=E[(X1+X2)^3]=0
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
<td>0.0</td>
</tr>
</tbody>
</table>

**Definition notes**

- All scenarios: Full-data superpopulation mean before outcome masking.

<details>
<summary>Submitted estimand definitions</summary>

Submitted English definitions appear below; other original-language definitions remain in the linked JSON. Concise formulas above are display interpretations and still require scientific review.

**Scenario(s):** original

Marginal full-data response mean in the iid superpopulation, before outcome masking.

[Open raw scientific record (JSON)](./mdi-hu-follmann-qin-2010-cubic-mean-v1.json).

</details>


**Original submitted target notation:** theta = E(Y)


## Identifiability assumptions

- Individuals iid; X1 and X2 independent N(0,1).
- MAR: R independent of Y conditional on fully observed X1,X2.
- P(R=1\|X)&gt;0 at every finite X, without a uniform lower bound over Gaussian support.
- Independent mean-zero outcome noise.

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Adaptations from the source (submitted, unverified):**

- One call generates one sample instead of repeating the paper's n=500 simulation 1000 times.
- R=0 and finite Y_observed=0 encode missing Y for the numeric-only interface; always mask using R.

**Warnings:**

- No explicit latent-variable metadata or reliably identifiable latent declarations; absence from this list does not prove that no latent variables exist.
