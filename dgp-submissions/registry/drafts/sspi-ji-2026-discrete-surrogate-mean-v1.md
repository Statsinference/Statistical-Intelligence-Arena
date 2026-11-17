# Population mean with a miscalibrated three-level surrogate

> **Unverified extraction — scientific review required.**

**Primary area:** Semi-Supervised Inference

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Ji, W., Lei, L. and Zrnic, T. (2026). Predictions as Surrogates: Revisiting Surrogate Outcomes in the Age of AI. Biometrika, asag053, advance online accepted manuscript, published 10 September 2026.

**DOI:** 10.1093/biomet/asag053 · **Source locator:** Section 4.3.1, PDF p. 16 (mixture law and observed prediction); Appendix E.1.3 and Figure 6, PDF p. 42 (mu1=-2,mu2=0,sigma^2=1,n=1000,N=9000; choose plotted mu3=4).

## DGP / generation mechanism

**Sampling design:** Unit: An independently sampled individual; Dependence: Independent rows, with within-row dependence specified by the equations.; N Semantics: Total rows. L=max(1,min(n-1,(n*source_n_labeled+(source_n_labeled+source_n_unlabeled)//2)//(source_n_labeled+source_n_unlabeled))).; Predictor Provenance: The source provides a fixed stylized prediction Y_hat=Z on every row; X1 stores this observed auxiliary prediction. It requires no model fitting or training split in the DGP. Recalibration methods fit their map using labeled data and must specify their own splitting rule.

**Generator source:** [generator.py](../generators/sspi-ji-2026-discrete-surrogate-mean-v1.py)

**Keywords (source-described):** Nonlinearity

**Observed variables**

X1, R, Y_obs

**Latent variables**

Z

**Latent-variable identification:** candidates from equations need review

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

```math
Z\sim \mathrm{Uniform}(\{1,2,3\})
```

```math
\varepsilon\sim \mathcal{N}(0,1) \text{ independently }
```

```math
Y=\mu_{Z}+\varepsilon, \text{ with } (\mu_{1},\mu_{2},\mu_{3})=(-2,0,4).
```

```math
\mathrm{The} \text{ source } \mathrm{assumes} \text{ an } \text{ observed } \text{ fixed } \mathrm{surrogate} \mathrm{prediction} Y_{\mathrm{hat}}=Z
```

Export it as X1 with role auxiliary_prediction, on both labeled and unlabeled rows.

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
Z~Uniform({1,2,3}); epsilon~N(0,1) independently; Y=mu_Z+epsilon, with (mu1,mu2,mu3)=(-2,0,4).
The source assumes an observed fixed surrogate prediction Y_hat=Z. Export it as X1 with role auxiliary_prediction, on both labeled and unlabeled rows.
Two independent samples from the same population: source_n_labeled rows with observed Y and source_n_unlabeled rows with observed X only. R=1 in the first labeled block; Y_obs=Y there. R=0 in the remaining block; Y_obs=0 is a placeholder.
</pre>

</details>


## Parameter scenarios, estimands and truth

<table>
<thead><tr><th>Scenario</th><th>Estimand</th><th>Definition</th><th>Reported value</th></tr></thead>
<tbody>
<tr>
<td>original</td>
<td rowspan="1">Population outcome mean</td>
<td rowspan="1">

$`\mathbb{E}[Y]`$

</td>
<td>0.6666666666666666</td>
</tr>
</tbody>
</table>

<details>
<summary>Submitted estimand definitions</summary>

Submitted English definitions appear below; other original-language definitions remain in the linked JSON. Concise formulas above are display interpretations and still require scientific review.

**Scenario(s):** original

Population mean of Y, aided by the observed discrete prediction.

[Open raw scientific record (JSON)](./sspi-ji-2026-discrete-surrogate-mean-v1.json).

</details>


**Original submitted target notation:** E[Y]


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

- Select mu3=4 from Figure 6; keep source n=1000,N=9000.
- Name the observed surrogate X1 to match the numeric table interface; its schema role is auxiliary_prediction. The surrogate is part of the specified sampling law and is available before target labels.
- Represent independent labeled/unlabeled samples in a single table: all X columns, label indicator R and Y_obs. A zero on an R=0 row is a finite placeholder.
- The generate argument n counts total rows. Source total yields exact source allocation; other n use nearest-integer ratio allocation with both groups nonempty.
- Use local PCG64 random streams, with independent covariate and response-noise streams. Each row remains an independent population draw.

**Warnings:**

- Latent-variable candidates inferred from source equations; confirm their roles and completeness against the original paper or generator.
