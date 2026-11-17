# Henzi–Ziegel–Gneiting Gamma conditional CDF: smooth and two threshold shifts

> **Unverified extraction — scientific review required.**

**Primary area:** Quantile Inference

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Henzi, A., Ziegel, J. F., and Gneiting, T. (2021). Isotonic distributional regression. Journal of the Royal Statistical Society: Series B (Statistical Methodology), 83(5), 963–993. DOI: 10.1111/rssb.12450.

**DOI:** 10.1111/rssb.12450 · **Source locator:** Version of Record, JRSS-B 83(5), 2021, 31-page PDF. Section 4: X~Uniform(0,10) in unnumbered paragraph immediately before (23), PDF p.17 / journal p.979; (23) Smooth Gamma and (24) Discontinuous Gamma on PDF p.17 / p.979; (25) Non-isotonic Gamma on PDF p.19 / p.981. PDF p.18 / p.980 is Table 1. Section 2.4 Theorem 3: PDF pp.12–13 / pp.974–975. Supplement dated 2021-03-19: S4 p.7 and S5/Table S1 p.8.

## DGP / generation mechanism

**Sampling design:** Unit: one fully observed scalar-covariate/response pair (X,Y_s); Dependence: iid across rows, dependent X and Y within each row; no clusters, panel, network or interference. Reusing a seed across scenarios is only a computational coupling, not an extra observed joint vector.

**Generator source:** [generator.py](../generators/qdi-henzi-2021-gamma-shift-v1.py)

**Keywords (source-described):** Nonlinearity

**Observed variables**

X, Y

**Latent variables**

G_i

**Latent-variable identification:** candidates from equations need review

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

**Formal Section 4, PDF p.17 / journal p.979, unnumbered paragraph before (23)**

$$
X_{i}\overset{\mathrm{iid}}{\sim} \mathrm{Uniform}(0,10)
$$

**(23) Smooth Gamma; formal PDF p.17 / journal p.979**

$$
G_{i} \mid  X_{i}=x \sim \Gamma(\text{ shape }=\sqrt{x}, \text{ scale }=\min(\max(x,1),6))
$$

$$
Y_{i}=G_{i}
$$

**(24) Discontinuous Gamma; formal PDF p.17 / journal p.979**

$$
Y_{i}=G_{i}+10\cdot 1\{X_{i}\geq 5\}
$$

**(25) Non-isotonic Gamma; formal PDF p.19 / journal p.981**

$$
Y_{i}=G_{i}-2\cdot 1\{X_{i}\geq 7\}
$$

**Adapted QDI target**

$$
\theta_{s}=P(Y_{i}\leq 10 \mid  X_{i}=5.5)
$$

<details>
<summary>Original source equations (verbatim)</summary>

<pre>
X_i iid Uniform(0,10)
G_i | X_i=x ~ Gamma(shape=sqrt(x), scale=min(max(x,1),6)); Y_i=G_i
Y_i=G_i+10*1{X_i&gt;=5}
Y_i=G_i-2*1{X_i&gt;=7}
theta_s=P(Y_i&lt;=10 | X_i=5.5)
</pre>

</details>


## Parameter scenarios, estimands and truth

| Scenario | Estimand | Definition | Reported value | Evidence status |
|---|---|---|---|---|
| smooth_gamma | Conditional cumulative distribution function | Scalar conditional CDF P(Y_s&lt;=10 \| X=5.5) for each source scenario, using the explicitly specified conditional-law version. Not a marginal CDF, quantile, causal effect, or simultaneous band. | 0.44022759069779993 | reported_numeric |
| discontinuous_gamma | Conditional cumulative distribution function | Scalar conditional CDF P(Y_s&lt;=10 \| X=5.5) for each source scenario, using the explicitly specified conditional-law version. Not a marginal CDF, quantile, causal effect, or simultaneous band. | 0.0 | reported_numeric |
| non_isotonic_gamma | Conditional cumulative distribution function | Scalar conditional CDF P(Y_s&lt;=10 \| X=5.5) for each source scenario, using the explicitly specified conditional-law version. Not a marginal CDF, quantile, causal effect, or simultaneous band. | 0.44022759069779993 | reported_numeric |

**Original submitted target notation:** theta_s = F_s(10 \| 5.5)


## Identifiability assumptions

- Independent identically distributed observation pairs (X,Y_s), as implemented from the Section 4 sampling design; independent validation sampling is explicit in supplement S4.
- X is fully observed Uniform(0,10); Y_s is fully observed. No censoring, selection or missingness.
- X=5.5 is interior with design density 0.1. Since P(X=5.5)=0, pointwise observational identification uses the locally continuous version of the conditional CDF specified by the DGP, not conditioning on a positive-mass stratum.
- All three conditional laws are continuous in y; at the discontinuous scenario query the CDF is exactly zero at its lower support endpoint. Positive density and interior-CDF asymptotics are not asserted there.
- Smooth and upward-shift laws are stochastically increasing in X; downward shift at X=7 violates global isotonicity. Uniform continuity in X fails at shifts; formal Theorem 3 is not claimed for all scenarios or at the X=0 limiting boundary.
- No causal interpretation or causal identification assumptions are needed.

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Adaptations from the source (submitted, unverified):**

- Keep published equations (23)–(25) and their parameters unchanged; rename the selected scenario response to Y. Use the formal unjittered law and &gt;=7 NI threshold; separately document differences from the inspected author R script.
- Fix the scalar noncausal QDI target P(Y&lt;=10 \| X=5.5), selected by the user; the source evaluates distributional predictions by CRPS/L2, not this scalar numeric truth.
- Use n=128, seed=1729 local checks instead of the source 500 replicates at n=500/1000/2000/4000 with independent m=5000 test sets. No estimator fitting or coverage evaluation.
- Use local NumPy RNG and independently written Python rather than reproducing the author R random stream. Redraw exact X=0 finite-RNG endpoint; ideal continuous law gives that endpoint zero mass.

**Warnings:**

- Latent-variable candidates inferred from source equations; confirm their roles and completeness against the original paper or generator.
