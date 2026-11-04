# Cosine single-index mean with Gaussian covariates

> **Unverified extraction — scientific review required.**

**Primary area:** Semi-Supervised Inference

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Zhang, Y. and Bradic, J. (2022). High-dimensional semi-supervised learning: in search of optimal inference of the mean. Biometrika 109(2), 387–403.

**DOI:** 10.1093/biomet/asab042 · **Source locator:** Section 5.1, Model 2, PDF p. 11 / journal p. 397; Model 1 defines Gaussian noise; Figure 2 supplies n and m/n. Section 1 defines the two samples.

## DGP / generation mechanism

**Sampling design:** Unit: An independently sampled individual; Dependence: Independent rows, with within-row dependence specified by the equations.; N Semantics: Total rows. L=max(1,min(n-1,(n*source_n_labeled+(source_n_labeled+source_n_unlabeled)//2)//(source_n_labeled+source_n_unlabeled))).; Predictor Provenance: The generator exposes covariates as auxiliary information; fitted predictions are supplied by subsequent statistical methods using permitted labeled data and their documented training or cross-fitting splits. This contribution supplies the sampling law and observed data; later methods specify training and validation partitions. Prediction columns are absent.

**Generator source:** [generator.py](../generators/sspi-zhang-bradic-2022-cosine-index-v1.py)

**Keywords (source-described):** Interactions · Nonlinearity

**Observed variables**

X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, X11, X12, X13, X14, X15, X16, X17, X18, X19, X20, X21, X22, X23, X24, X25, X26, X27, X28, X29, X30, X31, X32, X33, X34, X35, X36, X37, X38, X39, X40, X41, X42, X43, X44, X45, X46, X47, X48, X49, X50, R, Y_obs

**Latent variables**

Not explicitly identified (review required)

**Latent-variable identification:** not explicitly specified

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

$$
X_{j}\overset{\mathrm{iid}}{\sim} \mathcal{N}(0,1), j=1,\ldots ,50
$$

$$
\varepsilon\sim \mathcal{N}(0,0.25)
$$

independent of X

$$
Y=3\cdot \cos(X_{1}+X_{2}+X_{3})+\varepsilon
$$

$$
\mathrm{Source} p=51 \mathrm{includes} \text{ an } \mathrm{intercept}.
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
X_j iid N(0,1), j=1,...,50; epsilon~N(0,0.25), independent of X.
Y=3*cos(X_1+X_2+X_3)+epsilon. Source p=51 includes an intercept.
Two independent samples from the same population: source_n_labeled rows with observed Y and source_n_unlabeled rows with observed X only. R=1 in the first labeled block; Y_obs=Y there. R=0 in the remaining block; Y_obs=0 is a placeholder.
</pre>

</details>


## Parameter scenarios, estimands and truth

| Scenario | Estimand | Definition | True value | Evidence status |
|---|---|---|---|---|
| original | E[Y] | Population mean of Y in the common labeled/unlabeled population. | 0.6693904804452895 | reported_numeric |

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
