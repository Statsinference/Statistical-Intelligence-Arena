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
def components(c,x):
    p=_expit(c['propensity_scale']*x[:,:3].sum(axis=1))
    h=c['outcome_shift']; baseline=(x[:,0]+h)*(x[:,1]+x[:,2]+h)
    return p,baseline,baseline+c['treatment_effect']

def generate(config,n,seed):
    _validate(config,n)
    rng=np.random.default_rng(seed); rho=config['rho']
    if abs(rho)>=1: raise ValueError('invalid rho')
    z=rng.standard_normal((n,config['dimension'])); x=np.empty_like(z); x[:,0]=z[:,0]
    for j in range(1,x.shape[1]): x[:,j]=rho*x[:,j-1]+np.sqrt(1-rho*rho)*z[:,j]
    p,m0,m1=components(config,x); a=rng.binomial(1,p)
    y=np.where(a==1,m1,m0)+rng.normal(0,config['noise_sd'],n)
    return _observed(x,a,y)
