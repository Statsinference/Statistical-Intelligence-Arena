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

SOURCE_PARAMETERS = {'x0_mean': -0.35, 'u0_mean': 0.35, 'noise_sd': 0.5, 'a0_logit': [-0.5, 0.35, -0.35], 'z0': [0.2, 0.5, 0.5, 0.75], 'w0': [0.2, 0.5, -0.95], 'x1': [0.2, 0.7, 0.7], 'u1': [0.2, 0.7, 0.7], 'a1_logit': [-0.5, 0.5, 0.35, 0.35], 'z1': [0.2, 0.5, 0.5, -0.75], 'w1': [0.35, 0.45, -0.85], 'y': [-1.3, 1, 1.14, 0.5, -0.7, 0.2, -0.7]}
OBSERVED = ['X0', 'A0', 'Z0', 'W0', 'X1', 'A1', 'Z1', 'W1', 'Y']

def _draw(c,n,rng):
    sd=c['noise_sd'];noise=lambda:rng.normal(0,sd,n)
    x0=rng.normal(c['x0_mean'],sd,n);u0=rng.normal(c['u0_mean'],sd,n)
    b=c['a0_logit'];a0=_bernoulli(rng,_expit(b[0]+b[1]*x0+b[2]*u0))
    b=c['z0'];z0=b[0]+b[1]*a0+b[2]*x0+b[3]*u0+noise()
    b=c['w0'];w0=b[0]+b[1]*x0+b[2]*u0+noise()
    b=c['x1'];x1=b[0]+b[1]*a0+b[2]*x0+noise()
    b=c['u1'];u1=b[0]+b[1]*a0+b[2]*u0+noise()
    b=c['a1_logit'];a1=_bernoulli(rng,_expit(b[0]+b[1]*a0+b[2]*(x0+x1)+b[3]*(u0+u1)))
    b=c['z1'];z1=b[0]+b[1]*(a0+a1)+b[2]*(x0+x1)+b[3]*(u0+u1)+noise()
    b=c['w1'];w1=b[0]+b[1]*(x0+x1)+b[2]*(u0+u1)+noise()
    b=c['y'];y=b[0]+b[1]*a1+b[2]*a0+b[3]*x1+b[4]*u1+b[5]*x0+b[6]*u0+noise()
    return dict(X0=x0,A0=a0,Z0=z0,W0=w0,X1=x1,A1=a1,Z1=z1,W1=w1,Y=y,U0=u0,U1=u1)

def generate(config,n,seed):
    _validate(config,n,seed)
    rng=np.random.Generator(np.random.PCG64(seed))
    full=_draw(config,n,rng)
    return {k:full[k].tolist() for k in OBSERVED}
