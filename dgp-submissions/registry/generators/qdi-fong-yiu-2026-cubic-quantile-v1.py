"""Observed-only inverse-transform reconstruction of Fong & Yiu Section 7.1."""
import math
import random
from fractions import Fraction


def generate(config, n, seed):
    """Return exactly n Y values; n overrides the scenario's nominal paper_n."""
    if isinstance(n, bool) or not isinstance(n, int) or n < 1:
        raise ValueError("n must be a positive integer")
    if isinstance(seed, bool) or not isinstance(seed, int):
        raise ValueError("seed must be an integer")
    values = []
    for name in ("cubic_coefficient", "shift", "linear_coefficient", "quantile_level"):
        value = config[name]
        if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
            raise ValueError(name + " must be a finite number")
        values.append(float(value))
    a, b, c, tau = values
    if a < 0 or c <= 0 or not 0 <= b <= 1 or not 0 < tau < 1:
        raise ValueError("Require a >= 0, c > 0, b in [0,1], tau in (0,1)")
    rng = random.Random(seed)
    # random() includes zero. Evaluate its exact decimal-parameter endpoint
    # once to avoid -0.25600000000000006 falling below schema's -0.256.
    # Ordinary draws retain the original arithmetic; no clipping is applied.
    zero_endpoint = float(-Fraction(str(a)) * Fraction(str(b)) ** 3)
    observed = []
    for _ in range(n):
        u = rng.random()
        observed.append(zero_endpoint if u == 0.0 else a * (u - b) ** 3 + c * u)
    # U is internal randomness, never an observed covariate or an output column.
    return {"Y": observed}
