"""Standard NIE1 adaptation: cheng; extract the whole ZIP for nie_standard_v1.

This is a new adapted SEM/target, not an overwrite of the source-paper DGP.
Only generate()'s observed columns belong in a method input. Read the bundled
README.md, SCIENTIFIC_SPEC.md and this record's source_audit.json first.
"""
from nie_standard_v1 import sample_task as _task, sample_mechanism as _mechanism
from nie_standard_v1 import truth as _truth, as_columns

SOURCE_ID = 'cheng'

def sample_mechanism(mechanism_seed=0, *, randomize=False):
    return _mechanism(SOURCE_ID, mechanism_seed, randomize=randomize)

def sample_task(n, observation_seed, *, mechanism_seed=0, config=None,
                randomize=False, compute_truth=False):
    return _task(SOURCE_ID, n, observation_seed, mechanism_seed=mechanism_seed,
                 config=config, randomize=randomize, compute_truth=compute_truth)

def generate(config, n, seed):
    """Arena-compatible observed-only columns; seed redraws rows, not parameters."""
    return as_columns(sample_task(n, seed, config=config, compute_truth=False))

def truth(config=None):
    return _truth(SOURCE_ID, config)
