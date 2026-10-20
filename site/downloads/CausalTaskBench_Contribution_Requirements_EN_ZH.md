# Statistical Inference Arena: Contribution Requirements / 统计推断竞技场：完整贡献规范

**Protocol / 协议 v0.3 · 2026-10-18 · Output schema / 输出格式 0.2.0 · Draft / 草案**

Legacy CausalTaskBench filenames are retained for compatibility. This bilingual version contains the same nine chapters as the standalone English and Chinese versions, including the complete student workflow.

文件名沿用 CausalTaskBench 以保持兼容。本双语版与英文、中文单语版的九章内容相同，并包含完整学生操作流程。

## 1. Purpose, first release and scope / 目标、首版范围与当前状态

**English**

The first release evaluates **confidence intervals for causal estimands**, with point estimation, availability and cost reported alongside them. The planned development sequence is: register classical data-generating processes (DGPs), define a training hyperdistribution, build a small prior-data fitted network (PFN) baseline, then evaluate its intervals on independent repetitions at fixed DGPs. This is a plan for constructing and evaluating methods; it does not presume that PFNs outperform classical estimators.

The six task categories are **ATE, CATE, mediation, instrumental variables, proximal causal inference, and DID/synthetic control**. DID and synthetic control share one collection category but require distinct scientific and uncertainty contracts. Start with one precisely specified task rather than assuming one model already supports every category.

Phase 1 prioritizes **Layer B: method evaluation**: roles, estimand, identification conditions, observed inputs and budgets are supplied. **Layer A: complete scientific analysis** is optional and may be added later with separate prompts, permissions, outputs and review. A method's numerical performance does not establish complete-analysis capability.

Current status: protocol and contributor scaffolding. The mediation reference demo, end-to-end training runner and statistical evaluator still require implementation and review. This document records no trained checkpoint, successful experiment or accepted contribution. No training is launched as part of this revision.

**中文**

首版评价**因果目标参数的置信区间**，同时报告点估计、输出可用率与成本。计划路线为：登记经典数据生成过程（DGP），定义训练超分布，建立小型先验数据拟合网络（PFN）基线，再在固定 DGP 下通过独立重复评价区间。这是一套方法构建与评测计划，不预设 PFN 优于经典估计器。

六类任务为 **ATE、CATE、中介分析、工具变量、近端因果推断、DID／合成控制**。DID 与合成控制归于同一收集类别，但科学目标与不确定性约定分别定义。先完成一个精确定义的任务，不假设一个模型已经支持全部类别。

第一阶段优先 **B 层：方法评测**，提供变量角色、目标参数、识别条件、可见输入与预算。**A 层：完整科学分析**可后续加入，使用独立的问题、权限、输出和审核。数值方法表现不能直接证明完整分析能力。

当前状态是协议与贡献模板。中介参考演示、端到端训练运行器和统计评测器仍待实现与审核。本文不代表已有训练检查点、成功实验或已接收贡献；本轮修订不启动训练。

## 2. Scientific contract for the six task categories / 六类任务的科学约定

**English**

Each task fixes its estimand, population, scale, intervention contrast, observation/assignment units, dependence, and identification assumptions before selecting a method. Record which roles and scientific facts are supplied; an observational table alone does not determine them. Pretreatment predictors are not automatically confounders.

| Category | Required target and design specification |
| --- | --- |
| ATE | Define `E[Y(1)-Y(0)]`, the target population and treatment versions. State consistency, relevant exchangeability, positivity and interference conditions; specify sampling weights or selection if applicable. |
| CATE | Define `tau(x)=E[Y(1)-Y(0) given X=x]`, the conditioning variables and a fixed query or prespecified query grid/distribution. Record support/overlap and smoothness or structural assumptions used by the estimator and its interval. A collection of pointwise intervals is not a simultaneous band. |
| Mediation | Define `NIE=E[Y(1,M(1))-Y(1,M(0))]` and complementary `NDE=E[Y(1,M(0))-Y(0,M(0))]`. State timing, consistency, treatment and mediator-outcome exchangeability, the required cross-world assumptions, treatment positivity and mediator support. The simple natural-effect route excludes treatment-induced mediator-outcome confounding. Treatment randomization alone is insufficient. |
| IV | Specify the instrument, treatment and outcome. Distinguish LATE for a declared complier population from ATE or a structural coefficient. State relevance, exclusion, instrument exogeneity and monotonicity where needed. Record instrument strength. Weak-IV-valid confidence sets can be unbounded or disconnected. |
| Proximal | Specify treatment-inducing and outcome-inducing proxy roles, latent-confounding assumptions, the bridge equation, existence/completeness and relevant positivity/integrability conditions. Define the effect functional recovered by the bridge; ordinary covariate adjustment is not a substitute. |
| DID / synthetic control | DID: define group-time or aggregate ATT, treatment timing, comparison group, no anticipation, parallel trends and any staggered-adoption restrictions. Synthetic control: define the treated-unit/time target, donor eligibility, counterfactual model and pre/post periods. Record within-unit and temporal dependence, spillovers and the assignment or sampling basis for inference. Do not reuse a generic iid interval without justification. |

The main track requests `target_object: parameter_ci` for causal effect parameters. The retained `mean_ci` format can describe an explicitly separated conditional-mean subtask. Future-response `prediction_set` outputs remain schema-compatible but are **outside this first CI comparison**.

Fix `coverage_scope` as `marginal`, `fixed_query`, `group`, `pointwise` or `simultaneous`, and write its probability statement. For a fixed-query CATE interval, the query is held fixed while datasets are repeated. A grid evaluation must specify each query and any aggregation weights; simultaneous coverage needs a versioned output/evaluator extension.

Use exact analytic truth or a numerical oracle with quantified approximation error for parameter-coverage evaluation. Real-data reference estimates are not exact truths. Semisynthetic tasks must distinguish a fixed empirical covariate pool from a superpopulation target. An assumption-violation probe must be labeled as such; a simulator's known causal target does not make it identifiable from the method's observed inputs.

**First pilot: an explicitly illustrative mediation mechanism**

The starter's `dgps/cards/mediation_illustrative.md` is a proposed teaching example, with no external-paper attribution and no implemented generator. It uses the temporal order X, A, M, Y:

```text
X ~ N(0,1)
A given X ~ Bernoulli(expit(c0 + cX*X))
M = a0 + aA*A + aX*X + eM
Y = b0 + bA*A + bM*M + bAM*A*M + bX*X + eY
NIE = aA*(bM + bAM)
NDE = bA + bAM*a0
```

