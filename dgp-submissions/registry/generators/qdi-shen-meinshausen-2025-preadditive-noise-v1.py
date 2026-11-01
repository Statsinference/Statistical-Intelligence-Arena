"""Literal official supplementary Table C.1 DGP; only observed X,Y leave this module."""
import math
import random


def validate(config):
    expected = {"softplus": (-2., 2., 1., 50000), "square": (0., 2., 1., 50000),
                "cubic": (-2., 2., 1.1, 100000), "log": (0., 2., 1., 100000)}
    name = config["transform"]
    if name not in expected:
        raise ValueError("Unknown source transform")
    if tuple(config[k] for k in ("x_lower", "x_upper", "noise_sd", "source_training_n")) != expected[name]:
        raise ValueError("Source parameters changed: declare and review a new scenario")
    constants = {"x_distribution": "uniform", "noise_distribution": "normal",
                 "noise_mean": 0., "w": 1., "beta": 0., "query_x": .5, "tau": .5,
                 "source_variant": "literal_printed_table"}
    if any(config[k] != v for k, v in constants.items()):
        raise ValueError("This contribution fixes the printed mechanism and QDI query")


def transform(name, u):
    if name == "softplus":
        return max(u, 0.) + math.log1p(math.exp(-abs(u)))
    if name == "square":
        return max(u, 0.) ** 2 / 2.
    if name == "cubic":
        return u ** 3 / 3.
    if name == "log":
        # Table C.1: log(u), including downward jump at 2.
        # Fixed author snapshot eb6b83b, simulator.py:30 instead uses log(1+u).
        return (u - 2.) / 3. + math.log(3.) if u <= 2. else math.log(u)
    raise ValueError("Unknown transform")


def generate(config, n, seed):
    validate(config)
    if isinstance(n, bool) or not isinstance(n, int) or n < 1:
        raise ValueError("n must be a positive integer")
    if isinstance(seed, bool) or not isinstance(seed, int):
        raise ValueError("seed must be an integer")
    rng = random.Random(seed)
    data = {"X": [], "Y": []}
    for _ in range(n):
        x = rng.uniform(config["x_lower"], config["x_upper"])
        eta = rng.gauss(0., config["noise_sd"])
        data["X"].append(x)
        data["Y"].append(transform(config["transform"], x + eta))
    return data
