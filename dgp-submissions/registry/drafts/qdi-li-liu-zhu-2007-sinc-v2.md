# Conditional quantile in the Li-Liu-Zhu sinc demonstration mechanism

> **Unverified extraction — scientific review required.**

**Primary area:** Quantile Inference

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Li, Y., Liu, Y. and Zhu, J. (2007). Quantile Regression in Reproducing Kernel Hilbert Spaces. Journal of the American Statistical Association 102(477), 255-268. DOI: 10.1198/016214506000000979.

**DOI:** 10.1198/016214506000000979 · **Source locator:** Section 1, illustrative solution-path example; PDF page 2 = journal page 256; unnumbered sinc model in left column, six training observations.

## DGP / generation mechanism

**Sampling design:** Unit: One fully observed independent row (X,Y); Dependence: IID rows; coordinate and noise independence as recorded in equations and source adaptations.

**Generator source:** [generator.py](../generators/qdi-li-liu-zhu-2007-sinc-v2.py)

**Keywords (source-described):** Nonlinearity

**Observed variables**

X1, Y

**Latent variables**

Not explicitly identified (review required)

**Latent-variable identification:** explicit structured metadata

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

**Original source equations (verbatim):** [Open raw scientific record (JSON)](./qdi-li-liu-zhu-2007-sinc-v2.json).

**E1**

```math
X_i\sim U(-2,2),\quad\varepsilon_i\sim\mathcal N(0,0.2^2),\quad X_i\perp\varepsilon_i
```

The displayed marginals are source-supported; the independence/product-sampling part is a declared implementation convention. See source_recheck.json.

**E2**

```math
Y_i=\frac{\sin(\pi X_i)}{\pi X_i}+\varepsilon_i,\quad \mathrm{sinc}(0)=1
```

**E3**

```math
Q_\tau(x)=\mathrm{sinc}(x)+0.2\Phi^{-1}(\tau)
```


## Parameter scenarios, estimands and truth

<table>
<thead><tr><th>Scenario</th><th>Estimand</th><th>Definition</th><th>Reported value</th></tr></thead>
<tbody>
<tr>
<td>source_law_fixed_query</td>
<td rowspan="1">Conditional quantile</td>
<td rowspan="1">

$`Q_{0.9}(Y\mid X=0.5)`$

</td>
<td>0.8929300854765015</td>
</tr>
</tbody>
</table>

<details>
<summary>Submitted estimand definitions</summary>

Submitted English definitions appear below; other original-language definitions remain in the linked JSON. Concise formulas above are display interpretations and still require scientific review.

**Scenario(s):** source_law_fixed_query

Conditional 0.9 quantile at X=0.5, using the sinc data law of the Section 1 demonstration.

[Open raw scientific record (JSON)](./qdi-li-liu-zhu-2007-sinc-v2.json).

</details>


**Original submitted target notation:** Q_{0.9}(0.5)


## Identifiability assumptions

- Independent, identically distributed fully observed rows from the stated synthetic population.
- All noise variables are independent of observed covariates; coordinate dependence is exactly as stated in equations and implementation conventions.
- Quantiles use the left generalized inverse inf{y:F(y)&gt;=tau}; the selected continuous law has positive density at the registered quantile.

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Adaptations from the source (submitted, unverified):**

- The source uses n=6 to illustrate a solution path. generate accepts arbitrary n for collection checks; source_n=6 is retained as metadata. This is not the Section 5 main experiment.
- A fixed conditional 0.9 quantile at x=0.5 is registered; independent covariate/noise draws and iid rows are explicit implementation conventions.
- Independent Python/NumPy implementation from mathematical formulas; no author code is redistributed. PCG64(seed) replaces unspecified/source software random-number generation. Sample size is the generate n argument; source_n only records the published sample sizes. No fitting, bootstrap, confidence-band coverage experiment or PFN training is included.
- Clarified that generation constants are specified jointly in the displayed equations and config.json; not every fixed source constant is exposed as a configurable parameter.
- Source recheck did not turn the disclosed independence completion into a source fact. Marginal laws and equations match the read source, while the implementation product law still needs a maintainer decision before claiming a fully source-verified joint DGP.

**Warnings:**

- Nothing automatically flagged; this does NOT equal scientific acceptance.
