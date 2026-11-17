# Transformed Gaussian covariates and latent-linear outcomes

> **Unverified extraction — scientific review required.**

**Primary area:** ATE — Average Treatment Effect

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Ming-Yueh Huang and Kwun Chuen Gary Chan (2017). Joint sufficient dimension reduction and estimation of conditional and average treatment effects. Biometrika, 104(3):583–596. DOI 10.1093/biomet/asx028

**DOI:** 10.1093/biomet/asx028 · **Source locator:** Supplement asx028_supp.pdf Section 3.1, PDF/printed p.4, unnumbered Setting 1 and Setting 2 paragraphs; Section 3.4 PDF/printed p.6 for both reported ATEs = 1; main article Section 2.1 PDF p.3 / journal p.585 for estimand and assumptions; collected second setting

## DGP / generation mechanism

**Sampling design:** Unit: independent individual; Dependence: Three observed covariates affect assignment/outcomes. Do not add +10 to X2 and do not square X4: those are different Kang–Schafer variants, not this source. Internal Z1–Z3 are not learner inputs. Noise definition is inherited from the immediately preceding sentence; this explicit scope interpretation is flagged for human review. Independent treatment/noise random draws conditional on covariates; no clusters or panel structure.

**Generator source:** [generator.py](../generators/ate-huang-chan-2017-05-19-setting-2-v1.py)

**Keywords (source-described):** Interactions · Nonlinearity

**Observed variables**

X1–X10 (10 variables), A, Y, Z1, Z2, Z3

<details>
<summary>All observed variable names</summary>

X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, A, Y, Z1, Z2, Z3

</details>

**Latent variables**

Z1,...,Z10

**Latent-variable identification:** explicit structured metadata

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

```math
Z_{1},\ldots ,Z_{10}\overset{\mathrm{iid}}{\sim} \mathcal{N}(0,1).
```

```math
X_{1}=\exp(Z_{1}/2)
```

```math
X_{2}=Z_{2}/(1+\exp(Z_{1}))
```

```math
X_{3}=(Z_{1}\cdot Z_{3}/25+3/5)^{3}
```

```math
X_{4},\ldots ,X_{10}=Z_{4},\ldots ,Z_{10}.
```

```math
p(X)=\mathrm{expit}(X_{1}-X_{2}+X_{3})
```

```math
A\mid X\sim \mathrm{Bernoulli}(p).
```

```math
Y^{(1)}=1+Z_{1}+\varepsilon_{1}
```

```math
Y^{(0)}=Z_{2}+\varepsilon_{0}
```

epsilon0,epsilon1 as defined in the same paragraph, N(0,1/10) independently

```math
Y=A\cdot Y^{(1)}+(1-A)\cdot Y^{(0)}.
```

<details>
<summary>Original source equations (verbatim)</summary>

<pre>
Z1,...,Z10 iid N(0,1).
X1=exp(Z1/2); X2=Z2/(1+exp(Z1)); X3=(Z1*Z3/25+3/5)**3; X4,...,X10=Z4,...,Z10.
p(X)=expit(X1-X2+X3); A|X~Bernoulli(p).
Y(1)=1+Z1+epsilon1; Y(0)=Z2+epsilon0; epsilon0,epsilon1 as defined in the same paragraph, N(0,1/10) independently; Y=A*Y(1)+(1-A)*Y(0).
</pre>

</details>


## Parameter scenarios, estimands and truth

<table>
<thead><tr><th>Scenario</th><th>Estimand</th><th>Definition</th><th>Reported value</th></tr></thead>
<tbody>
<tr>
<td>original</td>
<td rowspan="1">ATE</td>
<td rowspan="1">

$`\mathbb{E}[Y^{(1)}-Y^{(0)}]`$

</td>
<td>1.0</td>
</tr>
</tbody>
</table>

**Definition notes**

- All scenarios: Population ATE; expectation is over the DGP's full population.

<details>
<summary>Submitted estimand definitions</summary>

Submitted English definitions appear below; other original-language definitions remain in the linked JSON. Concise formulas above are display interpretations and still require scientific review.

**Scenario(s):** original

E[Y(1)-Y(0)] in the full declared covariate population; treatment 1 versus 0; population, not sample-conditional, target.

[Open raw scientific record (JSON)](./ate-huang-chan-2017-05-19-setting-2-v1.json).

</details>


**Original submitted target notation:** ATE


## Identifiability assumptions

- Consistency and no interference across independent individuals.
- Conditional exchangeability given observed baseline X under the declared synthetic assignment.
- Pointwise positivity; no uniform overlap bound claimed for unbounded Gaussian logistic settings.

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Adaptations from the source (submitted, unverified):**

- Source treatment indicator is named A in the observed output; no scientific change.
- Independently implemented Python/NumPy sampler; source estimator fitting and large simulation replications are outside this collection task.
- Setting 2 epsilon definitions are read as inherited from Setting 1 in the same paragraph; this explicitly documented scope reading needs human confirmation.

**Warnings:**

- Nothing automatically flagged; this does NOT equal scientific acceptance.
