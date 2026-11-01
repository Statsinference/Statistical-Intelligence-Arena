"""Observed-data generator for CCF2018 supplement S.II.7 Model 3.

Returns only the observable columns {X, Y}. No oracle nuisance, latent
variables, or true conditional mean is included in the output.

Model 3: m(x) = 0.3*exp(-4*(2x+1)^2) + 0.7*exp(-16*(2x-1)^2)

Two Gaussian peaks:
  Left peak:  amplitude 0.3, width parameter 4, centered at x=-1/2 (where 2x+1=0)
  Right peak: amplitude 0.7, width parameter 16, centered at x=+1/2 (where 2x-1=0)

Sampling frame: X ~ U[-1,1], eps ~ N(0,1) homoscedastic, independent.
"""
import math
import random


def _m_model3(x):
    """m(x) = 0.3*exp(-4*(2x+1)^2) + 0.7*exp(-16*(2x-1)^2)."""
    left = 2.0 * x + 1.0
    right = 2.0 * x - 1.0
    return 0.3 * math.exp(-4.0 * left * left) + 0.7 * math.exp(-16.0 * right * right)


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
    model = config.get("model_name", "M3")
    if model != "M3":
        raise ValueError("model_name must be M3; got " + str(model))


def generate(config, n, seed):
    """Return observed columns only: {X: [...], Y: [...]}, length n per column.

    Uses a local RNG seeded with `seed`; fixed seed is fully reproducible.
    Does not return the population truth m(x0) or any oracle value.
    The query_point in config is metadata only; it does not filter samples.
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
        m_val = _m_model3(x)
        eps = rng.gauss(noise_mean, noise_sd)
        y = m_val + eps
        xs.append(x)
        ys.append(y)
    return {"X": xs, "Y": ys}
