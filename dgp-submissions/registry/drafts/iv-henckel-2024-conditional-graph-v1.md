# Conditional instruments in a confounded graph with a mediated total effect

> **Unverified extraction — scientific review required.**

**Primary area:** IV — Instrumental Variables

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Henckel, L., Buttenschoen, M. and Maathuis, M. H. (2024). Graphical tools for selecting conditional instrumental sets. Biometrika 111(3), 771-788. DOI:10.1093/biomet/asad066.

**DOI:** 10.1093/biomet/asad066 · **Source locator:** arXiv:2208.03697 downloaded 2026-10-29: Section 2 eq (1), Figure 1(a), Section 5 PDF pp 11-13; supplement E PDF p 41; author efficientCIS commit 2882bded6c57aeaf8da9df8561da329e71dd932c, SimulationStudy/Main/G1a.R lines 31-42 and 93-95, HelperFunctions/functions.R lines 66-78, 100-121, 197-209.

## DGP / generation mechanism

**Sampling design:** Unit: individual; Dependence: iid conditional on frozen structural coefficients; shared coefficients do not create observation-level dependence

**Generator source:** [generator.py](../generators/iv-henckel-2024-conditional-graph-v1.py)

**Keywords (source-described):** Not specified

**Observed variables**

A, C, L1, B, D, L2, X, M, Y

**Latent variables**

Not explicitly identified (review required)

**Latent-variable identification:** not explicitly specified

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

**Equation 1**

$$
A <- \varepsilon_{A}
$$

**Equation 2**

$$
C <- \varepsilon_{C}
$$

**Equation 3**

$$
L_{1} <- \varepsilon_{\mathrm{L1}}
$$

**Equation 4**

$$
B <- (-0.78408214029946133)\cdot C + \varepsilon_{B}
$$

**Equation 5**

$$
D <- (0.2011394215552596)\cdot A + (0.40685244250001207)\cdot L_{1} + (0.60072810314434222)\cdot B + \varepsilon_{D}
$$

**Equation 6**

$$
L_{2} <- \varepsilon_{\mathrm{L2}}
$$

**Equation 7**

$$
X <- (1.4038923130557954)\cdot L_{1} + (-1.0690158213970873)\cdot B + (-1.8992312433635747)\cdot L_{2} + \varepsilon_{X}
$$

**Equation 8**

$$
M <- (0.35800137127747389)\cdot X + \varepsilon_{M}
$$

**Equation 9**

$$
Y <- (-0.79585700972545459)\cdot C + (-0.71641682995974743)\cdot L_{2} + (-0.52749259051598618)\cdot X + (1.4218960031282049)\cdot M + \varepsilon_{Y}
$$

**Equation 10**

$$
\mathrm{Gaussian} \mathrm{scenario}: \text{ independent } \varepsilon_{v} \sim \mathcal{N}(0,\text{ variance }_{v})
$$

$$
\mathrm{uniform} \mathrm{scenario}: \text{ independent } \varepsilon_{v} \sim \mathrm{Uniform}(-\sqrt{3 \text{ variance }_{v}},\sqrt{3 \text{ variance }_{v}}).
$$

**Equation 11**

$$
\tau_{YX} = \mathrm{coefficient}[Y,X] + \mathrm{coefficient}[M,X]\cdot \mathrm{coefficient}[Y,M].
$$

<details>
<summary>Original source equations (verbatim)</summary>

<pre>
A &lt;- epsilon_A
C &lt;- epsilon_C
L1 &lt;- epsilon_L1
B &lt;- (-0.78408214029946133)*C + epsilon_B
D &lt;- (0.2011394215552596)*A + (0.40685244250001207)*L1 + (0.60072810314434222)*B + epsilon_D
L2 &lt;- epsilon_L2
X &lt;- (1.4038923130557954)*L1 + (-1.0690158213970873)*B + (-1.8992312433635747)*L2 + epsilon_X
M &lt;- (0.35800137127747389)*X + epsilon_M
Y &lt;- (-0.79585700972545459)*C + (-0.71641682995974743)*L2 + (-0.52749259051598618)*X + (1.4218960031282049)*M + epsilon_Y
Gaussian scenario: independent epsilon_v ~ N(0,variance_v); uniform scenario: independent epsilon_v ~ Uniform(-sqrt(3 variance_v),sqrt(3 variance_v)).
tau_YX = coefficient[Y,X] + coefficient[M,X]*coefficient[Y,M].
</pre>

</details>


## Parameter scenarios, estimands and truth

| Scenario | Estimand | Definition | Reported value | Evidence status |
|---|---|---|---|---|
| frozen_gaussian | Population total causal effect | Population total effect d E[Y\|do(X=x)]/dx, equivalently E[Y\|do(X=1)]-E[Y\|do(X=0)], including X-&gt;M-&gt;Y. | -0.018451871582129575 | reported_numeric |
| frozen_uniform | Population total causal effect | Population total effect d E[Y\|do(X=x)]/dx, equivalently E[Y\|do(X=1)]-E[Y\|do(X=0)], including X-&gt;M-&gt;Y. | -0.018451871582129575 | reported_numeric |

**Original submitted target notation:** tau_YX


## Identifiability assumptions

- Acyclic additive linear SEM with mutually independent node errors, including latent roots L1,L2; iid units and no interference.
- Conditional IV tuple Z=(A,B,D), W=C is valid in source G1; use no adjustment for the post-treatment mediator M.
- Population conditional relevance is checked from the full model covariance; conditional exclusion/exogeneity follow graph separation after removing directed causal paths X-&gt;Y.

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Adaptations from the source (submitted, unverified):**

- Freeze one new PCG64 parameter draw seed 1729 from the original coefficient and variance laws; this is not the original R seed-5 draw or its published RMSE experiment.
- Keep the graph G1 from the author code; rename code node e to M to expose its mediator role.
- Both Gaussian and uniform errors use the same frozen graph and coefficients as two scenarios, not separate families.
- Return observed nodes only; latent L1 and L2 are retained internally. Sample size is a hook input rather than fixed at 50 or 500.

**Warnings:**

- No explicit latent-variable metadata or reliably identifiable latent declarations; absence from this list does not prove that no latent variables exist.
