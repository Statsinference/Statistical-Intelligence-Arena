# Nie–Wager (2021) Setup A: Friedman baseline with a sinusoidal propensity

> **Unverified extraction — scientific review required.**

**Primary area:** CATE — Conditional Average Treatment Effect

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Nie, X. and Wager, S. (2021). Quasi-oracle estimation of heterogeneous treatment effects. Biometrika 108(2), 299-319. DOI: 10.1093/biomet/asaa076.

**DOI:** — · **Source locator:** Section 6.1 'Baseline methods and simulation setups', arXiv:1712.04912v4 (6 Aug 2020) PDF p.15 (general data-generating law) and PDF p.16 (unnumbered Setup A paragraph, since the setups carry no equation numbers: 'We use the scaled Friedman (1991) function ... e*(Xi) = trim0.1{sin(pi Xi1 Xi2)} and tau*(Xi) = (Xi1 + Xi2)/2').

## DGP / generation mechanism

**Sampling design:** Unit: individual; Dependence: independent and identically distributed

**Generator source:** [generator.py](../generators/cate-nie-2021-setup-a-v1.py)

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
\mathrm{Xj} \sim \mathrm{Uniform}(0,1) \text{ independently }, j = 1..5
```

**Treatment**

```math
e(X) = \mathrm{trim}_{0.1}\{\sin(\pi X_{1} X_{2})\}, \mathrm{trim}_{\eta}(u) = \max\{\eta, \min(u, 1-\eta)\}
```

**Baseline**

```math
b(X) = \sin(\pi X_{1} X_{2}) + 2 (X_{3} - 1/2)^{2} + X_{4} + 0.5 X_{5}
```

**Heterogeneity**

```math
\tau(X) = (X_{1} + X_{2}) / 2
```

**Outcome**

```math
Y = b(X) + A \tau(X) + \sigma\varepsilon, \varepsilon\sim \mathcal{N}(0,1)
```

```math
\sigma= 1
```

<details>
<summary>Original source equations (verbatim)</summary>

<pre>
Xj ~ Uniform(0,1) independently, j = 1..5
e(X) = trim_{0.1}{ sin(pi X1 X2) }, trim_eta(u) = max{eta, min(u, 1-eta)}
b(X) = sin(pi X1 X2) + 2 (X3 - 1/2)^2 + X4 + 0.5 X5
tau(X) = (X1 + X2) / 2
Y = b(X) + A tau(X) + sigma eps, eps ~ Normal(0,1), sigma = 1
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
<td>0.25</td>
</tr>
</tbody>
</table>

**Definition notes**

- All scenarios: Primary query x_0=(0.2,0.3,0.5,0.5,0.5); recovered from the original submission truth.py.

<details>
<summary>Submitted estimand definitions</summary>

Submitted English definitions appear below; other original-language definitions remain in the linked JSON. Concise formulas above are display interpretations and still require scientific review.

**Scenario(s):** original

Conditional average treatment effect at the declared query points; a simple linear surface in the first two coordinates, embedded in a deliberately difficult nuisance structure.

[Open raw scientific record (JSON)](./cate-nie-2021-setup-a-v1.json).

</details>


**Original submitted target notation:** tau(x0) = E[Y(1) - Y(0) \| X = x0]


## Identifiability assumptions

- SUTVA: one version of treatment, no interference
- Unconfoundedness: treatment depends on X only through sin(pi X1 X2), which is also part of the baseline; the design is observational by construction
- Overlap: e(X) is trimmed to [0.1, 0.9], so positivity holds with margin 0.1
- Homoscedastic Gaussian noise; sigma = 1 in this scenario

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Adaptations from the source (submitted, unverified):**

- Dimension fixed at d = 5, the smallest dimension for which the source's baseline is fully defined (it uses X1..X5); the source varies d in {6, 12} for the reported grid.
- The source writes Y = b(X) + (W - 0.5) tau(X) + sigma eps; this package uses Y = b(X) + A tau(X) + sigma eps with A in {0,1}. The CATE is unchanged; the marginal outcome law differs by the constant 0.5 tau(X).
- Noise scale is fixed at sigma = 1 (the source also reports sigma in {0.5, 2, 3}); those are scenarios, not implemented here.
- trim_eta is implemented as np.clip(., 0.1, 0.9), matching trim_0.1 in the source.

**Warnings:**

- Latent-variable candidates inferred from source equations; confirm their roles and completeness against the original paper or generator.
