# Finite-horizon Markov mediation with three contemporaneous mediators

> **Unverified extraction — scientific review required.**

**Primary area:** Mediation — Direct and Indirect Effects

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Luo, L., Shi, C., Wang, J., Wu, Z. and Li, L. (2025). Multivariate dynamic mediation analysis under a reinforcement learning framework. The Annals of Statistics 53(1). DOI: 10.1214/24-AOS2475.

**DOI:** 10.1214/24-aos2475 · **Source locator:** Author arXiv:2310.16203, equations (3),(4), Definition 1 Eq. (8), §4.1 Simulation setup PDF pp.15–16; §4.2 T=10 setting.

## DGP / generation mechanism

**Sampling design:** Unit: subject trajectory; Dependence: IID subjects; ten temporally dependent observations retained in 50 wide columns per subject

**Generator source:** [generator.py](../generators/mediation-luo-et-al-2025-dynamic-markov-v1.py)

**Keywords (source-described):** Not specified

**Observed variables**

A01, M01_1, M01_2, M01_3, R01, A02, M02_1, M02_2, M02_3, R02, A03, M03_1, M03_2, M03_3, R03, A04, M04_1, M04_2, M04_3, R04, A05, M05_1, M05_2, M05_3, R05, A06, M06_1, M06_2, M06_3, R06, A07, M07_1, M07_2, M07_3, R07, A08, M08_1, M08_2, M08_3, R08, A09, M09_1, M09_2, M09_3, R09, A10, M10_1, M10_2, M10_3, R10

**Latent variables**

Not explicitly identified (review required)

**Latent-variable identification:** not explicitly specified

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

**Treatment**

```math
A_{t}\overset{\mathrm{iid}}{\sim} \mathrm{Bernoulli}(.5), t=1,\ldots ,10
```

**Coefficients**

```math
\mathrm{Every} \mathrm{entry} \text{ of } \Theta_{1t}=(\alpha_{1t},\delta_{1t},\Gamma_{1t},\zeta_{1t}) \text{ and } \Theta_{2t}=(\alpha_{2t},\delta_{2t},\gamma_{2t},\zeta_{2t,k}\mathrm{appa}_{t}) \text{ is } \text{ drawn } \text{ independently } \mathrm{Uniform}(-0.5,0.5)
```

realized arrays stored in config.json

**Mediators**

```math
\mu_{t}=\alpha_{1t}+\delta_{1t} A_{t}+\Gamma_{1t} M_{t-1}+\zeta_{1t} R_{t-1}
```

```math
M_{t}=\mu_{t}+(I-W^{T})^{-1} \varepsilon_{\mathrm{wt}}
```

```math
\mathrm{Equivalently} M_{t}-\mu_{t}=W^{T}(M_{t}-\mu_{t})+\varepsilon_{\mathrm{wt}}
```

**Outcome**

```math
R_{t}=\alpha_{2t}+\delta_{2t} A_{t}+\gamma_{2t}^{T} M_{t-1}+\zeta_{2t} R_{t-1}+\kappa_{t}^{T} M_{t}+\varepsilon_{rt}
```

**W**

[[0,-0.80,0.61],[0,0,-0.82],[0,0,0]]

```math
M_{0}=0,R_{0}=0
```

epsilon_wt and epsilon_rt independent standard normal

**Target**

```math
\eta_{1}^{10}= [E \sum R_{t}|\mathrm{do} A=1 - E \sum R_{t}|\mathrm{do} A=0] - [E \sum R_{t}|\mathrm{do} A=1,M_{t1}=0 - E \sum R_{t}|\mathrm{do} A=0,M_{t1}=0]
```

<details>
<summary>Original source equations (verbatim)</summary>

<pre>
A_t iid~Bernoulli(.5), t=1,...,10
Every entry of Theta_1t=(alpha_1t,delta_1t,Gamma_1t,zeta_1t) and Theta_2t=(alpha_2t,delta_2t,gamma_2t,zeta_2t,kappa_t) is drawn independently Uniform(-0.5,0.5); realized arrays stored in config.json
mu_t=alpha_1t+delta_1t A_t+Gamma_1t M_(t-1)+zeta_1t R_(t-1); M_t=mu_t+(I-W^T)^-1 epsilon_wt. Equivalently M_t-mu_t=W^T(M_t-mu_t)+epsilon_wt
R_t=alpha_2t+delta_2t A_t+gamma_2t^T M_(t-1)+zeta_2t R_(t-1)+kappa_t^T M_t+epsilon_rt
[[0,-0.80,0.61],[0,0,-0.82],[0,0,0]]; M_0=0,R_0=0; epsilon_wt and epsilon_rt independent standard normal
eta_1^(10)= [E sum R_t|do A=1 - E sum R_t|do A=0] - [E sum R_t|do A=1,M_t1=0 - E sum R_t|do A=0,M_t1=0]
</pre>

</details>


## Parameter scenarios, estimands and truth

| Scenario | Estimand | Definition | Reported value |
|---|---|---|---|
| finite_T10_seeded_coefficients | Dynamic mediation effect | For ten time points, contrast E[sum_t R_t\|do(A_s=1)]-E[sum_t R_t\|do(A_s=0)] and subtract the same contrast with do(M_{s,1}=0) for all s. | -0.02804345470955405 |

**Original submitted target notation:** eta_1^(10)


## Identifiability assumptions

- IID subjects with within-subject Markov dependence
- Sequential randomized A_t~Bernoulli(.5)
- No unmeasured mediator-outcome confounding beyond independent standard normal structural errors
- Linear recursive structural equations and fixed acyclic W
- Knockout of mediator 1 at all times is well-defined

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Adaptations from the source (submitted, unverified):**

- Fix one reproducible draw of all time-specific coefficients from the source Uniform(-0.5,0.5) distribution using Python seed 20251031; the paper does not publish its realized coefficient arrays, so numeric truth differs from authors’ run.
- Use wide per-subject rows (A01,M01_1,...,R10), retaining time dependence within each row; do not flatten panel observations as IID.
- Compute the paper’s individual mediator-1 effect by exact linear expectation recursion rather than the authors’ 10-million-sample Monte Carlo approximation.
- Use n input, with source n=100 recorded in config.

**Warnings:**

- No explicit latent-variable metadata or reliably identifiable latent declarations; absence from this list does not prove that no latent variables exist.
