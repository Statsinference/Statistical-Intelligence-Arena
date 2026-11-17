# Math probe batch 6

### 875 mediation-miles-2019-toxicity-path-specific-v1 2

```math
C_{1} = (0.8, 0.6, -0.3)^{T} + (1, 0.1, 0.2)^{T} C_{0} + (0.5, -0.4, 0.5)^{T} A + (-0.1, 0.8, -0.2)^{T} C_{0} A + \mathcal{N}(0, I_{3})
```

### 876 mediation-miles-2019-toxicity-path-specific-v1 3

```math
M = -0.5 - 0.2 C_{0} + 0.3 A + [-0.2, 0.1, 0.5] C_{1} + [0.4, 0, 0] A C_{1} + \mathcal{N}(0, 1)
```

### 877 mediation-miles-2019-toxicity-path-specific-v1 4

```math
Y = 0.2 + 0.2 C_{0} + 0.6 A + [1, 0.7, 0.3] C_{1} - 0.9 M - 0.8 A M + \mathcal{N}(0, 1)
```

### 878 mediation-miles-2019-toxicity-path-specific-v1 5

```math
\beta_{0} = \mathrm{int} \mathrm{int} \mathrm{int} \mathbb{E}(Y|m, c_{1}, \text{ a }', c_{0}) \mathrm{dF}(m|c_{1}, \text{ a }, c_{0}) \mathrm{dF}(c_{1}|\text{ a }', c_{0}) \mathrm{dF}(c_{0})
```

### 879 mediation-shan-li-ai-2026-missing-confounders-aux-shadow-v1 0

```math
X_{1} = \Phi(\varepsilon_{1})
```

### 880 mediation-shan-li-ai-2026-missing-confounders-aux-shadow-v1 1

```math
X_{2} = \Phi(\varepsilon_{2}) (\mathrm{both} \mathrm{Uniform}(0,1))
```

### 881 mediation-shan-li-ai-2026-missing-confounders-aux-shadow-v1 2

```math
X_{3} \sim \mathrm{Bernoulli}(0.5)
```

### 882 mediation-shan-li-ai-2026-missing-confounders-aux-shadow-v1 3

```math
T \sim \mathrm{Bernoulli}(\mathrm{expit}(0.1 + X_{1}^{2} - X_{2} + 0.2 X_{3}))
```

### 883 mediation-shan-li-ai-2026-missing-confounders-aux-shadow-v1 4

```math
M = -1 + T - T X_{1}^{2} + 4 X_{1}^{2} - \sin(X_{2}) + X_{3} + \varepsilon_{3}
```

### 884 mediation-shan-li-ai-2026-missing-confounders-aux-shadow-v1 5

```math
Y = -1 + T + 3 T M - 1.5 M + T X_{1} + 5 \sin(X_{1}) - 2 X_{2}^{2} + X_{3} + \varepsilon_{4}
```

### 885 mediation-shan-li-ai-2026-missing-confounders-aux-shadow-v1 6

```math
(R_{1},R_{2}) \sim \mathrm{Multinomial}(p_{11}, p_{10}, p_{01}, p_{00})
```

### 886 mediation-shan-li-ai-2026-missing-confounders-aux-shadow-v1 7

```math
p_{11} = 1/(1 + 3 \exp(-U))
```

### 887 mediation-shan-li-ai-2026-missing-confounders-aux-shadow-v1 8

```math
p_{10} = p_{01} = p_{00} = 1/(\exp(U) + 3)
```

### 888 mediation-shan-li-ai-2026-missing-confounders-aux-shadow-v1 9

```math
\theta= \mathbb{E}[Y(1, M(0))] = 3.192275262794844
```

### 889 mediation-shan-li-ai-2026-missing-confounders-internal-shadow-v1 0

```math
X_{1} = \Phi(\varepsilon_{1})
```

### 890 mediation-shan-li-ai-2026-missing-confounders-internal-shadow-v1 1

```math
X_{2} = \Phi(\varepsilon_{2}) (\mathrm{both} \mathrm{Uniform}(0,1))
```

### 891 mediation-shan-li-ai-2026-missing-confounders-internal-shadow-v1 2

```math
X_{3} \sim \mathrm{Bernoulli}(0.5)
```

