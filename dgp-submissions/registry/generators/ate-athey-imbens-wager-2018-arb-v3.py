"""Sparse two-stage DGP from Athey, Imbens & Wager (2018), Section 5.2.
Only observed columns are returned; latent index and error terms remain internal.
"""
import math
import numpy as np


def _validate(config, n):
    required = ("n_reference", "p", "rho", "beta_y_profile", "beta_y_norm",
                "beta_w_profile", "beta_w_norm", "theta_noise_sd",
                "outcome_noise_sd", "treatment_effect", "beta_index_start")
    missing = [key for key in required if key not in config]
    if missing:
        raise ValueError("Missing config fields: " + ", ".join(missing))
    if isinstance(n, bool) or not isinstance(n, int) or n < 1:
        raise ValueError("n must be a positive integer")
    if int(config["p"]) != 2000 or int(config["n_reference"]) != 1000:
        raise ValueError("This contribution preserves the Table 3 reference dimensions p=2000, n=1000")
    if not math.isclose(float(config["rho"]), 0.5, rel_tol=0, abs_tol=1e-15):
        raise ValueError("This contribution preserves Table 3 rho=0.5")
    if config["beta_y_profile"] != "inverse_square":
        raise ValueError("Unsupported beta_Y profile")
    if config["beta_w_profile"] not in ("very_sparse", "dense"):
        raise ValueError("beta_W profile must be 'very_sparse' or 'dense'")
    if float(config["beta_y_norm"]) not in (1.0, 4.0):
        raise ValueError("Table 3 beta_Y norm must be 1 or 4")
    if float(config["beta_w_norm"]) not in (1.0, 4.0):
        raise ValueError("Table 3 beta_W norm must be 1 or 4")
    for key in ("theta_noise_sd", "outcome_noise_sd"):
        if not math.isfinite(float(config[key])) or float(config[key]) <= 0:
            raise ValueError(key + " must be finite and positive")
    if not math.isfinite(float(config["treatment_effect"])):
        raise ValueError("treatment_effect must be finite")
    if int(config["beta_index_start"]) != 1:
        raise ValueError("Coefficient profile uses indices j=1,...,p")


def _beta(profile, norm, p):
    j = np.arange(1, p + 1, dtype=float)
    if profile == "inverse_square":
        raw = j ** -2.0
    elif profile == "very_sparse":
        raw = j ** -2.0
    elif profile == "dense":
        raw = j ** -0.5
    else:
        raise ValueError("Unknown coefficient profile: " + str(profile))
    raw_norm = float(np.linalg.norm(raw))
    if not math.isfinite(raw_norm) or raw_norm <= 0:
        raise ValueError("Coefficient profile has invalid norm")
    return raw * (float(norm) / raw_norm)


def _expit_negative(theta):
    """Stable evaluation of 1/(1+exp(theta)) without overflow."""
    theta = np.asarray(theta, dtype=float)
    out = np.empty_like(theta)
    nonnegative = theta >= 0
    # For theta >= 0, exp(-theta)/(1+exp(-theta)) is stable.
    exp_neg = np.exp(-theta[nonnegative])
    out[nonnegative] = exp_neg / (1.0 + exp_neg)
    # For theta < 0, use 1/(1+exp(theta)) with exp(theta)<=1.
    exp_pos = np.exp(theta[~nonnegative])
    out[~nonnegative] = 1.0 / (1.0 + exp_pos)
    return out


def generate(config, n, seed):
    """Return only X1..Xp, W, and observed Y as equal-length numeric lists."""
    _validate(config, n)
    p = int(config["p"])
    rho = float(config["rho"])
    rng = np.random.default_rng(seed)

    # X rows are independent; within each row this recursion gives
    # Cov(X_ij, X_ik) = rho**abs(j-k), with unit marginal variances.
    innovations = rng.normal(size=(n, p))
    x = np.empty((n, p), dtype=float)
    x[:, 0] = innovations[:, 0]
    innovation_scale = math.sqrt(1.0 - rho * rho)
    for j in range(1, p):
        x[:, j] = rho * x[:, j - 1] + innovation_scale * innovations[:, j]

    beta_w = _beta(config["beta_w_profile"], config["beta_w_norm"], p)
    beta_y = _beta(config["beta_y_profile"], config["beta_y_norm"], p)

    # First-stage latent index theta_i = X_i^T beta_W + epsilon_i1.
    # epsilon_i1 and epsilon_i2 are independently sampled as the explicit
    # implementation convention documented in card.md.
    epsilon1 = rng.normal(0.0, float(config["theta_noise_sd"]), size=n)
    theta = x @ beta_w + epsilon1
    treatment_probability = _expit_negative(theta)
    w = rng.binomial(1, treatment_probability).astype(np.int64)

    epsilon2 = rng.normal(0.0, float(config["outcome_noise_sd"]), size=n)
    y = x @ beta_y + float(config["treatment_effect"]) * w + epsilon2

    result = {f"X{j + 1}": x[:, j].tolist() for j in range(p)}
    result["W"] = w.tolist()
    result["Y"] = y.tolist()
    return result
