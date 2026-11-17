# Math probe batch 8

### 1225 qdi-hall-wolff-yao-1999-sine-triangular-v1 8

```math
G(z)=0 \text{ for } z\leq -1
```

### 1226 qdi-hall-wolff-yao-1999-sine-triangular-v1 9

```math
(1+z)^{2}/2 \text{ for } -1<z\leq 0
```

### 1227 qdi-hall-wolff-yao-1999-sine-triangular-v1 10

```math
1-(1-z)^{2}/2 \text{ for } 0<z<1
```

### 1228 qdi-hall-wolff-yao-1999-sine-triangular-v1 11

```math
1 \text{ for } z\geq 1.
```

### 1229 qdi-hall-wolff-yao-1999-sine-triangular-v1 12

```math
\theta=F(1\mid 0.1)=1-2\cdot \sin(0.31416)^{2}=0.8090161307517588 (\mathrm{binary64} \mathrm{evaluation}).
```

### 1230 qdi-hall-yao-2005-additive-sine-v1 0

```math
X_{ij},\varepsilon_i\overset{\mathrm{ind}}{\sim}\mathcal N(0,1),\quad j=1,\ldots,4
```

### 1231 qdi-hall-yao-2005-additive-sine-v1 1

```math
Y_i=\frac12\sum_{j=1}^4\sin(X_{ij})+\varepsilon_i
```

### 1232 qdi-hall-yao-2005-additive-sine-v1 2

```math
F_{Y\mid X}(y\mid x)=\Phi\!\left(y-\frac12\sum_{j=1}^4\sin x_j\right)
```

### 1233 qdi-hall-yao-2005-gaussian-index-v1 0

```math
X_{ij},\varepsilon_i\overset{\mathrm{ind}}{\sim}\mathcal N(0,1),\quad j=1,\ldots,4
```

### 1234 qdi-hall-yao-2005-gaussian-index-v1 1

```math
Y_i=\frac{X_{i1}+2X_{i2}+3X_{i4}}{\sqrt{14}}+\varepsilon_i
```

### 1235 qdi-hall-yao-2005-gaussian-index-v1 2

```math
Q_Y(0.9)=\sqrt 2\,\Phi^{-1}(0.9)
```

### 1236 qdi-henzi-2021-gamma-shift-v1 0

```math
X_{i}\overset{\mathrm{iid}}{\sim} \mathrm{Uniform}(0,10)
```

### 1237 qdi-henzi-2021-gamma-shift-v1 1

```math
G_{i} \mid  X_{i}=x \sim \Gamma(\text{ shape }=\sqrt{x}, \text{ scale }=\min(\max(x,1),6))
```

### 1238 qdi-henzi-2021-gamma-shift-v1 2

```math
Y_{i}=G_{i}
```

### 1239 qdi-henzi-2021-gamma-shift-v1 3

```math
Y_{i}=G_{i}+10\cdot 1\{X_{i}\geq 5\}
```

### 1240 qdi-henzi-2021-gamma-shift-v1 4

```math
Y_{i}=G_{i}-2\cdot 1\{X_{i}\geq 7\}
```

### 1241 qdi-henzi-2021-gamma-shift-v1 5

```math
\theta_{s}=P(Y_{i}\leq 10 \mid  X_{i}=5.5)
```

### 1242 qdi-henzi-2021-poisson-clipped-rate-v1 0

```math
X_{i}\overset{\mathrm{iid}}{\sim} \mathrm{Uniform}(0,10)
```

### 1243 qdi-henzi-2021-poisson-clipped-rate-v1 1

```math
\lambda(x)=\min(\max(x,1),6) = 1 \text{ if } 0<x\leq 1
```

### 1244 qdi-henzi-2021-poisson-clipped-rate-v1 2

```math
x \text{ if } 1<x<6
```

### 1245 qdi-henzi-2021-poisson-clipped-rate-v1 3

```math
6 \text{ if } 6\leq x<10
```

