"""Proximal mediation with one latent confounder and correlated measured X."""
import numpy as np
def generate(config,n,seed):
    if not isinstance(n,int) or n<1: raise ValueError('n must be positive integer')
    c=config;r=np.random.Generator(np.random.PCG64(seed))
    xu=r.standard_normal((n,3))@np.linalg.cholesky(c['cov_xu']).T+np.array([.25,.25,0])
    x1,x2,u=xu.T;s=x1+x2
    a=(r.random(n)<1/(1+np.exp(.5*s+.4*u))).astype(int)
    z=.2-.52*a+.2*s-u+r.normal(size=n)
    w=.3+.2*s-.6*u+r.normal(size=n)
    m=c['a_to_m']*a-.5*s+.4*u+r.normal(size=n)
    y=2+c['direct_effect']*a+c['m_to_y']*m+2*w-s-u+2*r.normal(size=n)
    return {k:v.tolist() for k,v in dict(X1=x1,X2=x2,A=a,Z=z,W=w,M=m,Y=y).items()}
