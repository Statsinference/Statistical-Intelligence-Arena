"""User-approved whole-experiment-success conditional author-code null law."""
import numbers
import numpy as np
EXPECTED={"scenario":"whole_experiment_success_null","units":25,"periods":1000}
def validate(config):
    if type(config) is not dict or set(config)!=set(EXPECTED) or any(type(config[k]) is not type(v) or config[k]!=v for k,v in EXPECTED.items()):
        raise ValueError("Only registered N25/T1000 whole-experiment conditional null is supported")
def _attempt(rng):
    calibration_x=rng.uniform(-10.,10.,size=(10000,25))
    calibration_t=rng.exponential(scale=np.exp(-1.-.5*calibration_x))
    h=float(np.max(np.quantile(calibration_t,.15,axis=1,method="linear")))
    x=rng.uniform(-10.,10.,25)
    ti=rng.exponential(scale=np.exp(-1.-.5*x))
    s=np.minimum(ti,h)
    t1=float(np.min(s)); first=int(np.argmin(s))
    if not t1<h:
        return None
    time=np.linspace(0.,h,1000)
    k=int(np.searchsorted(time,t1,side="right"))
    # The exact source guard is enforced; no new rescue/conditioning rule.
    if not 1<=k<1000:
        raise RuntimeError("Source time-index guard failed after successful continuous adoption")
    return x,h,t1,first,k

def _generate_with_diagnostics(config,n,seed):
    validate(config)
    if isinstance(n,(bool,np.bool_)) or not isinstance(n,numbers.Integral) or n!=25:
        raise ValueError("n must equal25 unit rows")
    if isinstance(seed,(bool,np.bool_)) or not isinstance(seed,numbers.Integral) or seed<0:
        raise ValueError("seed must be a nonnegative integer")
    rng=np.random.default_rng(int(seed)); attempts=0
    while True:
        attempts+=1
        design=_attempt(rng)
        if design is not None:
            break
    x,h,t1,first,k=design
    eps=rng.normal(0.,.15,25000).reshape((25,1000),order="F")
    y=np.empty((25,1000)); previous=np.zeros(25)
    for j in range(1000):
        y[:,j]=.2*previous+.5*x+.5*np.sqrt(j+1)+eps[:,j]
        previous=y[:,j]
    g=np.zeros(25,dtype=int); g[first]=1
    out={"G":g.tolist(),"X1":x.tolist(),"Tmax":[h]*25,
         "first_adoption":[t1]*25,"pre_last_index":[k]*25}
    out.update({f"Y_t{j+1:04d}":y[:,j].tolist() for j in range(1000)})
    return out,{"attempts":attempts,"rejections":attempts-1}

def generate(config,n,seed):
    return _generate_with_diagnostics(config,n,seed)[0]