### 1246 qdi-henzi-2021-poisson-clipped-rate-v1 4

```math
Y_{i} \mid  X_{i}=x \sim \mathrm{Poisson}(\lambda(x))
```

### 1247 qdi-henzi-2021-poisson-clipped-rate-v1 5

```math
P(Y_{i}=k\mid X_{i}=x)=\exp(-\lambda(x))\cdot \lambda(x)^{k}/k!, k=0,1,\ldots
```

### 1248 qdi-henzi-2021-poisson-clipped-rate-v1 6

```math
\theta=P(Y\leq 3\mid X=5)=\exp(-5)\cdot (1+5+25/2+125/6)=(118/3)\cdot \exp(-5)
```

### 1249 qdi-henzi-2021-poisson-clipped-rate-v1 7

```math
\theta=\int_{5}^{\infty} t^{3}\cdot \exp(-t)/6 \mathrm{dt} (\Gamma/\mathrm{Erlang} \mathrm{survival})
```

### 1250 qdi-li-liu-zhu-2007-exponential-surface-v1 0

```math
X_{i1},X_{i2}\overset{\mathrm{iid}}{\sim}U(0,1),\quad\varepsilon_i\perp X_i
```

### 1251 qdi-li-liu-zhu-2007-exponential-surface-v1 1

```math
m(x)=\frac{40e^{8\{(x_1-0.5)^2+(x_2-0.5)^2\}}}{e^{8\{(x_1-0.2)^2+(x_2-0.7)^2\}}+e^{8\{(x_1-0.7)^2+(x_2-0.2)^2\}}}
```

### 1252 qdi-li-liu-zhu-2007-exponential-surface-v1 2

```math
Y_i=m(X_i)+\varepsilon_i,\quad\varepsilon_i\sim\mathcal N(0,1)\;\text{or}\;t_3\;\text{or}\;0.1\mathcal N(0,25)+0.9\mathcal N(0,1)
```

### 1253 qdi-li-liu-zhu-2007-exponential-surface-v1 3

```math
Q_\tau(x)=m(x)+F_\varepsilon^{-1}(\tau)
```

### 1254 qdi-li-liu-zhu-2007-sinc-v1 0

```math
X_i\sim U(-2,2),\quad\varepsilon_i\sim\mathcal N(0,0.2^2),\quad X_i\perp\varepsilon_i
```

### 1255 qdi-li-liu-zhu-2007-sinc-v1 1

```math
Y_i=\frac{\sin(\pi X_i)}{\pi X_i}+\varepsilon_i,\quad \mathrm{sinc}(0)=1
```

### 1256 qdi-li-liu-zhu-2007-sinc-v1 2

```math
Q_\tau(x)=\mathrm{sinc}(x)+0.2\Phi^{-1}(\tau)
```

### 1257 qdi-shen-meinshausen-2025-preadditive-noise-v1 0

```math
Y=g(WX+\eta)+\beta^{T} X
```

### 1258 qdi-shen-meinshausen-2025-preadditive-noise-v1 1

```math
\mathrm{collected} \mathrm{simulation} \mathrm{specializes} \text{ to } d=k=1,W=1,\beta=0, \mathrm{so} Y=g_{s}(X+\eta).
```

### 1259 qdi-shen-meinshausen-2025-preadditive-noise-v1 2

```math
(X_{i},\eta_{i}) \text{ iid } \text{ across } i
```

### 1260 qdi-shen-meinshausen-2025-preadditive-noise-v1 3

```math
\eta_{i}\sim \mathcal{N}(0,\sigma_{s}^{2})
```

### 1261 qdi-shen-meinshausen-2025-preadditive-noise-v1 4

```math
\sigma_{\mathrm{cubic}}=1.1, \text{ all } \mathrm{others}=1.
```

### 1262 qdi-shen-meinshausen-2025-preadditive-noise-v1 5

```math
X_{i}\sim \mathrm{Unif}[-2,2] \text{ for } \mathrm{softplus},\mathrm{cubic}
```

