# Wang and Tchetgen Tchetgen (2018) binary odds-product algebraic causal completion

> **Unverified extraction — scientific review required.**

**Primary area:** IV — Instrumental Variables

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Wang, L. and Tchetgen Tchetgen, E. J. (2018). Bounded, efficient and multiply robust estimation of average treatment effects using instrumental variables. Journal of the Royal Statistical Society Series B, 80(3), 531-550. DOI: 10.1111/rssb.12262.

**DOI:** — · **Source locator:** PMC author manuscript, PMCID PMC6051728 / NIHMS927773; Section 4.1 Proposition 2 Eqs.(6),(7); Section 5 opening paragraph and seven unnumbered simulation displays, following parameter paragraph and Table 2 caption. Section 3 Theorem 1 for causal conditions. HTML section/eq anchors, not inferred PDF page numbers.

## DGP / generation mechanism

**Sampling design:** Unit: individual; Dependence: iid units. X2,U,V_Z,V_D,V_Y independent; U binary, V_Z,V_D,V_Y independent Uniform(0,1). Z depends on X2; D on X2,Z,U,V_D; potential Y(a) on X2,U,V_Y. Shared V_Y couples Y(0),Y(1). Only Y=Y(D) is observed; U and uniforms hidden.

**Generator source:** [generator.py](../generators/iv-wang-2018-average-wald-v1.py)

**Keywords (source-described):** Interactions · Nonlinearity

**Observed variables**

X2, Z, D, Y, U

**Latent variables**

V_D, V_Y

**Latent-variable identification:** candidates from equations need review

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

**Baseline and latent distribution**

```math
X=(1,X_{2})
```

X2 uniform on (-1,-0.5) union (0.5,1), density 1

```math
U\sim \mathrm{Bernoulli}(0.5)
```

independent of X2 (explicit adaptation)

```math
\mathrm{Individuals} \text{ iid }.
```

**Instrument**

```math
Z\mid X,U \sim \mathrm{Bernoulli}(\mathrm{expit}(0.1-0.5 X_{2})).
```

**Source contrasts and odds products**

```math
\delta(X)=\tanh(0.1+0.5 X_{2}), \mathrm{deltaD}(X)=\tanh(-0.5 X_{2}), OPD(X)=\exp(-0.5+X_{2}), OPY(X)=\exp(-X_{2}). \alpha=(0.1,0.5)
```

```math
\beta=(0,-0.5)
```

```math
\gamma=(0.1,-0.5)
```

```math
\eta=(-0.5,1)
```

```math
\zeta=(0,-1)
```

```math
\kappa=0.1.
```

**Eq6 and Eq7 mapping**

```math
\mathrm{Let} B=q(2-d)+d. F(d,q)=[B-\sqrt{B^{2}+4q(1-d)(1-q)}]/[2(q-1)]=2q(1-d)/[B+\sqrt{B^{2}+4q(1-d)(1-q)}]
```

```math
\mathrm{For} q=1, F(d,1)=(1-d)/2. \mathrm{p0D}=F(\mathrm{deltaD},OPD)
```

```math
\mathrm{p0Y}=F(\mathrm{deltaD}\cdot \delta,OPY).
```

**Treatment**

```math
D\mid Z,X,U \sim \mathrm{Bernoulli}(\mathrm{p0D}(X)+Z \mathrm{deltaD}(X)+0.1(2U-1)).
```

**Source outcome marginal**

Source notation retained without guessing:

<pre>Y|Z,X,U ~ Bernoulli(p0Y(X)+Z deltaD(X)delta(X)+0.1(2U-1)), recovered by the explicit causal completion below. No probability clipping.</pre>

**Algebraic causal completion adaptation**

```math
\mathrm{rD}=\mathrm{p0D}+0.1(2U-1)
```

```math
\mathrm{rY}=\mathrm{p0Y}+0.1(2U-1), t=\delta(X)
```

```math
\text{ independent } V_{Z},V_{D},V_{Y}\sim \mathrm{Uniform}(0,1)
```

independent of X,U. Z=1{V_Z&lt;expit(gamma^T X)}, D(z)=1{V_D&lt;rD+z deltaD}

```math
g_{a}=\mathrm{rY}-t\cdot \mathrm{rD}+\text{ a }\cdot t, Y(\text{ a })=1\{V_{Y}<g_{a}\}
```

```math
\mathrm{Observe} D=D(Z)
```

```math
Y=Y(D)
```

```math
\mathrm{Then} \mathbb{E}[Y|Z,X,U]=g_{0}+P(D=1|Z,X,U)\cdot (g_{1}-g_{0})=\mathrm{rY}+Z \mathrm{deltaD}\cdot t. \mathbb{E}[Y(1)-Y(0)|X,U]=t.
```

**Population target**

```math
\Delta_{W}=\int_{-1}^{-0.5} \tanh(0.1+0.5x) \mathrm{dx} + \int_{0.5}^{1} \tanh(0.1+0.5x) \mathrm{dx}
```

