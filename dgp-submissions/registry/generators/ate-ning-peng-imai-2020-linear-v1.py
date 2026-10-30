import numpy as np

def generate(config, n, seed):
    """Generate observed X1..Xd, A and Y only; local RNG, reproducible seed."""
    if not isinstance(n, int) or n < 1:
        raise ValueError("n must be a positive integer")
    d = int(config["d"])
    rho = float(config["rho"])
    if d < 10:
        raise ValueError("d must be at least 10 for the source outcome equations")
    if not (-1.0 < rho < 1.0):
        raise ValueError("rho must lie strictly between -1 and 1")
    rng = np.random.default_rng(seed)
    # Stationary AR(1) recursion yields Cov(X_j, X_k)=rho**abs(j-k).
    X = np.empty((n, d), dtype=float)
    X[:, 0] = rng.normal(0.0, 1.0, size=n)
    innovation_scale = np.sqrt(1.0 - rho * rho)
    for j in range(1, d):
        X[:, j] = rho * X[:, j - 1] + innovation_scale * rng.normal(0.0, 1.0, size=n)
    b = np.asarray(config["treatment_coefficients"], dtype=float)
    eta = X[:, :6] @ b
    # Equivalent to the source expression 1 - 1/(1 + exp(eta)).
    propensity = 1.0 / (1.0 + np.exp(-eta))
    A = rng.binomial(1, propensity, size=n)
    y1_idx = np.asarray(config["y1_indices_1based"], dtype=int) - 1
    y0_idx = np.asarray(config["y0_indices_1based"], dtype=int) - 1
    eps1 = rng.normal(0.0, float(config["error_sd"]), size=n)
    eps0 = rng.normal(0.0, float(config["error_sd"]), size=n)
    y1 = float(config["y1_intercept"]) + float(config["y1_coefficient"]) * X[:, y1_idx].sum(axis=1) + eps1
    y0 = float(config["y0_intercept"]) + float(config["y0_coefficient"]) * X[:, y0_idx].sum(axis=1) + eps0
    Y = np.where(A == 1, y1, y0)
    out = {f"X{j + 1}": X[:, j].tolist() for j in range(d)}
    out["A"] = A.tolist()
    out["Y"] = Y.tolist()
    return out
