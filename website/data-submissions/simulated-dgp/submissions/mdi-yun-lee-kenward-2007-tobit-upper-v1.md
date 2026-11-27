# Gaussian regression slope under known-threshold right censoring

## Research question

- **Question and intended use.** Estimate the complete-data linear regression slope $\beta_1 = 3$ and construct a nominal 95% confidence interval when outcomes exceeding the known upper reporting threshold $c = 3$ are right-censored. This design is proposed as a benchmark candidate for missing-data inference under identified threshold-based MNAR censoring.
- **Behavior under test.** Because censoring ($Y_i > 3$) occurs disproportionately at the upper end of the fixed covariate grid ($x_i \to 1$, where $\mathbb{E}[Y_i \mid x_i] = 4$), complete-case ordinary least squares suffers severe downward attenuation bias even though overall expected censoring is only $18.48\%$. The case evaluates whether estimators correctly incorporate the censored tail probability $\Pr(Y_i > 3 \mid x_i)$ through Tobit or hierarchical-likelihood inference in a moderate sample ($n = 100$).

## Study design and data source

- **Motivation and references.** Yun, Lee and Kenward (2007), *Using hierarchical likelihood for missing data problems*, *Biometrika* 94(4), 905–919, [DOI](https://doi.org/10.1093/biomet/asm063), verified from the [published PDF mirror](https://citeseerx.ist.psu.edu/document?doi=a6c166bb97a4a7deee230820b300ac48cd78c69e&repid=rep1&type=pdf), Example 4 (pp. 911–913, Figure 1 and Table 1(a)). The fixed regressor grid $x_i = -1 + 2i/100$, Gaussian regression parameters $(1, 3, \sigma^2 = 1)$, upper threshold $c = 3$, and sample size $n = 100$ follow the source verbatim. Adaptations adopt 1,000 benchmark replicates (versus 10,000 in the source study), store censored outcomes as finite placeholder `0` (serialized as float `0.0`) in `Y_obs` paired with the uncensored indicator `R` (recoverable to top-coded Tobit input via $R_i Y_{\mathrm{obs},i} + 3(1 - R_i)$), and extend $x_i = -1 + 2i/n$ for alternative sample sizes $n \ge 2$ (the generator rejects $n < 2$ because at least two distinct design points are required to identify the slope).
- **Population and sampling.** Each table contains $n = 100$ deterministic design points $x_1, \ldots, x_{100}$ with independent standard normal disturbances. Expected censoring across the fixed grid is $\frac{1}{100}\sum_{i=1}^{100} \{1 - \Phi(2 - 3x_i)\} = 18.4771\%$, and the realized censored count follows a Poisson–binomial distribution with fraction SD $\approx 0.02864$.

## DAG and identification

- **Variables and causal structure.** $X$ (`X`) is the fixed observed regressor, $Y$ is the latent complete Gaussian response, $R$ (`R`) is the uncensored indicator determined directly by $Y \le 3$, and $Y_{\mathrm{obs}}$ (`Y_obs`) is the masked observed outcome.
- **DAG edges.** `X -> Y, Y -> R, Y -> Y_obs, R -> Y_obs`
- **Assumptions.** Errors are i.i.d. $\mathcal{N}(0, \sigma^2)$ ($\sigma > 0$) across a fixed design containing at least two distinct $x_i$ values, and the upper cutoff $c = 3$ is known. Each unit contributes the Gaussian density $\sigma^{-1}\phi((y - \beta_0 - \beta_1 x_i)/\sigma)$ on uncensored rows ($R_i = 1$, $y \le 3$) and the upper tail probability $1 - \Phi((3 - \beta_0 - \beta_1 x_i)/\sigma)$ on censored rows ($R_i = 0$). Because two Gaussian densities agreeing on $(-\infty, 3]$ have identical quadratic log-densities, the observed-data likelihood uniquely identifies $(\beta_0 + \beta_1 x_i, \sigma)$ at each $x_i$, and $\ge 2$ distinct design values uniquely identify $(\beta_0, \beta_1, \sigma^2)$.

```mermaid
flowchart LR
    X["X (fixed regressor)"] --> Y["Y (complete outcome)"]
    Y["Y (complete outcome)"] --> R["R (uncensored indicator)"]
    Y["Y (complete outcome)"] --> Y_obs["Y_obs (masked outcome)"]
    R["R (uncensored indicator)"] --> Y_obs["Y_obs (masked outcome)"]
```

## Variables and data-generating process

- **Variables and observed input.** Each row is one unit. Methods receive the three observed columns `X`, `R`, and `Y_obs`, together with the known upper censoring threshold $c = 3$ as documented task specification. For uncensored rows (`R == 1`), `Y_obs` equals $Y_i \le 3$; for censored rows (`R == 0`), `Y_obs` holds finite placeholder `0` (serialized as float `0.0`). Unobserved censored outcomes and disturbances are excluded from estimator inputs.
- **Draw order and scenarios.** Under the single scenario `original` ($n = 100$): construct $x_i = -1 + 2i/100$, draw $\epsilon_i \overset{\mathrm{iid}}{\sim} \mathcal{N}(0, 1)$, set $Y_i = 1 + 3x_i + \epsilon_i$, compute $R_i = \mathbf{1}\{Y_i \le 3\}$, and record $Y_{\mathrm{obs},i} = R_i Y_i$.

### Structural equations

- **Structural parents.** `X -> Y, Y -> R, Y -> Y_obs, R -> Y_obs`

```math
\begin{aligned}
x_i &= -1 + \frac{2i}{n}, && i = 1, \ldots, n, \quad n = 100, \\
\epsilon_i &\overset{\mathrm{iid}}{\sim} \mathcal{N}(0, 1), && i = 1, \ldots, n, \\
Y_i &= 1 + 3x_i + \epsilon_i, && \\
R_i &= \mathbf{1}\{Y_i \le 3\}, \qquad Y_{\mathrm{obs},i} = R_i Y_i.
\end{aligned}
```

Disturbances $\epsilon_i$ are i.i.d. standard normal across the fixed design points $x_1, \ldots, x_{100}$; censored observations ($Y_i > 3$, $R_i = 0$) are encoded with finite placeholder $Y_{\mathrm{obs},i} = 0$ while retaining the known upper cutoff $c = 3$ (conventional top-coded Tobit input is $R_i Y_{\mathrm{obs},i} + 3(1 - R_i)$ paired with $R_i$).

| Symbol | Meaning | Definition or setting |
| --- | --- | --- |
| $i, n$ | Unit index and sample size | $i = 1, \ldots, n$; fixed $n = 100$ from source Example 4 (`original`). |
| $x_i$ | Fixed scalar regressor | Deterministic grid $x_i = -1 + 2i/100 \in [-0.98, 1.00]$; column `X`. |
| $\epsilon_i$ | Outcome disturbance | Independent $\mathcal{N}(0, 1)$ noise across fixed design points; latent. |
| $Y_i$ | Complete Gaussian outcome | $Y_i = 1 + 3x_i + \epsilon_i$ with fixed source intercept $1$ and slope $\beta_1 = 3$; latent when $R_i = 0$. |
| $R_i$ | Uncensored response indicator | $R_i = \mathbf{1}\{Y_i \le 3\}$ for known upper cutoff $c = 3$ (expected censoring rate $18.48\%$, Poisson–binomial SD $0.02864$); column `R`. |
| $Y_{\mathrm{obs},i}$ | Observed masked outcome | Equals $Y_i$ when $R_i = 1$ and finite placeholder $0$ when $R_i = 0$; column `Y_obs`. |
| $\beta_1$ | Complete-data regression slope | $\beta_1 = \{\mathbb{E}[Y \mid x = 1] - \mathbb{E}[Y \mid x = -0.98]\}/1.98 = 3$. |

## Data-generating process and estimand

- **Estimand.** The scalar target is the complete-data regression slope $\beta_1 = 3$ (response units per covariate unit).
- **Truth check.** The structural conditional mean $\mathbb{E}[Y_i \mid x_i] = 1 + 3x_i$ gives $\beta_1 = 3$ directly. Independent verification in `verify.py` integrates the complete Gaussian first moment numerically at the grid endpoints $x = -0.98$ and $x = 1.00$ to recover $\beta_1 = 3$ within $10^{-12}$, checks the exact Poisson–binomial censoring variance, verifies elementwise $R_i = 1 \Rightarrow Y_{\mathrm{obs},i} \le 3$ safely even on empty uncensored slices, tests the censoring boundary at $Y = 3$ and $3 \pm \varepsilon$, and checks generated uncensored outcome moments.

## Benchmark comparison

- **Output and comparator.** Methods return a scalar point estimate of $\beta_1$ and a nominal 95% confidence interval where applicable using `X`, `R`, `Y_obs`, and the documented upper cutoff $c = 3$. Comparators follow the protocol: (1) complete-case least squares with nominal OLS $t_{m-2}$ interval as a truncation baseline (reporting empirical coverage), (2) censored Gaussian maximum likelihood (Tobit MLE using known $c = 3$, inverting the profile likelihood-ratio statistic with the 95% $\chi^2_1$ cutoff), and (3) Yun–Lee–Kenward adjusted profile hierarchical likelihood (inverting twice the adjusted profile log-likelihood difference using the nominal 95% $\chi^2_1$ cutoff).
- **Scoring and replication.** Evaluate all methods on 1,000 paired independent replicate tables at $n = 100$. Report bias, RMSE, empirical 95% coverage, mean interval width, Monte Carlo standard errors, valid denominators, and all failure or nonconvergence counts.

## Materials and access

- **Public materials.** The simulation design is published in Yun, Lee and Kenward (2007), [DOI](https://doi.org/10.1093/biomet/asm063) and the [PDF mirror](https://citeseerx.ist.psu.edu/document?doi=a6c166bb97a4a7deee230820b300ac48cd78c69e&repid=rep1&type=pdf), governed by publisher terms.
- **Reproduction and protected materials.** The private review archive `mdi-yun-lee-kenward-2007-tobit-upper-v1.zip` (SHA-256 `aca753f70556e8c3fc1dd9284595ead4a6e2459307fe05f846b3bcf01c7264b8`) bundles `generator.py`, `truth.py`, `verify.py`, `reproduce.py`, `collection.json`, `config.json`, `schema.csv`, `card.md`, `PROVENANCE.md`, `source_audit.json`, `requirements.txt` (`numpy==2.3.5`, `scipy==1.16.3`), check records, and `MANIFEST.json`. After verifying the manifest in Python 3.12, run:

```bash
python3 reproduce.py --scenario original --n 100 --seed 1729 --out ../yun-lee-kenward-2007-check
```

The command validates all truth, Poisson–binomial, boundary, generated-outcome, and actual-table checks and writes `observed.csv` (`X,R,Y_obs`, 100 rows) separately from `reference.json`.
