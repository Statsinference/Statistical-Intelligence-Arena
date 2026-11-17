# Sparse high-dimensional linear mediation with correlated Gaussian errors

> **Unverified extraction — scientific review required.**

**Primary area:** Mediation — Direct and Indirect Effects

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Jones, J., Ertefaie, A. and Strawderman, R. L. (2025). Causal mediation analysis: selection with asymptotically valid inference. Journal of the Royal Statistical Society: Series B 87(3), 678–700. DOI: 10.1093/jrsssb/qkae109.

**DOI:** 10.1093/jrsssb/qkae109 · **Source locator:** Final article §5, Simulation B; compared with author code mediation-new-sims/R/sim_conf.R, function do_sim_paths, lines 84–117, commit 7617776b1a6415a185e18d336a5709c4d38f0555. Paper prose is followed where the two differ.

## DGP / generation mechanism

**Sampling design:** Unit: individual; Dependence: IID rows; within-row 100-dimensional correlated mediator disturbances

**Generator source:** [generator.py](../generators/mediation-jones-et-al-2025-correlated-sparse-v1.py)

**Keywords (source-described):** High-dimensionality

**Observed variables**

A, M001, M002, M003, M004, M005, M006, M007, M008, M009, M010, M011, M012, M013, M014, M015, M016, M017, M018, M019, M020, M021, M022, M023, M024, M025, M026, M027, M028, M029, M030, M031, M032, M033, M034, M035, M036, M037, M038, M039, M040, M041, M042, M043, M044, M045, M046, M047, M048, M049, M050, M051, M052, M053, M054, M055, M056, M057, M058, M059, M060, M061, M062, M063, M064, M065, M066, M067, M068, M069, M070, M071, M072, M073, M074, M075, M076, M077, M078, M079, M080, M081, M082, M083, M084, M085, M086, M087, M088, M089, M090, M091, M092, M093, M094, M095, M096, M097, M098, M099, M100, Y

**Latent variables**

E

**Latent-variable identification:** candidates from equations need review

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

**Treatment**

$$
A\sim \mathrm{Bernoulli}(0.5)
$$

**Errors**

$$
E\sim \mathcal{N}_{100}(0,\Sigma)
$$

$$
\Sigma_{ii}=1
$$

$$
\Sigma_{12}=0.5
$$

$$
\Sigma_{ij}=0.5 \text{ for } i,j\geq 3,i\neq j
$$

$$
\Sigma_{ij}=0.25 \text{ for } i \in \{1,2\},j \in \{3,\ldots ,100\}
$$

**Mediator**

$$
M_{j}=\alpha_{j} A+E_{j}, \alpha_{j}=1 \text{ for } j=1,2,3 \text{ and } 0 \text{ otherwise }
$$

**Outcome**

$$
Y=2A+M_{1}+M_{2}+M_{4}+M_{5}+M_{6}+\varepsilon_{Y}, \varepsilon_{Y}\sim \mathcal{N}(0,1)
$$

independent of (A,E)

**Target**

$$
\mathrm{NIE}_{1}=\sum_{j} \alpha_{j} \beta_{j}=2
$$

<details>
<summary>Original source equations (verbatim)</summary>

<pre>
A~Bernoulli(0.5)
E~N_100(0,Sigma), Sigma_ii=1; Sigma_12=0.5; Sigma_ij=0.5 for i,j&gt;=3,i!=j; Sigma_ij=0.25 for i in {1,2},j in {3,...,100}
M_j=alpha_j A+E_j, alpha_j=1 for j=1,2,3 and 0 otherwise
Y=2A+M1+M2+M4+M5+M6+epsilon_Y, epsilon_Y~N(0,1) independent of (A,E)
NIE_1=sum_j alpha_j beta_j=2
</pre>

</details>


## Parameter scenarios, estimands and truth

| Scenario | Estimand | Definition | Reported value | Evidence status |
|---|---|---|---|---|
| simulation_b_n200_p100_rho05 | NIE | E[Y(1,M(1))-Y(1,M(0))] for the full 100-vector mediator under the additive structural equations. | 2.0 | reported_numeric |

**Original submitted target notation:** NIE_1


## Identifiability assumptions

- IID individuals; randomized A
- Joint mediator vector intervention under the structural equations
- Finite Gaussian moments
- This full-vector causal effect is defined despite within-vector mediator-error correlations; subset effects require extra identification care

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Adaptations from the source (submitted, unverified):**

- Implement final article §5 Simulation B index convention: M1,M2 active mediators, M3 exposure-only, M4–M6 outcome-only; the archived author code uses a different ordering.
- Implement article prose that all nonmediators correlate 0.25 with M1,M2; author code connects only M3–M7 at 0.25. Gaussian noise, unit variance and randomized treatment are corroborated by the code.
- Report the joint-vector natural indirect effect over all 100 mediators, not the selected-subset effect under the paper’s deliberately correlated-error misspecification.
- Independent NumPy implementation with different random stream; source n=200 is recorded while generate(n,seed) varies n.

**Warnings:**

- Latent-variable candidates inferred from source equations; confirm their roles and completeness against the original paper or generator.