### 1263 qdi-shen-meinshausen-2025-preadditive-noise-v1 6

```math
X_{i}\sim \mathrm{Unif}[0,2] \text{ for } \mathrm{square},\log.
```

### 1264 qdi-shen-meinshausen-2025-preadditive-noise-v1 7

```math
g_{\mathrm{softplus}}(u)=\ln(1+\exp(u)).
```

### 1265 qdi-shen-meinshausen-2025-preadditive-noise-v1 8

```math
g_{\mathrm{square}}(u)=\max(u,0)^{2}/2.
```

### 1266 qdi-shen-meinshausen-2025-preadditive-noise-v1 9

```math
g_{\mathrm{cubic}}(u)=u^{3}/3.
```

### 1267 qdi-shen-meinshausen-2025-preadditive-noise-v1 10

```math
g_{\log}(u)=(u-2)/3+\ln(3) \text{ if } u\leq 2
```

### 1268 qdi-shen-meinshausen-2025-preadditive-noise-v1 11

```math
\ln(u) \text{ if } u>2
```

### 1269 qdi-shen-meinshausen-2025-preadditive-noise-v1 12

```math
q_{s}=\inf\{y:P_{\eta}(g_{s}(0.5+\eta)\leq y)\geq 0.5\}
```

### 1270 qdi-tan-wang-zhou-20220201-active10-mixture-v2 0

```math
A=(1,3,5,7,9,11,13,15,17,19)
```

### 1271 qdi-tan-wang-zhou-20220201-active10-mixture-v2 1

```math
W_{ik}=X_{\mathrm{original},i},A[k]
```

### 1272 qdi-tan-wang-zhou-20220201-active10-mixture-v2 2

```math
W_{i} \sim \mathcal{N}_{10}(0,\Sigma_{AA})
```

### 1273 qdi-tan-wang-zhou-20220201-active10-mixture-v2 3

```math
(\Sigma_{AA})_{jk}=0.7^{\lvert \mathrm{Aj}-\mathrm{Ak}\rvert}=0.49^{\lvert j-k\rvert}
```

### 1274 qdi-tan-wang-zhou-20220201-active10-mixture-v2 4

```math
Z_{ik}\overset{\mathrm{iid}}{\sim} \mathcal{N}(0,1)
```

### 1275 qdi-tan-wang-zhou-20220201-active10-mixture-v2 5

```math
W_{i1}=Z_{i1}
```

### 1276 qdi-tan-wang-zhou-20220201-active10-mixture-v2 6

```math
W_{ik}=0.49\cdot W_{i,k-1}+\sqrt{1-0.49^{2}}\cdot Z_{ik}, k=2,\ldots ,10.
```

### 1277 qdi-tan-wang-zhou-20220201-active10-mixture-v2 7

```math
b=(1.8,1.6,1.4,1.2,1,-1,-1.2,-1.4,-1.6,-1.8)
```

### 1278 qdi-tan-wang-zhou-20220201-active10-mixture-v2 8

```math
\mathrm{intercept}=0. W_{k} \text{ is } \text{ the } \mathrm{original} \mathrm{coordinate} 2k-1.
```

### 1279 qdi-tan-wang-zhou-20220201-active10-mixture-v2 9

```math
B_{i} \sim \mathrm{Bernoulli}(0.7)
```

### 1280 qdi-tan-wang-zhou-20220201-active10-mixture-v2 10

```math
U_{i} \sim \mathcal{N}(0,1)
```

### 1281 qdi-tan-wang-zhou-20220201-active10-mixture-v2 11

```math
\varepsilon_{i}=[B_{i}+5\cdot (1-B_{i})]\cdot U_{i} \sim 0.7\cdot \mathcal{N}(0,1)+0.3\cdot \mathcal{N}(0,25)
```

### 1282 qdi-tan-wang-zhou-20220201-active10-mixture-v2 12

```math
\mathrm{Normal} \mathrm{second} \mathrm{parameter} \text{ is } \text{ variance }.
```