These formulas assume independent mean-zero errors, the declared causal model and E[X]=0. For another population, the NDE is `bA + bAM*(a0 + aX*E[X])`. Specify noise distributions, coefficients, overlap and sampling units before implementation. The initial task targets NIE; NDE requires a separate target ID and evaluation. Independently verify these formulas and the identification assumptions before using this card as a reference demo. A mediation-specific sample-dependent teacher also needs its own derivation; renaming an ATE teacher is insufficient.

**中文**

每个任务应先固定目标参数、总体、尺度、干预对比、观测与处理分配单位、依赖结构和识别假设，再选择方法。记录哪些角色与科学事实由任务提供；仅凭观察数据表不能确定这些内容。处理前预测变量不自动等于混杂变量。

| 类别 | 必须明确的目标与设计 |
| --- | --- |
| ATE | 定义 `E[Y(1)-Y(0)]`、目标总体及处理版本。说明一致性、相关可交换性、正值性和干扰条件；适用时规定抽样权重与选择机制。 |
| CATE | 定义 `tau(x)=E[Y(1)-Y(0) given X=x]`、条件变量及固定查询点或预定查询网格／分布。记录支持与重叠，以及估计器和区间依赖的光滑性或结构假设。一组逐点区间不等于同时置信带。 |
| 中介分析 | 定义 `NIE=E[Y(1,M(1))-Y(1,M(0))]`，以及互补的 `NDE=E[Y(1,M(0))-Y(0,M(0))]`。说明时间顺序、一致性、处理和中介－结局可交换性、所需跨世界假设、处理正值性与中介支持。简单自然效应识别路线排除处理诱导的中介－结局混杂；仅随机化处理不足以识别自然效应。 |
| IV | 指定工具变量、处理和结局。区分明确依从者总体的 LATE、ATE 与结构系数。按需说明相关性、排除限制、工具变量外生性和单调性，并记录工具变量强度。弱 IV 有效置信集可能无界或不连通。 |
| 近端因果推断 | 指定处理诱导代理变量与结局诱导代理变量的角色、潜在混杂假设、桥方程、存在性／完备性及相关正值性／可积条件。定义通过桥函数恢复的效应泛函，不能用普通协变量调整替代。 |
| DID／合成控制 | DID：定义组别－时间或汇总 ATT、处理时点、比较组、无预期效应、平行趋势及分期处理限制。合成控制：定义处理单位／时点目标、供体资格、反事实模型及处理前后时期。记录单位内与时间依赖、溢出效应，以及推断所依据的分配或抽样机制；不能无理由套用一般 iid 区间。 |

因果效应主轨道使用 `target_object: parameter_ci`。保留的 `mean_ci` 格式可用于另行定义的条件均值子任务。未来响应的 `prediction_set` 输出保留格式兼容，**不属于本轮 CI 主比较**。

固定 `coverage_scope` 为 `marginal`、`fixed_query`、`group`、`pointwise` 或 `simultaneous`，并写出对应概率陈述。固定查询点 CATE 区间保持查询点不变、重复抽取数据集。网格评测须说明每个查询与汇总权重；同时覆盖需版本化输出和评测器扩展。

参数覆盖评价应采用精确解析真值，或带有量化近似误差的数值真值计算。真实数据的参考估计不是精确真值。半合成任务须区分固定经验协变量池与超总体目标。假设违背探针须明确标注；模拟器知道真实因果目标，不代表方法仅靠观察输入就能识别它。

**首个试点：明确标为教学设定的中介机制**

模板中的 `dgps/cards/mediation_illustrative.md` 是拟议教学例子，没有外部论文归属，也未实现生成器。时间顺序为 X、A、M、Y：

```text
X ~ N(0,1)
A given X ~ Bernoulli(expit(c0 + cX*X))
M = a0 + aA*A + aX*X + eM
Y = b0 + bA*A + bM*M + bAM*A*M + bX*X + eY
NIE = aA*(bM + bAM)
NDE = bA + bAM*a0
```

这些公式依赖相互独立的均值零误差、已声明因果模型及 E[X]=0。换用其他总体时，NDE 为 `bA + bAM*(a0 + aX*E[X])`。实现前还须指定噪声分布、系数、重叠及抽样单位。首个任务以 NIE 为目标；NDE 应使用独立目标编号与评测。将该说明用于参考演示前，须独立核验公式和识别假设。中介特定的样本依赖教师也需独立推导，不能仅重命名 ATE 教师。

## 3. Register classical DGPs and verify their truth / 登记经典 DGP 并核验真值

**English**

Begin by collecting established simulation settings from original methodological papers and their official code. A real-data paper is optional; a canonical synthetic setting is a valid first contribution.

For every source, record the exact paper/version and stable URL or DOI, section/page/equation/table, code repository/commit where available, and license/access terms. Trace the simulated variable equations, assignment mechanism, noise laws, coefficient values, dependence, sample sizes and target definition. If the source leaves something ambiguous, record the ambiguity and proposed resolution for scientific review.

Create one `dgps/catalog.csv` row per registered mechanism or configuration family. Link detailed equations and parameters rather than hiding them in a short label. The source ledger must distinguish:

- faithful reproduction of a published mechanism;

- an explicit modification, with each changed equation, parameter or sampling choice;

- a new stress-test mechanism, with its own rationale and validity conditions.

Record variable roles, sampling/assignment units, parameter domains and restrictions, truth class, oracle implementation and its numerical error, and version/hash. Confirm the estimand with an independent derivation or numerical implementation. For mediation, test the treatment reference level and mediator contrast; for IV, check the target population and weak-instrument regime.

Keep nuisance functions, latent variables, potential outcomes and exact effects in the generator/oracle interface. Export only permitted observed variables to the learner. The training supervisor may use oracle information to construct labels; the evaluation service may use it to score outputs. It must not enter the deployed model's input by an unnoticed column or metadata field.

Direct reuse of a public classical mechanism is a transparent starting point, **not a solution to contamination or prior exposure**. Preserve public provenance and disclose possible model exposure; the split policy in Section 4 determines what generalization claim is supportable.

**中文**

首先从原始方法论文及其官方代码收集已有模拟设定。真实数据论文并非必需；规范的合成设定可以成为首个贡献。

