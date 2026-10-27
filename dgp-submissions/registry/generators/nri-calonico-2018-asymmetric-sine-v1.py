"""Calonico--Cattaneo--Farrell (JASA, 2018), Section 4 regression DGP."""
import math
import numpy as np


def validate_config(config):
    """The query is fixed before sampling; it never affects the data law."""
    if set(config) != {'query_x', 'noise_sd'}:
        raise ValueError('Expected only query_x and noise_sd')
    for key in ['query_x', 'noise_sd']:
        if type(config[key]) not in (int, float) or not math.isfinite(config[key]):
            raise ValueError(key + ' must be a finite number')
    if not -1 <= config['query_x'] <= 1:
        raise ValueError('query_x must lie in the design support [-1,1]')
    if config['noise_sd'] <= 0:
        raise ValueError('noise_sd must be positive; registered source scenarios use 1')


def regression_mean(x):
    """Vectorized source equation; an oracle for generation, never an output column."""
    return np.sin(1.5 * np.pi * x) / (1 + 18 * x**2 * (np.sign(x) + 1))


def generate(config, n, seed):
    """Return exactly the observed X and Y columns as numeric Python lists."""
    validate_config(config)
    if type(n) is not int or n <= 0:
        raise ValueError('n must be a positive integer')
    if type(seed) is not int or seed < 0:
        raise ValueError('seed must be a nonnegative integer')
    rng = np.random.Generator(np.random.PCG64(seed))
    x = rng.uniform(-1, 1, n)
    error = rng.normal(0, config['noise_sd'], n)
    y = regression_mean(x) + error
    return {'X': x.tolist(), 'Y': y.tolist()}
