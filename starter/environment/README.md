# Environment plan — protocol v0.3

The present Python format checks use the standard library (Python 3.9+). No estimator, model dependency, data generator, training runner, statistical evaluator, environment lock or measured benchmark is supplied. The fixture check can additionally compare JSON Schema when jsonschema is installed; it does not require that dependency.

As part of implementation and before training/evaluation, record:
- exact language/package/system versions and immutable environment lock;
- source/DGP/configuration/checkpoint hashes and licenses;
- real generation, training, inference and evaluation entrypoints;
- CPU/GPU, memory, precision, threads, batching and resource/timeout policy;
- seed handling for data, algorithm and training initialization;
- all offline teacher/training, loading and warmed end-to-end costs.

TODO: runnable environment and commands. configs/train.yaml and configs/evaluate.yaml are human-reviewed plans, not executable programs. Do not claim that the structural checker validates their YAML semantics or implements the planned workflow.
