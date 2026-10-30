"""Independent reconstruction of the Section 5.2 two-cluster DGP.

Only observed columns X1,...,Xp, W, Y are returned. Latent cluster C, noise Z,
individual counterfactuals, and the true ATE are never exported.
"""
import math
import numpy as np


def _beta_vector(profile, p, target_norm):
    j = np.arange(1, p + 1, dtype=float)
    if profile == "dense":
        raw = 1.0 / np.sqrt(j)
    elif profile == "harmonic":
        raw = 1.0 / (j + 9.0)
    elif profile == "moderately_sparse":
        raw = np.zeros(p, dtype=float)
        raw[:min(10, p)] = 10.0
        raw[10:min(100, p)] = 1.0
    elif profile == "very_sparse":
        raw = np.zeros(p, dtype=float)
        raw[:min(10, p)] = 1.0
    else:
        raise ValueError(f"Unknown beta_profile: {profile}")
    norm = float(np.linalg.norm(raw))
    if not math.isfinite(norm) or norm <= 0:
        raise ValueError("beta profile has invalid norm")
    return target_norm * raw / norm


def _delta_vector(profile, p, n, dense_multiplier, sparse_multiplier, period):
    if n < 1:
        raise ValueError("n must be positive")
    if profile == "delta_dense":
        return np.full(p, dense_multiplier / math.sqrt(n), dtype=float)
    if profile == "delta_sparse":
        delta = np.zeros(p, dtype=float)
        delta[np.arange(p) % period == 0] = sparse_multiplier / math.sqrt(n)
        return delta
    raise ValueError(f"Unknown delta_profile: {profile}")


def _validate(config, n):
    if isinstance(n, bool) or not isinstance(n, int) or n < 1:
        raise ValueError("n must be a positive integer")
    p = int(config["p"])
    if p < 1:
        raise ValueError("p must be positive")
    for key in ("z_sd", "epsilon_sd", "beta_l2_norm"):
        value = float(config[key])
        if not math.isfinite(value) or value <= 0:
            raise ValueError(f"{key} must be finite and positive")
    for key in ("cluster_zero_probability", "treatment_probability_if_cluster_zero", "treatment_probability_if_cluster_delta"):
        value = float(config[key])
        if not math.isfinite(value) or not 0.0 <= value <= 1.0:
            raise ValueError(f"{key} must be a probability")
    if int(config["delta_sparse_period"]) < 1:
        raise ValueError("delta_sparse_period must be positive")
    if config["beta_profile"] not in {"dense", "harmonic", "moderately_sparse", "very_sparse"}:
        raise ValueError("Unknown beta_profile")
    if config["delta_profile"] not in {"delta_dense", "delta_sparse"}:
        raise ValueError("Unknown delta_profile")


def generate(config, n, seed):
    """Return the observed table as {column_name: list[number]}.

    The source gives P(C=0|W=0)=.8, P(C=0|W=1)=.2 and P(W=1)=.5.
    The equivalent reverse factorization is P(C=0)=.5, P(W=1|C=0)=.2,
    P(W=1|C=delta)=.8; it preserves the joint law while treating C as baseline.
    """
    _validate(config, n)
    rng = np.random.default_rng(seed)
    p = int(config["p"])
    beta = _beta_vector(config["beta_profile"], p, float(config["beta_l2_norm"]))
    delta = _delta_vector(
        config["delta_profile"], p, n,
        float(config["delta_dense_multiplier"]),
        float(config["delta_sparse_multiplier"]),
        int(config["delta_sparse_period"]),
    )

    # Pretreatment two-cluster membership and assigned treatment. This is a
    # Bayes-equivalent factorization of the source's stated joint law.
    cluster_zero = rng.binomial(1, float(config["cluster_zero_probability"]), size=n).astype(bool)
    prob_w = np.where(
        cluster_zero,
        float(config["treatment_probability_if_cluster_zero"]),
        float(config["treatment_probability_if_cluster_delta"]),
    )
    W = rng.binomial(1, prob_w, size=n).astype(int)

    # Z coordinates are independent N(0,1), so X=C+Z. C is either 0 or delta.
    Z = rng.normal(0.0, float(config["z_sd"]), size=(n, p))
    C = (~cluster_zero).astype(float)[:, None] * delta[None, :]
    X = C + Z
    epsilon = rng.normal(0.0, float(config["epsilon_sd"]), size=n)
    Y = X @ beta + float(config["treatment_effect"]) * W + epsilon

    result = {f"X{j + 1}": X[:, j].tolist() for j in range(p)}
    result["W"] = W.tolist()
    result["Y"] = Y.tolist()
    return result
