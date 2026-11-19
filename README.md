
<h1 align="center">
  <img src="docs/assets/statsarena-logo.jpg" width="66" height="66" alt="StatArena logo" />
  StatArena
</h1>

<p align="center">
  <strong>The Statistical Intelligence Arena</strong><br />
  <em>From Inference to Decision</em>
</p>

<p align="center">
  <a href="https://statsinference.github.io/" title="Open the StatsArena leaderboard website">
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

Prior-Data Fitted Networks (PFNs) suggest an alternative to fitting statistical models from scratch for each dataset: learning reusable statistical patterns through pretraining on diverse tasks. Building on more than a century of statistical research, StatArena explores a fundamental question: **what statistical capabilities can foundation models acquire through pretraining, and which of these capabilities can generalize across tasks?** Through open contributions of statistical methods, tasks, and data-generating processes, together with continuously updated leaderboards, StatArena aims to connect the statistical research community with advances in foundation models, enabling researchers to compare, evaluate, and build upon one another's methods. Our broader vision is to advance statistical intelligence in AI, **from inference to decision**.

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

## Contact

For questions and feedback, please contact the project leads: [Shi Bo](mailto:shibo@bu.edu) · [Jiaming Hu](mailto:jh7453@bu.edu) · [Zhiheng Zhang](mailto:zhangzhiheng@mail.shufe.edu.cn)

## License

The repository includes the [Apache License 2.0](LICENSE). Please see [NOTICE.md](NOTICE.md) for the current release status and rights information concerning other project materials.

## Acknowledgements

[Statistical Inference Arena (StatsArena)](https://statsinference.github.io/) is an open academic collaboration jointly led by [Shanghai University of Finance and Economics](https://www.sufe.edu.cn/) and [Boston University](https://www.bu.edu/).
