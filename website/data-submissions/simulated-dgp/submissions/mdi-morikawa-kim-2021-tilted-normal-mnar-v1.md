# Full-population mean under identified exponentially tilted Gaussian MNAR

## Research question

- **Question and intended use.** Estimate the full-population outcome mean $\theta = \mathbb{E}[Y] \approx -0.0002555$ and construct a nominal 95% confidence interval when response depends directly on the unobserved continuous outcome (MNAR), without any excluded instrumental or shadow variable. This design is proposed as an evaluation benchmark candidate for semiparametric nonignorable missing-data inference.
- **Behavior under test.** Because response propensity $\pi(x, y)$ declines with larger $Y$, both the complete-case sample mean (asymptotic limit $`\approx -0.06281`$) and MAR standardization using the respondent mean $\mathbb{E}[m(X)] = -0.0225$ are biased downward. Identification relies on the interaction term $`0.6 x_1 x_2`$ in the respondent outcome regression $m(x)$ inducing an observable interaction coefficient $`-0.6\gamma x_1 x_2 = +0.18 x_1 x_2`$ in the marginal nonresponse log-odds $`\mathrm{logit}\{q(x)\}`$. The case evaluates whether estimators exploit this nonlinear structural identification and approach the semiparametric efficiency bound (under the paper's smoothness, moment, and nonsingularity conditions).

## Study design and data source

- **Motivation and references.** Morikawa and Kim (2021), *Semiparametric optimal estimation with nonignorable nonresponse data*, *The Annals of Statistics* 49(5), 2991–3014, [DOI](https://doi.org/10.1214/21-AOS2070), verified from the author manuscript [arXiv:1612.09207v3](https://arxiv.org/html/1612.09207v3), Sections 2, 3.1, 5–6, and Appendix A (Scenario 3, $`n = 500`$). All printed covariate variances, conditional regression parameters, and logistic selection coefficients are preserved verbatim (noting the paper writes $+0.3y$ in the logistic denominator exponent, which equals $-0.3y$ in the response logit). Adaptations use the analytically equivalent pattern-mixture sampling order $(X \to R \mid X \to Y \mid X, R)$ implied by exponential tilting, adopt 1,000 benchmark replicates (versus 2,000 in the source study), and record missing outcomes via `R` and finite placeholder `0` (serialized as float `0.0`) in `Y_obs`.
- **Population and sampling.** Each replicate draws $n = 500$ i.i.d. units from the continuous joint distribution of $`(X_1, X_2, R, Y)`$. Marginal nonresponse probability is $\mathbb{E}[q(X)] \approx 29.66\%$ (matching the paper's reported rounded 30% nonresponse rate).

## DAG and identification

- **Variables and causal structure.** $`X = (X_1, X_2)`$ (`X1`, `X2`) is the fully observed bivariate covariate vector, $R$ (`R`) is the response indicator, $Y$ is the latent complete outcome, and $`Y_{\mathrm{obs}}`$ (`Y_obs`) is the masked observed outcome. The DAG below depicts the generative pattern-mixture sampling factorization $P(X)P(R \mid X)P(Y \mid X, R)$ (so `R -> Y` reflects the sampling order; under the equivalent joint selection factorization $P(X)P(Y \mid X)P(R \mid X, Y)$ with $\Pr(R = 1 \mid X, Y) = \pi(X, Y)$, the selection arrow runs `Y -> R`).
- **DAG edges.** `X -> R, X -> Y, R -> Y, Y -> Y_obs, R -> Y_obs`
- **Assumptions.** Units are i.i.d. with positive respondent probability and full-support bivariate Gaussian covariates ($`\det \Sigma_X = 1/8 > 0`$, making $`\{1, x_1, x_2, x_1 x_2\}`$ linearly independent); the response-logit selection model $`\pi(x, y) = \mathrm{expit}(\alpha_0 + \alpha_1 x_1 + \alpha_2 x_2 + \gamma y)`$ is additive in $`(x_1, x_2, y)`$ (excluding any $`x_1 x_2`$ term); and the respondent distribution $Y \mid (X = x, R = 1) \sim \mathcal{N}(m(x), \sigma^2)$ has constant within-pattern variance $\sigma^2 = 1/4$ and nonzero interaction $`0.6 x_1 x_2`$. By Bayes' rule and the Gaussian moment-generating function, writing $`a(x) = \alpha_0 + \alpha_1 x_1 + \alpha_2 x_2`$ yields $`\mathrm{logit}\{q(x)\} = -a(x) - \gamma m(x) + \gamma^2\sigma^2/2 = -0.8695 + 0.62 x_1 + 0.62 x_2 + 0.18 x_1 x_2`$. The observable respondent law identifies $(m, \sigma^2)$, the observable interaction coefficient in $`\mathrm{logit}\{q(x)\}`$ is $-0.6\gamma = +0.18$ and uniquely identifies $\gamma = -0.18/0.6 = -0.3$, and the remaining linear and constant terms identify $`(\alpha_0, \alpha_1, \alpha_2)`$ and $\theta$.

```mermaid
flowchart LR
    X["X (bivariate Gaussian covariates)"] --> R["R (response indicator)"]
    X["X (bivariate Gaussian covariates)"] --> Y["Y (complete outcome)"]
    R["R (response indicator)"] --> Y["Y (complete outcome)"]
    Y["Y (complete outcome)"] --> Y_obs["Y_obs (masked outcome)"]
    R["R (response indicator)"] --> Y_obs["Y_obs (masked outcome)"]
```

## Variables and data-generating process

- **Variables and observed input.** One row corresponds to one unit. Every estimator receives the four columns `X1`, `X2`, `R`, and `Y_obs`. Both covariates are real-valued, `R` is binary, and `Y_obs` equals $`Y_i`$ when `R == 1` and finite placeholder `0` (serialized as float `0.0`) when `R == 0`. Unobserved outcomes, Gaussian disturbances, and oracle selection functions are withheld from estimator inputs.
- **Draw order and scenarios.** Under the single scenario `original` ($`n = 500`$): independently for each unit $i$, draw $`X_{i1} \sim \mathcal{N}(0, 1/2)`$ and $`X_{i2} \mid X_{i1} \sim \mathcal{N}(-X_{i1}/3, 1/4)`$, compute $`m(X_i)`$ and $`q(X_i)`$, draw $`R_i \sim \mathrm{Bernoulli}\{1 - q(X_i)\}`$, draw $`\epsilon_i \sim \mathcal{N}(0, 1/4)`$, form $`Y_i = m(X_i) + 0.075(1 - R_i) + \epsilon_i`$, and record $`Y_{\mathrm{obs},i} = R_i Y_i`$.

### Structural equations

- **Structural parents.** `X -> R, X -> Y, R -> Y, Y -> Y_obs, R -> Y_obs`

```math
\begin{aligned}
X_{i1} &\overset{\mathrm{iid}}{\sim} \mathcal{N}(0, 1/2), \qquad X_{i2} \mid (X_{i1} = x_1) \sim \mathcal{N}(-x_1 / 3, 1/4), && i = 1, \ldots, n, \quad n = 500, \\
m(x) &= 0.0775 + 0.4 x_1 + 0.4 x_2 + 0.6 x_1 x_2, && \\
\pi(x, y) &= \mathrm{expit}(0.904 - 0.5 x_1 - 0.5 x_2 - 0.3 y), && \\
q(x) &= \mathrm{expit}\!\left(-0.904 + 0.5 x_1 + 0.5 x_2 + 0.3 m(x) + \frac{0.3^2}{8}\right), && \\
R_i \mid (X_i = x) &\sim \mathrm{Bernoulli}\{1 - q(x)\}, && \\
\epsilon_i &\overset{\mathrm{iid}}{\sim} \mathcal{N}(0, 1/4), && \epsilon_i \perp (X_i, R_i), \\
Y_i &= m(X_i) + (1 - R_i)\frac{0.3}{4} + \epsilon_i, \qquad Y_{\mathrm{obs},i} = R_i Y_i.
\end{aligned}
```

By Bayes' rule and the Gaussian moment-generating function, writing $`a(x) = \alpha_0 + \alpha_1 x_1 + \alpha_2 x_2`$ and $\gamma = -0.3$ gives $`\mathrm{logit}\{q(x)\} = -a(x) - \gamma m(x) + \gamma^2\sigma^2/2 = -0.8695 + 0.62 x_1 + 0.62 x_2 + 0.18 x_1 x_2`$ (with interaction $`-0.6\gamma x_1 x_2 = +0.18 x_1 x_2`$) and nonrespondent shift $-\gamma\sigma^2 = +0.075$. Within-pattern variance $\mathrm{Var}(Y \mid X, R) = 1/4$ is constant, while full-data $`\mathrm{Var}(Y \mid X) = 1/4 + 0.075^2 q(X)\{1 - q(X)\}`$ varies with $X$.

| Symbol | Meaning | Definition or setting |
| --- | --- | --- |
| $i, n$ | Unit index and sample size | $i = 1, \ldots, n$; fixed $n = 500$ from source Scenario 3 (`original`). |
| $`X_{i1}, X_{i2}, X_i`$ | Observed correlated covariates | $`X_{i1} \sim \mathcal{N}(0, 1/2)`$, $`X_{i2} \mid X_{i1} \sim \mathcal{N}(-X_{i1}/3, 1/4)`$, $`\det \Sigma_X = 1/8`$, $`\mathbb{E}[X_{i1}X_{i2}] = -1/6`$; columns `X1`, `X2`. |
| $m(x)$ | Respondent conditional mean | $`m(x) = 0.0775 + 0.4x_1 + 0.4x_2 + 0.6x_1x_2`$; fixed printed source coefficients. |
| $\pi(x, y)$ | Selection response propensity | $`\pi(x, y) = \Pr(R = 1 \mid X = x, Y = y) = \mathrm{expit}(0.904 - 0.5x_1 - 0.5x_2 - 0.3y)`$ ($`\gamma = -0.3`$ in response logit). |
| $q(x)$ | Marginal nonresponse probability | $`\Pr(R = 0 \mid X = x) = \mathrm{expit}(-0.904 + 0.5x_1 + 0.5x_2 + 0.3m(x) + 0.01125) = \mathrm{expit}(-0.8695 + 0.62x_1 + 0.62x_2 + 0.18x_1x_2)`$; $\mathbb{E}[q(X)] \approx 29.66\%$. |
| $`R_i`$ | Response indicator | Drawn from $`\mathrm{Bernoulli}\{1 - q(X_i)\}`$; column `R`. |
| $`\epsilon_i`$ | Pattern-mixture disturbance | Independent $\mathcal{N}(0, 1/4)$ noise (constant within-pattern variance $\sigma^2 = 1/4$, SD $`0.5`$), independent of $`(X_i, R_i)`$; latent. |
| $`Y_i, Y_{\mathrm{obs},i}`$ | Complete and masked outcomes | $`Y_i = m(X_i) + 0.075(1 - R_i) + \epsilon_i`$ (exponential tilt shift $-\gamma\sigma^2 = +0.075$ for nonrespondents); `Y_obs` $`= R_i Y_i`$ with placeholder `0` when $`R_i = 0`$. |
| $\theta$ | Full-population outcome mean | $`\theta = \mathbb{E}[Y] = 0.0775 - 0.1 + 0.075\,\mathbb{E}[q(X)] \approx -0.0002554579`$. |

## Data-generating process and estimand

- **Estimand.** The scalar target is the full-population outcome mean $`\theta = \mathbb{E}[Y] = \mathbb{E}[m(X)] + (0.3/4)\,\mathbb{E}[q(X)] \approx -0.0002554579`$ in response units. Using the printed source coefficients at full precision (calibrated near zero), $\mathbb{E}[m(X)] = 0.0775 + 0.6(-1/6) = -0.0225$ and $\theta \approx -0.00025545787650235394$.
- **Truth check.** `truth.py` evaluates $\mathbb{E}[q(X)]$ via tensor Gauss–Hermite quadrature on the standardized bivariate Gaussian coordinates and combines it with the exact cross-moment $`\mathbb{E}[X_1 X_2] = -1/6`$. Independent verification in `verify.py` integrates $\mathbb{E}[m(X) + 0.075 q(X)]$ adaptively in 2D (matching within $`10^{-12}`$), recovers the interaction coefficient $+0.18 = -0.6\gamma$ via a four-point mixed difference of the implemented $`\mathrm{logit}\{q(x)\}`$, reconstructs response odds from $`(f_1, f_0, q)`$ across multiple $(x, y)$ points, and checks generated respondent conditional moments.

## Benchmark comparison

- **Output and comparator.** Methods return a scalar point estimate of $\theta$ and a nominal 95% confidence interval where applicable using `X1`, `X2`, `R`, and `Y_obs`. Comparators follow the protocol: (1) complete-case mean (population limit $`\approx -0.06281`$) with a nominal Student $`t_{m-1}`$ interval around the respondent mean using its respondent variance for $m$ respondents (requiring $`m \ge 2`$), (2) MAR standardization with respondent regression (limit $-0.0225$, averaging predicted respondent means from the specified interaction regression over all $X$ with an empirical sandwich normal interval propagating fitted regression and covariate-averaging uncertainty), (3) the Riddles–Kim–Im (2016) propensity-score estimator (method-specific SE with two-sided 95% normal quantile), and (4) Morikawa–Kim parametric and nonparametric respondent-model estimators (method-specific SE with two-sided 95% normal quantile; efficiency claims depend on estimator-specific smoothness, moment, and nonsingularity conditions).
- **Scoring and replication.** Compare methods over 1,000 paired independent datasets of size $n = 500$. Report bias, RMSE, empirical 95% coverage, mean interval width, Monte Carlo standard errors, valid denominators, and all failure or nonconvergence counts.

## Materials and access

- **Public materials.** The mechanism is documented in Morikawa and Kim (2021), [DOI](https://doi.org/10.1214/21-AOS2070) and [arXiv:1612.09207v3](https://arxiv.org/html/1612.09207v3), governed by the publisher's license terms.
- **Reproduction and protected materials.** The private review archive `mdi-morikawa-kim-2021-tilted-normal-mnar-v1.zip` (SHA-256 `9ca6cc7d697490ddc02c5131d6af180e82b51f9ade202afcbbe07ea4085d1810`) includes `generator.py`, `truth.py`, `verify.py`, `reproduce.py`, `collection.json`, `config.json`, `schema.csv`, `card.md`, `PROVENANCE.md`, `source_audit.json`, `requirements.txt` (`numpy==2.3.5`, `scipy==1.16.3`), check logs, and `MANIFEST.json`. After verifying the manifest in Python 3.12, run:

```bash
python3 reproduce.py --scenario original --n 500 --seed 1729 --out ../morikawa-kim-2021-check
```

The script validates all numerical, mixed-difference, generated-respondent, and actual-table checks and exports `observed.csv` (`X1,X2,R,Y_obs`, 500 rows) separately from `reference.json`.
