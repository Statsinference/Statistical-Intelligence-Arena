"""Example StatArena Lite method for instrumental variables."""

import numpy as np


def estimate(study):
    """Return an unadjusted Wald estimate and a 95% interval."""
    if study["domain"] != "iv":
        raise ValueError("This example expects the IV domain.")

    instrument = study["Z"].ravel()
    treatment = study["D"].ravel()
    outcome = study["Y"].ravel()
    encouraged = instrument == 1
    control = instrument == 0
    first_stage = treatment[encouraged].mean() - treatment[control].mean()
    if first_stage == 0:
        raise ValueError("The treatment difference between instrument groups is zero.")
    point = (outcome[encouraged].mean() - outcome[control].mean()) / first_stage

    residual = outcome - point * treatment
    variance = sum(residual[group].var(ddof=1) / group.sum() for group in (encouraged, control))
    margin = 1.95996398454 * np.sqrt(variance) / abs(first_stage)
    return point, point - margin, point + margin
