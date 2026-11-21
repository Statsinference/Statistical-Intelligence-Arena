
<h1 align="center">
  <img src="docs/assets/statsarena-logo.jpg" width="66" height="66" alt="StatArena logo" />
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="docs/assets/statarena-wordmark-dark.svg" />
    <img src="docs/assets/statarena-wordmark-light.svg" width="317" height="55" alt="StatArena" />
  </picture>
</h1>

<p align="center">
  <strong>The Statistical Intelligence Arena</strong>
</p>

<p align="center">
  <a href="https://statsinference.github.io/" title="Open the StatArena leaderboard website">
    <img src="docs/assets/badge-leaderboard.svg" alt="Leaderboard" height="36" />
  </a>
  <a href="method-submissions/README.md" title="Contribute a method">
    <img src="docs/assets/badge-method.svg" alt="Contribute Method" height="36" />
  </a>
  <a href="dgp-submissions/README.md" title="Contribute a DGP or data">
    <img src="docs/assets/badge-data.svg" alt="Contribute Data" height="36" />
  </a>
</p>

## Overview

**StatArena (The Statistical Intelligence Arena)** is an open academic benchmark and research collaboration dedicated to evaluating statistical methods and advancing statistical intelligence in AI. Beginning with causal inference and expanding to broader statistical problems, StatArena brings together diverse statistical tasks, data-generating processes (DGPs), and standardized evaluation protocols. It provides a common framework for comparing statistical foundation models and established methods across estimation accuracy, bias, variance, confidence interval length, coverage, uncertainty calibration, and computational efficiency, with broader evaluation of hypothesis testing and statistical decision-making as the benchmark evolves.

Prior-Data Fitted Networks (PFNs) suggest an alternative to fitting statistical models from scratch for each dataset: learning reusable statistical patterns through pretraining on diverse tasks. Building on more than a century of statistical research, StatArena explores a fundamental question: **what statistical capabilities can foundation models acquire through pretraining, and which of these capabilities can generalize across tasks?** Through open contributions of statistical methods, tasks, and data-generating processes, together with continuously updated leaderboards, StatArena aims to connect the statistical research community with advances in foundation models, enabling researchers to compare, evaluate, and build upon one another's methods. Our broader vision is to advance statistical intelligence in AI.

## Run an IV example with StatArena Lite

This quickstart runs the built-in instrumental variables (IV) baseline on **16 simulated studies in the public development split**. The target is the local average treatment effect (LATE). For each study, the method returns a point estimate and a nominal 95% confidence interval. For the official leaderboard, see the [submission workflow](method-submissions/README.md).

### 1. Run the built-in baseline

Use Python 3.10 or later. On the first run, Lite downloads and verifies the pinned IV starter from Hugging Face.

```bash
git clone https://github.com/Statsinference/Statistical-Intelligence-Arena.git
cd Statistical-Intelligence-Arena
python -m pip install -e ./lite
statarena-lite run --domain iv --split dev --method baseline
```

Lite saves one prediction per study to `lite-results/iv-dev-baseline.csv`, scores the predictions against the starter's reference values and prints the metrics as JSON. For this example, expect an RMSE of about **1.144** and coverage of **68.75%** (reported as `0.6875` in the JSON).

### 2. Try a bundled Python method

The runnable example implements an unadjusted IV Wald estimator. Pass the file directly to `--method`, or copy it and edit `estimate(study)` to try your own estimator.

```bash
statarena-lite run --domain iv --split dev --method ./lite/examples/my_method.py
```

This run writes `lite-results/iv-dev-my_method.csv` and scores it automatically. If you already have predictions from another pipeline, use `statarena-lite score` with the matching domain and split.

Run `statarena-lite list` to see all supported domains. Use `dev` to develop a method and `test` to evaluate a fixed method on the 32-study public reference split. See the [Lite guide](lite/README.md) for input schemas, CSV format and scoring commands.

## Domain Coverage

**183 DGPs** across **10 research domains**. **6 domains** list methods.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/assets/domain-coverage-dark.svg" />
  <img src="docs/assets/domain-coverage-light.svg" width="856" alt="StatArena domain coverage. The table below lists the exact DGP and method counts." />
</picture>

<details>
<summary>View the data table</summary>

| Research domain | DGPs | Methods |
| :--- | ---: | ---: |
| Average Treatment Effect | 22 | 2 |
| Conditional Average Treatment Effect | 12 | 2 |
| Causal Mediation Analysis | 31 | 2 |
| Instrumental Variables | 21 | 2 |
| Proximal Causal Inference | 15 | 2 |
| Difference-in-Differences | 11 | 2 |
| Nonparametric Regression | 20 | 0 |
| Quantile Inference | 27 | 0 |
| Semi-Supervised Inference | 16 | 0 |
| Missing Data | 8 | 0 |

</details>

The Difference-in-Differences count includes Synthetic Control DGPs.

## Contributing DGPs / Methods

## Contributors

