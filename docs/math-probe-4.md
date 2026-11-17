# Math probe batch 4

### 525 ate-wager-athey-2018-confounded-null-v1 4

```math
\tau(X)=0
```

### 526 ate-wager-athey-2018-confounded-null-v1 5

```math
Y=m(X)+(A-0.5)\cdot \tau(X)+\varepsilon
```

### 527 ate-wager-athey-2018-confounded-null-v1 6

```math
\varepsilon\sim \mathcal{N}(0,1)
```

### 528 cate-wager-athey-2018-logistic-v1 0

```math
X_{j}\overset{\mathrm{iid}}{\sim} \mathrm{Uniform}(0,1), j=1,\ldots ,6
```

### 529 cate-wager-athey-2018-logistic-v1 1

```math
e(X)=0.5
```

### 530 cate-wager-athey-2018-logistic-v1 2

```math
A\mid X\sim \mathrm{Bernoulli}(e(X))
```

### 531 cate-wager-athey-2018-logistic-v1 3

```math
m(X)=0
```

### 532 cate-wager-athey-2018-logistic-v1 4

```math
\tau(X)=s(X_{1})\cdot s(X_{2}), s(u)=1+1/[1+\exp(-20\cdot (u-1/3))]
```

### 533 cate-wager-athey-2018-logistic-v1 5

```math
Y=m(X)+(A-0.5)\cdot \tau(X)+\varepsilon
```

### 534 cate-wager-athey-2018-logistic-v1 6

```math
\varepsilon\sim \mathcal{N}(0,1)
```

### 535 did-santanna-zhao-2020-panel-dgp1-v1 0

```math
X \sim \mathcal{N}(0,I_{4})
```

### 536 did-santanna-zhao-2020-panel-dgp1-v1 1

```math
Z_{j}=(\mathrm{Ztilde}_{j}-\mathbb{E}[\mathrm{Ztilde}_{j}])/\mathrm{sd}(\mathrm{Ztilde}_{j})
```

### 537 did-santanna-zhao-2020-panel-dgp1-v1 2

```math
\mathrm{Ztilde}=(\exp(X_{1}/2),10+X_{2}/(1+\exp(X_{1})),(0.6+X_{1}\cdot X_{3}/25)^{3},(20+X_{2}+X_{4})^{2})
```

### 538 did-santanna-zhao-2020-panel-dgp1-v1 3

```math
f(Z)=210+27.4\cdot Z_{1}+13.7\cdot (Z_{2}+Z_{3}+Z_{4})
```

### 539 did-santanna-zhao-2020-panel-dgp1-v1 4

```math
g(Z)=0.75\cdot (-Z_{1}+0.5\cdot Z_{2}-0.25\cdot Z_{3}-0.1\cdot Z_{4})
```

### 540 did-santanna-zhao-2020-panel-dgp1-v1 5

```math
D=1\{U\leq \mathrm{sigmoid}(g(Z))\}
```

### 541 did-santanna-zhao-2020-panel-dgp1-v1 6

```math
U\sim U(0,1)
```

### 542 did-santanna-zhao-2020-panel-dgp1-v1 7

```math
v=D\cdot f(Z)+\eta
```

### 543 did-santanna-zhao-2020-panel-dgp1-v1 8

```math
\eta\sim \mathcal{N}(0,1)
```

### 544 did-santanna-zhao-2020-panel-dgp1-v1 9

```math
Y_{\mathrm{pre}}=f(Z)+v+\varepsilon_{0}
```

### 545 did-santanna-zhao-2020-panel-dgp1-v1 10

```math
Y_{1}(d)=2\cdot f(Z)+v+\varepsilon_{1}(d)
```

### 546 did-santanna-zhao-2020-panel-dgp1-v1 11

```math
Y_{\mathrm{post}}=Y_{1}(D)
```

### 547 iv-dikkala-2020-sine-v1 0

```math
Z\sim \mathcal{N}(0,\mathrm{SD}=2)
```

### 548 iv-dikkala-2020-sine-v1 1

```math
U\sim \mathcal{N}(0,\mathrm{SD}=2)
```

### 549 iv-dikkala-2020-sine-v1 2

```math
\delta,\zeta\sim \mathcal{N}(0,\mathrm{SD}=0.1)
```

### 550 iv-dikkala-2020-sine-v1 3

```math
P=0.6\cdot Z+0.4\cdot U+\delta
```

### 551 iv-dikkala-2020-sine-v1 4

```math
Y=\sin(P)+U+\zeta
```

### 552 iv-hartford-2017-demand-v1 0

```math
T\sim \mathrm{Uniform}(0,10)
```

### 553 iv-hartford-2017-demand-v1 1

```math
S\sim \mathrm{DiscreteUniform}(\{1,\ldots ,7\})
```

