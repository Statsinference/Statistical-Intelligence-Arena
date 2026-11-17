# Binary potential-outcome finite-population designs under complete randomization

> **Unverified extraction — scientific review required.**

**Primary area:** ATE — Average Treatment Effect

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Ding, P. and Dasgupta, T. (2016). A Potential Tale of Two-by-Two Tables From Completely Randomized Experiments. Journal of the American Statistical Association, 111(513), 157–168. DOI: 10.1080/01621459.2014.995796.

**DOI:** 10.1080/01621459.2014.995796 · **Source locator:** Read version: arXiv:1501.02389v1 (2015-01-10), 39-page PDF. Section 2.1–2.2, PDF pp. 4–5: finite-population ATE and complete randomization; Section 6, PDF pp. 18–19, Table 5: Cases 1–12 potential-outcome cell counts and simulation setup. ATE definition is an unnumbered displayed/inline expression in Section 2.1; Eq. (1) is a variance expression, not the ATE definition. Publisher final pagination is JASA 111(513), 157–168; publisher full text was inaccessible, so final-version PDF page/equation mapping is unverified. Appendix E Cases 13–19 not included.

## DGP / generation mechanism

**Sampling design:** Unit: Individual experimental unit in a fixed finite population of N=200 units.; Dependence: Potential outcomes are fixed attributes of units, not iid generated errors. Under complete randomization, treatment indicators are dependent across units because the treated count is fixed (negative assignment dependence). No interference is assumed; outcomes have no cross-unit dependence beyond the shared randomization design. The implementation additionally samples n units without replacement before randomizing the sampled subset.

**Generator source:** [generator.py](../generators/ate-ding-dasgupta-2016-binary-rct-v1.py)

**Keywords (source-described):** Not specified

**Observed variables**

A, Y

**Latent variables**

Not explicitly identified (review required)

**Latent-variable identification:** not explicitly specified

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

**Fixed finite-population potential-outcome cells**

```math
\mathrm{N}_{11}=\#\{i:Y_{i}(1)=1,Y_{i}(0)=1\}
```

```math
\mathrm{N}_{10}=\#\{i:Y_{i}(1)=1,Y_{i}(0)=0\}
```

```math
\mathrm{N}_{01}=\#\{i:Y_{i}(1)=0,Y_{i}(0)=1\}
```

```math
\mathrm{N}_{00}=\#\{i:Y_{i}(1)=0,Y_{i}(0)=0\}
```

```math
\mathrm{N}=\mathrm{N}_{11}+\mathrm{N}_{10}+\mathrm{N}_{01}+\mathrm{N}_{00}=200.
```

**Complete randomization (user-approved allocation adaptation)**

```math
\mathrm{N}_{1}=\mathrm{N}_{0}=100
```

```math
P(A=\text{ a })=1/\mathrm{binom}(\mathrm{N},\mathrm{N}_{1}) \text{ for } \mathrm{every} \mathrm{assignment} \text{ vector } \text{ a } \text{ with } \sum_{i} \text{ a }_{i}=\mathrm{N}_{1}.
```

**Observed outcome**

```math
Y_{i}=A_{i} Y_{i}(1)+(1-A_{i})Y_{i}(0)
```

Only (A_i,Y_i) are returned.

**Finite-population ATE**

```math
\tau=\mathrm{N}^{-1} \sum_{i}[Y_{i}(1)-Y_{i}(0)]=(\mathrm{N}_{10}-\mathrm{N}_{01})/\mathrm{N}.
```

<details>
<summary>Original source equations (verbatim)</summary>

<pre>
N11=#{i:Y_i(1)=1,Y_i(0)=1}; N10=#{i:Y_i(1)=1,Y_i(0)=0}; N01=#{i:Y_i(1)=0,Y_i(0)=1}; N00=#{i:Y_i(1)=0,Y_i(0)=0}; N=N11+N10+N01+N00=200.
N1=N0=100; P(A=a)=1/binom(N,N1) for every assignment vector a with sum_i a_i=N1.
Y_i=A_i Y_i(1)+(1-A_i)Y_i(0). Only (A_i,Y_i) are returned.
tau=N^{-1} sum_i[Y_i(1)-Y_i(0)]=(N10-N01)/N.
</pre>

</details>


## Parameter scenarios, estimands and truth