对每个来源记录准确论文与版本、稳定链接或 DOI、章节／页码／公式／表格、可用时代码仓库与提交版本，以及许可和访问条件。追溯变量方程、处理分配机制、噪声分布、系数、依赖结构、样本量及目标定义。原文若有歧义，应记录歧义和拟议解释，交由科学复核。

在 `dgps/catalog.csv` 中为每个已登记机制或配置族建立一行，并链接详细方程和参数，不以简短名称代替。来源记录应区分：

- 对已发表机制的忠实复现；

- 明确修改，逐项列出变化的方程、参数或抽样方式；

- 新增压力测试机制，说明其理由与有效性条件。

记录变量角色、抽样／分配单位、参数范围与限制、真值等级、真值实现和数值误差，以及版本与校验和。通过独立推导或数值实现核验目标。中介任务应检查结局处理参考水平和中介对比方向；IV 应检查目标总体及弱工具变量设定。

辅助函数、潜变量、潜在结果及真实效应保留在生成器／真值接口，仅向学习器导出允许的观察变量。训练监督端可用真值信息构造标签；评测端可用其评分，但不能通过隐蔽列或元数据进入部署模型输入。

直接复用公开经典机制是透明的起点，**不等于已经解决污染或预训练暴露问题**。保留公开来源记录并披露模型可能见过的内容；第4章的划分约定决定可支持何种泛化结论。

## 4. From the DGP registry to a training hyperdistribution / 从 DGP 登记表构造训练超分布

**English**

Define the hyperdistribution **conditional on a task/estimand k**. Let F identify a registered mechanism family for that task and eta its admissible configuration:
```text
(F, eta) given k ~ Pi_k
P = P_(k,F,eta)
n ~ pi_n(. given k,F,eta)
D_n ~ SamplingDesign(P,n)
```
For iid individual sampling, the final step is `D_n ~ P^n`; panel, cluster and network designs require their declared sampler. Pi_k is a distribution over mechanisms/configurations, not the empirical distribution of rows in one table.

In `hyperdistribution.yaml`, specify task/target ID, mechanism mixture weights, parameter ranges and distribution shapes, dependence among parameters, validity constraints/rejection rules, n distribution, unit of sampling, output roles and the label-oracle reference. Mixture weights must sum to one over included mechanism families. A first mediation pilot may use a single task and mechanism family. If constraints reject sampled configurations, record how rejection changes the effective distribution.

For each sampled P, draw one or more datasets and obtain supervision `T_k(P,D_n)`. State whether labels are the fixed target `theta_k(P)`, a sample-dependent estimator/teacher, a variance quantity or an error-distribution target. Record how labels are computed and what randomness they include. Repeated datasets from the same P and draws of new P have separate IDs/seeds. An eventual joint model may add a task mixture, but must condition on task/target and roles or use explicit heads/adapters. Do not mix six estimands into an unlabelled scalar output or assume the table tells the model which effect to estimate.

Freeze three uses: **training** for shared weights, **development** for selecting the hyperdistribution, architecture, teacher and CI rules, and **evaluation** for final comparisons. State permitted public access and model-pretraining exposure. Distinguish held-out seeds, parameter regions, functional mechanisms, source-DGP families and entire task categories. Seed holdout tests new datasets; it does not establish mechanism or task transfer. Specify which sources remain public even when configurations or labels are restricted.

Classic DGPs used in training may also define an explicitly labeled in-distribution evaluation on fresh datasets. Stronger transfer claims require an appropriate holdout and exposure audit. Repeated evaluation feedback must not silently become development data; changing choices after evaluation requires a documented new development cycle and fresh evaluation assets.

**中文**

应**针对具体任务／目标 k**定义超分布。令 F 表示该任务下已登记机制族，eta 表示其允许配置：
```text
(F, eta) given k ~ Pi_k
P = P_(k,F,eta)
n ~ pi_n(. given k,F,eta)
D_n ~ SamplingDesign(P,n)
```
独立个体抽样时，最后一步为 `D_n ~ P^n`；面板、聚类及网络设计使用各自抽样器。Pi_k 是机制／配置上的分布，不是单张表中观测行的经验分布。

在 `hyperdistribution.yaml` 中指定任务／目标编号、机制混合权重、参数范围及分布形状、参数间依赖、有效性约束／拒绝规则、n 的分布、抽样单位、输出角色及标签真值接口。纳入机制族的权重之和须为1。首个中介试点可只用一个任务和机制族。若约束导致拒绝配置，须记录这如何改变实际抽样分布。

对每个抽取的 P 生成一个或多个数据集，并得到监督 `T_k(P,D_n)`。说明标签是固定目标 `theta_k(P)`、依赖当前样本的估计器／教师、方差量，还是误差分布目标；记录计算过程及包含的随机性。同一 P 的重复数据与抽取新 P 应有独立编号和种子。将来若构建联合模型，可再增加任务混合，但须提供任务／目标与角色条件，或使用明确的分头／适配器。不能把六类目标混成无标识的标量输出，也不能假设数据表自动告诉模型应估计哪个效应。

冻结三类用途：**训练**用于共享权重；**开发**用于选择超分布、架构、教师与 CI 规则；**评测**用于最终比较。说明允许公开的资源及模型预训练暴露。区分留出种子、参数区域、函数机制、来源 DGP 族及整个任务类别。种子留出只测试新数据集，不证明机制或任务迁移。即使配置或标签受限，也须明确哪些来源仍公开。

训练使用的经典 DGP 可以用于明确标注的分布内评测，只要使用新数据集。更强迁移主张需要匹配的留出设计与暴露审计。不能悄悄将反复获得的评测反馈当作开发数据；评测后修改选择，应记录新开发周期并使用新的评测资源。

## 5. Small-PFN baseline and interval construction / 小型 PFN 基线与区间构造

**English**

A small-PFN baseline is a planned, budgeted prototype, not an already trained model. Start from a shared architecture/adapter where appropriate, then document the changes required by the task: variable-role encoding, table/context structure, treatment or query specification, target normalization, output head, teacher and loss. Distinct targets need not require distinct backbones, but a shared backbone does not automatically support new estimands. Do not turn a mediator into an ordinary adjustment covariate and call the result NIE.

