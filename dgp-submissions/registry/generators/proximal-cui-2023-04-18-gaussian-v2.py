import numpy as np


def _expit(t):
    t=np.asarray(t,dtype=float)
    return np.exp(-np.logaddexp(0.,-t))


def _bernoulli(rng,p):
    p=np.asarray(p,dtype=float)
    if not np.isfinite(p).all() or np.any((p<0)|(p>1)):
        raise ValueError("Computed probability is outside [0,1]; sampling stopped without clipping")
    return (rng.random(p.shape)<p).astype(np.int8)


def _validate(config,n,seed):
    if isinstance(n,bool) or not isinstance(n,(int,np.integer)) or n<1:
        raise ValueError("n must be a positive integer")
    if isinstance(seed,bool) or not isinstance(seed,(int,np.integer)) or seed<0:
        raise ValueError("seed must be a nonnegative integer")
    if set(config)!=set(SOURCE_PARAMETERS):
        raise ValueError("Configuration keys differ from the registered source specification")
    for k,value in SOURCE_PARAMETERS.items():
        if k=="beta":
            if not any(abs(config[k]-float(np.log(r)))<1e-14 for r in [.2,.5,.7,1.]):
                raise ValueError("Effect value is outside the four registered scenarios")
        elif config[k]!=value:
            raise ValueError("Parameter differs from the registered scenario: "+k)

SOURCE_PARAMETERS = {'x_mean': [0.25, 0.25], 'x_cov': [[0.0625, 0], [0, 0.0625]], 'a_logit': [0, -0.125, -0.125], 'zwu_intercepts': [0.25, 0.25, 0.25], 'zwu_a': [0.25, 0.125, 0.25], 'zwu_x': [[0.25, 0.25], [0.25, 0.25], [0.25, 0.25]], 'zwu_cov': [[1, 0.25, 0.5], [0.25, 1, 0.5], [0.5, 0.5, 1]], 'y_intercept': 2, 'y_a': 2, 'y_x': [0.25, 0.25], 'bridge_w': 4, 'omega': 2, 'y_sd': 0.25}
OBSERVED = ['X1', 'X2', 'A', 'Z', 'W', 'Y']

def _draw(c,n,rng):
    x=rng.multivariate_normal(c['x_mean'],c['x_cov'],n)
    a=_bernoulli(rng,_expit(c['a_logit'][0]+x@np.asarray(c['a_logit'][1:])))
    mu=np.asarray(c['zwu_intercepts'])+a[:,None]*np.asarray(c['zwu_a'])+x@np.asarray(c['zwu_x']).T
    zwu=mu+rng.normal(size=(n,3))@np.linalg.cholesky(c['zwu_cov']).T
    z,w,u=zwu.T
    ratio=c['zwu_cov'][1][2]/c['zwu_cov'][2][2]
    g=c['zwu_intercepts'][1]+x@np.asarray(c['zwu_x'][1])+ratio*(u-c['zwu_intercepts'][2]-x@np.asarray(c['zwu_x'][2]))
    y=c['y_intercept']+c['y_a']*a+x@np.asarray(c['y_x'])+(c['bridge_w']-c['omega'])*g+c['omega']*w+rng.normal(0,c['y_sd'],n)
    return dict(X1=x[:,0],X2=x[:,1],A=a,Z=z,W=w,Y=y,U=u)

def generate(config,n,seed):
    _validate(config,n,seed)
    rng=np.random.Generator(np.random.PCG64(seed))
    full=_draw(config,n,rng)
    return {k:full[k].tolist() for k in OBSERVED}
