# Nie–Wager (2021) Setup D: unrelated treatment and control surfaces

> **Unverified extraction — scientific review required.**

**Primary area:** CATE — Conditional Average Treatment Effect

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Nie, X. and Wager, S. (2021). Quasi-oracle estimation of heterogeneous treatment effects. Biometrika 108(2), 299-319. DOI: 10.1093/biomet/asaa076.

**DOI:** — · **Source locator:** Section 6.1, arXiv:1712.04912v4 (6 Aug 2020) PDF p.16, unnumbered Setup D paragraph (no equation number in the source): 'e*(Xi) = 1/(1 + e^{-Xi1} + e^{-Xi2}), tau*(Xi) = max{Xi1+Xi2+Xi3, 0} - max{Xi4+Xi5, 0}, and b*(Xi) = (max{Xi1+Xi2+Xi3,0} + max{Xi4+Xi5,0})/2'. The same paragraph continues: 'Here, mu*(0)(X) and mu*(1)(X) are uncorrelated, and so there is no upside to learning them jointly.'

## DGP / generation mechanism

**Sampling design:** Unit: individual; Dependence: independent and identically distributed

**Generator source:** [generator.py](../generators/cate-nie-2021-setup-d-v1.py)

**Keywords (source-described):** Interactions · Nonlinearity

**Observed variables**

X1–X5 (5 variables), A, Y

<details>
<summary>All observed variable names</summary>

X1, X2, X3, X4, X5, A, Y

</details>

**Latent variables**

Xj

**Latent-variable identification:** candidates from equations need review

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

**X1-X5**

```math
\mathrm{Xj} \sim \mathcal{N}(0,1) \text{ independently }, j = 1..5
```

**Treatment**

```math
e(X) = 1 / (1 + \exp(-X_{1}) + \exp(-X_{2}))
```

**Baseline**

```math
b(X) = (\max\{X_{1}+X_{2}+X_{3}, 0\} + \max\{X_{4}+X_{5}, 0\}) / 2
```

**Heterogeneity**

```math
\tau(X) = \max\{X_{1}+X_{2}+X_{3}, 0\} - \max\{X_{4}+X_{5}, 0\}
```

**Outcome**

```math
Y = b(X) + (A - 1/2) \tau(X) + \sigma\varepsilon, \varepsilon\sim \mathcal{N}(0,1)
```

```math
\sigma= 1
```

**Arm surfaces**

```math
\mu_{0}(X) = b(X) - \tau(X)/2 = \max\{X_{4}+X_{5}, 0\}
```

```math
\mu_{1}(X) = b(X) + \tau(X)/2 = \max\{X_{1}+X_{2}+X_{3}, 0\}
```

<details>
<summary>Original source equations (verbatim)</summary>

<pre>
Xj ~ Normal(0,1) independently, j = 1..5
e(X) = 1 / (1 + exp(-X1) + exp(-X2))
b(X) = (max{X1+X2+X3, 0} + max{X4+X5, 0}) / 2
tau(X) = max{X1+X2+X3, 0} - max{X4+X5, 0}
Y = b(X) + (A - 1/2) tau(X) + sigma eps, eps ~ Normal(0,1), sigma = 1
mu0(X) = b(X) - tau(X)/2 = max{X4+X5, 0};  mu1(X) = b(X) + tau(X)/2 = max{X1+X2+X3, 0}
</pre>

</details>


## Parameter scenarios, estimands and truth

<table>
<thead><tr><th>Scenario</th><th>Estimand</th><th>Definition</th><th>Reported value</th></tr></thead>
<tbody>
<tr>
<td>original</td>
<td rowspan="1">CATE</td>
<td rowspan="1">

$`\mathbb{E}[Y^{(1)}-Y^{(0)}\mid X=x_0]`$

</td>
<td>1.5</td>
</tr>
</tbody>
</table>

**Definition notes**

- All scenarios: Primary query x_0=(0.5,0.5,0.5,0,0); recovered from the original submission truth.py.

<details>
<summary>Submitted estimand definitions</summary>

Submitted English definitions appear below; other original-language definitions remain in the linked JSON. Concise formulas above are display interpretations and still require scientific review.

**Scenario(s):** original

Conditional average treatment effect at the declared query points; a difference of two rectified sums supported on disjoint coordinate blocks.

[Open raw scientific record (JSON)](./cate-nie-2021-setup-d-v1.json).

</details>


**Original submitted target notation:** tau(x0) = E[Y(1) - Y(0) \| X = x0]


## Identifiability assumptions

- SUTVA: one version of treatment, no interference
- Unconfoundedness: treatment depends on X1, X2 through a sum of exponentials; the baseline uses all five coordinates, so confounding is strong
- Overlap: e(x) in (0, 1/3] because the denominator is at least 1 + 2 exp(min(-x1,-x2)) &gt; 1; the design leans towards control
- Homoscedastic Gaussian noise with sigma = 1

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Adaptations from the source (submitted, unverified):**

- Dimension fixed at d = 5, the smallest dimension for which Setup D is defined; the source varies d in {6, 12}.
- The source writes Y = b(X) + (W - 0.5) tau(X) + sigma eps with W in {0,1}; this package keeps that centred form exactly and writes it as Y = b(X) + (A - 1/2) tau(X) + sigma eps with A in {0,1}. The CATE is unchanged by the rewrite.
- Keeping the centring is essential for this design and is therefore not treated as a cosmetic choice: it is what makes the two arm surfaces disjoint. With it, mu0(X) = b - tau/2 = max{X4+X5,0} and mu1(X) = b + tau/2 = max{X1+X2+X3,0}, so each arm depends on its own coordinate block only. A plain Y = b(X) + A tau(X) would leave both arms carrying b(X) and would destroy the unrelated-arms property that Setup D exists to test.
- sigma fixed at 1.

**Warnings:**

- Latent-variable candidates inferred from source equations; confirm their roles and completeness against the original paper or generator.
