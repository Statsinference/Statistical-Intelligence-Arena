# Best linear slope under a quadratic Gaussian response

> **Unverified extraction — scientific review required.**

**Primary area:** Semi-Supervised Inference

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Azriel, D., Brown, L. D., Sklar, M., Berk, R., Buja, A. and Zhao, L. (2022). Semi-Supervised Linear Regression. JASA 117(540), 2238–2251.

**DOI:** 10.1080/01621459.2021.1915320 · **Source locator:** Section 5.1, equation (27), PDF p. 18; Figure 1, PDF p. 19 (alpha=1/2, beta=1, n=100, m=2n); Section 1.1 and Section 2 define sampling and projection.

## DGP / generation mechanism

**Sampling design:** Unit: An independently sampled individual; Dependence: Independent rows, with within-row dependence specified by the equations.; N Semantics: Total rows. L=max(1,min(n-1,(n*source_n_labeled+(source_n_labeled+source_n_unlabeled)//2)//(source_n_labeled+source_n_unlabeled))).; Predictor Provenance: The generator exposes covariates as auxiliary information; fitted predictions are supplied by subsequent statistical methods using permitted labeled data and their documented training or cross-fitting splits. This contribution supplies the sampling law and observed data; later methods specify training and validation partitions. Prediction columns are absent.

**Generator source:** [generator.py](../generators/sspi-azriel-2022-quadratic-projection-v1.py)

**Keywords (source-described):** Nonlinearity

**Observed variables**

X1, R, Y_obs

**Latent variables**

Not explicitly identified (review required)

**Latent-variable identification:** not explicitly specified

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

```math
X\sim \mathcal{N}(0,1) \text{ and } \varepsilon\sim \mathcal{N}(0,1) \text{ independently }.
```

```math
Y=0.5\cdot X^{2}+X+\varepsilon.
```

Source notation retained without guessing:

<pre>Two independent samples from the same population: source_n_labeled rows with observed Y and source_n_unlabeled rows with observed X only. R=1 in the first labeled block</pre>

```math
Y_{\mathrm{obs}}=Y \text{ there }. R=0 \in \text{ the } \mathrm{remaining} \mathrm{block}
```

```math
Y_{\mathrm{obs}}=0 \text{ is } \text{ a } \text{ placeholder }.
```

<details>
<summary>Original source equations (verbatim)</summary>

<pre>
X~N(0,1) and epsilon~N(0,1) independently.
Y=0.5*X^2+X+epsilon.
Two independent samples from the same population: source_n_labeled rows with observed Y and source_n_unlabeled rows with observed X only. R=1 in the first labeled block; Y_obs=Y there. R=0 in the remaining block; Y_obs=0 is a placeholder.
</pre>

</details>


## Parameter scenarios, estimands and truth

<table>
<thead><tr><th>Scenario</th><th>Estimand</th><th>Definition</th><th>Reported value</th></tr></thead>
<tbody>
<tr>
<td>original</td>
<td rowspan="1">Population least-squares projection slope</td>
<td rowspan="1">

$`\beta^{*},\quad (\alpha^{*},\beta^{*})=\operatorname*{argmin}_{\alpha,\beta}\mathbb{E}[(Y-\alpha-\beta X)^2]`$

</td>
<td>1.0</td>
</tr>
</tbody>
</table>

**Definition notes**

- All scenarios: Population least-squares projection slope.

<details>
<summary>Submitted estimand definitions</summary>

Submitted English definitions appear below; other original-language definitions remain in the linked JSON. Concise formulas above are display interpretations and still require scientific review.

**Scenario(s):** original

Slope in the population least-squares projection of Y on (1,X).

[Open raw scientific record (JSON)](./sspi-azriel-2022-quadratic-projection-v1.json).

</details>


**Original submitted target notation:** beta_L2


## Identifiability assumptions

- Independent sampling units; labeled and unlabeled samples are independent draws from the same joint/marginal population.
- Label availability is fixed by sampling design independently of generated values, corresponding to MCAR sampling.
- The stated distributions, independence conditions and selected population functional define the target. Its numerical verification applies to the declared scenario.

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Adaptations from the source (submitted, unverified):**

- Select alpha=1/2 and n=100 from the source Figure 1 grid, beta=1 and m=2n.
- Return the slope component of the population linear projection through the scalar truth interface.
- Represent independent labeled/unlabeled samples in a single table: all X columns, label indicator R and Y_obs. A zero on an R=0 row is a finite placeholder.
- The generate argument n counts total rows. Source total yields exact source allocation; other n use nearest-integer ratio allocation with both groups nonempty.
- Use local PCG64 random streams, with independent covariate and response-noise streams. Each row remains an independent population draw.

**Warnings:**

- No explicit latent-variable metadata or reliably identifiable latent declarations; absence from this list does not prove that no latent variables exist.
