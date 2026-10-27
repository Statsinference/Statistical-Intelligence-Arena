# DGP nri-calonico-2018-asymmetric-sine-v1 (English title required)

> **Unverified extraction — scientific review required.**

**Primary area:** Nonparametric Regression

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Calonico, S., Cattaneo, M. D., and Farrell, M. H. (2018). On the Effect of Bias Estimation on Coverage Accuracy in Nonparametric Inference. Journal of the American Statistical Association, 113(522), 767–779. DOI: 10.1080/01621459.2017.1285776.

**DOI:** — · **Source locator:** Final journal typeset PDF, Section 4 Simulation Results and Figure 1, printed p.776 (PDF p.10); Table 1, printed p.777 (PDF p.11); conditional mean definition in Section 3.1. Version cross-check: arXiv:1508.02973v6 (2018-03-07).

## DGP / generation mechanism

**Sampling design:** Unit: individual; Dependence: IID rows; X and epsilon independent within a row, Y=m(X)+epsilon. Reusing seed across query scenarios intentionally produces the same sample.

**Generator source:** [generator.py](../generators/nri-calonico-2018-asymmetric-sine-v1.py)

**Keywords (source-described):** Nonlinearity

**Observed variables**

X, Y

**Latent variables**

Not explicitly identified (review required)

**Latent-variable identification:** not explicitly specified

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

$$
X \sim Uniform[-1,1]
$$

$$
\varepsilon \sim \mathcal{N}(0,1), X
$$

independent of epsilon in the declared implementation

$$
Y=m(X)+\varepsilon
$$

$$
m(x)=\sin(3\cdot \pi\cdot x/2)/(1+18\cdot x^{2}\cdot (sgn(x)+1))
$$

$$
sgn(0)=0.
$$

$$
Equivalently, m(x)=\sin(3\cdot \pi\cdot x/2) for x<=0
$$

$$
m(x)=\sin(3\cdot \pi\cdot x/2)/(1+36\cdot x^{2}) for x>0.
$$

$$
\theta(x_{0})=\mathbb{E}[Y\mid X=x_{0}]=m(x_{0})
$$

x0 in {-2/3,-1/3,0,1/3,2/3}.

Ordered exact source-query truths: 0,-1,0,1/5,0. These are analytically derived here, not reported estimator results.

<details>
<summary>Original source equations (verbatim)</summary>

<pre>
X ~ Uniform[-1,1], epsilon ~ N(0,1), X independent of epsilon in the declared implementation.
Y=m(X)+epsilon; m(x)=sin(3*pi*x/2)/(1+18*x^2*(sgn(x)+1)); sgn(0)=0.
Equivalently, m(x)=sin(3*pi*x/2) for x&lt;=0; m(x)=sin(3*pi*x/2)/(1+36*x^2) for x&gt;0.
theta(x0)=E[Y|X=x0]=m(x0); x0 in {-2/3,-1/3,0,1/3,2/3}.
Ordered exact source-query truths: 0,-1,0,1/5,0. These are analytically derived here, not reported estimator results.
</pre>

</details>


## Parameter scenarios, estimands and truth

| Scenario | Estimand | Definition | True value | Evidence status |
|---|---|---|---|---|
| source_x_neg_two_thirds | m(x0) | E[Y \| X=x0], the continuous conditional regression mean at the fixed config.query_x; not a prediction quantile, population average, causal contrast or simultaneous band. | -1.2246467991473532e-16 | reported_numeric |
| source_x_neg_one_third | m(x0) | E[Y \| X=x0], the continuous conditional regression mean at the fixed config.query_x; not a prediction quantile, population average, causal contrast or simultaneous band. | -1.0 | reported_numeric |
| source_x_zero | m(x0) | E[Y \| X=x0], the continuous conditional regression mean at the fixed config.query_x; not a prediction quantile, population average, causal contrast or simultaneous band. | 0.0 | reported_numeric |
| source_x_pos_one_third | m(x0) | E[Y \| X=x0], the continuous conditional regression mean at the fixed config.query_x; not a prediction quantile, population average, causal contrast or simultaneous band. | 0.2 | reported_numeric |
| source_x_pos_two_thirds | m(x0) | E[Y \| X=x0], the continuous conditional regression mean at the fixed config.query_x; not a prediction quantile, population average, causal contrast or simultaneous band. | 7.203804700866784e-18 | reported_numeric |

## Identifiability assumptions

- IID individuals (X_i,Y_i) with random design X_i uniform on [-1,1].
- Declared implementation uses epsilon_i independent of X_i and iid N(0,1); hence E[epsilon_i\|X_i]=0.
- Finite conditional moments and positive design density in neighborhoods of the five interior queries.
- The continuous conditional-mean version m(x) defines the point target; the query is prespecified, not selected from outcomes.
- This is a descriptive conditional mean, with no treatment, intervention, ignorability or IV assumptions.
- No claim that every CI method or high-order smoothness theorem applies at every point; m is C2 but not C3 at x=0.

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Warnings:**

- No explicit latent-variable metadata or reliably identifiable latent declarations; absence from this list does not prove that no latent variables exist.
