"""Two-time-point proximal longitudinal model, one row per independent person."""
import numpy as np

def generate(config,n,seed):
    if not isinstance(n,int) or n<1: raise ValueError('n must be positive integer')
    c=config; r=np.random.Generator(np.random.PCG64(seed)); sd=c['noise_sd']
    x0=r.normal(-.35,sd,n); u0=r.normal(.35,sd,n)
    a0=(r.random(n)<1/(1+np.exp(.5-.35*x0+.35*u0))).astype(int)
    z0=.2+.5*a0+.5*x0+.75*u0+r.normal(0,sd,n)
    w0=.2+.5*x0-.95*u0+r.normal(0,sd,n)
    x1=.2+.7*a0+.7*x0+r.normal(0,sd,n)
    u1=.2+.7*a0+.7*u0+r.normal(0,sd,n)
    a1=(r.random(n)<1/(1+np.exp(.5-.5*a0-.35*(x0+x1)-.35*(u0+u1)))).astype(int)
    z1=.2+.5*(a0+a1)+.5*(x0+x1)-.75*(u0+u1)+r.normal(0,sd,n)
    w1=.35+.45*(x0+x1)-.85*(u0+u1)+r.normal(0,sd,n)
    y=-1.3+c['direct_a1']*a1+c['direct_a0']*a0+.5*x1-.7*u1+.2*x0-.7*u0+r.normal(0,sd,n)
    return {k:v.tolist() for k,v in dict(X0=x0,A0=a0,Z0=z0,W0=w0,X1=x1,A1=a1,Z1=z1,W1=w1,Y=y).items()}
