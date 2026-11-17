# Sparse natural indirect effect with ten candidate mediators, scenario LNN (linear propensity, nonlinear mediator confounding, nonlinear outcome confounding)

> **Unverified extraction — scientific review required.**

**Primary area:** Mediation — Direct and Indirect Effects

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Jones, J., Ertefaie, A. and Strawderman, R. L. (2025). Causal mediation analysis: selection with asymptotically valid inference. Journal of the Royal Statistical Society Series B: Statistical Methodology 87(3), 678-700. DOI: 10.1093/jrsssb/qkae109.

**DOI:** 10.1093/jrsssb/qkae109 · **Source locator:** Section 5 'Simulation Studies', arXiv:2110.06127v2 PDF page 15 (the two forms of mu_D0, psi_M and psi_Y, and the three-letter scenario naming; this contribution registers LNN), and Appendix A 'Simulation Results', PDF page 26 (all variances, dimensions and the structural parameters alpha_0, beta_0, gamma_0, and the statement NIE = 2.4). Structural model (1) is on PDF page 4; Proposition 2.1 giving NDE = gamma_0 and NIE = alpha_0 . beta_0 is on PDF page 6.

## DGP / generation mechanism

**Sampling design:** Unit: individual; Dependence: iid individuals; X, then D, then the ten-dimensional mediator vector, then Y are generated in temporal order within an individual

**Generator source:** [generator.py](../generators/mediation-jones-2024-sparse-mediators-lnn-v1.py)

**Keywords (source-described):** Nonlinearity

**Observed variables**

X1, X2, X3, D, M1–M10 (10 variables), Y

<details>
<summary>All observed variable names</summary>

X1, X2, X3, D, M1, M2, M3, M4, M5, M6, M7, M8, M9, M10, Y

</details>

**Latent variables**

Not explicitly identified (review required)

**Latent-variable identification:** explicit structured metadata

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

**Baseline confounders**

```math
X_{l} \sim \mathcal{N}(0, 1/4) \text{ independently }, l = 1, 2, 3
```

**Treatment propensity (scenario LNN)**

```math
\mu_{\mathrm{D0}}(X) = \mathrm{expit}\{0.8 (X_{1} + X_{2})\}
```

**Mediator confounding (scenario LNN)**

```math
\psi_{M}(X) = X_{1}^{2} + X_{2} - X_{3}
```

**Outcome confounding (scenario LNN)**

```math
\psi_{Y}(X) = 2 (X_{1} - 0.5)^{2} + X_{2} + 2 X_{3}
```

**Treatment**

```math
D \mid  X \sim \mathrm{Bernoulli}(\mu_{\mathrm{D0}}(X))
```

**Mediator vector**

```math
M = \alpha_{0} D + \psi_{M}(X) 1_{p} + \eta, \eta_{j} \sim \mathcal{N}(0, 1) \text{ independently }, p = 10, \alpha_{0} = (1, 2, 2, 0, \ldots , 0)
```

**Outcome**

```math
Y = \gamma_{0} D + \beta_{0}' M + \psi_{Y}(X) + \varepsilon, \varepsilon\sim \mathcal{N}(0, 1)
```

```math
\gamma_{0} = 2, \beta_{0} = (0.8, 0.4, 0.4, 0, \ldots , 0)
```

**Source identities (Proposition 2.1)**

```math
\mathrm{NDE} = \gamma_{0} = 2
```

```math
\mathrm{NIE} = \alpha_{0} . \beta_{0} = 2.4
```

<details>
<summary>Original source equations (verbatim)</summary>

<pre>
X_l ~ N(0, 1/4) independently, l = 1, 2, 3
mu_D0(X) = expit{0.8 (X1 + X2)}
psi_M(X) = X1^2 + X2 - X3
psi_Y(X) = 2 (X1 - 0.5)^2 + X2 + 2 X3
D | X ~ Bernoulli(mu_D0(X))
M = alpha_0 D + psi_M(X) 1_p + eta, eta_j ~ N(0, 1) independently, p = 10, alpha_0 = (1, 2, 2, 0, ..., 0)
Y = gamma_0 D + beta_0&#x27; M + psi_Y(X) + epsilon, epsilon ~ N(0, 1), gamma_0 = 2, beta_0 = (0.8, 0.4, 0.4, 0, ..., 0)
NDE = gamma_0 = 2; NIE = alpha_0 . beta_0 = 2.4
</pre>

</details>


## Parameter scenarios, estimands and truth

<table>
<thead><tr><th>Scenario</th><th>Estimand</th><th>Definition</th><th>Reported value</th></tr></thead>
<tbody>
<tr>
<td>LNN</td>
<td rowspan="1">NIE</td>
<td rowspan="1">

$`\mathbb{E}\!\left[Y\{1,M(1)\}-Y\{1,M(0)\}\right]`$