### 892 mediation-shan-li-ai-2026-missing-confounders-internal-shadow-v1 3

```math
T \sim \mathrm{Bernoulli}(\mathrm{expit}(0.1 + X_{1}^{2} - X_{2} + 0.2 X_{3}))
```

### 893 mediation-shan-li-ai-2026-missing-confounders-internal-shadow-v1 4

```math
M = -1 + T - T X_{1}^{2} + 4 X_{1}^{2} - \sin(X_{2}) + X_{3} + \varepsilon_{3}
```

### 894 mediation-shan-li-ai-2026-missing-confounders-internal-shadow-v1 5

```math
Y = -1 + T + 3 T M - 1.5 M + T X_{1} + 5 \sin(X_{1}) - 2 X_{2}^{2} + X_{3} + \varepsilon_{4}
```

### 895 mediation-shan-li-ai-2026-missing-confounders-internal-shadow-v1 6

```math
(R_{1},R_{2}) \sim \mathrm{Multinomial}(p_{11}, p_{10}, p_{01}, p_{00})
```

### 896 mediation-shan-li-ai-2026-missing-confounders-internal-shadow-v1 7

```math
p_{11} = 1/(1 + 3 \exp(-U))
```

### 897 mediation-shan-li-ai-2026-missing-confounders-internal-shadow-v1 8

```math
p_{10} = p_{01} = p_{00} = 1/(\exp(U) + 3)
```

### 898 mediation-shan-li-ai-2026-missing-confounders-internal-shadow-v1 9

```math
\theta= \mathbb{E}[Y(1, M(0))] = 3.192275262794844
```

### 899 mediation-standard-nie1-cheng-v1 0

```math
\psi=\mathbb{E}[Y(1,M(1))-Y(1,M(0))]
```

### 900 mediation-standard-nie1-diaz-hejazi-v1 0

```math
\psi=\mathbb{E}[Y(1,M(1))-Y(1,M(0))]
```

### 901 mediation-standard-nie1-diaz-intermediate-v1 0

```math
\psi=\mathbb{E}[Y(1,M(1))-Y(1,M(0))]
```

### 902 mediation-standard-nie1-eric-v1 0

```math
\psi=\mathbb{E}[Y(1,M(1))-Y(1,M(0))]
```

### 903 mediation-standard-nie1-he-song-xu-v1 0

```math
\psi=\mathbb{E}[Y(1,M(1))-Y(1,M(0))]
```

### 904 mediation-standard-nie1-jones-correlated-v1 0

```math
\psi=\mathbb{E}[Y(1,M(1))-Y(1,M(0))]
```

### 905 mediation-standard-nie1-jones-lnl-v1 0

```math
\psi=\mathbb{E}[Y(1,M(1))-Y(1,M(0))]
```

### 906 mediation-standard-nie1-jones-lnn-v1 0

```math
\psi=\mathbb{E}[Y(1,M(1))-Y(1,M(0))]
```

### 907 mediation-standard-nie1-jones-nnn-v1 0

```math
\psi=\mathbb{E}[Y(1,M(1))-Y(1,M(0))]
```

### 908 mediation-standard-nie1-miles-v1 0

```math
\psi=\mathbb{E}[Y(1,M(1))-Y(1,M(0))]
```

### 909 mediation-standard-nie1-shan-v1 0

```math
\psi=\mathbb{E}[Y(1,M(1))-Y(1,M(0))]
```

### 910 mediation-standard-nie1-xia-binary-v1 0

```math
\psi=\mathbb{E}[Y(1,M(1))-Y(1,M(0))]
```

### 911 mediation-standard-nie1-xia-continuous-v1 0

```math
\psi=\mathbb{E}[Y(1,M(1))-Y(1,M(0))]
```

### 912 mediation-standard-nie1-zuo-v1 0

```math
\psi=\mathbb{E}[Y(1,M(1))-Y(1,M(0))]
```

### 913 mediation-xia-chan-2023-binary-plackett-v1 0

```math
X\sim \mathcal{N}(0,1)
```

### 914 mediation-xia-chan-2023-binary-plackett-v1 1

```math
A\mid X\sim \mathrm{Bern}(\mathrm{expit}(-0.2+0.3X))
```

### 915 mediation-xia-chan-2023-binary-plackett-v1 2

