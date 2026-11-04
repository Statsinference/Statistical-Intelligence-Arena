# Conditional mean of the nonlinear AR(1) regression in the Zhao–Wu simultaneous confidence band simulation

> **Unverified extraction — scientific review required.**

**Primary area:** Nonparametric Regression

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Zhao, Z. and Wu, W. B. (2008). Confidence bands in nonparametric time series regression. The Annals of Statistics 36(4), 1854-1878. DOI: 10.1214/07-AOS533.

**DOI:** — · **Source locator:** Formula bodies: (1.1) on PDF p.2, (5.1) on PDF p.12, (5.2) on PDF p.12. Section starts: Section 5 on PDF p.11, Section 6 on PDF p.13. Unnumbered paragraph on PDF p.11: "In this section" (standard-normal innovations and two structural models). Unnumbered paragraph on PDF p.12: "To assess the performance of our SCB" (Model1 numerical mean, scale, n, replications, evaluation interval). All PDF pages are 1-based pages of the fixed reading file 0808.1010v1. No printed journal page is inferred by adding an offset.

## DGP / generation mechanism

**Sampling design:** Unit: time series observation (consecutive pairs of one Markov chain realisation); Dependence: Time-homogeneous Markov recursion with finite zero initialization and burn-in 1000; adjacent pairs share X_(i+1)=Y_i; exact stationarity is not asserted.

**Generator source:** [generator.py](../generators/nri-zhao-wu-2008-ar1scb-v1.py)

**Keywords (source-described):** Nonlinearity

**Observed variables**

X, Y

**Latent variables**

Not explicitly identified (review required)

**Latent-variable identification:** not explicitly specified

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

**1. Initialization**

Source notation retained without guessing:

<pre>Set Y0=0 and burn_in=1000 before collecting the n regression pairs</pre>

Implementation choices

not source-specified initialization or burn-in parameters.

**2. Innovation sequence**

$$
\varepsilon_{t}\overset{\mathrm{iid}}{\sim} \mathcal{N}(0,1)
$$

independent of the past

draw sequentially during recursion

Source standard-normal innovations

$$
\text{ noise } \mathrm{multiplier} s=0.4.
$$

**3. Recursion**

$$
Y_{t}=0.9\cdot \sin(Y_{t-1})+0.4\cdot \varepsilon_{t} \text{ for } \mathrm{burn}_{in}+n \mathrm{updates}
$$

Compute source nonlinear mean before adding each independent innovation.

**4. Observation pairs**

$$
\mathrm{Return} (X_{i},Y_{i})=(Y_{\mathrm{burn}_{in}+i-1},Y_{\mathrm{burn}_{in}+i}), i=1..n
$$

Deterministic export in time order

$$
X_{i+1}=Y_{i} \mathrm{exactly}
$$

no innovation column.

<details>
<summary>Original source equations (verbatim)</summary>

<pre>
Set Y0=0 and burn_in=1000 before collecting the n regression pairs. Implementation choices; not source-specified initialization or burn-in parameters.
epsilon_t iid N(0,1), independent of the past; draw sequentially during recursion. Source standard-normal innovations; noise multiplier s=0.4.
Y_t=0.9*sin(Y_(t-1))+0.4*epsilon_t for burn_in+n updates. Compute source nonlinear mean before adding each independent innovation.
Return (X_i,Y_i)=(Y_(burn_in+i-1),Y_(burn_in+i)), i=1..n. Deterministic export in time order; X_(i+1)=Y_i exactly; no innovation column.
</pre>

</details>


## Parameter scenarios, estimands and truth

| Scenario | Estimand | Definition | True value | Evidence status |
|---|---|---|---|---|
| original-s04 | mu(x0) = E[Y_i \| X_i = x0] = 0.9*sin(x0) | Pointwise conditional mean of the Markov regression at a single fixed query point x0 inside the source design interval T = [-1.1,1.1]; a scalar quantity, not a simultaneous confidence band and not a coverage probability. | 0.4314829847437827 | reported_numeric |
| interior-anchor | mu(x0) = E[Y_i \| X_i = x0] = 0.9*sin(x0) | Pointwise conditional mean of the Markov regression at a single fixed query point x0 inside the source design interval T = [-1.1,1.1]; a scalar quantity, not a simultaneous confidence band and not a coverage probability. | 0.0 | reported_numeric |

## Identifiability assumptions

- Time-homogeneous first-order Markov recursion Y_t=.9*sin(Y_(t-1))+.4*epsilon_t; innovations iid N(0,1) and independent of the past.
- The mean map is globally contractive with Lipschitz constant .9. The process admits an invariant law, but the finite simulation starts at zero; burn-in 1000 does not certify exact stationarity.
- Adjacent exported rows are dependent: X_(i+1)=Y_i. The marginal distribution after finite initialization need not equal the invariant law.
- For every exported time, the new innovation has conditional mean zero. Therefore E[Y_t\|Y_(t-1)=x]=.9*sin(x) without an exact-stationarity assumption.
- The positive Gaussian transition density gives support around each fixed query after at least one update.
- No band coverage, finite-sample cutoff, mixing-rate estimate or named human scientific acceptance is established by the diagnostics.

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Warnings:**

- No explicit latent-variable metadata or reliably identifiable latent declarations; absence from this list does not prove that no latent variables exist.