antiderivative 2 log cosh(0.1+0.5x).

<details>
<summary>Original source equations (verbatim)</summary>

<pre>
X=(1,X2); X2 uniform on (-1,-0.5) union (0.5,1), density 1; U~Bernoulli(0.5), independent of X2 (explicit adaptation). Individuals iid.
Z|X,U ~ Bernoulli(expit(0.1-0.5 X2)).
delta(X)=tanh(0.1+0.5 X2), deltaD(X)=tanh(-0.5 X2), OPD(X)=exp(-0.5+X2), OPY(X)=exp(-X2). alpha=(0.1,0.5), beta=(0,-0.5), gamma=(0.1,-0.5), eta=(-0.5,1), zeta=(0,-1), kappa=0.1.
Let B=q(2-d)+d. F(d,q)=[B-sqrt(B^2+4q(1-d)(1-q))]/[2(q-1)]=2q(1-d)/[B+sqrt(B^2+4q(1-d)(1-q))]. For q=1, F(d,1)=(1-d)/2. p0D=F(deltaD,OPD), p0Y=F(deltaD*delta,OPY).
D|Z,X,U ~ Bernoulli(p0D(X)+Z deltaD(X)+0.1(2U-1)).
Y|Z,X,U ~ Bernoulli(p0Y(X)+Z deltaD(X)delta(X)+0.1(2U-1)), recovered by the explicit causal completion below. No probability clipping.
rD=p0D+0.1(2U-1), rY=p0Y+0.1(2U-1), t=delta(X); independent V_Z,V_D,V_Y~Uniform(0,1), independent of X,U. Z=1{V_Z&lt;expit(gamma^T X)}, D(z)=1{V_D&lt;rD+z deltaD}, g_a=rY-t*rD+a*t, Y(a)=1{V_Y&lt;g_a}. Observe D=D(Z), Y=Y(D). Then E[Y|Z,X,U]=g0+P(D=1|Z,X,U)*(g1-g0)=rY+Z deltaD*t. E[Y(1)-Y(0)|X,U]=t.
Delta_W=integral_{-1}^{-0.5} tanh(0.1+0.5x) dx + integral_{0.5}^{1} tanh(0.1+0.5x) dx; antiderivative 2 log cosh(0.1+0.5x).
</pre>

</details>


## Parameter scenarios, estimands and truth

| Scenario | Estimand | Definition | Reported value |
|---|---|---|---|
| source_section5 | ATE | Population causal ATE E[Y(1)-Y(0)] in the explicitly adapted algebraic causal completion = E[tanh(0.1+0.5 X2)] = average conditional Wald ratio. Binary intervention a=1 versus a=0, full iid superpopulation; not a LATE. | 0.08670199394664552 |

**Original submitted target notation:** ATE


## Identifiability assumptions

- iid individuals, X2 uniform on (-1,-0.5) union (0.5,1), U independent Bernoulli(0.5), conditional instrument overlap and nonzero deltaD on both intervals
- Independent potential-response uniform V_Y and treatment uniform V_D, both independent of X,U and instrument innovation; consistency Y=Y(D), iid units and no interference
- The adapted Y(a) depends on a,X,U,V_Y only, establishing exclusion; Z independent of U given X; Y(a) independent of D,Z given X,U by independent innovations
- Conditional mean treatment effect g1-g0=delta(X) does not depend on U (A5.b); treatment mean difference deltaD(X) does not depend on U (A5.a). These are derived for our explicit completion, not asserted source structural equations
- No monotonicity or causal LATE claim; deltaD changes sign between intervals

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Adaptations from the source (submitted, unverified):**

- Algebraic causal completion adaptation: rD=p0D+kappa(2U-1), rY=p0Y+kappa(2U-1), t=delta(X); D(z)=1{V_D&lt;rD+z*deltaD}, Y(a)=1{V_Y&lt;rY-t*rD+a*t}, using independent Uniform(0,1) V_D,V_Y. This constructed coupling recovers source conditional Bernoulli marginals, is not an author-specified coupling, and adds no numeric coefficients.
- Set U independent of X; use independent random innovations across individuals and generation stages. The source gives U marginal Bernoulli(0.5) without an explicit X-U coupling.
- Target the causal ATE of our explicitly constructed completion, which algebraically equals the source average Wald functional. Causal interpretation is for this adaptation, not a claim that the paper specified this potential-outcome construction.
- Rationalize Eqs.(6),(7) for numerical stability, including the continuous q=1 limit; coefficients unchanged.
- Return X2,Z,D,Y only; implicit intercept omitted. Accept arbitrary n and seed instead of the source n=500 and 1000 estimator repetitions. Omit analyst misspecification covariates and estimator comparisons because they do not alter this DGP.

**Warnings:**

- Latent-variable candidates inferred from source equations; confirm their roles and completeness against the original paper or generator.
