# Math probe batch 5

### 700 did-ye-2024-code-case2-gaussian-bracketing-v1 5

```math
\mathrm{Population} \mathrm{ATT4}=1
```

### 701 did-zhao-cui-2025-bridge-iv-v1 0

```math
X_{1},X_{2}\overset{\mathrm{iid}}{\sim} \mathcal{N}(0,1)
```

### 702 did-zhao-cui-2025-bridge-iv-v1 1

```math
Z,T\overset{\mathrm{iid}}{\sim} \mathrm{Bernoulli}(0.5)
```

### 703 did-zhao-cui-2025-bridge-iv-v1 2

```math
U_{0},U_{1} \text{ iid } \mathrm{bridge}(\phi=0.5), \mathrm{density} f(u)=1/[2\cdot \pi\cdot \cosh(u/2)]
```

### 704 did-zhao-cui-2025-bridge-iv-v1 3

```math
p_{0}=\mathrm{expit}(2-7Z+0.2U_{0}+2X_{1})
```

### 705 did-zhao-cui-2025-bridge-iv-v1 4

```math
p_{1}=\mathrm{expit}(-1.5+5Z-0.15U_{1}+1.5X_{2})
```

### 706 did-zhao-cui-2025-bridge-iv-v1 5

```math
A_{0}\sim \mathrm{Bernoulli}(p_{0})
```

### 707 did-zhao-cui-2025-bridge-iv-v1 6

```math
A_{1}\sim \mathrm{Bernoulli}(p_{1}), \text{ conditionally } \text{ independent }.
```

### 708 did-zhao-cui-2025-bridge-iv-v1 7

```math
s(X)=1.5X_{1}+2X_{2}-0.5
```

### 709 did-zhao-cui-2025-bridge-iv-v1 8

```math
Y_{0}=200+10\cdot [A_{0}\cdot s(X)+0.5U_{0}+2Z+1.5X_{1}+2X_{2}]+e_{0}
```

### 710 did-zhao-cui-2025-bridge-iv-v1 9

```math
Y_{1}=240+10\cdot [A_{1}\cdot s(X)+0.5U_{1}+2Z+2X_{1}+1.5X_{2}]+e_{1}
```

### 711 did-zhao-cui-2025-bridge-iv-v1 10

```math
e_{0},e_{1}\overset{\mathrm{iid}}{\sim} \mathcal{N}(0,1)
```

### 712 did-zhao-cui-2025-bridge-iv-v1 11

```math
A=(1-T)\cdot A_{0}+T\cdot A_{1}
```

### 713 did-zhao-cui-2025-bridge-iv-v1 12

```math
Y=(1-T)\cdot Y_{0}+T\cdot Y_{1}
```

### 714 did-zhao-cui-2025-bridge-iv-v1 13

```math
\mathrm{paper} \mathrm{baseline} n=5000 \text{ independently } \mathrm{tested}
```

### 715 did-zhao-cui-2025-bridge-iv-v1 14

```math
\tau_{t}(x)=\mathbb{E}[Y_{t}(1)-Y_{t}(0)\mid X=x]=10\cdot s(x)
```

### 716 did-zhao-cui-2025-bridge-iv-v1 15

```math
\mathrm{ATE}=\mathbb{E}[\tau_{t}(X)]=-5
```

### 717 did-zhao-cui-2025-instrumented-v1 0

```math
Z_i\sim \mathrm{Bernoulli}(0.5),\quad T_i\sim \mathrm{Bernoulli}(0.5)
```

### 718 did-zhao-cui-2025-instrumented-v1 1

```math
f_U(u)=\frac{1}{2\pi\cosh(u/2)},\quad E[U_{ti}]=0,\quad \mathrm{Var}(U_{ti})=\pi^2
```

### 719 did-zhao-cui-2025-instrumented-v1 2

```math
V_{ti}\sim\mathrm{Uniform}(0,1),\quad U_{ti}=2\log\tan(\pi V_{ti}/2)
```

### 720 did-zhao-cui-2025-instrumented-v1 3

```math
A_{0i}\mid X_i,Z_i,U_{0i}\sim\mathrm{Bernoulli}\left(\frac{1}{1+\exp[-(2-7Z_i+0.2U_{0i}+2X_{1i})]}\right)
```

### 721 did-zhao-cui-2025-instrumented-v1 4

```math
A_{1i}\mid X_i,Z_i,U_{1i}\sim\mathrm{Bernoulli}\left(\frac{1}{1+\exp[-(-1.5+5Z_i-0.15U_{1i}+1.5X_{2i})]}\right)
```

