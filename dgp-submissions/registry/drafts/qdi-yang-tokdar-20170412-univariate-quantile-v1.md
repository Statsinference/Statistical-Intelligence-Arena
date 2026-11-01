# Yang--Tokdar univariate quantile-plane DGP: conditional 0.9 quantile at X=0.5

> **Unverified extraction — scientific review required.**

**Primary area:** Quantile Inference

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Yang, Yun and Tokdar, Surya T. (2017). Joint Estimation of Quantile Planes Over Arbitrary Predictor Spaces. Journal of the American Statistical Association 112(519), 1107-1120. DOI: 10.1080/01621459.2016.1192545. Published online 2017-04-12. Current primary source: published Section 5.1, journal page 1113 (local PDF page 8 including cover).

**DOI:** 10.1080/01621459.2016.1192545 · **Source locator:** Published JASA 2017, Section 5.1 Performance Assessment: Univariate X, PDF page 8 (including publisher cover), journal page 1113, unnumbered model at the start of the section. Historical comparison only: arXiv:1507.03130v1 (2015-07-11), Section 5.2, PDF/printed page 12. Published Section 5.2 is multivariate and excluded. Supplement and estimator-code locators remain separate; the exact selected-experiment script/commit/seed remain unlocated.

## DGP / generation mechanism

**Sampling design:** Unit: one fully observed pair (X,Y) from the synthetic population; Dependence: iid rows; X and Y are dependent within a row. Internal U_i independent of X_i and across units. No latent variable is exported.; Source Experiment: {'datasets': 100, 'observations_per_dataset': 1000}; Collection Check: {'n': 128, 'seed': 1729}

**Generator source:** [generator.py](../generators/qdi-yang-tokdar-20170412-univariate-quantile-v1.py)

**Keywords (source-described):** Linearity

**Observed variables**

X, Y

**Latent variables**

U

**Latent-variable identification:** candidates from equations need review

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

$$
X \sim \mathrm{Uniform}(-1,1)
$$

$$
Q_Y(\tau\mid X=x) = 3\cdot (\tau-1/2)\cdot \log(1/[\tau\cdot (1-\tau)]) + 4\cdot (\tau-1/2)^{2}\cdot \log(1/[\tau\cdot (1-\tau)])\cdot x
$$

$$
0<\tau<1
$$

$$
U \sim \mathrm{Uniform}(0,1)
$$

independent of X

$$
Y=Q_Y(U\mid X)
$$

$$
iid pairs across rows
$$

only X,Y observed/exported

$$
\theta=Q_Y(0.9\mid X=0.5)=(38/25)\cdot \log(100/9)
$$

<details>
<summary>Original source equations (verbatim)</summary>

<pre>
X ~ Uniform(-1,1)
Q_Y(tau|X=x) = 3*(tau-1/2)*log(1/[tau*(1-tau)]) + 4*(tau-1/2)^2*log(1/[tau*(1-tau)])*x; 0&lt;tau&lt;1
U ~ Uniform(0,1), independent of X; Y=Q_Y(U|X); iid pairs across rows; only X,Y observed/exported
theta=Q_Y(0.9|X=0.5)=(38/25)*log(100/9)
</pre>

</details>


## Parameter scenarios, estimands and truth

| Scenario | Estimand | Definition | True value | Evidence status |
|---|---|---|---|---|
| original_law_x05_tau09 | theta = Q_Y(0.9 \| X=0.5) | inf{y: F_Y(y \| X=0.5) &gt;= 0.9} under the source superpopulation; use the conditional distribution version continuous in x specified by the quantile-plane law. A noncausal scalar conditional quantile, not a marginal quantile, beta_1(0.9), prediction interval, or simultaneous band. | 3.6600773251508456 | reported_numeric |

## Identifiability assumptions

- Independent identically distributed rows (X_i,Y_i); stochastic predictor design X_i uniform(-1,1). Published Section 4 PDF p.7/journal1112 specifies independent predictor draws; Section 2.3 PDF p.5/journal1110 gives the likelihood. iid joint realization and independent inverse-transform uniforms are explicit here; published Eq.(2) PDF p.2/journal1107 gives the sampling representation.
- Complete observation of X and Y without selection, censoring, missingness, clusters, panels, interference or additional measurement error in the published Section 5.1 univariate simulation.
- X has positive density 1/2 near the interior query x=0.5. Because a single continuous-X point has probability zero, use the smooth conditional-law version fixed by the model; do not identify an arbitrary point-version without regularity.
- The stated quantile function is differentiable and strictly increasing in tau for every x in [-1,1], tends to minus/plus infinity at the endpoints and yields a continuous positive conditional density at the target; analytic proof in card.
- Only regularity needed to define the scalar truth is asserted. Bayesian-prior conditions of the paper are not additional DGP parameters. No causal intervention, exchangeability or mediation assumptions apply.

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Warnings:**

- Latent-variable candidates inferred from source equations; confirm their roles and completeness against the original paper or generator.
