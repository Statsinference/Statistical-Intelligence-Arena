# Truncated-normal-factor Poisson donor-and-proxy panel

> **Unverified extraction — scientific review required.**

**Primary area:** Legacy DiD / Synthetic Control — classification needed

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Shi, X., Li, K. Q., Yu, M., Miao, W., Kuchibhotla, A. K., Hu, M., and Tchetgen Tchetgen, E. (2026). Theory for Identification and Inference with Synthetic Controls: A Proximal Causal Inference Framework. Journal of the American Statistical Association, advance online publication. DOI:10.1080/01621459.2026.2639734

**DOI:** 10.1080/01621459.2026.2639734 · **Source locator:** Formal supplement J.8, PDF49-51, Eq S.25 and Fig S.8 (Figshare31627658.v1); main Section4 loading formula at r1; 2023 code commit1973d7c8fc2ecd2a94b73292b58a594361db0542, Simulation/myfunctions_NonlinearSetting.R lines26-44,116-130

## DGP / generation mechanism

**Sampling design:** Unit: One fixed three-unit panel experiment; n=3 means treated, donor, supplemental proxy unit rows; columns are 100 pre and100 post counts.; Dependence: Shared lambda_t induces positive contemporaneous unconditional cross-unit covariance. Given the entire factor path, all observed Poisson draws are independent. Factor paths are iid across times. No independent-row assumption.

**Generator source:** [generator.py](https://github.com/Statsinference/stats-inference-arena/blob/main/dgp-submissions/registry/generators/did-shi-2026-poisson-proxy-logrr-v1.py)

**Keywords (source-described):** Nonlinearity · Panel data

**Observed variables**

G, P, Y_pre001, Y_pre002, Y_pre003, Y_pre004, Y_pre005, Y_pre006, Y_pre007, Y_pre008, Y_pre009, Y_pre010, Y_pre011, Y_pre012, Y_pre013, Y_pre014, Y_pre015, Y_pre016, Y_pre017, Y_pre018, Y_pre019, Y_pre020, Y_pre021, Y_pre022, Y_pre023, Y_pre024, Y_pre025, Y_pre026, Y_pre027, Y_pre028, Y_pre029, Y_pre030, Y_pre031, Y_pre032, Y_pre033, Y_pre034, Y_pre035, Y_pre036, Y_pre037, Y_pre038, Y_pre039, Y_pre040, Y_pre041, Y_pre042, Y_pre043, Y_pre044, Y_pre045, Y_pre046, Y_pre047, Y_pre048, Y_pre049, Y_pre050, Y_pre051, Y_pre052, Y_pre053, Y_pre054, Y_pre055, Y_pre056, Y_pre057, Y_pre058, Y_pre059, Y_pre060, Y_pre061, Y_pre062, Y_pre063, Y_pre064, Y_pre065, Y_pre066, Y_pre067, Y_pre068, Y_pre069, Y_pre070, Y_pre071, Y_pre072, Y_pre073, Y_pre074, Y_pre075, Y_pre076, Y_pre077, Y_pre078, Y_pre079, Y_pre080, Y_pre081, Y_pre082, Y_pre083, Y_pre084, Y_pre085, Y_pre086, Y_pre087, Y_pre088, Y_pre089, Y_pre090, Y_pre091, Y_pre092, Y_pre093, Y_pre094, Y_pre095, Y_pre096, Y_pre097, Y_pre098, Y_pre099, Y_pre100, Y_post001, Y_post002, Y_post003, Y_post004, Y_post005, Y_post006, Y_post007, Y_post008, Y_post009, Y_post010, Y_post011, Y_post012, Y_post013, Y_post014, Y_post015, Y_post016, Y_post017, Y_post018, Y_post019, Y_post020, Y_post021, Y_post022, Y_post023, Y_post024, Y_post025, Y_post026, Y_post027, Y_post028, Y_post029, Y_post030, Y_post031, Y_post032, Y_post033, Y_post034, Y_post035, Y_post036, Y_post037, Y_post038, Y_post039, Y_post040, Y_post041, Y_post042, Y_post043, Y_post044, Y_post045, Y_post046, Y_post047, Y_post048, Y_post049, Y_post050, Y_post051, Y_post052, Y_post053, Y_post054, Y_post055, Y_post056, Y_post057, Y_post058, Y_post059, Y_post060, Y_post061, Y_post062, Y_post063, Y_post064, Y_post065, Y_post066, Y_post067, Y_post068, Y_post069, Y_post070, Y_post071, Y_post072, Y_post073, Y_post074, Y_post075, Y_post076, Y_post077, Y_post078, Y_post079, Y_post080, Y_post081, Y_post082, Y_post083, Y_post084, Y_post085, Y_post086, Y_post087, Y_post088, Y_post089, Y_post090, Y_post091, Y_post092, Y_post093, Y_post094, Y_post095, Y_post096, Y_post097, Y_post098, Y_post099, Y_post100

**Latent variables**

lambda_t, W_1t, W_2t

**Latent-variable identification:** candidates from equations need review

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

**factor**

$$
\lambda_{t} \text{ iid } TN(0.5,0.1^{2};(0,1))
$$

$$
t=1,\ldots ,200
$$

**conditional_marginals**

$$
Y_{t}\mid \lambda_{t} \sim \mathrm{Pois}(\exp(\lambda_{t}-2\cdot 1(t>100)))
$$

$$
W_{1t},W_{2t}\mid \lambda_{t} \sim \mathrm{Pois}(\lambda_{t}/(e-1))
$$

**joint_law_adaptation**

Given lambda_1:200, all 600 observed draws are

mutually independent

factors

independent across periods

**estimand**

$$
\log(\mathbb{E}[Y_{t}(1)]/\mathbb{E}[Y_{t}(0)])=-2
$$

<details>
<summary>Original source equations (verbatim)</summary>

<pre>
lambda_t iid TN(0.5,0.1^2;(0,1)); t=1,...,200
Y_t|lambda_t ~ Pois(exp(lambda_t-2*1(t&gt;100))); W_1t,W_2t|lambda_t ~ Pois(lambda_t/(e-1))
Given lambda_1:200, all 600 observed draws are mutually independent; factors independent across periods.
log(E[Y_t(1)]/E[Y_t(0)])=-2
</pre>

</details>


## Parameter scenarios, estimands and truth

| Scenario | Estimand | Definition | Reported value | Evidence status |
|---|---|---|---|---|
| baseline | log_RR_pop | For the treated unit at any post period, log(E[Y_t(1)]/E[Y_t(0)]) over the truncated-normal factor and Poisson population; equals -2. This is neither the impossible printed negative rate ratio nor an additive ATT nor finite-sample SATT. | -2 | reported_numeric |

## Identifiability assumptions

- Consistency with deterministic treated-row treatment beginning after period100 and no interference on controls.
- The untreated treated-unit mean is exp(lambda); its post treatment mean is exp(lambda-2), while controls remain Poisson(lambda/(e-1)).
- Common iid truncated-normal factor and conditional product-Poisson sampling across all units and times are the explicitly authorized joint-law adaptation.
- Both control roles are observed and have identical loading1; proxy identities are fixed. Identification by a particular estimator is not established by this generator.

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Warnings:**

- Latent-variable candidates inferred from source equations; confirm their roles and completeness against the original paper or generator.
