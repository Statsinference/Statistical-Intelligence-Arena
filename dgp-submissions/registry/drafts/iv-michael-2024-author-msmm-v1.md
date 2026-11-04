# DGP iv-michael-2024-author-msmm-v1 (English title required)

> **Unverified extraction — scientific review required.**

**Primary area:** IV — Instrumental Variables

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Michael H, Cui Y, Lorch SA, Tchetgen Tchetgen EJ (2024). Instrumental Variable Estimation of Marginal Structural Mean Models for Time-Varying Treatment. JASA 119(546):1240–1251. DOI:10.1080/01621459.2023.2183131.

**DOI:** — · **Source locator:** English description not yet supplied; consult the original scientific record (JSON).

## DGP / generation mechanism

**Sampling design:** Unit: English description not yet supplied; consult the original scientific record (JSON).; Dependence: iid subjects, each with a full T=3 trajectory. A_(t-1) feeds into L_t; U_t is shared between L and treatment/outcome. Source implementation makes U_t recoverable from observed history; no irreducible hidden-confounding claim.

**Generator source:** [generator.py](../generators/iv-michael-2024-author-msmm-v1.py)

**Keywords (source-described):** Interactions · Nonlinearity

**Observed variables**

L1, Z1, A1, L2, Z2, A2, L3, Z3, A3, Y

**Latent variables**

Not explicitly identified (review required)

**Latent-variable identification:** not explicitly specified

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

**Original source equations (verbatim):** [Open raw scientific record (JSON)](./iv-michael-2024-author-msmm-v1.json).

**DGP equation 1**

$$
T=3
$$

$$
U_{t}\overset{\mathrm{iid}}{\sim} \mathcal{N}(0,1)
$$

$$
m_{1}=1, m_{t}=A_{t-1} (t\geq 2).
$$

**DGP equation 2**

$$
L_{t}=m_{t}+U_{t}, \delta_{t}=\Phi(0.96+0.46L_{t}).
$$

**DGP equation 3**

$$
Z_{t}\mid L_{t} \sim \mathrm{Bernoulli}[\mathrm{expit}(0.53-0.10L_{t})].
$$

**DGP equation 4**

$$
p_{t}=\Phi(-0.16+0.11L_{t}+0.26U_{t})(1-\delta_{t})+Z_{t}\delta_{t}
$$

**DGP equation 5**

$$
A_{t}\mid L_{t},U_{t},Z_{t} \sim \mathrm{Bernoulli}(p_{t}).
$$

**DGP equation 6**

$$
Y=\sum_{t=1}^{3}U_{t}/\sqrt{3}+\sum_{t=1}^{3}(L_{t}-m_{t})/\sqrt{3}+\sum_{t=1}^{3}\beta_{t}A_{t}+\varepsilon
$$

**DGP equation 7**

$$
\beta_{1}=\beta_{2}=\beta_{3}=1
$$

$$
\varepsilon\sim \mathcal{N}(0,1).
$$


## Parameter scenarios, estimands and truth

| Scenario | Estimand | Definition | True value | Evidence status |
|---|---|---|---|---|
| author_T3 | beta_T | English description not yet supplied; consult the original scientific record (JSON). | 1.0 | reported_numeric |

## Identifiability assumptions

- English description not yet supplied; consult the original scientific record (JSON).

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Warnings:**

- No explicit latent-variable metadata or reliably identifiable latent declarations; absence from this list does not prove that no latent variables exist.
