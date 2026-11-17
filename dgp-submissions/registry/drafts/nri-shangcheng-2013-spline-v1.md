# Pointwise conditional mean in the Shang–Cheng smoothing-spline design

> **Unverified extraction — scientific review required.**

**Primary area:** Nonparametric Regression

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Shang, Z. and Cheng, G. (2013). Local and global asymptotic inference in smoothing spline models. The Annals of Statistics 41(5), 2608–2638. DOI: 10.1214/13-AOS1164.

**DOI:** — · **Source locator:** Formula bodies: (6.1) on PDF p.24, (6.2) on PDF p.24, (6.4) on PDF p.25. Section starts: Section 6 on PDF p.24. Unnumbered paragraph on PDF p.25: "To examine the pointwise asymptotic CI" (unnumbered Beta-density mixture and experiment parameters). All PDF pages are 1-based pages of the fixed reading file 1212.6788v3. No printed journal page is inferred by adding an offset.

## DGP / generation mechanism

**Sampling design:** Unit: independent observed pair (Z,Y); Dependence: iid across pairs; within a pair, Y depends on Z through g0(Z)

**Generator source:** [generator.py](../generators/nri-shangcheng-2013-spline-v1.py)

**Keywords (source-described):** Nonlinearity

**Observed variables**

Z, Y

**Latent variables**

Not explicitly identified (review required)

**Latent-variable identification:** not explicitly specified

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

**1. Observed design**

$$
Z_{i}\overset{\mathrm{iid}}{\sim} \mathrm{Uniform}(0,1)
$$

Source interval [0,1].

**2. Regression function**

$$
B_{\text{ a },b}(z)=\Gamma(\text{ a }+b)/(\Gamma(\text{ a })\cdot \Gamma(b))\cdot z^{\text{ a }-1}\cdot (1-z)^{b-1}
$$

$$
g_{0}(z)=0.6\cdot B_{30,17}(z)+0.4\cdot B_{3,11}(z)
$$

Deterministic source Beta densities

all declared shapes exceed 1, so both endpoint limits are 0.

**3. Gaussian error**

$$
\varepsilon_{i}\overset{\mathrm{iid}}{\sim} \mathcal{N}(0,0.05^{2})
$$

independent of Z

$$
\mathrm{Noise} \mathrm{sd}=0.05
$$

$$
\text{ variance }=0.0025.
$$

**4. Observed response**

$$
Y_{i}=g_{0}(Z_{i})+\varepsilon_{i}
$$

return Z,Y. No additional noise or oracle column

Source notation retained without guessing:

<pre>Both z0=.5 and .64 are contribution query choices.</pre>

<details>
<summary>Original source equations (verbatim)</summary>

<pre>
Z_i iid Uniform(0,1). Source interval [0,1].
B_(a,b)(z)=Gamma(a+b)/(Gamma(a)*Gamma(b))*z^(a-1)*(1-z)^(b-1); g0(z)=0.6*B_(30,17)(z)+0.4*B_(3,11)(z). Deterministic source Beta densities; all declared shapes exceed 1, so both endpoint limits are 0.
epsilon_i iid N(0,0.05^2), independent of Z. Noise sd=0.05; variance=0.0025.
Y_i=g0(Z_i)+epsilon_i; return Z,Y. No additional noise or oracle column. Both z0=.5 and .64 are contribution query choices.
</pre>

</details>


## Parameter scenarios, estimands and truth

| Scenario | Estimand | Definition | Reported value | Evidence status |
|---|---|---|---|---|
| peak-mode | Pointwise conditional mean | The scalar conditional mean at the scenario's fixed query point z0. This is a pointwise target, not a simultaneous confidence-band target. | 3.406258317314956 | reported_numeric |
| query-z0-050 | Pointwise conditional mean | The scalar conditional mean at the scenario's fixed query point z0. This is a pointwise target, not a simultaneous confidence-band target. | 0.5910281636814358 | reported_numeric |

**Original submitted target notation:** g0(z0) = E[Y \| Z = z0]


## Identifiability assumptions

- Observed pairs (Z,Y) are independent and identically distributed across sampling units
- Z is Uniform(0,1) and the Gaussian regression error is independent of Z
- The declared two-component Beta-density mixture is the conditional mean function
- The query point is fixed in the interior of [0,1]; machine checks do not establish smoothing-spline confidence-interval or simultaneous-band coverage

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Adaptations from the source (submitted, unverified):**

- Keep the Case (I) Gaussian regression DGP and its Beta mixture unchanged.
- Replace interval/curve-level inference by scalar g0(z0); both z0=0.5 and z0=0.64 are contribution choices. A 30-point evaluation grid does not establish an original fixed query at 0.5.
- Use the requested n and CPU checks; do not fit periodic splines or assess coverage.

**Warnings:**

- No explicit latent-variable metadata or reliably identifiable latent declarations; absence from this list does not prove that no latent variables exist.
