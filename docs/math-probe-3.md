# Math probe batch 3

### 350 ate-huang-chan-2017-05-19-setting-2-v1 9

```math
Y=A\cdot Y(1)+(1-A)\cdot Y(0).
```

### 351 ate-ma-zhu-zhang-tsai-carroll-2019-06-01-model-1-v1 0

```math
X\sim \mathcal{N}_{20}(0,\Sigma), \Sigma[j,k]=0.5^{\lvert j-k\rvert}
```

### 352 ate-ma-zhu-zhang-tsai-carroll-2019-06-01-model-1-v1 1

```math
p(X)=\mathrm{expit}((X_{1}+X_{2})\cdot (X_{3}+1)/2)
```

### 353 ate-ma-zhu-zhang-tsai-carroll-2019-06-01-model-1-v1 2

```math
A\mid X\sim \mathrm{Bernoulli}(p).
```

### 354 ate-ma-zhu-zhang-tsai-carroll-2019-06-01-model-1-v1 3

```math
Y=A+X_{1}^{2}+X_{2}^{2}+\varepsilon
```

### 355 ate-ma-zhu-zhang-tsai-carroll-2019-06-01-model-1-v1 4

```math
\varepsilon\sim \mathcal{N}(0,1)
```

### 356 ate-ma-zhu-zhang-tsai-carroll-2019-06-01-model-2-v1 0

```math
X\sim \mathcal{N}_{20}(0,\Sigma), \Sigma[j,k]=0.5^{\lvert j-k\rvert}
```

### 357 ate-ma-zhu-zhang-tsai-carroll-2019-06-01-model-2-v1 1

```math
p(X)=\mathrm{expit}((X_{1}+X_{2}+X_{3})/2)
```

### 358 ate-ma-zhu-zhang-tsai-carroll-2019-06-01-model-2-v1 2

```math
A\mid X\sim \mathrm{Bernoulli}(p).
```

### 359 ate-ma-zhu-zhang-tsai-carroll-2019-06-01-model-2-v1 3

```math
Y=A+(X_{1}+2)\cdot (X_{2}+X_{3}+2)+\varepsilon
```

### 360 ate-ma-zhu-zhang-tsai-carroll-2019-06-01-model-2-v1 4

```math
\varepsilon\sim \mathcal{N}(0,1)
```

### 361 ate-nie-wager-2020-09-24-eq9-discontinuous-v1 0

```math
X\sim \mathcal{N}_{10}(0,I)
```

### 362 ate-nie-wager-2020-09-24-eq9-discontinuous-v1 1

```math
A\sim \mathrm{Bernoulli}(0.5)
```

### 363 ate-nie-wager-2020-09-24-eq9-discontinuous-v1 2

```math
b(X)=3/(1+\exp(X_{3}-X_{2}))
```

### 364 ate-nie-wager-2020-09-24-eq9-discontinuous-v1 3

```math
\tau(X)=1\{X_{1}>0\}/(1+\exp(-X_{2})).
```

### 365 ate-nie-wager-2020-09-24-eq9-discontinuous-v1 4

```math
Y\mid X,A\sim \mathcal{N}(b(X)+(A-0.5)\cdot \tau(X),\sigma^{2})
```

### 366 ate-nie-wager-2020-09-24-eq9-discontinuous-v1 5

```math
\sigma=1, \mathrm{selected} \text{ from } \mathrm{Figure} 2 \text{ noise } \mathrm{levels}.
```

### 367 ate-nie-wager-2020-09-24-eq9-smooth-v1 0

```math
X\sim \mathcal{N}_{10}(0,I)
```

### 368 ate-nie-wager-2020-09-24-eq9-smooth-v1 1

```math
A\sim \mathrm{Bernoulli}(0.5)
```

### 369 ate-nie-wager-2020-09-24-eq9-smooth-v1 2

```math
b(X)=3/(1+\exp(X_{3}-X_{2}))
```

### 370 ate-nie-wager-2020-09-24-eq9-smooth-v1 3

```math
\tau(X)=1/(1+\exp(X_{1}-X_{2})).
```

