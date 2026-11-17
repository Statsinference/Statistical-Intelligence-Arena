# Math probe batch 7

### 1050 nri-highdim-sparse-additive-v1 7

```math
f_{j}=0 \text{ for } j=5,\ldots ,600.
```

### 1051 nri-highdim-sparse-additive-v1 8

```math
m(x^{\ast})=\mathbb{E}[Y\mid X=x^{\ast}]=\sum_{j=1}^{4} f_{j}(0.5), x^{\ast}=(0.5,\ldots ,0.5), \text{ with } \mathrm{truth} -1.1.
```

### 1052 nri-shangcheng-2013-spline-v1 0

```math
Z_{i}\overset{\mathrm{iid}}{\sim} \mathrm{Uniform}(0,1)
```

### 1053 nri-shangcheng-2013-spline-v1 1

```math
B_{\text{ a },b}(z)=\Gamma(\text{ a }+b)/(\Gamma(\text{ a })\cdot \Gamma(b))\cdot z^{\text{ a }-1}\cdot (1-z)^{b-1}
```

### 1054 nri-shangcheng-2013-spline-v1 2

```math
g_{0}(z)=0.6\cdot B_{30,17}(z)+0.4\cdot B_{3,11}(z)
```

### 1055 nri-shangcheng-2013-spline-v1 3

```math
\varepsilon_{i}\overset{\mathrm{iid}}{\sim} \mathcal{N}(0,0.05^{2})
```

### 1056 nri-shangcheng-2013-spline-v1 4

```math
\mathrm{Noise} \mathrm{sd}=0.05
```

### 1057 nri-shangcheng-2013-spline-v1 5

```math
\text{ variance }=0.0025.
```

### 1058 nri-shangcheng-2013-spline-v1 6

```math
Y_{i}=g_{0}(Z_{i})+\varepsilon_{i}
```

### 1059 nri-wangghosal-2023-isotonic-v1 0

```math
\mathrm{X1}_{i}\overset{\mathrm{iid}}{\sim} \mathrm{Uniform}(0,1)
```

### 1060 nri-wangghosal-2023-isotonic-v1 1

```math
\mathrm{X2}_{i}\overset{\mathrm{iid}}{\sim} \mathrm{Uniform}(0,1)
```

### 1061 nri-wangghosal-2023-isotonic-v1 2

```math
\varepsilon_{i}\overset{\mathrm{iid}}{\sim} \mathcal{N}(0,1)
```

### 1062 nri-wangghosal-2023-isotonic-v1 3

```math
\mathrm{Main} \mathrm{simulation} \mathrm{error} \mathrm{sd}=1
```

### 1063 nri-wangghosal-2023-isotonic-v1 4

```math
f_{1}=(X_{1}+X_{2})^{2}
```

### 1064 nri-wangghosal-2023-isotonic-v1 5

```math
f_{2}=\sqrt{X_{1}+X_{2}}
```

### 1065 nri-wangghosal-2023-isotonic-v1 6

```math
f_{3}=X_{1}\cdot X_{2}
```

### 1066 nri-wangghosal-2023-isotonic-v1 7

```math
f_{4}=\exp(X_{1}+X_{2})
```

### 1067 nri-wangghosal-2023-isotonic-v1 8

```math
f_{5}=\exp(X_{1}\cdot X_{2})
```

### 1068 nri-wangghosal-2023-isotonic-v1 9

```math
Y_{i}=f_{k}(\mathrm{X1}_{i},\mathrm{X2}_{i})+\varepsilon_{i}
```

### 1069 nri-wangyang-2007-hdadditive-v1 0

```math
Z_{s}\overset{\mathrm{iid}}{\sim} \mathcal{N}(0,1) \mathrm{conditional} \text{ on } -2.5\leq Z_{s}\leq 2.5, s=0..n+29-1
```

### 1070 nri-wangyang-2007-hdadditive-v1 1

```math
\mathrm{sd}=1 \mathrm{before} \mathrm{truncation}
```

### 1071 nri-wangyang-2007-hdadditive-v1 2

```math
\text{ source } d=30, \mathrm{bound}=2.5.
```

### 1072 nri-wangyang-2007-hdadditive-v1 3

```math
X_{t}=(Z_{t+29},Z_{t+28},\ldots ,Z_{t}), t=0..n-1
```

### 1073 nri-wangyang-2007-hdadditive-v1 4

