# Extreme quantile with a tail-dependent Cauchy auxiliary variable

> **Unverified extraction — scientific review required.**

**Primary area:** Semi-Supervised Inference

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Ahmed, H., Einmahl, J. H. J. and Zhou, C. (2025). Extreme Value Statistics in Semi-Supervised Models. JASA 120(549), 291–304.

**DOI:** 10.1080/01621459.2024.2333582 · **Source locator:** Section 2.1 defines independent samples; Section 4, first-quadrant bivariate Cauchy construction and equation (16); extreme-quantile paragraph preceding Table 3 (s=0,n=500,m=1000,p=0.002).

## DGP / generation mechanism

**Sampling design:** Unit: An independently sampled individual; Dependence: Independent rows, with within-row dependence specified by the equations.; N Semantics: Total rows. L=max(1,min(n-1,(n*source_n_labeled+(source_n_labeled+source_n_unlabeled)//2)//(source_n_labeled+source_n_unlabeled))).; Predictor Provenance: The generator exposes covariates as auxiliary information; fitted predictions are supplied by subsequent statistical methods using permitted labeled data and their documented training or cross-fitting splits. This contribution supplies the sampling law and observed data; later methods specify training and validation partitions. Prediction columns are absent.

**Generator source:** [generator.py](../generators/sspi-ahmed-2025-cauchy-tail-quantile-v1.py)

**Keywords (source-described):** Nonlinearity

**Observed variables**

X1, R, Y_obs

**Latent variables**

G1, G2

**Latent-variable identification:** candidates from equations need review

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

Source notation retained without guessing:

<pre>(V,U) has the bivariate standard Cauchy law restricted to V&gt;0,U&gt;0, with scale matrix I_2 (source s=0).</pre>

$$
\mathrm{Equivalent} \text{ independent }-\mathrm{normal} \mathrm{construction}: G_{0},G_{1},G_{2}\overset{\mathrm{iid}}{\sim} \mathcal{N}(0,1)
$$

$$
V=\lvert G_{1}\rvert/\lvert G_{0}\rvert
$$

$$
U=\lvert G_{2}\rvert/\lvert G_{0}\rvert.
$$

$$
F_{0}(v)=2\cdot \mathrm{atan}(v)/\pi\text{ for } v\geq 0
$$

$$
\mathrm{Outcome} Y=-\log(1-F_{0}(V))
$$

$$
\text{ observed } \mathrm{covariate} X_{1}=U
$$

$$
\mathrm{Source} \gamma=0 \in \mathrm{equation} (16).
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
(V,U) has the bivariate standard Cauchy law restricted to V&gt;0,U&gt;0, with scale matrix I_2 (source s=0).
Equivalent independent-normal construction: G0,G1,G2 iid N(0,1), V=abs(G1)/abs(G0), U=abs(G2)/abs(G0).
F_0(v)=2*atan(v)/pi for v&gt;=0. Outcome Y=-log(1-F_0(V)); observed covariate X1=U. Source gamma=0 in equation (16).
Two independent samples from the same population: source_n_labeled rows with observed Y and source_n_unlabeled rows with observed X only. R=1 in the first labeled block; Y_obs=Y there. R=0 in the remaining block; Y_obs=0 is a placeholder.
</pre>

</details>


## Parameter scenarios, estimands and truth

| Scenario | Estimand | Definition | Reported value | Evidence status |
|---|---|---|---|---|
| original | Marginal population quantile | Marginal quantile inf{y:Pr(Y&lt;=y)&gt;=0.998} in the common population; tail probability is fixed at 0.002. | 6.214608098422191 | reported_numeric |

**Original submitted target notation:** Q_Y(0.998)


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

- Select s=0,gamma=0,n=500,m=1000 and p=1/500 from the source quantile setting.
- Rename source target X as Y and source auxiliary Y as X1 to match the collection schema.
- Use the equivalent absolute-normal construction for the s=0 first-quadrant law and evaluate the survival probability with atan2 for tail stability.
- Represent independent labeled/unlabeled samples in a single table: all X columns, label indicator R and Y_obs. A zero on an R=0 row is a finite placeholder.
- The generate argument n counts total rows. Source total yields exact source allocation; other n use nearest-integer ratio allocation with both groups nonempty.
- Use local PCG64 random streams, with independent covariate and response-noise streams. Each row remains an independent population draw.

**Warnings:**

- Latent-variable candidates inferred from source equations; confirm their roles and completeness against the original paper or generator.
