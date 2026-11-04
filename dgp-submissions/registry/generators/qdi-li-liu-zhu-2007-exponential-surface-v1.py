import math
import numpy as np

def generate(config,n,seed):
    if not isinstance(n,int) or n<1: raise ValueError("n must be a positive integer")
    rng=np.random.Generator(np.random.PCG64(seed))
    x=rng.uniform(0,1,(n,2))
    a=config['surface_rate']
    center=a*np.sum((x-.5)**2,axis=1)
    d1=a*np.sum((x-np.array([.2,.7]))**2,axis=1)
    d2=a*np.sum((x-np.array([.7,.2]))**2,axis=1)
    m=config['surface_multiplier']*np.exp(center-np.logaddexp(d1,d2))
    if config['error']=='normal':e=rng.standard_normal(n)
    elif config['error']=='t3':e=rng.standard_t(3,n)
    elif config['error']=='normal_mixture':
        component=rng.uniform(size=n)<.1
        e=rng.standard_normal(n)*np.where(component,5.,1.)
    else:raise ValueError('Unsupported error scenario')
    y=m+e
    out={"X"+str(j+1):x[:,j].tolist() for j in range(x.shape[1])}
    out["Y"]=y.tolist()
    return out