```math
m(X)=\sum_{\text{ a }=1}^{30} \sin(\pi\cdot X_{a}/2.5)
```

### 1074 nri-wangyang-2007-hdadditive-v1 5

```math
L=\text{ mean }(\lvert X_{a}\rvert)
```

### 1075 nri-wangyang-2007-hdadditive-v1 6

```math
\sigma(X)=0.1\cdot (\sqrt{30}/2)\cdot (5-\exp(L))/(5+\exp(L))
```

### 1076 nri-wangyang-2007-hdadditive-v1 7

```math
\varepsilon_{t}\overset{\mathrm{iid}}{\sim} \mathcal{N}(0,1)
```

### 1077 nri-wangyang-2007-hdadditive-v1 8

```math
\mathrm{Noise} \mathrm{sd}=1 \mathrm{before} \mathrm{multiplication} \text{ by } \sigma(X).
```

### 1078 nri-wangyang-2007-hdadditive-v1 9

```math
Y_{t}=m(X_{t})+\sigma(X_{t})\cdot \varepsilon_{t}
```

### 1079 nri-wangyang-2007-hdadditive-v1 10

```math
\mathrm{Conditional} \text{ variance }=\sigma(X_{t})^{2}
```

### 1080 nri-yuparkmammen-2008-binarygam-v1 0

```math
X_{1}\sim \mathcal{N}(0,1) \mathrm{conditional} \text{ on } -1\leq X_{1}\leq 1, \mathrm{using} \mathrm{rejection} \mathrm{resampling}
```

### 1081 nri-yuparkmammen-2008-binarygam-v1 1

```math
\mathrm{Source} \mathrm{design} j=1
```

### 1082 nri-yuparkmammen-2008-binarygam-v1 2

```math
\mathrm{pre}-\mathrm{truncation} \text{ mean }=0, \mathrm{sd}=1.
```

### 1083 nri-yuparkmammen-2008-binarygam-v1 3

```math
X_{2}\sim \mathcal{N}(0,1) \mathrm{conditional} \text{ on } -1\leq X_{2}\leq 1
```

### 1084 nri-yuparkmammen-2008-binarygam-v1 4

```math
\mathrm{Source} j=1 \mathrm{correlation}=0
```

### 1085 nri-yuparkmammen-2008-binarygam-v1 5

```math
\text{ the } \mathrm{correlated} j=2 \mathrm{design} \text{ is } \text{ not } \mathrm{generated}.
```

### 1086 nri-yuparkmammen-2008-binarygam-v1 6

```math
\eta=\sin(\pi\cdot X_{1})+0.5\cdot (X_{2}+\sin(\pi\cdot X_{2}))
```

### 1087 nri-yuparkmammen-2008-binarygam-v1 7

```math
m=1/(1+\exp(-\eta)) \text{ for } \mathrm{Bernoulli}
```

### 1088 nri-yuparkmammen-2008-binarygam-v1 8

```math
m=\exp(\eta) \text{ for } \mathrm{Poisson}
```

### 1089 nri-yuparkmammen-2008-binarygam-v1 9

```math
Y\mid X\sim \mathrm{Bernoulli}(m) \text{ or } \mathrm{Poisson}(m)
```

### 1090 nri-yuparkmammen-2008-binarygam-v1 10

```math
\mathrm{Bernoulli} \mathrm{inversion} \text{ or } \mathrm{Knuth} \mathrm{product} \mathrm{sampler}
```

### 1091 nri-yuparkmammen-2008-binarygam-v1 11

```math
\mathrm{Conditional} \text{ variance }=m\cdot (1-m) \text{ or } m, \text{ respectively }
```

### 1092 nri-zhangfansun-2009-clustervc-v1 0

```math
\mathrm{Source} \mathrm{base}=6, \text{ scale }=2
```

### 1093 nri-zhangfansun-2009-clustervc-v1 1

```math
Z_{i}\sim \mathcal{N}(0,I_{2}), \mathrm{one} \mathrm{two}-\text{ vector } \mathrm{shared} \text{ by } \text{ all } \text{ rows } \text{ of } \mathrm{cluster} i
```

### 1094 nri-zhangfansun-2009-clustervc-v1 2

```math
e_{i}\sim \mathcal{N}(0,0.25\cdot I_{3}), \mathrm{shared} \mathrm{within} \mathrm{cluster} \text{ and }
```