### 1283 qdi-tan-wang-zhou-20220201-active10-mixture-v2 13

```math
Y_{i}=\sum_{k=1}^{10} b_{k} W_{ik}+\varepsilon_{i}
```

### 1284 qdi-tan-wang-zhou-20220201-active10-mixture-v2 14

```math
w_{0}=e_{1} \in R^{10}
```

### 1285 qdi-tan-wang-zhou-20220201-active10-mixture-v2 15

```math
\theta_{\tau}=1.8+q_{\tau}
```

### 1286 qdi-tan-wang-zhou-20220201-active10-mixture-v2 16

```math
0.7\cdot \Phi(q_{\tau})+0.3\cdot \Phi(q_{\tau}/5)=\tau, \tau\in \{0.5,0.9\}.
```

### 1287 qdi-yang-he-2012-conditional-quantile-v1 0

```math
X \sim \chi-\mathrm{square}(\mathrm{df}=2)
```

### 1288 qdi-yang-he-2012-conditional-quantile-v1 1

```math
Z = 2B, B \sim \mathrm{Bernoulli}(0.5)
```

### 1289 qdi-yang-he-2012-conditional-quantile-v1 2

```math
Y=X+Z+e
```

### 1290 qdi-yang-he-2012-conditional-quantile-v1 3

```math
e\sim \mathcal{N}(\text{ mean }=0, \text{ variance }=4).
```

### 1291 qdi-yang-he-2012-conditional-quantile-v1 4

```math
Y=X+Z+e
```

### 1292 qdi-yang-he-2012-conditional-quantile-v1 5

```math
\log(e)\sim \mathcal{N}(\text{ mean }=0, \text{ variance }=1)
```

### 1293 qdi-yang-he-2012-conditional-quantile-v1 6

```math
Y=X+Z+(1+X/2)e
```

### 1294 qdi-yang-he-2012-conditional-quantile-v1 7

```math
e\sim \mathcal{N}(\text{ mean }=0, \text{ variance }=4).
```

### 1295 qdi-yang-he-2012-conditional-quantile-v1 8

```math
Y=X+Z+(1+X/2)e
```

### 1296 qdi-yang-he-2012-conditional-quantile-v1 9

```math
\log(e)\sim \mathcal{N}(\text{ mean }=0, \text{ variance }=1)
```

### 1297 qdi-yang-he-2012-conditional-quantile-v1 10

```math
\theta_{m}=2+s_{m}(2)q_{e}(0.95), \text{ with } s_{1}=s_{2}=1, s_{3}(x)=s_{4}(x)=1+x/2
```

### 1298 qdi-yang-he-2012-conditional-quantile-v1 11

```math
q_{\mathrm{normal}}(\tau)=2 \Phi^{-1}(\tau), q_{\mathrm{lognormal}}(\tau)=\exp(\Phi^{-1}(\tau)).
```

### 1299 qdi-yang-tokdar-2017-triangular-quantile-v1 0

```math
\mathrm{Published} \mathrm{illustration} n=1000
```

### 1300 qdi-yang-tokdar-2017-triangular-quantile-v1 1

```math
B=(-1,2)
```

### 1301 qdi-yang-tokdar-2017-triangular-quantile-v1 2

```math
C=(2,-1)
```

### 1302 qdi-yang-tokdar-2017-triangular-quantile-v1 3

```math
R_{i},T_{i}\overset{\mathrm{iid}}{\sim} \mathrm{Uniform}(0,1)
```

### 1303 qdi-yang-tokdar-2017-triangular-quantile-v1 4

```math
\text{ if } R_{i}+T_{i}>1 \text{ then } (u_{i},v_{i})=(1-R_{i},1-T_{i}), \mathrm{else} (R_{i},T_{i})
```

### 1304 qdi-yang-tokdar-2017-triangular-quantile-v1 5

```math
\mathrm{Density} \text{ of } (u_{i},v_{i}) \text{ is } 2 \text{ on } u\geq 0,v\geq 0,u+v\leq 1.
```

