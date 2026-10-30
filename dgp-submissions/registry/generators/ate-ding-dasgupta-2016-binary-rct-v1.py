"""Observed-data generator for a finite-population binary potential-outcome RCT."""
import numpy as np

def generate(config, n, seed):
    """SRSWOR sample n units from N=200, then completely randomize n/2 to A=1.

    The SRS stage is an explicit interface adaptation; the source design itself
    fixes the finite population and randomizes treatment. Only A and observed Y
    are returned; potential outcomes and cell labels remain internal.
    """
    if n < 2 or n % 2:
        raise ValueError("n must be an even integer >= 2 for the 1:1 allocation")
    N = int(config["N"])
    if N != 200 or int(config["N1"]) != 100 or int(config["N0"]) != 100:
        raise ValueError("This registered adaptation requires N=200 and N1=N0=100")
    counts = [int(config[k]) for k in ("N11", "N10", "N01", "N00")]
    if sum(counts) != N or any(c < 0 for c in counts):
        raise ValueError("Potential-outcome cell counts must be nonnegative and sum to N")
    rng = np.random.default_rng(seed)
    # Cell order: (Y(1),Y(0)) = (1,1),(1,0),(0,1),(0,0).
    y1 = np.concatenate([np.ones(counts[0], dtype=int), np.ones(counts[1], dtype=int),
                         np.zeros(counts[2], dtype=int), np.zeros(counts[3], dtype=int)])
    y0 = np.concatenate([np.ones(counts[0], dtype=int), np.zeros(counts[1], dtype=int),
                         np.ones(counts[2], dtype=int), np.zeros(counts[3], dtype=int)])
    selected = rng.choice(N, size=n, replace=False)
    assignment = np.zeros(n, dtype=int)
    assignment[rng.permutation(n)[: n // 2]] = 1
    observed = np.where(assignment == 1, y1[selected], y0[selected]).astype(int)
    return {"A": assignment.tolist(), "Y": observed.tolist()}
