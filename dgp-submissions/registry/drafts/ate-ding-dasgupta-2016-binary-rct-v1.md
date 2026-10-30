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

**Keywords (source-described):** Linearity

**Observed variables**

A, Y

**Latent variables**

Not explicitly identified (review required)

**Latent-variable identification:** not explicitly specified

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

$$
N_{11}=#\{i:Y_i(1)=1,Y_i(0)=1\}
$$

$$
N_{10}=#\{i:Y_i(1)=1,Y_i(0)=0\}
$$

$$
N_{01}=#\{i:Y_i(1)=0,Y_i(0)=1\}
$$

$$
N_{00}=#\{i:Y_i(1)=0,Y_i(0)=0\}
$$

$$
N=N_{11}+N_{10}+N_{01}+N_{00}=200.
$$

$$
N_{1}=N_{0}=100
$$

$$
P(A=a)=1/binom(N,N_{1}) for every assignment vector a with sum_i a_i=N_{1}.
$$

$$
Y_i=A_i Y_i(1)+(1-A_i)Y_i(0). Only (A_i,Y_i) are returned.
$$

$$
\tau=N^\{-1\} sum_i[Y_i(1)-Y_i(0)]=(N_{10}-N_{01})/N.
$$

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

| Scenario | Estimand | Definition | True value | Evidence status |
|---|---|---|---|---|
| case01_independent_null | tau = N^{-1} sum_i [Y_i(1)-Y_i(0)] = (N10-N01)/N | Finite-population average treatment effect / causal risk difference for intervention A=1 versus A=0 over the N=200 experimental units. Y_i(1) and Y_i(0) are binary fixed potential outcomes; observed Y_i=A_i Y_i(1)+(1-A_i)Y_i(0). | 0.0 | reported_numeric |
| case02_independent_positive | tau = N^{-1} sum_i [Y_i(1)-Y_i(0)] = (N10-N01)/N | Finite-population average treatment effect / causal risk difference for intervention A=1 versus A=0 over the N=200 experimental units. Y_i(1) and Y_i(0) are binary fixed potential outcomes; observed Y_i=A_i Y_i(1)+(1-A_i)Y_i(0). | 0.2 | reported_numeric |
| case03_independent_positive | tau = N^{-1} sum_i [Y_i(1)-Y_i(0)] = (N10-N01)/N | Finite-population average treatment effect / causal risk difference for intervention A=1 versus A=0 over the N=200 experimental units. Y_i(1) and Y_i(0) are binary fixed potential outcomes; observed Y_i=A_i Y_i(1)+(1-A_i)Y_i(0). | 0.35 | reported_numeric |
| case04_independent_negative | tau = N^{-1} sum_i [Y_i(1)-Y_i(0)] = (N10-N01)/N | Finite-population average treatment effect / causal risk difference for intervention A=1 versus A=0 over the N=200 experimental units. Y_i(1) and Y_i(0) are binary fixed potential outcomes; observed Y_i=A_i Y_i(1)+(1-A_i)Y_i(0). | -0.3 | reported_numeric |
| case05_independent_negative | tau = N^{-1} sum_i [Y_i(1)-Y_i(0)] = (N10-N01)/N | Finite-population average treatment effect / causal risk difference for intervention A=1 versus A=0 over the N=200 experimental units. Y_i(1) and Y_i(0) are binary fixed potential outcomes; observed Y_i=A_i Y_i(1)+(1-A_i)Y_i(0). | -0.35 | reported_numeric |
| case06_positive_association_null | tau = N^{-1} sum_i [Y_i(1)-Y_i(0)] = (N10-N01)/N | Finite-population average treatment effect / causal risk difference for intervention A=1 versus A=0 over the N=200 experimental units. Y_i(1) and Y_i(0) are binary fixed potential outcomes; observed Y_i=A_i Y_i(1)+(1-A_i)Y_i(0). | 0.0 | reported_numeric |
| case07_positive_association | tau = N^{-1} sum_i [Y_i(1)-Y_i(0)] = (N10-N01)/N | Finite-population average treatment effect / causal risk difference for intervention A=1 versus A=0 over the N=200 experimental units. Y_i(1) and Y_i(0) are binary fixed potential outcomes; observed Y_i=A_i Y_i(1)+(1-A_i)Y_i(0). | 0.1 | reported_numeric |
| case08_positive_association | tau = N^{-1} sum_i [Y_i(1)-Y_i(0)] = (N10-N01)/N | Finite-population average treatment effect / causal risk difference for intervention A=1 versus A=0 over the N=200 experimental units. Y_i(1) and Y_i(0) are binary fixed potential outcomes; observed Y_i=A_i Y_i(1)+(1-A_i)Y_i(0). | 0.2 | reported_numeric |
| case09_positive_association | tau = N^{-1} sum_i [Y_i(1)-Y_i(0)] = (N10-N01)/N | Finite-population average treatment effect / causal risk difference for intervention A=1 versus A=0 over the N=200 experimental units. Y_i(1) and Y_i(0) are binary fixed potential outcomes; observed Y_i=A_i Y_i(1)+(1-A_i)Y_i(0). | 0.5 | reported_numeric |
| case10_positive_association_negative | tau = N^{-1} sum_i [Y_i(1)-Y_i(0)] = (N10-N01)/N | Finite-population average treatment effect / causal risk difference for intervention A=1 versus A=0 over the N=200 experimental units. Y_i(1) and Y_i(0) are binary fixed potential outcomes; observed Y_i=A_i Y_i(1)+(1-A_i)Y_i(0). | -0.1 | reported_numeric |
| case11_positive_association_negative | tau = N^{-1} sum_i [Y_i(1)-Y_i(0)] = (N10-N01)/N | Finite-population average treatment effect / causal risk difference for intervention A=1 versus A=0 over the N=200 experimental units. Y_i(1) and Y_i(0) are binary fixed potential outcomes; observed Y_i=A_i Y_i(1)+(1-A_i)Y_i(0). | -0.2 | reported_numeric |
| case12_positive_association_negative | tau = N^{-1} sum_i [Y_i(1)-Y_i(0)] = (N10-N01)/N | Finite-population average treatment effect / causal risk difference for intervention A=1 versus A=0 over the N=200 experimental units. Y_i(1) and Y_i(0) are binary fixed potential outcomes; observed Y_i=A_i Y_i(1)+(1-A_i)Y_i(0). | -0.5 | reported_numeric |

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

**Warnings:**

- No explicit latent-variable metadata or reliably identifiable latent declarations; absence from this list does not prove that no latent variables exist.