### 1305 qdi-yang-tokdar-2017-triangular-quantile-v1 6

```math
X_{i}=A+u_{i}(B-A)+v_{i}(C-A)=(-1+3v_{i},1+u_{i}-2v_{i})
```

### 1306 qdi-yang-tokdar-2017-triangular-quantile-v1 7

```math
X_{i}\sim \mathrm{Uniform}_{\mathrm{area}}(D). D=\{x_{1}\geq -1,2x_{1}+3x_{2}\geq 1,x_{1}+x_{2}\leq 1\}
```

### 1307 qdi-yang-tokdar-2017-triangular-quantile-v1 8

```math
\mathrm{area}=3/2, \mathrm{density}=2/3.
```

### 1308 qdi-yang-tokdar-2017-triangular-quantile-v1 9

```math
s_{i}=\mathrm{X1}_{i}+\mathrm{X2}_{i} \in [0,1]
```

### 1309 qdi-yang-tokdar-2017-triangular-quantile-v1 10

```math
\text{ a }_{i}=(1-s_{i})/3 \in [0,1/3]
```

### 1310 qdi-yang-tokdar-2017-triangular-quantile-v1 11

```math
b_{i}=(2+s_{i})/3 \in [2/3,1]
```

### 1311 qdi-yang-tokdar-2017-triangular-quantile-v1 12

```math
\text{ a }_{i}+b_{i}=1.
```

### 1312 qdi-yang-tokdar-2017-triangular-quantile-v1 13

```math
Z_{i}\sim \mathcal{N}(0,1)
```

### 1313 qdi-yang-tokdar-2017-triangular-quantile-v1 14

```math
Y_{i}=\text{ a }_{i} Z_{i}+b_{i}(1+Z_{i}/5)=\mu_{i}+\sigma_{i} Z_{i}
```

### 1314 qdi-yang-tokdar-2017-triangular-quantile-v1 15

```math
\mu_{i}=(2+s_{i})/3, \sigma_{i}=(7-4s_{i})/15 \in [1/5,7/15]. Y_{i}\mid X_{i}\sim \mathcal{N}(\mu_{i},\sigma_{i}^{2}). \varepsilon_{i}=Y_{i}-\mu_{i} \mathrm{has} \mathrm{conditional} \text{ variance } \sigma_{i}^{2}
```

### 1315 qdi-yang-tokdar-2017-triangular-quantile-v1 16

```math
\mathrm{Repeat} \text{ the } \mathrm{row} \mathrm{law} \text{ iid } \text{ for } i=1,\ldots ,n
```

### 1316 qdi-yang-tokdar-2017-triangular-quantile-v1 17

```math
\mathrm{Within}-\mathrm{row} X_{1}/X_{2} \mathrm{covariance}=-5/12
```

### 1317 qdi-yang-tokdar-2017-triangular-quantile-v1 18

```math
s=x_{1}+x_{2}
```

### 1318 qdi-yang-tokdar-2017-triangular-quantile-v1 19

```math
Q_{Y}(\tau|x)=(1-s)/3\cdot Q_{\mathcal{N}}(\tau|0,1)+(2+s)/3\cdot Q_{\mathcal{N}}(\tau|1,0.2^{2}), \text{ where } \mathrm{second} Q_{\mathrm{N}} \mathrm{parameter} \text{ is } \text{ variance }.
```

### 1319 qdi-yang-tokdar-2017-triangular-quantile-v1 20

```math
z_{\tau}=\Phi^{-1}(\tau)
```

### 1320 qdi-yang-tokdar-2017-triangular-quantile-v1 21

```math
\beta_{0}(\tau)=2/3+(7/15)z_{\tau}
```

### 1321 qdi-yang-tokdar-2017-triangular-quantile-v1 22

```math
\beta_{1}(\tau)=\beta_{2}(\tau)=1/3-(4/15)z_{\tau}
```

### 1322 qdi-yang-tokdar-2017-triangular-quantile-v1 23

