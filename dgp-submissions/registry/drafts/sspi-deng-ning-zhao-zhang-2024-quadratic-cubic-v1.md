# Folded-AR Gaussian Quadratic Interaction and Cubic Projection

> **Unverified extraction — scientific review required.**

**Primary area:** Semi-Supervised Inference

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Deng, S., Ning, Y., Zhao, J. and Zhang, H. (2024). Optimal and Safe Estimation for High-Dimensional Semi-Supervised Learning. Journal of the American Statistical Association 119(548), 2748-2759. DOI: 10.1080/01621459.2023.2277409.

**DOI:** 10.1080/01621459.2023.2277409 · **Source locator:** Pinned arXiv v2 Section 6.1, Model 2, printed/PDF p.16; p=500,nL=200 in Section 6.2 pp.17-19 and Figures 1-3 pp.18-20, select N/n=5. Page numbers refer to arXiv v2, not the journal.

## DGP / generation mechanism

**Sampling design:** Unit: individual; Dependence: Independent complete-data units; fixed labeled/unlabeled group indicators, not independent Bernoulli indicators. Coordinate dependence is specified in equations.; N Semantics: n is combined table row count; Labeled Reference: 200; Unlabeled Reference: 1000; Predictor Source: No external or oracle predictor supplied. Downstream nuisance regressors must be trained on labeled training folds only; cross-fitting and tuning belong to the later estimator benchmark. No prediction is substituted for Y_obs.

**Generator source:** [generator.py](../generators/sspi-deng-ning-zhao-zhang-2024-quadratic-cubic-v1.py)

**Keywords (source-described):** Interactions · Nonlinearity · High-dimensionality

**Observed variables**

X1–X500 (500 variables), R, Y_obs

<details>
<summary>All observed variable names</summary>

X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, X11, X12, X13, X14, X15, X16, X17, X18, X19, X20, X21, X22, X23, X24, X25, X26, X27, X28, X29, X30, X31, X32, X33, X34, X35, X36, X37, X38, X39, X40, X41, X42, X43, X44, X45, X46, X47, X48, X49, X50, X51, X52, X53, X54, X55, X56, X57, X58, X59, X60, X61, X62, X63, X64, X65, X66, X67, X68, X69, X70, X71, X72, X73, X74, X75, X76, X77, X78, X79, X80, X81, X82, X83, X84, X85, X86, X87, X88, X89, X90, X91, X92, X93, X94, X95, X96, X97, X98, X99, X100, X101, X102, X103, X104, X105, X106, X107, X108, X109, X110, X111, X112, X113, X114, X115, X116, X117, X118, X119, X120, X121, X122, X123, X124, X125, X126, X127, X128, X129, X130, X131, X132, X133, X134, X135, X136, X137, X138, X139, X140, X141, X142, X143, X144, X145, X146, X147, X148, X149, X150, X151, X152, X153, X154, X155, X156, X157, X158, X159, X160, X161, X162, X163, X164, X165, X166, X167, X168, X169, X170, X171, X172, X173, X174, X175, X176, X177, X178, X179, X180, X181, X182, X183, X184, X185, X186, X187, X188, X189, X190, X191, X192, X193, X194, X195, X196, X197, X198, X199, X200, X201, X202, X203, X204, X205, X206, X207, X208, X209, X210, X211, X212, X213, X214, X215, X216, X217, X218, X219, X220, X221, X222, X223, X224, X225, X226, X227, X228, X229, X230, X231, X232, X233, X234, X235, X236, X237, X238, X239, X240, X241, X242, X243, X244, X245, X246, X247, X248, X249, X250, X251, X252, X253, X254, X255, X256, X257, X258, X259, X260, X261, X262, X263, X264, X265, X266, X267, X268, X269, X270, X271, X272, X273, X274, X275, X276, X277, X278, X279, X280, X281, X282, X283, X284, X285, X286, X287, X288, X289, X290, X291, X292, X293, X294, X295, X296, X297, X298, X299, X300, X301, X302, X303, X304, X305, X306, X307, X308, X309, X310, X311, X312, X313, X314, X315, X316, X317, X318, X319, X320, X321, X322, X323, X324, X325, X326, X327, X328, X329, X330, X331, X332, X333, X334, X335, X336, X337, X338, X339, X340, X341, X342, X343, X344, X345, X346, X347, X348, X349, X350, X351, X352, X353, X354, X355, X356, X357, X358, X359, X360, X361, X362, X363, X364, X365, X366, X367, X368, X369, X370, X371, X372, X373, X374, X375, X376, X377, X378, X379, X380, X381, X382, X383, X384, X385, X386, X387, X388, X389, X390, X391, X392, X393, X394, X395, X396, X397, X398, X399, X400, X401, X402, X403, X404, X405, X406, X407, X408, X409, X410, X411, X412, X413, X414, X415, X416, X417, X418, X419, X420, X421, X422, X423, X424, X425, X426, X427, X428, X429, X430, X431, X432, X433, X434, X435, X436, X437, X438, X439, X440, X441, X442, X443, X444, X445, X446, X447, X448, X449, X450, X451, X452, X453, X454, X455, X456, X457, X458, X459, X460, X461, X462, X463, X464, X465, X466, X467, X468, X469, X470, X471, X472, X473, X474, X475, X476, X477, X478, X479, X480, X481, X482, X483, X484, X485, X486, X487, X488, X489, X490, X491, X492, X493, X494, X495, X496, X497, X498, X499, X500, R, Y_obs

