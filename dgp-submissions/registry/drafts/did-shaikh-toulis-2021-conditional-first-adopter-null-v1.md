# First-adopter Cox adoption with AR(1) outcomes conditional on whole-experiment success

> **Unverified extraction — scientific review required.**

**Primary area:** Legacy DiD / Synthetic Control — classification needed

**Suggested cross-tags (unverified):** none

## Reference paper

**Citation:** Shaikh, A. M., and Toulis, P. (2021). Randomization Tests in Observational Studies With Staggered Adoption of Treatment. Journal of the American Statistical Association, 116(536), 1835–1848. DOI:10.1080/01621459.2021.1974458

**DOI:** 10.1080/01621459.2021.1974458 · **Source locator:** file31887428; code_original.zip Section4 functions.R38–122,223–247; Section_4.2.R261–289; author commit4e24efd06b49f6d18508086f779cbf1ac91a608e

## DGP / generation mechanism

**Sampling design:** Unit: Exactly25 unit rows and1000 outcomes; horizon random from10000 calibration panels; Dependence: Shared random horizon and success conditioning induce panel-design dependence; conditional innovations iid normal with unit AR1 recursion.

**Generator source:** [generator.py](../generators/did-shaikh-toulis-2021-conditional-first-adopter-null-v1.py)

**Keywords (source-described):** Nonlinearity

**Observed variables**

