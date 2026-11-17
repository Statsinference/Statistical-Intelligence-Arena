# Pointwise conditional mean in the Liang-Liu-Li-Tsai partially linear single-index design

> **Unverified extraction — scientific review required.**

**Primary area:** Nonparametric Regression

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Liang, H., Liu, X., Li, R. and Tsai, C.-L. (2010). Estimation and testing for partially linear single-index models. The Annals of Statistics 38(6), 3811-3836. DOI: 10.1214/10-AOS835.

**DOI:** — · **Source locator:** Formula bodies: (2.1) on PDF p.3, (4.2) on PDF p.10. Section starts: Section 2 on PDF p.3, Section 2.1 on PDF p.3, Section 4 on PDF p.10, Section Example4.1 on PDF p.10, Section Table2 on PDF p.11. Unnumbered paragraph on PDF p.10: "We generated 500 realizations" (Example4.1 repetition count and sample-size grid). Unnumbered paragraph on PDF p.10: "where z1,z2,z3 are independent" (covariate laws, odd/even X, epsilon distribution, a,b and resulting alpha,beta). All PDF pages are 1-based pages of the fixed reading file 1211.3509v1. No printed journal page is inferred by adding an offset.

## DGP / generation mechanism

**Sampling design:** Unit: one independent observed row (Z1,Z2,Z3,X,Y), preserving 1-based row order; Dependence: Independent rows with deterministic alternating X: odd rows 0, even rows 1. They are not identically distributed. Z draws and errors are independent across rows; there is no cluster/Markov dependence.

**Generator source:** [generator.py](../generators/nri-liangliu-2010-singleindex-v1.py)

**Keywords (source-described):** Interactions · Nonlinearity

**Observed variables**

Z1, Z2, Z3, X, Y

**Latent variables**

Not explicitly identified (review required)

**Latent-variable identification:** not explicitly specified

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

**1. Continuous design**

```math
\mathrm{For} \text{ each } \mathrm{row} i=1..n, \text{ independently } \mathrm{draw} Z_{i1},Z_{i2},Z_{i3}\overset{\mathrm{iid}}{\sim} \mathrm{Uniform}(0,1)
```

Three independent source uniforms

no truncation of the resulting index.

**2. Fixed binary design**

Source notation retained without guessing:

<pre>Set X_i=0 for odd i, X_i=1 for even i (1-based row index)</pre>

Deterministic source design

Source notation retained without guessing:

<pre>no Bernoulli random draw, no added index column, no new noise.</pre>

**3. Single index**

```math
t_{i}=(Z_{i1}+Z_{i2}+Z_{i3})/\sqrt{3}, \text{ with } 0\leq t_{i}\leq \sqrt{3}
```

Weights 1/sqrt(3), stored as their finite JSON approximations

0.5774 is only a four-decimal display.

**4. Mean function**

```math
m_{i}=\sin(\pi\cdot (t_{i}-0.3912)/(1.3409-0.3912))+0.3\cdot X_{i}
```

Deterministic

a,b are phase/scale constants, not truncation limits

Sine can be negative outside [a,b].

**5. Innovation**

```math
\varepsilon_{i}\overset{\mathrm{iid}}{\sim} \mathcal{N}(0,1)
```

independent of all design uniforms

```math
\mathrm{Source} \mathrm{multiplier} 0.1 \mathrm{gives} \text{ noise } \mathrm{sd}=0.1 \text{ and } \text{ variance }=0.01
```

it is applied once.

**6. Response and export**

```math
Y_{i}=m_{i}+0.1\cdot \varepsilon_{i}
```

export Z1,Z2,Z3,X,Y in row order. No index t, noiseless mean or noise column is returned.

<details>
<summary>Original source equations (verbatim)</summary>

