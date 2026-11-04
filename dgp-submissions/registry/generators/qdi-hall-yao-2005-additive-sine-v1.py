import math
import numpy as np

def generate(config,n,seed):
    if not isinstance(n,int) or n<1: raise ValueError("n must be a positive integer")
    rng=np.random.Generator(np.random.PCG64(seed))
    x=rng.standard_normal((n,4))
    y=config['sine_coefficient']*np.sin(x).sum(axis=1)+config['noise_sd']*rng.standard_normal(n)
    out={"X"+str(j+1):x[:,j].tolist() for j in range(x.shape[1])}
    out["Y"]=y.tolist()
    return out
