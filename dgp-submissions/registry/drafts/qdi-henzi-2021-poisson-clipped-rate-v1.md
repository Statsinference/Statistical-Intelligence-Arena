# Conditional CDF at (x=5,y=3) in the Henzi-Ziegel-Gneiting clipped-rate Poisson mechanism

> **Unverified extraction — scientific review required.**

**Primary area:** Quantile Inference

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Henzi, Alexander; Ziegel, Johanna F.; Gneiting, Tilmann (2021). Isotonic Distributional Regression. Journal of the Royal Statistical Society: Series B (Statistical Methodology), 83(5), 963-993. DOI: 10.1111/rssb.12450.

**DOI:** 10.1111/rssb.12450 · **Source locator:** Primary: published Version of Record, JRSS-B 83(5):963-993 (2021), Section 4. Covariate law: PDF p.17 / journal p.979, unnumbered paragraph immediately before equation (23); Poisson law: equation (26), PDF p.19 / journal p.981. Regularity: Section 2.4, Theorem 3, PDF pp.12-13 / journal pp.974-975. Official supplement rssb12450-sup-0001-Supinfo.pdf (dated 19 March 2021), S2 PDF pp.2-5 (proof still called Theorem 2.3), S4 PDF p.7, S5 Table S1 PDF p.8. Historical arXiv v3: equation (26) p.19, Theorem 2.3 pp.13-14, Appendix D pp.41-42, Appendix E Table 3 p.43. Author reference commit c339ffa652ca24111f183ed833aa7bd5fa43acfd, simulation_example.R top-level script lines 42-79; seeds at 55/70, Poisson at 61/79, training jitter at 67-68.

## DGP / generation mechanism

**Sampling design:** Unit: one observed covariate-count pair (X_i,Y_i); Dependence: iid observed pairs across rows; within each pair, Y depends on X only through lambda(X). n counts fully observed pairs, not clusters or repeated measurements. No treatment, mediator, missingness, label indicator, censoring or interference mechanism applies.

**Generator source:** [generator.py](../generators/qdi-henzi-2021-poisson-clipped-rate-v1.py)

**Keywords (source-described):** Nonlinearity

**Observed variables**

X, Y

**Latent variables**

Not explicitly identified (review required)

**Latent-variable identification:** not explicitly specified

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

**Source covariate: published Section 4, PDF p.17 / journal p.979, unnumbered paragraph before (23)**

```math
X_{i}\overset{\mathrm{iid}}{\sim} \mathrm{Uniform}(0,10)
```

**Source conditional intensity: published equation (26), PDF p.19 / journal p.981**

```math
\lambda(x)=\min(\max(x,1),6) = 1 \text{ if } 0<x\leq 1
```

```math
x \text{ if } 1<x<6
```

```math
6 \text{ if } 6\leq x<10
```

**Source count: published equation (26), PDF p.19 / journal p.981; Y4 renamed Y**

```math
Y_{i} \mid  X_{i}=x \sim \mathrm{Poisson}(\lambda(x))
```

independently across i

```math
P(Y_{i}=k\mid X_{i}=x)=\exp(-\lambda(x))\cdot \lambda(x)^{k}/k!, k=0,1,\ldots
```

**Adapted scalar target**

```math
\theta=P(Y\leq 3\mid X=5)=\exp(-5)\cdot (1+5+25/2+125/6)=(118/3)\cdot \exp(-5)
```

**Independent verification identity**

```math
\theta=\int_{5}^{\infty} t^{3}\cdot \exp(-t)/6 \mathrm{dt} (\Gamma/\mathrm{Erlang} \mathrm{survival})
```

<details>
<summary>Original source equations (verbatim)</summary>

<pre>
X_i iid ~ Uniform(0,10)
lambda(x)=min(max(x,1),6) = 1 if 0&lt;x&lt;=1; x if 1&lt;x&lt;6; 6 if 6&lt;=x&lt;10
Y_i | X_i=x ~ Poisson(lambda(x)), independently across i; P(Y_i=k|X_i=x)=exp(-lambda(x))*lambda(x)^k/k!, k=0,1,...
theta=P(Y&lt;=3|X=5)=exp(-5)*(1+5+25/2+125/6)=(118/3)*exp(-5)
theta=Integral_5^infinity t^3*exp(-t)/6 dt (Gamma/Erlang survival)
</pre>

