# Fong-Yiu bounded cubic quantile distribution: marginal 0.9 quantile

> **Unverified extraction — scientific review required.**

**Primary area:** Quantile Inference

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Fong, Edwin and Yiu, Andrew (2026). Bayesian quantile estimation and regression with martingale posteriors. Journal of the Royal Statistical Society Series B: Statistical Methodology, 88(4), 1130-1159. doi:10.1093/jrsssb/qkaf080. Reference preprint: arXiv:2406.03358v1 (5 June 2024). First published online 16 December 2025; issue assignment September 2026. These are distinct dates.

**DOI:** 10.1093/jrsssb/qkaf080 · **Source locator:** Primary: publisher 2026 issue PDF, Section 7.1, PDF p.23 / journal p.1152, first-paragraph unnumbered quantile equation; Figure 4 and discussion PDF p.24 / journal p.1153. Code availability: PDF p.28 / journal p.1157. Supporting arXiv:2406.03358v1 Section 7.1 PDF/printed p.25, Figure 4 and p.26 discussion; publisher supplement E.3.1 PDF/printed pp.47-48, formula/support on p.48. Author code: commit a779aef7ce40d6403e006c65b5177603cebd4758, run_scripts/7.1_sim_qmp.py lines 14-36 (grid, quantile, sim, seed, sizes); qmp/qmp_functions.py lines 45-49 (Q0). Full file hashes and paper-code differences in author_code_audit.json.

## DGP / generation mechanism

**Sampling design:** Unit: one fully observed scalar response Y per row; Dependence: iid across rows; no clustering, serial dependence or interference structure; Sample Sizes: [50, 500]; N Semantics: n is the actual requested row count and overrides nominal paper_n; the latter is design metadata only.; Cross Scenario Coupling: Author script uses n=50 as prefix of a single n=500 sample. Local generator yields prefixes for matching seed across n; iid refers to rows within a dataset, not independence of scenarios sharing a seed.

**Generator source:** [generator.py](../generators/qdi-fong-yiu-2026-cubic-quantile-v1.py)

**Keywords (source-described):** Nonlinearity

**Observed variables**

Y

**Latent variables**

U_i

**Latent-variable identification:** candidates from equations need review

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

$$
Y_1,\ldots ,Y_n iid \sim P\cdot , Q\cdot (u)=4(u-0.4)^{3}+0.2u, 0<u<1
$$

n in {50,500}.

$$
U_i iid \sim \mathrm{Uniform}(0,1)
$$

$$
Y_i=4(U_i-0.4)^{3}+0.2U_i. No added noise
$$

only Y is observed.

$$
Q'(u)=12(u-0.4)^{2}+0.2>=0.2
$$

$$
Q(0)=-0.256
$$

$$
Q(1)=1.064 (continuous endpoint extensions).
$$

$$
\theta=inf\{y:F_Y(y)>=0.9\}=Q\cdot (0.9)=17/25=0.68.
$$

$$
Q\cdot (u)=4u^{3}-4.8u^{2}+2.12u-0.256
$$

F_Y(y) is the unique inverse root in [0,1] on the support, with 0/1 outside.

<details>
<summary>Original source equations (verbatim)</summary>

<pre>
Y_1,...,Y_n iid ~ P*, Q*(u)=4(u-0.4)^3+0.2u, 0&lt;u&lt;1; n in {50,500}.
U_i iid ~ Uniform(0,1); Y_i=4(U_i-0.4)^3+0.2U_i. No added noise; only Y is observed.
Q&#x27;(u)=12(u-0.4)^2+0.2&gt;=0.2; Q(0)=-0.256; Q(1)=1.064 (continuous endpoint extensions).
theta=inf{y:F_Y(y)&gt;=0.9}=Q*(0.9)=17/25=0.68.
Q*(u)=4u^3-4.8u^2+2.12u-0.256; F_Y(y) is the unique inverse root in [0,1] on the support, with 0/1 outside.
</pre>

</details>


## Parameter scenarios, estimands and truth

| Scenario | Estimand | Definition | True value | Evidence status |
|---|---|---|---|---|
| original_n50 | theta = Q_Y(0.9) | Marginal population quantile inf{y: P(Y&lt;=y)&gt;=0.9} under Y=4(U-0.4)^3+0.2U, U~Uniform(0,1); no conditioning variables or interventions. The fixed query is tau=0.9 in both scenarios. | 0.68 | reported_numeric |
| original_n500 | theta = Q_Y(0.9) | Marginal population quantile inf{y: P(Y&lt;=y)&gt;=0.9} under Y=4(U-0.4)^3+0.2U, U~Uniform(0,1); no conditioning variables or interventions. The fixed query is tau=0.9 in both scenarios. | 0.68 | reported_numeric |

## Identifiability assumptions

- Independent and identically distributed scalar observations from the declared P*: explicitly stated in publisher Section 7.1 journal p.1152 (PDF p.23), consistent with arXiv v1 p.25.
- Y is fully observed; no selection, censoring or missingness is introduced. The simulator has no covariates; U is internal inverse-transform randomness, not an observed covariate.
- Derived regularity: Q is continuous and Q'(u)=12(u-0.4)^2+0.2&gt;=0.2 on [0,1], so the marginal quantile is unique and F has positive continuous density at the interior target.
- The target is a functional of the observed marginal distribution. At Q(0.9)=0.68 the density is 0.3125. No causal intervention, confounding, cross-world or mediation assumptions apply.

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Warnings:**

- Latent-variable candidates inferred from source equations; confirm their roles and completeness against the original paper or generator.
