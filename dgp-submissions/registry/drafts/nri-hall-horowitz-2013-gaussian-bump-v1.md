# Hall--Horowitz Gaussian bump on a linear trend: pointwise regression-mean inference

> **Unverified extraction — scientific review required.**

**Primary area:** Nonparametric Regression

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Hall, P. and Horowitz, J. (2013). A simple bootstrap method for constructing nonparametric confidence bands for functions. The Annals of Statistics, 41(4), 1892-1921. DOI: 10.1214/13-AOS1137.

**DOI:** 10.1214/13-aos1137 · **Source locator:** arXiv:1309.4864v1, IMS electronic reprint (2013-09-19): section 2.1 equation (2.1), PDF p4; section 3.1 g1 and design/noise settings, PDF p13; section 3.2 Tables 1-3, PDF pp16-17, and discussion of x=0,+/-0.15,+/-0.3, PDF p21. Page numbers refer to this reprint, not original journal pagination.

## DGP / generation mechanism

**Sampling design:** Unit: one observation pair (X,Y); Dependence: IID rows; independent X and epsilon within each row in the implementation. Fixed seed across query scenarios intentionally reuses the same sample.

**Generator source:** [generator.py](../generators/nri-hall-horowitz-2013-gaussian-bump-v1.py)

**Keywords (source-described):** Nonlinearity

**Observed variables**

X, Y

**Latent variables**

Not explicitly identified (review required)

**Latent-variable identification:** not explicitly specified

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

**Design**

```math
X_{i} \text{ iid } \mathrm{Uniform}[-1,1].
```

**Errors**

```math
\varepsilon_{i}\overset{\mathrm{iid}}{\sim} \mathcal{N}(0,\sigma^{2}), \sigma\in \{1,0.5,0.2\}
```

independent of X_i in the implementation

**Source g1**

Source notation retained without guessing:

<pre>g1(x)=x+5*phi(10*x)=x+5/sqrt(2*pi)*exp(-50*x^2). phi is the standard normal density, without an extra factor 10.</pre>

**Response**

```math
Y_{i}=g_{1}(X_{i})+\varepsilon_{i}.
```

**Target**

```math
\theta(x_{0})=\mathbb{E}[Y\mid X=x_{0}]=g_{1}(x_{0})
```

x0 in {-0.3,-0.15,0,0.15,0.3}.

<details>
<summary>Original source equations (verbatim)</summary>

<pre>
X_i iid Uniform[-1,1].
epsilon_i iid Normal(0,sigma^2), sigma in {1,0.5,0.2}; independent of X_i in the implementation.
g1(x)=x+5*phi(10*x)=x+5/sqrt(2*pi)*exp(-50*x^2). phi is the standard normal density, without an extra factor 10.
Y_i=g1(X_i)+epsilon_i.
theta(x0)=E[Y|X=x0]=g1(x0); x0 in {-0.3,-0.15,0,0.15,0.3}.
</pre>

</details>


## Parameter scenarios, estimands and truth

<table>
<thead><tr><th>Scenario</th><th>Estimand</th><th>Definition</th><th>Reported value</th></tr></thead>
<tbody>
<tr>
<td>source_sd100_query_neg030</td>
<td rowspan="1">Pointwise conditional mean</td>
<td rowspan="1">

$`\mathbb{E}[Y\mid X=-0.30]`$

</td>
<td>-0.27784075794030993</td>
</tr>
<tr>
<td>source_sd100_query_neg015</td>
<td rowspan="1">Pointwise conditional mean</td>
<td rowspan="1">

$`\mathbb{E}[Y\mid X=-0.15]`$

</td>
<td>0.49758797832945867</td>
</tr>
<tr>
<td>source_sd100_query_zero</td>
<td rowspan="1">Pointwise conditional mean</td>
<td rowspan="1">

$`\mathbb{E}[Y\mid X=0]`$

</td>
<td>1.9947114020071635</td>
</tr>
<tr>
<td>source_sd100_query_pos015</td>
<td rowspan="1">Pointwise conditional mean</td>
<td rowspan="1">

$`\mathbb{E}[Y\mid X=0.15]`$

</td>
<td>0.7975879783294587</td>
</tr>
<tr>
<td>source_sd100_query_pos030</td>
<td rowspan="1">Pointwise conditional mean</td>
<td rowspan="1">

$`\mathbb{E}[Y\mid X=0.30]`$

</td>
<td>0.32215924205969004</td>
</tr>
<tr>
<td>source_sd050_query_neg030</td>
<td rowspan="1">Pointwise conditional mean</td>
<td rowspan="1">

$`\mathbb{E}[Y\mid X=-0.30]`$

</td>
<td>-0.27784075794030993</td>
</tr>
<tr>
<td>source_sd050_query_neg015</td>
<td rowspan="1">Pointwise conditional mean</td>
<td rowspan="1">

$`\mathbb{E}[Y\mid X=-0.15]`$

