"""Authorized adapted S.25 count-panel mechanism; observations only."""
import math
import numbers
import numpy as np

_EXPECTED = {"r": 1, "zeta": 0.0, "T_pre": 100, "T_post": 100,
             "beta": -2.0, "factor_mean": 0.5, "factor_sd": 0.1,
             "factor_lower": 0.0, "factor_upper": 1.0,
             "mu_treated": 1.0, "mu_donor": 1.0, "mu_proxy": 1.0}

def _validate(config):
    if not isinstance(config, dict) or set(config) != set(_EXPECTED):
        raise ValueError("Only the complete registered baseline configuration is supported")
    for key, expected in _EXPECTED.items():
        value = config[key]
        if isinstance(value, (bool, np.bool_)) or not isinstance(value, numbers.Real):
            raise ValueError("Configuration values must be finite real numbers")
        if not math.isfinite(float(value)) or value != expected:
            raise ValueError("Unsupported baseline parameter: " + key)


def generate(config, n, seed):
    """Three unit rows, 200 count observations; seed uses a local Generator.

    The common factor is iid through time. Given its entire path, all unit
    and time Poisson draws are independent: explicitly authorized adaptation
    of the 2023 code's joint sampling law to the formal 2026 parameters.
    """
    _validate(config)
    if isinstance(n, (bool, np.bool_)) or not isinstance(n, numbers.Integral) or n != 3:
        raise ValueError("n denotes unit rows and must be exactly 3")
    if isinstance(seed, (bool, np.bool_)) or not isinstance(seed, numbers.Integral) or seed < 0:
        raise ValueError("seed must be a nonnegative integer")
    rng = np.random.default_rng(int(seed))
    factor = rng.normal(0.5, 0.1, size=200)
    bad = (factor <= 0.0) | (factor >= 1.0)
    while np.any(bad):
        factor[bad] = rng.normal(0.5, 0.1, size=int(np.sum(bad)))
        bad = (factor <= 0.0) | (factor >= 1.0)
    # Rejection yields the exact truncated-normal law; clipping is not used.
    treated_rates = np.exp(factor)
    treated_rates[100:] *= math.exp(-2.0)
    control_rates = factor / math.expm1(1.0)
    rates = np.vstack((treated_rates, control_rates, control_rates))
    counts = rng.poisson(rates)
    result = {"G": [1, 0, 0], "P": [0, 0, 1]}
    for time in range(200):
        name = ("Y_pre%03d" % (time + 1)) if time < 100 else ("Y_post%03d" % (time - 99))
        result[name] = counts[:, time].tolist()
    return result
