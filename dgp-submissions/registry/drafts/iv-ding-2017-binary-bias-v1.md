# DGP iv-ding-2017-binary-bias-v1 (English title required)

> **Unverified extraction — scientific review required.**

**Primary area:** IV — Instrumental Variables

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Ding, P., VanderWeele, T. J. and Robins, J. M. (2017). Instrumental variables as bias amplifiers with general outcome and confounding. Biometrika 104(2), 291–302. DOI: 10.1093/biomet/asx009.

**DOI:** — · **Source locator:** arXiv:1701.04177v1 (2017-01-16), §5.1 PDF p.8 and Table 1 p.9, Cases 1–3; causal graph Fig.1(b) p.2 and causal framework §2 pp.3–4. PDF page numbers refer to this fixed preprint, not journal pagination.

## DGP / generation mechanism

**Sampling design:** Unit: individual; Dependence: iid across individuals; within-unit dependence through latent U and the declared SCM

**Generator source:** [generator.py](../generators/iv-ding-2017-binary-bias-v1.py)

**Keywords (source-described):** Interactions · Nonlinearity

**Observed variables**

Z, A, Y

**Latent variables**

U

**Latent-variable identification:** candidates from equations need review

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

$$
Z \sim \mathrm{Bernoulli}(0.5)
$$

$$
U \sim \mathrm{Bernoulli}(0.5), V_{A},V_{Y}\overset{\mathrm{iid}}{\sim} \mathrm{Uniform}(0,1)
$$

all four independent.

$$
p[z,u]=P(A=1|Z=z,U=u), r[\text{ a },u]=P(Y=1|A=\text{ a },U=u)
$$

fixed values from source Table 1.

$$
A(z)=1\{V_{A}<p[z,U]\}
$$

$$
A=A(Z)
$$

$$
Y(\text{ a })=1\{V_{Y}<r[\text{ a },U]\}
$$

$$
Y=Y(A).
$$

$$
q=(0.5,0.5), \delta[u]=p[1,u]-p[0,u], \tau[u]=r[1,u]-r[0,u].
$$

$$
\mathrm{LATE}=\sum_{u} q[u]\cdot \delta[u]\cdot \tau[u] / \sum_{u} q[u]\cdot \delta[u].
$$

$$
\mathrm{Source} \text{ population } \mathrm{ATE}=\sum_{u} q[u]\cdot \tau[u]
$$

it is an audit quantity, not the registered IV target.

<details>
<summary>Original source equations (verbatim)</summary>

<pre>
Z ~ Bernoulli(0.5), U ~ Bernoulli(0.5), V_A,V_Y iid Uniform(0,1); all four independent.
p[z,u]=P(A=1|Z=z,U=u), r[a,u]=P(Y=1|A=a,U=u); fixed values from source Table 1.
A(z)=1{V_A&lt;p[z,U]}, A=A(Z); Y(a)=1{V_Y&lt;r[a,U]}, Y=Y(A).
q=(0.5,0.5), delta[u]=p[1,u]-p[0,u], tau[u]=r[1,u]-r[0,u].
LATE=sum_u q[u]*delta[u]*tau[u] / sum_u q[u]*delta[u].
Source population ATE=sum_u q[u]*tau[u]; it is an audit quantity, not the registered IV target.
</pre>

</details>


## Parameter scenarios, estimands and truth

| Scenario | Estimand | Definition | Reported value | Evidence status |
|---|---|---|---|---|
| source_table1_case1 | LATE | E[Y(1)-Y(0) \| A(1)&gt;A(0)], treatment intervention 0 to 1 among instrument compliers. | 0.05545454545454545 | reported_numeric |
| source_table1_case2 | LATE | E[Y(1)-Y(0) \| A(1)&gt;A(0)], treatment intervention 0 to 1 among instrument compliers. | 0.01 | reported_numeric |
| source_table1_case3 | LATE | E[Y(1)-Y(0) \| A(1)&gt;A(0)], treatment intervention 0 to 1 among instrument compliers. | 0.022500000000000003 | reported_numeric |

**Original submitted target notation:** LATE


## Identifiability assumptions

- Consistency and no interference; iid individuals.
- Randomized binary Z independent of U and all exogenous thresholds; 0&lt;P(Z=1)&lt;1.
- Exclusion: Y(a,z)=Y(a), so Z affects Y only through A.
- Treatment monotonicity A(1)&gt;=A(0) under the declared shared-threshold coupling.
- Nonzero first stage P(A(1)&gt;A(0))&gt;0 in each source scenario.
- The chosen SCM has independent treatment/outcome thresholds given U; U is unobserved.
- These IV conditions identify LATE, not the overall ATE without further restrictions.

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Adaptations from the source (submitted, unverified):**

- English description pending; see [original scientific record](./iv-ding-2017-binary-bias-v1.json).
- English description pending; see [original scientific record](./iv-ding-2017-binary-bias-v1.json).
- English description pending; see [original scientific record](./iv-ding-2017-binary-bias-v1.json).
- English description pending; see [original scientific record](./iv-ding-2017-binary-bias-v1.json).
- English description pending; see [original scientific record](./iv-ding-2017-binary-bias-v1.json).
- English description pending; see [original scientific record](./iv-ding-2017-binary-bias-v1.json).

**Warnings:**

- Latent-variable candidates inferred from source equations; confirm their roles and completeness against the original paper or generator.
