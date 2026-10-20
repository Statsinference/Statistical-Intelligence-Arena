# Method interface plan — protocol v0.3

**No estimator or training implementation is supplied.** methods.json is an illustrative registry with planned entries. The reference mediation walkthrough is ../demo/README.md.

Layer B supplies the observed data, task/target, role mapping, query contract, identifying design knowledge, nominal level and budget. Return one schema-0.2.0 record per attempted method/DGP/replicate/target/query. The truth oracle and hidden labels are excluded. Optional Layer A is evaluated independently.

## Required comparison entries

Provide a justified implemented classical reference and a PFN interface for the same estimand. The PFN interface may explicitly report unsupported with a reason. Do not silently replace NIE/CATE/LATE with ATE. For the illustrated linear mediation model, regression plug-in plus a fully rerun bootstrap is one possible reference, pending a complete interval justification; no universal best baseline is declared.

Classify execution honestly:
- native_frozen: supported target directly from the fixed checkpoint, with no declared adaptation;
- adapted: specified correction, calibration or target adaptation using only permitted information;
- refit: per-dataset fitting under the task contract.

A contributor need not pretrain a model. The proposed small reference PFN is a separate planned path in ../configs/train.yaml. Reused models need exact checkpoint/hash/license, training exposure and target support. If joint multi-task training is proposed later, explicit task/role/target/query conditioning and compatible outputs are required.

## Supervision and uncertainty

Record whether offline labels are true parameters, FSP-style teachers, distillation or another justified construction. Derive any teacher for the actual causal functional. Optional mean/variance heads must define targets and CI construction; they do not automatically provide valid uncertainty.

Predeclare tuning, selection and calibration using public development only. Match total observed labels and disclose context/calibration/tuning allocations, allowed reuse and all computation. Separate offline training, loading and warmed end-to-end costs.

TODO: actual entrypoints, method versions, assumptions/support, CI formula, missing-data policy, failure/abstention behavior and evidence. Weak-IV disconnected parameter sets require an extension; core connected intervals may be unbounded. Generic prediction_set compatibility does not add a future-response track.