### 554 iv-hartford-2017-demand-v1 2

```math
Z,V,W\overset{\mathrm{iid}}{\sim} \mathcal{N}(0,1)
```

### 555 iv-hartford-2017-demand-v1 3

```math
\psi(T)=2\cdot ((T-5)^{4}/600+\exp(-4\cdot (T-5)^{2})+T/10-2)
```

### 556 iv-hartford-2017-demand-v1 4

```math
P=25+(Z+3)\cdot \psi(T)+V
```

### 557 iv-hartford-2017-demand-v1 5

```math
e=\rho\cdot V+\sqrt{1-\rho^{2}}\cdot W
```

### 558 iv-hartford-2017-demand-v1 6

```math
\rho=0.8
```

### 559 iv-hartford-2017-demand-v1 7

```math
Y=100+(10+P)\cdot S\cdot \psi(T)-2\cdot P+e
```

### 560 nie-eric-original-v1 0

```math
X_{1} \sim \mathrm{Bernoulli}(0.4)
```

### 561 nie-eric-original-v1 1

```math
X_{2} \mid  X_{1} \sim \mathrm{Bernoulli}(0.3 + 0.4 X_{1})
```

### 562 nie-eric-original-v1 2

```math
X_{3} \mid  X_{1},X_{2} \sim \mathcal{N}(-0.024 - 0.4 X_{1} + 0.4 X_{2}, 1)
```

### 563 nie-eric-original-v1 3

```math
\mathrm{logit} P(A=1\mid X) = 0.4 + X_{1} - X_{2} + 0.1 X_{3} - 1.5 X_{1} X_{3}
```

### 564 nie-eric-original-v1 4

```math
\mathrm{logit} P(M=1\mid A,X) = 0.5 - X_{1} + 0.5 X_{2} - 0.9 X_{3} - 1.5 X_{1} X_{3} + A
```

### 565 nie-eric-original-v1 5

```math
Y = 1 + 0.2 X_{1} + 0.3 X_{2} + 1.4 X_{3} - 2.5 A - 3.5 M + 5 A M + \varepsilon
```

### 566 nie-eric-original-v1 6

```math
\varepsilon\sim \mathcal{N}(0,1)
```

### 567 qr-athey-tibshirani-wager-2019-mean-v1 0

```math
X_{j}\overset{\mathrm{iid}}{\sim} \mathrm{Uniform}(-1,1), j=1,\ldots ,40
```

### 568 qr-athey-tibshirani-wager-2019-mean-v1 1

```math
\varepsilon\sim \mathcal{N}(0,1)
```

### 569 qr-athey-tibshirani-wager-2019-mean-v1 2

```math
Y=0.8\cdot I(X_{1}>0)+\varepsilon
```

### 570 qr-athey-tibshirani-wager-2019-mean-v1 3

```math
Q_{q}(Y\mid X=x)=0.8\cdot I(x_{1}>0)+\Phi_{\mathrm{inverse}}(q)
```

### 571 qr-athey-tibshirani-wager-2019-scale-v1 0

```math
X_{j}\overset{\mathrm{iid}}{\sim} \mathrm{Uniform}(-1,1), j=1,\ldots ,40
```

### 572 qr-athey-tibshirani-wager-2019-scale-v1 1

```math
\varepsilon\sim \mathcal{N}(0,1)
```

### 573 qr-athey-tibshirani-wager-2019-scale-v1 2

```math
Y=(1+I(X_{1}>0))\cdot \varepsilon
```

### 574 qr-athey-tibshirani-wager-2019-scale-v1 3

```math
Q_{q}(Y\mid X=x)=(1+I(x_{1}>0))\cdot \Phi_{\mathrm{inverse}}(q)
```

### 575 proximal-cui-2024-linear-v1 0

```math
\begin{aligned}
X_1,X_2&\overset{\mathrm{iid}}{\sim}\mathcal{N}(0.25,0.25^2)\\
p(X)&=[1+\exp\{0.125(X_1+X_2)\}]^{-1}\\
A\mid X&\sim\mathrm{Bernoulli}(p(X))
\end{aligned}
```

### 576 proximal-cui-2024-linear-v1 1

```math
\begin{aligned}
(Z,W,U)\mid A,X&\sim\mathcal{N}_{3}(m,\Sigma)\\
m&=(0.25+0.25A+0.25s,\ 0.25+0.125A+0.25s,\ 0.25+0.25A+0.25s)\\
s&=X_1+X_2
\end{aligned}
```

### 577 proximal-cui-2024-linear-v1 2

```math
\begin{aligned}
\Sigma&=\begin{bmatrix}
1 & 0.25 & 0.5\\
0.25 & 1 & 0.5\\
0.5 & 0.5 & 1
\end{bmatrix}\\
m_W(U,X)&=0.125+0.125s+0.5U
\end{aligned}
```