</td>
<td>2.4000000000000004</td>
</tr>
</tbody>
</table>

**Definition notes**

- All scenarios: M is the joint mediator vector; under the stated additive model this equals the coefficient inner product.

<details>
<summary>Submitted estimand definitions</summary>

Submitted English definitions appear below; other original-language definitions remain in the linked JSON. Concise formulas above are display interpretations and still require scientific review.

**Scenario(s):** LNN

Natural indirect effect through the sparse mediator set: NIE = E[Y(1, M(1))] - E[Y(1, M(0))]. Under the source's additive structural model (its equation (1)) and its Proposition 2.1 this equals the inner product alpha_0 . beta_0 of the treatment-to-mediator and mediator-to-outcome coefficient vectors. The companion natural direct effect equals gamma_0. This is NOT a total effect and NOT a single-mediator indirect effect; ten candidate mediators are generated and only the first three are true mediators.

[Open raw scientific record (JSON)](./mediation-jones-2024-sparse-mediators-lnn-v1.json).

</details>


**Original submitted target notation:** NIE = alpha_0 . beta_0


## Identifiability assumptions

- Consistency and well-defined joint interventions on the treatment and the mediator vector
- Independent individuals; no interference
- Treatment exchangeability given X and mediator-outcome exchangeability given (X, D), as encoded by the source's additive model and its Assumptions 2.1 and 2.2
- The source's sparsity assumptions: the first three mediators form the good mediator set S*, and no mediator outside S* is related to any variable in S*
- Mean-zero errors conditional on the preceding variables: E(eta\|X,D) = 0 and E(epsilon\|X,D,M) = 0
- Treatment positivity: the source states it deliberately chose the small covariate variance 1/4 to minimise the chance of inadvertent positivity violations; expit of a bounded linear or product term stays strictly inside (0,1) for every finite X, but no uniform overlap bound is claimed on unbounded Gaussian support
- The source notes that under slightly more general assumptions its estimands also admit an interventional-effect interpretation; the registered definition follows the natural-effect reading the source adopts

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Adaptations from the source (submitted, unverified):**

- Version used: arXiv:2110.06127v2 preprint; the published journal version was not accessible to the collector, so section and page locators refer to the preprint PDF and journal pages 678-700 were not cross-checked.
- Only the source's 'Large' parameter setting is registered. The source's 'Small' setting makes alpha_0 and beta_0 depend on the sample size n (contributions of order n^{-1/2}), which is a drifting local parameter sequence rather than a fixed data-generating mechanism, so it is deliberately not registered.
- SCENARIO SLICING: the source gives a linear and a nonlinear form for each of mu_D0, psi_M and psi_Y and names scenarios by the three-letter triple in that order, mentioning LNN explicitly as an example, which makes eight combinations possible. A change of functional form is a change of mechanism rather than a change of a parameter, so a triple is a contribution rather than a scenario inside one. THREE of the eight are registered, deliberately and not exhaustively, as a reference triple plus its two one-factor neighbours: LNN, the only triple the source names; NNN, which differs from LNN in mu_D0 alone and is the only registered pack carrying the source's X1 * X2 product term; and LNL, which differs from LNN in psi_Y alone. Each registered pair therefore isolates a single nuisance function. The remaining five triples are NOT submitted: they would add relabellings of the same family and inflate the mechanism count without adding a distinct data law. All three share the mechanism_family_id 'jones-2024-robinson-additive-sparse-mediator-selection', so a reviewer who prefers to count the family as a single DGP can collapse them. The source does not state which of the eight combinations it actually ran, and no functional form beyond the two it prints is invented here. This one is LNN.
- The source sets p = 10 candidate mediators in the main text and reports a p = 60 setting in its Appendix B. Only p = 10 is registered: the p = 60 variant shares the functional forms of the p = 10 LNN pack and differs only in that dimension, so registering it as a separate mechanism would be a parameter sweep rather than a new data law. It is kept out of the submission for that reason.
- The source also uses cross-fitting with K = 10 folds, a perturbation bootstrap with exponential weights, and five competing estimators. All of that is estimation machinery applied to the same data; none of it is reproduced and none is registered as a separate mechanism.
- Sampling is re-implemented with NumPy Generator(PCG64); no attempt is made to match the source software draw-for-draw.
- Citation verified against Crossref for DOI 10.1093/jrsssb/qkae109: the authors are Jeremiah Jones, Ashkan Ertefaie and Robert L. Strawderman (an earlier draft of this contribution wrote the first author's initial as M., which was wrong), published online 2024-11-28 and in print in volume 87(3), pages 678-700, dated 2025-07-14. The print year 2025 is the one cited, matching volume 87(3). The contribution_id slug still carries '2024' from the online-first date and is deliberately left unchanged so earlier identifiers stay stable.

**Warnings:**

- Nothing automatically flagged; this does NOT equal scientific acceptance.