### 1095 nri-zhangfansun-2009-clustervc-v1 3

```math
\mathrm{Each} \mathrm{random}-\mathrm{effect} \mathrm{sd}=0.5
```

### 1096 nri-zhangfansun-2009-clustervc-v1 4

```math
U_{ij}\sim \mathrm{Uniform}(0,1), \mathrm{newly} \text{ drawn } \text{ for } \text{ each } \mathrm{individual}
```

### 1097 nri-zhangfansun-2009-clustervc-v1 5

```math
X_{ij}\sim \mathcal{N}(0,I_{3}), \mathrm{newly} \text{ drawn } \text{ for } \text{ each } \mathrm{individual}
```

### 1098 nri-zhangfansun-2009-clustervc-v1 6

```math
\mathrm{Each} \mathrm{sd}=1
```

### 1099 nri-zhangfansun-2009-clustervc-v1 7

```math
\beta_{0}(u)=\sin(2\cdot \pi\cdot u)
```

### 1100 nri-zhangfansun-2009-clustervc-v1 8

```math
\beta(u)=\mathrm{ones}(2)\cdot \sin(2\cdot \pi\cdot u)
```

### 1101 nri-zhangfansun-2009-clustervc-v1 9

```math
\alpha_{0}(u)=\mathrm{ones}(3)\cdot \sin(2\cdot \pi\cdot u)
```

### 1102 nri-zhangfansun-2009-clustervc-v1 10

```math
\alpha_{1}(u)=\mathrm{ones}(3)\cdot \cos(2\cdot \pi\cdot u)
```

### 1103 nri-zhangfansun-2009-clustervc-v1 11

```math
\alpha_{2}(u)=\mathrm{ones}(3)\cdot \sin(\pi\cdot u)
```

### 1104 nri-zhangfansun-2009-clustervc-v1 12

```math
\text{ a }_{i}(u)=\alpha_{0}(u)+\alpha_{1}(u)\cdot Z_{i1}+\alpha_{2}(u)\cdot Z_{i2}+e_{i}
```

### 1105 nri-zhangfansun-2009-clustervc-v1 13

```math
\varepsilon_{ij}\sim \mathcal{N}(0,0.5^{2})
```

### 1106 nri-zhangfansun-2009-clustervc-v1 14

```math
\mathrm{Measurement}-\mathrm{error} \mathrm{sd}=0.5.
```

### 1107 nri-zhangfansun-2009-clustervc-v1 15

```math
Y_{ij}=\beta_{0}(U_{ij})+X_{ij}^{T}\cdot \text{ a }_{i}(U_{ij})+Z_{i}^{T}\cdot \beta(U_{ij})+\varepsilon_{ij}
```

### 1108 nri-zhao-wu-2008-ar1scb-v1 0

```math
\varepsilon_{t}\overset{\mathrm{iid}}{\sim} \mathcal{N}(0,1)
```

### 1109 nri-zhao-wu-2008-ar1scb-v1 1

```math
\text{ noise } \mathrm{multiplier} s=0.4.
```

### 1110 nri-zhao-wu-2008-ar1scb-v1 2

```math
Y_{t}=0.9\cdot \sin(Y_{t-1})+0.4\cdot \varepsilon_{t} \text{ for } \mathrm{burn}_{in}+n \mathrm{updates}
```

### 1111 nri-zhao-wu-2008-ar1scb-v1 3

```math
\mathrm{Return} (X_{i},Y_{i})=(Y_{\mathrm{burn}_{in}+i-1},Y_{\mathrm{burn}_{in}+i}), i=1..n
```

### 1112 nri-zhao-wu-2008-ar1scb-v1 4

```math
X_{i+1}=Y_{i} \mathrm{exactly}
```

### 1113 proximal-cui-2023-04-18-gaussian-v2 0

```math
X=(X_{1},X_{2})
```

### 1114 proximal-cui-2023-04-18-gaussian-v2 1

```math
\sigma(t)=1/(1+\exp(-t))
```

### 1115 proximal-cui-2023-04-18-gaussian-v2 2

```math
X \sim \mathcal{N}_{2}((0.25,0.25), \begin{bmatrix}
0.0625 & 0 \\
0 & 0.0625
\end{bmatrix})
```

### 1116 proximal-cui-2023-04-18-gaussian-v2 3

```math
A \mid  X \sim \mathrm{Bernoulli}(\sigma(-0.125 X_{1} - 0.125 X_{2}))
```

