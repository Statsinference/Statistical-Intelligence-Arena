"""Direct sampler of the explicitly derived 10-coordinate Gaussian marginal."""
import math
import numpy as np


def generate(config, n, seed):
    """Return observed W1,...,W10,Y only; n overrides the source experiment size."""
    p = config["p"]
    if type(p) is not int or p != 10:
        raise ValueError("this active-coordinate adaptation requires p=10")
    if type(n) is not int or n < 1:
        raise ValueError("n must be a positive integer")
    rho = float(config["rho"])
    weight = float(config["noise"]["weight_narrow"])
    variances = [float(config["noise"][key]) for key in ("variance_narrow", "variance_wide")]
    if not -1 < rho < 1 or not 0 <= weight <= 1:
        raise ValueError("invalid correlation or mixing probability")
    if not all(math.isfinite(v) and v > 0 for v in variances):
        raise ValueError("normal component variances must be finite and positive")
    beta = np.zeros(p)
    for index, coefficient in config["beta_nonzero"].items():
        j = int(index)
        if not 1 <= j <= p or not math.isfinite(float(coefficient)):
            raise ValueError("invalid one-based coefficient entry")
        beta[j - 1] = float(coefficient)
    # Stationary AR(1) along the feature index; independent rows. This is
    # a matrix-free factorization of Sigma[j,k] = rho**abs(j-k).
    rng = np.random.Generator(np.random.PCG64(seed))
    x = rng.standard_normal((n, p))
    innovation_scale = math.sqrt(1 - rho * rho)
    for j in range(1, p):
        x[:, j] = rho * x[:, j - 1] + innovation_scale * x[:, j]
    is_narrow = rng.random(n) < weight
    scale = np.where(is_narrow, math.sqrt(variances[0]), math.sqrt(variances[1]))
    epsilon = scale * rng.standard_normal(n)
    y = x @ beta + epsilon
    # Query parameters do not affect the observed distribution. Do not center
    # epsilon at its tau-quantile: that would change the source DGP.
    result = {f"W{j + 1}": x[:, j].tolist() for j in range(p)}
    result["Y"] = y.tolist()
    return result