### 722 did-zhao-cui-2025-instrumented-v1 5

```math
h(X_{i})=1.5X_{1i}+2X_{2i}-0.5
```

### 723 did-zhao-cui-2025-instrumented-v1 6

```math
Y_{0i}=200+10[A_{0i}h(X_i)+0.5U_{0i}+2Z_i+1.5X_{1i}+2X_{2i}]+\epsilon_{0i}
```

### 724 did-zhao-cui-2025-instrumented-v1 7

```math
Y_{1i}=240+10[A_{1i}h(X_i)+0.5U_{1i}+2Z_i+2X_{1i}+1.5X_{2i}]+\epsilon_{1i}
```

### 725 did-zhao-cui-2025-instrumented-v1 8

```math
A_i=(1-T_i)A_{0i}+T_iA_{1i},\quad Y_i=(1-T_i)Y_{0i}+T_iY_{1i}
```

### 726 did-zhao-cui-2025-instrumented-v1 9

```math
\mathrm{ATE}=\mathbb{E}[10h(X_{i})]=-5
```

### 727 iv-athey-tibshirani-wager-2019-compliance-v1 0

```math
X \sim \mathcal{N}(0,I_{10})
```

### 728 iv-athey-tibshirani-wager-2019-compliance-v1 1

```math
\varepsilon\sim \mathcal{N}(0,1)
```

### 729 iv-athey-tibshirani-wager-2019-compliance-v1 2

```math
Z \sim \mathrm{Bernoulli}(1/3)
```

### 730 iv-athey-tibshirani-wager-2019-compliance-v1 3

```math
Q\mid \varepsilon\sim \mathrm{Bernoulli}(\mathrm{expit}(\omega\varepsilon))
```

### 731 iv-athey-tibshirani-wager-2019-compliance-v1 4

```math
A=ZQ
```

### 732 iv-athey-tibshirani-wager-2019-compliance-v1 5

```math
Y=\mu(X)+(A-1/2)\tau(X)+\varepsilon.
```

### 733 iv-athey-tibshirani-wager-2019-compliance-v1 6

```math
\tau(x)=\sum_{j=1}^{k} \max(0,x_{j})
```

### 734 iv-athey-tibshirani-wager-2019-compliance-v1 7

```math
\mu(x)=c[\max(0,x_{5})+\max(0,x_{6})].
```

### 735 iv-athey-tibshirani-wager-2019-compliance-v1 8

```math
\tau(x)=\max(0,\sum_{j=1}^{k} x_{j})
```

### 736 iv-athey-tibshirani-wager-2019-compliance-v1 9

```math
\mu(x)=c \max(0,x_{5}+x_{6}).
```

### 737 iv-athey-tibshirani-wager-2019-compliance-v1 10

```math
k \in \{2,4\}
```

### 738 iv-athey-tibshirani-wager-2019-compliance-v1 11

```math
\omega\in \{0,1\}
```

### 739 iv-athey-tibshirani-wager-2019-compliance-v1 12

```math
c \in \{0,3\}
```

### 740 iv-athey-tibshirani-wager-2019-compliance-v1 13

```math
p=10.
```

### 741 iv-ding-2017-binary-bias-v1 0

```math
Z \sim \mathrm{Bernoulli}(0.5)
```

### 742 iv-ding-2017-binary-bias-v1 1

```math
U \sim \mathrm{Bernoulli}(0.5), V_{A},V_{Y}\overset{\mathrm{iid}}{\sim} \mathrm{Uniform}(0,1)
```

### 743 iv-ding-2017-binary-bias-v1 2

```math
p[z,u]=P(A=1|Z=z,U=u), r[\text{ a },u]=P(Y=1|A=\text{ a },U=u)
```

### 744 iv-ding-2017-binary-bias-v1 3

```math
A(z)=1\{V_{A}<p[z,U]\}
```

### 745 iv-ding-2017-binary-bias-v1 4

```math
A=A(Z)
```

### 746 iv-ding-2017-binary-bias-v1 5

```math
Y(\text{ a })=1\{V_{Y}<r[\text{ a },U]\}
```

### 747 iv-ding-2017-binary-bias-v1 6

```math
Y=Y(A).
```

### 748 iv-ding-2017-binary-bias-v1 7

```math
q=(0.5,0.5), \delta[u]=p[1,u]-p[0,u], \tau[u]=r[1,u]-r[0,u].
```