### 1117 proximal-cui-2023-04-18-gaussian-v2 4

```math
V=(Z,W,U)^{T} \mid  A,X \sim \mathcal{N}_{3}(\mu(A,X),\Sigma)
```

### 1118 proximal-cui-2023-04-18-gaussian-v2 5

```math
\mu(A,X) = (0.25,0.25,0.25)^{T} + A(0.25,0.125,0.25)^{T} + (0.25 X_{1} + 0.25 X_{2})(1,1,1)^{T}
```

### 1119 proximal-cui-2023-04-18-gaussian-v2 6

```math
\Sigma= \begin{bmatrix}
1 & 0.25 & 0.5 \\
0.25 & 1 & 0.5 \\
0.5 & 0.5 & 1
\end{bmatrix}
```

### 1120 proximal-cui-2023-04-18-gaussian-v2 7

```math
g(U,X) = 0.25 + 0.25(X_{1}+X_{2}) + 0.5[U - 0.25 - 0.25(X_{1}+X_{2})]
```

### 1121 proximal-cui-2023-04-18-gaussian-v2 8

```math
\varepsilon_{Y} \sim \mathcal{N}(0,0.25^{2})
```

### 1122 proximal-cui-2023-04-18-gaussian-v2 9

```math
Y = 2 + 2A + 0.25(X_{1}+X_{2}) + (4-2)g(U,X) + 2W + \varepsilon_{Y}
```

### 1123 proximal-cui-2023-04-18-gaussian-v2 10

```math
Y = 2.25 + 2A + 0.5(X_{1}+X_{2}) + U + 2W + \varepsilon_{Y}
```

### 1124 proximal-dukes-2023-03-03-mediation-v1 0

```math
T=X_{1}+X_{2}
```

### 1125 proximal-dukes-2023-03-03-mediation-v1 1

```math
\sigma(t)=1/(1+\exp(-t))
```

### 1126 proximal-dukes-2023-03-03-mediation-v1 2

```math
(X_{1},X_{2},U)^{T} \sim \mathcal{N}_{3}((0.25,0.25,0)^{T}, \begin{bmatrix}
0.25 & 0 & 0.05 \\
0 & 0.25 & 0.05 \\
0.05 & 0.05 & 1
\end{bmatrix})
```

### 1127 proximal-dukes-2023-03-03-mediation-v1 3

```math
A \mid  T,U \sim \mathrm{Bernoulli}(\sigma(-0.5T - 0.4U))
```

### 1128 proximal-dukes-2023-03-03-mediation-v1 4

```math
Z = 0.2 - 0.52A + 0.2T - U + \varepsilon_{Z}
```

### 1129 proximal-dukes-2023-03-03-mediation-v1 5

```math
W = 0.3 + 0.2T - 0.6U + \varepsilon_{W}
```

### 1130 proximal-dukes-2023-03-03-mediation-v1 6

```math
M = -0.3A - 0.5T + 0.4U + \varepsilon_{M}
```

### 1131 proximal-dukes-2023-03-03-mediation-v1 7

```math
Y = 2 + 2A + M + 2W - T - U + \varepsilon_{Y}
```

### 1132 proximal-dukes-2023-03-03-mediation-v1 8

```math
\mathcal{N}(0,1)
```

### 1133 proximal-dukes-2023-03-03-mediation-v1 9

```math
\varepsilon_{Y} \sim \mathcal{N}(0,2^{2})
```

### 1134 proximal-li-2023-07-10-binary-tnd-v1 0

```math
U \sim \mathrm{Bernoulli}(0.5)
```

### 1135 proximal-li-2023-07-10-binary-tnd-v1 1

```math
Z \mid  U \sim \mathrm{Bernoulli}(0.2 + 0.4U)
```

### 1136 proximal-li-2023-07-10-binary-tnd-v1 2

```math
A \mid  U \sim \mathrm{Bernoulli}(0.2 + 0.4U)
```

### 1137 proximal-li-2023-07-10-binary-tnd-v1 3

```math
Y \mid  A,U \sim \mathrm{Bernoulli}(\exp(\eta_{0} + \beta A - 0.693U))
```

### 1138 proximal-li-2023-07-10-binary-tnd-v1 4

```math
\eta_{0}=\ln(0.01)
```

### 1139 proximal-li-2023-07-10-binary-tnd-v1 5

