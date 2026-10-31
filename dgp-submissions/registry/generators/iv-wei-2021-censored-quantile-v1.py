import math,random
def generate(config,n,seed):
 if not isinstance(config, dict) or 'scenarios' in config: raise ValueError('Pass one selected scenario parameter object, not the whole config.json')
 if isinstance(n, bool) or not isinstance(n, int) or n < 1: raise ValueError('n must be a positive integer')
 c = config
 if not 0<c['tau']<1 or not 0<=c['pc']<=1 or not 0<=c['pa']<=1-c['pc'] or c['censor_upper']<=0: raise ValueError('invalid quantile, stratum probabilities or censoring bound')
 if n<1 or c['model'] not in ('G','H'):raise ValueError('invalid n/scenario')
 rng=random.Random(seed);out={k:[] for k in ('X1','X2','V','D','W','E')}
 for _ in range(n):
  x1=rng.random();x2=int(rng.random()<.5);group=rng.random()
  lin=.1*x2+x1*x1+x1*x2+rng.gauss(0,.5);v=int(rng.random()<1/(1+math.exp(-lin)))
  d=v if group<c['pc'] else 1 if group<c['pc']+c['pa'] else 0
  if group<c['pc']:
   u=rng.random()
   if not 0<u<1:raise ArithmeticError('inverse CDF endpoint; no silent clipping')
   logt=-.2*x1-.3*x2+(c['effect']*d+math.log(-math.log1p(-u)) if c['model']=='G' else math.log(u)+c['effect']*math.exp(.3*u)*d)
  else:logt=-.1*x1-.2*x2+.2*d+rng.gauss(0,.5)
  t=math.exp(logt);censor=c['censor_upper']*rng.random()+x2
  for k,a in zip(out,(x1,x2,v,d,min(t,censor),int(t<=censor))):out[k].append(a)
 return out
