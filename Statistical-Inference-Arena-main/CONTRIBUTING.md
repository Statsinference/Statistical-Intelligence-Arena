# Contributing to Statistical Inference Arena

**For the current internal student and researcher team.** The benchmark is under active development (protocol v0.3, output schema v0.2.0). We are **not** operating a public expert-recruitment or automated submission service at this stage.

> **Start with the [GitHub README](README.md#getting-started-for-students),** then read the [student guide in English](docs/student_guide_en.md) or [中文学生操作指南](docs/student_guide_zh.md). The [full requirements (English)](docs/contribution_en.md) / [中文版](docs/contribution_zh.md) are the authoritative scientific specification.

## How to contribute one new causal task

1. **Coordinate with the team.** Choose one of the six registered families (`ate`, `cate`, `mediation`, `iv`, `proximal`, `did_sc`), select a specific estimand and confirm a scientific reviewer. For DiD / synthetic control, explicitly choose the sub-design.
2. **Read the demo plan first.** Review [starter/demo/README.md](starter/demo/README.md) and the [illustrative mediation card](starter/dgps/cards/mediation_illustrative.md). A runnable reference demo is **not yet included in this snapshot**; the spec is not a completed experiment.
3. **Copy [starter/](starter/README.md)** into a separate task-specific workspace. Do not alter the canonical starter to represent your own finished task.
4. **Establish scientific validity.** Define the target and identification conditions, register source-faithful DGPs and any adaptations, build an independent truth calculation and describe the permitted observed inputs. Consult the full protocol before changing the task/output contract.
5. **Register methods and the evaluation design.** Implement a valid classical reference and a PFN adapter when supported (or an explicit unsupported response). Specify `Pi_k`, information budgets, repeated independent datasets at fixed DGPs, CI construction, failure/availability policy and Monte Carlo uncertainty.
6. **Check your work.** Run the existing structural validators described below. Record actual implementation/evaluation evidence and known limitations; do not present illustrative output as measured data.
7. **Ask for an internal review / open a PR.** Follow the [PR checklist](.github/PULL_REQUEST_TEMPLATE.md). Scientific and independent reproduction review are separate from automated format checking.

## Available structural checks

Run from `starter/` (Python 3.9+):

```bash
python validate_submission.py --mode scaffold
python evaluation/check_contract.py
python validate_submission.py --mode submission
```

**The untouched starter should pass the first two and fail submission mode** due to placeholders and example outputs. This is deliberate. Run the checks on your working copy once actual code and evidence are available.

From the repository root, check documentation/site consistency:

```bash
python scripts/check_repository.py
```

These commands do not train a model, compute CI coverage or certify causal inference validity.

## Before claiming completion

Use the milestones **proposal**, **reference-demo-ready**, **training-ready**, **statistically validated** in the specific sense defined by [the student guide](docs/student_guide_en.md). A filled YAML configuration, successful schema check or copied illustration does **not** demonstrate a successful scientific experiment.

Keep canonical English/Chinese protocols, reviewed PDFs, portable website downloads and starter archives synchronized when editing the relevant files. This README update does not modify the underlying scientific protocol.
