# Kernel Meets Sieve Example 5.1: high-dimensional sparse additive regression

> **Unverified extraction — scientific review required.**

**Primary area:** Nonparametric Regression

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Junwei Lu, Mladen Kolar and Han Liu (2020), Kernel Meets Sieve: Post-Regularization Confidence Bands for Sparse Additive Model, Journal of the American Statistical Association 115(532):2084–2099, DOI: 10.1080/01621459.2019.1689984. DGP locator: arXiv:1503.02978v2 (2018-02-12).

**DOI:** — · **Source locator:** Preprint arXiv:1503.02978v2, PDF p.21, Section 5.1, Example 5.1 (generation equations and parameters); PDF p.22 for the original centered-band target. No code commit is identified in the source section or supplied materials (missing).

## DGP / generation mechanism

**Sampling design:** Unit: One iid row (X_1,...,X_600,Y); Dependence: Rows are iid; covariates within a row share U_i and hence have pairwise correlation t^2/(1+t^2)=0.09/(1.09)≈0.0825688 for j≠j'.

**Generator source:** [generator.py](../generators/nri-highdim-sparse-additive-v1.py)

**Keywords (source-described):** Nonlinearity · High-dimensionality

**Observed variables**

X1–X600 (600 variables), Y

<details>
<summary>All observed variable names</summary>

X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, X11, X12, X13, X14, X15, X16, X17, X18, X19, X20, X21, X22, X23, X24, X25, X26, X27, X28, X29, X30, X31, X32, X33, X34, X35, X36, X37, X38, X39, X40, X41, X42, X43, X44, X45, X46, X47, X48, X49, X50, X51, X52, X53, X54, X55, X56, X57, X58, X59, X60, X61, X62, X63, X64, X65, X66, X67, X68, X69, X70, X71, X72, X73, X74, X75, X76, X77, X78, X79, X80, X81, X82, X83, X84, X85, X86, X87, X88, X89, X90, X91, X92, X93, X94, X95, X96, X97, X98, X99, X100, X101, X102, X103, X104, X105, X106, X107, X108, X109, X110, X111, X112, X113, X114, X115, X116, X117, X118, X119, X120, X121, X122, X123, X124, X125, X126, X127, X128, X129, X130, X131, X132, X133, X134, X135, X136, X137, X138, X139, X140, X141, X142, X143, X144, X145, X146, X147, X148, X149, X150, X151, X152, X153, X154, X155, X156, X157, X158, X159, X160, X161, X162, X163, X164, X165, X166, X167, X168, X169, X170, X171, X172, X173, X174, X175, X176, X177, X178, X179, X180, X181, X182, X183, X184, X185, X186, X187, X188, X189, X190, X191, X192, X193, X194, X195, X196, X197, X198, X199, X200, X201, X202, X203, X204, X205, X206, X207, X208, X209, X210, X211, X212, X213, X214, X215, X216, X217, X218, X219, X220, X221, X222, X223, X224, X225, X226, X227, X228, X229, X230, X231, X232, X233, X234, X235, X236, X237, X238, X239, X240, X241, X242, X243, X244, X245, X246, X247, X248, X249, X250, X251, X252, X253, X254, X255, X256, X257, X258, X259, X260, X261, X262, X263, X264, X265, X266, X267, X268, X269, X270, X271, X272, X273, X274, X275, X276, X277, X278, X279, X280, X281, X282, X283, X284, X285, X286, X287, X288, X289, X290, X291, X292, X293, X294, X295, X296, X297, X298, X299, X300, X301, X302, X303, X304, X305, X306, X307, X308, X309, X310, X311, X312, X313, X314, X315, X316, X317, X318, X319, X320, X321, X322, X323, X324, X325, X326, X327, X328, X329, X330, X331, X332, X333, X334, X335, X336, X337, X338, X339, X340, X341, X342, X343, X344, X345, X346, X347, X348, X349, X350, X351, X352, X353, X354, X355, X356, X357, X358, X359, X360, X361, X362, X363, X364, X365, X366, X367, X368, X369, X370, X371, X372, X373, X374, X375, X376, X377, X378, X379, X380, X381, X382, X383, X384, X385, X386, X387, X388, X389, X390, X391, X392, X393, X394, X395, X396, X397, X398, X399, X400, X401, X402, X403, X404, X405, X406, X407, X408, X409, X410, X411, X412, X413, X414, X415, X416, X417, X418, X419, X420, X421, X422, X423, X424, X425, X426, X427, X428, X429, X430, X431, X432, X433, X434, X435, X436, X437, X438, X439, X440, X441, X442, X443, X444, X445, X446, X447, X448, X449, X450, X451, X452, X453, X454, X455, X456, X457, X458, X459, X460, X461, X462, X463, X464, X465, X466, X467, X468, X469, X470, X471, X472, X473, X474, X475, X476, X477, X478, X479, X480, X481, X482, X483, X484, X485, X486, X487, X488, X489, X490, X491, X492, X493, X494, X495, X496, X497, X498, X499, X500, X501, X502, X503, X504, X505, X506, X507, X508, X509, X510, X511, X512, X513, X514, X515, X516, X517, X518, X519, X520, X521, X522, X523, X524, X525, X526, X527, X528, X529, X530, X531, X532, X533, X534, X535, X536, X537, X538, X539, X540, X541, X542, X543, X544, X545, X546, X547, X548, X549, X550, X551, X552, X553, X554, X555, X556, X557, X558, X559, X560, X561, X562, X563, X564, X565, X566, X567, X568, X569, X570, X571, X572, X573, X574, X575, X576, X577, X578, X579, X580, X581, X582, X583, X584, X585, X586, X587, X588, X589, X590, X591, X592, X593, X594, X595, X596, X597, X598, X599, X600, Y

