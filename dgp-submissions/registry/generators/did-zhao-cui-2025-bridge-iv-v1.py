"""Independent implementation of Zhao & Cui2025 Section6 observed-data law."""
import math
import random

_EXPECTED = {'baseline_n': 5000, 'bridge_phi': 0.5, 'x_sd': 1, 'time_probability': 0.5, 'instrument_probability': 0.5, 'a0_coefficients': [2, -7, 0.2, 2], 'a1_coefficients': [-1.5, 5, -0.15, 1.5], 'outcome_intercepts': [200, 240], 'outcome_scale': 10, 'cate_coefficients': [-0.5, 1.5, 2], 'u_coefficient': 0.5, 'z_coefficient': 2, 'baseline_x_coefficients': [[1.5, 2], [2, 1.5]], 'outcome_error_sd': 1, 'estimand': 'population_ATE', 'sample_size_policy': 'external_n_independent_cross_sectional_rows'}

def _validate(config):
    if not isinstance(config, dict) or config != _EXPECTED:
        raise ValueError("Only the documented Section6 baseline mechanism is supported")

def _expit(x):
    if x >= 0:
        return 1.0 / (1.0 + math.exp(-x))
    e = math.exp(x)
    return e / (1.0 + e)

def _bridge(rng):
    # Inverse of F(u)=2/pi*atan(exp(u/2)); random() is in[0,1).
    # Exclude the machine endpoint0, not truncate a bridge tail.
    v = rng.random()
    while v == 0.0:
        v = rng.random()
    return 2.0 * math.log(math.tan(math.pi * v / 2.0))

def generate(config, n, seed):
    _validate(config)
    if isinstance(n, bool) or not isinstance(n, int) or n < 1:
        raise ValueError("n must be a positive integer count of independent cross-sectional rows")
    if isinstance(seed, bool) or not isinstance(seed, int):
        raise ValueError("seed must be integer")
    rng = random.Random(seed)
    out = {k: [] for k in ("X1", "X2", "Z", "T", "A", "Y")}
    for _ in range(n):
        x1, x2 = rng.gauss(0.0, 1.0), rng.gauss(0.0, 1.0)
        z, t = int(rng.random() < .5), int(rng.random() < .5)
        u0, u1 = _bridge(rng), _bridge(rng)
        a0 = int(rng.random() < _expit(2 - 7*z + .2*u0 + 2*x1))
        a1 = int(rng.random() < _expit(-1.5 + 5*z - .15*u1 + 1.5*x2))
        signal = 1.5*x1 + 2*x2 - .5
        y0 = 200 + 10*(a0*signal + .5*u0 + 2*z + 1.5*x1 + 2*x2) + rng.gauss(0.0, 1.0)
        y1 = 240 + 10*(a1*signal + .5*u1 + 2*z + 2*x1 + 1.5*x2) + rng.gauss(0.0, 1.0)
        row = (x1, x2, z, t, a1 if t else a0, y1 if t else y0)
        for k, v in zip(out, row):
            if not math.isfinite(v):
                raise ArithmeticError("Nonfinite observed sample")
            out[k].append(v)
    assert all(len(v) == n for v in out.values())
    return out