### 371 ate-nie-wager-2020-09-24-eq9-smooth-v1 4

```math
Y\mid X,A\sim \mathcal{N}(b(X)+(A-0.5)\cdot \tau(X),\sigma^{2})
```

### 372 ate-nie-wager-2020-09-24-eq9-smooth-v1 5

```math
\sigma=1, \mathrm{selected} \text{ from } \mathrm{Figure} 2 \text{ noise } \mathrm{levels}.
```

### 373 ate-nie-wager-2020-09-24-setup-b-v1 0

```math
X\sim \mathcal{N}_{d}(0,I)
```

### 374 ate-nie-wager-2020-09-24-setup-b-v1 1

```math
p(X)=0.5
```

### 375 ate-nie-wager-2020-09-24-setup-b-v1 2

```math
A\sim \mathrm{Bernoulli}(0.5)
```

### 376 ate-nie-wager-2020-09-24-setup-b-v1 3

```math
b(X)=\max(X_{1}+X_{2},X_{3},0)+\max(X_{4}+X_{5},0).
```

### 377 ate-nie-wager-2020-09-24-setup-b-v1 4

```math
\tau(X)=X_{1}+\log(1+\exp(X_{2}))
```

### 378 ate-nie-wager-2020-09-24-setup-b-v1 5

```math
Y=b(X)+(A-0.5)\cdot \tau(X)+\varepsilon
```

### 379 ate-nie-wager-2020-09-24-setup-b-v1 6

```math
\varepsilon\sim \mathcal{N}(0,1).
```

### 380 ate-nie-wager-2020-09-24-setup-c-v1 0

```math
X\sim \mathcal{N}_{d}(0,I)
```

### 381 ate-nie-wager-2020-09-24-setup-c-v1 1

```math
p(X)=1/(1+\exp(X_{2}+X_{3}))
```

### 382 ate-nie-wager-2020-09-24-setup-c-v1 2

```math
A\mid X\sim \mathrm{Bernoulli}(p).
```

### 383 ate-nie-wager-2020-09-24-setup-c-v1 3

```math
b(X)=2\cdot \log(1+\exp(X_{1}+X_{2}+X_{3}))
```

### 384 ate-nie-wager-2020-09-24-setup-c-v1 4

```math
\tau(X)=1.
```

### 385 ate-nie-wager-2020-09-24-setup-c-v1 5

```math
Y=b(X)+(A-0.5)\cdot \tau(X)+\varepsilon
```

### 386 ate-nie-wager-2020-09-24-setup-c-v1 6

```math
\varepsilon\sim \mathcal{N}(0,1).
```

### 387 ate-nie-wager-2020-09-24-setup-d-v1 0

```math
X\sim \mathcal{N}_{d}(0,I)
```

### 388 ate-nie-wager-2020-09-24-setup-d-v1 1

```math
p(X)=1/(1+\exp(-X_{1})+\exp(-X_{2}))
```

### 389 ate-nie-wager-2020-09-24-setup-d-v1 2

```math
A\mid X\sim \mathrm{Bernoulli}(p).
```

### 390 ate-nie-wager-2020-09-24-setup-d-v1 3

```math
u=\max(X_{1}+X_{2}+X_{3},0)
```

### 391 ate-nie-wager-2020-09-24-setup-d-v1 4

```math
v=\max(X_{4}+X_{5},0)
```

### 392 ate-nie-wager-2020-09-24-setup-d-v1 5

```math
b=(u+v)/2
```

### 393 ate-nie-wager-2020-09-24-setup-d-v1 6

```math
\tau=u-v.
```

### 394 ate-nie-wager-2020-09-24-setup-d-v1 7

```math
Y=b(X)+(A-0.5)\cdot \tau(X)+\varepsilon, \varepsilon\sim \mathcal{N}(0,1)
```

### 395 ate-nie-wager-2020-09-24-setup-d-v1 8

```math
\mathrm{equivalently} \mathbb{E}[Y|X,A=1]=u \text{ and } \mathbb{E}[Y|X,A=0]=v.
```

