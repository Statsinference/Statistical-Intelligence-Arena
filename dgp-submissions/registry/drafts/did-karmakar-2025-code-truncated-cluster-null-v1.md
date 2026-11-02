# Karmakar et al. official2024 code-version truncated cluster null

> **Unverified extraction — scientific review required.**

**Primary area:** DiD / Synthetic Control

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Karmakar, Mukherjee, Kar (2025), Using Penalized Synthetic Controls on Truncated Data, JASA120(549):64–79

**DOI:** 10.6084/m9.figshare.27115129.v2 · **Source locator:** Official2024 file49432675 simulation/gen_control.R7–88;3assign_trt.R3–37;run_sc_simulation_comparison.R18–37; article DOI10.1080/01621459.2024.2406583

## DGP / generation mechanism

**Sampling design:** Unit: One30-unit panel; n must equal30,3groups each10;45pre10post observed.; Dependence: Unit intercepts persistent; independent normal errors; shared group renewal damping induces serial and within-group dependence; treatment depends on pre outcomes.

**Generator source:** [generator.py](../generators/did-karmakar-2025-code-truncated-cluster-null-v1.py)

**Keywords (source-described):** Nonlinearity · Panel data

**Observed variables**

G, C, Y_pre001, Y_pre002, Y_pre003, Y_pre004, Y_pre005, Y_pre006, Y_pre007, Y_pre008, Y_pre009, Y_pre010, Y_pre011, Y_pre012, Y_pre013, Y_pre014, Y_pre015, Y_pre016, Y_pre017, Y_pre018, Y_pre019, Y_pre020, Y_pre021, Y_pre022, Y_pre023, Y_pre024, Y_pre025, Y_pre026, Y_pre027, Y_pre028, Y_pre029, Y_pre030, Y_pre031, Y_pre032, Y_pre033, Y_pre034, Y_pre035, Y_pre036, Y_pre037, Y_pre038, Y_pre039, Y_pre040, Y_pre041, Y_pre042, Y_pre043, Y_pre044, Y_pre045, Y_post001, Y_post002, Y_post003, Y_post004, Y_post005, Y_post006, Y_post007, Y_post008, Y_post009, Y_post010

**Latent variables**

Z_it

**Latent-variable identification:** candidates from equations need review

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

$$
Z_it=a_i+\mathrm{floor}((t-1)/4)+2\cdot ((t-1)mod4)+eps_it-80q_ct
$$

a_i iidU(10,60),eps iidN(0,25)

$$
Y_it=\max(Z_it,0),t_{1}..55
$$

q from source inclusive floor/ceil renewal algorithm across99 periods

one selected per10-unit group

$$
p_i=(1+mean(Y_i,20:45))/sum_group(1+mean(Y_j,20:45))
$$

$$
Eff=(0,0,0)
$$

$$
ATT=SATT=0
$$

<details>
<summary>Original source equations (verbatim)</summary>

<pre>
Z_it=a_i+floor((t-1)/4)+2*((t-1)mod4)+eps_it-80q_ct; a_i iidU(10,60),eps iidN(0,25)
Y_it=max(Z_it,0),t1..55; q from source inclusive floor/ceil renewal algorithm across99 periods
one selected per10-unit group; p_i=(1+mean(Y_i,20:45))/sum_group(1+mean(Y_j,20:45))
Eff=(0,0,0); ATT=SATT=0
</pre>

</details>


## Parameter scenarios, estimands and truth

| Scenario | Estimand | Definition | True value | Evidence status |
|---|---|---|---|---|
| baseline | ATT | Population average post-period treatment effect conditional on selected treated units; equals finite-panel SATT=0 under sharp null. | 0.0 | reported_numeric |

## Identifiability assumptions

- Code id1 heteroTRUE sets every group effect0.
- Consistency and no interference; history-dependent assignment retained.

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Warnings:**

- Latent-variable candidates inferred from source equations; confirm their roles and completeness against the original paper or generator.