<pre>
For each row i=1..n, independently draw Z_i1,Z_i2,Z_i3 iid Uniform(0,1). Three independent source uniforms; no truncation of the resulting index.
Set X_i=0 for odd i, X_i=1 for even i (1-based row index). Deterministic source design; no Bernoulli random draw, no added index column, no new noise.
t_i=(Z_i1+Z_i2+Z_i3)/sqrt(3), with 0&lt;=t_i&lt;=sqrt(3). Weights 1/sqrt(3), stored as their finite JSON approximations; 0.5774 is only a four-decimal display.
m_i=sin(pi*(t_i-0.3912)/(1.3409-0.3912))+0.3*X_i. Deterministic; a,b are phase/scale constants, not truncation limits. Sine can be negative outside [a,b].
epsilon_i iid N(0,1), independent of all design uniforms. Source multiplier 0.1 gives noise sd=0.1 and variance=0.01; it is applied once.
Y_i=m_i+0.1*epsilon_i; export Z1,Z2,Z3,X,Y in row order. No index t, noiseless mean or noise column is returned.
</pre>

</details>


## Parameter scenarios, estimands and truth

| Scenario | Estimand | Definition | Reported value |
|---|---|---|---|
| index-mid-x0 | Pointwise conditional mean | The scalar conditional mean at the scenario's fixed covariate query (z0, x0). The nonparametric component is evaluated at the single-index value t0 = z0'alpha with alpha = (1,1,1)/sqrt(3); the linear component contributes x0*beta. This is a pointwise target, not a curve-level or band target. | 0.9818328784088086 |
| index-mid-x1 | Pointwise conditional mean | The scalar conditional mean at the scenario's fixed covariate query (z0, x0). The nonparametric component is evaluated at the single-index value t0 = z0'alpha with alpha = (1,1,1)/sqrt(3); the linear component contributes x0*beta. This is a pointwise target, not a curve-level or band target. | 1.2818328784088087 |
| index-low-x0 | Pointwise conditional mean | The scalar conditional mean at the scenario's fixed covariate query (z0, x0). The nonparametric component is evaluated at the single-index value t0 = z0'alpha with alpha = (1,1,1)/sqrt(3); the linear component contributes x0*beta. This is a pointwise target, not a curve-level or band target. | 0.8402560393492512 |
| index-high-x1 | Pointwise conditional mean | The scalar conditional mean at the scenario's fixed covariate query (z0, x0). The nonparametric component is evaluated at the single-index value t0 = z0'alpha with alpha = (1,1,1)/sqrt(3); the linear component contributes x0*beta. This is a pointwise target, not a curve-level or band target. | 0.47575809676587577 |

**Original submitted target notation:** eta(z0'alpha) + x0*beta = E[Y \| Z = z0, X = x0]


## Identifiability assumptions

- For each row, Z1,Z2,Z3 are independent Uniform(0,1); uniforms and zero-mean Gaussian errors are independent across rows.
- X is fixed by the 1-based row index: odd rows 0, even rows 1. Rows are independent but not identically distributed; no stochastic Bernoulli design or causal treatment assignment is introduced.
- With fixed design X, the common regression function is m(z,x)=sin(pi*((z1+z2+z3)/sqrt(3)-a)/(b-a))+beta*x. Independent centred errors identify this function in both X groups.
- The source formula uses the full index support [0,sqrt(3)]; a=.3912 and b=1.3409 are phase/scale constants, not clipping, truncation or domain limits.
- Complete queries fix Z1,Z2,Z3 and X in config. All queries have valid Z in [0,1]^3 and binary X. The n&gt;=2 interface check has both fixed X levels; this is pointwise mean verification, not a confidence-band result.

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Adaptations from the source (submitted, unverified):**

- Retain model (4.2), independent U(0,1) Z coordinates, source 1-based fixed odd/even X=0/1, exact index formula (Z1+Z2+Z3)/sqrt(3), beta=.3, a=.3912, b=1.3409 and error sd=.1. Weights are stored as finite JSON approximations to 1/sqrt(3); .5774 in the source is its four-decimal display.
- Select four fixed complete queries (Z1,Z2,Z3,X) and target their scalar conditional response means. These queries are contribution choices, not source experiment parameters.
- Use the requested interface row count rather than only source n=50/100/200. Preserve alternating X in numeric list order; a separate index column is unnecessary. Source 500 estimator repetitions, profile least squares, SCAD and tests are not executed.

**Warnings:**

- No explicit latent-variable metadata or reliably identifiable latent declarations; absence from this list does not prove that no latent variables exist.
