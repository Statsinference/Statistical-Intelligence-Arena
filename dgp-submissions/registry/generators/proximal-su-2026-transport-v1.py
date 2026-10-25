"""Two-source observed-data law. Masked zeros are structural placeholders, not measurements."""
import math
import numpy as np
def generate(config,n,seed):
    if not isinstance(n,int) or n<1: raise ValueError('n must be positive integer')
    c=config;r=np.random.Generator(np.random.PCG64(seed))
    normal=r.standard_normal((n,3))@np.linalg.cholesky(c['copula_cov']).T
    x=np.array([.5*(1+math.erf(v/math.sqrt(2))) for v in normal.flat]).reshape(n,3)
    u=r.uniform(-1,0,(n,3));sx=x.sum(axis=1);su=u.sum(axis=1)
    s=(r.random(n)<1/(1+np.exp(-(c['selection_intercept']+.5*sx+.5*su)))).astype(int)
    a=(r.random(n)<.5).astype(int)
    z=u+x+r.normal(0,.5,(n,3)); w=u+x+r.normal(0,.5,(n,3));sw=w.sum(axis=1)
    y=.5+su+sx+sw+c['effect_scale']*a*(-1+su+sw)+r.normal(0,.5,n)
    out={f'X{j+1}':x[:,j].tolist() for j in range(3)}
    out.update({f'W{j+1}':w[:,j].tolist() for j in range(3)})
    out.update({f'SZ{j+1}':(s*z[:,j]).tolist() for j in range(3)})
    out.update(S=s.tolist(),SA=(s*a).tolist(),SY=(s*y).tolist())
    return out