The training configuration and checkpoint metadata must record: architecture and parameter count; depth, width, attention and input masking where relevant; output/teacher/loss definition; code and DGP registry versions; hyperdistribution hash; model and data seeds; fresh-versus-cached task sampling; number of distinct tasks and presentations; sample-size distribution; optimizer, updates/epochs, batch size, stopping/selection rule; hardware, precision, budget and checkpoint hash. A numerical training-task count is a declared budget, not a universal scientific requirement.

The model receives observed data, explicit task/target ID, role mapping and permitted query metadata, including x for CATE. Oracle quantities can supervise offline training or serve the evaluator, but cannot appear as inference inputs. Freeze the checkpoint and method-selection rule before final evaluation. Shared weights can then be reused across new datasets; per-table nuisance fitting or calibration is an additional online step and must be recorded.

Declare exactly how an interval is produced. Options may include a native model uncertainty output, calibrated estimation-error quantiles, a bootstrap that reruns the relevant procedure, or an influence-function/one-step correction with a variance estimator. Each requires target- and design-specific justification. No particular teacher, FSP objective or EIF construction is mandatory. For nonregular or weakly identified targets, ordinary Wald or bootstrap intervals may be inadequate.

If a variance head is used, define its exact target: the estimator's sampling variance, an asymptotic variance coefficient to be divided by n, a conditional teacher-label variance, or a predictive variance are different objects. State any n scaling and how the point and variance outputs form an interval. A variance head and a positive output transform do not establish coverage.

A learned distribution over training labels is not automatically the frequentist sampling law of the deployed estimator at fixed P. Native credible intervals retain their label; their repeated-sampling coverage is evaluated rather than assumed. Record `native_frozen`, `adapted` or `refit`, and list calibration, correction, resampling or fine-tuning steps. Frozen weights alone do not imply a single forward pass.

Every task supplies a runnable classical/reference baseline and at least one PFN adapter entry. If an existing PFN cannot support the task, return `unsupported` with model/version and a concrete reason. Contributors need not independently pretrain a model for every method; team training can follow a reviewed training plan. Classical-best or PFN-better claims must be limited to the observed regime, budgets and metrics.

**中文**

小型 PFN 基线是有预算的原型计划，不是已训练模型。适当复用共享架构或适配器，再记录任务所需变化：变量角色编码、数据表／上下文结构、处理或查询定义、目标标准化、输出头、教师与损失。不同目标未必需要不同主干，但共享主干不会自动支持新目标。不能把中介当普通调整协变量，再把结果称为 NIE。

训练配置与检查点元数据须记录：架构和参数量；适用时的层数、宽度、注意力及输入掩码；输出／教师／损失；代码与 DGP 登记版本；超分布校验和；模型和数据种子；任务是重新生成还是缓存复用；不同任务数量与总呈现次数；样本量分布；优化器、更新次数／轮次、批量、停止与选择规则；硬件、精度、预算及检查点校验和。训练任务数量是声明的预算，不是通用科学门槛。

模型输入含观察数据、明确的任务／目标编号、角色映射及允许的查询元数据，CATE 须提供查询 x。真值信息可以用于离线监督或评测，不能进入推断输入。最终评测前冻结检查点与方法选择规则。共享权重随后可在新数据集复用；逐表辅助函数拟合或校准是额外在线操作，须单独记录。

明确区间的具体构造方式。可选方案包括模型原生不确定性输出、校准估计误差分位数、完整重跑相关流程的自助重抽样，或影响函数／一步修正及其方差估计。每种方案都需针对目标和设计论证，不强制某种教师、FSP 目标或 EIF 构造。非正则或弱识别目标下，一般 Wald 或 bootstrap 区间可能不适用。

若使用方差头，须定义其准确目标：估计器的抽样方差、需要除以 n 的渐近方差系数、教师标签的条件方差、未来结果的预测方差是不同对象。说明 n 的缩放，以及点估计和方差输出如何构成区间。方差头及正值变换本身不证明覆盖。

训练标签的学习分布，不自动等于固定 P 下部署估计器的频率学抽样分布。模型原生可信区间保留其名称，重复抽样覆盖需实测而非默认成立。记录 `native_frozen`、`adapted` 或 `refit`，列出校准、修正、重抽样和微调操作。权重冻结不等于仅一次前向传播。

每个任务须有可运行经典／参考基线及至少一个 PFN 适配器记录。若现有 PFN 无法支持任务，应返回 `unsupported`，给出模型、版本与具体原因。不要求贡献者为每个方法独立预训练；团队训练可在训练计划通过审核后开展。传统方法最优或 PFN 更好的结论须限定于有证据的设定、预算和指标。

## 6. Required package and interface boundaries / 必交任务包与接口边界

**English**

Keep the legacy starter paths compatible and add the scientific/training specification files below. A path in this table is a required template or eventual contribution artifact, not evidence that an executable runner already exists.

| Path | Required content |
| --- | --- |
| `task.yaml`, `task.md`, `scientific_spec.md` | Protocol/task version, owners, selected category, target/object/scope, identification, units, permitted inputs and budgets; optional Layer A separately. |
| `dgps/catalog.csv` and linked mechanism specifications | Exact source/page/equation/code version, reproduction differences, rights, parameters, roles, sampling, target/oracle and truth checks. |
| `hyperdistribution.yaml` | Task-conditioned Pi_k hierarchy, mechanism weights, configuration distributions/constraints, n, sampling units, label oracle and train/development/evaluation splits. |
| `configs/train.yaml` | Planned architecture, role/query mapping, teacher/head/loss, seeds, task sampling, optimizer, compute and checkpoint-selection budget. |
| `data/`, `environment/` | Observed-input dictionary, generator/access and hashes; pinned execution environment and bounded commands once implemented. |
| `solution/methods.json`, `methods/` or declared implementation paths | Classical reference, PFN adapter, support status, interval construction, execution mode and actual entrypoints when implemented. |
| `configs/evaluate.yaml`, `evaluation/protocol.yaml`, `evaluation/result.schema.json`, seed ledger | Fixed-DGP/n/query grid, R, paired seeds, CI evaluator, truth join, coverage gate, failure policy and positive/incorrect controls. |
| `reports/`, `review/`, `PROVENANCE.md`, `LICENSE.md` | Actual run outputs/logs/costs when available; AI findings, scientific review, independent rerun, exposure audit, rights and versions. |

Each catalog entry needs stable IDs and links to details; blank fields require an explicit unresolved item. New configuration files do not execute training by themselves. A proposed training interface takes a train config and produces weights plus metadata; a proposed evaluation interface takes frozen methods, fixed DGP configs and a seed ledger and produces per-replicate outputs plus summaries. **Those are interface requirements, not runnable commands supplied by this protocol.**

