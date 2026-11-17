# Binary instrumental variable model with a nonlinear complier effect curve

> **Unverified extraction — scientific review required.**

**Primary area:** IV — Instrumental Variables

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Wang L, Zhang Y, Richardson TS, Robins JM (2021). Estimation of local treatment effects under the binary instrumental variable model. Biometrika 108(4):881-894. DOI:10.1093/biomet/asab003.

**DOI:** — · **Source locator:** English description not yet supplied; consult the original scientific record (JSON).

## DGP / generation mechanism

**Sampling design:** Unit: individual; Dependence: iid individuals. One active scalar x~U(-1,1); Z depends on x, and D/Y are sampled jointly conditional on x,Z. Binary principal-stratum model without interference.

**Generator source:** [generator.py](../generators/iv-wang-2021-binary-late-v1.py)

**Keywords (source-described):** Nonlinearity

**Observed variables**

x, Z, D, Y

**Latent variables**

Not explicitly identified (review required)

**Latent-variable identification:** not explicitly specified

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

**Original source equations (verbatim):** [Open raw scientific record (JSON)](./iv-wang-2021-binary-late-v1.json).

**DGP equation 1**

```math
x\sim \mathrm{Uniform}(-1,1)
```

```math
\delta=\tanh(-x)
```

```math
r=\exp(-0.4+x).
```

**DGP equation 2**

```math
\phi_{j}=\mathrm{expit}(-0.4+0.8x), j=1,\ldots ,4
```

```math
Z\mid x\sim \mathrm{Bernoulli}[\mathrm{expit}(0.1-x)].
```

**DGP equation 3**

```math
c=\phi_{1},\quad a=(1-c)\phi_{2},\quad n=(1-c)(1-\phi_{2})
```

**DGP equation 4**

```math
q_{0}=2r(1-\delta) / [r(2-\delta)+\delta+\sqrt{\delta^{2}(r-1)^{2}+4r}], q_{1}=q_{0}+\delta.
```

**DGP equation 5**

```math
p_{0}=(n(1-\phi_{3})+c(1-q_{0}),\ n\phi_{3}+c q_{0},\ a(1-\phi_{4}),\ a\phi_{4})
```

**DGP equation 6**

```math
p_{1}=(n(1-\phi_{3}),\ n\phi_{3},\ a(1-\phi_{4})+c(1-q_{1}),\ a\phi_{4}+c q_{1})
```

**DGP equation 7**

```math
(D,Y)\mid x,Z=z \sim \mathrm{Categorical}(p_{z})
```

```math
\mathrm{cells}=(00,01,10,11).
```


## Parameter scenarios, estimands and truth

| Scenario | Estimand | Definition | Reported value |
|---|---|---|---|
| source_additive | Conditional LATE curve transformed-slope parameter | Slope alpha1 in atanh(delta_L(x))=alpha0+alpha1*x, where delta_L(x)=E[Y(1)-Y(0)\|D(1)&gt;D(0),x]. Potential outcomes contrast D=1 versus D=0 among conditional compliers. Equivalently [atanh(delta_L(0.5))-atanh(delta_L(-0.5))]/1.0 under the declared curve model. This parameter is not a risk difference itself and is not the population ATE. | -1.0 |

**Original submitted target notation:** alpha1


## Identifiability assumptions

- Consistency, well-defined interventions, independent individuals and no interference.
- A1 exclusion: Y(z,d)=Y(d).
- A2 conditional IV independence: Z independent of potential outcomes and potential treatments given x.
- A3 conditional IV relevance: nonzero complier probability.
- A4 IV positivity on the declared bounded covariate support.
- A5 monotonicity: D(1)&gt;=D(0); no defiers.
- Correct tanh curve model for the transformed-curve slope target; no need to identify never-takers treated or always-takers untreated outcomes.

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Adaptations from the source (submitted, unverified):**

- Keep the additive Section 5 observed-data probability law and all its numeric parameters from the explicitly read arXiv v2. Only this single DGP scenario is declared; nuisance-model fitting variants are not separate DGPs.
- Scalar collection interface reports the original curve parameter alpha1, the slope of atanh(LATE(x)), rather than the full two-component alpha vector or the entire curve. No new causal target population or intervention is introduced.
- Return scalar x without the deterministic intercept column. Reconstruct the same observed joint law using Supplement S1 and a new local Python RNG categorical inverse CDF; author RNG and Monte Carlo outputs are not reproduced.
- Run the required n=128 CPU check rather than the original estimator simulation. Full journal-Version-of-Record versus v2 comparison remains pending; the source version is explicit.

**Warnings:**

- No explicit latent-variable metadata or reliably identifiable latent declarations; absence from this list does not prove that no latent variables exist.
