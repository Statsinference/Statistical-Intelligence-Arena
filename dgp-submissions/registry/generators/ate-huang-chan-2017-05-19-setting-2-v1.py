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

MIN_DIM=3
def components(config,x):
    if np.any(x[:,0]<=0): raise ValueError("X1 must be positive")
    p=_expit(x[:,:3]@np.asarray(config["propensity_coefficients"]))
    m1=config["intercept_treated"]+2*np.log(x[:,0])
    m0=config["intercept_control"]+x[:,1]*(1+x[:,0]**2)
    return p,m0,m1

def generate(config,n,seed):
    _validate(config,n)
    rng=np.random.default_rng(seed)
    z=rng.standard_normal((n,config["dimension"]))
    x=z.copy(); x[:,0]=np.exp(z[:,0]/2)
    x[:,1]=z[:,1]*_expit(-z[:,0])
    x[:,2]=(z[:,0]*z[:,2]/config["transform_divisor"]+config["transform_offset"])**3
    p,_,_=components(config,x)
    a=rng.binomial(1,p)
    e0=rng.normal(0,config["noise_sd"],n); e1=rng.normal(0,config["noise_sd"],n)
    y0=config["intercept_control"]+z[:,1]+e0
    y1=config["intercept_treated"]+z[:,0]+e1
    return _observed(x,a,np.where(a==1,y1,y0))