The existing output schema remains **0.2.0**; protocol version **0.3** does not rename the JSON schema. Each result identifies task/version, mechanism, replicate, method, target, query/group when applicable, status, estimate, uncertainty, diagnostics, evidence, cost and provenance. `uncertainty.coverage_scope` is mandatory, including for point-only or unsupported outputs, and describes the requested scope rather than proving coverage.

The core CI format contains one connected interval, possibly unbounded through `-inf`/`+inf` string endpoints. Empty/disconnected parameter confidence sets, simultaneous bands, vector effects and identified sets require explicit extensions; do not relabel them `prediction_set` or silently take a convex hull. The compatible `prediction_set` type can use disjoint `intervals`, but is outside the main CI track.

An `ok` scalar parameter output needs a finite estimate; point-only outputs use uncertainty `none` and do not enter interval-length comparisons. Non-ok statuses `unsupported`, `abstained`, `failed`, `not_identified` retain reason and IDs with null estimate and uncertainty `none`. JSON NaN/Infinity are rejected. Structure validation is distinct from execution and scientific validation.

**中文**

保留原模板路径兼容，并补充下列科学与训练配置文件。表中路径表示必交模板或最终贡献产物，不证明对应运行器已经存在。

| 路径 | 必交内容 |
| --- | --- |
| `task.yaml`、`task.md`、`scientific_spec.md` | 协议／任务版本、负责人、任务类别、目标／对象／范围、识别、单位、允许输入和预算；可选 A 层单独定义。 |
| `dgps/catalog.csv` 及链接的机制说明 | 准确来源／页码／公式／代码版本、复现差异、权限、参数、角色、抽样、目标／真值接口与核验。 |
| `hyperdistribution.yaml` | 任务条件下 Pi_k 层次、机制权重、配置分布与约束、n、抽样单位、标签真值接口，以及训练／开发／评测划分。 |
| `configs/train.yaml` | 拟议架构、角色／查询映射、教师／输出头／损失、种子、任务抽样、优化器、计算与检查点选择预算。 |
| `data/`、`environment/` | 观察输入字典、生成器或数据入口及校验和；锁定环境，以及实现后可运行的有界命令。 |
| `solution/methods.json`、`methods/` 或明确声明的实现路径 | 经典参考方法、PFN 适配器、支持状态、区间构造、执行方式，以及实现后的实际入口。 |
| `configs/evaluate.yaml`、`evaluation/protocol.yaml`、`evaluation/result.schema.json`、种子清单 | 固定 DGP／n／查询网格、R、配对种子、CI 评测器、真值关联、覆盖门槛、失败规则及正反对照。 |
| `reports/`、`review/`、`PROVENANCE.md`、`LICENSE.md` | 可用时的真实运行输出／日志／成本；AI 发现、科学复核、独立重跑、暴露审计、权限与版本。 |

每条登记须有稳定编号和详细说明链接，空缺字段须列为明确未决项。新增配置文件本身不会执行训练。拟议训练接口读取训练配置，输出权重和元数据；拟议评测接口读取冻结方法、固定 DGP 配置及种子清单，输出逐重复结果与汇总。**这些是接口要求，不是本协议已提供的可执行命令。**

现有输出格式版本仍为 **0.2.0**；协议 **0.3** 不等于 JSON 格式升级。每条结果记录任务／版本、机制、重复、方法、目标、适用时的查询／分组、状态、估计、不确定性、诊断、证据、成本和来源。`uncertainty.coverage_scope` 始终必填，包括仅点估计或不支持的输出；它描述请求范围，不证明覆盖成立。

核心 CI 格式只包含一个连通区间，可通过 `-inf`／`+inf` 字符串端点表示无界。空或不连通参数置信集、同时置信带、向量效应和识别集需明确扩展，不能改标 `prediction_set` 或静默取凸包。兼容的 `prediction_set` 类型可使用不连通 `intervals`，但不进入 CI 主轨道。

`ok` 的标量参数输出须有有限估计；仅点估计使用不确定性 `none`，不进入区间长度比较。非 ok 状态 `unsupported`、`abstained`、`failed`、`not_identified` 保留原因与编号，估计为空且不确定性为 `none`。拒绝 JSON NaN/Infinity。结构验证、执行验证与科学验证是不同环节。

## 7. CI evaluation at fixed DGPs / 固定 DGP 下的 CI 评测

**English**

Freeze an evaluation grid of mechanism configurations, n and targets/queries. Within each cell, hold P and its true parameter fixed, generate R independent datasets using the declared sampling/assignment design, and rerun the complete allowed method. Pair methods on the same dataset/seed and, when relevant, the same query grid. A different random P in every repetition measures a mixture-average property, not coverage at a fixed DGP; report that separately.

Prespecify R, seeds, nominal levels, tolerances, tuning rules, timeouts and checkpoint status. Respect the independent unit: clusters, panels or networks may require whole-unit resampling, dependence-aware procedures, or a specified assignment experiment. Do not bootstrap rows merely because the input is tabular. Separate variation from dataset sampling, model-training seeds and numerical truth approximation.

Match **total observed-label budgets** across methods. Disclose context, calibration, tuning and any other held-out allocation; calibration labels are not free extra data. A different-budget comparison must be separately labeled. Classical reference tuning and PFN adaptation need explicit access and compute rules.

Report bias/RMSE, empirical estimator variance, reported variance/SE calibration when supplied, CI coverage and length, availability, failures and cost. A narrow interval with poor coverage is not an improvement. Before results, register `coverage_basis` (`valid_output` or `all_attempt_valid_covering`), its denominator, availability/failure requirements, nominal level, allowed undercoverage tolerance, confidence-bound method/level and gate. Selective abstention cannot pass solely through coverage among successes. No universal cutoff or minimum R is prescribed.

Compare interval lengths only among methods passing the same target/scope coverage gate; show overcoverage and availability alongside length. Insufficient Monte Carlo precision is inconclusive. Report every scheduled attempt, including unsupported, abstained, failed, timeout, nonfinite and infrastructure errors; predeclare retry rules. Retain unbounded intervals in length summaries. No global combined score is defined.