</details>

**Latent variables**

Not explicitly identified (review required)

**Latent-variable identification:** not explicitly specified

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

**Shared covariate construction**

$$
\mathrm{For} \text{ each } \mathrm{row} i \text{ and } j=1,\ldots ,600: W_{ij},U_{i} \mathrm{are} \text{ mutually } \text{ iid } \mathrm{Uniform}[0,1]
$$

$$
X_{ij}=(W_{ij}+0.3 U_{i})/1.3.
$$

**Sparse additive response**

$$
Y_{i}=\sum_{j=1}^{4} f_{j}(X_{ij})+\varepsilon_{i}, \varepsilon_{i}\overset{\mathrm{iid}}{\sim} \mathcal{N}(0,1.5^{2})
$$

independent of the covariates

**Active functions**

$$
f_{1}(t)=6[0.1 \sin(2 \pi t)+0.2 \cos(2 \pi t)+0.3 \sin^{2}(2 \pi t)+0.4 \cos^{3}(2 \pi t)+0.5 \sin^{3}(2 \pi t)]
$$

$$
f_{2}(t)=3(2t-1)^{2}
$$

$$
f_{3}(t)=5t
$$

$$
f_{4}(t)=4 \sin(2 \pi t)/(2-\sin(2 \pi t))
$$

$$
f_{j}=0 \text{ for } j=5,\ldots ,600.
$$

**Library estimand**

$$
m(x^{\ast})=\mathbb{E}[Y\mid X=x^{\ast}]=\sum_{j=1}^{4} f_{j}(0.5), x^{\ast}=(0.5,\ldots ,0.5), \text{ with } \mathrm{truth} -1.1.
$$

<details>
<summary>Original source equations (verbatim)</summary>

<pre>
For each row i and j=1,...,600: W_ij,U_i are mutually iid Uniform[0,1]; X_ij=(W_ij+0.3 U_i)/1.3.
Y_i=sum_{j=1}^4 f_j(X_ij)+epsilon_i, epsilon_i iid Normal(0,1.5^2), independent of the covariates.
f1(t)=6[0.1 sin(2 pi t)+0.2 cos(2 pi t)+0.3 sin^2(2 pi t)+0.4 cos^3(2 pi t)+0.5 sin^3(2 pi t)]; f2(t)=3(2t-1)^2; f3(t)=5t; f4(t)=4 sin(2 pi t)/(2-sin(2 pi t)); f_j=0 for j=5,...,600.
m(x*)=E[Y|X=x*]=sum_{j=1}^4 f_j(0.5), x*=(0.5,...,0.5), with truth -1.1.
</pre>

</details>


## Parameter scenarios, estimands and truth

| Scenario | Estimand | Definition | Reported value | Evidence status |
|---|---|---|---|---|
| original | Pointwise conditional mean | Noncausal pointwise conditional mean under the declared sparse-additive DGP, evaluated at the fixed query x*=(0.5,...,0.5). Since E[epsilon\|X]=0, m(x*) equals the sum of the four active component functions at the query; inactive coordinates contribute zero. This is a library adaptation and is not the paper's simultaneous confidence-band target. | -1.1000000000000003 | reported_numeric |

**Original submitted target notation:** m(x*) = E[Y \| X=x*] = sum_{j=1}^4 f_j(0.5), x*=(0.5,...,0.5) in R^600


## Identifiability assumptions

- Rows i are iid sampling units; within a row the 600 covariates are dependent through the shared latent U_i, while W_ij and U_i are mutually iid Uniform[0,1] before the displayed transformation.
- The observation model is fully observed numeric X_1,...,X_600,Y with epsilon independent of the covariates and E[epsilon\|X]=0.
- The fixed query x* lies in the covariate support [0,1]^600; the four displayed component functions are finite and smooth on [0,1].
- This is a noncausal regression functional: no treatment, intervention, no-unmeasured-confounding, mediation, or causal identification assumption is asserted.

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Adaptations from the source (submitted, unverified):**

- Use row-indexed W_ij and shared U_i to implement the source's iid copies of the vector X; this is an implementation indexing choice, not an independent-coordinate replacement.
- The library target is the full conditional mean m(x*)=sum_j f_j(x*_j) at fixed x*=(0.5,...,0.5), rather than the paper's centered component f1(t)-E[f1(X1)] confidence band and inactive f5 band.
- Keep the source response equation uncentered: no intercept insertion and no centering of any f_j during generation. The local check uses a scalar oracle and does not reproduce the paper's estimator, bootstrap, 500 repetitions, or coverage study.

**Warnings:**

- No explicit latent-variable metadata or reliably identifiable latent declarations; absence from this list does not prove that no latent variables exist.
