"""Published Section 6.1 equations; coefficients are frozen in config."""
import numpy as np

def generate(config,n,seed):
    rng=np.random.default_rng(seed)
    m=config['m']
    z=rng.binomial(2,.5,size=(n,m))
    u=rng.normal(0,np.sqrt(config['variance_u']),n)
    eps_a=rng.normal(0,np.sqrt(config['variance_eps_a']),n)
    eps_y=rng.normal(0,np.sqrt(config['variance_eps_y']),n)
    a=z@np.asarray(config['gamma'])+config['eta_a']*u+(1+z@np.asarray(config['delta']))*eps_a
    y=config['beta']*a+z@np.asarray(config['alpha'])+config['eta_y']*u+eps_y
    out={f'Z{j+1}':z[:,j].tolist() for j in range(m)}
    out.update(A=a.tolist(),Y=y.tolist())
    return out
