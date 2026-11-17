# MAR response with directly generated propensity score, light-tail Model 2

> **Unverified extraction — scientific review required.**

**Primary area:** Missing Data

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Liu, Y. and Fan, Y. (2023). Biased-sample empirical likelihood weighting for missing data problems: an alternative to inverse probability weighting. Journal of the Royal Statistical Society Series B 85(1), 67–83. DOI: 10.1093/jrsssb/qkac006.

**DOI:** 10.1093/jrsssb/qkac006 · **Source locator:** Section 3, Example 1, journal p. 76 (PDF p. 10); choose gamma=2.5, c=1, Model 2; Table 1 on journal p. 77/PDF p. 11.

## DGP / generation mechanism

**Sampling design:** Unit: individual; Dependence: iid

**Generator source:** [generator.py](../generators/mdi-liu-fan-2023-light-tail-model2-v1.py)

**Keywords (source-described):** Not specified

**Observed variables**

P, D, Y_observed

**Latent variables**

eta

**Latent-variable identification:** candidates from equations need review

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

**Propensity score coordinate**

$$
P=\pi(X) \mathrm{generated} \mathrm{directly}: \mathrm{Pr}(P\leq u)=u^{\gamma-1}, u \in [0,1]
$$

$$
\gamma=2.5
$$

equivalently Beta(1.5,1)

**Full outcome**

$$
\eta\sim \chi-\mathrm{square}(4)
$$

independent of P

$$
Y=1-P+c\cdot (\eta-4)/\sqrt{8}
$$

$$
c=1 (\mathrm{Model} 2)
$$

**Observation**

$$
D\mid P\sim \mathrm{Bernoulli}(P)
$$

$$
D=1 \mathrm{means} Y \text{ observed }
$$

**Observed encoding**

$$
Y_{\mathrm{observed}}=Y \text{ when } D=1 \text{ and } 0 \text{ placeholder } \text{ when } D=0
$$

**Target**

$$
\theta=\mathbb{E}(Y)=1/\gamma=0.4
$$

<details>
<summary>Original source equations (verbatim)</summary>

<pre>
P=pi(X) generated directly: Pr(P&lt;=u)=u^(gamma-1), u in [0,1], gamma=2.5; equivalently Beta(1.5,1)
eta~chi-square(4) independent of P; Y=1-P+c*(eta-4)/sqrt(8), c=1 (Model 2)
D|P~Bernoulli(P); D=1 means Y observed
Y_observed=Y when D=1 and 0 placeholder when D=0
theta=E(Y)=1/gamma=0.4
</pre>

</details>


## Parameter scenarios, estimands and truth

| Scenario | Estimand | Definition | Reported value | Evidence status |
|---|---|---|---|---|
| original | Full-data population outcome mean | Full-data superpopulation response mean before outcome masking. | 0.4 | reported_numeric |

**Original submitted target notation:** theta = E(Y)


## Identifiability assumptions

- The fully observed propensity score P=pi(X) is generated directly with CDF u^(gamma-1), 0&lt;=u&lt;=1. No original X is simulated.
- Independent eta~chi-square(df=4); Y=1-P+c(eta-4)/sqrt(8).
- MAR: D\|P~Bernoulli(P), D=1 means Y observed; D conditionally independent of eta and Y given P.
- P&gt;0 almost surely but is not bounded uniformly away from zero.

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Adaptations from the source (submitted, unverified):**

- One generate call returns one sample rather than all paper Monte Carlo repetitions.
- A finite zero placeholder encodes missing Y in the numeric-only interface; mask with the observation indicator.

**Warnings:**

- Latent-variable candidates inferred from source equations; confirm their roles and completeness against the original paper or generator.