```math
M\mid A,X\sim \mathrm{Bern}(\mathrm{expit}(-0.3-0.2A+0.5X))
```

### 916 mediation-xia-chan-2023-binary-plackett-v1 3

```math
C\mid A,X\sim \mathrm{Bern}(\mathrm{expit}(-0.2-0.1A+0.3X))
```

### 917 mediation-xia-chan-2023-binary-plackett-v1 4

```math
OR(M,C\mid A,X)=\exp(1-2A+3X)
```

### 918 mediation-xia-chan-2023-binary-plackett-v1 5

```math
\mathrm{joint} p_{11} \mathrm{solves} p_{11}(1-\mathrm{pM}-\mathrm{pC}+p_{11})/[(\mathrm{pM}-p_{11})(\mathrm{pC}-p_{11})]=OR
```

### 919 mediation-xia-chan-2023-binary-plackett-v1 6

```math
Y=1+3A+6M+3C+6X+4AC+2AM+\varepsilon_{Y}
```

### 920 mediation-xia-chan-2023-binary-plackett-v1 7

```math
\varepsilon_{Y}\sim \mathcal{N}(0,16)
```

### 921 mediation-xia-chan-2023-binary-plackett-v1 8

```math
\mathrm{NDE}=E_{X}[3+3\{\mathrm{pC}(1,X)-\mathrm{pC}(0,X)\}+4\mathrm{pC}(1,X)+2\mathrm{pM}(0,X)]
```

### 922 mediation-xia-chan-2023-continuous-copula-v1 0

```math
X\sim \mathcal{N}(0,1)
```

### 923 mediation-xia-chan-2023-continuous-copula-v1 1

```math
A\mid X\sim \mathrm{Bern}(\mathrm{expit}(-0.4+0.6X))
```

### 924 mediation-xia-chan-2023-continuous-copula-v1 2

```math
(E_{M},E_{C})\sim \mathcal{N}_{2}(0,\begin{bmatrix}
1 & 0.2 \\
0.2 & 1
\end{bmatrix})
```

### 925 mediation-xia-chan-2023-continuous-copula-v1 3

```math
M=3+2A+4X+5E_{M}
```

### 926 mediation-xia-chan-2023-continuous-copula-v1 4

```math
C=1+2A+2X+4E_{C}
```

### 927 mediation-xia-chan-2023-continuous-copula-v1 5

```math
Y=1+2A+2M+3C+5X+4AC+2AM+\varepsilon_{Y}
```

### 928 mediation-xia-chan-2023-continuous-copula-v1 6

```math
\varepsilon_{Y}\sim \mathcal{N}(0,16)
```

### 929 mediation-xia-chan-2023-continuous-copula-v1 7

```math
\mathrm{NDE}=2+3(2)+4\mathbb{E}[C(1)]+2\mathbb{E}[M(0)]=26
```

### 930 mediation-zhou-2022-ordered-two-mediators-v1 0

```math
(U_{1},U_{2},U_{3},UXY) \sim \mathcal{N}(0, I_{4})
```

### 931 mediation-zhou-2022-ordered-two-mediators-v1 1

```math
\mathrm{Xj} \sim \mathcal{N}((U_{1},U_{2},U_{3},UXY) \beta_{\mathrm{Xj}}, 1), j = 1,2,3,4
```

### 932 mediation-zhou-2022-ordered-two-mediators-v1 2

```math
A \sim \mathrm{Bernoulli}(\mathrm{logit}^{-1}[(1,X_{1},X_{2},X_{3},X_{4}) \beta_{A}])
```

### 933 mediation-zhou-2022-ordered-two-mediators-v1 3

```math
M_{1} \sim \mathcal{N}((1,X_{1},X_{2},X_{3},X_{4},A) \beta_{\mathrm{M1}}, 1)
```

### 934 mediation-zhou-2022-ordered-two-mediators-v1 4

```math
M_{2} \sim \mathcal{N}((1,X_{1},X_{2},X_{3},X_{4},A,M_{1}) \beta_{\mathrm{M2}}, 1)
```

### 935 mediation-zhou-2022-ordered-two-mediators-v1 5

