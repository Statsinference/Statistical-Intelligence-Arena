# Fixed-query CATE with product-ramp qualitative heterogeneity

## Research question

- **Question and intended use.** Propose a source-grounded evaluation candidate for one scalar fixed-query CATE and an optional 95% pointwise interval. A two-sided ramp with a nonempty zero slab, multiplied by a second covariate that can change sign; not a single-variable hinge or a polynomial.
- **Behavior under test.** Preserve the source joint observed law and explicitly define the additive intervention contrast. Family membership is based on structural form; seeds and parameter variants are not additional contributions.

## Study design and data source

- **Motivation and references.** Shi, C., Lu, W., and Song, R. (2019). On Testing Conditional Qualitative Treatment Effects. The Annals of Statistics 47(4), 2348-2377. DOI: 10.1214/18-AOS1750. [Article](https://doi.org/10.1214/18-AOS1750); [source version](https://pmc.ncbi.nlm.nih.gov/articles/PMC6561732/). Exact location: Section 6 Scenario 2; PMC author manuscript NIHMS987209; original HTML MathML for Section 6, including piecewise branches, was read.
- **Population and sampling.** Independent synthetic individuals, with proposed evaluation table size $n=300$. The collection interface additionally supports other positive $n$ for checks. One declared scenario, `source_fixed_query`. Fixed query, exact parameters and seeds are available in the separate private review ZIP. This proposal is not a completed estimator comparison.
- **Adaptations.** Choose a fixed scalar CATE query before data generation; the query and reported scalar reference are defined for this contribution, not a paper-reported estimate. Use an independently authored Python/NumPy PCG64 reconstruction; no claim to identical R or MATLAB random samples. Run $n=128$ for the interface check, using the seed recorded in the private checks/report.json. The source/evaluation table size is documented separately; no method training or CI comparison is performed.

## DAG and identification

- **Variables and causal structure.** Each row contains $X_{1}$, $X_{2}$, A, $Y$. $X$ denotes the complete observed baseline covariate vector. All outcome disturbances are independent exogenous errors. No latent common cause of treatment and outcome is introduced. Latent pre-clipping draws and auxiliary noises, where used, are not supplied to methods.
- **DAG edges.** `X -> Y, A -> Y`
- **Assumptions.** Consistency, well-defined treatment versions and no interference. Independent individuals within the declared sampling design; no latent common cause of treatment and outcome after adjustment. Conditional exchangeability given all observed baseline adjustment variables. Positive treatment probability at supported queries and finite conditional means; continuous conditional response version at continuous queries. The source distribution and mechanism are fixed. Uniform overlap is supported by bounded predictors where used; randomization is exactly one half for the trial designs. Adjustment set: all $X$ columns.

```mermaid
flowchart LR
    X["X (baseline covariates)"]
    A["A (treatment)"]
    Y["Y (outcome)"]
    X --> Y
    A --> Y
```

## Variables and data-generating process

- **Variables and observed input.** The schema lists only observed numeric columns. Potential outcomes, nuisance functions and true effects stay internal. All methods receive the same table, role definitions and fixed query, with no oracle features. Treatment is A, the outcome is $Y$ and the baseline columns are $X_{1}$ through $X_{2}$.
- **Draw order and scenarios.** Baseline variables first, then treatment conditional on its stated parents, followed by independent outcome noise and observed outcome.  All source coefficients below are fixed across tables.

### Structural equations

- **Structural parents.** `X -> Y, A -> Y`

```math
\begin{aligned}
X_{i1},X_{i2}&\overset{iid}{\sim}U[-2,2],\quad A_i\sim\mathrm{Bernoulli}(1/2),\quad A_i\perp X_i,\\
b(x)&=1-(x_1-x_2)/2,\quad \phi(z)=\begin{cases}z&0\le z\le2,\\0&\delta-2\le z<0,\\2+z-\delta&-2\le z<\delta-2,\end{cases}\quad\delta=\sqrt{8\cdot0.04},\\
h(x)&=x_1\phi(x_2),\quad\mu_0(x)=b(x),\quad\mu_1(x)=b(x)+h(x),\\
\epsilon_i&\sim N(0,0.25),\quad\epsilon_i\perp(X_i,A_i),\quad Y_i=b(X_i)+A_ih(X_i)+\epsilon_i.
\end{aligned}
```

| Symbol | Meaning | Definition or setting |
| --- | --- | --- |
| $i$ | Independent individual index | One independently sampled individual per row. |
| $X_i,\ x$ | Two independent observed covariates and arguments | Columns `X1`, `X2` are independent $U[-2,2]$ draws. |
| $b,\ h,\ \phi,\ z$ | Baseline, contrast, modifier and its scalar argument | Explicit functions above; $\phi_1(x_1)=x_1$, and $z$ is the scalar modifier argument. Positive-part alternatives are not counted separately. |
| $\delta$ | Source qualitative-heterogeneity strength | Source Scenario 2: $\mathrm{VD}=0.04$, $\mathrm{VD}=\delta^2/8$; hence $\delta=\sqrt{0.32}$. |
| $\epsilon_i$ | Unobserved independent error | Independent Gaussian error with mean $0$, variance $0.25$ and standard deviation $0.5$; not exported. |
| $A_i,\ Y_i$ | Observed treatment and outcome | Treatment column `A` takes values in $\{0,1\}$; outcome column `Y` follows the law above. |
| $\mu_a$ | Intervention-specific conditional means | Defined explicitly above; internal simulator quantities are not exported. |
| $x_\star$ | Prespecified scalar-target query | Exact coordinates in private config.json; common to all methods and held fixed across tables. |
| $\tau$ | Additive conditional average treatment effect | $\mathbb{E}[Y(1)-Y(0)\mid\text{target conditioning variables at the fixed query}]$; the conditioning set is specified in the estimand section. No averaging over the fixed query. |
| $n$ | Number of observed rows | Selected source-supported evaluation size $300$; interface smoke uses $128$; no simulated estimator study is claimed. |

## Data-generating process and estimand

- **Estimand.** $\tau(x_\star)=\mathbb{E}[Y(1)-Y(0)\mid X=x_\star]$. This is one prespecified scalar difference in outcome units; identify it by adjustment for $X$. The query is fixed across repeated datasets. The pointwise coverage probability is $\Pr\{\tau(q_\star)\in C(D_n;q_\star)\}$, where $q_\star$ denotes the declared query and $C$ an interval computed from the observed dataset $D_n$. It is not a simultaneous band or a population-average effect.
- **Truth check.** Zero-mean independent noise gives $\tau(x)=x_1\phi(x_2)$. The paper studies conditional qualitative treatment effects, rather than fixed-query intervals. Independently integrating $\mathbb{E}[\tau(X)\{\mathbf{1}(\tau(X)>0)-\mathbf{1}(X_1>0)\}]$ yields $\mathrm{VD}=\delta^2/8=0.04$ at the selected source setting. A separately written scalar reconstruction and numerical integration in `verify.py` check multiple queries and structural controls. The fixed-query scalar reference stays in the private ZIP. These checks share the source specification and numerical library and do not replace independent human replication.

## Benchmark comparison

- **Output and comparator.** One scalar estimate and optionally a nominal 95% pointwise interval; baseline: An arm-specific regression T-learner with flexible spline and interaction terms on the same observed inputs. Every comparator uses the same observed table and query. This package implements generation and oracle checks only, not the comparison methods.
- **Scoring and replication.** Proposed, unexecuted plan: 1,000 independent repeated tables at $n=300$ with the same scenario, equal weights and paired data across methods. Freeze seeds and queries before evaluation. Report bias, RMSE, success/availability, 95% coverage and mean interval length for valid results, plus all-attempt valid-and-covering frequency. Comparisons of interval length require a prespecified common coverage/availability gate; the gate and estimator tuning are future evaluation work. No length ranking or coverage result is claimed here. Record all failures/timeouts/nonfinite estimates and do not replace failed seeds. A Monte Carlo standard error or binomial interval must accompany coverage; small-sample oracle checks do not establish coverage.

## Materials and access

- **Public materials.** [The Annals of Statistics article](https://doi.org/10.1214/18-AOS1750) and [source version](https://pmc.ncbi.nlm.nih.gov/articles/PMC6561732/). No original PDF or author code is redistributed. Independently authored implementation of published equations.
- **Reproduction and protected materials.** The separate cate-shi-2019-product-ramp-v1-review2.zip contains the complete eight-file student contribution, actual checks and SHA-256 manifest. Exact query, scenario-specific truths, seeds and generated samples are for private maintainer review through the submitter's agreed channel. Run `python collect.py check path/to/cate-shi-2019-product-ramp-v1 --run --n 128 --seed REVIEW_SEED` with the student tool and NumPy. Replace REVIEW_SEED by the run seed in the private checks/report.json. The recorded generation/verification environment is CPython 3.12.14 with NumPy 2.3.5. Published formula coefficients shown above are public source settings; the contribution-specific query, run seeds, generated samples and scalar reference stay in the private ZIP. No official evaluation tables have been created. Formal scientific review, independent human rerun, acceptance remain pending. AI assisted source reconstruction, code and prose; it does not sign off scientific acceptance.
