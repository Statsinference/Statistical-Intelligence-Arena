# Full conditional mean in the two-level varying-coefficient cluster model

> **Unverified extraction — scientific review required.**

**Primary area:** Nonparametric Regression

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Zhang, W., Fan, J. and Sun, Y. (2009). A semiparametric model for cluster data. The Annals of Statistics 37(5A), 2377-2408. DOI: 10.1214/08-AOS662.

**DOI:** — · **Source locator:** Formula bodies: (1.4) on PDF p.4. Section starts: Section 5 on PDF p.13. Unnumbered paragraph on PDF p.13: "In model (1.4), we take" (dimensions, cluster sizes, all distributions and coefficient functions). All PDF pages are 1-based pages of the fixed reading file 0908.3382v1. No printed journal page is inferred by adding an offset.

## DGP / generation mechanism

**Sampling design:** Unit: A numeric row for one individual, retaining its cluster identifier. The interface fixes n individuals rather than the source m=100 clusters. The terminal cluster absorbs the row budget; all clusters have at least 6 rows when n&gt;=6, while n&lt;6 produces one smaller budget cluster.; Dependence: Shared Z_i and random effect e_i induce within-cluster dependence. Independent per-cluster Z/e draws; fixed total n couples cluster sizes and determines the terminal budget cluster. Preserve cluster identifiers in analysis.

**Generator source:** [generator.py](../generators/nri-zhangfansun-2009-clustervc-v1.py)

**Keywords (source-described):** Interactions · Nonlinearity

**Observed variables**

cluster, U, X1, X2, X3, Z1, Z2, Y

**Latent variables**

e_i

**Latent-variable identification:** candidates from equations need review

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

**1. Cluster size and row budget**

Source notation retained without guessing:

<pre>For each cluster draw xi_i~N(0,1) and source candidate size floor(2*abs(xi_i)+6)</pre>

apply the declared fixed-n terminal-budget rule

$$
\mathrm{Source} \mathrm{base}=6, \text{ scale }=2
$$

Source notation retained without guessing:

<pre>when remaining&lt;12, the terminal cluster takes the remaining rows</pre>

Other oversized draws also absorb the remaining budget.

**2. Cluster covariates**

$$
Z_{i}\sim \mathcal{N}(0,I_{2}), \mathrm{one} \mathrm{two}-\text{ vector } \mathrm{shared} \text{ by } \text{ all } \text{ rows } \text{ of } \mathrm{cluster} i
$$

Source notation retained without guessing:

<pre>Mean zero, each sd=1, independent components and independent cluster draws.</pre>

**3. Random coefficients**

$$
e_{i}\sim \mathcal{N}(0,0.25\cdot I_{3}), \mathrm{shared} \mathrm{within} \mathrm{cluster} \text{ and }
$$

independent of Z_i

$$
\mathrm{Each} \mathrm{random}-\mathrm{effect} \mathrm{sd}=0.5
$$

not observed/exported.

**4. Individual index**

$$
U_{ij}\sim \mathrm{Uniform}(0,1), \mathrm{newly} \text{ drawn } \text{ for } \text{ each } \mathrm{individual}
$$

Independent of cluster variables and other individual draws

**5. Individual covariates**

$$
X_{ij}\sim \mathcal{N}(0,I_{3}), \mathrm{newly} \text{ drawn } \text{ for } \text{ each } \mathrm{individual}
$$

$$
\mathrm{Each} \mathrm{sd}=1
$$

independent coordinates and

independent of U,Z,e

**6. Coefficient functions**

$$
\beta_{0}(u)=\sin(2\cdot \pi\cdot u)
$$

$$
\beta(u)=\mathrm{ones}(2)\cdot \sin(2\cdot \pi\cdot u)
$$

$$
\alpha_{0}(u)=\mathrm{ones}(3)\cdot \sin(2\cdot \pi\cdot u)
$$

$$
\alpha_{1}(u)=\mathrm{ones}(3)\cdot \cos(2\cdot \pi\cdot u)
$$

$$
\alpha_{2}(u)=\mathrm{ones}(3)\cdot \sin(\pi\cdot u)
$$

$$
\text{ a }_{i}(u)=\alpha_{0}(u)+\alpha_{1}(u)\cdot Z_{i1}+\alpha_{2}(u)\cdot Z_{i2}+e_{i}
$$

Deterministic functions of current u and shared Z/e

Follow the source simulation paragraph including beta0.

**7. Measurement error**

$$
\varepsilon_{ij}\sim \mathcal{N}(0,0.5^{2})
$$

independent of all previous variables and errors

$$
\mathrm{Measurement}-\mathrm{error} \mathrm{sd}=0.5.
$$

**8. Outcome and observed columns**