</details>


## Parameter scenarios, estimands and truth

<table>
<thead><tr><th>Scenario</th><th>Estimand</th><th>Definition</th><th>Reported value</th></tr></thead>
<tbody>
<tr>
<td>original_poisson_qdi</td>
<td rowspan="1">Conditional cumulative distribution function</td>
<td rowspan="1">

$`\Pr(Y\le 3\mid X=5)`$

</td>
<td>0.2650259152973617</td>
</tr>
</tbody>
</table>

<details>
<summary>Submitted estimand definitions</summary>

Submitted English definitions appear below; other original-language definitions remain in the linked JSON. Concise formulas above are display interpretations and still require scientific review.

**Scenario(s):** original_poisson_qdi

P(Y&lt;=3 \| X=5) in the source synthetic superpopulation, using its continuous-in-x conditional probability kernel. Inclusive CDF threshold y=3, fixed covariate query x=5, scalar probability in [0,1]. This is conditional, not marginal, and not a quantile or a causal effect.

[Open raw scientific record (JSON)](./qdi-henzi-2021-poisson-clipped-rate-v1.json).

</details>


**Original submitted target notation:** theta = F_{Y\|X=5}(3)


## Identifiability assumptions

- One fully observed pair (X_i,Y_i) per independent identically distributed row; X_i~Uniform(0,10), Y_i\|X_i~Poisson(min(max(X_i,1),6)); no missingness, censoring, selection or cross-row dependence.
- The conditional kernel is the one defined by equation (26). Because P(X=5)=0, point identification from the joint law uses the continuous-in-x version with positive covariate density around 5; a single zero-probability conditioning event alone does not identify an arbitrary conditional version.
- For isotonic interpretation, the usual numerical order of X is used. Nondecreasing clipped intensity implies stochastically increasing conditional laws, hence nonincreasing F_x(y) in x. These properties follow from the DGP and are not causal assumptions.
- Uniform design has positive density 0.1 on (0,10); lambda is continuous and 1-Lipschitz, bounded in [1,6]. Poisson coupling gives sup_y \|F_x(y)-F_xprime(y)\| &lt;= \|x-xprime\|. After X/10 rescaling, these support the density/order/continuity setting of published Section 2.4 Theorem 3 (PDF pp.12-13 / journal pp.974-975; supplement S2 retains the label Theorem 2.3); this submission proves no estimator rate or confidence-band coverage.
- Y is discrete on the nonnegative integers, with finite moments and no Lebesgue density. Positive response-density assumptions for continuous quantiles are inapplicable. No treatment, intervention, exchangeability or mediation condition is imposed.

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Adaptations from the source (submitted, unverified):**

- Keep the published Section 4 equation (26) Uniform(0,10) and Poisson(min(max(x,1),6)) law unchanged; rename source response Y4 to observed column Y.
- Use the requested fixed scalar conditional CDF P(Y&lt;=3 \| X=5). This is a user-selected QDI target, not a numerical result reported by the source, which evaluates distributional predictions by CRPS.
- Implement the unjittered equation (26), without the author training-script perturbations X+=Uniform(-1e-6,1e-6) and Y+=Uniform(-1e-6,1e-6) at lines 67-68. This preserves the requested discrete response. Do not claim exact reproduction of the full author preprocessing pipeline.
- Use local Python random.Random and a Poisson arrival-count sampler instead of R runif/rpois. Equality in law is intended; R/Python draws are not bitwise identical.
- Run only n=128 CPU interface checks and numerical truth checks. Do not reproduce the 500-replicate training/validation experiment, fit predictors, train PFN, or evaluate interval coverage.

**Warnings:**

- No explicit latent-variable metadata or reliably identifiable latent declarations; absence from this list does not prove that no latent variables exist.