```math
Y \sim \mathcal{N}((1,UXY,X_{1},X_{2},X_{3},X_{4},A,M_{1},M_{2}) \beta_{Y}, 1)
```

### 936 mediation-zhou-2022-ordered-two-mediators-v1 6

```math
\beta_{\mathrm{X1}}=(0.77,-0.86,0.35,0.88)
```

### 937 mediation-zhou-2022-ordered-two-mediators-v1 7

```math
\beta_{\mathrm{X2}}=(-0.99,-0.72,-0.1,0.54)
```

### 938 mediation-zhou-2022-ordered-two-mediators-v1 8

```math
\beta_{\mathrm{X3}}=(-0.74,0.1,0.91,0.46)
```

### 939 mediation-zhou-2022-ordered-two-mediators-v1 9

```math
\beta_{\mathrm{X4}}=(-0.21,-0.43,-0.21,-0.7)
```

### 940 mediation-zhou-2022-ordered-two-mediators-v1 10

```math
\beta_{A}=(-0.36,-0.08,-0.06,0.4,-0.14)
```

### 941 mediation-zhou-2022-ordered-two-mediators-v1 11

```math
\beta_{\mathrm{M1}}=(0,0.3,0.42,0.48,0.28,0.41)
```

### 942 mediation-zhou-2022-ordered-two-mediators-v1 12

```math
\beta_{\mathrm{M2}}=(0.04,0.2,0.09,0.12,0.39,0.34,0.24)
```

### 943 mediation-zhou-2022-ordered-two-mediators-v1 13

```math
\beta_{Y}=(-0.27,-0.1,0.25,0.2,-0.08,0.78,0.76,-0.4,0.96)
```

### 944 mediation-zuo-et-al-2025-continuous-mnar-v1 0

```math
X\sim \mathcal{N}(0,1)
```

### 945 mediation-zuo-et-al-2025-continuous-mnar-v1 1

```math
T\sim \mathrm{Bern}(0.5), \text{ independent }
```

### 946 mediation-zuo-et-al-2025-continuous-mnar-v1 2

```math
M\mid T,X\sim \mathcal{N}(T+X,1)
```

### 947 mediation-zuo-et-al-2025-continuous-mnar-v1 3

```math
Y\mid M,T,X\sim \mathcal{N}(M+T+MT+X,1)
```

### 948 mediation-zuo-et-al-2025-continuous-mnar-v1 4

```math
R_{M}\mid M,T,X\sim \mathrm{Bern}(\mathrm{expit}(1.4+M+T+X))
```

### 949 mediation-zuo-et-al-2025-continuous-mnar-v1 5

```math
R_{Y}\mid Y,T,X\sim \mathrm{Bern}(\mathrm{expit}(1.8+Y+T+X))
```

### 950 mediation-zuo-et-al-2025-continuous-mnar-v1 6

```math
M_{\mathrm{obs0}}=R_{M}\cdot M
```

### 951 mediation-zuo-et-al-2025-continuous-mnar-v1 7

```math
Y_{\mathrm{obs0}}=R_{Y}\cdot Y
```

### 952 nri-calonico-2018-asymmetric-sine-v1 0

```math
X \sim \mathrm{Uniform}[-1,1]
```

### 953 nri-calonico-2018-asymmetric-sine-v1 1

```math
\varepsilon\sim \mathcal{N}(0,1), X
```

### 954 nri-calonico-2018-asymmetric-sine-v1 2

```math
Y=m(X)+\varepsilon
```

### 955 nri-calonico-2018-asymmetric-sine-v1 3

```math
m(x)=\sin(3\cdot \pi\cdot x/2)/(1+18\cdot x^{2}\cdot (\mathrm{sgn}(x)+1))
```

### 956 nri-calonico-2018-asymmetric-sine-v1 4

```math
\mathrm{sgn}(0)=0.
```

### 957 nri-calonico-2018-asymmetric-sine-v1 5

```math
\mathrm{Equivalently}, m(x)=\sin(3\cdot \pi\cdot x/2) \text{ for } x\leq 0
```

### 958 nri-calonico-2018-asymmetric-sine-v1 6

```math
m(x)=\sin(3\cdot \pi\cdot x/2)/(1+36\cdot x^{2}) \text{ for } x>0.
```

### 959 nri-calonico-2018-asymmetric-sine-v1 7