### 749 iv-ding-2017-binary-bias-v1 8

```math
\mathrm{LATE}=\sum_{u} q[u]\cdot \delta[u]\cdot \tau[u] / \sum_{u} q[u]\cdot \delta[u].
```

### 750 iv-ding-2017-binary-bias-v1 9

```math
\mathrm{Source} \text{ population } \mathrm{ATE}=\sum_{u} q[u]\cdot \tau[u]
```

### 751 iv-kang-2016-invalid-linear-v1 0

```math
Z_{j}\overset{\mathrm{iid}}{\sim} \mathcal{N}(0,1), j=1,\ldots ,10
```

### 752 iv-kang-2016-invalid-linear-v1 1

```math
(\xi,\varepsilon) \mathrm{joint} \mathrm{normal}: \text{ mean } 0, \mathrm{variances} 1, \mathrm{correlation} \rho=0.8.
```

### 753 iv-kang-2016-invalid-linear-v1 2

```math
D=1+\sum_{j=1}^{10} Z_{j}+\xi.
```

### 754 iv-kang-2016-invalid-linear-v1 3

```math
Y=1+Z_{1}+Z_{2}+Z_{3}+\beta D+\varepsilon
```

### 755 iv-kang-2016-invalid-linear-v1 4

```math
\beta=1.
```

### 756 mdi-han-wang-2013-quadratic-mean-v1 0

```math
X \sim \mathrm{Uniform}(-2.5,2.5)
```

### 757 mdi-han-wang-2013-quadratic-mean-v1 1

```math
Y\mid X=x \sim \mathcal{N}(1+2x+3x^{2}, 4x^{2}+2), \text{ with } \mathrm{second} \mathrm{argument} \text{ variance }
```

### 758 mdi-han-wang-2013-quadratic-mean-v1 2

```math
R\mid X=x \sim \mathrm{Bernoulli}(1/[1+\exp(0.8+0.5x-0.3x^{2})])
```

### 759 mdi-han-wang-2013-quadratic-mean-v1 3

```math
R=1 \mathrm{means} \text{ observed }
```

### 760 mdi-han-wang-2013-quadratic-mean-v1 4

```math
Y_{\mathrm{observed}}=Y \text{ when } R=1 \text{ and } 0 \text{ placeholder } \text{ when } R=0
```

### 761 mdi-han-wang-2013-quadratic-mean-v1 5

```math
\theta=\mathbb{E}(Y)=7.25
```

### 762 mdi-hu-follmann-qin-2010-cubic-mean-v1 0

```math
X_{1},X_{2} \text{ independently } \sim \mathcal{N}(0,1)
```

### 763 mdi-hu-follmann-qin-2010-cubic-mean-v1 1

```math
Y\mid X \sim \mathcal{N}((X_{1}+X_{2})^{3},1)
```

### 764 mdi-hu-follmann-qin-2010-cubic-mean-v1 2

```math
R\mid X \sim \mathrm{Bernoulli}(\pi(X)), \pi(X)=1-1/[1+\exp(1-3X_{1}+2X_{2}^{2})]=\mathrm{expit}(1-3X_{1}+2X_{2}^{2})
```

### 765 mdi-hu-follmann-qin-2010-cubic-mean-v1 3

```math
Y_{\mathrm{observed}}=Y \text{ if } R=1, \text{ otherwise } 0 \text{ placeholder }
```

### 766 mdi-hu-follmann-qin-2010-cubic-mean-v1 4

```math
\theta=\mathbb{E}(Y)=\mathbb{E}[(X_{1}+X_{2})^{3}]=0
```

### 767 mdi-hu-follmann-wang-2014-linear-balance-v2 0

```math
Y=3X_{1}+5X_{2}+\varepsilon, \varepsilon\text{ independent } \mathcal{N}(0,1)
```

### 768 mdi-hu-follmann-wang-2014-linear-balance-v2 1

```math
R\mid X\sim \mathrm{Bernoulli}(\mathrm{expit}(X_{1}))
```

### 769 mdi-hu-follmann-wang-2014-linear-balance-v2 2

```math
Y_{\mathrm{observed}}=Y \text{ if } R=1
```

### 770 mdi-hu-follmann-wang-2014-linear-balance-v2 3

```math
\theta=\mathbb{E}(Y)=0
```

### 771 mdi-liu-fan-2023-light-tail-model2-v1 0

```math
P=\pi(X) \mathrm{generated} \mathrm{directly}: \mathrm{Pr}(P\leq u)=u^{\gamma-1}, u \in [0,1]
```