### 396 ate-nie-wager-2021-a-v1 0

```math
X_{j}\overset{\mathrm{iid}}{\sim} \mathrm{Uniform}(0,1), j=1,\ldots ,6
```

### 397 ate-nie-wager-2021-a-v1 1

```math
b(X)=\sin(\pi\cdot X_{1}\cdot X_{2})+2\cdot (X_{3}-0.5)^{2}+X_{4}+0.5\cdot X_{5}
```

### 398 ate-nie-wager-2021-a-v1 2

```math
e(X)=\max(0.1,\min(\sin(\pi\cdot X_{1}\cdot X_{2}),0.9))
```

### 399 ate-nie-wager-2021-a-v1 3

```math
A\mid X\sim \mathrm{Bernoulli}(e(X))
```

### 400 ate-nie-wager-2021-a-v1 4

```math
\tau(X)=(X_{1}+X_{2})/2
```

### 401 ate-nie-wager-2021-a-v1 5

```math
Y=b(X)+(A-0.5)\cdot \tau(X)+\varepsilon
```

### 402 ate-nie-wager-2021-a-v1 6

```math
\varepsilon\sim \mathcal{N}(0,1)
```

### 403 ate-ning-peng-imai-2020-06-03-ar1-linear-v1 0

```math
X \sim \mathcal{N}_{d}(0,\Sigma), \Sigma[j,k]=\rho^{\lvert j-k\rvert}
```

### 404 ate-ning-peng-imai-2020-06-03-ar1-linear-v1 1

```math
\rho=0.5.
```

### 405 ate-ning-peng-imai-2020-06-03-ar1-linear-v1 2

```math
s=-X_{1}+X_{2}/2-X_{3}/4-X_{4}/10-X_{5}/10+X_{6}/10
```

### 406 ate-ning-peng-imai-2020-06-03-ar1-linear-v1 3

```math
p=1-1/(1+\exp(s))=\mathrm{expit}(s)
```

### 407 ate-ning-peng-imai-2020-06-03-ar1-linear-v1 4

```math
A\mid X\sim \mathrm{Bernoulli}(p).
```

### 408 ate-ning-peng-imai-2020-06-03-ar1-linear-v1 5

```math
Y(1)=2+0.137\cdot (X_{5}+X_{6}+X_{7}+X_{8})+\varepsilon_{1}
```

### 409 ate-ning-peng-imai-2020-06-03-ar1-linear-v1 6

```math
Y(0)=1+0.291\cdot (X_{5}+X_{6}+X_{7}+X_{8}+X_{9}+X_{10})+\varepsilon_{0}.
```

### 410 ate-ning-peng-imai-2020-06-03-ar1-linear-v1 7

```math
\varepsilon_{0},\varepsilon_{1}\overset{\mathrm{iid}}{\sim} \mathcal{N}(0,1)
```

### 411 ate-ning-peng-imai-2020-06-03-ar1-linear-v1 8

```math
Y=A\cdot Y(1)+(1-A)\cdot Y(0).
```

### 412 ate-ning-peng-imai-2020-linear-v1 0

```math
X_{i} \sim \mathcal{N}_{d}(0,\Sigma)
```

### 413 ate-ning-peng-imai-2020-linear-v1 1

```math
\Sigma_{jk} = \rho^{\lvert j-k\rvert}, \rho=1/2
```

### 414 ate-ning-peng-imai-2020-linear-v1 2

```math
i=1,\ldots ,n \text{ independently }.
```

### 415 ate-ning-peng-imai-2020-linear-v1 3

```math
A_{i} \mid  X_{i} \sim \mathrm{Bernoulli}(e_{i})
```

### 416 ate-ning-peng-imai-2020-linear-v1 4

```math
e_{i} = 1 - 1/\{1 + \exp(-X_{i1} + X_{i2}/2 - X_{i3}/4 - X_{i4}/10 - X_{i5}/10 + X_{i6}/10)\} = \mathrm{expit}(\eta_{i})
```

### 417 ate-ning-peng-imai-2020-linear-v1 5