G, X1, Tmax, first_adoption, pre_last_index, Y_t0001, Y_t0002, Y_t0003, Y_t0004, Y_t0005, Y_t0006, Y_t0007, Y_t0008, Y_t0009, Y_t0010, Y_t0011, Y_t0012, Y_t0013, Y_t0014, Y_t0015, Y_t0016, Y_t0017, Y_t0018, Y_t0019, Y_t0020, Y_t0021, Y_t0022, Y_t0023, Y_t0024, Y_t0025, Y_t0026, Y_t0027, Y_t0028, Y_t0029, Y_t0030, Y_t0031, Y_t0032, Y_t0033, Y_t0034, Y_t0035, Y_t0036, Y_t0037, Y_t0038, Y_t0039, Y_t0040, Y_t0041, Y_t0042, Y_t0043, Y_t0044, Y_t0045, Y_t0046, Y_t0047, Y_t0048, Y_t0049, Y_t0050, Y_t0051, Y_t0052, Y_t0053, Y_t0054, Y_t0055, Y_t0056, Y_t0057, Y_t0058, Y_t0059, Y_t0060, Y_t0061, Y_t0062, Y_t0063, Y_t0064, Y_t0065, Y_t0066, Y_t0067, Y_t0068, Y_t0069, Y_t0070, Y_t0071, Y_t0072, Y_t0073, Y_t0074, Y_t0075, Y_t0076, Y_t0077, Y_t0078, Y_t0079, Y_t0080, Y_t0081, Y_t0082, Y_t0083, Y_t0084, Y_t0085, Y_t0086, Y_t0087, Y_t0088, Y_t0089, Y_t0090, Y_t0091, Y_t0092, Y_t0093, Y_t0094, Y_t0095, Y_t0096, Y_t0097, Y_t0098, Y_t0099, Y_t0100, Y_t0101, Y_t0102, Y_t0103, Y_t0104, Y_t0105, Y_t0106, Y_t0107, Y_t0108, Y_t0109, Y_t0110, Y_t0111, Y_t0112, Y_t0113, Y_t0114, Y_t0115, Y_t0116, Y_t0117, Y_t0118, Y_t0119, Y_t0120, Y_t0121, Y_t0122, Y_t0123, Y_t0124, Y_t0125, Y_t0126, Y_t0127, Y_t0128, Y_t0129, Y_t0130, Y_t0131, Y_t0132, Y_t0133, Y_t0134, Y_t0135, Y_t0136, Y_t0137, Y_t0138, Y_t0139, Y_t0140, Y_t0141, Y_t0142, Y_t0143, Y_t0144, Y_t0145, Y_t0146, Y_t0147, Y_t0148, Y_t0149, Y_t0150, Y_t0151, Y_t0152, Y_t0153, Y_t0154, Y_t0155, Y_t0156, Y_t0157, Y_t0158, Y_t0159, Y_t0160, Y_t0161, Y_t0162, Y_t0163, Y_t0164, Y_t0165, Y_t0166, Y_t0167, Y_t0168, Y_t0169, Y_t0170, Y_t0171, Y_t0172, Y_t0173, Y_t0174, Y_t0175, Y_t0176, Y_t0177, Y_t0178, Y_t0179, Y_t0180, Y_t0181, Y_t0182, Y_t0183, Y_t0184, Y_t0185, Y_t0186, Y_t0187, Y_t0188, Y_t0189, Y_t0190, Y_t0191, Y_t0192, Y_t0193, Y_t0194, Y_t0195, Y_t0196, Y_t0197, Y_t0198, Y_t0199, Y_t0200, Y_t0201, Y_t0202, Y_t0203, Y_t0204, Y_t0205, Y_t0206, Y_t0207, Y_t0208, Y_t0209, Y_t0210, Y_t0211, Y_t0212, Y_t0213, Y_t0214, Y_t0215, Y_t0216, Y_t0217, Y_t0218, Y_t0219, Y_t0220, Y_t0221, Y_t0222, Y_t0223, Y_t0224, Y_t0225, Y_t0226, Y_t0227, Y_t0228, Y_t0229, Y_t0230, Y_t0231, Y_t0232, Y_t0233, Y_t0234, Y_t0235, Y_t0236, Y_t0237, Y_t0238, Y_t0239, Y_t0240, Y_t0241, Y_t0242, Y_t0243, Y_t0244, Y_t0245, Y_t0246, Y_t0247, Y_t0248, Y_t0249, Y_t0250, Y_t0251, Y_t0252, Y_t0253, Y_t0254, Y_t0255, Y_t0256, Y_t0257, Y_t0258, Y_t0259, Y_t0260, Y_t0261, Y_t0262, Y_t0263, Y_t0264, Y_t0265, Y_t0266, Y_t0267, Y_t0268, Y_t0269, Y_t0270, Y_t0271, Y_t0272, Y_t0273, Y_t0274, Y_t0275, Y_t0276, Y_t0277, Y_t0278, Y_t0279, Y_t0280, Y_t0281, Y_t0282, Y_t0283, Y_t0284, Y_t0285, Y_t0286, Y_t0287, Y_t0288, Y_t0289, Y_t0290, Y_t0291, Y_t0292, Y_t0293, Y_t0294, Y_t0295, Y_t0296, Y_t0297, Y_t0298, Y_t0299, Y_t0300, Y_t0301, Y_t0302, Y_t0303, Y_t0304, Y_t0305, Y_t0306, Y_t0307, Y_t0308, Y_t0309, Y_t0310, Y_t0311, Y_t0312, Y_t0313, Y_t0314, Y_t0315, Y_t0316, Y_t0317, Y_t0318, Y_t0319, Y_t0320, Y_t0321, Y_t0322, Y_t0323, Y_t0324, Y_t0325, Y_t0326, Y_t0327, Y_t0328, Y_t0329, Y_t0330, Y_t0331, Y_t0332, Y_t0333, Y_t0334, Y_t0335, Y_t0336, Y_t0337, Y_t0338, Y_t0339, Y_t0340, Y_t0341, Y_t0342, Y_t0343, Y_t0344, Y_t0345, Y_t0346, Y_t0347, Y_t0348, Y_t0349, Y_t0350, Y_t0351, Y_t0352, Y_t0353, Y_t0354, Y_t0355, Y_t0356, Y_t0357, Y_t0358, Y_t0359, Y_t0360, Y_t0361, Y_t0362, Y_t0363, Y_t0364, Y_t0365, Y_t0366, Y_t0367, Y_t0368, Y_t0369, Y_t0370, Y_t0371, Y_t0372, Y_t0373, Y_t0374, Y_t0375, Y_t0376, Y_t0377, Y_t0378, Y_t0379, Y_t0380, Y_t0381, Y_t0382, Y_t0383, Y_t0384, Y_t0385, Y_t0386, Y_t0387, Y_t0388, Y_t0389, Y_t0390, Y_t0391, Y_t0392, Y_t0393, Y_t0394, Y_t0395, Y_t0396, Y_t0397, Y_t0398, Y_t0399, Y_t0400, Y_t0401, Y_t0402, Y_t0403, Y_t0404, Y_t0405, Y_t0406, Y_t0407, Y_t0408, Y_t0409, Y_t0410, Y_t0411, Y_t0412, Y_t0413, Y_t0414, Y_t0415, Y_t0416, Y_t0417, Y_t0418, Y_t0419, Y_t0420, Y_t0421, Y_t0422, Y_t0423, Y_t0424, Y_t0425, Y_t0426, Y_t0427, Y_t0428, Y_t0429, Y_t0430, Y_t0431, Y_t0432, Y_t0433, Y_t0434, Y_t0435, Y_t0436, Y_t0437, Y_t0438, Y_t0439, Y_t0440, Y_t0441, Y_t0442, Y_t0443, Y_t0444, Y_t0445, Y_t0446, Y_t0447, Y_t0448, Y_t0449, Y_t0450, Y_t0451, Y_t0452, Y_t0453, Y_t0454, Y_t0455, Y_t0456, Y_t0457, Y_t0458, Y_t0459, Y_t0460, Y_t0461, Y_t0462, Y_t0463, Y_t0464, Y_t0465, Y_t0466, Y_t0467, Y_t0468, Y_t0469, Y_t0470, Y_t0471, Y_t0472, Y_t0473, Y_t0474, Y_t0475, Y_t0476, Y_t0477, Y_t0478, Y_t0479, Y_t0480, Y_t0481, Y_t0482, Y_t0483, Y_t0484, Y_t0485, Y_t0486, Y_t0487, Y_t0488, Y_t0489, Y_t0490, Y_t0491, Y_t0492, Y_t0493, Y_t0494, Y_t0495, Y_t0496, Y_t0497, Y_t0498, Y_t0499, Y_t0500, Y_t0501, Y_t0502, Y_t0503, Y_t0504, Y_t0505, Y_t0506, Y_t0507, Y_t0508, Y_t0509, Y_t0510, Y_t0511, Y_t0512, Y_t0513, Y_t0514, Y_t0515, Y_t0516, Y_t0517, Y_t0518, Y_t0519, Y_t0520, Y_t0521, Y_t0522, Y_t0523, Y_t0524, Y_t0525, Y_t0526, Y_t0527, Y_t0528, Y_t0529, Y_t0530, Y_t0531, Y_t0532, Y_t0533, Y_t0534, Y_t0535, Y_t0536, Y_t0537, Y_t0538, Y_t0539, Y_t0540, Y_t0541, Y_t0542, Y_t0543, Y_t0544, Y_t0545, Y_t0546, Y_t0547, Y_t0548, Y_t0549, Y_t0550, Y_t0551, Y_t0552, Y_t0553, Y_t0554, Y_t0555, Y_t0556, Y_t0557, Y_t0558, Y_t0559, Y_t0560, Y_t0561, Y_t0562, Y_t0563, Y_t0564, Y_t0565, Y_t0566, Y_t0567, Y_t0568, Y_t0569, Y_t0570, Y_t0571, Y_t0572, Y_t0573, Y_t0574, Y_t0575, Y_t0576, Y_t0577, Y_t0578, Y_t0579, Y_t0580, Y_t0581, Y_t0582, Y_t0583, Y_t0584, Y_t0585, Y_t0586, Y_t0587, Y_t0588, Y_t0589, Y_t0590, Y_t0591, Y_t0592, Y_t0593, Y_t0594, Y_t0595, Y_t0596, Y_t0597, Y_t0598, Y_t0599, Y_t0600, Y_t0601, Y_t0602, Y_t0603, Y_t0604, Y_t0605, Y_t0606, Y_t0607, Y_t0608, Y_t0609, Y_t0610, Y_t0611, Y_t0612, Y_t0613, Y_t0614, Y_t0615, Y_t0616, Y_t0617, Y_t0618, Y_t0619, Y_t0620, Y_t0621, Y_t0622, Y_t0623, Y_t0624, Y_t0625, Y_t0626, Y_t0627, Y_t0628, Y_t0629, Y_t0630, Y_t0631, Y_t0632, Y_t0633, Y_t0634, Y_t0635, Y_t0636, Y_t0637, Y_t0638, Y_t0639, Y_t0640, Y_t0641, Y_t0642, Y_t0643, Y_t0644, Y_t0645, Y_t0646, Y_t0647, Y_t0648, Y_t0649, Y_t0650, Y_t0651, Y_t0652, Y_t0653, Y_t0654, Y_t0655, Y_t0656, Y_t0657, Y_t0658, Y_t0659, Y_t0660, Y_t0661, Y_t0662, Y_t0663, Y_t0664, Y_t0665, Y_t0666, Y_t0667, Y_t0668, Y_t0669, Y_t0670, Y_t0671, Y_t0672, Y_t0673, Y_t0674, Y_t0675, Y_t0676, Y_t0677, Y_t0678, Y_t0679, Y_t0680, Y_t0681, Y_t0682, Y_t0683, Y_t0684, Y_t0685, Y_t0686, Y_t0687, Y_t0688, Y_t0689, Y_t0690, Y_t0691, Y_t0692, Y_t0693, Y_t0694, Y_t0695, Y_t0696, Y_t0697, Y_t0698, Y_t0699, Y_t0700, Y_t0701, Y_t0702, Y_t0703, Y_t0704, Y_t0705, Y_t0706, Y_t0707, Y_t0708, Y_t0709, Y_t0710, Y_t0711, Y_t0712, Y_t0713, Y_t0714, Y_t0715, Y_t0716, Y_t0717, Y_t0718, Y_t0719, Y_t0720, Y_t0721, Y_t0722, Y_t0723, Y_t0724, Y_t0725, Y_t0726, Y_t0727, Y_t0728, Y_t0729, Y_t0730, Y_t0731, Y_t0732, Y_t0733, Y_t0734, Y_t0735, Y_t0736, Y_t0737, Y_t0738, Y_t0739, Y_t0740, Y_t0741, Y_t0742, Y_t0743, Y_t0744, Y_t0745, Y_t0746, Y_t0747, Y_t0748, Y_t0749, Y_t0750, Y_t0751, Y_t0752, Y_t0753, Y_t0754, Y_t0755, Y_t0756, Y_t0757, Y_t0758, Y_t0759, Y_t0760, Y_t0761, Y_t0762, Y_t0763, Y_t0764, Y_t0765, Y_t0766, Y_t0767, Y_t0768, Y_t0769, Y_t0770, Y_t0771, Y_t0772, Y_t0773, Y_t0774, Y_t0775, Y_t0776, Y_t0777, Y_t0778, Y_t0779, Y_t0780, Y_t0781, Y_t0782, Y_t0783, Y_t0784, Y_t0785, Y_t0786, Y_t0787, Y_t0788, Y_t0789, Y_t0790, Y_t0791, Y_t0792, Y_t0793, Y_t0794, Y_t0795, Y_t0796, Y_t0797, Y_t0798, Y_t0799, Y_t0800, Y_t0801, Y_t0802, Y_t0803, Y_t0804, Y_t0805, Y_t0806, Y_t0807, Y_t0808, Y_t0809, Y_t0810, Y_t0811, Y_t0812, Y_t0813, Y_t0814, Y_t0815, Y_t0816, Y_t0817, Y_t0818, Y_t0819, Y_t0820, Y_t0821, Y_t0822, Y_t0823, Y_t0824, Y_t0825, Y_t0826, Y_t0827, Y_t0828, Y_t0829, Y_t0830, Y_t0831, Y_t0832, Y_t0833, Y_t0834, Y_t0835, Y_t0836, Y_t0837, Y_t0838, Y_t0839, Y_t0840, Y_t0841, Y_t0842, Y_t0843, Y_t0844, Y_t0845, Y_t0846, Y_t0847, Y_t0848, Y_t0849, Y_t0850, Y_t0851, Y_t0852, Y_t0853, Y_t0854, Y_t0855, Y_t0856, Y_t0857, Y_t0858, Y_t0859, Y_t0860, Y_t0861, Y_t0862, Y_t0863, Y_t0864, Y_t0865, Y_t0866, Y_t0867, Y_t0868, Y_t0869, Y_t0870, Y_t0871, Y_t0872, Y_t0873, Y_t0874, Y_t0875, Y_t0876, Y_t0877, Y_t0878, Y_t0879, Y_t0880, Y_t0881, Y_t0882, Y_t0883, Y_t0884, Y_t0885, Y_t0886, Y_t0887, Y_t0888, Y_t0889, Y_t0890, Y_t0891, Y_t0892, Y_t0893, Y_t0894, Y_t0895, Y_t0896, Y_t0897, Y_t0898, Y_t0899, Y_t0900, Y_t0901, Y_t0902, Y_t0903, Y_t0904, Y_t0905, Y_t0906, Y_t0907, Y_t0908, Y_t0909, Y_t0910, Y_t0911, Y_t0912, Y_t0913, Y_t0914, Y_t0915, Y_t0916, Y_t0917, Y_t0918, Y_t0919, Y_t0920, Y_t0921, Y_t0922, Y_t0923, Y_t0924, Y_t0925, Y_t0926, Y_t0927, Y_t0928, Y_t0929, Y_t0930, Y_t0931, Y_t0932, Y_t0933, Y_t0934, Y_t0935, Y_t0936, Y_t0937, Y_t0938, Y_t0939, Y_t0940, Y_t0941, Y_t0942, Y_t0943, Y_t0944, Y_t0945, Y_t0946, Y_t0947, Y_t0948, Y_t0949, Y_t0950, Y_t0951, Y_t0952, Y_t0953, Y_t0954, Y_t0955, Y_t0956, Y_t0957, Y_t0958, Y_t0959, Y_t0960, Y_t0961, Y_t0962, Y_t0963, Y_t0964, Y_t0965, Y_t0966, Y_t0967, Y_t0968, Y_t0969, Y_t0970, Y_t0971, Y_t0972, Y_t0973, Y_t0974, Y_t0975, Y_t0976, Y_t0977, Y_t0978, Y_t0979, Y_t0980, Y_t0981, Y_t0982, Y_t0983, Y_t0984, Y_t0985, Y_t0986, Y_t0987, Y_t0988, Y_t0989, Y_t0990, Y_t0991, Y_t0992, Y_t0993, Y_t0994, Y_t0995, Y_t0996, Y_t0997, Y_t0998, Y_t0999, Y_t1000