```math
\theta(x_{0})=\mathbb{E}[Y\mid X=x_{0}]=m(x_{0})
```

### 960 nri-damped-sine-v1 0

```math
Y = m(X) + \varepsilon,  X \sim U[-1,1]
```

### 961 nri-damped-sine-v1 1

```math
\varepsilon\sim \mathcal{N}(0,1)
```

### 962 nri-damped-sine-v1 2

```math
m(x) = \sin(3\cdot \pi\cdot x/2) / (1 + 18\cdot x^{2}\cdot (\mathrm{sgn}(x)+1))
```

### 963 nri-damped-sine-v1 3

```math
m(x) = \sin(\pi\cdot x/2) / (1 + 2\cdot x^{2}\cdot (\mathrm{sgn}(x)+1))
```

### 964 nri-damped-sine-v1 4

```math
m(x_{0}) = \mathbb{E}[Y \mid  X = x_{0}]  \text{ at }  x_{0} \in \{-2/3,-1/3,0,1/3,2/3\}
```

### 965 nri-damped-sine-v1 5

```math
m_{5}(-2/3)=0, m_{5}(-1/3)=-1, m_{5}(0)=0, m_{5}(1/3)=0.2, m_{5}(2/3)=0
```

### 966 nri-linear-gaussian-bump-v1 0

```math
Y = m(X) + \varepsilon,  X \sim U[-1,1]
```

### 967 nri-linear-gaussian-bump-v1 1

```math
\varepsilon\sim \mathcal{N}(0,1)
```

### 968 nri-linear-gaussian-bump-v1 2

```math
m(x) = 2x + 2\cdot \exp(-64\cdot x^{2})
```

### 969 nri-linear-gaussian-bump-v1 3

```math
m(x) = x + 5\cdot \phi(10x),  \phi(z) = \exp(-z^{2}/2)/\sqrt{2\cdot \pi}
```

### 970 nri-linear-gaussian-bump-v1 4

```math
m(x_{0}) = \mathbb{E}[Y \mid  X = x_{0}]  \text{ at }  x_{0} = 0
```

### 971 nri-linear-gaussian-bump-v1 5

```math
m(0) = 2\cdot 0 + 2\cdot \exp(0) = 2
```

### 972 nri-linear-gaussian-bump-v1 6

```math
m(0) = 0 + 5\cdot \phi(0) = 5/\sqrt{2\cdot \pi} \approx 1.994711
```

### 973 nri-sine-gaussian-bump-v1 0

```math
Y = m(X) + \varepsilon,  X \sim U[-1,1]
```

### 974 nri-sine-gaussian-bump-v1 1

```math
\varepsilon\sim \mathcal{N}(0,1)
```

### 975 nri-sine-gaussian-bump-v1 2

```math
m(x) = \sin(4x) + 2\cdot \exp(-64\cdot x^{2})
```

### 976 nri-sine-gaussian-bump-v1 3

```math
m(x_{0}) = \mathbb{E}[Y \mid  X = x_{0}]  \text{ at }  x_{0} \in \{-2/3,-1/3,0,1/3,2/3\}
```

### 977 nri-sine-gaussian-bump-v1 4

```math
m(0) = \sin(0) + 2\cdot \exp(0) = 0 + 2 = 2  (\mathrm{exact})
```

### 978 nri-two-gaussian-peaks-v1 0

```math
Y = m(X) + \varepsilon,  X \sim U[-1,1]
```

### 979 nri-two-gaussian-peaks-v1 1

```math
\varepsilon\sim \mathcal{N}(0,1)  \mathrm{homoscedastic}
```

### 980 nri-two-gaussian-peaks-v1 2

```math
m(x) = 0.3\cdot \exp(-4\cdot (2x+1)^{2}) + 0.7\cdot \exp(-16\cdot (2x-1)^{2})
```

### 981 nri-two-gaussian-peaks-v1 3

```math
\mathrm{left} \mathrm{peak} \text{ at } x=-1/2 (\mathrm{amplitude} 0.3)
```

### 982 nri-two-gaussian-peaks-v1 4

```math
\mathrm{right} \mathrm{peak} \text{ at } x=1/2 (\mathrm{amplitude} 0.7)
```