For independent binary repetition indicators, coverage MCSE is approximately `sqrt(p*(1-p)/R)`; p=0.95 and R=1000 gives about 0.0069, a planning example only. Report a prespecified binomial interval or a design-appropriate alternative. For CATE, query-specific coverage can use independent datasets at each fixed query; pooled query indicators within a dataset are dependent. Use independent-replicate/design-aware uncertainty for grid summaries and paired method differences, not an artificial binomial denominator of R times the number of queries.

Separate offline pretraining/development cost, loading and warmed end-to-end per-dataset cost. Warmed time includes preprocessing, fitting, calibration/correction, all model calls, interval construction and output. Record hardware, precision, threads, batching, warmup, repetitions and memory; pure forward time is supplementary. Optional later diagnostics include size distortion, skewness, tail behavior and coverage error versus n. Higher-order rate claims require a target-specific argument and adequate empirical precision.

**中文**

冻结由机制配置、n 和目标／查询组成的评测网格。每个单元内保持 P 及其真实参数不变，按规定抽样／分配设计生成 R 个独立数据集，并完整重跑允许的方法。各方法使用相同数据集与种子，适用时共用查询网格。若每次重复都抽取不同 P，评价的是混合平均性质，不是固定 DGP 覆盖，应分开报告。

预定 R、种子、名义水平、容差、调参规则、超时与检查点状态。尊重独立单位：聚类、面板或网络可能需要整单位重抽样、依赖感知流程或特定分配实验。不能因为输入是表格就按行 bootstrap。区分数据抽样、模型训练种子与数值真值近似造成的变化。

各方法须匹配**观察标签总预算**，披露上下文、校准、调参及其他留出分配；校准标签不是免费额外数据。不同预算比较应另行标注。经典参考调参与 PFN 适配均需明确数据权限与计算规则。

报告偏差／RMSE、估计器经验方差、可用时的报告方差／SE 校准、CI 覆盖和长度、可用率、失败及成本。覆盖不足的窄区间不构成改进。结果出现前登记 `coverage_basis`（`valid_output` 或 `all_attempt_valid_covering`）、对应分母、可用率／失败要求、名义水平、欠覆盖容差、置信界方法／水平及门槛。不能通过选择性弃答，仅靠成功输出中的覆盖率过关。这里不规定通用阈值或最低 R。

只有通过相同目标／范围覆盖门槛的方法才能比较区间长度，同时展示过覆盖和可用率。蒙特卡洛精度不足视为结论不充分。报告全部计划尝试，包括不支持、弃答、失败、超时、非有限输出和基础设施故障，预定重试规则。长度汇总保留无界区间，不定义全局综合分数。

独立二项重复指标的覆盖率 MCSE 约为 `sqrt(p*(1-p)/R)`；p=0.95、R=1000 时约为0.0069，仅作预算示例。报告预定二项区间或适合设计的替代方法。CATE 在每个固定查询点可用独立数据集评价覆盖；同一数据集内多个查询指标相依。网格汇总与配对方法差异应采用独立重复或设计感知的不确定性，不能将 R 乘查询数量充当独立二项分母。

分开报告离线预训练／开发、加载和预热后逐数据集端到端成本。预热后成本包括预处理、拟合、校准／修正、全部模型调用、区间构造及输出。记录硬件、精度、线程、批处理、预热、重复与内存；纯前向传播耗时仅作补充。后续可选诊断包括实际显著性水平偏离、偏度、尾部行为与覆盖误差随 n 的变化。高阶收敛速度主张需针对目标的论证与足够评测精度。

## 8. Complete student contribution walkthrough / 完整学生贡献操作流程

**English**

Follow these steps for one selected task. This chapter contains the complete workflow; the separate student walkthrough is a convenient copy. Record planned work as planned, and attach execution evidence only after the relevant implementation exists.

**8.1 Copy the template and claim one task**

Copy the current contributor starter into a separate task directory. Select `ate`, `cate`, `mediation`, `iv`, `proximal` or `did_sc`; choose a specific estimand and scientific owner. The current starter is scaffolding. **A runnable mediation reference demo is still to be implemented**; once reviewed, it can become the worked example for later students. Do not describe copying the template as reproducing a successful experiment. Deliver a short proposal with target, population, available source and planned evidence.

**8.2 Read the original source and register the mechanism**

Read the original method paper and official simulation code, not only a summary. Fill the catalog's source version, page/equation, code commit, rights and reproduction differences. Transcribe the variable equations, parameters, assignment and noise laws, sampling unit and target into a reviewable specification. Mark unresolved details rather than guessing a paper's implementation. If starting from a new canonical example, label it as newly specified rather than falsely attributing it to a paper.

**8.3 Implement observed data and independently check truth**

Implement the registered DGP and a separate truth calculation. Check units, signs, intervention levels and sampling dependence on small deterministic inputs or analytically tractable configurations. Verify source-faithful and modified versions separately. Export only observed variables; keep oracle labels in separate artifacts. Record approximation error and what the independent check shares with the primary implementation. Deliver generator/oracle code plus evidence; this step is not yet a PFN experiment.

**8.4 Configure Pi_k and freeze data-use splits**

Fill `hyperdistribution.yaml` for the selected task: registered mechanism IDs, normalized weights, admissible parameter distributions, constraints, n and sampling design, and label-oracle path. Define separate training, development and evaluation registries/seeds. Declare whether evaluation is in-distribution, parameter-held-out, mechanism-held-out or task-held-out. A small single-family mediation pilot is sufficient as a first plan. Deliver a sampling specification with examples of valid and rejected configurations; no training command is implied.

**8.5 Update roles, target, teacher, head and CI rule**

Map observed columns to the selected causal roles and make task/target ID explicit; add the fixed x or grid for CATE. Specify the teacher in `configs/train.yaml`: true target, reviewed sample-dependent teacher or estimator distillation are different choices. Update the output head/loss and interval construction to match it. Record architecture and masking changes. Check that oracle information is used only for supervision/evaluation. A new target requires a justified adapter, not a renamed output field.

**8.6 Implement the classical reference and PFN adapter**

Register both in `solution/methods.json`. Implement a suitable classical estimator and interval before comparing the PFN. Give both the same target and observed-label budget; disclose calibration/tuning splits and fitting rules. An existing unsupported PFN returns its precise limitation. Specify native-frozen, adapted or refit operation and record every correction or resampling step. Deliver real entrypoints and a pinned environment once implemented; do not fill them with invented commands or results.

**8.7 Run available structural checks, then an implemented smoke test**

