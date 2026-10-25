"""Code-scale Gaussian sine IV DGP, with sample normalization removed explicitly."""
from __future__ import annotations
import math
from numbers import Real
import numpy as np

def validate_config(config: dict) -> None:
    required={'instrument_strength','instrument_sd','confounder_sd','treatment_noise_sd','outcome_noise_sd','treatment_low','treatment_high'}
    if not isinstance(config,dict) or set(config)!=required:
        raise ValueError('Unexpected configuration keys')
    if any(isinstance(v,bool) or not isinstance(v,Real) or not math.isfinite(v) for v in config.values()):
        raise ValueError('All configuration values must be finite numbers')
    if not 0 < config['instrument_strength'] <= 1:
        raise ValueError('Identification scenario requires 0 < instrument_strength <= 1')
    if any(config[k] <= 0 for k in ('instrument_sd','confounder_sd','treatment_noise_sd','outcome_noise_sd')):
        raise ValueError('Standard deviations must be positive')

def generate(config: dict,n: int,seed: int) -> dict[str,list]:
    validate_config(config)
    if type(n) is not int or n<1 or type(seed) is not int or seed<0:
        raise ValueError('n must be a positive integer and seed a nonnegative integer')
    rng=np.random.Generator(np.random.PCG64(seed))
    z=rng.normal(0,config['instrument_sd'],n)
    u=rng.normal(0,config['confounder_sd'],n)
    delta=rng.normal(0,config['treatment_noise_sd'],n)
    zeta=rng.normal(0,config['outcome_noise_sd'],n)
    a=config['instrument_strength']
    p=a*z+(1-a)*u+delta
    y=np.sin(p)+u+zeta
    return {'Z1':z.tolist(),'P':p.tolist(),'Y':y.tolist()}