### 983 nri-two-gaussian-peaks-v1 5

```math
m(x_{0}) = \mathbb{E}[Y \mid  X = x_{0}]  \text{ at }  x_{0} \in \{-2/3,-1/3,0,1/3,2/3\}
```

### 984 nri-two-gaussian-peaks-v1 6

```math
m_{3}(-2/3)=0.3\cdot e^{-4/9}+0.7\cdot e^{-784/9}
```

### 985 nri-two-gaussian-peaks-v1 7

```math
m_{3}(-1/3)=0.3\cdot e^{-4/9}+0.7\cdot e^{-400/9}
```

### 986 nri-two-gaussian-peaks-v1 8

```math
m_{3}(0)=0.3\cdot e^{-4}+0.7\cdot e^{-16}
```

### 987 nri-two-gaussian-peaks-v1 9

```math
m_{3}(1/3)=0.3\cdot e^{-100/9}+0.7\cdot e^{-16/9}
```

### 988 nri-two-gaussian-peaks-v1 10

```math
m_{3}(2/3)=0.3\cdot e^{-196/9}+0.7\cdot e^{-16/9}
```

### 989 nri-binary-kink-v1 0

```math
\text{ a }_{s} = 0.2 + 0.8s, s \in \{0,0.1,\ldots ,1\}
```

### 990 nri-binary-kink-v1 1

```math
p_{s}(x) = 0.2 x / \text{ a }_{s} \text{ for } 0\leq x\leq \text{ a }_{s}
```

### 991 nri-binary-kink-v1 2

```math
p_{s}(x) = 0.2 + 0.8 (x-\text{ a }_{s})/(1-\text{ a }_{s}) \text{ for } \text{ a }_{s}<x\leq 1
```

### 992 nri-binary-kink-v1 3

```math
\text{ a }_{1}=1
```

### 993 nri-binary-kink-v1 4

```math
p_{1}(x)=0.2x \text{ for } 0\leq x<1 \text{ and } p_{1}(1)=1 \text{ by } \mathrm{library} \mathrm{convention}
```

### 994 nri-binary-kink-v1 5

```math
X_{i}\sim \mathrm{Uniform}[0,1] \text{ independently }
```

### 995 nri-binary-kink-v1 6

```math
Y_{i}\mid X_{i}=x\sim \mathrm{Bernoulli}(p_{s}(x)) \text{ independently }
```

### 996 nri-binary-kink-v1 7

```math
m_{s}(0.5)=\mathbb{E}[Y\mid X=0.5]=p_{s}(0.5)
```

### 997 nri-binary-monomial-v1 0

```math
X_{i} \sim \mathrm{Uniform}[0,1] \text{ independently }
```

### 998 nri-binary-monomial-v1 1

```math
p_{s}(x) = x^{1-s}, s \in \{0,0.1,\ldots ,1\}\setminus \{1\}
```

### 999 nri-binary-monomial-v1 2

```math
Y_{i} \mid  X_{i}=x \sim \mathrm{Bernoulli}(p_{s}(x)) \text{ independently }
```

### 1000 nri-binary-monomial-v1 3

```math
m_{s}(0.5) = \mathbb{E}[Y \mid  X=0.5] = p_{s}(0.5) = 0.5^{1-s}
```

### 1001 nri-binary-s-shape-v1 0

```math
X_{i} \sim \mathrm{Uniform}[0,1] \text{ independently }
```

### 1002 nri-binary-s-shape-v1 1

```math
p_{s}(x) = [1 + ((1-x)/x)^{1+s}]^{-1}, s \in \{0,0.1,\ldots ,1\}, 0<x<1
```

### 1003 nri-binary-s-shape-v1 2

```math
p_{s}(0)=0 \text{ and } p_{s}(1)=1 \text{ by } \mathrm{limits}
```

### 1004 nri-binary-s-shape-v1 3

```math
p_{s}(x) = x^{1+s} / (x^{1+s} + (1-x)^{1+s}), \text{ with } \text{ endpoint } \mathrm{values} 0 \text{ and } 1
```

### 1005 nri-binary-s-shape-v1 4

```math
Y_{i} \mid  X_{i}=x \sim \mathrm{Bernoulli}(p_{s}(x)) \text{ independently }
```