```math
W \mid  U \sim \mathrm{Bernoulli}(0.02 - 0.01U)
```

### 1140 proximal-li-2023-07-10-binary-tnd-v1 6

```math
D \mid  U \sim \mathrm{Bernoulli}(0.02 - 0.015U)
```

### 1141 proximal-li-2023-07-10-binary-tnd-v1 7

```math
S \mid  Y,D,W,U \sim \mathrm{Bernoulli}(\max(Y,D,W) \times  (0.1 + 0.4U))
```

### 1142 proximal-li-2023-07-10-binary-tnd-v1 8

```math
S=1
```

### 1143 proximal-li-2023-07-10-binary-tnd-v1 9

```math
\eta_{0}=\log(0.01)
```

### 1144 proximal-li-2023-07-10-binary-tnd-v1 10

```math
\beta\in \{\log(0.2), \log(0.5), \log(0.7), 0\}
```

### 1145 proximal-li-2023-07-10-continuous-tnd-v1 0

```math
\sigma(t)=1/(1+\exp(-t))
```

### 1146 proximal-li-2023-07-10-continuous-tnd-v1 1

```math
U \sim \mathrm{Uniform}(0,1)
```

### 1147 proximal-li-2023-07-10-continuous-tnd-v1 2

```math
X \sim \mathrm{Uniform}(0,1)
```

### 1148 proximal-li-2023-07-10-continuous-tnd-v1 3

```math
A \mid  U,X \sim \mathrm{Bernoulli}(\sigma(-1 + U + 0.25X))
```

### 1149 proximal-li-2023-07-10-continuous-tnd-v1 4

```math
Z = 0.25A + 0.25X + 5U + \varepsilon_{Z}
```

### 1150 proximal-li-2023-07-10-continuous-tnd-v1 5

```math
W = 0.25X + 2U + \varepsilon_{W}
```

### 1151 proximal-li-2023-07-10-continuous-tnd-v1 6

```math
Y \mid  A,U,X \sim \mathrm{Bernoulli}(\exp(\eta_{0} + \beta A - 2U - 0.25X - 0.75UX))
```

### 1152 proximal-li-2023-07-10-continuous-tnd-v1 7

```math
\eta_{0}=\ln(0.01)
```

### 1153 proximal-li-2023-07-10-continuous-tnd-v1 8

```math
D \mid  U,X \sim \mathrm{Bernoulli}(\exp(-4.605 + 0.25X - 0.2U))
```

### 1154 proximal-li-2023-07-10-continuous-tnd-v1 9

```math
S \mid  Y,D,U,X \sim \mathrm{Bernoulli}(\max(Y,D) \times  \sigma(-1.4 + 0.5X + 2U + UX))
```

### 1155 proximal-li-2023-07-10-continuous-tnd-v1 10

```math
\mathcal{N}(0,0.25^{2})
```

### 1156 proximal-li-2023-07-10-continuous-tnd-v1 11

```math
S=1
```

### 1157 proximal-li-2023-07-10-continuous-tnd-v1 12

```math
\eta_{0}=\log(0.01)
```

### 1158 proximal-li-2023-07-10-continuous-tnd-v1 13

```math
\beta\in \{\log(0.2), \log(0.5), \log(0.7), 0\}
```

### 1159 proximal-ying-2023-03-30-longitudinal-v1 0

```math
\sigma(t)=1/(1+\exp(-t))
```

### 1160 proximal-ying-2023-03-30-longitudinal-v1 1

```math
\mathcal{N}(0,0.5^{2})
```

### 1161 proximal-ying-2023-03-30-longitudinal-v1 2

```math
X_{0} \sim \mathcal{N}(-0.35,0.5^{2})
```

### 1162 proximal-ying-2023-03-30-longitudinal-v1 3

```math
U_{0} \sim \mathcal{N}(0.35,0.5^{2})
```

### 1163 proximal-ying-2023-03-30-longitudinal-v1 4

```math
A_{0} \mid  X_{0},U_{0} \sim \mathrm{Bernoulli}(\sigma(-0.5 + 0.35X_{0} - 0.35U_{0}))
```

### 1164 proximal-ying-2023-03-30-longitudinal-v1 5

```math
Z_{0} = 0.2 + 0.5A_{0} + 0.5X_{0} + 0.75U_{0} + \varepsilon_{Z0}
```

### 1165 proximal-ying-2023-03-30-longitudinal-v1 6

