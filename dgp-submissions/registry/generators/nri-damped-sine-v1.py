"""Observed-data generator for CCF2018 supplement S.II.7 Models 5 and 6.

Returns only the observable columns {X, Y}. No oracle nuisance, latent
variables, or true conditional mean is included in the output.

Model 5 (Hall-Horowitz g2):
    m(x) = sin(3*pi*x/2) / (1 + 18*x^2*(sgn(x)+1))

Model 6 (Hall-Horowitz g3 = g2(x/3)):
    m(x) = sin(pi*x/2) / (1 + 2*x^2*(sgn(x)+1))

Both share: X ~ U[-1,1], eps ~ N(0,1) independent.
"""
import math
import random


def _sgn(x):
    """Sign function: returns -1, 0, or +1."""
    if x > 0:
        return 1
    if x < 0:
        return -1
    return 0


def _m_model5(x):
    """m(x) = sin(3*pi*x/2) / (1 + 18*x^2*(sgn(x)+1))

    For x <= 0: sgn(x)+1 = 0 (x<0) or 1 (x=0, but x^2=0 anyway)
                → denominator = 1, m(x) = sin(3*pi*x/2)
    For x > 0:  sgn(x)+1 = 2
                → denominator = 1 + 36*x^2
    """
    numer = math.sin(1.5 * math.pi * x)
    denom = 1.0 + 18.0 * x * x * (_sgn(x) + 1)
    return numer / denom


def _m_model6(x):
    """m(x) = sin(pi*x/2) / (1 + 2*x^2*(sgn(x)+1))

    This equals g3(x) = g2(x/3) in Hall-Horowitz (2013), where
    g2(u) = sin(3*pi*u/2) / (1 + 18*u^2*(sgn(u)+1)).
    """
    numer = math.sin(0.5 * math.pi * x)
    denom = 1.0 + 2.0 * x * x * (_sgn(x) + 1)
    return numer / denom


def _regression_mean(x, config):
    model = config.get("model_name", "M5")
    if model == "M5":
        return _m_model5(x)
    elif model == "M6":
        return _m_model6(x)
    else:
        raise ValueError("Unknown model_name: " + str(model) + "; expected M5 or M6")


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
    model = config.get("model_name", "M5")
    if model not in ("M5", "M6"):
        raise ValueError("model_name must be M5 or M6")


def generate(config, n, seed):
    """Return observed columns only: {X: [...], Y: [...]}, length n per column.

    Uses a local RNG seeded with `seed`; fixed seed is fully reproducible.
    Does not return the population truth m(x0) or any oracle value.
    The query_point in config is stored metadata; it does not filter samples.
    All n observations are iid from (X, Y) over the full support X ~ U[-1,1].
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
        m_val = _regression_mean(x, config)
        eps = rng.gauss(noise_mean, noise_sd)
        y = m_val + eps
        xs.append(x)
        ys.append(y)
    return {"X": xs, "Y": ys}
