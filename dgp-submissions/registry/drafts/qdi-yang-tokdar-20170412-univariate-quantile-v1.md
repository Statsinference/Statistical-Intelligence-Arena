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

**Keywords (source-described):** Not specified

**Observed variables**

X, Y

**Latent variables**

U

**Latent-variable identification:** candidates from equations need review

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

**Published Section 5.1 predictor, PDF p.8 / JASA p.1113, unnumbered**

$$
X \sim \mathrm{Uniform}(-1,1)
$$

**Published Section 5.1 conditional quantile, PDF p.8 / JASA p.1113, unnumbered**

$$
Q_{Y}(\tau\mid X=x) = 3\cdot (\tau-1/2)\cdot \log(1/[\tau\cdot (1-\tau)]) + 4\cdot (\tau-1/2)^{2}\cdot \log(1/[\tau\cdot (1-\tau)])\cdot x
$$

$$
0<\tau<1
$$

**Derived sampling representation, not an added noise law**

$$
U \sim \mathrm{Uniform}(0,1)
$$

independent of X

$$
Y=Q_{Y}(U\mid X)
$$

$$
\text{ iid } \mathrm{pairs} \text{ across } \text{ rows }
$$

only X,Y observed/exported

**Collection target adaptation**

$$
\theta=Q_{Y}(0.9\mid X=0.5)=(38/25)\cdot \log(100/9)
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

| Scenario | Estimand | Definition | Reported value | Evidence status |
|---|---|---|---|---|
| original_law_x05_tau09 | Conditional quantile | inf{y: F_Y(y \| X=0.5) &gt;= 0.9} under the source superpopulation; use the conditional distribution version continuous in x specified by the quantile-plane law. A noncausal scalar conditional quantile, not a marginal quantile, beta_1(0.9), prediction interval, or simultaneous band. | 3.6600773251508456 | reported_numeric |

**Original submitted target notation:** theta = Q_Y(0.9 \| X=0.5)


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

**Adaptations from the source (submitted, unverified):**

- Retain the complete published Section 5.1 quantile law, X~Uniform(-1,1), coefficients 3 and 4, center 1/2 and powers. Choose query_x=0.5 and quantile_level=0.9 for the scalar Arena target; this query and numeric result are collection adaptations, not a single-point result designated or reported by the paper.
- Implement this conditional law by Y=Q(U\|X), U uniform(0,1) independent of X, using local Python Random(seed) and iid rows. This is an independent law-equivalent implementation, not author-code or original-dataset replay; the published Section 5.1 experiment script, commit and author RNG/seed have not been located.
- Output observed X,Y only. Finite-precision random() draws reject u=0 and use stable logarithms; no arbitrary tail clipping, extra noise or changed coefficient. Local seed and finite PRNG support are implementation choices.
- Check n=128, seed=1729 rather than rerun the paper experiments (100 datasets of n=1000), estimators, MCMC, bootstrap or coverage. Analytic special cases are diagnostics within one declared scenario, not new mechanisms.
- Retain source-only audit evidence dated 2026-10-31 for the supplement, published main text, pinned GitHub estimator snapshot and observed CRAN documentation. Do not import estimator preprocessing, example noise, censoring or base distributions into the DGP.
- Documentation-only revision 2026-11-01 makes the already-read published version the current primary source. The preprint is historical comparison only. No change to the generation law, query, six implementation/config/schema/dependency files, numerical tolerances, scenario count or stable identifiers. Historical v1 comments in unchanged implementation/config files do not override the published primary reference in this manifest and card.
- 2026-11-01 source-gap audit: obtain/review raw CRAN2.1-0 artifacts by read-only reuse of parallel official-source downloads, verify all35 members against fixed mirror commit, reread author websites, historical metadata and75 text files; update only provenance/missing evidence. Preserve formal primary source, complete law, scalar adaptation, six implementation files and tolerances; original experiment script/seed/RNG remain unlocated within the bounded search.

**Warnings:**

- Latent-variable candidates inferred from source equations; confirm their roles and completeness against the original paper or generator.
