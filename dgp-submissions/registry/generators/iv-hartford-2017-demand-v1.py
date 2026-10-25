"""Raw-unit demand equations from Hartford et al. (ICML 2017), Section 4.1."""
from __future__ import annotations
import math
from numbers import Real
import numpy as np

def validate_config(config: dict) -> None:
    if not isinstance(config, dict) or set(config) != {'rho', 'price_low', 'price_high'}:
        raise ValueError('Expected rho, price_low, price_high only')
    if any(isinstance(v, bool) or not isinstance(v, Real) or not math.isfinite(v) for v in config.values()):
        raise ValueError('All configuration values must be finite numbers')
    if not -1 < config['rho'] < 1:
        raise ValueError('rho must be strictly between -1 and 1')

def generate(config: dict, n: int, seed: int) -> dict[str, list]:
    validate_config(config)
    if type(n) is not int or n < 1 or type(seed) is not int or seed < 0:
        raise ValueError('n must be a positive integer and seed a nonnegative integer')
    rng = np.random.Generator(np.random.PCG64(seed))
    t = rng.uniform(0.0, 10.0, n)
    s = rng.integers(1, 8, n)
    z, v, w = (rng.standard_normal(n) for _ in range(3))
    psi = 2*((t-5)**4/600 + np.exp(-4*(t-5)**2) + t/10 - 2)
    p = 25 + (z+3)*psi + v
    error = config['rho']*v + math.sqrt(1-config['rho']**2)*w
    y = 100 + (10+p)*s*psi - 2*p + error
    return {'T':t.tolist(), 'S':s.tolist(), 'Z':z.tolist(), 'P':p.tolist(), 'Y':y.tolist()}