**Latent variables**

Ti

**Latent-variable identification:** candidates from equations need review

**Equations / distributions (LaTeX rendering)**

> Automatically typeset for readability; English display transcriptions are not changes to the submitted scientific data.

**adoption**

```math
X\sim U[-10,10]
```

```math
\mathrm{Ti}\mid \Xi\sim \mathrm{Exp}(\exp(1+.5\Xi))
```

```math
H=\mathrm{max10000} \mathrm{sample15}\%\mathrm{quantiles}
```

```math
\mathrm{condition} \mathrm{minTi}<H
```

**outcome**

```math
\mathrm{Yij}=.2 \mathrm{Yi},j-1+.5\Xi+.5\sqrt{j}+\mathrm{epsij}
```

```math
\mathrm{Yi0}=0
```

```math
\varepsilon\sim \mathcal{N}(0,.15^{2})
```

tau0

<details>
<summary>Original source equations (verbatim)</summary>

<pre>
X~U[-10,10]; Ti|Xi~Exp(exp(1+.5Xi)); H=max10000 sample15%quantiles; condition minTi&lt;H
Yij=.2 Yi,j-1+.5Xi+.5sqrt(j)+epsij; Yi0=0; eps~N(0,.15^2); tau0
</pre>

</details>


## Parameter scenarios, estimands and truth

