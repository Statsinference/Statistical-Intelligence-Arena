"""Independent implementation of the cited mechanism; exports observed columns only."""
import math
import numpy as np

MECHANISM = 'interaction'
DIMENSION = 3

def validate(config):
    if config["dimension"] != DIMENSION or config["mechanism"] != MECHANISM:
        raise ValueError("Use the declared mechanism and dimension matching schema.csv")
    if config["labeled_reference"] <= 0 or config["unlabeled_reference"] <= 0:
        raise ValueError("Both sample groups must be present")

def conditional_mean(x, config):
    return x[:, 0] * x[:, 1] + 0.5 * (x[:, 2] + 0.5)**2

def generate(config, n, seed):
    validate(config)
    if isinstance(n, bool) or not isinstance(n, int) or n < 2:
        raise ValueError("n is the combined row count and must be an integer >=2")
    # Explicit PCG64, local streams; no global RNG and no fitted/oracle prediction column.
    rng = np.random.Generator(np.random.PCG64(seed))
    d = config["dimension"]
    x = rng.normal(size=(n,d))
    n_l = min(n-1, max(1, n * config["labeled_reference"] //
                       (config["labeled_reference"] + config["unlabeled_reference"])))
    # Two independent iid samples concatenated: the first n_l rows are labeled.
    # Generate Y ONLY for labeled units; unobserved labels never enter returned data.
    mu = conditional_mean(x[:n_l], config)
    labels = mu + rng.normal(0, config["noise_sd"], size=n_l)
    y_obs = np.zeros(n, dtype=float)
    y_obs[:n_l] = labels
    r = np.zeros(n, dtype=int)
    r[:n_l] = 1
    result = {f"X{j+1}": x[:, j].tolist() for j in range(d)}
    result.update(R=r.tolist(), Y_obs=y_obs.tolist())
    return result
