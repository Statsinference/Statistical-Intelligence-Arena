"""Observed-data reconstruction of Zhao & Wu (2008) Model 1.

Only the observed regression pairs (X_i, Y_i) = (Y_{i-1}, Y_i) are returned;
no innovation sequence, latent state or oracle column is exported.
WARNING: consecutive rows share a Y value, so rows are NOT independent draws.
"""
import math
import random

REQUIRED = ("mu_scale", "noise_sd", "burn_in", "query_x")


def validate(config):
    for key in REQUIRED:
        if key not in config:
            raise ValueError("Missing configuration key: " + key)
    mu_scale = float(config["mu_scale"])
    noise_sd = float(config["noise_sd"])
    burn_in = config["burn_in"]
    query_x = float(config["query_x"])
    if not math.isfinite(mu_scale):
        raise ValueError("mu_scale must be finite")
    if abs(mu_scale) >= 1.0:
        raise ValueError("|mu_scale| >= 1 breaks the contraction that makes the chain geometrically ergodic")
    if not math.isfinite(noise_sd) or noise_sd <= 0.0:
        raise ValueError("noise_sd must be finite and positive")
    if isinstance(burn_in, bool) or not isinstance(burn_in, int) or burn_in < 0:
        raise ValueError("burn_in must be a nonnegative integer")
    if not math.isfinite(query_x):
        raise ValueError("query_x must be finite")
    return mu_scale, noise_sd, burn_in, query_x


def simulate_chain(config, steps, seed):
    """Y_0 = 0 and Y_t = mu_scale*sin(Y_{t-1}) + noise_sd*eps_t; returns Y_0..Y_{steps-1}."""
    if isinstance(steps, bool) or not isinstance(steps, int) or steps < 2:
        raise ValueError("steps must be an integer >= 2")
    mu_scale, noise_sd = float(config["mu_scale"]), float(config["noise_sd"])
    rng = random.Random(seed)
    chain = [0.0]
    state = 0.0
    for _ in range(steps - 1):
        state = mu_scale * math.sin(state) + noise_sd * rng.gauss(0.0, 1.0)
        chain.append(state)
    return chain


def generate(config, n, seed):
    _, _, burn_in, _ = validate(config)
    if isinstance(n, bool) or not isinstance(n, int) or n < 1:
        raise ValueError("n must be a positive integer")
    chain = simulate_chain(config, burn_in + n + 1, seed)
    return {"X": chain[burn_in:burn_in + n], "Y": chain[burn_in + 1:burn_in + n + 1]}
