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

SOURCE_PARAMETERS = {'u_probability': 0.5, 'z_probability': [0.2, 0.4], 'a_probability': [0.2, 0.4], 'eta0': -4.605170185988091, 'beta': -0.6931471805599453, 'y_u': -0.693, 'w_probability': [0.02, -0.01], 'd_probability': [0.02, -0.015], 's_probability': [0.1, 0.4], 'selected_sample': True, 'max_candidates': 100000000}
OBSERVED = ['A', 'Z', 'W', 'Y']

def _draw(c,n,rng):
    u=_bernoulli(rng,np.full(n,c['u_probability']))
    b=c['z_probability'];z=_bernoulli(rng,b[0]+b[1]*u)
    b=c['a_probability'];a=_bernoulli(rng,b[0]+b[1]*u)
    y=_bernoulli(rng,np.exp(c['eta0']+c['beta']*a+c['y_u']*u))
    b=c['w_probability'];w=_bernoulli(rng,b[0]+b[1]*u)
    b=c['d_probability'];d=_bernoulli(rng,b[0]+b[1]*u)
    b=c['s_probability'];s=_bernoulli(rng,np.maximum.reduce([y,d,w])*(b[0]+b[1]*u))
    return dict(A=a,Z=z,W=w,Y=y,U=u,D=d,S=s)

def generate(config,n,seed):
    _validate(config,n,seed)
    rng=np.random.Generator(np.random.PCG64(seed))
    chunks={k:[] for k in OBSERVED};accepted=drawn=0
    while accepted<n:
        if drawn>=config['max_candidates']:
            raise RuntimeError("Selection candidate budget exhausted; no partial sample returned")
        batch=min(max(8192,180*(n-accepted)),1000000,config['max_candidates']-drawn)
        full=_draw(config,batch,rng);keep=full['S']==1
        for k in OBSERVED:chunks[k].append(full[k][keep])
        accepted+=int(keep.sum());drawn+=batch
    return {k:np.concatenate(chunks[k])[:n].tolist() for k in OBSERVED}