<table>
  <thead>
    <tr><th colspan="4" align="left">Project Leadership</th></tr>
  </thead>
  <tbody>
    <tr>
      <td width="25%"><a href="mailto:shibo@bu.edu">Shi Bo</a><br><small><sub>Boston University</sub></small></td>
      <td width="25%"><a href="mailto:jh7453@bu.edu">Jiaming Hu</a><br><small><sub>Boston University</sub></small></td>
      <td width="25%"><a href="mailto:zhangzhiheng@mail.shufe.edu.cn">Zhiheng Zhang</a><br><small><sub>Shanghai University of Finance and Economics</sub></small></td>
      <td width="25%"></td>
    </tr>
    <tr><th colspan="4" align="left">Method Contributors (Alphabetical Order)</th></tr>
    <tr>
      <td>Yao Fu<br><small><sub>Southern University of Science and Technology</sub></small></td>
      <td>Suo Li<br><small><sub>Shanghai University of Finance and Economics</sub></small></td>
      <td>Kongchang Zhou<br><small><sub>Southern University of Science and Technology</sub></small></td>
      <td></td>
    </tr>
    <tr><th colspan="4" align="left">Data Contributors (Alphabetical Order)</th></tr>
    <tr>
      <td>Ruihan Huang<br><small><sub>Shanghai University of Finance and Economics</sub></small></td>
      <td>Ziyang Huang<br><small><sub>Shanghai University of Finance and Economics</sub></small></td>
      <td>Xuyuxin Ma<br><small><sub>Shanghai University of Finance and Economics</sub></small></td>
      <td>Mingyuan Ma<br><small><sub>Beijing Jiaotong University</sub></small></td>
    </tr>
    <tr>
      <td>Jianying Su<br><small><sub>Shanghai University of Finance and Economics</sub></small></td>
      <td>Cong Wang<br><small><sub>Shanghai University of Finance and Economics</sub></small></td>
      <td>Hangfei Wu<br><small><sub>Shanghai University of Finance and Economics</sub></small></td>
      <td>Qimiao Xu<br><small><sub>Shanghai University of Finance and Economics</sub></small></td>
    </tr>
    <tr>
      <td>Yidan Xu<br><small><sub>Shanghai University of Finance and Economics</sub></small></td>
      <td>Zhuoxin Yan<br><small><sub>Shanghai University of Finance and Economics</sub></small></td>
      <td>Jiayi Zhang<br><small><sub>Shanghai University of Finance and Economics</sub></small></td>
      <td>Weibo Zhang<br><small><sub>Shanghai University of Finance and Economics</sub></small></td>
    </tr>
    <tr>
      <td>Junhong Zheng<br><small><sub>Shanghai University of Finance and Economics</sub></small></td>
      <td>Yuan Zhong<br><small><sub>Shanghai University of Finance and Economics</sub></small></td>
      <td></td>
      <td></td>
    </tr>
    <tr><th colspan="4" align="left">Advisors</th></tr>
  </tbody>
</table>



## Citation

The Statistical Intelligence Arena team. (2026, November 22). *StatArena: The Statistical Intelligence Arena* (v0.1.0) [Software]. [GitHub repository](https://github.com/Statsinference/Statistical-Intelligence-Arena).

See the [citation metadata](CITATION.cff) and the [StatArena leaderboard](https://statsinference.github.io/). The following public dataset revisions match the StatArena Lite runner.

- [ATE and CATE](https://huggingface.co/datasets/fuyao11/StatsInference-Arena-ATE-CATE/tree/6de515dae59a4b502d6ceb66a03180fd08a46a59)
- [Mediation](https://huggingface.co/datasets/shibo769/StatsInference-Arena-Mediation/tree/f70008b2eb4dd82fa9d981d3759ea4dcf5983e33)
- [IV](https://huggingface.co/datasets/Brownight/StatsInference-Arena-IV/tree/f4d6f68c73f745872b46d919a156c2c300476308)
- [Proximal](https://huggingface.co/datasets/wytzzka/StatsInference-Arena-Proximal/tree/2027f348fa54db3db9dd006e2f4d7dcf55282b22)
- [DiD](https://huggingface.co/datasets/lisuo/StatsInference-Arena-DiD/tree/ac97ca41e0a8c4797a8fa33d2d0d47c02ce6a87c)

## Contact

For questions and feedback, please contact the project leads: [Shi Bo](mailto:shibo@bu.edu) · [Jiaming Hu](mailto:jh7453@bu.edu) · [Zhiheng Zhang](mailto:zhangzhiheng@mail.shufe.edu.cn)

## License

The repository includes the [Apache License 2.0](LICENSE). Please see [NOTICE.md](NOTICE.md) for the current release status and rights information concerning other project materials.

## Acknowledgements

[StatArena (The Statistical Intelligence Arena)](https://statsinference.github.io/) is an open academic collaboration jointly led by [Shanghai University of Finance and Economics](https://www.sufe.edu.cn/) and [Boston University](https://www.bu.edu/).
