# Linear projection under correlated nonlinear regression with shared noise

> **Unverified extraction — scientific review required.**

**Primary area:** Semi-Supervised Inference

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Song, S., Lin, Y. and Zhou, Y. (2024). A General M-estimation Theory in Semi-Supervised Framework. JASA 119(546), 1065–1075.

**DOI:** 10.1080/01621459.2023.2169699 · **Source locator:** Official supplement Section 3.2, Setting S1, PDF p. 43; sample grid p. 44; Figure 11(b), p. 50. Released dataGeneration.R: GenerateData option S1 and g_S1.

## DGP / generation mechanism

**Sampling design:** Unit: An independently sampled individual; Dependence: Independent rows, with within-row dependence specified by the equations.; N Semantics: Total rows. L=max(1,min(n-1,(n*source_n_labeled+(source_n_labeled+source_n_unlabeled)//2)//(source_n_labeled+source_n_unlabeled))).; Predictor Provenance: The generator exposes covariates as auxiliary information; fitted predictions are supplied by subsequent statistical methods using permitted labeled data and their documented training or cross-fitting splits. This contribution supplies the sampling law and observed data; later methods specify training and validation partitions. Prediction columns are absent.

**Generator source:** [generator.py](../generators/sspi-song-2024-nonlinear-noise-projection-v1.py)

**Keywords (source-described):** Nonlinearity · Heteroskedasticity

**Observed variables**

X1–X4 (4 variables), R, Y_obs

<details>
<summary>All observed variable names</summary>

X1, X2, X3, X4, R, Y_obs

</details>

**Latent variables**

eta

**Latent-variable identification:** candidates from equations need review

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

```math
X\sim \mathcal{N}_{4}(0,\Sigma)
```

```math
\Sigma_{jk}=0.5^{\lvert j-k\rvert}
```

```math
\eta\sim \mathcal{N}(0,1) \text{ independently }.
```

```math
Y=(1/4)\cdot \sum_{j=1}^{4} [\exp(X_{j}+2\cdot \cos(X_{j})-0.3\cdot \eta)+0.1\cdot \exp(X_{j}+\sin(X_{j}))+2.5\cdot X_{j}^{3}]+\eta
```

The same eta appears in every term within a row.

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
X~N_4(0,Sigma), Sigma_jk=0.5^abs(j-k); eta~N(0,1) independently.
Y=(1/4)*sum_{j=1}^4 [exp(X_j+2*cos(X_j)-0.3*eta)+0.1*exp(X_j+sin(X_j))+2.5*X_j^3]+eta. The same eta appears in every term within a row.
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

$`\beta_1^{*},\quad (\alpha^{*},\beta^{*})=\operatorname*{argmin}_{\alpha,\beta}\mathbb{E}[(Y-\alpha-X^\top\beta)^2]`$

</td>
<td>2.5194516102296536</td>
</tr>
</tbody>
</table>

**Definition notes**

- All scenarios: First slope; four covariates.

<details>
<summary>Submitted estimand definitions</summary>

Submitted English definitions appear below; other original-language definitions remain in the linked JSON. Concise formulas above are display interpretations and still require scientific review.

**Scenario(s):** original

First slope in the population least-squares projection of Y on (1,X1,...,X4).

[Open raw scientific record (JSON)](./sspi-song-2024-nonlinear-noise-projection-v1.json).

</details>


**Original submitted target notation:** theta_L2[1]


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

- Select S1 with p=4,n=250,N=1000 from Figure 11(b).
- Return the first slope component through the scalar truth interface; retain the source intercept in the projection definition.
- Represent independent labeled/unlabeled samples in a single table: all X columns, label indicator R and Y_obs. A zero on an R=0 row is a finite placeholder.
- The generate argument n counts total rows. Source total yields exact source allocation; other n use nearest-integer ratio allocation with both groups nonempty.
- Use local PCG64 random streams, with independent covariate and response-noise streams. Each row remains an independent population draw.

**Warnings:**

- Latent-variable candidates inferred from source equations; confirm their roles and completeness against the original paper or generator.
