# Marginal distribution inference with sparse Gaussian linear signal

> **Unverified extraction — scientific review required.**

**Primary area:** Semi-Supervised Inference

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Wen, M., Jia, Y., Ren, H., Wang, Z. and Zou, C. (2025). Semi-supervised distribution learning. Biometrika 112(1), asae056.

**DOI:** 10.1093/biomet/asae056 · **Source locator:** Section 3, unnumbered DGP equations, PDF p. 6; Table 1, Figure 1 and sample sizes, PDF p. 7. Section 2 defines labeled/unlabeled samples and marginal CDF.

## DGP / generation mechanism

**Sampling design:** Unit: An independently sampled individual; Dependence: Independent rows, with within-row dependence specified by the equations.; N Semantics: Total rows. L=max(1,min(n-1,(n*source_n_labeled+(source_n_labeled+source_n_unlabeled)//2)//(source_n_labeled+source_n_unlabeled))).; Predictor Provenance: The generator exposes covariates as auxiliary information; fitted predictions are supplied by subsequent statistical methods using permitted labeled data and their documented training or cross-fitting splits. This contribution supplies the sampling law and observed data; later methods specify training and validation partitions. Prediction columns are absent.

**Generator source:** [generator.py](../generators/sspi-wen-2025-gaussian-cdf-v1.py)

**Keywords (source-described):** Linearity

**Observed variables**

X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, X11, X12, X13, X14, X15, X16, X17, X18, X19, X20, X21, X22, X23, X24, X25, X26, X27, X28, X29, X30, X31, X32, X33, X34, X35, X36, X37, X38, X39, X40, X41, X42, X43, X44, X45, X46, X47, X48, X49, X50, X51, X52, X53, X54, X55, X56, X57, X58, X59, X60, X61, X62, X63, X64, X65, X66, X67, X68, X69, X70, X71, X72, X73, X74, X75, X76, X77, X78, X79, X80, X81, X82, X83, X84, X85, X86, X87, X88, X89, X90, X91, X92, X93, X94, X95, X96, X97, X98, X99, X100, R, Y_obs

**Latent variables**

Not explicitly identified (review required)

**Latent-variable identification:** not explicitly specified

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

$$
X\sim \mathcal{N}_{100}(0,I)
$$

$$
\varepsilon\sim \mathcal{N}(0,1) \text{ independently }
$$

$$
s=\lceil 0.1\cdot p\rceil=10.
$$

$$
Y=\sum_{j=1}^{10} X_{j}/\sqrt{10}+0.5\cdot \varepsilon.
$$

Source notation retained without guessing:

<pre>Two independent samples from the same population: source_n_labeled rows with observed Y and source_n_unlabeled rows with observed X only. R=1 in the first labeled block</pre>

$$
Y_{\mathrm{obs}}=Y \text{ there }. R=0 \in \text{ the } \mathrm{remaining} \mathrm{block}
$$

$$
Y_{\mathrm{obs}}=0 \text{ is } \text{ a } \text{ placeholder }.
$$

<details>
<summary>Original source equations (verbatim)</summary>

<pre>
X~N_100(0,I); epsilon~N(0,1) independently; s=ceil(0.1*p)=10.
Y=sum_{j=1}^{10} X_j/sqrt(10)+0.5*epsilon.
Two independent samples from the same population: source_n_labeled rows with observed Y and source_n_unlabeled rows with observed X only. R=1 in the first labeled block; Y_obs=Y there. R=0 in the remaining block; Y_obs=0 is a placeholder.
</pre>

</details>


## Parameter scenarios, estimands and truth

| Scenario | Estimand | Definition | True value | Evidence status |
|---|---|---|---|---|
| original | F_Y(1) | Marginal population CDF Pr(Y&lt;=1), using the semi-supervised observation design. | 0.8144533152386513 | reported_numeric |

## Identifiability assumptions

- Independent sampling units; labeled and unlabeled samples are independent draws from the same joint/marginal population.
- Label availability is fixed by sampling design independently of generated values, corresponding to MCAR sampling.
- The stated distributions, independence conditions and selected population functional define the target. Its numerical verification applies to the declared scenario.

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Warnings:**

- No explicit latent-variable metadata or reliably identifiable latent declarations; absence from this list does not prove that no latent variables exist.
