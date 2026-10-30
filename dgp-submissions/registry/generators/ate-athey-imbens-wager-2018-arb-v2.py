"""Independent reconstruction of the Section 5.2 many-cluster ATE design."""
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
        raw[:10] = 10.0
        raw[10:100] = 1.0
    elif profile == "very_sparse":
        raw = np.zeros(p, dtype=float)
        raw[:10] = 1.0
    else:
        raise ValueError(f"Unknown beta_profile: {profile}")
    norm = float(np.linalg.norm(raw))
    if not math.isfinite(norm) or norm <= 0.0:
        raise ValueError("beta profile has invalid norm")
    return float(target_norm) * raw / norm


def _validate(config, n):
    if isinstance(n, bool) or not isinstance(n, int) or n < 1:
        raise ValueError("n must be a positive integer")
    p = int(config["p"])
    if p < 100:
        raise ValueError("p must be at least 100 for the source beta profiles")
    if int(config["center_count"]) != 20 or int(config["centers_first_group"]) != 10:
        raise ValueError("The source many-cluster design requires 20 centres split into groups of 10")
    eta = float(config["eta"])
    if eta not in (0.1, 0.25):
        raise ValueError("eta must be one of the source values 0.1 or 0.25")
    for key in ("center_sd", "z_sd", "epsilon_sd", "beta_l2_norm"):
        value = float(config[key])
        if not math.isfinite(value) or value <= 0.0:
            raise ValueError(f"{key} must be finite and positive")
    if config["beta_profile"] not in {"dense", "harmonic", "moderately_sparse", "very_sparse"}:
        raise ValueError("Unknown beta_profile")
    if not math.isfinite(float(config["treatment_effect"])):
        raise ValueError("treatment_effect must be finite")


def generate(config, n, seed):
    """Return observed columns only: X1..Xp, W, Y; no centres or truth labels."""
    _validate(config, n)
    rng = np.random.default_rng(seed)
    p = int(config["p"])
    k_count = int(config["center_count"])
    first_group = int(config["centers_first_group"])
    eta = float(config["eta"])

    beta = _beta_vector(config["beta_profile"], p, float(config["beta_l2_norm"]))

    # Source order: generate the 20 centres, assign each person to one centre,
    # then randomize treatment according to the centre group.
    centers = rng.normal(float(config["center_mean"]), float(config["center_sd"]), size=(k_count, p))
    cluster_index = rng.integers(0, k_count, size=n)
    cluster_center = centers[cluster_index]

    treatment_probability = np.where(cluster_index < first_group, eta, 1.0 - eta)
    W = rng.binomial(1, treatment_probability, size=n).astype(int)

    # Covariate and outcome noise are independent local-RNG draws under the
    # explicit implementation convention documented in collection.json/card.md.
    Z = rng.normal(float(config["z_mean"]), float(config["z_sd"]), size=(n, p))
    X = cluster_center + Z
    epsilon = rng.normal(float(config["epsilon_mean"]), float(config["epsilon_sd"]), size=n)
    Y = X @ beta + float(config["treatment_effect"]) * W + epsilon

    observed = {f"X{j + 1}": X[:, j].tolist() for j in range(p)}
    observed["W"] = W.tolist()
    observed["Y"] = Y.tolist()
    return observed
