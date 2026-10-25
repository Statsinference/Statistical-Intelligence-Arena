# IV: DeepIV raw-unit demand with endogenous continuous price

> **Unverified extraction — scientific review required.**

**Primary area:** IV — Instrumental Variables

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Hartford, J., Lewis, G., Leyton-Brown, K. and Taddy, M. (2017). Deep IV: A Flexible Approach for Counterfactual Prediction. ICML, PMLR 70:1414-1423.

**DOI:** — · **Source locator:** Published PDF p. 6, Section 4.1, simulation equations; experiments/data_generator.py lines 80-140 for psi, uniform customer type, rho=0.8 and code normalization.

## DGP / generation mechanism

**Sampling design:** Unit: individual; Dependence: iid individuals; exogenous random draws mutually independent within individual except explicitly shared latent errors

**Generator source:** [generator.py](../generators/iv-hartford-2017-demand-v1.py)

**Observed variables**

T, S, Z, P, Y

**Latent variables**

V, W

**Latent-variable identification:** candidates from equations need review

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

$$
T\sim \mathrm{Uniform}(0,10)
$$

$$
S\sim DiscreteUniform(\{1,\ldots ,7\})
$$

$$
Z,V,W\overset{\mathrm{iid}}{\sim} \mathcal{N}(0,1), mutually independent
$$

$$
psi(T)=2\cdot ((T-5)^{4}/600+\exp(-4\cdot (T-5)^{2})+T/10-2)
$$

$$
P=25+(Z+3)\cdot psi(T)+V
$$

$$
e=\rho\cdot V+sqrt(1-\rho^{2})\cdot W
$$

$$
\rho=0.8
$$

$$
Y=100+(10+P)\cdot S\cdot psi(T)-2\cdot P+e
$$

<details>
<summary>Original source equations (verbatim)</summary>

<pre>
T~Uniform(0,10); S~DiscreteUniform({1,...,7}); Z,V,W iid Normal(0,1), mutually independent
psi(T)=2*((T-5)^4/600+exp(-4*(T-5)^2)+T/10-2)
P=25+(Z+3)*psi(T)+V
e=rho*V+sqrt(1-rho^2)*W; rho=0.8
Y=100+(10+P)*S*psi(T)-2*P+e
</pre>

</details>


## Parameter scenarios, estimands and truth

| Scenario | Estimand | Definition | True value | Evidence status |
|---|---|---|---|---|
| paper_raw_rho08 | theta_IV = E[Y(do(P=21))-Y(do(P=20))] | Population structural mean contrast of a one-unit price intervention, averaging independent T~Uniform(0,10) and S~DiscreteUniform(1,...,7); nuisance latent errors retain their marginal distribution. | -11.624351792971128 | reported_numeric |

## Identifiability assumptions

- Consistency and no interference; iid individuals.
- Instrument Z is independent of T,S,V,W; exclusion: Z enters Y only through price P.
- E[e\|T,S,Z]=0 because e=rho*V+sqrt(1-rho^2)*W with independent centered normals.
- Relevance holds for almost every T: d E[P\|T,Z]/dZ=psi(T), whose zeros have probability zero under continuous T.
- Identification uses the additive structural-error conditional-moment model, nonzero Gaussian location shifts almost everywhere, and an appropriate regularity/completeness class; arbitrary IV problems are not automatically identified.

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Warnings:**

- Latent-variable candidates inferred from source equations; confirm their roles and completeness against the original paper or generator.