### 1006 nri-binary-s-shape-v1 5

```math
m_{s}(0.5) = \mathbb{E}[Y \mid  X=0.5] = p_{s}(0.5) = 0.5 \text{ for } \mathrm{every} \mathrm{declared} s
```

### 1007 nri-binary-step-v1 0

```math
X_{i} \sim \mathrm{Uniform}[0,1] \text{ independently }
```

### 1008 nri-binary-step-v1 1

```math
p_{s}(x) = (\lfloor k\cdot x\rfloor + 1\{x \neq 1\}) / k, k = 15 - 10\cdot s, s \in \{0.1, 0.2, \ldots , 1.0\}, k \in \{14, 13, \ldots , 5\}
```

### 1009 nri-binary-step-v1 2

```math
p_{s}(0) = 1/k
```

### 1010 nri-binary-step-v1 3

```math
p_{s}(j/k) = (j+1)/k \text{ for } j=0,\ldots ,k-1
```

### 1011 nri-binary-step-v1 4

```math
p_{s}(1) = 1
```

### 1012 nri-binary-step-v1 5

```math
Y_{i} \mid  X_{i}=x \sim \mathrm{Bernoulli}(p_{s}(x)) \text{ independently }
```

### 1013 nri-binary-step-v1 6

```math
m_{s}(0.5) = \mathbb{E}[Y \mid  X=0.5] = p_{s}(0.5) = (\lfloor k\cdot 0.5\rfloor+1)/k
```

### 1014 nri-binary-step-v1 7

```math
\text{ for } s=0.5, k=10: \lfloor 5.0\rfloor=5, \mathrm{value}=6/10=0.6
```

### 1015 nri-binary-wave-v1 0

```math
X_{i} \sim \mathrm{Uniform}[0,1] \text{ independently }
```

### 1016 nri-binary-wave-v1 1

```math
p_{s}(x) = 0.5 - (2s-1)(x-0.5) + 8s(x-0.5)^{3}, s \in \{0,0.1,\ldots ,1\}
```

### 1017 nri-binary-wave-v1 2

```math
p_{s}(x) = 8s\cdot x^{3} - 12s\cdot x^{2} + (4s+1)\cdot x
```

### 1018 nri-binary-wave-v1 3

```math
p_{s}(0)=0
```

### 1019 nri-binary-wave-v1 4

```math
p_{s}(0.5)=0.5 \text{ for } \text{ all } s
```

### 1020 nri-binary-wave-v1 5

```math
p_{s}(1)=1
```

### 1021 nri-binary-wave-v1 6

```math
s=0 \mathrm{reduces} \text{ to } p(x)=x (\mathrm{excluded} \text{ as } \mathrm{duplicate})
```

### 1022 nri-binary-wave-v1 7

```math
p_{s}'(x) = -(2s-1) + 24s(x-0.5)^{2}
```

### 1023 nri-binary-wave-v1 8

```math
\mathrm{monotone} \text{ on } [0,1] \mathrm{iff} s\leq 0.5
```

### 1024 nri-binary-wave-v1 9

```math
Y_{i} \mid  X_{i}=x \sim \mathrm{Bernoulli}(p_{s}(x)) \text{ independently }
```

### 1025 nri-binary-wave-v1 10

```math
m_{s}(0.5) = \mathbb{E}[Y \mid  X=0.5] = p_{s}(0.5) = 0.5 \text{ for } \text{ all } s
```

### 1026 nri-hall-horowitz-2013-gaussian-bump-v1 0

```math
X_{i} \text{ iid } \mathrm{Uniform}[-1,1].
```

### 1027 nri-hall-horowitz-2013-gaussian-bump-v1 1

```math
\varepsilon_{i}\overset{\mathrm{iid}}{\sim} \mathcal{N}(0,\sigma^{2}), \sigma\in \{1,0.5,0.2\}
```

### 1028 nri-hall-horowitz-2013-gaussian-bump-v1 2

```math
Y_{i}=g_{1}(X_{i})+\varepsilon_{i}.
```

### 1029 nri-hall-horowitz-2013-gaussian-bump-v1 3

```math
\theta(x_{0})=\mathbb{E}[Y\mid X=x_{0}]=g_{1}(x_{0})
```

### 1030 nri-hallhorowitz-2013-band-v1 0

