"""Source-grounded observed-data generator. See card.md and source_map.json."""
import numpy as np

def _expit(x):
    return np.exp(-np.logaddexp(0.0, -np.asarray(x, dtype=float)))

def _validate(config, n):
    if isinstance(n, bool) or not isinstance(n, int) or n < 1:
        raise ValueError("n must be a positive integer")
    d = config["dimension"]
    if isinstance(d, bool) or not isinstance(d, int) or d < MIN_DIM:
        raise ValueError("invalid dimension")
    if not np.isfinite(config["noise_sd"]) or config["noise_sd"] <= 0:
        raise ValueError("noise_sd must be positive")

def _observed(x, a, y):
    if not np.isfinite(x).all() or not np.isfinite(y).all():
        raise ValueError("nonfinite sample; no silent clipping or row deletion")
    result = {f"X{j+1}": x[:,j].tolist() for j in range(x.shape[1])}
    result.update(A=a.astype(int).tolist(), Y=y.tolist())
    return result

MIN_DIM=1
def components(config,x):
    p=np.full(x.shape[0],config["treatment_probability"])
    return p,np.zeros(x.shape[0]),np.full(x.shape[0],config["response_magnitude"]*config["response_probability"])

def generate(config,n,seed):
    _validate(config,n)
    rng=np.random.default_rng(seed)
    x=rng.uniform(0,1,(n,config["dimension"]))
    a=rng.binomial(1,config["treatment_probability"],n)
    b=rng.binomial(1,config["response_probability"],n)
    y=config["response_magnitude"]*a*b+rng.normal(0,config["noise_sd"],n)
    return _observed(x,a,y)
