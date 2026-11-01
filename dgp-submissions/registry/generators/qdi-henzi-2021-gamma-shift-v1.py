"""Observed iid X,Y from JRSS-B 83(5), pp.979/981, equations (23)-(25).

Follow the published conditional laws: no author-script training jitter; NI uses >=7.
"""
import math
import numpy as np


def generate(config, n, seed):
    """Return finite observed columns only; never export the base Gamma draw."""
    if isinstance(n, bool) or not isinstance(n, int) or n < 1:
        raise ValueError('n must be a positive integer')
    for k in ('x_min', 'x_max', 'shape_power', 'scale_min', 'scale_max', 'shift_size'):
        if isinstance(config[k], bool) or not math.isfinite(float(config[k])):
            raise ValueError(k + ' must be finite numeric')
    if not (0 <= config['x_min'] < config['x_max'] and config['shape_power'] > 0
            and 0 < config['scale_min'] <= config['scale_max']):
        raise ValueError('Invalid distribution parameters')
    threshold = config['shift_threshold']
    if threshold is None and config['shift_size'] != 0:
        raise ValueError('Nonzero shift needs threshold')
    if threshold is not None and not math.isfinite(float(threshold)):
        raise ValueError('Invalid threshold')
    rng = np.random.default_rng(seed)
    x = rng.uniform(config['x_min'], config['x_max'], size=n)
    # The continuous law assigns zero mass to X=0; redraw that finite-RNG endpoint.
    while np.any(x <= 0):
        mask = x <= 0
        x[mask] = rng.uniform(config['x_min'], config['x_max'], size=int(mask.sum()))
    y = rng.gamma(shape=x ** config['shape_power'],
                  scale=np.clip(x, config['scale_min'], config['scale_max']))
    if threshold is not None:
        y = y + config['shift_size'] * (x >= threshold)
    return {'X': x.tolist(), 'Y': y.tolist()}
