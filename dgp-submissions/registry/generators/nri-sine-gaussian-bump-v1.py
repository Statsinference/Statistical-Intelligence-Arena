"""Observed-data generator for CCF2018 supplement S.II.7 Model 1.

Returns only the observable columns {X, Y}. No oracle nuisance, latent
variables, or true conditional mean is included in the output.

Model 1: m(x) = sin(4*x) + 2*exp(-64*x^2)

Sampling frame: X ~ U[-1,1], eps ~ N(0,1) independent.
"""
import math
import random


def _m_model1(x):
    """m(x) = sin(4x) + 2*exp(-64*x^2).

    sin component: oscillates with angular frequency 4 rad/unit.
    Gaussian bump: amplitude 2, width parameter 64, centered at x=0.
    """
    return math.sin(4.0 * x) + 2.0 * math.exp(-64.0 * x * x)


def _validate(config):
    for key in ("x_lower", "x_upper", "noise_sd", "query_point"):
        if key not in config:
            raise ValueError("Missing config key: " + key)
    if not math.isfinite(config["noise_sd"]) or config["noise_sd"] <= 0:
        raise ValueError("noise_sd must be finite and positive")
    if not (math.isfinite(config["x_lower"]) and math.isfinite(config["x_upper"])):
        raise ValueError("x_lower and x_upper must be finite")
    if config["x_lower"] >= config["x_upper"]:
        raise ValueError("x_lower must be strictly less than x_upper")
    if not math.isfinite(config.get("noise_mean", 0.0)):
        raise ValueError("noise_mean must be finite")
    model = config.get("model_name", "M1")
    if model != "M1":
        raise ValueError("model_name must be M1; got " + str(model))


def generate(config, n, seed):
    """Return observed columns only: {X: [...], Y: [...]}, length n per column.

    Uses a local RNG seeded with `seed`; fixed seed is fully reproducible.
    Does not return the population truth m(x0) or any oracle value.
    The query_point in config is metadata; it does not filter samples.
    All n observations are iid from (X,Y) over the full support X ~ U[-1,1].
    """
    _validate(config)
    if isinstance(n, bool) or not isinstance(n, int) or n < 1:
        raise ValueError("n must be a positive integer")
    rng = random.Random(seed)
    x_lo = config["x_lower"]
    x_hi = config["x_upper"]
    noise_mean = config.get("noise_mean", 0.0)
    noise_sd = config["noise_sd"]
    xs, ys = [], []
    for _ in range(n):
        x = rng.uniform(x_lo, x_hi)
        m_val = _m_model1(x)
        eps = rng.gauss(noise_mean, noise_sd)
        y = m_val + eps
        xs.append(x)
        ys.append(y)
    return {"X": xs, "Y": ys}
