# IV: DeepIV raw-unit demand with endogenous continuous price

> **Unverified extraction — scientific review required.**

**Primary area:** IV — Instrumental Variables

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Hartford, J., Lewis, G., Leyton-Brown, K. and Taddy, M. (2017). Deep IV: A Flexible Approach for Counterfactual Prediction. ICML, PMLR 70:1414-1423.

**DOI:** — · **Source locator:** Published PDF p. 6, Section 4.1, simulation equations; experiments/data_generator.py lines 80-140 for psi, uniform customer type, rho=0.8 and code normalization.

## DGP / generation mechanism

**Sampling design:** Unit: individual; Dependence: iid individuals; exogenous random draws mutually independent within individual except explicitly shared latent errors

**Generator source:** [generator.py](../generators/iv-hartford-2017-demand-v1.py)

**Keywords (source-described):** Interactions · Nonlinearity

**Observed variables**

T, S, Z, P, Y

**Latent variables**

V, W

**Latent-variable identification:** candidates from equations need review

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

**1**

```math
T\sim \mathrm{Uniform}(0,10)
```

```math
S\sim \mathrm{DiscreteUniform}(\{1,\ldots ,7\})
```

```math
Z,V,W\overset{\mathrm{iid}}{\sim} \mathcal{N}(0,1)
```

mutually independent

**2**

```math
\psi(T)=2\cdot ((T-5)^{4}/600+\exp(-4\cdot (T-5)^{2})+T/10-2)
```

**3**

```math
P=25+(Z+3)\cdot \psi(T)+V
```

**4**

```math
e=\rho\cdot V+\sqrt{1-\rho^{2}}\cdot W
```

```math
\rho=0.8
```

**5**

```math
Y=100+(10+P)\cdot S\cdot \psi(T)-2\cdot P+e
```

<details>
<summary>Original source equations (verbatim)</summary>

<pre>
T~Uniform(0,10); S~DiscreteUniform({1,...,7}); Z,V,W iid Normal(0,1), mutually independent
psi(T)=2*((T-5)^4/600+exp(-4*(T-5)^2)+T/10-2)
P=25+(Z+3)*psi(T)+V
e=rho*V+sqrt(1-rho^2)*W; rho=0.8
Y=100+(10+P)*S*psi(T)-2*P+e
</pre>

</details>


## Parameter scenarios, estimands and truth

<table>
<thead><tr><th>Scenario</th><th>Estimand</th><th>Definition</th><th>Reported value</th></tr></thead>
<tbody>
<tr>
<td>paper_raw_rho08</td>
<td rowspan="1">Population structural mean price contrast</td>
<td rowspan="1">

$`\mathbb{E}[Y(21)-Y(20)]`$

</td>
<td>-11.624351792971128</td>
</tr>
</tbody>
</table>

**Definition notes**

- All scenarios: Intervention on price P, averaged over T and S.

<details>
<summary>Submitted estimand definitions</summary>

Submitted English definitions appear below; other original-language definitions remain in the linked JSON. Concise formulas above are display interpretations and still require scientific review.

**Scenario(s):** paper_raw_rho08

Population structural mean contrast of a one-unit price intervention, averaging independent T~Uniform(0,10) and S~DiscreteUniform(1,...,7); nuisance latent errors retain their marginal distribution.

[Open raw scientific record (JSON)](./iv-hartford-2017-demand-v1.json).

</details>


**Original submitted target notation:** theta_IV = E[Y(do(P=21))-Y(do(P=20))]


## Identifiability assumptions

- Consistency and no interference; iid individuals.
- Instrument Z is independent of T,S,V,W; exclusion: Z enters Y only through price P.
- E[e\|T,S,Z]=0 because e=rho*V+sqrt(1-rho^2)*W with independent centered normals.
- Relevance holds for almost every T: d E[P\|T,Z]/dZ=psi(T), whose zeros have probability zero under continuous T.
- Identification uses the additive structural-error conditional-moment model, nonzero Gaussian location shifts almost everywhere, and an appropriate regularity/completeness class; arbitrary IV problems are not automatically identified.

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Adaptations from the source (submitted, unverified):**

- Use the main-paper raw-unit equations including the +100 intercept; do not use author-code price/outcome normalization. Author code omits +100 and scales the structural mean before adding error, so this is not an exact code reproduction.
- Use S uniform on {1,...,7}, independently of T, as specified in author code; store S as a numeric category instead of seven one-hot columns. rho=0.8 is the author-code default.
- Collect a scalar population structural contrast E[Y(do(P=21))-Y(do(P=20))] instead of fitting the complete response surface. This is a continuous-treatment IV contrast, not a binary ATE or a regression conditional on observed P.
- Use a local NumPy PCG64 stream and n=128, seed=1729 for interface checking; distributional reconstruction only, with no estimator fitting.

**Warnings:**

- Latent-variable candidates inferred from source equations; confirm their roles and completeness against the original paper or generator.
