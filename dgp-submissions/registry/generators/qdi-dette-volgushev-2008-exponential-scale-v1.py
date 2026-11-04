import math
import numpy as np

def generate(config,n,seed):
    if not isinstance(n,int) or n<1: raise ValueError("n must be a positive integer")
    rng=np.random.Generator(np.random.PCG64(seed))
    x=rng.uniform(0,5,(n,1))
    v=x[:,0]
    e=rng.exponential(1/config['exp_rate'],n)
    y=config['intercept']+config['slope']*v+np.exp(-v)*(e-math.log(config['center_log_argument']))
    out={"X"+str(j+1):x[:,j].tolist() for j in range(x.shape[1])}
    out["Y"]=y.tolist()
    return out
