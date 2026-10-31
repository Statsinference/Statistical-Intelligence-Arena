import math,random
def generate(config,n,seed):
 if not isinstance(config, dict) or 'scenarios' in config: raise ValueError('Pass one selected scenario parameter object, not the whole config.json')
 if isinstance(n, bool) or not isinstance(n, int) or n < 1: raise ValueError('n must be a positive integer')
 c = config
 if not all(math.isfinite(float(v)) for key in ('beta','d_intercept','y_intercept','rho') for v in [c[key]]): raise ValueError('finite scalar parameters required')
 if not all(math.isfinite(float(v)) for key in ('gamma','pi') for v in c[key]): raise ValueError('finite coefficients required')
 if len(c['gamma'])!=10 or len(c['pi'])!=10 or abs(c['rho'])>=1:raise ValueError('invalid coefficients/covariance')
 r=random.Random(seed);out={**{f'Z{j+1}':[] for j in range(10)},'D':[],'Y':[]}
 for _ in range(n):
  z=[r.gauss(0,1) for j in range(10)];e=r.gauss(0,1);v=r.gauss(0,1)
  d=c['d_intercept']+sum(a*b for a,b in zip(z,c['gamma']))+e
  y=c['y_intercept']+c['beta']*d+sum(a*b for a,b in zip(z,c['pi']))+c['rho']*e+math.sqrt(1-c['rho']**2)*v
  for j,a in enumerate(z):out[f'Z{j+1}'].append(a)
  out['D'].append(d);out['Y'].append(y)
 return out