```math
\eta_{i}=-X_{i1}+X_{i2}/2-X_{i3}/4-X_{i4}/10-X_{i5}/10+X_{i6}/10.
```

### 418 ate-ning-peng-imai-2020-linear-v1 6

```math
Y_{i}(1)=2+0.137(X_{i5}+X_{i6}+X_{i7}+X_{i8})+\varepsilon_{i1}.
```

### 419 ate-ning-peng-imai-2020-linear-v1 7

```math
Y_{i}(0)=1+0.291(X_{i5}+X_{i6}+X_{i7}+X_{i8}+X_{i9}+X_{i10})+\varepsilon_{i0}.
```

### 420 ate-ning-peng-imai-2020-linear-v1 8

```math
Y_{i}=A_{i} Y_{i}(1)+(1-A_{i})Y_{i}(0)
```

### 421 ate-ning-peng-imai-2020-linear-v1 9

```math
\mathrm{ATE}=\mathbb{E}[Y(1)-Y(0)]=2-1+0.137 \mathbb{E}[X_{5}+X_{6}+X_{7}+X_{8}]-0.291 \mathbb{E}[X_{5}+\ldots +X_{10}]+\mathbb{E}[\varepsilon_{1}-\varepsilon_{0}]=1.
```

### 422 ate-wager-athey-2018-06-06-rare-response-v1 0

```math
X\sim \mathrm{Uniform}([0,1]^{10})
```

### 423 ate-wager-athey-2018-06-06-rare-response-v1 1

```math
A\sim \mathrm{Bernoulli}(0.5)
```

### 424 ate-wager-athey-2018-06-06-rare-response-v1 2

```math
B\sim \mathrm{Bernoulli}(0.05)
```

### 425 ate-wager-athey-2018-06-06-rare-response-v1 3

```math
\varepsilon\sim \mathcal{N}(0,0.1^{2})
```

### 426 ate-wager-athey-2018-06-06-rare-response-v1 4

```math
Y=2\cdot A\cdot B+\varepsilon
```

### 427 ate-yang-wang-ding-2019-mnar-confounder-v1 0

```math
X_{1} \sim \mathcal{N}(\text{ mean }=1, \text{ variance }=1)
```

### 428 ate-yang-wang-ding-2019-mnar-confounder-v1 1

```math
X_{2} \sim \mathrm{Bernoulli}(0.5)
```

### 429 ate-yang-wang-ding-2019-mnar-confounder-v1 2

```math
Y(0) = 0.5 + 2\cdot X_{1} + X_{2} + \varepsilon(0), \varepsilon(0) \sim \mathcal{N}(0,1)
```

### 430 ate-yang-wang-ding-2019-mnar-confounder-v1 3

```math
Y(1) = 3\cdot X_{1} + 2\cdot X_{2} + \varepsilon(1), \varepsilon(1) \sim \mathcal{N}(0,1)
```

### 431 ate-yang-wang-ding-2019-mnar-confounder-v1 4

```math
A \mid  X_{1},X_{2} \sim \mathrm{Bernoulli}(\pi)
```

### 432 ate-yang-wang-ding-2019-mnar-confounder-v1 5

```math
\mathrm{logit}(\pi) = 1.25 - 0.5\cdot X_{1} - 0.5\cdot X_{2}
```

### 433 ate-yang-wang-ding-2019-mnar-confounder-v1 6

```math
R_{1} \mid  X_{1},X_{2},A \sim \mathrm{Bernoulli}(p)
```

### 434 ate-yang-wang-ding-2019-mnar-confounder-v1 7

```math
\mathrm{logit}(p) = -2 + 2\cdot X_{1} + A\cdot (1.5 + X_{2})
```

### 435 ate-yang-wang-ding-2019-mnar-confounder-v1 8

```math
R_{1}=1 \mathrm{means} X_{1} \text{ observed }
```

### 436 ate-yang-wang-ding-2019-mnar-confounder-v1 9

```math
Y = A\cdot Y(1) + (1-A)\cdot Y(0)
```

### 437 ate-yang-wang-ding-2019-mnar-confounder-v1 10

