# Multiple confounders subject to MNAR: Section 5.3 equation-based candidate

> **Unverified extraction — scientific review required.**

**Primary area:** ATE — Average Treatment Effect

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Yang, S., Wang, L. and Ding, P. (2019). Causal inference with confounders missing not at random. Biometrika, 106(4), 875-888.

**DOI:** 10.1093/biomet/asz048 · **Source locator:** Section 5.3, Multiple confounders subject to missingness, printed pp. 885-886; author PDF pp. 10-11 of 27 (viewer pages 11-12 if one-indexed); DGP equations are unnumbered prose. See also Section 2.1 Assumptions 1-2 and Section 2.3 Assumptions 6-7.

## DGP / generation mechanism

**Sampling design:** Unit: individual; Dependence: Individuals are iid under the implementation. Within an individual, X5 is a sum of X1-X4 and epsilon5; X6 depends on X5; treatment depends on all six covariates; the missingness pattern depends on A and all six covariates. Potential outcomes share the same X vector, while only Y(A) is released as observed Y.

**Generator source:** [generator.py](../generators/ate-yang-wang-ding-2019-mnar-confounder-v2.py)

**Keywords (source-described):** Nonlinearity

**Observed variables**

X1–X6 (6 variables), A, Y, R5, R6

<details>
<summary>All observed variable names</summary>

X1, X2, X3, X4, X5, X6, A, Y, R5, R6

</details>

**Latent variables**

Not explicitly identified (review required)

**Latent-variable identification:** not explicitly specified

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

**X1-X2**

```math
X_{1}, X_{2} \text{ independently } \mathrm{sampled} \mathcal{N}(\text{ mean }=1, \text{ variance }=1)
```

independence is an explicit implementation adaptation because joint independence is not stated in Section 5.3.

**X3-X4**

```math
\mathrm{Xj}=(\mathrm{Bj}-0.5)/0.5 \text{ where } \mathrm{Bj} \text{ independently } \mathrm{follows} \mathrm{Bernoulli}(0.5), j=3,4
```

hence Xj is -1 or +1 with equal probability.

**X5**

```math
X_{5}=X_{1}+X_{2}+X_{3}+X_{4}+\varepsilon_{5}
```

```math
\varepsilon_{5}\sim \mathcal{N}(0,1), \text{ independently } \mathrm{generated}.
```

**X6**

```math
X_{6}\mid X_{5}\sim \mathrm{Bernoulli}(p_{6}), \mathrm{logit}(p_{6})=-X_{5}.
```

**Potential outcomes**

```math
Y(0)=(1,X^{T}) \beta_{0}+\varepsilon_{0}
```

```math
Y(1)=(1,X^{T}) \beta_{1}+\varepsilon_{1}
```

```math
\beta_{0}=(-1.5,1,-1,1,-1,1,1)^{T}
```

```math
\beta_{1}=(0,-1,1,-1,1,-1,-1)^{T}
```

```math
\varepsilon_{0},\varepsilon_{1}\sim \mathcal{N}(0,1).
```

**Treatment**

```math
A\mid X\sim \mathrm{Bernoulli}(\mathrm{expit}((1,X^{T}) \alpha))
```

```math
\alpha=0.5\cdot (2,1,1,1,1,-2,-2)^{T}.
```

**Missing pattern**

```math
R=(R_{5},R_{6}) \in \{(11),(10),(01),(00)\}
```

```math
\mathrm{Let} q=(1,A,X^{T}) \eta, \eta=0.25\cdot (-4,1,1,1,1,1,-1,-1)^{T}
```

Source notation retained without guessing:

<pre>Interpreting the printed RHS as direct probabilities: p11=1/(1+3 exp(q))</pre>

```math
\mathrm{pkl}=1/(\exp(-q)+3) \text{ for } \mathrm{kl}=10,01,00
```

The source prints &#x27;logit(p...)&#x27; before these right-hand sides

this interpretation is necessary for a multinomial probability vector and requires scientific confirmation.

**Observed outcome**

```math
Y=A\cdot Y(1)+(1-A)\cdot Y(0).
```

**Equation-implied ATE**

```math
\mathrm{ATE}=\mathbb{E}[Y(1)-Y(0)]=1.5-2\mathbb{E}[X_{1}]+2\mathbb{E}[X_{2}]-2\mathbb{E}[X_{3}]+2\mathbb{E}[X_{4}]-2\mathbb{E}[X_{5}]-2\mathbb{E}[X_{6}] = -2.5-2\mathbb{E}[X_{6}] \mathrm{under} \text{ the } \mathrm{declared} \mathrm{factorization}
```