| Scenario | Estimand | Definition | Reported value |
|---|---|---|---|
| baseline | Conditional first-adopter average treatment effect | Mean effect on first-adopter post cells in whole-experiment-success conditional population; also realized SATT=0 pathwise | 0.0 |

**Original submitted target notation:** ATT_cond


## Identifiability assumptions

- Native additive tau0, consistency; successful generation ensures nonempty pre/post.

## Provenance and review

**Submitted by:** github_file_upload

**Mode:** structured_zip

**Original versus adapted:** adapted_from_source

**Status:** needs_scientific_review

**Adaptations from the source (submitted, unverified):**

- Explicit user approval: conditional mechanism adaptation with full population/distribution disclosure.
- Condition on generation success min(T)&lt;Tmax; reject whole experiment including10000 calibration panels. Original driver shared calibration, this contribution uses fresh calibration per experiment.
- Author-code parameters beta.5/intercept1/sigma.15/delta.5 and1000-point index-time AR differ from paper; first adopter response only.
- Conditional Tmax reweighted and X/group dependence altered; not original unconditional reproduction.
- NumPy local RNG and vectorized calibration preserve mathematical laws, not R bitstream.

**Warnings:**

- Latent-variable candidates inferred from source equations; confirm their roles and completeness against the original paper or generator.
- Legacy combined DiD / Synthetic Control family: human classification required; not automatically reassigned.
