"""Section 5.2 moderately sparse two-stage DGP; observed columns only."""
import math
import numpy as np


def expit(x):
    """Stable logistic transform for an ndarray."""
    x = np.asarray(x, dtype=float)
    out = np.empty_like(x)
    pos = x >= 0
    out[pos] = 1.0 / (1.0 + np.exp(-x[pos]))
    ex = np.exp(x[~pos])
    out[~pos] = ex / (1.0 + ex)
    return out


def beta_y(config):
    """Build source-defined profile with the 23 mod p index permutation and L2 normalization."""
    p = int(config["p"])
    mult = int(config["index_multiplier"])
    if p < 100 or math.gcd(mult, p) != 1:
        raise ValueError("This source setting requires p >= 100 and an index multiplier coprime to p")
    k = (mult * np.arange(p, dtype=np.int64)) % p
    model = config["beta_y_model"]
    if model == "dense":
        raw = 1.0 / np.sqrt(k + 1.0)
    elif model == "harmonic":
        raw = 1.0 / (10.0 + k)
    elif model == "moderately_sparse":
        raw = np.zeros(p, dtype=float)
        raw[k < 10] = 10.0
        raw[(k >= 10) & (k < 100)] = 1.0
    elif model == "very_sparse":
        raw = (k < 10).astype(float)
    else:
        raise ValueError("Unknown beta_y_model")
    norm = float(np.linalg.norm(raw))
    if not math.isfinite(norm) or norm <= 0:
        raise ValueError("Outcome coefficient profile has invalid norm")
    beta = raw / norm * float(config["beta_y_norm"])
    return beta


def generate(config, n, seed):
    """Return X1..Xp, W and Y; latent probabilities, coefficients and potential outcomes stay private."""
    if isinstance(n, bool) or not isinstance(n, int) or n < 1:
        raise ValueError("n must be a positive integer")
    p = int(config["p"])
    rho = float(config["rho"])
    n_terms = int(config["treatment_n_terms"])
    denominator = float(config["treatment_denominator"])
    tau = float(config["treatment_effect"])
    noise_sd = float(config["outcome_noise_sd"])
    if p < n_terms or not (0.0 < rho < 1.0):
        raise ValueError("Invalid p or rho for AR(1) covariance")
    if n_terms != 100 or denominator != 40.0:
        raise ValueError("Treatment design must match the source's first-100 sum divided by 40")
    if noise_sd <= 0.0 or not math.isfinite(noise_sd) or not math.isfinite(tau):
        raise ValueError("Invalid treatment effect or outcome noise scale")

    rng = np.random.default_rng(seed)
    # AR(1) innovation recursion yields Cov(X_j, X_k) = rho^|j-k| exactly.
    innovations = rng.normal(size=(n, p))
    X = np.empty((n, p), dtype=float)
    X[:, 0] = innovations[:, 0]
    innovation_scale = math.sqrt(1.0 - rho * rho)
    for j in range(1, p):
        X[:, j] = rho * X[:, j - 1] + innovation_scale * innovations[:, j]

    linear_treatment = X[:, :n_terms].sum(axis=1) / denominator
    propensity = expit(linear_treatment)
    W = rng.binomial(1, propensity)

    beta = beta_y(config)
    epsilon = rng.normal(loc=0.0, scale=noise_sd, size=n)
    Y = X @ beta + tau * W + epsilon

    out = {f"X{j+1}": X[:, j].tolist() for j in range(p)}
    out["W"] = W.astype(int).tolist()
    out["Y"] = Y.astype(float).tolist()
    return out
