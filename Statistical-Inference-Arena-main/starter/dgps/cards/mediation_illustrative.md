# Illustrative mediation DGP card

Status: PLANNED / NOT IMPLEMENTED. Source relation: original_illustrative.
Citation: no_external_source_claimed. This card is a teaching example, not a reproduction of a named classical paper.
Protocol v0.3, 2026-10-18.

## Variables and mechanism

X precedes binary A, mediator M follows A, and Y follows M.

X ~ N(0,1)
A | X ~ Bernoulli(expit(c0 + cX X))
M = a0 + aA A + aX X + eM
Y = b0 + bA A + bM M + bAM A M + bX X + eY

The proposed errors are independent, mean zero and independent of X and assignment randomness. TODO: select noise distributions/variances, coefficients, overlap constraints, independent units and sample sizes. No numeric parameter configuration is registered.

## Targets and analytic truth

NIE = E[Y(1,M(1)) - Y(1,M(0))] = aA (bM + bAM).
Complementary NDE = E[Y(1,M(0)) - Y(0,M(0))] = bA + bAM a0.

These formulas use the stated superpopulation E[X]=0. More generally the NDE is bA + bAM (a0 + aX E[X]); a fixed empirical covariate pool may have a different mean. Do not reuse the zero-mean formula after changing the target population.

The starter task evaluates NIE only. NDE is a separate target ID/evaluation if enabled. A simple causal identification route needs consistency, treatment and mediator-outcome exchangeability, appropriate cross-world assumptions and support, with no treatment-induced mediator-outcome confounder for this route. Randomizing A alone does not establish all mediation assumptions.

## Planned pipeline

- Generator: implement observed (X,A,M,Y), with oracle quantities stored separately for truth/training supervision.
- Reference: assess a regression plug-in plus fully rerun iid bootstrap under the stated model. This is a proposed baseline, not a claimed best method.
- PFN: first specify the same target and allowed input, then choose reusable regression adaptation or a small dedicated training plan.
- Teacher: select and derive the target/supervision. An efficient fluctuation or variance target requires a valid mediation-specific derivation, not an ATE formula copied under a new label.
- Evaluation: fix each mechanism, draw paired independent repeated datasets, and compare CI validity before length.

TODO: independent analytic verification, implementation/version, lawful provenance and review. No generator, checkpoint, runner, timings or empirical performance are included.
