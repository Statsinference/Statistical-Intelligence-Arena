"""Observed-data generator for the upper step binary-regression DGP.

Source: Dimitriadis, Dümbgen, Henzi, Puke & Ziegel (2023), Biometrika 110(3):663-680.
DGP checked from arXiv:2203.04065v2 (2022-11-02), PDF p.8, Section 5, item 4 (Step).
Formal Biometrika final-version DGP differences not checked; see card.md [*].

Step function: p_s(x) = (floor(k*x) + 1{x != 1}) / k, k = 15 - 10*s.
X ~ Uniform[0, 1]; Y | X ~ Bernoulli(p_s(X)).
Returns only observed columns X and Y (no oracle values).
"""
import math
import random


def _validate(config):
    if not isinstance(config, dict):
        raise ValueError("config must be a scenario dictionary")
    s = config.get("s")
    x_star = config.get("x_star")
    if isinstance(s, bool) or not isinstance(s, (int, float)) or not math.isfinite(float(s)):
        raise ValueError("s must be a finite numeric value")
    s_f = float(s)
    if not (0.0 < s_f <= 1.0 + 1e-12):
        raise ValueError("s must lie in (0, 1]; s=0 is excluded (k=15 is outside {5,...,14})")
    k_float = 15.0 - 10.0 * s_f
    k = int(round(k_float))
    if abs(k_float - k) > 1e-9 or not (5 <= k <= 14):
        raise ValueError(
            f"k = 15 - 10*s = {k_float:.6g} must be an integer in {{5,...,14}}; "
            f"s must be a multiple of 0.1 in (0, 1]"
        )
    if isinstance(x_star, bool) or not isinstance(x_star, (int, float)) or not math.isfinite(float(x_star)):
        raise ValueError("x_star must be a finite numeric value")
    if not 0.0 <= float(x_star) <= 1.0:
        raise ValueError("x_star must lie in [0, 1]")


def _k_from_config(config):
    """Return integer k = 15 - 10*s from a validated config."""
    return int(round(15.0 - 10.0 * float(config["s"])))


def _p_step(x, k):
    """Upper step function: p_s(x) = (floor(k*x) + 1{x != 1}) / k.

    Right-continuous piecewise constant on [j/k, (j+1)/k) with value (j+1)/k,
    for j = 0, ..., k-1; p_s(1) = 1.
    """
    if x >= 1.0:
        return 1.0
    j = int(math.floor(k * x))
    # Guard: floor can return k if x is just below 1 due to floating-point
    if j >= k:
        return 1.0
    return (j + 1) / k


def generate(config, n, seed):
    """Return only the observed columns X and Y, each with length n.

    X_i ~ Uniform[0, 1] independently.
    Y_i | X_i = x ~ Bernoulli(p_s(x)) independently.
    Fixed seed gives reproducible output; different seeds give different output.
    """
    _validate(config)
    if isinstance(n, bool) or not isinstance(n, int) or n < 1:
        raise ValueError("n must be a positive integer")
    k = _k_from_config(config)
    rng = random.Random(seed)
    x_values = []
    y_values = []
    for _ in range(n):
        x = rng.random()           # U[0, 1)
        probability = _p_step(x, k)
        y = int(rng.random() < probability)
        x_values.append(x)
        y_values.append(y)
    return {"X": x_values, "Y": y_values}