### 578 proximal-cui-2024-linear-v1 3

```math
\begin{aligned}
Y&=2+2A+0.25s+4m_W+2(W-m_W)+\varepsilon\\
\varepsilon&\sim\mathcal{N}(0,0.25^2)
\end{aligned}
```

### 579 proximal-cui-2024-linear-v1 4

```math
h(W,A,X)=2+2A+4W+0.25s
```

### 580 proximal-dukes-2023-mediation-v1 0

```math
\begin{aligned}
(X_1,X_2,U)&\sim\mathcal{N}_{3}((0.25,0.25,0),\Sigma)\\
\Sigma&=\begin{bmatrix}
0.25 & 0 & 0.05\\
0 & 0.25 & 0.05\\
0.05 & 0.05 & 1
\end{bmatrix}
\end{aligned}
```

### 581 proximal-dukes-2023-mediation-v1 1

```math
A\mid X,U\sim\mathrm{Bernoulli}(\mathrm{expit}[-0.5(X_1+X_2)-0.4U])
```

### 582 proximal-dukes-2023-mediation-v1 2

```math
\begin{aligned}
Z&=0.2-0.52A+0.2(X_1+X_2)-U+\varepsilon_{z}\\
W&=0.3+0.2(X_1+X_2)-0.6U+\varepsilon_{w}
\end{aligned}
```

### 583 proximal-dukes-2023-mediation-v1 3

```math
\begin{aligned}
M&=-0.3A-0.5(X_1+X_2)+0.4U+\varepsilon_{m}\\
Y&=2+2A+M+2W-X_1-X_2-U+2\varepsilon_{y}
\end{aligned}
```

### 584 proximal-dukes-2023-mediation-v1 4

```math
\varepsilon_{z},\varepsilon_{w},\varepsilon_{m},\varepsilon_{y}\overset{\mathrm{ind}}{\sim}\mathcal{N}(0,1)
```

### 585 proximal-imbens-2025-longterm-v1 0

```math
\begin{aligned}
G=1&:\ \text{observational sample},\qquad G=0:\ \text{experimental sample}\\
\widetilde X,U&\overset{\mathrm{ind}}{\sim}\mathcal{N}_{5}(0,0.5I)
\end{aligned}
```

### 586 proximal-imbens-2025-longterm-v1 1

```math
\begin{aligned}
P(A=1\mid\widetilde X,U,G=1)&=[1+\exp(\kappa_x^\top\widetilde X+\kappa_u^\top U)]^{-1}\\
P(A=1\mid G=0)&=\tfrac12
\end{aligned}
```

### 587 proximal-imbens-2025-longterm-v1 2

```math
\begin{aligned}
\widetilde S_1&=\tau_1A+\beta_1\widetilde X+\gamma_1U+\varepsilon_1\\
\widetilde S_2&=\tau_2A+\alpha_2\widetilde S_1+\beta_2\widetilde X+\gamma_2U+\varepsilon_2
\end{aligned}
```

### 588 proximal-imbens-2025-longterm-v1 3

```math
\begin{aligned}
\widetilde S_3&=\tau_3A+\alpha_3\widetilde S_2+\beta_3\widetilde X+\gamma_3U+\varepsilon_3\\
Y&=\tau_yA+\alpha_y^\top\widetilde S_3+\beta_y^\top\widetilde X+\gamma_y^\top U+\varepsilon_{y}
\end{aligned}
```

### 589 proximal-imbens-2025-longterm-v1 4

```math
g(v)=\mathrm{sign}(v)|v|^2
```

### 590 proximal-imbens-2025-longterm-v1 5

```math
\tau_2=\tau_y=0.5
```

### 591 proximal-qi-2024-linear-itr-v1 0

```math
\begin{aligned}
X_1,X_2&\overset{\mathrm{iid}}{\sim}\mathcal{N}(0.25,0.25^2)\\
p(X)&=[1+\exp\{0.125(X_1+X_2)\}]^{-1}\\
A\mid X&\sim\mathrm{Bernoulli}(p(X))
\end{aligned}
```

### 592 proximal-qi-2024-linear-itr-v1 1

```math
\begin{aligned}
(Z,W,U)\mid A,X&\sim\mathcal{N}_{3}(m,\Sigma)\\
m&=(0.25+0.25A+0.25s,\ 0.25+0.125A+0.25s,\ 0.25+0.25A+0.25s)\\
s&=X_1+X_2
\end{aligned}
```

### 593 proximal-qi-2024-linear-itr-v1 2

```math
\begin{aligned}
\Sigma&=\begin{bmatrix}
1 & 0.25 & 0.5\\
0.25 & 1 & 0.5\\
0.5 & 0.5 & 1
\end{bmatrix}\\
m_W(U,X)&=0.125+0.125s+0.5U
\end{aligned}
```

