# Fixed-query CATE with an effect that is exactly zero on an interval under covariate-dependent treatment

## Research question

- **Question and intended use.** Propose a candidate for scalar CATE evaluation on the probability scale at one prespecified covariate value, in an observational design with a single measured confounder.
- **Behavior under test.** The effect of treatment on a binary outcome is a smooth cubic of one uniform covariate that is exactly zero on $[-1/2,1/3]$, positive below and negative above. Treatment probability depends on the covariate (0.4 to 0.6). This is the source's exceptional law: on a set of positive probability the treatment has no effect. The design tests pointwise CATE estimation for a small, locally flat effect on the probability scale with mild confounding.

## Study design and data source

- **Motivation and references.** Luedtke and van der Laan (2016), *Statistical inference for the mean outcome under a possibly non-unique optimal treatment strategy*, The Annals of Statistics 44(2), 713–742, [DOI](https://doi.org/10.1214/15-AOS1384); [arXiv](https://arxiv.org/abs/1603.07573). Section 8, simulation C-E, supplies the covariate law, the covariate-dependent treatment probability and the outcome probabilities below; the source reports the optimal value 0.308. The source infers the optimal value; the fixed-query CATE target, the renaming of $W$ to $X$, the implementation and the comparison are adaptations.
- **Population and sampling.** Independent synthetic individuals. Each table has $n=1000$, one of the source sizes 250, 1000 and 4000. One scenario, `source_fixed_query`, with fixed source values.

## DAG and identification

- **Variables and causal structure.** $X$ is the observed baseline covariate (source $W$), $A$ the binary treatment and $Y$ the binary outcome. $X$ affects both the treatment probability and the outcome probability, so it is a measured confounder; it also modifies the effect. There are no latent variables.
- **DAG edges.** `X -> A, X -> Y, A -> Y`
- **Assumptions.** Independent units, consistency, no interference, no unmeasured confounding given $X$, and positivity ($0.4\le P(A=1\mid X)\le0.8$) identify $\tau(x)=E[Y\mid A=1,X=x]-E[Y\mid A=0,X=x]$. No assumption is deliberately violated.

*X causes A and Y; A causes Y.*

```mermaid
block-beta
  columns 3
  space X("X (covariate)") space
  space:3
  A("A (treatment)") space Y("Y (outcome)")
  X --> A
  X --> Y
  A --> Y
```

## Variables and data-generating process

- **Variables and observed input.** One row per individual. Every method receives the columns `X,A,Y` and the same query. Outcome probabilities, potential outcomes and reference values are not given to methods.
- **Draw order and scenarios.** Per row: $X$, then $A$ given $X$, then $Y$ given $(A,X)$. Rows and tables are independent; all values are fixed source settings. The query and evaluation seeds stay in private review.

### Structural equations

- **Structural parents.** `X -> A, X -> Y, A -> Y`

```math
\begin{aligned}
X_i &\sim \mathrm{Uniform}(-1,1), && i=1,\ldots,n,\\
A_i\mid X_i &\sim \mathrm{Bernoulli}(0.5+0.1X_i),\\
h(u) &= -u^3+u^2-\tfrac13u+\tfrac1{27},\\
\bar Q(1,x) &= 0.3+h(x+\tfrac56)\,\mathbf 1\{x<-\tfrac12\}+h(x)\,\mathbf 1\{x>\tfrac13\},\\
\bar Q(0,x) &= 0.3,\\
Y_i\mid A_i,X_i &\sim \mathrm{Bernoulli}\{\bar Q(A_i,X_i)\}.
\end{aligned}
```

| Symbol | Meaning | Definition or setting |
| --- | --- | --- |
| $i,n$ | Row index and table size | $n=1000$, one of the source sizes 250, 1000 and 4000. |
| $X_i$ | Observed covariate | Column `X`; $\mathrm{Uniform}(-1,1)$ (source $W$). |
| $A_i$ | Observed binary treatment | Column `A`; $P(A_i=1\mid X_i)=0.5+0.1X_i\in(0.4,0.6)$. |
| $h(u)$ | Cubic piece | $-u^3+u^2-u/3+1/27=(1/3-u)^3$; fixed source form. |
| $\bar Q(a,x)$ | Outcome probability | As displayed; the shift $5/6$ and break points $-1/2$, $1/3$ are fixed source values. Values stay in $(0.004,0.43)$. |
| $Y_i$ | Observed binary outcome | Column `Y`; Bernoulli with probability $\bar Q(A_i,X_i)$ (source writes Binomial for a single binary draw). |
| $\tau(x)$ | CATE function | $-(x+1/2)^3$ for $x<-1/2$; $0$ on $[-1/2,1/3]$; $(1/3-x)^3$ for $x>1/3$. |
| $x_\star$ | Fixed query | One prespecified point of $(-1,1)$, fixed across tables; given in the private `config.json`. |
| $a,Y_i(a)$ | Intervention level and potential outcome | $a\in\{0,1\}$; set $A_i=a$ in the outcome law. |

## Data-generating process and estimand

- **Estimand.** $\tau(x)=\bar Q(1,x)-\bar Q(0,x)$ at the fixed query $x_\star$, on the probability scale: $P(Y(1)=1\mid X=x_\star)-P(Y(0)=1\mid X=x_\star)$. Pointwise, not an ATE or the optimal value.
- **Truth check.** `truth.py` evaluates the closed form. `verify.py` reproduces the source's optimal value 0.308 from the generator's outcome probabilities, checks the generator against the closed form, and confirms $\tau=0$ on the interval $[-1/2,1/3]$. The reference value stays private.

## Benchmark comparison

- **Output and comparator.** A scalar CATE estimate at the query and optionally a nominal 95% pointwise interval. Baselines: a logistic-regression T-learner with a flexible term in $X$ and an AIPW-based DR-learner with known-form nuisance models fitted on the same table.
- **Scoring and replication.** 1,000 independent tables at $n=1000$, identical across methods, equal weights. Report bias and RMSE with the success rate; coverage and mean length for valid intervals and the all-attempt valid-and-covering rate. Report failures separately; no seed replacement. No completed comparison is claimed.

## Materials and access

- **Public materials.** [DOI](https://doi.org/10.1214/15-AOS1384) and [arXiv](https://arxiv.org/abs/1603.07573); the paper and author code are not redistributed.
- **Reproduction and protected materials.** The standard ZIP `cate-luedtke-vdl-2016-continuous-exceptional-v1.zip` (collection.json, card.md, config.json, schema.csv, generator.py, truth.py, verify.py, requirements.txt, checks, MANIFEST.json) is available for private review. Run the collection check from the student package root:

```bash
python collect.py check path/to/cate-luedtke-vdl-2016-continuous-exceptional-v1 --run --n 128 --seed 1729
```