```math
\mathrm{ATE}=\mathbb{E}[Y(1)-Y(0)]=-0.5 + 1\cdot \mathbb{E}[X_{1}] + 1\cdot \mathbb{E}[X_{2}] = -0.5+1+0.5=1
```

### 438 ate-yang-wang-ding-2019-mnar-confounder-v2 0

```math
X_{1}, X_{2} \text{ independently } \mathrm{sampled} \mathcal{N}(\text{ mean }=1, \text{ variance }=1)
```

### 439 ate-yang-wang-ding-2019-mnar-confounder-v2 1

```math
\mathrm{Xj}=(\mathrm{Bj}-0.5)/0.5 \text{ where } \mathrm{Bj} \text{ independently } \mathrm{follows} \mathrm{Bernoulli}(0.5), j=3,4
```

### 440 ate-yang-wang-ding-2019-mnar-confounder-v2 2

```math
X_{5}=X_{1}+X_{2}+X_{3}+X_{4}+\varepsilon_{5}
```

### 441 ate-yang-wang-ding-2019-mnar-confounder-v2 3

```math
\varepsilon_{5}\sim \mathcal{N}(0,1), \text{ independently } \mathrm{generated}.
```

### 442 ate-yang-wang-ding-2019-mnar-confounder-v2 4

```math
X_{6}\mid X_{5}\sim \mathrm{Bernoulli}(p_{6}), \mathrm{logit}(p_{6})=-X_{5}.
```

### 443 ate-yang-wang-ding-2019-mnar-confounder-v2 5

```math
Y(0)=(1,X^{T}) \beta_{0}+\varepsilon_{0}
```

### 444 ate-yang-wang-ding-2019-mnar-confounder-v2 6

```math
Y(1)=(1,X^{T}) \beta_{1}+\varepsilon_{1}
```

### 445 ate-yang-wang-ding-2019-mnar-confounder-v2 7

```math
\beta_{0}=(-1.5,1,-1,1,-1,1,1)^{T}
```

### 446 ate-yang-wang-ding-2019-mnar-confounder-v2 8

```math
\beta_{1}=(0,-1,1,-1,1,-1,-1)^{T}
```

### 447 ate-yang-wang-ding-2019-mnar-confounder-v2 9

```math
\varepsilon_{0},\varepsilon_{1}\sim \mathcal{N}(0,1).
```

### 448 ate-yang-wang-ding-2019-mnar-confounder-v2 10

```math
A\mid X\sim \mathrm{Bernoulli}(\mathrm{expit}((1,X^{T}) \alpha))
```

### 449 ate-yang-wang-ding-2019-mnar-confounder-v2 11

```math
\alpha=0.5\cdot (2,1,1,1,1,-2,-2)^{T}.
```

### 450 ate-yang-wang-ding-2019-mnar-confounder-v2 12

```math
R=(R_{5},R_{6}) \in \{(11),(10),(01),(00)\}
```

### 451 ate-yang-wang-ding-2019-mnar-confounder-v2 13

```math
\mathrm{Let} q=(1,A,X^{T}) \eta, \eta=0.25\cdot (-4,1,1,1,1,1,-1,-1)^{T}
```

### 452 ate-yang-wang-ding-2019-mnar-confounder-v2 14

```math
\mathrm{pkl}=1/(\exp(-q)+3) \text{ for } \mathrm{kl}=10,01,00
```

### 453 ate-yang-wang-ding-2019-mnar-confounder-v2 15

```math
Y=A\cdot Y(1)+(1-A)\cdot Y(0).
```

### 454 ate-yang-wang-ding-2019-mnar-confounder-v2 16

```math
\mathrm{ATE}=\mathbb{E}[Y(1)-Y(0)]=1.5-2\mathbb{E}[X_{1}]+2\mathbb{E}[X_{2}]-2\mathbb{E}[X_{3}]+2\mathbb{E}[X_{4}]-2\mathbb{E}[X_{5}]-2\mathbb{E}[X_{6}] = -2.5-2\mathbb{E}[X_{6}] \mathrm{under} \text{ the } \mathrm{declared} \mathrm{factorization}
```

