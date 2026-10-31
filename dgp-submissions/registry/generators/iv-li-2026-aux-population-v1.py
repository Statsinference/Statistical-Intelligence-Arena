import math,random
def e(x):
 if x>=0:return 1/(1+math.exp(-x))
 t=math.exp(x);return t/(1+t)
def generate(config,n,seed):
 if not isinstance(config, dict) or 'scenarios' in config: raise ValueError('Pass one selected scenario parameter object, not the whole config.json')
 if isinstance(n, bool) or not isinstance(n, int) or n < 1: raise ValueError('n must be a positive integer')
 c = config
 if n<1:raise ValueError('n must be positive')
 rng=random.Random(seed);out={k:[] for k in ('V1','V2','V3','V4','R','Z_obs','X','Y')}
 for _ in range(n):
  V=[rng.gauss(0,1) for _ in range(4)];v=[e(c['transform_intercept']+c['transform_slope']*a) for a in V];a,b,d,f=v
  rho=math.sqrt(.75+1.5*a+1.5*b-.3*d-.3*f);u=rng.uniform(-rho,rho)
  r=int(rng.random()<e(.8+3*a-2*b-d-f));z=int(rng.random()<e(-.5-a+1.5*b+2*d-f)) if r else 0
  px=(e(1.3-2.4*z) if r else e(a-b+.8*d-.6*f))+c['u_treatment_coef']*u
  if not 0<=px<=1:raise ArithmeticError('propensity outside [0,1], not clipped')
  x=int(rng.random()<px);y=(2-r+2*a-b+d-.5*f)*(1+c.get('effect_scale',1.)*x)+u+rng.gauss(0,c['noise_sd'])
  for k,value in zip(out,(*V,r,z,x,y)):out[k].append(value)
 return out
