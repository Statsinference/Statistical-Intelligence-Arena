# IV: sine structural response with Gaussian confounding

> **Unverified extraction — scientific review required.**

**Primary area:** IV — Instrumental Variables

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Dikkala, N., Lewis, G., Mackey, L. and Syrgkanis, V. (2020). Minimax Estimation of Conditional Moment Models. NeurIPS 33:12248-12262.

**DOI:** — · **Source locator:** Supplement Appendix J, printed p.48 (supplement PDF p.33), sine h0 and first-stage equations; Fig.15 printed p.50 for nx=nz=1, alpha=.6. Author mliv/dgps.py lines 53-54 and 154-163; standardize at 89-95.

## DGP / generation mechanism

**Sampling design:** Unit: individual; Dependence: iid individuals; exogenous random draws mutually independent within individual except explicitly shared latent errors

**Generator source:** [generator.py](../generators/iv-dikkala-2020-sine-v1.py)

**Keywords (source-described):** Nonlinearity

**Observed variables**

Z1, P, Y

**Latent variables**

U, delta, zeta

**Latent-variable identification:** candidates from equations need review

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

$$
Z\sim \mathcal{N}(0,\mathrm{SD}=2)
$$

$$
U\sim \mathcal{N}(0,\mathrm{SD}=2)
$$

$$
\delta,\zeta\sim \mathcal{N}(0,\mathrm{SD}=0.1)
$$

mutually independent

$$
P=0.6\cdot Z+0.4\cdot U+\delta
$$

$$
Y=\sin(P)+U+\zeta
$$

<details>
<summary>Original source equations (verbatim)</summary>

<pre>
Z~Normal(0,SD=2), U~Normal(0,SD=2), delta,zeta~Normal(0,SD=0.1), mutually independent
P=0.6*Z+0.4*U+delta
Y=sin(P)+U+zeta
</pre>

</details>


## Parameter scenarios, estimands and truth

| Scenario | Estimand | Definition | True value | Evidence status |
|---|---|---|---|---|
| code_scale_alpha06_raw | theta_IV = h0(0.5)-h0(0) | Structural outcome contrast for interventions P=.5 versus P=0, retaining the marginal centered latent confounder and outcome noise. This is not E[Y\|P=.5]-E[Y\|P=0]. | 0.479425538604203 | reported_numeric |

## Identifiability assumptions

- iid individuals, consistency and no interference.
- Z is independent of U,delta,zeta; Z enters Y only through P (exclusion).
- E[U+zeta\|Z]=0; nonzero instrument_strength gives a relevant Gaussian location first stage.
- Identification uses an appropriate integrable structural-response class and Gaussian convolution injectivity/completeness; zero instrument strength would remove identification.

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Warnings:**

- Latent-variable candidates inferred from source equations; confirm their roles and completeness against the original paper or generator.