### 455 cate-athey-2019-heterogeneity-confounding-v1 0

```math
\mathrm{Xj} \sim \mathrm{Uniform}(0,1) \text{ independently }, j = 1..5
```

### 456 cate-athey-2019-heterogeneity-confounding-v1 1

```math
P(A=1\mid X) = 0.25 (1 + 20 X_{3} (1-X_{3})^{3})
```

### 457 cate-athey-2019-heterogeneity-confounding-v1 2

```math
m(X) = 2 X_{3} - 1
```

### 458 cate-athey-2019-heterogeneity-confounding-v1 3

```math
\tau(X) = s(X_{1}) s(X_{2}), s(u) = 1 + 1/(1 + \exp(-20 (u - 1/3)))
```

### 459 cate-athey-2019-heterogeneity-confounding-v1 4

```math
Y = m(X) + A \tau(X) + \varepsilon, \varepsilon\sim \mathcal{N}(0,1)
```

### 460 cate-athey-tibshirani-wager-2019-confounded-v1 0

```math
X_{j}\overset{\mathrm{iid}}{\sim} \mathrm{Uniform}(0,1), j=1,\ldots ,10
```

### 461 cate-athey-tibshirani-wager-2019-confounded-v1 1

```math
e(X)=[1+20\cdot X_{3}\cdot (1-X_{3})^{3}]/4
```

### 462 cate-athey-tibshirani-wager-2019-confounded-v1 2

```math
A\mid X\sim \mathrm{Bernoulli}(e(X))
```

### 463 cate-athey-tibshirani-wager-2019-confounded-v1 3

```math
m(X)=2\cdot X_{3}-1
```

### 464 cate-athey-tibshirani-wager-2019-confounded-v1 4

```math
\tau(X)=s(X_{1})\cdot s(X_{2}), s(u)=1+1/[1+\exp(-20\cdot (u-1/3))]
```

### 465 cate-athey-tibshirani-wager-2019-confounded-v1 5

```math
Y=m(X)+(A-0.5)\cdot \tau(X)+\varepsilon
```

### 466 cate-athey-tibshirani-wager-2019-confounded-v1 6

```math
\varepsilon\sim \mathcal{N}(0,1)
```

### 467 cate-lei-2021-conformal-cate-v1 0

```math
\mathrm{Xj} = \Phi(X'_{j}), X' \mathrm{equicorrelated} \mathrm{Gaussian} \text{ with } \rho= 0, \mathrm{so} \mathrm{Xj} \sim \mathrm{Uniform}(0,1) \text{ independently }, j = 1..10
```

### 468 cate-lei-2021-conformal-cate-v1 1

```math
e(X) = (1/4) \{1 + F_{2,4}(X_{1})\}, F_{2,4} \text{ the } \mathrm{Beta}(2,4) \mathrm{cdf}
```

### 469 cate-lei-2021-conformal-cate-v1 2

```math
Y(0) = 0
```

### 470 cate-lei-2021-conformal-cate-v1 3

```math
\mathbb{E}[Y(1)\mid X] = f(X_{1}) f(X_{2}), f(u) = 2 / (1 + \exp(-12 (u - 1/2)))
```

### 471 cate-lei-2021-conformal-cate-v1 4

```math
Y(1) = \mathbb{E}[Y(1)\mid X] + \sigma\varepsilon
```

### 472 cate-lei-2021-conformal-cate-v1 5

```math
\tau(X) = f(X_{1}) f(X_{2})
```

### 473 cate-lei-2021-conformal-cate-v1 6

```math
Y = A Y(1) + (1-A) Y(0)
```

### 474 cate-lei-2021-conformal-cate-v1 7

```math
\sigma= 1
```

### 475 cate-nie-2021-setup-a-v1 0

```math
\mathrm{Xj} \sim \mathrm{Uniform}(0,1) \text{ independently }, j = 1..5
```

### 476 cate-nie-2021-setup-a-v1 1

```math
e(X) = \mathrm{trim}_{0.1}\{\sin(\pi X_{1} X_{2})\}, \mathrm{trim}_{\eta}(u) = \max\{\eta, \min(u, 1-\eta)\}
```

