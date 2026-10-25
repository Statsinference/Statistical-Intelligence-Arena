"""JRSS-B 2025 section 7.2, fixed coefficient realization, two data sources."""
import numpy as np

def generate(config,n,seed):
    if not isinstance(n,int) or n<2: raise ValueError('n must be integer >=2')
    c=config;r=np.random.Generator(np.random.PCG64(seed));p=c['p'];k=c['latent_dim']
    b={name:np.asarray(value) for name,value in c['coefficients'].items()}
    # G=1 observational (Y available); G=0 experimental (Y unavailable).
    g=(np.arange(n)<n//2).astype(int)
    x=r.normal(0,np.sqrt(c['baseline_variance']),(n,p))
    u=r.normal(0,np.sqrt(c['baseline_variance']),(n,k))
    prob=np.where(g==1,np.exp(-np.logaddexp(0,x@b['kappa_x']+u@b['kappa_u'])),.5)
    a=(r.random(n)<prob).astype(int);s=c['effect_scale'];sd=np.sqrt(c['noise_variance'])
    s1=s*a[:,None]*b['tau1']+x@b['beta1'].T+u@b['gamma1'].T+r.normal(0,sd,(n,k))
    s2=s*a*float(b['tau2'])+s1@b['alpha2']+x@b['beta2']+u@b['gamma2']+r.normal(0,sd,n)
    s3=s*a[:,None]*b['tau3']+s2[:,None]*b['alpha3']+x@b['beta3'].T+u@b['gamma3'].T+r.normal(0,sd,(n,k))
    y=s*a*float(b['tau_y'])+s3@b['alpha_y']+x@b['beta_y']+u@b['gamma_y']+r.normal(0,sd,n)
    transform=lambda v:np.sign(v)*np.abs(v)**c['power']
    x,s1,s2,s3=map(transform,(x,s1,s2,s3))
    out={f'X{j+1}':x[:,j] for j in range(p)}
    out.update({f'S1_{j+1}':s1[:,j] for j in range(k)})
    out['S2']=s2
    out.update({f'S3_{j+1}':s3[:,j] for j in range(k)})
    out.update(G=g,A=a,GY=g*y)
    return {key:value.tolist() for key,value in out.items()}