### 594 proximal-qi-2024-linear-itr-v1 3

```math
\begin{aligned}
Y&=2+0.25s+8m_W+2(W-m_W)\\
&\quad+A(0.5+3X_1-5X_2+c_4m_W)+\varepsilon\\
\varepsilon&\sim\mathrm{Uniform}(-1,1)
\end{aligned}
```

### 595 proximal-qi-2024-linear-itr-v1 4

```math
\mathrm{L1}:\ c_4=0.25,\qquad\mathrm{L2}:\ c_4=0
```

### 596 proximal-qi-2024-quadratic-v1 0

```math
\begin{aligned}
X_1,X_2&\overset{\mathrm{iid}}{\sim}\mathcal{N}(0.25,0.25^2)\\
p(X)&=[1+\exp\{0.125(X_1+X_2)\}]^{-1}\\
A\mid X&\sim\mathrm{Bernoulli}(p(X))
\end{aligned}
```

### 597 proximal-qi-2024-quadratic-v1 1

```math
\begin{aligned}
(Z,W,U)\mid A,X&\sim\mathcal{N}_{3}(m,\Sigma)\\
m&=(0.25+0.25A+0.25s,\ 0.25+0.125A+0.25s,\ 0.25+0.25A+0.25s)\\
s&=X_1+X_2
\end{aligned}
```

### 598 proximal-qi-2024-quadratic-v1 2

```math
\begin{aligned}
\Sigma&=\begin{bmatrix}
1 & 0.25 & 0.5\\
0.25 & 1 & 0.5\\
0.5 & 0.5 & 1
\end{bmatrix}\\
m_W(U,X)&=0.125+0.125s+0.5U
\end{aligned}
```

### 599 proximal-qi-2024-quadratic-v1 3

```math
\begin{aligned}
Y&=2+X_1^2+X_2^2+5m_W+2(W-m_W)\\
&\quad +A(0.25-6X_1X_2)+\varepsilon\\
\varepsilon&\sim\mathrm{Uniform}(-1,1)
\end{aligned}
```

### 600 proximal-qi-2024-trigonometric-v1 0

```math
\begin{aligned}
X_1,X_2&\overset{\mathrm{iid}}{\sim}\mathcal{N}(0.25,0.25^2)\\
p(X)&=[1+\exp\{0.125(X_1+X_2)\}]^{-1}\\
A\mid X&\sim\mathrm{Bernoulli}(p(X))
\end{aligned}
```

### 601 proximal-qi-2024-trigonometric-v1 1

```math
\begin{aligned}
(Z,W,U)\mid A,X&\sim\mathcal{N}_{3}(m,\Sigma)\\
m&=(0.25+0.25A+0.25s,\ 0.25+0.125A+0.25s,\ 0.25+0.25A+0.25s)\\
s&=X_1+X_2
\end{aligned}
```

### 602 proximal-qi-2024-trigonometric-v1 2

```math
\begin{aligned}
\Sigma&=\begin{bmatrix}
1 & 0.25 & 0.5\\
0.25 & 1 & 0.5\\
0.5 & 0.5 & 1
\end{bmatrix}\\
m_W(U,X)&=0.125+0.125s+0.5U
\end{aligned}
```

### 603 proximal-qi-2024-trigonometric-v1 3

```math
\begin{aligned}
g(X)&=-2.5+\sin(X_1)-2\cos(X_2)\\
d(U,X)&=2.3+|X_1-1|-|X_2+1|+g(X)m_W
\end{aligned}
```

### 604 proximal-qi-2024-trigonometric-v1 4

```math
\begin{aligned}
Y&=2+X_1^2+X_2^2+4m_W+2(W-m_W)\\
&\quad+A\,d(U,X)+\varepsilon\\
\varepsilon&\sim\mathrm{Uniform}(-1,1)
\end{aligned}
```

### 605 proximal-shi-2026-sc-gaussian-v1 0

```math
\begin{aligned}
t&=1,\ldots,T\\
A_t&=\mathbf1\{t>T_0\},\quad T_0=\lfloor T/2\rfloor\\
\lambda_{tk}&\overset{\mathrm{ind}}{\sim}\mathcal{N}(0.5,0.5^2),\quad k=1,\ldots,5
\end{aligned}
```

### 606 proximal-shi-2026-sc-gaussian-v1 1

```math
\begin{aligned}
\mu_0&=(1,1,1,1,1)\\
D&=\mathrm{diag}(3,6,6,6,6)\\
Y_t&=2A_t+\sum_{k=1}^5\lambda_{tk}+\varepsilon_{0t}
\end{aligned}
```

### 607 proximal-shi-2026-sc-gaussian-v1 2