### 477 cate-nie-2021-setup-a-v1 2

```math
b(X) = \sin(\pi X_{1} X_{2}) + 2 (X_{3} - 1/2)^{2} + X_{4} + 0.5 X_{5}
```

### 478 cate-nie-2021-setup-a-v1 3

```math
\tau(X) = (X_{1} + X_{2}) / 2
```

### 479 cate-nie-2021-setup-a-v1 4

```math
Y = b(X) + A \tau(X) + \sigma\varepsilon, \varepsilon\sim \mathcal{N}(0,1)
```

### 480 cate-nie-2021-setup-a-v1 5

```math
\sigma= 1
```

### 481 cate-nie-2021-setup-b-v1 0

```math
\mathrm{Xj} \sim \mathcal{N}(0,1) \text{ independently }, j = 1..5
```

### 482 cate-nie-2021-setup-b-v1 1

```math
e(X) = 1/2
```

### 483 cate-nie-2021-setup-b-v1 2

```math
b(X) = \max\{X_{1} + X_{2}, X_{3}, 0\} + \max\{X_{4} + X_{5}, 0\}
```

### 484 cate-nie-2021-setup-b-v1 3

```math
\tau(X) = X_{1} + \log(1 + \exp(X_{2}))
```

### 485 cate-nie-2021-setup-b-v1 4

```math
Y = b(X) + A \tau(X) + \sigma\varepsilon, \varepsilon\sim \mathcal{N}(0,1)
```

### 486 cate-nie-2021-setup-b-v1 5

```math
\sigma= 1
```

### 487 cate-nie-2021-setup-c-v1 0

```math
\mathrm{Xj} \sim \mathcal{N}(0,1) \text{ independently }, j = 1..3
```

### 488 cate-nie-2021-setup-c-v1 1

```math
e(X) = 1 / (1 + \exp(X_{2} + X_{3}))
```

### 489 cate-nie-2021-setup-c-v1 2

```math
b(X) = 2 \log(1 + \exp(X_{1} + X_{2} + X_{3}))
```

### 490 cate-nie-2021-setup-c-v1 3

```math
\tau(X) = 1
```

### 491 cate-nie-2021-setup-c-v1 4

```math
Y = b(X) + A \tau(X) + \sigma\varepsilon, \varepsilon\sim \mathcal{N}(0,1)
```

### 492 cate-nie-2021-setup-c-v1 5

```math
\sigma= 1
```

### 493 cate-nie-2021-setup-d-v1 0

```math
\mathrm{Xj} \sim \mathcal{N}(0,1) \text{ independently }, j = 1..5
```

### 494 cate-nie-2021-setup-d-v1 1

```math
e(X) = 1 / (1 + \exp(-X_{1}) + \exp(-X_{2}))
```

### 495 cate-nie-2021-setup-d-v1 2

```math
b(X) = (\max\{X_{1}+X_{2}+X_{3}, 0\} + \max\{X_{4}+X_{5}, 0\}) / 2
```

### 496 cate-nie-2021-setup-d-v1 3

```math
\tau(X) = \max\{X_{1}+X_{2}+X_{3}, 0\} - \max\{X_{4}+X_{5}, 0\}
```

### 497 cate-nie-2021-setup-d-v1 4

```math
Y = b(X) + (A - 1/2) \tau(X) + \sigma\varepsilon, \varepsilon\sim \mathcal{N}(0,1)
```

### 498 cate-nie-2021-setup-d-v1 5

```math
\sigma= 1
```

### 499 cate-nie-2021-setup-d-v1 6

```math
\mu_{0}(X) = b(X) - \tau(X)/2 = \max\{X_{4}+X_{5}, 0\}
```

### 500 cate-nie-2021-setup-d-v1 7

```math
\mu_{1}(X) = b(X) + \tau(X)/2 = \max\{X_{1}+X_{2}+X_{3}, 0\}
```

### 501 cate-wager-2018-null-confounded-v1 0

