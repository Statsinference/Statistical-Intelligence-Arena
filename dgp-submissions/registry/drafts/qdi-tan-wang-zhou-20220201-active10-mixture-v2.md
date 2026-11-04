# QDI: active-coordinate Gaussian-mixture marginal of the Tan-Wang-Zhou design (10-dimensional adaptation)

> **Unverified extraction — scientific review required.**

**Primary area:** Quantile Inference

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Tan, K. M., Wang, L., and Zhou, W.-X. (2022). High-Dimensional Quantile Regression: Convolution Smoothing and Concave Regularization. Journal of the Royal Statistical Society Series B: Statistical Methodology 84(1), 205-233. DOI: 10.1111/rssb.12485.

**DOI:** 10.1111/rssb.12485 · **Source locator:** Actual mechanism text read: arXiv:2109.05640v1, submitted 2021-09-12, Section 5 Numerical study, PDF page 20 (printed manuscript page 20), unnumbered paragraph beginning For all the numerical experiments. Mixture results: Table 4, PDF page 22. Journal bibliographic pages 205-233 are a different pagination; final journal DGP text not compared.

## DGP / generation mechanism

**Sampling design:** Unit: individual (one row); Dependence: iid individuals; within-row Cov(Wj,Wk)=0.49^abs(j-k)=0.7^abs(Aj-Ak). Feature-index AR(1) is a Gaussian factorization, not time-series dependence.

**Generator source:** [generator.py](../generators/qdi-tan-wang-zhou-20220201-active10-mixture-v2.py)

**Keywords (source-described):** Linearity

**Observed variables**

W1, W2, W3, W4, W5, W6, W7, W8, W9, W10, Y

**Latent variables**

Z_ik, B_i, U_i

**Latent-variable identification:** candidates from equations need review

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

**Source-to-observation mapping**

$$
A=(1,3,5,7,9,11,13,15,17,19)
$$

$$
W_{ik}=X_{\mathrm{original},i},A[k]
$$

The remaining 990 zero-coefficient coordinates are marginalized out.

**Marginal covariates**

$$
W_{i} \sim \mathcal{N}_{10}(0,\Sigma_{AA})
$$

$$
(\Sigma_{AA})_{jk}=0.7^{\lvert \mathrm{Aj}-\mathrm{Ak}\rvert}=0.49^{\lvert j-k\rvert}
$$

independent rows.

**Sampling factorization**

$$
Z_{ik}\overset{\mathrm{iid}}{\sim} \mathcal{N}(0,1)
$$

$$
W_{i1}=Z_{i1}
$$

$$
W_{ik}=0.49\cdot W_{i,k-1}+\sqrt{1-0.49^{2}}\cdot Z_{ik}, k=2,\ldots ,10.
$$

**Coefficients**

$$
b=(1.8,1.6,1.4,1.2,1,-1,-1.2,-1.4,-1.6,-1.8)
$$

$$
\mathrm{intercept}=0. W_{k} \text{ is } \text{ the } \mathrm{original} \mathrm{coordinate} 2k-1.
$$

**Noise**

$$
B_{i} \sim \mathrm{Bernoulli}(0.7)
$$

$$
U_{i} \sim \mathcal{N}(0,1)
$$

independent of W and across rows

$$
\varepsilon_{i}=[B_{i}+5\cdot (1-B_{i})]\cdot U_{i} \sim 0.7\cdot \mathcal{N}(0,1)+0.3\cdot \mathcal{N}(0,25)
$$

$$
\mathrm{Normal} \mathrm{second} \mathrm{parameter} \text{ is } \text{ variance }.
$$

**Response**

$$
Y_{i}=\sum_{k=1}^{10} b_{k} W_{ik}+\varepsilon_{i}
$$

This is the marginal (X_A,Y) law of the parent independent-noise model. No clipping, standardization or quantile recentering.

**Fixed scalar query**

$$
w_{0}=e_{1} \in R^{10}
$$

