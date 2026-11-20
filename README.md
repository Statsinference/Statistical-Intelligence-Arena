
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

## Running the Benchmark

Run StatArena Lite locally with Python 3.10 or later. The first run for each domain downloads its pinned public starter from Hugging Face. Start with the IV baseline on the 16-study development split.

```bash
git clone https://github.com/Statsinference/Statistical-Intelligence-Arena.git
cd Statistical-Intelligence-Arena
python -m pip install -e ./lite
statarena-lite list
statarena-lite run --domain iv --split dev --method baseline
```

The command prints a JSON report and saves a predictions CSV. The IV development baseline gives an RMSE of about 1.144 and 95% interval coverage of 68.75%.

To run your own method, copy the example, replace its estimator and pass the file to `--method`. The example implements an unadjusted IV Wald estimator.

```bash
cp lite/examples/my_method.py my_method.py
statarena-lite run --domain iv --split dev --method ./my_method.py
```

Each method receives one observed study at a time and returns a point estimate and a 95% confidence interval. To score predictions from your own pipeline, use `statarena-lite score`.

```bash
statarena-lite score --domain iv --split dev --predictions lite-results/iv-dev-my_method.csv
```

The available domains are `ate`, `cate`, `mediation`, `iv`, `proximal`, and `did`. Use `dev` while developing and `test` to evaluate a fixed method on the 32-study public reference split. See the [Lite guide](lite/README.md) for input schemas, the prediction format and dataset access.

## Domain Coverage

| Research domain | DGPs | Methods |
| :--- | :--- | :--- |
| [Average Treatment Effect](dgp-submissions/registry/by-domain/ate.md) | `▰▰▰▰▰▰▰▰▰▰▰` **22** | `▰▰` **2** |
| [Conditional Average Treatment Effect](dgp-submissions/registry/by-domain/cate.md) | `▰▰▰▰▰▰` **12** | `▰▰` **2** |
| [Causal Mediation](dgp-submissions/registry/by-domain/mediation.md) | `▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰` **31** | `▰▰` **2** |
| [Instrumental Variables](dgp-submissions/registry/by-domain/iv.md) | `▰▰▰▰▰▰▰▰▰▰▰` **21** | `▰▰` **2** |
| [Proximal Causal Inference](dgp-submissions/registry/by-domain/proximal.md) | `▰▰▰▰▰▰▰▰` **15** | `▰▰` **2** |
| [Difference-in-Differences](dgp-submissions/registry/by-domain/did_sc.md) | `▰▰▰▰▰▰` **11** | `▰▰` **2** |
| [Nonparametric Regression](dgp-submissions/registry/by-domain/nonparametric_regression.md) | `▰▰▰▰▰▰▰▰▰▰` **20** | — **0** |
| [Quantile Inference](dgp-submissions/registry/by-domain/quantile.md) | `▰▰▰▰▰▰▰▰▰▰▰▰▰▰` **27** | — **0** |
| [Semi-Supervised Inference](dgp-submissions/registry/by-domain/semi_supervised.md) | `▰▰▰▰▰▰▰▰` **16** | — **0** |
| [Missing Data](dgp-submissions/registry/by-domain/missing_data.md) | `▰▰▰▰` **8** | — **0** |



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
      <td>Zhiyuan Ma<br><small><sub>Beijing Jiaotong University</sub></small></td>
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