### 772 mdi-liu-fan-2023-light-tail-model2-v1 1

```math
\gamma=2.5
```

### 773 mdi-liu-fan-2023-light-tail-model2-v1 2

```math
\eta\sim \chi-\mathrm{square}(4)
```

### 774 mdi-liu-fan-2023-light-tail-model2-v1 3

```math
Y=1-P+c\cdot (\eta-4)/\sqrt{8}
```

### 775 mdi-liu-fan-2023-light-tail-model2-v1 4

```math
c=1 (\mathrm{Model} 2)
```

### 776 mdi-liu-fan-2023-light-tail-model2-v1 5

```math
D\mid P\sim \mathrm{Bernoulli}(P)
```

### 777 mdi-liu-fan-2023-light-tail-model2-v1 6

```math
D=1 \mathrm{means} Y \text{ observed }
```

### 778 mdi-liu-fan-2023-light-tail-model2-v1 7

```math
Y_{\mathrm{observed}}=Y \text{ when } D=1 \text{ and } 0 \text{ placeholder } \text{ when } D=0
```

### 779 mdi-liu-fan-2023-light-tail-model2-v1 8

```math
\theta=\mathbb{E}(Y)=1/\gamma=0.4
```

### 780 mdi-mueller-2009-cosine-mean-mar-v1 0

```math
X\sim \mathrm{Uniform}(-1,1)
```

### 781 mdi-mueller-2009-cosine-mean-mar-v1 1

```math
\varepsilon\sim \mathcal{N}(0,1)
```

### 782 mdi-mueller-2009-cosine-mean-mar-v1 2

```math
Y=\cos(2X)+\varepsilon
```

### 783 mdi-mueller-2009-cosine-mean-mar-v1 3

```math
R\mid X=x\sim \mathrm{Bernoulli}(\mathrm{expit}(x)).
```

### 784 mdi-mueller-2009-cosine-mean-mar-v1 4

```math
Y_{\mathrm{observed}}=Y \text{ if } R=1, \mathrm{else} \mathrm{finite} \mathrm{zero} \text{ placeholder }.
```

### 785 mdi-mueller-2009-cosine-mean-mar-v1 5

```math
\theta=\mathbb{E}(Y)=0.454648713412841
```

### 786 mdi-rotnitzky-lei-sued-robins-2012-continuous-first-v1 0

```math
(L_{1},L_{2},L_{3},L_{4},\varepsilon) \sim \mathcal{N}(0,I_{5})
```

### 787 mdi-rotnitzky-lei-sued-robins-2012-continuous-first-v1 1

```math
Y=210+27.4L_{1}+13.7(L_{2}+L_{3}+L_{4})+\varepsilon
```

### 788 mdi-rotnitzky-lei-sued-robins-2012-continuous-first-v1 2

```math
A\mid L\sim \mathrm{Bernoulli}(\mathrm{expit}(-L_{1}+0.5L_{2}-0.25L_{3}-0.1L_{4}))
```

### 789 mdi-rotnitzky-lei-sued-robins-2012-continuous-first-v1 3

```math
A=1 \mathrm{means} Y \text{ observed }
```

### 790 mdi-rotnitzky-lei-sued-robins-2012-continuous-first-v1 4

```math
Y_{\mathrm{observed}}=Y \text{ if } A=1, \text{ otherwise } \mathrm{finite} \mathrm{zero} \text{ placeholder }
```

### 791 mdi-rotnitzky-lei-sued-robins-2012-continuous-first-v1 5

```math
\beta_{0}=\mathbb{E}(Y)=210
```

### 792 mdi-vermeulen-vansteelandt-2015-quadratic-logistic-v1 0

```math
X\sim \mathcal{N}(0,1)
```

### 793 mdi-vermeulen-vansteelandt-2015-quadratic-logistic-v1 1

```math
Y\mid X=x\sim \mathcal{N}(x^{2},1)
```

### 794 mdi-vermeulen-vansteelandt-2015-quadratic-logistic-v1 2

```math
R\mid X=x\sim \mathrm{Bernoulli}(\mathrm{expit}(x)).
```

### 795 mdi-vermeulen-vansteelandt-2015-quadratic-logistic-v1 3

```math
Y_{\mathrm{observed}}=Y \text{ when } R=1, \text{ and } \mathrm{finite} 0 \text{ placeholder } \text{ when } R=0.
```

### 796 mdi-vermeulen-vansteelandt-2015-quadratic-logistic-v1 4

