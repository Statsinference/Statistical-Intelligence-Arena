# Endogenous Noncompliance and Local Treatment Effects

> **Unverified extraction — scientific review required.**

**Primary area:** IV — Instrumental Variables

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Athey, S., Tibshirani, J. and Wager, S. (2019). Generalized random forests. The Annals of Statistics 47(2), 1148–1178. DOI: 10.1214/18-AOS1709.

**DOI:** — · **Source locator:** arXiv v4 (2018-04-05), Appendix C.2, PDF pp.45–47, equation (49) and Table 2. Main paper §7 supplies local IV interpretation.

## DGP / generation mechanism

**Sampling design:** Unit: individual; Dependence: iid across individuals; within-unit dependencies explicitly specified by the structural equations

**Generator source:** [generator.py](../generators/iv-athey-tibshirani-wager-2019-compliance-v1.py)

**Keywords (source-described):** Interactions · Nonlinearity

**Observed variables**

X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, Z, A, Y

**Latent variables**

Q

**Latent-variable identification:** candidates from equations need review

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

$$
X \sim \mathcal{N}(0,I_{10})
$$

$$
\varepsilon\sim \mathcal{N}(0,1)
$$

$$
Z \sim \mathrm{Bernoulli}(1/3)
$$

mutually independent

$$
Q\mid \varepsilon\sim \mathrm{Bernoulli}(\mathrm{expit}(\omega\varepsilon))
$$

$$
A=ZQ
$$

$$
Y=\mu(X)+(A-1/2)\tau(X)+\varepsilon.
$$

**Additive**

$$
\tau(x)=\sum_{j=1}^{k} \max(0,x_{j})
$$

$$
\mu(x)=c[\max(0,x_{5})+\max(0,x_{6})].
$$

**Nonadditive**

$$
\tau(x)=\max(0,\sum_{j=1}^{k} x_{j})
$$

$$
\mu(x)=c \max(0,x_{5}+x_{6}).
$$

$$
k \in \{2,4\}
$$

$$
\omega\in \{0,1\}
$$

$$
c \in \{0,3\}
$$

$$
p=10.
$$

<details>
<summary>Original source equations (verbatim)</summary>

<pre>
X ~ N(0,I₁₀); ε ~ N(0,1); Z ~ Bernoulli(1/3), mutually independent.
Q|ε ~ Bernoulli(expit(ωε)); A=ZQ; Y=μ(X)+(A−1/2)τ(X)+ε.
Additive: τ(x)=Σⱼ₌₁ᵏ max(0,xⱼ); μ(x)=c[max(0,x₅)+max(0,x₆)].
Nonadditive: τ(x)=max(0,Σⱼ₌₁ᵏ xⱼ); μ(x)=c max(0,x₅+x₆).
k ∈ {2,4}; ω ∈ {0,1}; c ∈ {0,3}; p=10.
</pre>

</details>


## Parameter scenarios, estimands and truth