```math
\begin{aligned}
W_t&=D\lambda_t+\varepsilon_{Wt}\\
Z_t&=D\lambda_t+\varepsilon_{Zt}
\end{aligned}
```

### 608 proximal-shi-2026-sc-gaussian-v1 3

```math
\begin{aligned}
h(W)&=W_1/3+(W_2+W_3+W_4+W_5)/6\\
\alpha^\top D&=\mu_0^\top,\qquad\sum_j\alpha_j=1
\end{aligned}
```

### 609 proximal-shi-2026-sc-poisson-v1 0

```math
\begin{aligned}
\lambda_t&\overset{\mathrm{ind}}{\sim}\mathcal{N}(0.5,0.1^2)\ \text{truncated to }(0,1)\\
A_t&=\mathbf1\{t>T_0\},\quad T_0=\lfloor T/2\rfloor
\end{aligned}
```

### 610 proximal-shi-2026-sc-poisson-v1 1

```math
\begin{aligned}
Y_t\mid\lambda_t&\sim\mathrm{Poisson}(\exp\{\lambda_t+\beta A_t\})\\
W_t,Z_t\mid\lambda_t&\overset{\mathrm{cond.ind.}}{\sim}\mathrm{Poisson}(\lambda_t/(e-1))\\
\beta&=-2
\end{aligned}
```

### 611 proximal-shi-2026-sc-poisson-v1 2

```math
\begin{aligned}
r&=1\\
h(W)&=\exp(W),\qquad E[\exp(W)\mid\lambda]=\exp(\lambda)
\end{aligned}
```

### 612 proximal-su-2026-transport-v1 0

```math
\begin{aligned}
V&\sim\mathcal{N}_{3}(0,\Sigma_X)\\
\Sigma_X&=\begin{bmatrix}
1 & 0.25 & 0.25\\
0.25 & 1 & 0.25\\
0.25 & 0.25 & 1
\end{bmatrix}\\
X_j&=\Phi(V_j)
\\
U_j&\overset{\mathrm{iid}}{\sim}\mathrm{Uniform}(-1,0)
\end{aligned}
```

### 613 proximal-su-2026-transport-v1 1

```math
S\mid X,U\sim\mathrm{Bernoulli}(\mathrm{expit}\{-0.625+0.5\sum_jX_j+0.5\sum_jU_j\})
```

### 614 proximal-su-2026-transport-v1 2

```math
\begin{aligned}
A\mid S=1&\sim\mathrm{Bernoulli}(0.5)\\
Z\mid X,U,S=1&\sim\mathcal{N}_{3}(U+X,0.25I)\\
W\mid X,U&\sim\mathcal{N}_{3}(U+X,0.25I)
\end{aligned}
```

### 615 proximal-su-2026-transport-v1 3

```math
\begin{aligned}
Y\mid S=1&=0.5-A+\sum_j U_j+A\sum_j U_j+\sum_jX_j\\
&\quad+\sum_jW_j+A\sum_jW_j+\varepsilon\\
\varepsilon&\sim\mathcal{N}(0,0.5^2)
\end{aligned}
```

### 616 proximal-su-2026-transport-v1 4

```math
\mathrm{observed}\{X,W,S,SA,SZ,SY\}
```

### 617 proximal-ying-2023-longitudinal-v1 0

```math
\begin{aligned}
X_0&\sim\mathcal{N}(-0.35,0.5^2)\\
U_0&\sim\mathcal{N}(0.35,0.5^2)\\
p_0&=[1+\exp(0.5-0.35X_0+0.35U_0)]^{-1}
\end{aligned}
```

### 618 proximal-ying-2023-longitudinal-v1 1

```math
\begin{aligned}
A_0&\sim\mathrm{Bernoulli}(p_0)\\
Z_0&=0.2+0.5A_0+0.5X_0+0.75U_0+\varepsilon_{z0}\\
W_0&=0.2+0.5X_0-0.95U_0+\varepsilon_{w0}
\end{aligned}
```

### 619 proximal-ying-2023-longitudinal-v1 2

```math
\begin{aligned}
X_1&=0.2+0.7A_0+0.7X_0+\varepsilon_{x1}\\
U_1&=0.2+0.7A_0+0.7U_0+\varepsilon_{u1}
\end{aligned}
```

### 620 proximal-ying-2023-longitudinal-v1 3

```math
\begin{aligned}
p_1&=[1+\exp\{0.5-0.5A_0-0.35(X_0+X_1)-0.35(U_0+U_1)\}]^{-1}\\
A_1&\sim\mathrm{Bernoulli}(p_1)
\end{aligned}
```

### 621 proximal-ying-2023-longitudinal-v1 4

```math
Z_1=0.2+0.5(A_0+A_1)+0.5(X_0+X_1)-0.75(U_0+U_1)+\varepsilon_{z1}
```