```math
\theta=\mathbb{E}(Y)=1
```

### 797 mdi-yiu-fong-holmes-rousseau-2025-piecewise-mean-mar-v1 0

```math
X\sim \mathrm{Uniform}[-1,1]
```

### 798 mdi-yiu-fong-holmes-rousseau-2025-piecewise-mean-mar-v1 1

```math
m(x)=\begin{cases}
(x+2)^{2}/2 & x\in [-1,-0.5) \\
x/2+0.875 & x\in [-0.5,0) \\
-5(x-0.2)^{2}+1.075 & x\in [0,0.5) \\
x+0.125 & x\in [0.5,1]
\end{cases}
```

### 799 mdi-yiu-fong-holmes-rousseau-2025-piecewise-mean-mar-v1 2

```math
Y\mid X=x\sim \mathcal{N}(m(x), [0.2-0.1\cos(2\pi x)]^{2})
```

### 800 mdi-yiu-fong-holmes-rousseau-2025-piecewise-mean-mar-v1 3

```math
R\mid X=x\sim \mathrm{Bernoulli}(0.5+0.4\mathrm{sign}(x)).
```

### 801 mdi-yiu-fong-holmes-rousseau-2025-piecewise-mean-mar-v1 4

```math
Y_{\mathrm{observed}}=Y \text{ if } R=1, \mathrm{else} \mathrm{finite} \mathrm{zero} \text{ placeholder }.
```

### 802 mdi-yiu-fong-holmes-rousseau-2025-piecewise-mean-mar-v1 5

```math
\theta=\mathbb{E}(Y)=0.84375
```

### 803 mediation-cheng-li-2025-principal-strata-kang-schafer-v1 0

```math
X = (X_{1}, X_{2}, X_{3}, X_{4}) \sim \mathcal{N}(0_{4\times 1}, I_{4\times 4})
```

### 804 mediation-cheng-li-2025-principal-strata-kang-schafer-v1 1

```math
Z \mid  X \sim \mathrm{Bernoulli}(\mathrm{expit}([-1, 0.5, -0.25, -0.1]^{T} X))
```

### 805 mediation-cheng-li-2025-principal-strata-kang-schafer-v1 2

```math
D \mid  Z, X \sim \mathrm{Bernoulli}(\mathrm{expit}(-1 + 2 Z + [1, -0.8, 0.6, -1]^{T} X))
```

### 806 mediation-cheng-li-2025-principal-strata-kang-schafer-v1 3

```math
M \mid  D, Z, X \sim \mathrm{Bernoulli}(\mathrm{expit}(-1.8 + 2 Z + 1.5 D + [1, -0.5, 0.9, -1]^{T} X))
```

### 807 mediation-cheng-li-2025-principal-strata-kang-schafer-v1 4

```math
Y \mid  M, D, Z, X \sim \mathcal{N}(210 + 1.5 Z - D + M + [27.4, 13.7, 13.7, 13.7]^{T} X, 1)
```

### 808 mediation-diaz-et-al-2021-intermediate-confounding-v1 0

```math
W_{1}\sim \mathrm{Bern}(0.6), W_{2}|W_{1}\sim \mathrm{Bern}(0.3), W_{3}|W_{1},W_{2}\sim \mathrm{Bern}(0.2+(W_{1}+W_{2})/3)
```

### 809 mediation-diaz-et-al-2021-intermediate-confounding-v1 1

```math
A\mid W\sim \mathrm{Bern}(\mathrm{expit}(0.25 \sum(W)+3W_{1}W_{2}-2))
```

### 810 mediation-diaz-et-al-2021-intermediate-confounding-v1 2

```math
Z\mid A,W\sim \mathrm{Bern}(\mathrm{expit}(\sum(W)/3-A-\mathrm{AW3}-0.25))
```

### 811 mediation-diaz-et-al-2021-intermediate-confounding-v1 3

```math
M\mid Z,A,W\sim \mathrm{Bern}(\mathrm{expit}(W_{1}+W_{2}+A-Z+AZ-0.3\mathrm{AW2}))
```

### 812 mediation-diaz-et-al-2021-intermediate-confounding-v1 4

```math
Y\mid M,Z,A,W\sim \mathrm{Bern}(\mathrm{expit}((A-Z+M-AZ)/(\sum(W)+1)))
```

### 813 mediation-diaz-hejazi-2020-discrete-three-mediators-v1 0

```math
W_{1}\sim \mathrm{Bern}(0.50)
```

