# Partially Invalid Instruments with Linear Endogenous Treatment

> **Unverified extraction — scientific review required.**

**Primary area:** IV — Instrumental Variables

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Kang, H., Zhang, A., Cai, T. T. and Small, D. S. (2016). Instrumental Variables Estimation With Some Invalid Instruments and its Application to Mendelian Randomization. JASA 111(513), 132–144. DOI: 10.1080/01621459.2014.994705.

**DOI:** — · **Source locator:** arXiv v3 (2014-09-21), §4 PDF pp.22–23; fixed parameters from hyunseungkang/sisVIVE README.md Examples lines 24–38, commit 0ae8499f260f37edd68a057d1e2f0634b1b98b42.

## DGP / generation mechanism

**Sampling design:** Unit: individual; Dependence: iid across individuals; within-unit dependencies explicitly specified by the structural equations

**Generator source:** [generator.py](../generators/iv-kang-2016-invalid-linear-v1.py)

**Observed variables**

Z1, Z2, Z3, Z4, Z5, Z6, Z7, Z8, Z9, Z10, D, Y

**Latent variables**

ξ

**Latent-variable identification:** candidates from equations need review

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

$$
Z_{j}\overset{\mathrm{iid}}{\sim} \mathcal{N}(0,1), j=1,\ldots ,10
$$

Z

independent of (ξ,ε)

$$
(\xi,\varepsilon) joint normal: mean 0, variances 1, correlation \rho=0.8.
$$

$$
D=1+\sum_{j=1}^{10} Z_{j}+\xi.
$$

$$
Y=1+Z_{1}+Z_{2}+Z_{3}+\beta D+\varepsilon
$$

$$
\beta=1.
$$

<details>
<summary>Original source equations (verbatim)</summary>

<pre>
Zⱼ iid N(0,1), j=1,…,10; Z independent of (ξ,ε).
(ξ,ε) joint normal: mean 0, variances 1, correlation ρ=0.8.
D=1+Σⱼ₌₁¹⁰ Zⱼ+ξ.
Y=1+Z₁+Z₂+Z₃+βD+ε; β=1.
</pre>

</details>


## Parameter scenarios, estimands and truth

| Scenario | Estimand | Definition | True value | Evidence status |
|---|---|---|---|---|
| author_readme_fixed | beta | Constant structural slope beta = E[Y(do(D=d+1))-Y(do(D=d))], with natural Z and errors held under the same intervention law. | 1.0 | reported_numeric |

## Identifiability assumptions

- Consistency and well-defined treatment interventions.
- Independent identically distributed units; no interference.
- Ten independent standard normal candidate instruments, independent of jointly Gaussian structural errors.
- Structural equation Y=1+Z1+Z2+Z3+beta*D+epsilon has a constant causal slope.
- Z4–Z10 are relevant and satisfy exclusion; Z1–Z3 violate exclusion. Do not apply all-IV validity.
- More than half of candidate instruments are valid (7/10); the linear invalid-IV identification framework applies.

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Warnings:**

- Latent-variable candidates inferred from source equations; confirm their roles and completeness against the original paper or generator.
