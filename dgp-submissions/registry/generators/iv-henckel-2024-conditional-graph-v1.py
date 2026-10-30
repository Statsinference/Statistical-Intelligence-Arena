"""Independent implementation of the audited G1 expanded DAG."""
import numpy as np

def generate(config, n, seed):
    rng = np.random.default_rng(seed)
    b = np.asarray(config['coefficients'], dtype=float)
    var = np.asarray(config['error_variances'], dtype=float)
    if config['error_distribution'] == 'gaussian':
        eps = rng.normal(size=(n,9))*np.sqrt(var)
    elif config['error_distribution'] == 'uniform':
        eps = rng.uniform(-1,1,size=(n,9))*np.sqrt(3*var)
    else:
        raise ValueError('Unsupported error distribution')
    values = np.zeros((n,9))
    for i in range(9):
        values[:,i] = values@b[i] + eps[:,i]
    return {v: values[:,i].tolist() for i,v in enumerate(config['nodes']) if v not in ('L1','L2')}