### 814 mediation-diaz-hejazi-2020-discrete-three-mediators-v1 1

```math
W_{2}\sim \mathrm{Bern}(0.65)
```

### 815 mediation-diaz-hejazi-2020-discrete-three-mediators-v1 2

```math
W_{3}\sim \mathrm{Bern}(0.35)
```

### 816 mediation-diaz-hejazi-2020-discrete-three-mediators-v1 3

```math
A\mid W\sim \mathrm{Bern}((W_{1}+W_{2}+W_{3})/4 + 0.1)
```

### 817 mediation-diaz-hejazi-2020-discrete-three-mediators-v1 4

```math
Z_{1}\mid A,W\sim \mathrm{Bern}(1-\mathrm{expit}((A+W_{1})/(A+W_{1}+0.5)))
```

### 818 mediation-diaz-hejazi-2020-discrete-three-mediators-v1 5

```math
Z_{2}\mid A,W\sim \mathrm{Bern}(\mathrm{expit}((A-1+W_{2})/(W_{3}+3)))
```

### 819 mediation-diaz-hejazi-2020-discrete-three-mediators-v1 6

```math
Z_{3}\mid A,W\sim \mathrm{Bern}(\mathrm{expit}((A-1+2W_{1}-1)/(2W_{1}+0.5)))
```

### 820 mediation-diaz-hejazi-2020-discrete-three-mediators-v1 7

```math
Y=Z_{1}+Z_{2}-Z_{3}+A-0.1(W_{1}+W_{2}+W_{3})^{2}+\varepsilon, \varepsilon\sim \mathcal{N}(0,0.25)
```

### 821 mediation-he-song-xu-2024-single-linear-v1 0

```math
A\sim \mathrm{Bern}(0.5)
```

### 822 mediation-he-song-xu-2024-single-linear-v1 1

```math
X_{1}\sim \mathcal{N}(0,1)
```

### 823 mediation-he-song-xu-2024-single-linear-v1 2

```math
X_{2}\sim \mathrm{Bern}(0.5), \text{ independently }
```

### 824 mediation-he-song-xu-2024-single-linear-v1 3

```math
M=\alpha_{S} A+1+X_{1}+X_{2}+\varepsilon_{M}, \varepsilon_{M}\sim \mathcal{N}(0,0.5^{2})
```

### 825 mediation-he-song-xu-2024-single-linear-v1 4

```math
Y=\beta_{M} M+1+X_{1}+X_{2}+A+\varepsilon_{Y}, \varepsilon_{Y}\sim \mathcal{N}(0,0.5^{2})
```

### 826 mediation-jones-2024-sparse-mediators-lnl-v1 0

```math
X_{l} \sim \mathcal{N}(0, 1/4) \text{ independently }, l = 1, 2, 3
```

### 827 mediation-jones-2024-sparse-mediators-lnl-v1 1

```math
\mu_{\mathrm{D0}}(X) = \mathrm{expit}\{0.8 (X_{1} + X_{2})\}
```

### 828 mediation-jones-2024-sparse-mediators-lnl-v1 2

```math
\psi_{M}(X) = X_{1}^{2} + X_{2} - X_{3}
```

### 829 mediation-jones-2024-sparse-mediators-lnl-v1 3

```math
\psi_{Y}(X) = 2 (X_{1} - 0.5) + X_{2} + 2 X_{3}
```

### 830 mediation-jones-2024-sparse-mediators-lnl-v1 4

```math
D \mid  X \sim \mathrm{Bernoulli}(\mu_{\mathrm{D0}}(X))
```

### 831 mediation-jones-2024-sparse-mediators-lnl-v1 5

```math
M = \alpha_{0} D + \psi_{M}(X) 1_{p} + \eta, \eta_{j} \sim \mathcal{N}(0, 1) \text{ independently }, p = 10, \alpha_{0} = (1, 2, 2, 0, \ldots , 0)
```

### 832 mediation-jones-2024-sparse-mediators-lnl-v1 6

```math
Y = \gamma_{0} D + \beta_{0}' M + \psi_{Y}(X) + \varepsilon, \varepsilon\sim \mathcal{N}(0, 1)
```

### 833 mediation-jones-2024-sparse-mediators-lnl-v1 7

```math
\gamma_{0} = 2, \beta_{0} = (0.8, 0.4, 0.4, 0, \ldots , 0)
```

### 834 mediation-jones-2024-sparse-mediators-lnl-v1 8

```math
\mathrm{NDE} = \gamma_{0} = 2
```

