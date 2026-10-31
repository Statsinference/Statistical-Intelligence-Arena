# Continuous-proxy double negative control test-negative design

> **Unverified extraction — scientific review required.**

**Primary area:** Proximal Causal Inference

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Kendrick Qijun Li, Xu Shi, Wang Miao, Eric Tchetgen Tchetgen (2024). Double Negative Control Inference in Test-Negative Design Studies of Vaccine Effectiveness. Journal of the American Statistical Association, 119(547), 1859-1870. DOI: 10.1080/01621459.2023.2220935.

**DOI:** 10.1080/01621459.2023.2220935 · **Source locator:** Author supplementary PDF at Git commit ba9dc3c581390fcefce0ca4cdabf65688a91a455; PDF p.25, Section I, Table S.1, binary and continuous blocks. Continuous block.

## DGP / generation mechanism

**Sampling design:** Unit: individual; Dependence: English description not yet supplied; consult the original scientific record (JSON).

**Generator source:** [generator.py](../generators/proximal-li-2023-07-10-continuous-tnd-v1.py)

**Keywords (source-described):** Interactions · Nonlinearity

**Observed variables**

X, A, Z, W, Y, U, D, S

**Latent variables**

Not explicitly identified (review required)

**Latent-variable identification:** not explicitly specified

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

**Original source equations (verbatim):** [Open raw scientific record (JSON)](./proximal-li-2023-07-10-continuous-tnd-v1.json).

English equation transcription pending

see the original record (JSON).

English equation transcription pending

see the original record (JSON).

$$
2. `A \mid  U,X \sim \mathrm{Bernoulli}(\sigma(-1 + U + 0.25X))`
$$

$$
3. `Z = 0.25A + 0.25X + 5U + \varepsilon Z`
$$

$$
4. `W = 0.25X + 2U + \varepsilon W`
$$

$$
5. `Y \mid  A,U,X \sim \mathrm{Bernoulli}(\exp(\eta_{0} + \beta A - 2U - 0.25X - 0.75UX))`，`\eta_{0}=ln(0.01)`
$$

$$
6. `D \mid  U,X \sim \mathrm{Bernoulli}(\exp(-4.605 + 0.25X - 0.2U))`
$$

$$
7. `S \mid  Y,D,U,X \sim \mathrm{Bernoulli}(\max(Y,D) \times  \sigma(-1.4 + 0.5X + 2U + UX))`
$$

English equation transcription pending

see the original record (JSON).

English equation transcription pending

see the original record (JSON).


## Parameter scenarios, estimands and truth

| Scenario | Estimand | Definition | True value | Evidence status |
|---|---|---|---|---|
| table-eta001-rr020 | beta_log_RR | log(E[Y(1)]/E[Y(0)]) in the source population before S selection; not selected-sample log odds ratio. | -1.6094379124341003 | reported_numeric |
| table-eta001-rr050 | beta_log_RR | log(E[Y(1)]/E[Y(0)]) in the source population before S selection; not selected-sample log odds ratio. | -0.6931471805599453 | reported_numeric |
| table-eta001-rr070 | beta_log_RR | log(E[Y(1)]/E[Y(0)]) in the source population before S selection; not selected-sample log odds ratio. | -0.35667494393873245 | reported_numeric |
| table-eta001-rr100 | beta_log_RR | log(E[Y(1)]/E[Y(0)]) in the source population before S selection; not selected-sample log odds ratio. | 0.0 | reported_numeric |

## Identifiability assumptions

- Consistency, no interference and IID source individuals
- Latent exchangeability given U,X and treatment positivity; negative-control exclusions and conditional proxy relevance/completeness
- The normal treatment bridge exists; common log-risk coefficient beta across U,X
- Among cases, S depends on U,X and not directly on A; case bridge weighting cancels the common selection factor in the risk ratio
- Estimating an unknown bridge from selected controls invokes the rare-disease approximation; no exact finite-sample estimator claim is made
- U and X, conditional proxy errors and Bernoulli draws use independent exogenous random numbers

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Warnings:**

- No explicit latent-variable metadata or reliably identifiable latent declarations; absence from this list does not prove that no latent variables exist.