### 622 proximal-ying-2023-longitudinal-v1 5

```math
W_1=0.35+0.45(X_0+X_1)-0.85(U_0+U_1)+\varepsilon_{w1}
```

### 623 proximal-ying-2023-longitudinal-v1 6

```math
Y=-1.3+A_1+1.14A_0+0.5X_1-0.7U_1+0.2X_0-0.7U_0+\varepsilon_{y}
```

### 624 did-abadie-lhour-2021-nonlinear-null-v1 0

```math
n_{1}=\min(n-1,\max(1,\lfloor n/5+0.5\rfloor))
```

### 625 did-abadie-lhour-2021-nonlinear-null-v1 1

```math
n_{0}=n-n_{1}
```

### 626 did-abadie-lhour-2021-nonlinear-null-v1 2

```math
\mathrm{baseline} n=500 \mathrm{gives} n_{1}=100,n_{0}=400
```

### 627 did-abadie-lhour-2021-nonlinear-null-v1 3

```math
p=4,r=2,\text{ a }=0.1,b=0.9,h=0.1
```

### 628 did-abadie-lhour-2021-nonlinear-null-v1 4

```math
X_{ij}\mid G_{i}=1\overset{\mathrm{iid}}{\sim} \mathrm{Uniform}(\text{ a },b)
```

### 629 did-abadie-lhour-2021-nonlinear-null-v1 5

```math
X_{ij}\mid G_{i}=0=\sqrt{U_{ij}}, U_{ij}\overset{\mathrm{iid}}{\sim} \mathrm{Uniform}(0,1)
```

### 630 did-abadie-lhour-2021-nonlinear-null-v1 6

```math
v=\sqrt{p\cdot \mathrm{Var}(X^{r}\mid G=1)}
```

### 631 did-abadie-lhour-2021-nonlinear-null-v1 7

```math
\mathbb{E}[X^{k}\mid G=1]=(b^{k+1}-\text{ a }^{k+1})/((k+1)\cdot (b-\text{ a }))
```

### 632 did-abadie-lhour-2021-nonlinear-null-v1 8

```math
v^{2}=6256/28125
```

### 633 did-abadie-lhour-2021-nonlinear-null-v1 9

```math
\mu_{i}=\sum_{j=1}^{4} X_{ij}^{2}/v.
```

### 634 did-abadie-lhour-2021-nonlinear-null-v1 10

```math
\text{ all } \mathrm{period}/\mathrm{unit} \mathrm{errors}\overset{\mathrm{iid}}{\sim} \mathcal{N}(0,1)
```

### 635 did-abadie-lhour-2021-nonlinear-null-v1 11

```math
\mathrm{The} \mathrm{same} X \text{ is } \mathrm{shared} \text{ across } \mathrm{periods}. A_{\mathrm{pre}}=0,A_{\mathrm{post}}=G
```

### 636 did-abadie-lhour-2021-nonlinear-null-v1 12

```math
\mathrm{treatment}_{\mathrm{effect}}=0.
```

### 637 did-abadie-lhour-2021-nonlinear-null-v1 13

```math
\mathrm{ATT}_{\mathrm{post}}=\mathbb{E}[Y_{2}(1)-Y_{2}(0)\mid G=1]=0
```

### 638 did-cwz-2021-donor-ar-null-v1 0

```math
t=1,\ldots ,21
```

### 639 did-cwz-2021-donor-ar-null-v1 1

```math
F_{1t},F_{2t}\overset{\mathrm{iid}}{\sim} \mathcal{N}(0,1)
```

### 640 did-cwz-2021-donor-ar-null-v1 2

```math
\varepsilon_{\mathrm{dt}}=0.6\cdot \varepsilon_{d,t-1}+\eta_{\mathrm{dt}}
```

### 641 did-cwz-2021-donor-ar-null-v1 3

```math
u_{t}=0.6\cdot u_{t}-1+\xi_{t}
```

### 642 did-cwz-2021-donor-ar-null-v1 4

```math
\eta_{\mathrm{dt}},\xi_{t}\overset{\mathrm{iid}}{\sim} \mathcal{N}(0,0.64)
```

### 643 did-cwz-2021-donor-ar-null-v1 5

```math
J=20
```

### 644 did-cwz-2021-donor-ar-null-v1 6

```math
\mathrm{reindex} \mathrm{donors} d=1,\ldots ,20 (\text{ source } j=d+1)
```

### 645 did-cwz-2021-donor-ar-null-v1 7

```math
\text{ a }_{d}=b_{d}=d/20. Y_{\mathrm{dt}}=\text{ a }_{d}+F_{1t}+b_{d}\cdot F_{2t}+\varepsilon_{\mathrm{dt}}.
```

### 646 did-cwz-2021-donor-ar-null-v1 8