The following commands are currently available from the starter directory:
```sh
python validate_submission.py --mode scaffold
python evaluation/check_contract.py
python validate_submission.py --mode submission
```
The unfinished starter should pass the first two and fail submission mode. These checks do not execute estimators or validate new YAML scientific content. Once generator, methods and evaluator are implemented, add an explicitly documented bounded smoke run and positive/incorrect controls. A smoke pass establishes plumbing, not CI coverage. Preserve actual logs and unresolved errors.

**8.8 Prepare small-scale training for a later execution stage**

After scientific and implementation review, freeze the pilot architecture, task sampling, teacher, optimizer, seeds, task/update budget and checkpoint-selection rule. The future training interface is: reviewed train configuration to checkpoint plus metadata and logs; **an executable training entrypoint is not supplied here**. This revision starts no training. Once that later stage is implemented and training-ready, record actual unique tasks, presentations, elapsed cost, failures and selected checkpoint. Do not infer training success from a completed configuration.

**8.9 Evaluate CI procedures on paired independent repetitions**

Freeze the checkpoint/methods and evaluation registry. For each fixed DGP and n, independently generate the registered R datasets and run both full procedures on each dataset; keep CATE queries fixed as declared. The future evaluator must produce per-replicate results, truth joins and design-aware summaries; **no statistical evaluation runner is supplied here**. Report gate basis/denominators, coverage MC intervals, length after the gate, point/variance calibration, every failure and separated costs. Do not average over changing P and call it fixed-DGP coverage.

**8.10 Complete AI pre-review and scientific/independent review**

Record the AI tool/version/date, reviewed artifacts, findings, fixes and unresolved issues. Ask a scientific reviewer to check the source reconstruction, target/identification, oracle, hyperdistribution and CI design. Have a person independent of evaluated-model development rerun the implemented workflow in a clean environment; same-team reviewers are allowed with documented independence and conflicts. AI agreement or a structural pass is not scientific acceptance.

**8.11 Freeze the contribution and state its actual milestone**

Package the specifications, code, rights, version/hashes, seed/split ledger, model exposure, actual checkpoint metadata if any, run evidence and review disposition. Use the milestones below and list remaining work. A proposal may be submitted for review before training; an unsupported PFN remains a documented capability limit. Submission format and scientific readiness are distinct, and no live acceptance service is asserted.

**中文**

针对选定任务按以下步骤操作。本章包含完整流程，单独学生指南是便于使用的副本。计划工作标为计划；相应实现存在并实际运行后，再附执行证据。

**8.1 复制模板并认领一个任务**

将当前贡献模板复制到独立任务目录，选择 `ate`、`cate`、`mediation`、`iv`、`proximal` 或 `did_sc`，固定具体目标与科学负责人。当前模板只是结构起点，**可运行中介参考演示仍待实现**；审核完成后才可作为后续学生的操作样例。复制模板不等于复现成功实验。先交简短提案，写明目标、总体、可用来源和计划证据。

**8.2 阅读原始来源并登记机制**

阅读原始方法论文与官方模拟代码，而不只读摘要。填写来源版本、页码／公式、代码提交、权限及复现差异，将变量方程、参数、分配与噪声分布、抽样单位和目标写成可审查说明。未决细节应明确标注，不猜测论文实现。若从新定义的规范例子起步，应标为新设定，不能虚构论文归属。

**8.3 实现观察数据并独立核验真值**

实现已登记 DGP 与独立真值计算，在小型确定输入或可解析配置上检查单位、符号、干预水平及抽样依赖。忠实复现版与修改版分别核验。仅导出观察变量，真值标签保存为独立产物。记录近似误差，以及独立核验与主实现共享哪些环节。交付生成器／真值代码及核验证据；此步还不是 PFN 实验。

**8.4 配置 Pi_k 并冻结数据用途划分**

为选定任务填写 `hyperdistribution.yaml`：机制编号、归一化权重、允许参数分布、约束、n 和抽样设计，以及标签真值路径。分别建立训练、开发和评测登记与种子，声明评测是分布内、参数留出、机制留出还是任务留出。首个计划可以只是单族小型中介试点。交付抽样说明及有效／拒绝配置例子，不表示已经可以运行训练命令。

**8.5 更新角色、目标、教师、输出头和 CI 规则**

将观察列映射到选定因果角色，明确任务／目标编号；CATE 增加固定 x 或查询网格。在 `configs/train.yaml` 中说明教师：真实目标、经审核的样本依赖教师与估计器蒸馏是不同选择。同步调整输出头／损失及区间构造，记录架构与掩码变化。确认真值信息仅用于监督／评测。新增目标需要有理由的适配器，而非改一个输出字段名。

**8.6 实现经典参考方法与 PFN 适配器**

在 `solution/methods.json` 登记两者。比较 PFN 前，先实现合适的经典估计器及区间。两者使用相同目标和观察标签预算，披露校准／调参划分及拟合规则。现有 PFN 不支持时返回具体限制。声明原生冻结、适配或逐表拟合，记录每个修正和重抽样步骤。实现后再填写真实入口和锁定环境，不填虚构命令或结果。

**8.7 运行现有结构检查，再运行已实现的冒烟测试**

从模板目录可以运行以下现有命令：
```sh
python validate_submission.py --mode scaffold
python evaluation/check_contract.py
python validate_submission.py --mode submission
```
未完成模板应通过前两项，并在提交模式失败。这些检查不执行估计器，也不验证新增 YAML 的科学内容。生成器、方法和评测器实现后，再补充明确记录的有界冒烟运行及正反对照。冒烟通过说明流程接通，不证明 CI 覆盖。保留真实日志与未解决错误。

**8.8 准备后续阶段的小规模训练**

科学与实现审核后，冻结试点架构、任务抽样、教师、优化器、种子、任务／更新预算及检查点选择规则。未来训练接口为：经审核的训练配置输入，输出检查点、元数据及日志；**此处未提供可执行训练入口**。本轮不启动训练。后续实现达到训练就绪后，记录实际不同任务数、呈现次数、耗时、失败与选中检查点。配置填写完成不代表训练成功。

**8.9 通过配对独立重复比较 CI**

冻结检查点／方法及评测登记。在每个固定 DGP 与 n 下，独立生成已登记的 R 个数据集，在每个数据集上运行两种完整流程；CATE 查询按约定保持固定。未来评测器须输出逐重复结果、真值关联及匹配设计的汇总；**此处未提供统计评测运行器**。报告覆盖门槛口径与分母、MC 区间、通过门槛后的长度、点估计／方差校准、全部失败及分项成本。不能将变化 P 的平均结果称为固定 DGP 覆盖。

