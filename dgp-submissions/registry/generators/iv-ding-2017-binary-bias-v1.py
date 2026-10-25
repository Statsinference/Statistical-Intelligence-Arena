"""Ding et al. (2017), Table 1: observed-law reconstruction with declared SCM."""
import math
import numpy as np


def probability(value):
    return type(value) in (int, float) and math.isfinite(value) and 0 <= value <= 1


def validate_config(config):
    if set(config) != {'z_probability', 'u_probability', 'treatment_probabilities', 'outcome_probabilities'}:
        raise ValueError('Unexpected configuration keys')
    for name in ['z_probability', 'u_probability']:
        if not probability(config[name]) or not 0 < config[name] < 1:
            raise ValueError(name + ' must be strictly between zero and one')
    for name in ['treatment_probabilities', 'outcome_probabilities']:
        matrix = config[name]
        if (not isinstance(matrix, list) or len(matrix) != 2
                or any(not isinstance(row, list) or len(row) != 2 for row in matrix)
                or any(not probability(x) for row in matrix for x in row)):
            raise ValueError(name + ' must be a 2 by 2 probability matrix')
    p = config['treatment_probabilities']
    if any(p[1][u] < p[0][u] for u in [0, 1]):
        raise ValueError('Monotonicity requires p[1,u] >= p[0,u]')
    if not any(p[1][u] > p[0][u] for u in [0, 1]):
        raise ValueError('LATE requires a nonzero first stage')


def generate(config, n, seed):
    validate_config(config)
    if type(n) is not int or n < 1:
        raise ValueError('n must be a positive integer')
    if type(seed) is not int or seed < 0:
        raise ValueError('seed must be a nonnegative integer')
    rng = np.random.Generator(np.random.PCG64(seed))
    # Fixed draw order: Z, latent U, treatment threshold, outcome threshold.
    z = (rng.random(n) < config['z_probability']).astype(int)
    u = (rng.random(n) < config['u_probability']).astype(int)
    p = np.asarray(config['treatment_probabilities'])
    r = np.asarray(config['outcome_probabilities'])
    a = (rng.random(n) < p[z, u]).astype(int)
    y = (rng.random(n) < r[a, u]).astype(int)
    return {'Z': z.tolist(), 'A': a.tolist(), 'Y': y.tolist()}