```math
W_{0} = 0.2 + 0.5X_{0} - 0.95U_{0} + \varepsilon_{W0}
```

### 1166 proximal-ying-2023-03-30-longitudinal-v1 7

```math
X_{1} = 0.2 + 0.7A_{0} + 0.7X_{0} + \varepsilon_{X1}
```

### 1167 proximal-ying-2023-03-30-longitudinal-v1 8

```math
U_{1} = 0.2 + 0.7A_{0} + 0.7U_{0} + \varepsilon_{U1}
```

### 1168 proximal-ying-2023-03-30-longitudinal-v1 9

```math
A_{1} \mid  A_{0},X_{0},X_{1},U_{0},U_{1} \sim \mathrm{Bernoulli}(\sigma(-0.5 + 0.5A_{0} + 0.35(X_{0}+X_{1}) + 0.35(U_{0}+U_{1})))
```

### 1169 proximal-ying-2023-03-30-longitudinal-v1 10

```math
Z_{1} = 0.2 + 0.5(A_{0}+A_{1}) + 0.5(X_{0}+X_{1}) - 0.75(U_{0}+U_{1}) + \varepsilon_{Z1}
```

### 1170 proximal-ying-2023-03-30-longitudinal-v1 11

```math
W_{1} = 0.35 + 0.45(X_{0}+X_{1}) - 0.85(U_{0}+U_{1}) + \varepsilon_{W1}
```

### 1171 proximal-ying-2023-03-30-longitudinal-v1 12

```math
Y = -1.3 + A_{1} + 1.14A_{0} + 0.5X_{1} - 0.7U_{1} + 0.2X_{0} - 0.7U_{0} + \varepsilon_{Y}
```

### 1172 qdi-bondell-reich-wang-2010-linear-scale-v2 0

```math
X_{ij}\overset{\mathrm{iid}}{\sim}U(0,1),\quad\varepsilon_i\sim\mathcal N(0,1),\quad\varepsilon_i\perp X_i
```

### 1173 qdi-bondell-reich-wang-2010-linear-scale-v2 1

```math
Y_i=1+\sum_{j=1}^4X_{ij}+\left(1+0.1\sum_{j=1}^4X_{ij}\right)\varepsilon_i
```

### 1174 qdi-bondell-reich-wang-2010-linear-scale-v2 2

```math
Q_\tau(x)=1+\sum_{j=1}^4x_j+\left(1+0.1\sum_{j=1}^4x_j\right)\Phi^{-1}(\tau)
```

### 1175 qdi-bondell-reich-wang-2010-sine-location-v2 0

```math
X_i\sim U(0,1),\quad\varepsilon_i\sim\mathcal N(0,1),\quad X_i\perp\varepsilon_i
```

### 1176 qdi-bondell-reich-wang-2010-sine-location-v2 1

```math
Y_i=0.5+2X_i+\sin(2\pi X_i-0.5)+\varepsilon_i
```

### 1177 qdi-bondell-reich-wang-2010-sine-location-v2 2

```math
Q_\tau(x)=m(x)+s(x)\Phi^{-1}(\tau)
```

### 1178 qdi-bondell-reich-wang-2010-sine-scale-v2 0

```math
X_i\sim U(0,1),\quad\varepsilon_i\sim\mathcal N(0,1),\quad X_i\perp\varepsilon_i
```

### 1179 qdi-bondell-reich-wang-2010-sine-scale-v2 1

```math
Y_i=3X_i+\{0.5+2X_i+\sin(2\pi X_i-0.5)\}\varepsilon_i
```

### 1180 qdi-bondell-reich-wang-2010-sine-scale-v2 2

```math
Q_\tau(x)=m(x)+s(x)\Phi^{-1}(\tau)
```

### 1181 qdi-dette-volgushev-2008-exponential-scale-v2 0

```math
X_i\sim U(0,5),\quad E_i\sim\mathrm{Exp}(\mathrm{rate}=1),\quad X_i\perp E_i
```

### 1182 qdi-dette-volgushev-2008-exponential-scale-v2 1

```math
Y_i=2+X_i+e^{-X_i}\{E_i-\log(2.6)\}
```

### 1183 qdi-dette-volgushev-2008-exponential-scale-v2 2

```math
Q_\tau(x)=2+x+e^{-x}\{-\log(1-\tau)-\log(2.6)\}
```

