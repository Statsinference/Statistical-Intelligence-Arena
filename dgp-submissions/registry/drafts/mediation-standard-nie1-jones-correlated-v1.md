# Standard NIE1 adaptation: jones correlated

> **Unverified extraction — scientific review required.**

**Primary area:** Mediation — Direct and Indirect Effects

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Jones, J., Ertefaie, A. and Strawderman, R. L. (2025). Causal mediation analysis: selection with asymptotically valid inference. Journal of the Royal Statistical Society: Series B 87(3), 678–700. DOI: 10.1093/jrsssb/qkae109.

**DOI:** 10.1093/jrsssb/qkae109 · **Source locator:** Final article §5, Simulation B; compared with author code mediation-new-sims/R/sim_conf.R, function do_sim_paths, lines 84–117, commit 7617776b1a6415a185e18d336a5709c4d38f0555. Paper prose is followed where the two differ.; adaptation: bundled SCIENTIFIC_SPEC.md and nie_standard_v1/generators.py::_draw

## DGP / generation mechanism

**Sampling design:** IID observations at a fixed structural configuration; separate mechanism and observation seeds.

**Generator source:** [generator.py](https://github.com/Statsinference/stats-inference-arena/blob/main/dgp-submissions/registry/generators/mediation-standard-nie1-jones-correlated-v1.py)

**Keywords (source-described):** High-dimensionality

**Observed variables**

A, M1, M2, M3, M4, M5, M6, M7, M8, M9, M10, M11, M12, M13, M14, M15, M16, M17, M18, M19, M20, M21, M22, M23, M24, M25, M26, M27, M28, M29, M30, M31, M32, M33, M34, M35, M36, M37, M38, M39, M40, M41, M42, M43, M44, M45, M46, M47, M48, M49, M50, M51, M52, M53, M54, M55, M56, M57, M58, M59, M60, M61, M62, M63, M64, M65, M66, M67, M68, M69, M70, M71, M72, M73, M74, M75, M76, M77, M78, M79, M80, M81, M82, M83, M84, M85, M86, M87, M88, M89, M90, M91, M92, M93, M94, M95, M96, M97, M98, M99, M100, Y

**Latent variables**

Not explicitly identified (review required)

**Latent-variable identification:** explicit structured metadata

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

**target**

$$
\psi=\mathbb{E}[Y(1,M(1))-Y(1,M(0))]
$$

**adapted structural equations**

Source notation retained without guessing:

<pre>q=int(c[&quot;p&quot;])
within=float(c[&quot;rho_within&quot;])
bridge=float(c[&quot;rho_bridge&quot;])
if not 0&lt;=bridge&lt;=within&lt;1: raise ValueError(&quot;Need 0 &lt;= bridge &lt;= within &lt; 1&quot;)
a=r.binomial(1,c[&quot;p_treatment&quot;],n)
m=np.sqrt(1-within)*r.standard_normal((n,q))+np.sqrt(bridge)*r.standard_normal((n,1))
group=r.standard_normal((n,2))
m[:,:2]+=np.sqrt(within-bridge)*group[:,0,None]
m[:,2:]+=np.sqrt(within-bridge)*group[:,1,None]
ai=np.asarray(c[&quot;a_to_m_indices&quot;])-1
bi=np.asarray(c[&quot;m_to_y_indices&quot;])-1
if np.any(ai&lt;0) or np.any(ai&gt;=q) or np.any(bi&lt;0) or np.any(bi&gt;=q): raise ValueError(&quot;Index outside mediator vector&quot;)
m[:,ai]+=c[&quot;a_to_m_coefficient&quot;]*a[:,None]
y=c[&quot;direct_effect&quot;]*a+c[&quot;m_to_y_coefficient&quot;]*m[:,bi].sum(1)+c[&quot;outcome_error_sd&quot;]*r.standard_normal(n)
return np.empty((n,0)),a,m,y,[&quot;continuous&quot;]*q,[],&quot;continuous&quot;</pre>

<details>
<summary>Original source equations (verbatim)</summary>

<pre>
NIE1 = E[Y(1,M(1))-Y(1,M(0))]
q=int(c[&quot;p&quot;])
within=float(c[&quot;rho_within&quot;])
bridge=float(c[&quot;rho_bridge&quot;])
if not 0&lt;=bridge&lt;=within&lt;1: raise ValueError(&quot;Need 0 &lt;= bridge &lt;= within &lt; 1&quot;)
a=r.binomial(1,c[&quot;p_treatment&quot;],n)
m=np.sqrt(1-within)*r.standard_normal((n,q))+np.sqrt(bridge)*r.standard_normal((n,1))
group=r.standard_normal((n,2))
m[:,:2]+=np.sqrt(within-bridge)*group[:,0,None]
m[:,2:]+=np.sqrt(within-bridge)*group[:,1,None]
ai=np.asarray(c[&quot;a_to_m_indices&quot;])-1
bi=np.asarray(c[&quot;m_to_y_indices&quot;])-1
if np.any(ai&lt;0) or np.any(ai&gt;=q) or np.any(bi&lt;0) or np.any(bi&gt;=q): raise ValueError(&quot;Index outside mediator vector&quot;)
m[:,ai]+=c[&quot;a_to_m_coefficient&quot;]*a[:,None]
y=c[&quot;direct_effect&quot;]*a+c[&quot;m_to_y_coefficient&quot;]*m[:,bi].sum(1)+c[&quot;outcome_error_sd&quot;]*r.standard_normal(n)
return np.empty((n,0)),a,m,y,[&quot;continuous&quot;]*q,[],&quot;continuous&quot;
</pre>

</details>


## Parameter scenarios, estimands and truth

| Scenario | Estimand | Definition | Reported value | Evidence status |
|---|---|---|---|---|
| native | NIE | NIE = E[Y(1,M(1))-Y(1,M(0))] in the adapted fixed-SEM superpopulation, jointly intervening on the complete mediator vector. | 2 | reported_numeric |

## Identifiability assumptions

- Independent exogenous structural errors and iid units conditional on fixed configuration.
- No treatment-induced mediator-outcome confounder remains in the adapted SEM.
- Causal identification additionally requires consistency, exchangeability/cross-world conditions and treatment/mediator support; treatment randomization alone is insufficient.

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Warnings:**

- Nothing automatically flagged; this does NOT equal scientific acceptance.