```math
\mathrm{Xj} \sim \mathrm{Uniform}(0,1) \text{ independently }, j = 1..5
```

### 502 cate-wager-2018-null-confounded-v1 1

```math
P(A=1\mid X) = 0.25 \cdot  (1 + 20 X_{1} (1-X_{1})^{3})
```

### 503 cate-wager-2018-null-confounded-v1 2

```math
m(X) = 2 X_{1} - 1
```

### 504 cate-wager-2018-null-confounded-v1 3

```math
\tau(X) = 0
```

### 505 cate-wager-2018-null-confounded-v1 4

```math
Y = m(X) + A \tau(X) + \varepsilon, \varepsilon\sim \mathcal{N}(0,1)
```

### 506 cate-wager-2018-sparse-signal-v1 0

```math
\mathrm{Xj} \sim \mathrm{Uniform}(0,1) \text{ independently }, j = 1..6
```

### 507 cate-wager-2018-sparse-signal-v1 1

```math
P(A=1\mid X) = 0.5
```

### 508 cate-wager-2018-sparse-signal-v1 2

```math
m(X) = 0
```

### 509 cate-wager-2018-sparse-signal-v1 3

```math
\tau(X) = (4/q) \sum_{j=1..q} [1/(1+\exp(-12 (\mathrm{Xj} - 1/2))) - 1/2]
```

### 510 cate-wager-2018-sparse-signal-v1 4

```math
q = 4
```

### 511 cate-wager-2018-sparse-signal-v1 5

```math
Y = m(X) + A \tau(X) + \varepsilon, \varepsilon\sim \mathcal{N}(0,1)
```

### 512 cate-ye-2023-interaction-zero-mean-v1 0

```math
P(A=1) = 0.5 (\mathrm{simple} \mathrm{randomisation}, \mathrm{two} \mathrm{arms} \text{ at } 1:1)
```

### 513 cate-ye-2023-interaction-zero-mean-v1 1

```math
Y(1) = \varepsilon, Y(2) = Y(1) + \zeta(U - \mathrm{muU})
```

### 514 cate-ye-2023-interaction-zero-mean-v1 2

```math
\zeta= 1, \mathrm{muU} = 0
```

### 515 cate-ye-2023-interaction-zero-mean-v1 3

```math
\tau(U) = \zeta(U - \mathrm{muU}) = U, \text{ with } \mathbb{E}[\tau(U)] = 0
```

### 516 cate-ye-2023-interaction-zero-mean-v1 4

```math
Y = A Y(2) + (1-A) Y(1) = \varepsilon+ A \tau(U)
```

### 517 cate-ye-2023-quadratic-misspecified-v1 0

```math
P(A=1) = 0.5 (\mathrm{simple} \mathrm{randomisation}, \mathrm{two} \mathrm{arms} \text{ at } 1:1)
```

### 518 cate-ye-2023-quadratic-misspecified-v1 1

```math
Y(1) = \varepsilon, Y(2) = -1.3 + Y(1) - 0.5(U - \mathrm{muU}) - 0.01(U^{2} - \mathrm{muU2}) + 0.3(W - \mathrm{muW})
```

### 519 cate-ye-2023-quadratic-misspecified-v1 2

```math
\tau(U, W) = -1.3 - 0.5 U - 0.01(U^{2} - 1) + 0.3 W
```

### 520 cate-ye-2023-quadratic-misspecified-v1 3

```math
Y = \varepsilon+ A \tau(U, W)
```

### 521 ate-wager-athey-2018-confounded-null-v1 0

```math
X_{j}\overset{\mathrm{iid}}{\sim} \mathrm{Uniform}(0,1), j=1,\ldots ,5
```

### 522 ate-wager-athey-2018-confounded-null-v1 1

```math
e(X)=[1+20\cdot X_{1}\cdot (1-X_{1})^{3}]/4
```

### 523 ate-wager-athey-2018-confounded-null-v1 2

```math
A\mid X\sim \mathrm{Bernoulli}(e(X))
```

### 524 ate-wager-athey-2018-confounded-null-v1 3

```math
m(X)=2\cdot X_{1}-1
```
