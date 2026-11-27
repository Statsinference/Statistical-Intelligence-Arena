# Fixed-query CATE with product-ramp qualitative heterogeneity

## Research question

- **Question and intended use.** Propose a source-grounded evaluation candidate for one scalar fixed-query CATE and an optional 95% pointwise interval. A two-sided ramp with a nonempty zero slab, multiplied by a second covariate that can change sign; not a single-variable hinge or a polynomial.
- **Behavior under test.** Preserve the source joint observed law and explicitly define the additive intervention contrast. Family membership is based on structural form; seeds and parameter variants are not additional contributions.

## Study design and data source

- **Motivation and references.** Shi, C., Lu, W., and Song, R. (2019). On Testing Conditional Qualitative Treatment Effects. The Annals of Statistics 47(4), 2348-2377. DOI: 10.1214/18-AOS1750. [Article](https://doi.org/10.1214/18-AOS1750); [source version](https://pmc.ncbi.nlm.nih.gov/articles/PMC6561732/). Exact location: Section 6 Scenario 2; PMC author manuscript NIHMS987209; original HTML MathML for Section 6, including piecewise branches, was read.
- **Population and sampling.** Independent synthetic individuals, with proposed evaluation table size n=300. The collection interface additionally supports other positive n for checks. One declared scenario, source_fixed_query. Fixed query, exact parameters and seeds are available in the separate private review ZIP. This proposal is not a completed estimator comparison.
- **Adaptations.** Choose a fixed scalar CATE query before data generation; the query and reported scalar reference are defined for this contribution, not a paper-reported estimate. Use an independently authored Python/NumPy PCG64 reconstruction; no claim to identical R or MATLAB random samples. Run n=128 for the interface check, using the seed recorded in the private checks/report.json. The source/evaluation table size is documented separately; no method training or CI comparison is performed.

## DAG and identification

- **Variables and causal structure.** Each row contains X1, X2, A, Y. X denotes the complete observed baseline covariate vector. All outcome disturbances are independent exogenous errors. No latent common cause of treatment and outcome is introduced. Latent pre-clipping draws and auxiliary noises, where used, are not supplied to methods.
- **DAG edges.** `X -> Y, A -> Y`
- **Assumptions.** Consistency, well-defined treatment versions and no interference. Independent individuals within the declared sampling design; no latent common cause of treatment and outcome after adjustment. Conditional exchangeability given all observed baseline adjustment variables. Positive treatment probability at supported queries and finite conditional means; continuous conditional response version at continuous queries. The source distribution and mechanism are fixed. Uniform overlap is supported by bounded predictors where used; randomization is exactly one half for the trial designs. Adjustment set: all X columns.

```mermaid
flowchart LR
    X["X (baseline covariates)"]
    A["A (treatment)"]
    Y["Y (outcome)"]
    X --> Y
    A --> Y
```

## Variables and data-generating process

- **Variables and observed input.** The schema lists only observed numeric columns. Potential outcomes, nuisance functions and true effects stay internal. All methods receive the same table, role definitions and fixed query, with no oracle features. Treatment is A, the outcome is Y and the baseline columns are X1 through X2.
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
| i | Independent individual index | One independently sampled individual per row. |
| X_i,x | Two independent observed covariates and arguments | Columns X1,X2 each uniform on [-2,2]. |
| b,h,phi,z | Baseline, contrast, modifier and its scalar argument | Explicit source functions above. phi1(x1)=x1; the positive-part alternatives are not counted separately. |
| delta | Source qualitative-heterogeneity strength | Chosen to match the source VD=.04; delta=(.12)^(2/3) for Scenario 1 or sqrt(.32) for Scenario 2; formula is source-derived. |
| epsilon_i | Unobserved independent error | Normal mean zero, variance .25, SD=.5. |
| A_i,Y_i | Observed treatment and outcome | Treatment column A in {0,1}; outcome column Y; units and generation law above. |
| mu_a or m_a | Intervention-specific conditional means | Defined explicitly above; internal simulator quantities are not exported. |
| x_star or v_star | Prespecified scalar-target query | Exact coordinates in private config.json; common to all methods and held fixed across tables. |
| tau | Additive conditional average treatment effect | E[Y(1)-Y(0)|conditioning variables at query]; no population averaging over the query. |
| n | Number of observed rows | Selected source-supported evaluation size 300; interface smoke uses 128; no simulated estimator study is claimed. |

## Data-generating process and estimand

- **Estimand.** tau(x_star)=E[Y(1)-Y(0)|X=x_star], scalar fixed-query difference in outcome units. The query is prespecified and identical across repeated tables. Coverage means P(tau(query) in CI(D_n)) with query held fixed, not a simultaneous band or an ATE.
- **Truth check.** Zero-mean independent noise implies tau(x)=x1*phi(x2). The original paper tests conditional qualitative treatment effects, rather than a scalar fixed-query CI. Besides arm-mean integration, verify.py numerically reconstructs the source value difference E[tau(X)*(I(tau(X)>0)-I(X1>0))]. With delta<=1 it equals delta^(3/2)/3 in Scenario 1 and delta^2/8 in Scenario 2, both .04 at the selected setting. A separate scalar reconstruction and numerical integration are provided in verify.py; special cases and multiple queries are checked. The scenario-specific numeric reference is reserved for the private ZIP. The two code routes share the source specification and NumPy primitives and are not independent human replication.

## Benchmark comparison

- **Output and comparator.** One scalar estimate and optionally a nominal 95% pointwise interval; baseline: An arm-specific regression T-learner with flexible spline and interaction terms on the same observed inputs. Every comparator uses the same observed table and query. This package implements generation and oracle checks only, not the comparison methods.
- **Scoring and replication.** Proposed, unexecuted plan: 1,000 independent repeated tables at n=300 with the same scenario, equal weights and paired data across methods. Freeze seeds and queries before evaluation. Report bias, RMSE, success/availability, 95% coverage and mean interval length for valid results, plus all-attempt valid-and-covering frequency. Comparisons of interval length require a prespecified common coverage/availability gate; the gate and estimator tuning are future evaluation work. No length ranking or coverage result is claimed here. Record all failures/timeouts/nonfinite estimates and do not replace failed seeds. A Monte Carlo standard error or binomial interval must accompany coverage; small-sample oracle checks do not establish coverage.

## Materials and access

- **Public materials.** [The Annals of Statistics article](https://doi.org/10.1214/18-AOS1750) and [source version](https://pmc.ncbi.nlm.nih.gov/articles/PMC6561732/). No original PDF or author code is redistributed. Independently authored implementation of published equations.
- **Reproduction and protected materials.** The separate cate-shi-2019-product-ramp-v1-review2.zip contains the complete eight-file student contribution, actual checks and SHA-256 manifest. Exact query, scenario-specific truths, seeds and generated samples are for private maintainer review through the submitter's agreed channel. Run `python collect.py check path/to/cate-shi-2019-product-ramp-v1 --run --n 128 --seed REVIEW_SEED` with the student tool and NumPy. Replace REVIEW_SEED by the run seed in the private checks/report.json. The recorded generation/verification environment is CPython 3.12.14 with NumPy 2.3.5. Published formula coefficients shown above are public source settings; the contribution-specific query, run seeds, generated samples and scalar reference stay in the private ZIP. No official evaluation tables have been created. Formal scientific review, independent human rerun, submission and acceptance remain pending. AI assisted source reconstruction, code and prose; it does not sign off scientific acceptance.