### 835 mediation-jones-2024-sparse-mediators-lnl-v1 9

```math
\mathrm{NIE} = \alpha_{0} . \beta_{0} = 2.4
```

### 836 mediation-jones-2024-sparse-mediators-lnn-v1 0

```math
X_{l} \sim \mathcal{N}(0, 1/4) \text{ independently }, l = 1, 2, 3
```

### 837 mediation-jones-2024-sparse-mediators-lnn-v1 1

```math
\mu_{\mathrm{D0}}(X) = \mathrm{expit}\{0.8 (X_{1} + X_{2})\}
```

### 838 mediation-jones-2024-sparse-mediators-lnn-v1 2

```math
\psi_{M}(X) = X_{1}^{2} + X_{2} - X_{3}
```

### 839 mediation-jones-2024-sparse-mediators-lnn-v1 3

```math
\psi_{Y}(X) = 2 (X_{1} - 0.5)^{2} + X_{2} + 2 X_{3}
```

### 840 mediation-jones-2024-sparse-mediators-lnn-v1 4

```math
D \mid  X \sim \mathrm{Bernoulli}(\mu_{\mathrm{D0}}(X))
```

### 841 mediation-jones-2024-sparse-mediators-lnn-v1 5

```math
M = \alpha_{0} D + \psi_{M}(X) 1_{p} + \eta, \eta_{j} \sim \mathcal{N}(0, 1) \text{ independently }, p = 10, \alpha_{0} = (1, 2, 2, 0, \ldots , 0)
```

### 842 mediation-jones-2024-sparse-mediators-lnn-v1 6

```math
Y = \gamma_{0} D + \beta_{0}' M + \psi_{Y}(X) + \varepsilon, \varepsilon\sim \mathcal{N}(0, 1)
```

### 843 mediation-jones-2024-sparse-mediators-lnn-v1 7

```math
\gamma_{0} = 2, \beta_{0} = (0.8, 0.4, 0.4, 0, \ldots , 0)
```

### 844 mediation-jones-2024-sparse-mediators-lnn-v1 8

```math
\mathrm{NDE} = \gamma_{0} = 2
```

### 845 mediation-jones-2024-sparse-mediators-lnn-v1 9

```math
\mathrm{NIE} = \alpha_{0} . \beta_{0} = 2.4
```

### 846 mediation-jones-2024-sparse-mediators-nnn-v1 0

```math
X_{l} \sim \mathcal{N}(0, 1/4) \text{ independently }, l = 1, 2, 3
```

### 847 mediation-jones-2024-sparse-mediators-nnn-v1 1

```math
\mu_{\mathrm{D0}}(X) = \mathrm{expit}\{0.8 (X_{1} X_{2} + X_{2})\}
```

### 848 mediation-jones-2024-sparse-mediators-nnn-v1 2

```math
\psi_{M}(X) = X_{1}^{2} + X_{2} - X_{3}
```

### 849 mediation-jones-2024-sparse-mediators-nnn-v1 3

```math
\psi_{Y}(X) = 2 (X_{1} - 0.5)^{2} + X_{2} + 2 X_{3}
```

### 850 mediation-jones-2024-sparse-mediators-nnn-v1 4

```math
D \mid  X \sim \mathrm{Bernoulli}(\mu_{\mathrm{D0}}(X))
```

### 851 mediation-jones-2024-sparse-mediators-nnn-v1 5

```math
M = \alpha_{0} D + \psi_{M}(X) 1_{p} + \eta, \eta_{j} \sim \mathcal{N}(0, 1) \text{ independently }, p = 10, \alpha_{0} = (1, 2, 2, 0, \ldots , 0)
```

### 852 mediation-jones-2024-sparse-mediators-nnn-v1 6

```math
Y = \gamma_{0} D + \beta_{0}' M + \psi_{Y}(X) + \varepsilon, \varepsilon\sim \mathcal{N}(0, 1)
```

### 853 mediation-jones-2024-sparse-mediators-nnn-v1 7

```math
\gamma_{0} = 2, \beta_{0} = (0.8, 0.4, 0.4, 0, \ldots , 0)
```

### 854 mediation-jones-2024-sparse-mediators-nnn-v1 8

```math
\mathrm{NDE} = \gamma_{0} = 2
```

### 855 mediation-jones-2024-sparse-mediators-nnn-v1 9

```math
\mathrm{NIE} = \alpha_{0} . \beta_{0} = 2.4
```

### 856 mediation-jones-et-al-2025-correlated-sparse-v1 0