</td>
<td>0.49758797832945867</td>
</tr>
<tr>
<td>source_sd050_query_zero</td>
<td rowspan="1">Pointwise conditional mean</td>
<td rowspan="1">

$`\mathbb{E}[Y\mid X=0]`$

</td>
<td>1.9947114020071635</td>
</tr>
<tr>
<td>source_sd050_query_pos015</td>
<td rowspan="1">Pointwise conditional mean</td>
<td rowspan="1">

$`\mathbb{E}[Y\mid X=0.15]`$

</td>
<td>0.7975879783294587</td>
</tr>
<tr>
<td>source_sd050_query_pos030</td>
<td rowspan="1">Pointwise conditional mean</td>
<td rowspan="1">

$`\mathbb{E}[Y\mid X=0.30]`$

</td>
<td>0.32215924205969004</td>
</tr>
<tr>
<td>source_sd020_query_neg030</td>
<td rowspan="1">Pointwise conditional mean</td>
<td rowspan="1">

$`\mathbb{E}[Y\mid X=-0.30]`$

</td>
<td>-0.27784075794030993</td>
</tr>
<tr>
<td>source_sd020_query_neg015</td>
<td rowspan="1">Pointwise conditional mean</td>
<td rowspan="1">

$`\mathbb{E}[Y\mid X=-0.15]`$

</td>
<td>0.49758797832945867</td>
</tr>
<tr>
<td>source_sd020_query_zero</td>
<td rowspan="1">Pointwise conditional mean</td>
<td rowspan="1">

$`\mathbb{E}[Y\mid X=0]`$

</td>
<td>1.9947114020071635</td>
</tr>
<tr>
<td>source_sd020_query_pos015</td>
<td rowspan="1">Pointwise conditional mean</td>
<td rowspan="1">

$`\mathbb{E}[Y\mid X=0.15]`$

</td>
<td>0.7975879783294587</td>
</tr>
<tr>
<td>source_sd020_query_pos030</td>
<td rowspan="1">Pointwise conditional mean</td>
<td rowspan="1">

$`\mathbb{E}[Y\mid X=0.30]`$

</td>
<td>0.32215924205969004</td>
</tr>
</tbody>
</table>

**Definition notes**

- All scenarios: Under the scenario-specific data law.

<details>
<summary>Submitted estimand definitions</summary>

Submitted English definitions appear below; other original-language definitions remain in the linked JSON. Concise formulas above are display interpretations and still require scientific review.

**Scenario(s):** source_sd100_query_neg030, source_sd100_query_neg015, source_sd100_query_zero, source_sd100_query_pos015, source_sd100_query_pos030, source_sd050_query_neg030, source_sd050_query_neg015, source_sd050_query_zero, source_sd050_query_pos015, source_sd050_query_pos030, source_sd020_query_neg030, source_sd020_query_neg015, source_sd020_query_zero, source_sd020_query_pos015, source_sd020_query_pos030

Continuous conditional-mean version E[Y\|X=x0]=x0+5*phi(10*x0) for a fixed query x0. Default x0=0; this is not a marginal mean or a future-response prediction target.

[Open raw scientific record (JSON)](./nri-hall-horowitz-2013-gaussian-bump-v1.json).

</details>


**Original submitted target notation:** theta(x0)=g1(x0)


## Identifiability assumptions

- IID observation pairs (X,Y); fully observed covariate and outcome.
- Declared product design: X uniform on [-1,1] independent of centered Gaussian epsilon; E[epsilon\|X]=0 and Var(epsilon\|X)=sigma^2.
- Use the continuous conditional-mean version to define a value at a point under a continuous design. X has density 1/2 on its support.
- The five registered query points lie in the interior and within the source evaluation region [-0.9,0.9].
- No causal exchangeability assumptions are needed. The smooth regression function does not by itself establish CI validity for an arbitrary estimator.

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Adaptations from the source (submitted, unverified):**

- Preserve the section 3.1 g1 equation, Uniform[-1,1] design and all three source error standard deviations; implement independent X and epsilon and IID pairs explicitly, consistent with the source model. The paragraph does not state the joint X-epsilon law separately.
- Represent the source pointwise regression-function target by five scalar queries x=-0.3,-0.15,0,0.15,0.3. These locations are discussed in section 3.2 (electronic reprint p21); this finite query set is a contribution-level selection, not a claimed reconstruction of the full plotting grid.
- Use Python random.Random (MT19937) with n uniform draws followed by n Gaussian draws. The original RNG, seed and exact draw order are not supplied in the inspected text; source simulation bitstreams are not reproduced.
- Use n=128, seed=1729 for the guide check. Keep source n=100,200,400 and 1000 replications in metadata; do not reproduce the original estimator/coverage simulations.
- Collect g1 as one mechanism. Do not repackage g2, already represented by nri-calonico-2018-asymmetric-sine-v1. Record g3 as the source-described truncation/rescaling of g2 and leave that related design uncollected in this one-new-mechanism contribution.

**Warnings:**

- No explicit latent-variable metadata or reliably identifiable latent declarations; absence from this list does not prove that no latent variables exist.
