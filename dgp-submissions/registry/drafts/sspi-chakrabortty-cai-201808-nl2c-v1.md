# Two-Component Interaction Semi-Supervised Projection Intercept

> **Unverified extraction — scientific review required.**

**Primary area:** Semi-Supervised Inference

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Chakrabortty, A. and Cai, T. (2018). Efficient and adaptive linear regression in semi-supervised settings. The Annals of Statistics 46(4), 1541-1572. DOI: 10.1214/17-AOS1594.

**DOI:** 10.1214/17-aos1594 · **Source locator:** Section 6.1, model (iii), journal p. 1559 = PDF p. 19; n=500 and N=10000 on journal p. 1558 = PDF p. 18; regression target in Section 2.

## DGP / generation mechanism

**Sampling design:** Unit: individual; Dependence: Independent complete-data units; fixed labeled/unlabeled group indicators, not independent Bernoulli indicators. Coordinate dependence is specified in equations.; N Semantics: n is combined table row count; Labeled Reference: 500; Unlabeled Reference: 10000; Predictor Source: No external or oracle predictor supplied. Downstream nuisance regressors must be trained on labeled training folds only; cross-fitting and tuning belong to the later estimator benchmark. No prediction is substituted for Y_obs.

**Generator source:** [generator.py](../generators/sspi-chakrabortty-cai-201808-nl2c-v1.py)

**Keywords (source-described):** Interactions · Nonlinearity

**Observed variables**

X1–X10 (10 variables), R, Y_obs

<details>
<summary>All observed variable names</summary>

X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, R, Y_obs

</details>

**Latent variables**

epsilon

**Latent-variable identification:** explicit structured metadata

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

**Covariates**

```math
\mathrm{Coordinates} \text{ independent } \mathcal{N}(0,1) \mathrm{conditional} \text{ on } -5 \leq X_{j} \leq 5
```

implemented by rejection, not clipping

This makes the source restriction explicit.

**Coefficient vectors**

```math
p=10
```

```math
b_{1}=(1,1,1,1,1,0,0,0,0,0)
```

```math
b_{2}=(1,1,1,1,1,1,1,1,1,1)
```

```math
\delta=(0,0,0,0,0,1,1,1,1,1)
```

```math
\omega=(1,0,1,0,1,0,1,0,1,0).
```

**Response**

```math
Y = (X^{T} b)(1 + X^{T} \delta) + \varepsilon
```

```math
\varepsilon\sim \mathcal{N}(0,1)
```

**Sampling and observed data**

Independent units and independent outcome noise

```math
\mathrm{Two} \text{ iid } \mathrm{samples} \text{ from } \text{ the } \mathrm{same} \text{ population }
```

fixed group sizes, R indicates observed Y

```math
\mathrm{Export} X,R,Y_{\mathrm{obs}} \text{ where } Y_{\mathrm{obs}}=Y \text{ when } R=1 \text{ and } 0 \text{ otherwise }
```

```math
n_{\mathrm{total}}=\mathrm{nL}+\mathrm{nU}.
```

<details>
<summary>Original source equations (verbatim)</summary>

<pre>
Coordinates independent N(0,1) conditional on -5 &lt;= X_j &lt;= 5; implemented by rejection, not clipping. This makes the source restriction explicit.
p=10; b1=(1,1,1,1,1,0,0,0,0,0), b2=(1,1,1,1,1,1,1,1,1,1); delta=(0,0,0,0,0,1,1,1,1,1); omega=(1,0,1,0,1,0,1,0,1,0).
Y = (X^T b)(1 + X^T delta) + epsilon; epsilon ~ N(0,1)
Independent units and independent outcome noise. Two iid samples from the same population; fixed group sizes, R indicates observed Y. Export X,R,Y_obs where Y_obs=Y when R=1 and 0 otherwise; n_total=nL+nU.
</pre>

</details>


## Parameter scenarios, estimands and truth

<table>
<thead><tr><th>Scenario</th><th>Estimand</th><th>Definition</th><th>Reported value</th></tr></thead>
<tbody>
<tr>
<td>source_b1_conditional_truncation</td>
<td rowspan="2">Population least-squares projection intercept</td>
<td rowspan="2">

$`\alpha^{*}=\mathbb{E}[Y],\quad (\alpha^{*},\beta^{*})=\operatorname*{argmin}_{\alpha,\beta}\mathbb{E}[(Y-\alpha-X^\top\beta)^2]`$

</td>
<td>0.0</td>
</tr>
<tr>
<td>source_b2_conditional_truncation</td>
<td>4.999925663981647</td>
</tr>
</tbody>
</table>

**Definition notes**

- All scenarios: The submitted design has E[X]=0.

<details>
<summary>Submitted estimand definitions</summary>

Submitted English definitions appear below; other original-language definitions remain in the linked JSON. Concise formulas above are display interpretations and still require scientific review.

**Scenario(s):** source_b1_conditional_truncation, source_b2_conditional_truncation

Intercept alpha of argmin_(alpha,beta) E[(Y-alpha-X^T beta)^2]; since E[X]=0 and Cov(X) is positive definite, alpha=E[Y].

[Open raw scientific record (JSON)](./sspi-chakrabortty-cai-201808-nl2c-v1.json).

</details>


**Original submitted target notation:** alpha_projection = E[Y]


## Identifiability assumptions

- Independent individuals; labeled and unlabeled observations have the same covariate law and common complete-data population.
- Fixed-size labeling independent of X,Y (two-sample/MCAR design); no MAR selection or distribution shift.
- Independent noise as specified; finite second moments; R must mask all uses of Y_obs.

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Adaptations from the source (submitted, unverified):**

- Map the two-sample SS design to one numeric table. API n is total rows, not the paper labeled n; R=1 for labeled rows; Y_obs=0 for R=0 is a sentinel, never a label. Source reference sample sizes are stored separately.
- For arbitrary CPU test n, labeled_count=max(1,min(n-1,floor(n*nL_ref/(nL_ref+nU_ref)))); first labeled_count rows form the independent labeled sample. At n=nL_ref+nU_ref the source counts are exact.
- Independent NumPy PCG64 implementation; no author code copied; original estimator tuning, fitted predictions, repeated CI experiments and PFN training are outside this DGP collection.
- Fix p=10; retain both source coefficient vectors as scenarios, not separate mechanisms.
- The paper states restriction to [-5,5]^p without specifying clipping versus rejection. We explicitly define independent conditional truncated normals via rejection; this is a declared adaptation requiring reviewer confirmation, not exact author-code reproduction.
- Select the intercept component of the population least-squares projection with an intercept. Since E[X]=0, this scalar equals E[Y]; the full regression vector is outside the scalar truth interface.

**Warnings:**

- Nothing automatically flagged; this does NOT equal scientific acceptance.