</details>

**Latent variables**

Z1, epsilon

**Latent-variable identification:** explicit structured metadata

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

**Covariates**

```math
Z\sim \mathcal{N}_{500}(0,\Sigma)
```

```math
\Sigma_{jk}=0.3^{\lvert j-k\rvert}
```

```math
X_{1}=\lvert Z_{1}\rvert
```

```math
\mathrm{Xj}=\mathrm{Zj} \text{ for } j>1
```

Exact stationary AR recursion generates Z.

**Response**

```math
Y = 0.6 (X_{1}+X_{2})^{2} + 0.4 X_{4}^{3} - X_{5} + 2 X_{6} + \varepsilon
```

```math
\varepsilon\sim \mathcal{N}(0,1)
```

independent of Z and all other units

**Sampling**

Source notation retained without guessing:

<pre>Independent iid labeled and unlabeled samples from the same complete-data population</pre>

```math
\mathrm{nL}=200,\mathrm{nU}=1000 \mathrm{reference}
```

Export X1..X500,R,Y_obs.

<details>
<summary>Original source equations (verbatim)</summary>

<pre>
Z~N_500(0,Sigma), Sigma_jk=0.3^|j-k|; X1=abs(Z1), Xj=Zj for j&gt;1. Exact stationary AR recursion generates Z.
Y = 0.6 (X1+X2)^2 + 0.4 X4^3 - X5 + 2 X6 + epsilon; epsilon~N(0,1) independent of Z and all other units.
Independent iid labeled and unlabeled samples from the same complete-data population; nL=200,nU=1000 reference. Export X1..X500,R,Y_obs.
</pre>

</details>


## Parameter scenarios, estimands and truth

| Scenario | Estimand | Definition | Reported value |
|---|---|---|---|
| source_formula_fixed | Population least-squares projection slope | Coordinate 4 of beta in argmin_(alpha,beta) E[(Y-alpha-X^T beta)^2]. All 500 observed covariates are included, with an intercept. | 1.2000000000000002 |

**Original submitted target notation:** beta_4


## Identifiability assumptions

- Independent units and independent standard Gaussian outcome noise.
- Labeled and unlabeled groups share one population; fixed group counts independent of data.
- Positive definite covariance of centered X and finite response second moment.
- R masks Y_obs; unlabeled zero values are placeholders.

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Adaptations from the source (submitted, unverified):**

- Map independent labeled/unlabeled samples to one table with n=total rows. nL=max(1,min(n-1,floor(n*200/1200))); nU=n-nL. At n=1200 the source sample counts (200,1000) are exact. R=0 implies Y_obs=0 placeholder, not observed zero.
- Export raw X1=abs(Z1) and raw Y from the printed response formula. Define the target as one slope in the population linear projection WITH intercept. These slopes equal those from population-centering X and Y as in the paper; do not fit a no-intercept regression to the exported raw table.
- Select one scalar coordinate of the original vector regression target, not a different DGP. No fitted prediction, oracle response or hidden noise is exported.
- Independent PCG64 implementation. All coefficients are fixed across rows and replications; p=500,nL=200,N/n=5 selected from source experiments. No original estimation algorithm or benchmark is reproduced.

**Warnings:**

- Nothing automatically flagged; this does NOT equal scientific acceptance.