```math
f_{X},Y(x,y)=(2/3)\cdot 1_{D}(x)\cdot \phi((y-\mu(x))/\sigma(x))/\sigma(x)
```

### 1323 qdi-yang-tokdar-2017-triangular-quantile-v1 24

```math
F_{Y}(y\mid x)=\Phi((y-\mu(x))/\sigma(x)).
```

### 1324 qdi-yang-tokdar-2017-triangular-quantile-v1 25

```math
x^{\ast}=(0,2/3), \tau^{\ast}=19/20
```

### 1325 qdi-yang-tokdar-2017-triangular-quantile-v1 26

```math
\theta=8/9+(13/45)\cdot \Phi^{-1}(19/20).
```

### 1326 qdi-yang-tokdar-20170412-univariate-quantile-v1 0

```math
X \sim \mathrm{Uniform}(-1,1)
```

### 1327 qdi-yang-tokdar-20170412-univariate-quantile-v1 1

```math
Q_{Y}(\tau\mid X=x) = 3\cdot (\tau-1/2)\cdot \log(1/[\tau\cdot (1-\tau)]) + 4\cdot (\tau-1/2)^{2}\cdot \log(1/[\tau\cdot (1-\tau)])\cdot x
```

### 1328 qdi-yang-tokdar-20170412-univariate-quantile-v1 2

```math
0<\tau<1
```

### 1329 qdi-yang-tokdar-20170412-univariate-quantile-v1 3

```math
U \sim \mathrm{Uniform}(0,1)
```

### 1330 qdi-yang-tokdar-20170412-univariate-quantile-v1 4

```math
Y=Q_{Y}(U\mid X)
```

### 1331 qdi-yang-tokdar-20170412-univariate-quantile-v1 5

```math
\text{ iid } \mathrm{pairs} \text{ across } \text{ rows }
```

### 1332 qdi-yang-tokdar-20170412-univariate-quantile-v1 6

```math
\theta=Q_{Y}(0.9\mid X=0.5)=(38/25)\cdot \log(100/9)
```

### 1333 sspi-ahmed-2025-cauchy-tail-quantile-v1 0

```math
\mathrm{Equivalent} \text{ independent }-\mathrm{normal} \mathrm{construction}: G_{0},G_{1},G_{2}\overset{\mathrm{iid}}{\sim} \mathcal{N}(0,1)
```

### 1334 sspi-ahmed-2025-cauchy-tail-quantile-v1 1

```math
V=\lvert G_{1}\rvert/\lvert G_{0}\rvert
```

### 1335 sspi-ahmed-2025-cauchy-tail-quantile-v1 2

```math
U=\lvert G_{2}\rvert/\lvert G_{0}\rvert.
```

### 1336 sspi-ahmed-2025-cauchy-tail-quantile-v1 3

```math
F_{0}(v)=2\cdot \mathrm{atan}(v)/\pi\text{ for } v\geq 0
```

### 1337 sspi-ahmed-2025-cauchy-tail-quantile-v1 4

```math
\mathrm{Outcome} Y=-\log(1-F_{0}(V))
```

### 1338 sspi-ahmed-2025-cauchy-tail-quantile-v1 5

```math
\text{ observed } \mathrm{covariate} X_{1}=U
```

### 1339 sspi-ahmed-2025-cauchy-tail-quantile-v1 6

```math
\mathrm{Source} \gamma=0 \in \mathrm{equation} (16).
```

### 1340 sspi-ahmed-2025-cauchy-tail-quantile-v1 7

```math
Y_{\mathrm{obs}}=Y \text{ there }. R=0 \in \text{ the } \mathrm{remaining} \mathrm{block}
```

### 1341 sspi-ahmed-2025-cauchy-tail-quantile-v1 8

```math
Y_{\mathrm{obs}}=0 \text{ is } \text{ a } \text{ placeholder }.
```

### 1342 sspi-azriel-2022-quadratic-projection-v1 0