$$
Y_{ij}=\beta_{0}(U_{ij})+X_{ij}^{T}\cdot \text{ a }_{i}(U_{ij})+Z_{i}^{T}\cdot \beta(U_{ij})+\varepsilon_{ij}
$$

return cluster,U,X1,X2,X3,Z1,Z2,Y

Independent cluster-level Z/e draws induce shared within-cluster effects

sizes are coupled by the n-row budget.

<details>
<summary>Original source equations (verbatim)</summary>

<pre>
For each cluster draw xi_i~N(0,1) and source candidate size floor(2*abs(xi_i)+6); apply the declared fixed-n terminal-budget rule. Source base=6, scale=2; when remaining&lt;12, the terminal cluster takes the remaining rows. Other oversized draws also absorb the remaining budget.
Z_i~N(0,I_2), one two-vector shared by all rows of cluster i. Mean zero, each sd=1, independent components and independent cluster draws.
e_i~N(0,0.25*I_3), shared within cluster and independent of Z_i. Each random-effect sd=0.5; not observed/exported.
U_ij~Uniform(0,1), newly drawn for each individual. Independent of cluster variables and other individual draws.
X_ij~N(0,I_3), newly drawn for each individual. Each sd=1; independent coordinates and independent of U,Z,e.
beta0(u)=sin(2*pi*u); beta(u)=ones(2)*sin(2*pi*u); alpha0(u)=ones(3)*sin(2*pi*u); alpha1(u)=ones(3)*cos(2*pi*u); alpha2(u)=ones(3)*sin(pi*u); a_i(u)=alpha0(u)+alpha1(u)*Z_i1+alpha2(u)*Z_i2+e_i. Deterministic functions of current u and shared Z/e. Follow the source simulation paragraph including beta0.
epsilon_ij~N(0,0.5^2), independent of all previous variables and errors. Measurement-error sd=0.5.
Y_ij=beta0(U_ij)+X_ij^T*a_i(U_ij)+Z_i^T*beta(U_ij)+epsilon_ij; return cluster,U,X1,X2,X3,Z1,Z2,Y. Independent cluster-level Z/e draws induce shared within-cluster effects; sizes are coupled by the n-row budget.
</pre>

</details>


## Parameter scenarios, estimands and truth

| Scenario | Estimand | Definition | Reported value | Evidence status |
|---|---|---|---|---|
| original-sigma05 | Pointwise conditional mean | Integrate the mean-zero random effect from the Section 5 simulation model: sin(2*pi*u)*(1+z1+z2)+sum(x)*(sin(2*pi*u)+z1*cos(2*pi*u)+z2*sin(pi*u)). The fixed query is u=.25, x=(0,0,0), z=(0,0), yielding 1. The source coefficient alpha01 is a different estimand, though it happens to equal 1 here. | 1.0 | reported_numeric |

**Original submitted target notation:** m(u0,x0,z0)=E[Y\|U=u0,X=x0,Z=z0]


## Identifiability assumptions

- Random effect e~N(0,0.25*I3) is independent of X,Z,U and has mean zero.
- Errors are independent N(0,0.5^2). Individual covariates are independent N(0,I3), cluster covariates N(0,I2), and U is Uniform(0,1).
- Different clusters use independent Z/e draws, while their sizes are coupled by the fixed row budget. Individuals in the same cluster are dependent and cannot be treated as independent rows.
- The interface adaptation constrains the terminal cluster size. Cluster-table acceptance requires maintainer confirmation under the student guide; executable schema compliance is not that confirmation.
- The whole conditional query is specified before generation and does not condition on unobserved random effects.

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Adaptations from the source (submitted, unverified):**

- Follow the Section 5 simulation paragraph, which explicitly includes beta0(u)=sin(2*pi*u); disclose that general display (1.4) omits it.
- Preserve cluster identifiers and shared Z/e in a numeric table. The interface fixes n individuals rather than m=100 clusters; the terminal cluster size is budget-constrained, so cluster sizes are not iid under this interface. For n&lt;6 the sole budget cluster is smaller than the source support. This is an adaptation, not an exact source design.
- Replace the source coefficient-function target alpha01(u0) by the full conditional mean m(u0,x0,z0)=E[Y\|U=u0,X=x0,Z=z0], integrating the unobserved random effect. Fix u0=0.25 and x0=z0=0; truth remains 1 by coincidence of these chosen values.
- Cluster-table acceptance by the maintainer is not proven by the open schema role vocabulary. The numeric contract runs, but the guide's request to confirm multilayer data remains an external review step.
- Use CPU mechanism checks, not the paper's estimator, MISE or confidence-band experiment.

**Warnings:**

- Latent-variable candidates inferred from source equations; confirm their roles and completeness against the original paper or generator.
