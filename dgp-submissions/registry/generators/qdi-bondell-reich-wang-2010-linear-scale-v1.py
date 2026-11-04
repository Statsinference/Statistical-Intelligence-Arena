import math
import numpy as np

def generate(config,n,seed):
    if not isinstance(n,int) or n<1: raise ValueError("n must be a positive integer")
    rng=np.random.Generator(np.random.PCG64(seed))
    x=rng.uniform(0,1,(n,4))
    m=config['intercept']+x@np.asarray(config['beta'])
    s=config['scale_intercept']+x@np.asarray(config['gamma'])
    y=m+s*rng.standard_normal(n)
    out={"X"+str(j+1):x[:,j].tolist() for j in range(x.shape[1])}
    out["Y"]=y.tolist()
    return out
