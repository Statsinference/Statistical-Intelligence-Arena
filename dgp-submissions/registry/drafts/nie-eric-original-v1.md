# Natural indirect effect in the Tchetgen Tchetgen–Shpitser mediation design

> **Unverified extraction — scientific review required.**

**Primary area:** Mediation — Direct and Indirect Effects

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Tchetgen Tchetgen, E. J. and Shpitser, I. (2012). Semiparametric theory for causal mediation analysis: efficiency bounds, multiple robustness and sensitivity analysis. The Annals of Statistics 40(3), 1816–1845. DOI: 10.1214/12-AOS990.

**DOI:** — · **Source locator:** Section 3, electronic-reprint PDF page 13: Model.X, Model.E, Model.M, Model.Y. NIE definition: equation (1), PDF page 2.

## DGP / generation mechanism

**Sampling design:** Unit: individual; Dependence: iid

**Generator source:** [generator.py](../generators/nie-eric-original-v1.py)

**Keywords (source-described):** Interactions · Nonlinearity

**Observed variables**

X1, X2, X3, A, M, Y

**Latent variables**

Not explicitly identified (review required)

**Latent-variable identification:** not explicitly specified

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

**Baseline X1**

```math
X_{1} \sim \mathrm{Bernoulli}(0.4)
```

**Baseline X2**

```math
X_{2} \mid  X_{1} \sim \mathrm{Bernoulli}(0.3 + 0.4 X_{1})
```

**Baseline X3**

```math
X_{3} \mid  X_{1},X_{2} \sim \mathcal{N}(-0.024 - 0.4 X_{1} + 0.4 X_{2}, 1)
```

**Treatment**

```math
\mathrm{logit} P(A=1\mid X) = 0.4 + X_{1} - X_{2} + 0.1 X_{3} - 1.5 X_{1} X_{3}
```

**Mediator**

```math
\mathrm{logit} P(M=1\mid A,X) = 0.5 - X_{1} + 0.5 X_{2} - 0.9 X_{3} - 1.5 X_{1} X_{3} + A
```

**Outcome**

```math
Y = 1 + 0.2 X_{1} + 0.3 X_{2} + 1.4 X_{3} - 2.5 A - 3.5 M + 5 A M + \varepsilon
```

```math
\varepsilon\sim \mathcal{N}(0,1)
```

<details>
<summary>Original source equations (verbatim)</summary>

<pre>
X1 ~ Bernoulli(0.4)
X2 | X1 ~ Bernoulli(0.3 + 0.4 X1)
X3 | X1,X2 ~ Normal(-0.024 - 0.4 X1 + 0.4 X2, 1)
logit P(A=1|X) = 0.4 + X1 - X2 + 0.1 X3 - 1.5 X1 X3
logit P(M=1|A,X) = 0.5 - X1 + 0.5 X2 - 0.9 X3 - 1.5 X1 X3 + A
Y = 1 + 0.2 X1 + 0.3 X2 + 1.4 X3 - 2.5 A - 3.5 M + 5 A M + epsilon; epsilon ~ Normal(0,1)
</pre>

</details>


## Parameter scenarios, estimands and truth

<table>
<thead><tr><th>Scenario</th><th>Estimand</th><th>Definition</th><th>Reported value</th></tr></thead>
<tbody>
<tr>
<td>original</td>
<td rowspan="1">NIE</td>
<td rowspan="1">

$`\mathbb{E}\!\left[Y^{(1,M^{(1)})}-Y^{(1,M^{(0)})}\right]`$

</td>
<td>0.2366199012683949</td>
</tr>
</tbody>
</table>

<details>
<summary>Submitted estimand definitions</summary>

Submitted English definitions appear below; other original-language definitions remain in the linked JSON. Concise formulas above are display interpretations and still require scientific review.

**Scenario(s):** original

E[Y(1,M(1)) - Y(1,M(0))] in the superpopulation defined by the fixed DGP.

[Open raw scientific record (JSON)](./nie-eric-original-v1.json).

</details>


**Original submitted target notation:** theta_NIE = theta_11 - theta_10


## Identifiability assumptions

- Consistency and well-defined treatment/mediator interventions
- Independent individuals; no interference
- Treatment exchangeability conditional on X
- Mediator–outcome exchangeability conditional on A,X and the required cross-world condition
- No treatment-induced mediator–outcome confounder in this simple natural-effect design
- Treatment and mediator positivity on the declared support; tail overlap may still be poor in finite samples

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Adaptations from the source (submitted, unverified):**

- Keep the Section 3 observed-data equations and fixed parameters unchanged; rename exposure E to A.
- Evaluate NIE = theta_11 - theta_10, whereas the Section 3 simulation compares natural direct-effect estimators.
- Use small CPU checks instead of reproducing the paper's entire n=600/1000, R=1000 simulation or any PFN experiment.
- Promote the existing student-toolkit example to contributions; generator.py, truth.py, verify.py and config.json are copied unchanged. This is an existing example-family registration, not a newly discovered mechanism.

**Warnings:**

- No explicit latent-variable metadata or reliably identifiable latent declarations; absence from this list does not prove that no latent variables exist.
