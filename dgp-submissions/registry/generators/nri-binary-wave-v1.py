"""Observed-data generator for the cubic wave binary-regression DGP.

Source: Dimitriadis, Dümbgen, Henzi, Puke & Ziegel (2023), Biometrika 110(3):663-680.
DGP checked from arXiv:2203.04065v2 (2022-11-02), PDF p.8, Section 5, item 5 (Wave).
Formal Biometrika final-version DGP differences not checked; see card.md [*].

Wave function: p_s(x) = 0.5 - (2s-1)(x-0.5) + 8s(x-0.5)^3.
Equivalent expanded form: p_s(x) = 8s*x^3 - 12s*x^2 + (4s+1)*x.
X ~ Uniform[0, 1]; Y | X ~ Bernoulli(p_s(X)).

Monotonicity holds only for s <= 0.5; s > 0.5 are non-monotone stress scenarios.
s = 0 degenerates to p(x) = x and is excluded as a duplicate of other templates.
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
        raise ValueError("s must lie in (0, 1]; s=0 is excluded (degenerate p(x)=x duplicate)")
    if isinstance(x_star, bool) or not isinstance(x_star, (int, float)) or not math.isfinite(float(x_star)):
        raise ValueError("x_star must be a finite numeric value")
    if not 0.0 <= float(x_star) <= 1.0:
        raise ValueError("x_star must lie in [0, 1]")


def _p_wave(x, s):
    """Cubic wave function: p_s(x) = 0.5 - (2s-1)(x-0.5) + 8s(x-0.5)^3.

    Uses the factored form for numerical stability near x=0.5. The value at x=0.5
    is exactly 0.5 because both (x-0.5) and (x-0.5)^3 vanish there.
    """
    d = x - 0.5
    return 0.5 - (2.0 * s - 1.0) * d + 8.0 * s * d * d * d


def generate(config, n, seed):
    """Return only the observed columns X and Y, each with length n.

    X_i ~ Uniform[0, 1) independently.
    Y_i | X_i = x ~ Bernoulli(p_s(x)) independently, with probability clamped
    to [0, 1] to absorb tiny floating-point excursions outside the support
    (e.g. at x=0 for small s the analytic value is 0 but float rounding may
    give a value of magnitude ~1e-17).
    Fixed seed gives reproducible output; different seeds give different output.
    """
    _validate(config)
    if isinstance(n, bool) or not isinstance(n, int) or n < 1:
        raise ValueError("n must be a positive integer")
    s = float(config["s"])
    rng = random.Random(seed)
    x_values = []
    y_values = []
    for _ in range(n):
        x = rng.random()                 # U[0, 1)
        probability = _p_wave(x, s)
        # Clamp to [0, 1] to absorb floating-point noise at the boundaries.
        if probability < 0.0:
            probability = 0.0
        elif probability > 1.0:
            probability = 1.0
        y = int(rng.random() < probability)
        x_values.append(x)
        y_values.append(y)
    return {"X": x_values, "Y": y_values}