```math
A\sim \mathrm{Bernoulli}(0.5)
```

### 857 mediation-jones-et-al-2025-correlated-sparse-v1 1

```math
E\sim \mathcal{N}_{100}(0,\Sigma)
```

### 858 mediation-jones-et-al-2025-correlated-sparse-v1 2

```math
\Sigma_{ii}=1
```

### 859 mediation-jones-et-al-2025-correlated-sparse-v1 3

```math
\Sigma_{12}=0.5
```

### 860 mediation-jones-et-al-2025-correlated-sparse-v1 4

```math
\Sigma_{ij}=0.5 \text{ for } i,j\geq 3,i\neq j
```

### 861 mediation-jones-et-al-2025-correlated-sparse-v1 5

```math
\Sigma_{ij}=0.25 \text{ for } i \in \{1,2\},j \in \{3,\ldots ,100\}
```

### 862 mediation-jones-et-al-2025-correlated-sparse-v1 6

```math
M_{j}=\alpha_{j} A+E_{j}, \alpha_{j}=1 \text{ for } j=1,2,3 \text{ and } 0 \text{ otherwise }
```

### 863 mediation-jones-et-al-2025-correlated-sparse-v1 7

```math
Y=2A+M_{1}+M_{2}+M_{4}+M_{5}+M_{6}+\varepsilon_{Y}, \varepsilon_{Y}\sim \mathcal{N}(0,1)
```

### 864 mediation-jones-et-al-2025-correlated-sparse-v1 8

```math
\mathrm{NIE}_{1}=\sum_{j} \alpha_{j} \beta_{j}=2
```

### 865 mediation-luo-et-al-2025-dynamic-markov-v1 0

```math
A_{t}\overset{\mathrm{iid}}{\sim} \mathrm{Bernoulli}(.5), t=1,\ldots ,10
```

### 866 mediation-luo-et-al-2025-dynamic-markov-v1 1

```math
\mathrm{Every} \mathrm{entry} \text{ of } \Theta_{1t}=(\alpha_{1t},\delta_{1t},\Gamma_{1t},\zeta_{1t}) \text{ and } \Theta_{2t}=(\alpha_{2t},\delta_{2t},\gamma_{2t},\zeta_{2t,k}\mathrm{appa}_{t}) \text{ is } \text{ drawn } \text{ independently } \mathrm{Uniform}(-0.5,0.5)
```

### 867 mediation-luo-et-al-2025-dynamic-markov-v1 2

```math
\mu_{t}=\alpha_{1t}+\delta_{1t} A_{t}+\Gamma_{1t} M_{t-1}+\zeta_{1t} R_{t-1}
```

### 868 mediation-luo-et-al-2025-dynamic-markov-v1 3

```math
M_{t}=\mu_{t}+(I-W^{T})^{-1} \varepsilon_{\mathrm{wt}}
```

### 869 mediation-luo-et-al-2025-dynamic-markov-v1 4

```math
\mathrm{Equivalently} M_{t}-\mu_{t}=W^{T}(M_{t}-\mu_{t})+\varepsilon_{\mathrm{wt}}
```

### 870 mediation-luo-et-al-2025-dynamic-markov-v1 5

```math
R_{t}=\alpha_{2t}+\delta_{2t} A_{t}+\gamma_{2t}^{T} M_{t-1}+\zeta_{2t} R_{t-1}+\kappa_{t}^{T} M_{t}+\varepsilon_{rt}
```

### 871 mediation-luo-et-al-2025-dynamic-markov-v1 6

```math
M_{0}=0,R_{0}=0
```

### 872 mediation-luo-et-al-2025-dynamic-markov-v1 7

```math
\eta_{1}^{10}= [E \sum R_{t}|\mathrm{do} A=1 - E \sum R_{t}|\mathrm{do} A=0] - [E \sum R_{t}|\mathrm{do} A=1,M_{t1}=0 - E \sum R_{t}|\mathrm{do} A=0,M_{t1}=0]
```

### 873 mediation-miles-2019-toxicity-path-specific-v1 0

```math
C_{0} \sim \mathrm{Uniform}(0, 2)
```

### 874 mediation-miles-2019-toxicity-path-specific-v1 1

```math
A \mid  C_{0} \sim \mathrm{Bernoulli}(1 - \{1 + \exp(0.9 + 0.3 C_{0})\}^{-1}) = \mathrm{Bernoulli}(\mathrm{expit}(0.9 + 0.3 C_{0}))
```
