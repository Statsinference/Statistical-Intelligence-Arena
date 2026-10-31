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

SOURCE_PARAMETERS = {'baseline_mean': [0.25, 0.25, 0], 'baseline_cov': [[0.25, 0, 0.05], [0, 0.25, 0.05], [0.05, 0.05, 1]], 'a_logit': [0, -0.5, -0.4], 'z': [0.2, -0.52, 0.2, -1], 'w': [0.3, 0.2, -0.6], 'm': [0, -0.3, -0.5, 0.4], 'y': [2, 2, 1, 2, -1, -1], 'proxy_sd': 1, 'mediator_sd': 1, 'y_sd': 2}
OBSERVED = ['X1', 'X2', 'A', 'Z', 'W', 'M', 'Y']

def _draw(c,n,rng):
    x1,x2,u=rng.multivariate_normal(c['baseline_mean'],c['baseline_cov'],n).T;xs=x1+x2
    b=c['a_logit'];a=_bernoulli(rng,_expit(b[0]+b[1]*xs+b[2]*u))
    b=c['z'];z=b[0]+b[1]*a+b[2]*xs+b[3]*u+rng.normal(0,c['proxy_sd'],n)
    b=c['w'];w=b[0]+b[1]*xs+b[2]*u+rng.normal(0,c['proxy_sd'],n)
    b=c['m'];m=b[0]+b[1]*a+b[2]*xs+b[3]*u+rng.normal(0,c['mediator_sd'],n)
    b=c['y'];y=b[0]+b[1]*a+b[2]*m+b[3]*w+b[4]*xs+b[5]*u+rng.normal(0,c['y_sd'],n)
    return dict(X1=x1,X2=x2,A=a,Z=z,W=w,M=m,Y=y,U=u)

def generate(config,n,seed):
    _validate(config,n,seed)
    rng=np.random.Generator(np.random.PCG64(seed))
    full=_draw(config,n,rng)
    return {k:full[k].tolist() for k in OBSERVED}
