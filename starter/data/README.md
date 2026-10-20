# Data and DGP specification — protocol v0.3

**No data or generator is supplied.** Start with ../dgps/catalog.csv and the DGP card, not an estimator. The current card is an original illustrative mediation model with no external-source claim. Verify any classical source, equations, adaptation and license before adding a sourced row.

The planned observed table contains X_1, A, M and Y; schema.csv is a dictionary, not a dataset. Row identifiers are not predictors. Oracle parameters, latent errors, potential outcomes, exact target and oracle nuisance functions remain in a separate evaluator/teacher channel. Known propensity may be supplied only when the declared assignment/design contract makes it available, not merely because the simulator knows it.

## Specify before generation

- Exact equations, fixed parameters or training parameter law, noise/support constraints, sample size and random seeds.
- Independent sampling/assignment unit; clustering, temporal/panel dependence, and which design components are fixed or redrawn.
- Target population and truth calculation; a fixed empirical covariate pool and a superpopulation are different experiments.
- Rights, provenance, source/adaptation versions, hashes, public/held-out partitions and access custodian.
- CATE query values/groups and their weights; repeated queries from one table do not increase the independent-replicate count.
- DiD timing/parallel-trends/no-anticipation contract, or a separate synthetic-control donor/pre/post/counterfactual-model contract.

../hyperdistribution.yaml governs task-conditional training mixtures and parameter support. ../configs/evaluate.yaml freezes individual evaluation DGPs. Novel seeds alone are not novel mechanisms, and a classical source does not establish absence from pretraining.

TODO: actual generator/access code, exact sources/configurations, independent truth validation and a small smoke dataset. The present format checker checks the dictionary and required-file presence only.