### 1184 qdi-hall-yao-2005-additive-sine-v2 0

```math
X_{ij},\varepsilon_i\overset{\mathrm{ind}}{\sim}\mathcal N(0,1),\quad j=1,\ldots,4
```

### 1185 qdi-hall-yao-2005-additive-sine-v2 1

```math
Y_i=\frac12\sum_{j=1}^4\sin(X_{ij})+\varepsilon_i
```

### 1186 qdi-hall-yao-2005-additive-sine-v2 2

```math
F_{Y\mid X}(y\mid x)=\Phi\!\left(y-\frac12\sum_{j=1}^4\sin x_j\right)
```

### 1187 qdi-hall-yao-2005-gaussian-index-v2 0

```math
X_{ij},\varepsilon_i\overset{\mathrm{ind}}{\sim}\mathcal N(0,1),\quad j=1,\ldots,4
```

### 1188 qdi-hall-yao-2005-gaussian-index-v2 1

```math
Y_i=\frac{X_{i1}+2X_{i2}+3X_{i4}}{\sqrt{14}}+\varepsilon_i
```

### 1189 qdi-hall-yao-2005-gaussian-index-v2 2

```math
Q_Y(0.9)=\sqrt 2\,\Phi^{-1}(0.9)
```

### 1190 qdi-li-liu-zhu-2007-exponential-surface-v2 0

```math
X_{i1},X_{i2}\overset{\mathrm{iid}}{\sim}U(0,1),\quad\varepsilon_i\perp X_i
```

### 1191 qdi-li-liu-zhu-2007-exponential-surface-v2 1

```math
m(x)=\frac{40e^{8\{(x_1-0.5)^2+(x_2-0.5)^2\}}}{e^{8\{(x_1-0.2)^2+(x_2-0.7)^2\}}+e^{8\{(x_1-0.7)^2+(x_2-0.2)^2\}}}
```

### 1192 qdi-li-liu-zhu-2007-exponential-surface-v2 2

```math
Y_i=m(X_i)+\varepsilon_i,\quad\varepsilon_i\sim\mathcal N(0,1)\;\text{or}\;t_3\;\text{or}\;0.1\mathcal N(0,25)+0.9\mathcal N(0,1)
```

### 1193 qdi-li-liu-zhu-2007-exponential-surface-v2 3

```math
Q_\tau(x)=m(x)+F_\varepsilon^{-1}(\tau)
```

### 1194 qdi-li-liu-zhu-2007-sinc-v2 0

```math
X_i\sim U(-2,2),\quad\varepsilon_i\sim\mathcal N(0,0.2^2),\quad X_i\perp\varepsilon_i
```

### 1195 qdi-li-liu-zhu-2007-sinc-v2 1

```math
Y_i=\frac{\sin(\pi X_i)}{\pi X_i}+\varepsilon_i,\quad \mathrm{sinc}(0)=1
```

### 1196 qdi-li-liu-zhu-2007-sinc-v2 2

```math
Q_\tau(x)=\mathrm{sinc}(x)+0.2\Phi^{-1}(\tau)
```

### 1197 qdi-bondell-reich-wang-2010-linear-scale-v1 0

```math
X_{ij}\overset{\mathrm{iid}}{\sim}U(0,1),\quad\varepsilon_i\sim\mathcal N(0,1),\quad\varepsilon_i\perp X_i
```

### 1198 qdi-bondell-reich-wang-2010-linear-scale-v1 1

```math
Y_i=1+\sum_{j=1}^4X_{ij}+\left(1+0.1\sum_{j=1}^4X_{ij}\right)\varepsilon_i
```

### 1199 qdi-bondell-reich-wang-2010-linear-scale-v1 2

```math
Q_\tau(x)=1+\sum_{j=1}^4x_j+\left(1+0.1\sum_{j=1}^4x_j\right)\Phi^{-1}(\tau)
```

### 1200 qdi-bondell-reich-wang-2010-sine-location-v1 0

```math
X_i\sim U(0,1),\quad\varepsilon_i\sim\mathcal N(0,1),\quad X_i\perp\varepsilon_i
```

### 1201 qdi-bondell-reich-wang-2010-sine-location-v1 1

```math
Y_i=0.5+2X_i+\sin(2\pi X_i-0.5)+\varepsilon_i
```

### 1202 qdi-bondell-reich-wang-2010-sine-location-v1 2

