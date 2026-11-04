# Lin et al. (2024) linear IV adapted from pinned WIT code

> **Unverified extraction — scientific review required.**

**Primary area:** IV — Instrumental Variables

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Lin, Y., Windmeijer, F., Song, X., and Fan, Q. (2024). On the instrumental variable estimation with many weak and invalid instruments. JRSS-B 86(4), 1068-1088. DOI: 10.1093/jrsssb/qkae025.

**DOI:** — · **Source locator:** Commit b0d078533650f0d0766b8c73aaaa99ddc97fe8a2; blob 179178ad1f19ac946bc470e61b6e17e7bec63b59; Simulation.R one-based lines 40-49 and 101-136. Paper Section 2.1 Eq.(1), Section 4. Handoff PDF p.17/journal p.1084; typesetting unresolved.

## DGP / generation mechanism

**Sampling design:** Unit: individual; Dependence: iid individuals; correlated Z components and correlated epsilon/eta within individuals; Z independent of errors

**Generator source:** [generator.py](../generators/iv-lin-2024-wit-code-v1.py)

**Keywords (source-described):** Linearity

**Observed variables**

Z1, Z2, Z3, Z4, Z5, Z6, Z7, Z8, Z9, Z10, Z11, Z12, Z13, Z14, Z15, Z16, Z17, Z18, Z19, Z20, Z21, D, Y

**Latent variables**

eta_i

**Latent-variable identification:** candidates from equations need review

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

**Instrument distribution**

$$
Z_i\sim\mathcal{N}_{21}(0,\Sigma_Z),\qquad (\Sigma_Z)_{jk}=0.8(0.3)^{|j-k|},\quad j,k=1,\ldots,21.
$$

**Joint structural error distribution**

$$
\begin{pmatrix}\varepsilon_i\\\eta_i\end{pmatrix}\sim\mathcal{N}_2\!\left(\begin{pmatrix}0\\0\end{pmatrix},\begin{pmatrix}1&0.6\\0.6&1\end{pmatrix}\right).
$$

**Sampling independence**

$$
Z_i\perp\!\!\!\perp(\varepsilon_i,\eta_i),\qquad (Z_i,\varepsilon_i,\eta_i)\overset{\mathrm{iid}}{\sim}P,\quad i=1,\ldots,n.
$$

**Common fixed parameters**

$$
p=21,\qquad\beta=1,\qquad\alpha=(0\mathbf{1}_{9}^{\top},0.4\mathbf{1}_{6}^{\top},0.2\mathbf{1}_{6}^{\top})^{\top}.
$$

**Default code_case_2 first-stage coefficients**

$$
\gamma_{\mathrm{code\_case\_2}}=0.15\mathbf{1}_{21}.
$$

**Alternative code_case_1 first-stage coefficients**

$$
\gamma_{\mathrm{code\_case\_1}}=0.4\mathbf{1}_{21}.
$$

**Endogenous continuous treatment**

$$
D_i=Z_i^{\top}\gamma+\eta_i.
$$

**Continuous outcome**

$$
Y_i=\beta D_i+Z_i^{\top}\alpha+\varepsilon_i.
$$

<details>
<summary>Original source equations (verbatim)</summary>

<pre>
Z_i ~ N_21(0, Sigma_Z); (Sigma_Z)_{jk} = 0.8 * 0.3^{|j-k|} for j,k=1,...,21, including diagonal entries 0.8.
(epsilon_i, eta_i)^T ~ N_2(0, [[1, 0.6], [0.6, 1]]); both variances are 1 and Corr(epsilon_i,eta_i)=0.6, following the pinned author code.
Z_i is independent of (epsilon_i, eta_i). The vectors (Z_i, epsilon_i, eta_i) are iid across individuals i=1,...,n; epsilon_i and eta_i are correlated within an individual.
p=21; beta=1; alpha=(0 repeated 9 times, 0.4 repeated 6 times, 0.2 repeated 6 times)^T. Thus Z1-Z9 have zero direct outcome coefficients, while Z10-Z21 have nonzero direct coefficients.
In code_case_2 (default), gamma=0.15*1_21. This is the active Case 2 setting of the pinned author script.
In code_case_1, gamma=0.4*1_21. This enables the commented Case 1 setting; it is another scenario of the same mechanism family.
D_i = Z_i^T gamma + eta_i.
Y_i = beta*D_i + Z_i^T alpha + epsilon_i. Only Z1,...,Z21,D,Y are observed outputs; epsilon and eta are internal disturbances.
</pre>

</details>


## Parameter scenarios, estimands and truth

| Scenario | Estimand | Definition | True value | Evidence status |
|---|---|---|---|---|
| code_case_2 | beta | Homogeneous structural coefficient: E[Y(do(D=d+1))-Y(do(D=d))]=beta for the specified superpopulation; both scenarios beta=1. Not LATE. | 1.0 | reported_numeric |
| code_case_1 | beta | Homogeneous structural coefficient: E[Y(do(D=d+1))-Y(do(D=d))]=beta for the specified superpopulation; both scenarios beta=1. Not LATE. | 1.0 | reported_numeric |

## Identifiability assumptions

- iid individuals, consistency, no interference
- Z independent of structural errors; positive definite covariances; nonzero first stage
- Z1-Z9 have zero direct effects conditional on other instruments; Z10-Z21 violate exclusion
- When validity is unknown, identification requires a rule such as plurality of equal reduced-form/first-stage coefficient ratios: valid group size 9 exceeds either invalid group size 6. No majority claimed.
- No LATE monotonicity condition for this homogeneous continuous-treatment target

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Warnings:**

- Latent-variable candidates inferred from source equations; confirm their roles and completeness against the original paper or generator.
