"""Section 5.2 LaLonde-inspired misspecified DGP; observed columns only."""
import math
import numpy as np


def generate(config, n, seed):
    """Return X1..Xp, W, Y only. theta and epsilon stay internal."""
    if isinstance(n, bool) or not isinstance(n, int) or n < 1:
        raise ValueError("n must be a positive integer")
    p = int(config["p"])
    first_p = int(config["outcome_first_p"])
    theta_den = float(config["theta_scale_denominator"])
    eps_sd = float(config["outcome_noise_sd"])
    effect_half = float(config["outcome_effect_half_scale"])
    if p < first_p or p != 1600:
        raise ValueError("The observed schema is fixed at p=1600; selected source scenario has p=1600")
    if not math.isfinite(theta_den) or theta_den <= 0:
        raise ValueError("theta_scale_denominator must be finite and positive")
    if not math.isfinite(eps_sd) or eps_sd <= 0 or not math.isfinite(effect_half):
        raise ValueError("Invalid outcome noise or treatment-effect scale")

    rng = np.random.default_rng(seed)
    # Source: X_i ~ N_p(0,I_p): independent N(0,1) coordinates.
    X = rng.normal(loc=0.0, scale=1.0, size=(n, p))

    # theta_i = log(1 + exp(-2 - 2 X_i1)) / 0.915.
    latent_linear = float(config["theta_intercept"]) + float(config["theta_x1_coefficient"]) * X[:, 0]
    theta = np.logaddexp(0.0, latent_linear) / theta_den

    # P(W=1|X)=1-exp(-theta); expm1 avoids cancellation for small theta.
    prob_w = -np.expm1(-theta)
    # Clip only floating point round-off to the valid Bernoulli probability interval.
    prob_w = np.minimum(1.0, np.maximum(0.0, prob_w))
    W = rng.binomial(1, prob_w)

    epsilon = rng.normal(loc=0.0, scale=eps_sd, size=n)
    baseline = X[:, :first_p].sum(axis=1)
    Y = baseline + theta * (2.0 * W - 1.0) * effect_half + epsilon

    out = {f"X{j + 1}": X[:, j].tolist() for j in range(p)}
    out["W"] = W.astype(int).tolist()
    out["Y"] = Y.astype(float).tolist()
    return out
