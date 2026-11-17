# Binary-outcome observational ATE design with nonlinear treatment and outcome regressions

> **Unverified extraction — scientific review required.**

**Primary area:** ATE — Average Treatment Effect

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Benkeser, D., Carone, M., van der Laan, M. J. and Gilbert, P. B. (2017). Doubly robust nonparametric inference on the average treatment effect. Biometrika 104(4), 863–880. DOI: 10.1093/biomet/asx053.

**DOI:** 10.1093/biomet/asx053 · **Source locator:** Section 5.1, 'Data-generating mechanism and crossvalidation set-up'; PMC full-text HTML lines 301–304; printed journal pages approximately 870–871. Equations are unnumbered in the prose. PDF page number not visually verified in this run. Exact expressions transcribed from PMC full-text text rendering.

## DGP / generation mechanism

**Sampling design:** Unit: individual; Dependence: iid individuals; within individual, A depends on W and Y depends on (A,W); W1 and W2 are mutually independent as specified in Section 5.1.

**Generator source:** [generator.py](../generators/ate-benkser-carone-vdl-gilbert-2017-dr-v1.py)

**Keywords (source-described):** Interactions · Nonlinearity

**Observed variables**

W1, W2, A, Y

**Latent variables**

Not explicitly identified (review required)

**Latent-variable identification:** not explicitly specified

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

**Baseline covariate W1**

```math
W_{1} \sim \mathrm{Uniform}(-2, 2)
```

**Baseline covariate W2**

```math
W_{2} \sim \mathrm{Bernoulli}(1/2)
```

independent of W1

**Treatment assignment**

```math
A \mid  W=(w_{1},w_{2}) \sim \mathrm{Bernoulli}(g_{0}(w_{1},w_{2}))
```

```math
g_{0}(w_{1},w_{2})=\mathrm{expit}(-w_{1} + 2\cdot w_{1}\cdot w_{2})
```

**Binary outcome**

```math
Y \mid  A=\text{ a },W=w \sim \mathrm{Bernoulli}(\mathrm{Qbar0}(\text{ a },w))
```

```math
\mathrm{Qbar0}(\text{ a },w)=\mathrm{expit}(0.2\cdot \text{ a } - w_{1} + 2\cdot w_{1}\cdot w_{2})
```

<details>
<summary>Original source equations (verbatim)</summary>

<pre>
W1 ~ Uniform(-2, 2)
W2 ~ Bernoulli(1/2), independent of W1
A | W=(w1,w2) ~ Bernoulli(g0(w1,w2)); g0(w1,w2)=expit(-w1 + 2*w1*w2)
Y | A=a,W=w ~ Bernoulli(Qbar0(a,w)); Qbar0(a,w)=expit(0.2*a - w1 + 2*w1*w2)
</pre>

</details>


## Parameter scenarios, estimands and truth

<table>
<thead><tr><th>Scenario</th><th>Estimand</th><th>Definition</th><th>Reported value</th></tr></thead>
<tbody>
<tr>
<td>section51_original</td>
<td rowspan="1">ATE</td>
<td rowspan="1">

$`\mathbb{E}[Y(1)-Y(0)]`$

</td>
<td>0.03802642731065545</td>
</tr>
</tbody>
</table>

**Definition notes**

- All scenarios: Population ATE; expectation is over the DGP's full population.

<details>
<summary>Submitted estimand definitions</summary>

Submitted English definitions appear below; other original-language definitions remain in the linked JSON. Concise formulas above are display interpretations and still require scientific review.

**Scenario(s):** section51_original

Population risk difference under interventions setting A=1 versus A=0, averaged over the source covariate distribution W=(W1,W2).

[Open raw scientific record (JSON)](./ate-benkser-carone-vdl-gilbert-2017-dr-v1.json).

</details>


**Original submitted target notation:** ATE = E[Y(1)-Y(0)]


## Identifiability assumptions

- Consistency and well-defined binary treatment interventions.
- Conditional exchangeability: (Y(0),Y(1)) independent of A given W.
- Positivity: 0 &lt; P(A=1\|W=w) &lt; 1 on the support of W; here the expit probability is strictly between zero and one for every finite w in the bounded support.
- Independent sampling of individuals; no interference.

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** exact_reproduction

**Status:** needs_scientific_review

**Adaptations from the source (submitted, unverified):**

- None described in the submitted metadata; this does not establish exact reproduction.

**Warnings:**

- No explicit latent-variable metadata or reliably identifiable latent declarations; absence from this list does not prove that no latent variables exist.
