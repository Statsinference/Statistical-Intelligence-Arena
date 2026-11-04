# Longitudinal two-time proximal MSM coefficient

> **Unverified extraction — scientific review required.**

**Primary area:** Proximal Causal Inference

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Andrew Ying, Wang Miao, Xu Shi, Eric J. Tchetgen Tchetgen (2023). Proximal causal inference for complex longitudinal studies. Journal of the Royal Statistical Society Series B: Statistical Methodology, 85(3), 684-704. DOI: 10.1093/jrsssb/qkad020.

**DOI:** 10.1093/jrsssb/qkad020 · **Source locator:** arXiv:2109.07030v5; PDF pp.47-48, Appendix F.1 (printed appendix pp.22-23), Eqs.(F.1)-(F.3)

## DGP / generation mechanism

**Sampling design:** Unit: individual subject (one wide row); Dependence: English description not yet supplied; consult the original scientific record (JSON).

**Generator source:** [generator.py](../generators/proximal-ying-2023-03-30-longitudinal-v1.py)

**Keywords (source-described):** Nonlinearity

**Observed variables**

X0, A0, Z0, W0, X1, A1, Z1, W1, Y, U0, U1

**Latent variables**

Not explicitly identified (review required)

**Latent-variable identification:** not explicitly specified

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

**Original source equations (verbatim):** [Open raw scientific record (JSON)](./proximal-ying-2023-03-30-longitudinal-v1.json).

定义 $`\sigma(t)=1/(1+\exp(-t))`$，所有下述高斯误差分别独立服从 $`\mathcal{N}(0,0.5^{2})`$。每个个体生成以下变量：

1. $`X_{0} \sim \mathcal{N}(-0.35,0.5^{2})`$；$`U_{0} \sim \mathcal{N}(0.35,0.5^{2})`$；两者独立。

**Step 2**

$$
A_{0} \mid  X_{0},U_{0} \sim \mathrm{Bernoulli}(\sigma(-0.5 + 0.35X_{0} - 0.35U_{0}))
$$

**Step 3**

$$
Z_{0} = 0.2 + 0.5A_{0} + 0.5X_{0} + 0.75U_{0} + \varepsilon_{Z0}
$$

**Step 4**

$$
W_{0} = 0.2 + 0.5X_{0} - 0.95U_{0} + \varepsilon_{W0}
$$

**Step 5**

$$
X_{1} = 0.2 + 0.7A_{0} + 0.7X_{0} + \varepsilon_{X1}
$$

**Step 6**

$$
U_{1} = 0.2 + 0.7A_{0} + 0.7U_{0} + \varepsilon_{U1}
$$

**Step 7**

$$
A_{1} \mid  A_{0},X_{0},X_{1},U_{0},U_{1} \sim \mathrm{Bernoulli}(\sigma(-0.5 + 0.5A_{0} + 0.35(X_{0}+X_{1}) + 0.35(U_{0}+U_{1})))
$$

**Step 8**

$$
Z_{1} = 0.2 + 0.5(A_{0}+A_{1}) + 0.5(X_{0}+X_{1}) - 0.75(U_{0}+U_{1}) + \varepsilon_{Z1}
$$

**Step 9**

$$
W_{1} = 0.35 + 0.45(X_{0}+X_{1}) - 0.85(U_{0}+U_{1}) + \varepsilon_{W1}
$$

**Step 10**

$$
Y = -1.3 + A_{1} + 1.14A_{0} + 0.5X_{1} - 0.7U_{1} + 0.2X_{0} - 0.7U_{0} + \varepsilon_{Y}
$$

除 <code>X0,U0</code> 的独立起始抽样外，时间节点所用结构误差也分别独立抽取。每名个体对应一行宽表，观测列为 <code>X0,A0,Z0,W0,X1,A1,Z1,W1,Y</code>；<code>U0,U1</code> 为内部潜在混杂。个体间独立，两个时点的观测在个体内按转移方程关联。


## Parameter scenarios, estimands and truth

| Scenario | Estimand | Definition | True value | Evidence status |
|---|---|---|---|---|
| original | beta1 | Common slope beta1 in E[Y(a0,a1)]=beta0+beta1*(a0+a1). The 11-vs-00 contrast is separately 2*beta1. | 1.0 | reported_numeric |

## Identifiability assumptions

- Consistency, no interference; IID subjects with explicitly dependent observations within subject
- Sequential latent exchangeability for treatment histories given latent U and observed X histories
- Z and W satisfy sequential proxy exclusion restrictions at each time given the relevant treatment/confounder history
- Sequential outcome bridges exist; proxy relevance/completeness conditions are those of the longitudinal proximal identification result
- Sequential positivity; Gaussian tails do not imply uniform overlap
- Independent initial X0,U0 and independent structural errors are an explicit joint-generation completion, separately disclosed as an implementation assumption

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Warnings:**

- No explicit latent-variable metadata or reliably identifiable latent declarations; absence from this list does not prove that no latent variables exist.