```math
W_{1}: w_{d}=1/20 (\mathrm{default})
```

### 647 did-cwz-2021-donor-ar-null-v1 9

```math
W_{2}: w_{1}=w_{2}=w_{3}=1/3, \mathrm{others0}
```

### 648 did-cwz-2021-donor-ar-null-v1 10

```math
W_{3}: w_{d}=-1/20
```

### 649 did-cwz-2021-donor-ar-null-v1 11

```math
W_{4}: w_{1}=1,w_{2}=-1,\mathrm{others0}
```

### 650 did-cwz-2021-donor-ar-null-v1 12

```math
Y_{0t}=Y_{0t}(0)+1\{t=21\}\cdot \theta_{T}, \theta_{T}=0. G_{0}=1,\mathrm{donors} G=0
```

### 651 did-cwz-2021-donor-ar-null-v1 13

```math
n=21 \text{ only }.
```

### 652 did-cwz-2021-donor-ar-null-v1 14

```math
Y_{0},21(1)-Y_{0},21(0)=\theta_{T}=0 \text{ for } \mathrm{every} \mathrm{realization}
```

### 653 did-ferman-2021-two-factor-null-v1 0

```math
k=1,2
```

### 654 did-ferman-2021-two-factor-null-v1 1

```math
F_{k0}\overset{\mathrm{iid}}{\sim} \mathcal{N}(0,1)
```

### 655 did-ferman-2021-two-factor-null-v1 2

```math
F_{ks}=0.5\cdot F_{k},s-1+\eta_{ks} \text{ for } s=1,\ldots ,21, \eta_{ks}\overset{\mathrm{iid}}{\sim} \mathcal{N}(0,0.75)
```

### 656 did-ferman-2021-two-factor-null-v1 3

```math
\mathrm{Omit} \text{ only } s=0
```

### 657 did-ferman-2021-two-factor-null-v1 4

```math
\mathrm{N}=11,J=10
```

### 658 did-ferman-2021-two-factor-null-v1 5

```math
\mu_{0}=\mu_{1}=\ldots =\mu_{5}=(1,0)
```

### 659 did-ferman-2021-two-factor-null-v1 6

```math
\mu_{6}=\ldots =\mu_{10}=(0,1)
```

### 660 did-ferman-2021-two-factor-null-v1 7

```math
\varepsilon_{is}\overset{\mathrm{iid}}{\sim} \mathcal{N}(0,1)
```

### 661 did-ferman-2021-two-factor-null-v1 8

```math
Y_{is}=\mu_{i}^{T} F_{s}+\varepsilon_{is}+1\{i=0,s=21\}\cdot \mathrm{post}_{\mathrm{effect}}
```

### 662 did-ferman-2021-two-factor-null-v1 9

```math
\mathrm{post}_{\mathrm{effect}}=0. G_{0}=1,G_{1}:10=0
```

### 663 did-ferman-2021-two-factor-null-v1 10

```math
s=1,\ldots ,20 \mathrm{pre} \text{ and } s=21 \mathrm{post}. n \mathrm{must} \mathrm{equal11}.
```

### 664 did-ferman-2021-two-factor-null-v1 11

```math
\tau_{01}=Y_{0},21(1)-Y_{0},21(0)=\mathrm{post}_{\mathrm{effect}}=0 \text{ with } \mathrm{common} \mathrm{exogenous} \mathrm{draws} \mathrm{held} \text{ fixed }
```

### 665 did-karmakar-2025-code-truncated-cluster-null-v1 0

```math
Z_{it}=\text{ a }_{i}+\lfloor (t-1)/4\rfloor+2\cdot ((t-1)\mathrm{mod4})+\varepsilon_{it}-80q_{\mathrm{ct}}
```

### 666 did-karmakar-2025-code-truncated-cluster-null-v1 1

```math
\text{ a }_{i} \mathrm{iidU}(10,60),\varepsilon\overset{\mathrm{iid}}{\sim} \mathcal{N}(0,25)
```

### 667 did-karmakar-2025-code-truncated-cluster-null-v1 2

```math
Y_{it}=\max(Z_{it},0),t_{1}..55
```

### 668 did-karmakar-2025-code-truncated-cluster-null-v1 3

```math
p_{i}=(1+\text{ mean }(Y_{i},20:45))/\sum_{\mathrm{group}}(1+\text{ mean }(Y_{j},20:45))
```

### 669 did-karmakar-2025-code-truncated-cluster-null-v1 4

```math
\mathrm{Eff}=(0,0,0)
```

### 670 did-karmakar-2025-code-truncated-cluster-null-v1 5

```math
\mathrm{ATT}=SATT=0
```

### 671 did-shaikh-toulis-2021-conditional-first-adopter-null-v1 0

```math
X\sim U[-10,10]
```