```math
X\sim \mathcal{N}(0,1) \text{ and } \varepsilon\sim \mathcal{N}(0,1) \text{ independently }.
```

### 1343 sspi-azriel-2022-quadratic-projection-v1 1

```math
Y=0.5\cdot X^{2}+X+\varepsilon.
```

### 1344 sspi-azriel-2022-quadratic-projection-v1 2

```math
Y_{\mathrm{obs}}=Y \text{ there }. R=0 \in \text{ the } \mathrm{remaining} \mathrm{block}
```

### 1345 sspi-azriel-2022-quadratic-projection-v1 3

```math
Y_{\mathrm{obs}}=0 \text{ is } \text{ a } \text{ placeholder }.
```

### 1346 sspi-cai-guo-2020-dense-explained-variance-v1 0

```math
X\sim \mathcal{N}_{800}(0,\Sigma)
```

### 1347 sspi-cai-guo-2020-dense-explained-variance-v1 1

```math
\Sigma_{ij}=0.5^{\lvert i-j\rvert}
```

### 1348 sspi-cai-guo-2020-dense-explained-variance-v1 2

```math
\varepsilon\sim \mathcal{N}(0,1) \text{ independently }.
```

### 1349 sspi-cai-guo-2020-dense-explained-variance-v1 3

```math
\beta_{j}=1.5\cdot 0.8^{j} \text{ for } j=1,\ldots ,800
```

### 1350 sspi-cai-guo-2020-dense-explained-variance-v1 4

```math
Y=\sum_{j} \beta_{j}\cdot X_{j}+\varepsilon.
```

### 1351 sspi-cai-guo-2020-dense-explained-variance-v1 5

```math
Y_{\mathrm{obs}}=Y \text{ there }. R=0 \in \text{ the } \mathrm{remaining} \mathrm{block}
```

### 1352 sspi-cai-guo-2020-dense-explained-variance-v1 6

```math
Y_{\mathrm{obs}}=0 \text{ is } \text{ a } \text{ placeholder }.
```

### 1353 sspi-ji-2026-discrete-surrogate-mean-v1 0

```math
Z\sim \mathrm{Uniform}(\{1,2,3\})
```

### 1354 sspi-ji-2026-discrete-surrogate-mean-v1 1

```math
\varepsilon\sim \mathcal{N}(0,1) \text{ independently }
```

### 1355 sspi-ji-2026-discrete-surrogate-mean-v1 2

```math
Y=\mu_{Z}+\varepsilon, \text{ with } (\mu_{1},\mu_{2},\mu_{3})=(-2,0,4).
```

### 1356 sspi-ji-2026-discrete-surrogate-mean-v1 3

```math
\mathrm{The} \text{ source } \mathrm{assumes} \text{ an } \text{ observed } \text{ fixed } \mathrm{surrogate} \mathrm{prediction} Y_{\mathrm{hat}}=Z
```

### 1357 sspi-ji-2026-discrete-surrogate-mean-v1 4

```math
Y_{\mathrm{obs}}=Y \text{ there }. R=0 \in \text{ the } \mathrm{remaining} \mathrm{block}
```

### 1358 sspi-ji-2026-discrete-surrogate-mean-v1 5

```math
Y_{\mathrm{obs}}=0 \text{ is } \text{ a } \text{ placeholder }.
```

### 1359 sspi-song-2024-even-mixture-logistic-projection-v1 0

```math
G\sim \mathcal{N}_{4}(0,\Sigma)
```

### 1360 sspi-song-2024-even-mixture-logistic-projection-v1 1

```math
\Sigma_{jk}=0.8^{\lvert j-k\rvert}, \text{ independently }. X=B\cdot 1+G.
```

### 1361 sspi-song-2024-even-mixture-logistic-projection-v1 2

```math
Y\mid X\sim \mathrm{Bernoulli}(\mathrm{expit}(\sum_{j=1}^{4} [0.9\cdot X_{j}^{4}\cdot \sin(X_{j})^{6}-2\cdot X_{j}^{2}+2.2]))
```