$$
\theta_{\tau}=1.8+q_{\tau}
$$

$$
0.7\cdot \Phi(q_{\tau})+0.3\cdot \Phi(q_{\tau}/5)=\tau, \tau\in \{0.5,0.9\}.
$$

<details>
<summary>Original source equations (verbatim)</summary>

<pre>
A=(1,3,5,7,9,11,13,15,17,19); W_ik=X_original,i,A[k]. The remaining 990 zero-coefficient coordinates are marginalized out.
W_i ~ N_10(0,Sigma_AA); (Sigma_AA)_jk=0.7^abs(Aj-Ak)=0.49^abs(j-k); independent rows.
Z_ik iid N(0,1); W_i1=Z_i1; W_ik=0.49*W_i,k-1+sqrt(1-0.49^2)*Z_ik, k=2,...,10.
b=(1.8,1.6,1.4,1.2,1,-1,-1.2,-1.4,-1.6,-1.8); intercept=0. W_k is the original coordinate 2k-1.
B_i ~ Bernoulli(0.7), U_i ~ N(0,1), independent of W and across rows; epsilon_i=[B_i+5*(1-B_i)]*U_i ~ 0.7*N(0,1)+0.3*N(0,25). Normal second parameter is variance.
Y_i=sum_(k=1)^10 b_k W_ik+epsilon_i. This is the marginal (X_A,Y) law of the parent independent-noise model. No clipping, standardization or quantile recentering.
w0=e1 in R^10; theta_tau=1.8+q_tau; 0.7*Phi(q_tau)+0.3*Phi(q_tau/5)=tau, tau in {0.5,0.9}.
</pre>

</details>


## Parameter scenarios, estimands and truth

| Scenario | Estimand | Definition | True value | Evidence status |
|---|---|---|---|---|
| q50-active10-mixture | theta_tau = Q_tau(Y \| W = e1) | inf{y:F_Y\|W(y\|e1)&gt;=tau}, with W=(X_original,1,X_original,3,...,X_original,19) in R^10 and e1=(1,0,...,0). The default tau is 0.9; a second scenario uses 0.5. theta_tau=1.8+F_epsilon^(-1)(tau). This equals the parent model full-X target because the removed coordinates have zero coefficients and epsilon is independent of the full X. | 1.7999999999997158 | reported_numeric |
| q90-active10-mixture | theta_tau = Q_tau(Y \| W = e1) | inf{y:F_Y\|W(y\|e1)&gt;=tau}, with W=(X_original,1,X_original,3,...,X_original,19) in R^10 and e1=(1,0,...,0). The default tau is 0.9; a second scenario uses 0.5. theta_tau=1.8+F_epsilon^(-1)(tau). This equals the parent model full-X target because the removed coordinates have zero coefficients and epsilon is independent of the full X. | 4.2114834571051345 | reported_numeric |

## Identifiability assumptions

- Independent, identically distributed individuals with W and Y fully observed; no censoring, missingness or selection.
- The original Gaussian model has Sigma_jk=0.7^abs(j-k); its known active set is A=(1,3,5,7,9,11,13,15,17,19). W=X_A is its exact Gaussian marginal with covariance 0.49^abs(j-k).
- The 990 removed coordinates have zero coefficients in the parent response equation. They are correlated with W, so they are not claimed to be independent or marginally uninformative.
- The mixture error is independent of the original full X and independent across individuals; this explicit joint-law completion is inherited from v1 and still requires scientific review.
- Y=b^T W+epsilon with zero intercept. The ten-coordinate active set is known by construction; no support-selection or high-dimensional inference task is claimed.
- The conditional CDF is continuous and strictly increasing, with positive density at the fixed query quantiles. Conditioning at W=e1 uses the model-defined continuous conditional law.
- Any subsequent confidence-interval method must supply its own regularity and coverage argument; generator checks do not establish statistical coverage.

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Warnings:**

- Latent-variable candidates inferred from source equations; confirm their roles and completeness against the original paper or generator.
