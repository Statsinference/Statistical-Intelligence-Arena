# Binary double negative control test-negative design

> **Unverified extraction — scientific review required.**

**Primary area:** Proximal Causal Inference

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Kendrick Qijun Li, Xu Shi, Wang Miao, Eric Tchetgen Tchetgen (2024). Double Negative Control Inference in Test-Negative Design Studies of Vaccine Effectiveness. Journal of the American Statistical Association, 119(547), 1859-1870. DOI: 10.1080/01621459.2023.2220935.

**DOI:** 10.1080/01621459.2023.2220935 · **Source locator:** Author supplementary PDF at Git commit ba9dc3c581390fcefce0ca4cdabf65688a91a455; PDF p.25, Section I, Table S.1, binary and continuous blocks. Binary block.

## DGP / generation mechanism

**Sampling design:** Unit: individual; Dependence: English description not yet supplied; consult the original scientific record (JSON).

**Generator source:** [generator.py](../generators/proximal-li-2023-07-10-binary-tnd-v1.py)

**Keywords (source-described):** Interactions · Nonlinearity

**Observed variables**

A, Z, W, Y, U, D, S

**Latent variables**

Not explicitly identified (review required)

**Latent-variable identification:** not explicitly specified

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

**Original source equations (verbatim):** [Open raw scientific record (JSON)](./proximal-li-2023-07-10-binary-tnd-v1.json).

English equation transcription pending; consult the linked original scientific record (JSON) for the complete source and context.

U

D

S

**Step 1**

```math
U \sim \mathrm{Bernoulli}(0.5)
```

**Step 2**

```math
Z \mid  U \sim \mathrm{Bernoulli}(0.2 + 0.4U)
```

**Step 3**

```math
A \mid  U \sim \mathrm{Bernoulli}(0.2 + 0.4U)
```

English equation transcription pending; consult the linked original scientific record (JSON) for the complete source and context.

```math
Y \mid  A,U \sim \mathrm{Bernoulli}(\exp(\eta_{0} + \beta A - 0.693U))
```

```math
\eta_{0}=\ln(0.01)
```

**Step 5**

```math
W \mid  U \sim \mathrm{Bernoulli}(0.02 - 0.01U)
```

**Step 6**

```math
D \mid  U \sim \mathrm{Bernoulli}(0.02 - 0.015U)
```

**Step 7**

```math
S \mid  Y,D,W,U \sim \mathrm{Bernoulli}(\max(Y,D,W) \times  (0.1 + 0.4U))
```

English equation transcription pending; consult the linked original scientific record (JSON) for the complete source and context.

```math
S=1
```

A,Z,W,Y

U,D,S

{0,1}

English equation transcription pending; consult the linked original scientific record (JSON) for the complete source and context.

```math
\eta_{0}=\log(0.01)
```

```math
\beta\in \{\log(0.2), \log(0.5), \log(0.7), 0\}
```


## Parameter scenarios, estimands and truth

| Scenario | Estimand | Definition | Reported value |
|---|---|---|---|
| table-eta001-rr020 | Causal log mean ratio | log(E[Y(1)]/E[Y(0)]) in the source population before S selection; not selected-sample log odds ratio. | -1.6094379124341003 |
| table-eta001-rr050 | Causal log mean ratio | log(E[Y(1)]/E[Y(0)]) in the source population before S selection; not selected-sample log odds ratio. | -0.6931471805599453 |
| table-eta001-rr070 | Causal log mean ratio | log(E[Y(1)]/E[Y(0)]) in the source population before S selection; not selected-sample log odds ratio. | -0.35667494393873245 |
| table-eta001-rr100 | Causal log mean ratio | log(E[Y(1)]/E[Y(0)]) in the source population before S selection; not selected-sample log odds ratio. | 0.0 |

**Original submitted target notation:** beta_log_RR


## Identifiability assumptions

- Consistency, no interference and IID source individuals
- Latent exchangeability given U and treatment positivity; negative-control exclusions for Z and W given U
- Binary proxy probability matrices have sufficient rank and a treatment confounding bridge exists
- Common log-risk coefficient beta; among cases, selection depends on U but not A after conditioning on U
- The unknown-bridge estimator based on selected controls uses a rare-disease approximation; this package does not assert exact unbiasedness for that estimator
- Conditional errors use independent random draws; only S=1 rows are observed

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Adaptations from the source (submitted, unverified):**

- English description pending; see [original scientific record](./proximal-li-2023-07-10-binary-tnd-v1.json).
- English description pending; see [original scientific record](./proximal-li-2023-07-10-binary-tnd-v1.json).
- English description pending; see [original scientific record](./proximal-li-2023-07-10-binary-tnd-v1.json).

**Warnings:**

- No explicit latent-variable metadata or reliably identifiable latent declarations; absence from this list does not prove that no latent variables exist.