```math
X_{i}\overset{\mathrm{iid}}{\sim} \mathrm{Uniform}(-1,1)
```

### 1031 nri-hallhorowitz-2013-band-v1 1

```math
g_{1}(x)=x+5\cdot \exp(-50\cdot x^{2})/\sqrt{2\cdot \pi}
```

### 1032 nri-hallhorowitz-2013-band-v1 2

```math
g_{2}(x)=\sin(3\cdot \pi\cdot x/2)/(1+18\cdot x^{2}\cdot (\mathrm{sgn}(x)+1))
```

### 1033 nri-hallhorowitz-2013-band-v1 3

```math
g_{3}(x)=\sin(\pi\cdot x/2)/(1+2\cdot x^{2}\cdot (\mathrm{sgn}(x)+1))
```

### 1034 nri-hallhorowitz-2013-band-v1 4

```math
\mathrm{sgn}(x)=-1/0/1 \text{ for } x<0/=0/>0
```

### 1035 nri-hallhorowitz-2013-band-v1 5

```math
\varepsilon_{i}\overset{\mathrm{iid}}{\sim} \mathcal{N}(0,\sigma^{2})
```

### 1036 nri-hallhorowitz-2013-band-v1 6

```math
Y_{i}=g_{j}(X_{i})+\varepsilon_{i}
```

### 1037 nri-liangliu-2010-singleindex-v1 0

```math
\mathrm{For} \text{ each } \mathrm{row} i=1..n, \text{ independently } \mathrm{draw} Z_{i1},Z_{i2},Z_{i3}\overset{\mathrm{iid}}{\sim} \mathrm{Uniform}(0,1)
```

### 1038 nri-liangliu-2010-singleindex-v1 1

```math
t_{i}=(Z_{i1}+Z_{i2}+Z_{i3})/\sqrt{3}, \text{ with } 0\leq t_{i}\leq \sqrt{3}
```

### 1039 nri-liangliu-2010-singleindex-v1 2

```math
m_{i}=\sin(\pi\cdot (t_{i}-0.3912)/(1.3409-0.3912))+0.3\cdot X_{i}
```

### 1040 nri-liangliu-2010-singleindex-v1 3

```math
\varepsilon_{i}\overset{\mathrm{iid}}{\sim} \mathcal{N}(0,1)
```

### 1041 nri-liangliu-2010-singleindex-v1 4

```math
\mathrm{Source} \mathrm{multiplier} 0.1 \mathrm{gives} \text{ noise } \mathrm{sd}=0.1 \text{ and } \text{ variance }=0.01
```

### 1042 nri-liangliu-2010-singleindex-v1 5

```math
Y_{i}=m_{i}+0.1\cdot \varepsilon_{i}
```

### 1043 nri-highdim-sparse-additive-v1 0

```math
\mathrm{For} \text{ each } \mathrm{row} i \text{ and } j=1,\ldots ,600: W_{ij},U_{i} \mathrm{are} \text{ mutually } \text{ iid } \mathrm{Uniform}[0,1]
```

### 1044 nri-highdim-sparse-additive-v1 1

```math
X_{ij}=(W_{ij}+0.3 U_{i})/1.3.
```

### 1045 nri-highdim-sparse-additive-v1 2

```math
Y_{i}=\sum_{j=1}^{4} f_{j}(X_{ij})+\varepsilon_{i}, \varepsilon_{i}\overset{\mathrm{iid}}{\sim} \mathcal{N}(0,1.5^{2})
```

### 1046 nri-highdim-sparse-additive-v1 3

```math
f_{1}(t)=6[0.1 \sin(2 \pi t)+0.2 \cos(2 \pi t)+0.3 \sin^{2}(2 \pi t)+0.4 \cos^{3}(2 \pi t)+0.5 \sin^{3}(2 \pi t)]
```

### 1047 nri-highdim-sparse-additive-v1 4

```math
f_{2}(t)=3(2t-1)^{2}
```

### 1048 nri-highdim-sparse-additive-v1 5

```math
f_{3}(t)=5t
```

### 1049 nri-highdim-sparse-additive-v1 6

```math
f_{4}(t)=4 \sin(2 \pi t)/(2-\sin(2 \pi t))
```