| Scenario | Estimand | Definition | Reported value |
|---|---|---|---|
| case01_independent_null | ATE | Finite-population average treatment effect / causal risk difference for intervention A=1 versus A=0 over the N=200 experimental units. Y_i(1) and Y_i(0) are binary fixed potential outcomes; observed Y_i=A_i Y_i(1)+(1-A_i)Y_i(0). | 0.0 |
| case02_independent_positive | ATE | Finite-population average treatment effect / causal risk difference for intervention A=1 versus A=0 over the N=200 experimental units. Y_i(1) and Y_i(0) are binary fixed potential outcomes; observed Y_i=A_i Y_i(1)+(1-A_i)Y_i(0). | 0.2 |
| case03_independent_positive | ATE | Finite-population average treatment effect / causal risk difference for intervention A=1 versus A=0 over the N=200 experimental units. Y_i(1) and Y_i(0) are binary fixed potential outcomes; observed Y_i=A_i Y_i(1)+(1-A_i)Y_i(0). | 0.35 |
| case04_independent_negative | ATE | Finite-population average treatment effect / causal risk difference for intervention A=1 versus A=0 over the N=200 experimental units. Y_i(1) and Y_i(0) are binary fixed potential outcomes; observed Y_i=A_i Y_i(1)+(1-A_i)Y_i(0). | -0.3 |
| case05_independent_negative | ATE | Finite-population average treatment effect / causal risk difference for intervention A=1 versus A=0 over the N=200 experimental units. Y_i(1) and Y_i(0) are binary fixed potential outcomes; observed Y_i=A_i Y_i(1)+(1-A_i)Y_i(0). | -0.35 |
| case06_positive_association_null | ATE | Finite-population average treatment effect / causal risk difference for intervention A=1 versus A=0 over the N=200 experimental units. Y_i(1) and Y_i(0) are binary fixed potential outcomes; observed Y_i=A_i Y_i(1)+(1-A_i)Y_i(0). | 0.0 |
| case07_positive_association | ATE | Finite-population average treatment effect / causal risk difference for intervention A=1 versus A=0 over the N=200 experimental units. Y_i(1) and Y_i(0) are binary fixed potential outcomes; observed Y_i=A_i Y_i(1)+(1-A_i)Y_i(0). | 0.1 |
| case08_positive_association | ATE | Finite-population average treatment effect / causal risk difference for intervention A=1 versus A=0 over the N=200 experimental units. Y_i(1) and Y_i(0) are binary fixed potential outcomes; observed Y_i=A_i Y_i(1)+(1-A_i)Y_i(0). | 0.2 |
| case09_positive_association | ATE | Finite-population average treatment effect / causal risk difference for intervention A=1 versus A=0 over the N=200 experimental units. Y_i(1) and Y_i(0) are binary fixed potential outcomes; observed Y_i=A_i Y_i(1)+(1-A_i)Y_i(0). | 0.5 |
| case10_positive_association_negative | ATE | Finite-population average treatment effect / causal risk difference for intervention A=1 versus A=0 over the N=200 experimental units. Y_i(1) and Y_i(0) are binary fixed potential outcomes; observed Y_i=A_i Y_i(1)+(1-A_i)Y_i(0). | -0.1 |
| case11_positive_association_negative | ATE | Finite-population average treatment effect / causal risk difference for intervention A=1 versus A=0 over the N=200 experimental units. Y_i(1) and Y_i(0) are binary fixed potential outcomes; observed Y_i=A_i Y_i(1)+(1-A_i)Y_i(0). | -0.2 |
| case12_positive_association_negative | ATE | Finite-population average treatment effect / causal risk difference for intervention A=1 versus A=0 over the N=200 experimental units. Y_i(1) and Y_i(0) are binary fixed potential outcomes; observed Y_i=A_i Y_i(1)+(1-A_i)Y_i(0). | -0.5 |

**Original submitted target notation:** tau = N^{-1} sum_i [Y_i(1)-Y_i(0)] = (N10-N01)/N


## Identifiability assumptions

- Well-defined binary treatment and consistency: observed outcome equals the potential outcome under assigned treatment.
- SUTVA/no interference: one unit’s potential outcomes do not depend on other units’ assignments.
- Complete randomization: exactly N1 treated and N0 controls, with all allocations of that size equally likely.
- The finite population and its potential outcomes are fixed; randomness is from treatment assignment (and, for this implementation interface only, the additional SRS sample stage).
- No observational unconfoundedness assumption is needed for design-based identification under randomized assignment.

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Adaptations from the source (submitted, unverified):**

- User-approved 1:1 allocation: set N1=N0=100 for each source Table 5 finite population of N=200; the inspected source text does not establish this allocation for Table 5, so it is an explicit user-requested assumption, not a source parameter.
- For the required generate(config,n,seed) interface and n=128 smoke check, first draw n units by simple random sampling without replacement from the fixed N=200 potential-outcome schedule, then perform complete randomization assigning exactly floor(n/2) to treatment (n must be even). This two-stage sampled-subset interface is an implementation adaptation; the source mechanism is finite-population complete randomization.
- Only the 12 main-text Table 5 scenarios are encoded. Supplementary Appendix E Cases 13–19 are not included. No original author code or commit was located.
- Use small CPU reproducibility and algebraic checks; do not reproduce the paper’s 5000 randomization repetitions or its full estimator comparison.

**Warnings:**

- No explicit latent-variable metadata or reliably identifiable latent declarations; absence from this list does not prove that no latent variables exist.