Source notation retained without guessing:

<pre>E[X6]≈0.2417754075740287, giving ATE≈-2.983550815148057, which conflicts with the paper&#x27;s reported tau=-0.5.</pre>

<details>
<summary>Original source equations (verbatim)</summary>

<pre>
X1, X2 independently sampled Normal(mean=1, variance=1); independence is an explicit implementation adaptation because joint independence is not stated in Section 5.3.
Xj=(Bj-0.5)/0.5 where Bj independently follows Bernoulli(0.5), j=3,4; hence Xj is -1 or +1 with equal probability.
X5=X1+X2+X3+X4+epsilon5; epsilon5~Normal(0,1), independently generated.
X6|X5~Bernoulli(p6), logit(p6)=-X5.
Y(0)=(1,X^T) beta0+epsilon0; Y(1)=(1,X^T) beta1+epsilon1; beta0=(-1.5,1,-1,1,-1,1,1)^T; beta1=(0,-1,1,-1,1,-1,-1)^T; epsilon0,epsilon1~Normal(0,1).
A|X~Bernoulli(expit((1,X^T) alpha)); alpha=0.5*(2,1,1,1,1,-2,-2)^T.
R=(R5,R6) in {(11),(10),(01),(00)}. Let q=(1,A,X^T) eta, eta=0.25*(-4,1,1,1,1,1,-1,-1)^T. Interpreting the printed RHS as direct probabilities: p11=1/(1+3 exp(q)); pkl=1/(exp(-q)+3) for kl=10,01,00. The source prints &#x27;logit(p...)&#x27; before these right-hand sides; this interpretation is necessary for a multinomial probability vector and requires scientific confirmation.
Y=A*Y(1)+(1-A)*Y(0).
ATE=E[Y(1)-Y(0)]=1.5-2E[X1]+2E[X2]-2E[X3]+2E[X4]-2E[X5]-2E[X6] = -2.5-2E[X6] under the declared factorization; E[X6]≈0.2417754075740287, giving ATE≈-2.983550815148057, which conflicts with the paper&#x27;s reported tau=-0.5.
</pre>

</details>


## Parameter scenarios, estimands and truth

| Scenario | Estimand | Definition | Reported value |
|---|---|---|---|
| section53_equation_based_candidate | ATE | Population E[Y(1)-Y(0)] for the intervention A=1 versus A=0, under the declared Section 5.3 equation-based mechanism and its explicitly stated factorization adaptations. | -2.9835508151480576 |

**Original submitted target notation:** ATE


## Identifiability assumptions

- Consistency: observed Y= A Y(1) + (1-A)Y(0).
- The implementation draws potential-outcome errors independently of treatment conditional on X; this cross-independence is an implementation assumption because Section 5.3 only states the marginal error laws.
- Outcome-independent missingness R independent of Y conditional on (A,X), satisfied by construction because the missing-pattern probabilities depend only on A and X.
- Positivity with uniform lower and upper bounds is not established on the full unbounded covariate support under the printed logistic treatment model; this is a scientific limitation, not a machine-check result.
- The source-reported tau=-0.5 conflicts with the coefficient equations under this declared implementation. The package's oracle is the equation-implied ATE for the runnable adapted mechanism and must not be mistaken for confirmation of the paper's reported value.

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Adaptations from the source (submitted, unverified):**

- The paper's stated tau=-0.5 is inconsistent with the supplied beta vectors and covariate-generating equations under the explicit independent factorization used here. This implementation retains the printed equations and computes their implied ATE; it does not force the reported -0.5 value.
- Section 5.3 displays the missing-pattern right-hand sides after 'logit(p_..)' although those four right-hand-side quantities sum to one only when interpreted as probabilities themselves, not logits. This runnable candidate uses them as direct multinomial probabilities; author/maintainer confirmation is required.
- The prose gives marginal distributions for X1 and X2 and does not explicitly state all within-person cross-independences. For a runnable joint distribution, this implementation generates X1 and X2 independently; it also independently generates X3, X4, epsilon5 and potential-outcome errors. These factorization choices are adaptations pending confirmation.
- Missing X5 and X6 values are represented in finite numeric output by sentinel 0.0 plus explicit R5/R6 observation indicators, because the collection runner validates finite numeric tables. The indicator distinguishes a masked value from a true zero; this is an interface adaptation, not imputation.

**Warnings:**

- No explicit latent-variable metadata or reliably identifiable latent declarations; absence from this list does not prove that no latent variables exist.
