# Marginal outcome CDF under exponential-predictor MAR nonresponse

## Research question

- **Question and intended use.** Estimate the full-data marginal distribution functional $`\eta_2 = \Pr(Y < 0.15) \approx 0.528267`$ and construct a nominal 95% confidence interval when continuous outcomes are missing at random with steeply declining response propensity in the right tail of an exponential predictor. This case is proposed as an evaluation benchmark candidate for missing-data inference beyond mean functionals.
- **Behavior under test.** Because response probability $\pi(x) = \mathrm{expit}(3 - 3x)$ drops sharply as $X$ increases (yielding $42.04\%$ expected missingness), the complete-case empirical CDF converges to $0.557693$ (an upward bias of $`+0.029426`$), while inverse probability weighting suffers from severe weak-overlap tail instability ($`\mathbb{E}[1/\pi(X)] = \infty`$). Moreover, indicator-based method-of-moments targets expose standard Rubin variance bias under uncongenial or parametric multiple imputation.

## Study design and data source

- **Motivation and references.** Yang and Kim (2016), *A note on multiple imputation for method of moments estimation*, *Biometrika* 103(1), 244–251, [DOI](https://doi.org/10.1093/biomet/asv073), verified from the [author-hosted version of record](https://shuyang.wordpress.ncsu.edu/files/2022/11/Yang-Kim-2016-Biometrika-A-note-on-multiple-imputation-for-method-of-moments-estimation.pdf), Section 5, Setting 1, Scenario (ii) and Table 1. The unit-rate exponential covariate, linear Gaussian response with error variance $0.5$, logistic response probability $\Pr(R = 1 \mid X = x) = \mathrm{expit}(3 - 3x)$ (equivalently missingness probability $`\Pr(R = 0 \mid X = x) = \mathrm{expit}(3x - 3)`$), sample size $n = 2000$, and second estimand $`\eta_2 = \Pr(Y < 0.15)`$ are taken verbatim from the source. Adaptations select the paper's second estimand and 1,000 benchmark replicates (versus 5,000 replicates with 500 imputations in source Table 1) and represent unavailable responses via finite placeholder `0` (serialized as float `0.0`) in `Y_obs` paired with `R`.
- **Population and sampling.** Units are $n = 2000$ independent and identically distributed draws from the continuous superpopulation $(X, Y, R)$. The observed respondent count is random with theoretical response probability $57.9573\%$ (missingness $`42.0427\%`$).

## DAG and identification

- **Variables and causal structure.** $X$ (`X`) is the fully observed exponential covariate, $Y$ is the latent complete outcome, $R$ (`R`) is the binary response indicator governed solely by $X$, and $`Y_{\mathrm{obs}}`$ (`Y_obs`) is the masked observed outcome.
- **DAG edges.** `X -> Y, X -> R, Y -> Y_obs, R -> Y_obs`
- **Assumptions.** Units are i.i.d.; missingness satisfies MAR ($`R \perp Y \mid X`$) with pointwise strictly positive response propensity $\pi(x) = \mathrm{expit}(3 - 3x) \in (0, 1)$ for all $x > 0$, nonparametrically identifying $`\eta_2 = \mathbb{E}[\Pr(Y < 0.15 \mid X, R = 1)]`$. **Overlap and regularity qualification:** because $\pi(x) \to 0$ as $x \to \infty$ faster than $e^{-x}$, there is no uniform lower bound on $\pi(x)$ and $\mathbb{E}[1/\pi(X)] = \infty$. Consequently, ordinary normalized IPW for $`\mathbf{1}\{Y < 0.15\}`$ has an infinite centered second moment and its untrimmed sandwich normal interval has no finite-variance normal justification (evaluated empirically as a stress comparator under the benchmark protocol). By contrast, for this indicator the oracle AIPW residual-variance term $`\mathbb{E}[g(X)\{1 - g(X)\}/\pi(X)]`$ is finite—though huge ($`\approx 1.34 \times 10^{43}`$), dominated by the Gaussian-tail region—so oracle AIPW uses a nominal normal interval evaluated empirically (while estimating nuisance functions requires separate rate and variance conditions, and any externally trimmed estimator targets a distinct trimmed estimand).

```mermaid
flowchart LR
    X["X (exponential covariate)"] --> Y["Y (complete outcome)"]
    X["X (exponential covariate)"] --> R["R (response indicator)"]
    Y["Y (complete outcome)"] --> Y_obs["Y_obs (masked outcome)"]
    R["R (response indicator)"] --> Y_obs["Y_obs (masked outcome)"]
```

## Variables and data-generating process

- **Variables and observed input.** Each row represents one independent unit. Methods receive the three observed columns `X` ($`> 0`$), `R` ($`\in \{0, 1\}`$), and `Y_obs` ($`\in \mathbb{R}`$, set to finite placeholder `0` / `0.0` whenever `R == 0`). Estimators must use `Y_obs` only where `R == 1` and preserve the strict indicator $`\mathbf{1}\{Y < 0.15\}`$. Unobserved outcomes, Gaussian disturbances, and oracle propensities are excluded from estimator inputs.
- **Draw order and scenarios.** Under the single scenario `original` ($`n = 2000`$): independently for each row $i = 1, \ldots, n$, draw $`X_i \sim \mathrm{Exp}(1)`$ and $`\epsilon_i \sim \mathcal{N}(0, 0.5)`$, form $`Y_i = 0.1 X_i + \epsilon_i`$, draw $`R_i \mid X_i \sim \mathrm{Bernoulli}\{\mathrm{expit}(3 - 3X_i)\}`$, and set $`Y_{\mathrm{obs},i} = R_i Y_i`$. All parameters stay fixed across replicates.

### Structural equations

- **Structural parents.** `X -> Y, X -> R, Y -> Y_obs, R -> Y_obs`

```math
\begin{aligned}
X_i &\overset{\mathrm{iid}}{\sim} \mathrm{Exp}(1), && i = 1, \ldots, n, \quad n = 2000, \\
\epsilon_i &\overset{\mathrm{iid}}{\sim} \mathcal{N}(0, 0.5), && \epsilon_i \perp X_i, \\
Y_i &= 0.1 X_i + \epsilon_i, && \\
R_i \mid (X_i, Y_i) &\sim \mathrm{Bernoulli}\bigl\{\mathrm{expit}(3 - 3X_i)\bigr\}, && \\
Y_{\mathrm{obs},i} &= R_i Y_i.
\end{aligned}
```

All rows are drawn independently across units and replicate tables; $\mathrm{expit}(t) = (1 + e^{-t})^{-1}$ specifies the response probability $`\Pr(R_i = 1 \mid X_i) = \mathrm{expit}(3 - 3X_i)`$ (equivalently missingness $`\Pr(R_i = 0 \mid X_i) = \mathrm{expit}(3X_i - 3)`$), and unobserved outcomes ($`R_i = 0`$) take finite placeholder $`Y_{\mathrm{obs},i} = 0`$.

| Symbol | Meaning | Definition or setting |
| --- | --- | --- |
| $i, n$ | Unit index and sample size | $i = 1, \ldots, n$; fixed $n = 2000$ from the source simulation (`original` scenario). |
| $`X_i`$ | Observed right-skewed covariate | Unit-rate exponential $\mathrm{Exp}(1)$ on $(0, \infty)$ with mean $1$; column `X`. |
| $`\epsilon_i`$ | Outcome disturbance | Independent $\mathcal{N}(0, 0.5)$ noise (variance $0.5$, SD $`1/\sqrt{2}`$); latent. |
| $`Y_i`$ | Complete continuous outcome | Linear regression $`Y_i = 0.1X_i + \epsilon_i`$; latent when $`R_i = 0`$. |
| $\mathrm{expit}(t)$ | Logistic response link | $\mathrm{expit}(t) = 1 / (1 + e^{-t})$; response probability $\pi(x) = \Pr(R = 1 \mid X = x) = \mathrm{expit}(3 - 3x)$, missingness $\Pr(R = 0 \mid X = x) = \mathrm{expit}(3x - 3)$ (expected missingness $`42.04\%`$). |
| $`R_i`$ | Response indicator | Drawn from $`\mathrm{Bernoulli}\{\mathrm{expit}(3 - 3X_i)\}`$ given $`X_i`$; column `R`. |
| $`Y_{\mathrm{obs},i}`$ | Observed masked outcome | Equals $`Y_i`$ when $`R_i = 1`$ and placeholder $0$ when $`R_i = 0`$; column `Y_obs`. |
| $`\eta_2`$ | Target marginal CDF | $`\eta_2 = \Pr(Y < 0.15) \approx 0.5282671016`$, evaluated on the full-data distribution. |

## Data-generating process and estimand

- **Estimand.** The scalar target is the full-data marginal distribution probability $`\eta_2 = \Pr(Y < 0.15) \approx 0.5282671016 \in [0, 1]`$.
- **Truth check.** Since $Y = 0.1 X + \epsilon$ is the continuous exponentially modified Gaussian convolution of $\mathrm{Exp}(\text{rate}=10)$ and $\mathcal{N}(0, 0.5)$, its exact CDF admits the closed form $`\eta_2 = \Phi(y_0/\sigma) - \exp(-\lambda y_0 + \tfrac{1}{2}\lambda^2\sigma^2)\,\Phi(y_0/\sigma - \lambda\sigma)`$ with $`y_0 = 0.15`$, $\lambda = 10$, and $\sigma = \sqrt{0.5}$, yielding $`\eta_2 = 0.5282671015927344`$. Independent adaptive quadrature of $`\int_0^\infty \Phi((0.15 - 0.1x)/\sqrt{0.5}) e^{-x}\,dx`$ in `verify.py` matches to within $10^{-12}$, alongside adaptive-quadrature checks of the exact nonresponse probability ($`0.42042699`$) and complete-case CDF limit ($`0.55769275`$) and generated respondent conditional-outcome and strict-threshold indicator moment checks.

## Benchmark comparison

- **Output and comparator.** Methods produce a scalar estimate of $`\eta_2`$ and a nominal 95% confidence interval where applicable from the identical observed columns `X`, `R`, and `Y_obs`. Comparators follow the untrimmed strict-threshold protocol: (1) complete-case CDF (averaging $`\mathbf{1}\{Y < 0.15\}`$ over respondents, asymptotic limit $0.557693$, with a 95% Wilson interval), (2) parametric multiple imputation ($`M = 500`$ Bayesian no-intercept Gaussian regression imputations with prior proportional to $\sigma^{-2}$, estimating the strict-threshold CDF in each completed table with Rubin's pooled variance and Table 1 Student $t$ interval using $(M - 1)/\lambda^2$ degrees of freedom), (3) over-imputation with bias-corrected variance (using the same 500 Bayesian regression draws to over-impute both respondents and nonrespondents, with eq. (13) corrected variance and eq. (14) Satterthwaite $t$ degrees of freedom), (4) oracle augmented IPW (averaging $`g(X) + R\{\mathbf{1}(Y < 0.15) - g(X)\}/\pi(X)`$ using the stated $g$ and $\pi$ with nominal normal interval from the sample SD divided by $\sqrt{n}$, evaluated empirically), and (5) oracle normalized IPW stress comparator ($`\sum R\mathbf{1}\{Y < 0.15\}/\pi(X)`$ divided by $\sum R/\pi(X)$ with nominal sandwich normal interval, reporting point metrics and empirical coverage while noting untrimmed weights have no finite-variance normal justification).
- **Scoring and replication.** Evaluate all methods on 1,000 paired independent datasets of size $n = 2000$. Report bias, RMSE, empirical 95% coverage, mean interval length, Monte Carlo uncertainty, valid denominators, and full failure or timeout counts.

## Materials and access

- **Public materials.** The design is documented in Yang and Kim (2016), [DOI](https://doi.org/10.1093/biomet/asv073) and the [author-hosted PDF](https://shuyang.wordpress.ncsu.edu/files/2022/11/Yang-Kim-2016-Biometrika-A-note-on-multiple-imputation-for-method-of-moments-estimation.pdf), subject to publisher copyright terms.
- **Reproduction and protected materials.** The private review archive `mdi-yang-kim-2016-exp-cdf-mar-v1.zip` (SHA-256 `006821e27091b146648ba541548dc5b6668c4f56ed4ae6a3f931c29a8d2b5d3d`) bundles `generator.py`, `truth.py`, `verify.py`, `reproduce.py`, `collection.json`, `config.json`, `schema.csv`, `card.md`, `PROVENANCE.md`, `source_audit.json`, `requirements.txt` (`numpy==2.3.5`, `scipy==1.16.3`), check reports, and `MANIFEST.json`. After manifest verification in Python 3.12, run:

```bash
python3 reproduce.py --scenario original --n 2000 --seed 1729 --out ../yang-kim-2016-check
```

The command validates all truth, generated-respondent, and actual-table checks and writes the 2,000-row observed table `observed.csv` (`X,R,Y_obs`) separately from `reference.json`.
