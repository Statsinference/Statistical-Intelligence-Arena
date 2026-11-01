"""Observed-data generator for Lu–Kolar–Liu (2020) Example 5.1.

Only X1,...,X600,Y are returned.  The shared U_i is used internally to create
within-row dependence and is never exposed as a learner column.
"""
import math
import random


def _validate(config):
    if config.get("dimension") != 600:
        raise ValueError("Example 5.1 requires dimension=600")
    if config.get("active_dimension") != 4 or config.get("active_indices") != [1, 2, 3, 4]:
        raise ValueError("Example 5.1 requires active indices 1,2,3,4")
    t = float(config["dependence_parameter_t"])
    if not math.isfinite(t) or t < 0:
        raise ValueError("dependence_parameter_t must be finite and nonnegative")
    lo, hi = float(config["covariate_uniform_lower"]), float(config["covariate_uniform_upper"])
    if lo != 0.0 or hi != 1.0:
        raise ValueError("Example 5.1 requires Uniform[0,1] inputs")
    if not math.isfinite(float(config["noise_sd"])) or float(config["noise_sd"]) <= 0:
        raise ValueError("noise_sd must be positive and finite")
    if len(config["f1_coefficients"]) != 5:
        raise ValueError("f1_coefficients must have length 5")
    if not all(math.isfinite(float(x)) for x in config["f1_coefficients"]):
        raise ValueError("f1_coefficients must be finite")
    if float(config["f4_denominator_constant"]) <= 1.0:
        raise ValueError("f4 denominator must stay positive on the declared support")


def _f1(x, c, scale):
    angle = 2.0 * math.pi * x
    s, co = math.sin(angle), math.cos(angle)
    return scale * (c[0] * s + c[1] * co + c[2] * s**2 + c[3] * co**3 + c[4] * s**3)


def _f2(x, scale):
    return scale * (2.0 * x - 1.0) ** 2


def _f3(x, scale):
    return scale * x


def _f4(x, scale, denominator_constant):
    s = math.sin(2.0 * math.pi * x)
    return scale * s / (denominator_constant - s)


def generate(config, n, seed):
    """Return observed columns only, with n finite rows and a local RNG."""
    _validate(config)
    if isinstance(n, bool) or not isinstance(n, int) or n < 1:
        raise ValueError("n must be a positive integer")
    rng = random.Random(seed)
    d = int(config["dimension"])
    t = float(config["dependence_parameter_t"])
    denom = 1.0 + t
    noise_sd = float(config["noise_sd"])
    c = [float(x) for x in config["f1_coefficients"]]
    out = {f"X{j}": [] for j in range(1, d + 1)}
    out["Y"] = []
    for _ in range(n):
        u = rng.random()
        x = [(rng.random() + t * u) / denom for _ in range(d)]
        mean = (
            _f1(x[0], c, float(config["f1_scale"]))
            + _f2(x[1], float(config["f2_scale"]))
            + _f3(x[2], float(config["f3_scale"]))
            + _f4(x[3], float(config["f4_scale"]), float(config["f4_denominator_constant"]))
        )
        y = mean + rng.gauss(0.0, noise_sd)
        for j, value in enumerate(x, start=1):
            out[f"X{j}"].append(value)
        out["Y"].append(y)
    return out