```math
Q_\tau(x)=m(x)+s(x)\Phi^{-1}(\tau)
```

### 1203 qdi-bondell-reich-wang-2010-sine-scale-v1 0

```math
X_i\sim U(0,1),\quad\varepsilon_i\sim\mathcal N(0,1),\quad X_i\perp\varepsilon_i
```

### 1204 qdi-bondell-reich-wang-2010-sine-scale-v1 1

```math
Y_i=3X_i+\{0.5+2X_i+\sin(2\pi X_i-0.5)\}\varepsilon_i
```

### 1205 qdi-bondell-reich-wang-2010-sine-scale-v1 2

```math
Q_\tau(x)=m(x)+s(x)\Phi^{-1}(\tau)
```

### 1206 qdi-dette-volgushev-2008-exponential-scale-v1 0

```math
X_i\sim U(0,5),\quad E_i\sim\mathrm{Exp}(\mathrm{rate}=1),\quad X_i\perp E_i
```

### 1207 qdi-dette-volgushev-2008-exponential-scale-v1 1

```math
Y_i=2+X_i+e^{-X_i}\{E_i-\log(2.6)\}
```

### 1208 qdi-dette-volgushev-2008-exponential-scale-v1 2

```math
Q_\tau(x)=2+x+e^{-x}\{-\log(1-\tau)-\log(2.6)\}
```

### 1209 qdi-fong-yiu-2026-cubic-quantile-v1 0

```math
Y_{1},\ldots ,Y_{n} \text{ iid } \sim P^{\ast}, Q^{\ast}(u)=4(u-0.4)^{3}+0.2u, 0<u<1
```

### 1210 qdi-fong-yiu-2026-cubic-quantile-v1 1

```math
U_{i}\overset{\mathrm{iid}}{\sim} \mathrm{Uniform}(0,1)
```

### 1211 qdi-fong-yiu-2026-cubic-quantile-v1 2

```math
Y_{i}=4(U_{i}-0.4)^{3}+0.2U_{i}. \mathrm{No} \text{ added } \text{ noise }
```

### 1212 qdi-fong-yiu-2026-cubic-quantile-v1 3

```math
Q'(u)=12(u-0.4)^{2}+0.2\geq 0.2
```

### 1213 qdi-fong-yiu-2026-cubic-quantile-v1 4

```math
Q(0)=-0.256
```

### 1214 qdi-fong-yiu-2026-cubic-quantile-v1 5

```math
Q(1)=1.064 (\text{ continuous } \text{ endpoint } \text{ extensions }).
```

### 1215 qdi-fong-yiu-2026-cubic-quantile-v1 6

```math
\theta=\inf\{y:F_{Y}(y)\geq 0.9\}=Q^{\ast}(0.9)=17/25=0.68.
```

### 1216 qdi-fong-yiu-2026-cubic-quantile-v1 7

```math
Q^{\ast}(u)=4u^{3}-4.8u^{2}+2.12u-0.256
```

### 1217 qdi-hall-wolff-yao-1999-sine-triangular-v1 0

```math
X_{i} \text{ iid } \sim f_{T}
```

### 1218 qdi-hall-wolff-yao-1999-sine-triangular-v1 1

```math
\varepsilon_{i} \text{ iid } \sim f_{T}
```

### 1219 qdi-hall-wolff-yao-1999-sine-triangular-v1 2

```math
f_{T}(u)=(1-|u|)1\{-1\leq u\leq 1\}.
```

### 1220 qdi-hall-wolff-yao-1999-sine-triangular-v1 3

```math
Y_{i} = 2\cdot \sin(3.1416\cdot X_{i}) + \varepsilon_{i}.
```

### 1221 qdi-hall-wolff-yao-1999-sine-triangular-v1 4

```math
\mathrm{For} \text{ independent } U_{i1},\ldots ,U_{i4} \sim \mathrm{Uniform}(0,1): X_{i}=U_{i1}-U_{i2}
```

### 1222 qdi-hall-wolff-yao-1999-sine-triangular-v1 5

```math
\varepsilon_{i}=U_{i3}-U_{i4}
```

### 1223 qdi-hall-wolff-yao-1999-sine-triangular-v1 6

```math
F(y\mid x)=G(z)
```

### 1224 qdi-hall-wolff-yao-1999-sine-triangular-v1 7

```math
z=y-2\cdot \sin(3.1416\cdot x)
```