**8.10 完成 AI 预审、科学复核与独立重跑**

记录 AI 工具／版本／日期、审查产物、发现、修复和未决项。科学复核检查来源重建、目标与识别、真值、超分布及 CI 设计。由独立于被评模型开发的人在干净环境重跑已实现流程；同团队审核可行，但须记录独立性及冲突。AI 一致意见或结构通过不等于科学接收。

**8.11 冻结贡献并声明实际里程碑**

打包科学说明、代码、权限、版本／校验和、种子／划分清单、模型暴露、实际存在的检查点元数据、运行证据及审核结论。按下列里程碑声明状态，列明未完成工作。提案可以在训练前提交审核；PFN 不支持仍属于明确能力限制。提交格式与科学完成度不同，本文不宣称已有在线接收服务。

## 9. Completion, review and staged milestones / 完成标准、审核与分阶段里程碑

**English**

Use a staged contribution process so students can submit a rigorous proposal before training. Reviewers assess the evidence for the declared milestone rather than treating a completed template as an implemented method.

| Milestone | Evidence required |
| --- | --- |
| Proposal | A selected task/estimand, source ledger, assumptions, truth plan, Pi_k, proposed baseline/PFN adapter, CI design, split policy and budget. Unresolved items and implementation owners are explicit. |
| Reference-demo-ready | An implemented generator and checked truth oracle; a runnable classical reference and declared PFN support/adapter; an implemented output/evaluation path; reproducible public smoke evidence and an environment. An unsupported PFN is recorded as a limit. |
| Training-ready | Reviewed input/teacher/head/loss definitions, executable training plumbing with bounded checks, frozen architecture/hyperdistribution, train/development splits, seeds, budget and checkpoint-selection plan. This status does not claim completed training. |
| Statistically validated | Actual frozen methods/checkpoints where used, paired fixed-DGP repetitions, target-appropriate coverage uncertainty and gates, lengths, failures/availability and costs, together with scientific review and independent rerun evidence. Claims are limited to the evaluated domain. |

The current protocol and starter are **draft specifications**. The mediation demo, training and statistical evaluation have not attained these implementation/validation milestones merely because templates are provided.

The final review package must answer the following checklist:

- Is the task/target/role/query contract explicit, with the required identification and sampling conditions?

- Can each DGP, source version, reproduction change and oracle be traced and independently checked?

- Are Pi_k, teacher labels and model inputs distinguished, with oracle information excluded from deployment inputs?

- Are train/development/evaluation uses, holdouts, model exposure and seed ledgers frozen and disclosed?

- Are the classical reference and PFN support/adapter documented with real entrypoints where implemented, environment and method mode?

- Are interval construction, observed-label budgets, fixed-DGP repetitions, MC uncertainty, coverage denominator/gate and every failure prespecified?

- Are actual outputs, costs, hashes and logs separated from illustrative examples and unexecuted plans?

- Are AI findings, scientific decisions, independent rerun evidence, remaining limitations and the claimed milestone recorded?

AI pre-review checks format, traceability, inconsistencies and obvious scientific mismatches. Scientific review checks estimand/identification, DGP/oracle, training design and uncertainty validity. An independent rerun checks the implemented workflow and reported numbers. Reviewers may come from the same team, but must be independent of the evaluated model's development and disclose conflicts. Unresolved scientific issues remain visible; any revision after frozen evaluation is versioned and re-evaluated as needed.

The contributor submits the selected milestone and evidence for review. Acceptance requires a recorded review decision. A structural validation pass alone does not establish statistical validity, and a successful result for one task does not establish support for all six categories.

**中文**

采用分阶段贡献流程，允许学生在训练前提交严谨提案。审核依据所声明里程碑的证据，不把填写完成的模板当作已实现方法。

| 里程碑 | 所需证据 |
| --- | --- |
| 提案 | 选定任务／目标、来源记录、假设、真值计划、Pi_k、拟议经典基线／PFN 适配器、CI 设计、划分及预算；明确未决项和实现负责人。 |
| 参考演示就绪 | 已实现生成器和经核验真值；可运行经典参考方法与已声明 PFN 支持／适配器；已实现输出／评测流程；可复现的公开冒烟证据与环境。PFN 不支持须记为限制。 |
| 训练就绪 | 经审核的输入／教师／输出头／损失，可执行且经过有界检查的训练流程，冻结架构／超分布、训练／开发划分、种子、预算及检查点选择计划。该状态不代表训练完成。 |
| 统计验证完成 | 实际冻结方法及适用时的检查点，配对固定 DGP 重复，匹配目标的覆盖不确定性与门槛、长度、失败／可用率和成本，以及科学复核与独立重跑证据。主张限于已评测范围。 |

当前协议与模板是**规范草案**。提供模板不代表中介演示、训练和统计评测已经达到这些实现／验证里程碑。

最终审核包须回答以下清单：

- 任务／目标／角色／查询约定是否明确，识别及抽样条件是否完整？

- 每个 DGP、来源版本、复现修改及真值计算能否追溯并独立核验？

- 是否区分 Pi_k、教师标签和模型输入，并排除部署输入中的真值信息？

- 是否冻结并披露训练／开发／评测用途、留出、模型暴露与种子清单？

- 是否记录经典参考与 PFN 支持／适配器，以及已实现时的真实入口、环境和方法模式？

- 是否预定区间构造、观察标签预算、固定 DGP 重复、MC 不确定性、覆盖分母／门槛及全部失败？

- 是否区分真实输出、成本、校验和与日志，以及教学例子和未执行计划？

- 是否记录 AI 发现、科学决定、独立重跑证据、剩余限制和声明里程碑？

AI 预审检查格式、可追溯性、不一致和明显科学错配；科学复核检查目标／识别、DGP／真值、训练设计和不确定性有效性；独立重跑检查已实现流程及报告数字。审核人可来自同一团队，但须独立于被评模型开发并披露冲突。未决科学问题须保留可见；冻结评测后如修改，应记录版本并按需重新评测。

贡献者按选定里程碑提交证据审核，接收须有正式记录的审核决定。结构验证通过不等于统计有效；单项任务表现良好也不代表六类任务均已支持。
