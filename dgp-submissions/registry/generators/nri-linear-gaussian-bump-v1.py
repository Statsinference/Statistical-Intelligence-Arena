"""Observed-data generator for CCF2018 supplement S.II.7 Models 2 and 4.

Returns only the observable columns {X, Y}. No oracle nuisance, latent
variables, or true conditional mean is included in the output.

Model 2: m(x) = 2x + 2*exp(-64*x^2)
Model 4: m(x) = x  + 5*phi(10x),  phi(z) = exp(-z^2/2)/sqrt(2*pi)

Both share the same sampling frame: X ~ U[-1,1], eps ~ N(0,1) independent.
"""
import math
import random


def _validate(config):
    required = {"x_lower", "x_upper", "noise_sd", "query_point"}
    for key in required:
        if key not in config:
            raise ValueError("Missing config key: " + key)
    if not math.isfinite(config["noise_sd"]) or config["noise_sd"] <= 0:
        raise ValueError("noise_sd must be finite and positive")
    if not math.isfinite(config["x_lower"]) or not math.isfinite(config["x_upper"]):
        raise ValueError("x_lower and x_upper must be finite")
    if config["x_lower"] >= config["x_upper"]:
        raise ValueError("x_lower must be strictly less than x_upper")
    if not math.isfinite(config.get("noise_mean", 0.0)):
        raise ValueError("noise_mean must be finite")


def _m_model2(x, config):
    """m(x) = linear_coeff*x + bump_amplitude*exp(-bump_width_sq*(x-bump_center)^2)"""
    a = config["linear_coeff"]
    A = config["bump_amplitude"]
    w = config["bump_width_sq"]
    c = config["bump_center"]
    return a * x + A * math.exp(-w * (x - c) ** 2)


def _phi(z):
    """Standard Gaussian density phi(z) = exp(-z^2/2) / sqrt(2*pi)."""
    return math.exp(-0.5 * z * z) / math.sqrt(2.0 * math.pi)


def _m_model4(x, config):
    """m(x) = linear_coeff*x + bump_amplitude*phi(phi_scale*(x-bump_center))"""
    a = config["linear_coeff"]
    A = config["bump_amplitude"]
    s = config["phi_scale"]
    c = config["bump_center"]
    return a * x + A * _phi(s * (x - c))


def _regression_mean(x, config):
    model = config.get("model_name", "M2")
    if model == "M2":
        return _m_model2(x, config)
    elif model == "M4":
        return _m_model4(x, config)
    else:
        raise ValueError("Unknown model_name: " + str(model) + "; expected M2 or M4")


def generate(config, n, seed):
    """Return observed columns only: {X: [...], Y: [...]}, length n per column.

    Uses a local RNG seeded with `seed`; fixed seed is fully reproducible.
    Does not return the population truth m(x0), potential outcomes, or oracle values.
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