### 672 did-shaikh-toulis-2021-conditional-first-adopter-null-v1 1

```math
\mathrm{Ti}\mid \Xi\sim \mathrm{Exp}(\exp(1+.5\Xi))
```

### 673 did-shaikh-toulis-2021-conditional-first-adopter-null-v1 2

```math
H=\mathrm{max10000} \mathrm{sample15}\%\mathrm{quantiles}
```

### 674 did-shaikh-toulis-2021-conditional-first-adopter-null-v1 3

```math
\mathrm{condition} \mathrm{minTi}<H
```

### 675 did-shaikh-toulis-2021-conditional-first-adopter-null-v1 4

```math
\mathrm{Yij}=.2 \mathrm{Yi},j-1+.5\Xi+.5\sqrt{j}+\mathrm{epsij}
```

### 676 did-shaikh-toulis-2021-conditional-first-adopter-null-v1 5

```math
\mathrm{Yi0}=0
```

### 677 did-shaikh-toulis-2021-conditional-first-adopter-null-v1 6

```math
\varepsilon\sim \mathcal{N}(0,.15^{2})
```

### 678 did-shi-2026-poisson-proxy-logrr-v1 0

```math
\lambda_{t} \text{ iid } TN(0.5,0.1^{2};(0,1))
```

### 679 did-shi-2026-poisson-proxy-logrr-v1 1

```math
t=1,\ldots ,200
```

### 680 did-shi-2026-poisson-proxy-logrr-v1 2

```math
Y_{t}\mid \lambda_{t} \sim \mathrm{Pois}(\exp(\lambda_{t}-2\cdot 1(t>100)))
```

### 681 did-shi-2026-poisson-proxy-logrr-v1 3

```math
W_{1t},W_{2t}\mid \lambda_{t} \sim \mathrm{Pois}(\lambda_{t}/(e-1))
```

### 682 did-shi-2026-poisson-proxy-logrr-v1 4

```math
\log(\mathbb{E}[Y_{t}(1)]/\mathbb{E}[Y_{t}(0)])=-2
```

### 683 did-ye-2024-bracketing-v1 0

```math
(p_a,p_b,p_{trt})=(0.2,0.5,0.3),\quad \sum_g n_g=n
```

### 684 did-ye-2024-bracketing-v1 1

```math
n_g=\lfloor np_g\rfloor+r_g,\quad r_g\in\{0,1\},\quad \sum_g r_g=n-\sum_g\lfloor np_g\rfloor
```

### 685 did-ye-2024-bracketing-v1 2

```math
\mu_a^{I}=(10,11,9,8)
```

### 686 did-ye-2024-bracketing-v1 3

```math
\mu_b^{I}=(4,5,3,2)
```

### 687 did-ye-2024-bracketing-v1 4

```math
\mu_{trt}^{I}=(3,4,2,1)
```

### 688 did-ye-2024-bracketing-v1 5

```math
\mu_a^{II}=(10,11,10,11)
```

### 689 did-ye-2024-bracketing-v1 6

```math
\mu_b^{II}=(4,6,2,3)
```

### 690 did-ye-2024-bracketing-v1 7

```math
\mu_{trt}^{II}=(3,4,0,1)
```

### 691 did-ye-2024-bracketing-v1 8

```math
(\theta_1,\theta_2,\theta_3,\theta_4)=(0,2,3,1)
```

### 692 did-ye-2024-bracketing-v1 9

```math
\epsilon_{it}\sim N(0,1),\quad i=1,\ldots,n,\quad t=1,2,3,4
```

### 693 did-ye-2024-bracketing-v1 10

```math
Y_{it}=\mu_{G_i,t}+\mathbf{1}\{G_i=trt\}\theta_t+\epsilon_{it}
```

### 694 did-ye-2024-bracketing-v1 11

```math
ATT_4=E[Y_{i4}(1)-Y_{i4}(0)\mid G_i=trt]=\theta_4=1
```

### 695 did-ye-2024-code-case2-gaussian-bracketing-v1 0

```math
Y_{\mathrm{gtj}}\sim \mathcal{N}(\mu_{\mathrm{gt}}+I(g=\mathrm{trt})\mathrm{att}_{t},1), \text{ independent } \text{ all } \mathrm{cells}
```

### 696 did-ye-2024-code-case2-gaussian-bracketing-v1 1

```math
\mu_{trt}=(3,4,0,1)
```

### 697 did-ye-2024-code-case2-gaussian-bracketing-v1 2

```math
\mu_{a}=(10,11,10,11)
```

### 698 did-ye-2024-code-case2-gaussian-bracketing-v1 3

```math
\mu_{b}=(4,6,2,3)
```

### 699 did-ye-2024-code-case2-gaussian-bracketing-v1 4

```math
\mathrm{att}=(0,2,3,1)
```
