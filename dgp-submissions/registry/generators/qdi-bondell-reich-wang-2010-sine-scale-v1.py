import math
import numpy as np

def generate(config,n,seed):
    if not isinstance(n,int) or n<1: raise ValueError("n must be a positive integer")
    rng=np.random.Generator(np.random.PCG64(seed))
    x=rng.uniform(0,1,(n,1))
    v=x[:,0]
    g=config['intercept']+config['slope']*v+np.sin(config['frequency']*v+config['phase'])
    y=3*v+g*rng.standard_normal(n)
    out={"X"+str(j+1):x[:,j].tolist() for j in range(x.shape[1])}
    out["Y"]=y.tolist()
    return out