| Scenario | Estimand | Definition | True value | Evidence status |
|---|---|---|---|---|
| source_additive_k2_omega0_mu0 | tau_IV(x*) | Conditional Wald ratio at fixed x*: {E[Y\|Z=1,x*]-E[Y\|Z=0,x*]}/{E[A\|Z=1,x*]-E[A\|Z=0,x*]}. | 1.0 | reported_numeric |
| source_additive_k2_omega0_mu3 | tau_IV(x*) | Conditional Wald ratio at fixed x*: {E[Y\|Z=1,x*]-E[Y\|Z=0,x*]}/{E[A\|Z=1,x*]-E[A\|Z=0,x*]}. | 1.0 | reported_numeric |
| source_additive_k2_omega1_mu0 | tau_IV(x*) | Conditional Wald ratio at fixed x*: {E[Y\|Z=1,x*]-E[Y\|Z=0,x*]}/{E[A\|Z=1,x*]-E[A\|Z=0,x*]}. | 1.0 | reported_numeric |
| source_additive_k2_omega1_mu3 | tau_IV(x*) | Conditional Wald ratio at fixed x*: {E[Y\|Z=1,x*]-E[Y\|Z=0,x*]}/{E[A\|Z=1,x*]-E[A\|Z=0,x*]}. | 1.0 | reported_numeric |
| source_additive_k4_omega0_mu0 | tau_IV(x*) | Conditional Wald ratio at fixed x*: {E[Y\|Z=1,x*]-E[Y\|Z=0,x*]}/{E[A\|Z=1,x*]-E[A\|Z=0,x*]}. | 1.75 | reported_numeric |
| source_additive_k4_omega0_mu3 | tau_IV(x*) | Conditional Wald ratio at fixed x*: {E[Y\|Z=1,x*]-E[Y\|Z=0,x*]}/{E[A\|Z=1,x*]-E[A\|Z=0,x*]}. | 1.75 | reported_numeric |
| source_additive_k4_omega1_mu0 | tau_IV(x*) | Conditional Wald ratio at fixed x*: {E[Y\|Z=1,x*]-E[Y\|Z=0,x*]}/{E[A\|Z=1,x*]-E[A\|Z=0,x*]}. | 1.75 | reported_numeric |
| source_additive_k4_omega1_mu3 | tau_IV(x*) | Conditional Wald ratio at fixed x*: {E[Y\|Z=1,x*]-E[Y\|Z=0,x*]}/{E[A\|Z=1,x*]-E[A\|Z=0,x*]}. | 1.75 | reported_numeric |
| source_nonadditive_k2_omega0_mu0 | tau_IV(x*) | Conditional Wald ratio at fixed x*: {E[Y\|Z=1,x*]-E[Y\|Z=0,x*]}/{E[A\|Z=1,x*]-E[A\|Z=0,x*]}. | 0.5 | reported_numeric |
| source_nonadditive_k2_omega0_mu3 | tau_IV(x*) | Conditional Wald ratio at fixed x*: {E[Y\|Z=1,x*]-E[Y\|Z=0,x*]}/{E[A\|Z=1,x*]-E[A\|Z=0,x*]}. | 0.5 | reported_numeric |
| source_nonadditive_k2_omega1_mu0 | tau_IV(x*) | Conditional Wald ratio at fixed x*: {E[Y\|Z=1,x*]-E[Y\|Z=0,x*]}/{E[A\|Z=1,x*]-E[A\|Z=0,x*]}. | 0.5 | reported_numeric |
| source_nonadditive_k2_omega1_mu3 | tau_IV(x*) | Conditional Wald ratio at fixed x*: {E[Y\|Z=1,x*]-E[Y\|Z=0,x*]}/{E[A\|Z=1,x*]-E[A\|Z=0,x*]}. | 0.5 | reported_numeric |
| source_nonadditive_k4_omega0_mu0 | tau_IV(x*) | Conditional Wald ratio at fixed x*: {E[Y\|Z=1,x*]-E[Y\|Z=0,x*]}/{E[A\|Z=1,x*]-E[A\|Z=0,x*]}. | 1.0 | reported_numeric |
| source_nonadditive_k4_omega0_mu3 | tau_IV(x*) | Conditional Wald ratio at fixed x*: {E[Y\|Z=1,x*]-E[Y\|Z=0,x*]}/{E[A\|Z=1,x*]-E[A\|Z=0,x*]}. | 1.0 | reported_numeric |
| source_nonadditive_k4_omega1_mu0 | tau_IV(x*) | Conditional Wald ratio at fixed x*: {E[Y\|Z=1,x*]-E[Y\|Z=0,x*]}/{E[A\|Z=1,x*]-E[A\|Z=0,x*]}. | 1.0 | reported_numeric |
| source_nonadditive_k4_omega1_mu3 | tau_IV(x*) | Conditional Wald ratio at fixed x*: {E[Y\|Z=1,x*]-E[Y\|Z=0,x*]}/{E[A\|Z=1,x*]-E[A\|Z=0,x*]}. | 1.0 | reported_numeric |

## Identifiability assumptions

- Consistency and well-defined treatment interventions.
- Independent identically distributed units; no interference.
- Z is randomized Bernoulli(1/3), independent of X, epsilon and compliance randomization.
- Exclusion: Z affects Y only through A. A(z)=z*Q; monotonicity A(1)&gt;=A(0).
- Relevance: E[A\|Z=1,X]-E[A\|Z=0,X]=1/2.
- Treatment effect tau(X) is independent of latent epsilon/Q conditional on X; hence conditional LATE equals CATE here, not in every IV model.

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Warnings:**

- Latent-variable candidates inferred from source equations; confirm their roles and completeness against the original paper or generator.