### 1362 sspi-song-2024-even-mixture-logistic-projection-v1 3

```math
Y_{\mathrm{obs}}=Y \text{ there }. R=0 \in \text{ the } \mathrm{remaining} \mathrm{block}
```

### 1363 sspi-song-2024-even-mixture-logistic-projection-v1 4

```math
Y_{\mathrm{obs}}=0 \text{ is } \text{ a } \text{ placeholder }.
```

### 1364 sspi-song-2024-nonlinear-noise-projection-v1 0

```math
X\sim \mathcal{N}_{4}(0,\Sigma)
```

### 1365 sspi-song-2024-nonlinear-noise-projection-v1 1

```math
\Sigma_{jk}=0.5^{\lvert j-k\rvert}
```

### 1366 sspi-song-2024-nonlinear-noise-projection-v1 2

```math
\eta\sim \mathcal{N}(0,1) \text{ independently }.
```

### 1367 sspi-song-2024-nonlinear-noise-projection-v1 3

```math
Y=(1/4)\cdot \sum_{j=1}^{4} [\exp(X_{j}+2\cdot \cos(X_{j})-0.3\cdot \eta)+0.1\cdot \exp(X_{j}+\sin(X_{j}))+2.5\cdot X_{j}^{3}]+\eta
```

### 1368 sspi-song-2024-nonlinear-noise-projection-v1 4

```math
Y_{\mathrm{obs}}=Y \text{ there }. R=0 \in \text{ the } \mathrm{remaining} \mathrm{block}
```

### 1369 sspi-song-2024-nonlinear-noise-projection-v1 5

```math
Y_{\mathrm{obs}}=0 \text{ is } \text{ a } \text{ placeholder }.
```

### 1370 sspi-wen-2025-gaussian-cdf-v1 0

```math
X\sim \mathcal{N}_{100}(0,I)
```

### 1371 sspi-wen-2025-gaussian-cdf-v1 1

```math
\varepsilon\sim \mathcal{N}(0,1) \text{ independently }
```

### 1372 sspi-wen-2025-gaussian-cdf-v1 2

```math
s=\lceil 0.1\cdot p\rceil=10.
```

### 1373 sspi-wen-2025-gaussian-cdf-v1 3

```math
Y=\sum_{j=1}^{10} X_{j}/\sqrt{10}+0.5\cdot \varepsilon.
```

### 1374 sspi-wen-2025-gaussian-cdf-v1 4

```math
Y_{\mathrm{obs}}=Y \text{ there }. R=0 \in \text{ the } \mathrm{remaining} \mathrm{block}
```

### 1375 sspi-wen-2025-gaussian-cdf-v1 5

```math
Y_{\mathrm{obs}}=0 \text{ is } \text{ a } \text{ placeholder }.
```

### 1376 sspi-zhang-bradic-2022-cosine-index-v1 0

```math
X_{j}\overset{\mathrm{iid}}{\sim} \mathcal{N}(0,1), j=1,\ldots ,50
```

### 1377 sspi-zhang-bradic-2022-cosine-index-v1 1

```math
\varepsilon\sim \mathcal{N}(0,0.25)
```

### 1378 sspi-zhang-bradic-2022-cosine-index-v1 2

```math
Y=3\cdot \cos(X_{1}+X_{2}+X_{3})+\varepsilon
```

### 1379 sspi-zhang-bradic-2022-cosine-index-v1 3

```math
\mathrm{Source} p=51 \mathrm{includes} \text{ an } \mathrm{intercept}.
```

### 1380 sspi-zhang-bradic-2022-cosine-index-v1 4

```math
Y_{\mathrm{obs}}=Y \text{ there }. R=0 \in \text{ the } \mathrm{remaining} \mathrm{block}
```

### 1381 sspi-zhang-bradic-2022-cosine-index-v1 5

```math
Y_{\mathrm{obs}}=0 \text{ is } \text{ a } \text{ placeholder }.
```
