import numpy as np

def _expit(x):
    return np.exp(-np.logaddexp(0.,-x))

def _bridge_half(rng,n):
    # F(u)=(2/pi)atan(exp(u/2)). No tail truncation.
    v=rng.random(n)
    while np.any(v==0):
        mask=v==0;v[mask]=rng.random(int(mask.sum()))
    return 2*np.log(np.tan(np.pi*v/2))

def generate(config,n,seed):
    if not isinstance(n,int) or isinstance(n,bool) or n<1: raise ValueError('n must be positive integer')
    if config['bridge_phi']!=0.5: raise ValueError('Only the source phi=0.5 bridge law is implemented')
    rng=np.random.default_rng(seed)
    x1=rng.normal(size=n);x2=rng.normal(size=n)
    z=rng.binomial(1,config['z_probability'],n);t=rng.binomial(1,config['time_probability'],n)
    u=[_bridge_half(rng,n),_bridge_half(rng,n)]
    e=config['effect_coefficients'];h=e[0]+e[1]*x1+e[2]*x2
    aa=[];yy=[]
    for j in range(2):
        b=config[f'a{j}_coefficients']
        prob=_expit(b[0]+b[1]*z+b[2]*u[j]+b[3]*x1+b[4]*x2)
        a=rng.binomial(1,prob)
        b_x=config['x_outcome_coefficients'][j]
        mu=config['outcome_intercepts'][j]+config['outcome_scale']*(a*h+config['u_coefficient']*u[j]+config['z_coefficient']*z+b_x[0]*x1+b_x[1]*x2)
        aa.append(a);yy.append(mu+rng.normal(0,config['noise_sd'],n))
    a=np.where(t==1,aa[1],aa[0]);y=np.where(t==1,yy[1],yy[0])
    return {'X1':x1.tolist(),'X2':x2.tolist(),'Z':z.tolist(),'T':t.tolist(),'A':a.tolist(),'Y':y.tolist()}
