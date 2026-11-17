# Math probe batch 2

### 175 iv-henckel-2024-conditional-graph-v1 6

```math
X <- (1.4038923130557954)\cdot L_{1} + (-1.0690158213970873)\cdot B + (-1.8992312433635747)\cdot L_{2} + \varepsilon_{X}
```

### 176 iv-henckel-2024-conditional-graph-v1 7

```math
M <- (0.35800137127747389)\cdot X + \varepsilon_{M}
```

### 177 iv-henckel-2024-conditional-graph-v1 8

```math
Y <- (-0.79585700972545459)\cdot C + (-0.71641682995974743)\cdot L_{2} + (-0.52749259051598618)\cdot X + (1.4218960031282049)\cdot M + \varepsilon_{Y}
```

### 178 iv-henckel-2024-conditional-graph-v1 9

```math
\mathrm{Gaussian} \mathrm{scenario}: \text{ independent } \varepsilon_{v} \sim \mathcal{N}(0,\text{ variance }_{v})
```

### 179 iv-henckel-2024-conditional-graph-v1 10

```math
\mathrm{uniform} \mathrm{scenario}: \text{ independent } \varepsilon_{v} \sim \mathrm{Uniform}(-\sqrt{3 \text{ variance }_{v}},\sqrt{3 \text{ variance }_{v}}).
```

### 180 iv-henckel-2024-conditional-graph-v1 11

```math
\tau_{YX} = \mathrm{coefficient}[Y,X] + \mathrm{coefficient}[M,X]\cdot \mathrm{coefficient}[Y,M].
```

### 181 iv-lin-2024-wit-code-v1 0

```math
Z_i\sim\mathcal{N}_{21}(0,\Sigma_Z),\qquad (\Sigma_Z)_{jk}=0.8(0.3)^{|j-k|},\quad j,k=1,\ldots,21.
```

### 182 iv-lin-2024-wit-code-v1 1

```math
\begin{pmatrix}\varepsilon_i\\\eta_i\end{pmatrix}\sim\mathcal{N}_2\!\left(\begin{pmatrix}0\\0\end{pmatrix},\begin{pmatrix}1&0.6\\0.6&1\end{pmatrix}\right).
```

### 183 iv-lin-2024-wit-code-v1 2

```math
Z_i\perp\!\!\!\perp(\varepsilon_i,\eta_i),\qquad (Z_i,\varepsilon_i,\eta_i)\overset{\mathrm{iid}}{\sim}P,\quad i=1,\ldots,n.
```

### 184 iv-lin-2024-wit-code-v1 3

```math
p=21,\qquad\beta=1,\qquad\alpha=(0\mathbf{1}_{9}^{\top},0.4\mathbf{1}_{6}^{\top},0.2\mathbf{1}_{6}^{\top})^{\top}.
```

### 185 iv-lin-2024-wit-code-v1 4

```math
\gamma_{\mathrm{code\_case\_2}}=0.15\mathbf{1}_{21}.
```

### 186 iv-lin-2024-wit-code-v1 5

```math
\gamma_{\mathrm{code\_case\_1}}=0.4\mathbf{1}_{21}.
```

### 187 iv-lin-2024-wit-code-v1 6

```math
D_i=Z_i^{\top}\gamma+\eta_i.
```

### 188 iv-lin-2024-wit-code-v1 7

```math
Y_i=\beta D_i+Z_i^{\top}\alpha+\varepsilon_i.
```

### 189 iv-qiu-2021-principal-stratum-poisson-v1 0

```math
X\sim \mathcal{N}_{p}(0,\Sigma)
```

### 190 iv-qiu-2021-principal-stratum-poisson-v1 1

```math
\Sigma_{jk}=1\cdot 0.5^{\lvert j-k\rvert}
```

### 191 iv-qiu-2021-principal-stratum-poisson-v1 2

```math
\mathrm{gamma1}_{j}=\mathrm{gamma2}_{j}=j^{-2}
```

### 192 iv-qiu-2021-principal-stratum-poisson-v1 3

```math
Z\mid X\sim \mathrm{Bernoulli}(\mathrm{expit}(X'\gamma_{1}))
```

### 193 iv-qiu-2021-principal-stratum-poisson-v1 4

```math
p=200.
```

### 194 iv-qiu-2021-principal-stratum-poisson-v1 5

```math
e_{\mathrm{d0}},e_{\mathrm{d1}}\overset{\mathrm{iid}}{\sim} \mathcal{N}(0,1)
```

### 195 iv-qiu-2021-principal-stratum-poisson-v1 6

```math
D_{0}=I(X'\gamma_{2}-1+e_{\mathrm{d0}}\geq 0)
```

### 196 iv-qiu-2021-principal-stratum-poisson-v1 7

```math
D_{1}^{\ast}=I(X'\gamma_{2}+1+e_{\mathrm{d1}}\geq 0)
```

### 197 iv-qiu-2021-principal-stratum-poisson-v1 8

```math
D_{1}=\max(D_{1}^{\ast},D_{0})
```

### 198 iv-qiu-2021-principal-stratum-poisson-v1 9

```math
D=Z D_{1}+(1-Z)D_{0}.
```

### 199 iv-qiu-2021-principal-stratum-poisson-v1 10

```math
e_{0}\sim \mathcal{N}(0,1)
```

### 200 iv-qiu-2021-principal-stratum-poisson-v1 11

```math
\beta_{j}=2\cdot j^{-2}
```

### 201 iv-qiu-2021-principal-stratum-poisson-v1 12

```math
K_{11}\sim \mathrm{Poisson}(\lambda_{11})
```

### 202 iv-qiu-2021-principal-stratum-poisson-v1 13

```math
K_{00}\sim \mathrm{Poisson}(0.5)
```

### 203 iv-qiu-2021-principal-stratum-poisson-v1 14

```math
B=X'\beta+e_{0}+K_{11}\cdot I(D_{0}=1)+K_{00}\cdot I(D_{1}=0)
```

### 204 iv-qiu-2021-principal-stratum-poisson-v1 15

```math
Y_{0}=B
```

### 205 iv-qiu-2021-principal-stratum-poisson-v1 16

```math
Y_{1}=1+B
```

### 206 iv-qiu-2021-principal-stratum-poisson-v1 17

```math
Y=D Y_{1}+(1-D)Y_{0}.
```

### 207 iv-qiu-2021-principal-stratum-poisson-v1 18

```math
\text{ source } \alpha_{0}=1.
```

### 208 iv-wang-2018-average-wald-v1 0

```math
X=(1,X_{2})
```

### 209 iv-wang-2018-average-wald-v1 1

```math
U\sim \mathrm{Bernoulli}(0.5)
```

### 210 iv-wang-2018-average-wald-v1 2

```math
\mathrm{Individuals} \text{ iid }.
```

### 211 iv-wang-2018-average-wald-v1 3

```math
Z\mid X,U \sim \mathrm{Bernoulli}(\mathrm{expit}(0.1-0.5 X_{2})).
```

### 212 iv-wang-2018-average-wald-v1 4

```math
\delta(X)=\tanh(0.1+0.5 X_{2}), \mathrm{deltaD}(X)=\tanh(-0.5 X_{2}), OPD(X)=\exp(-0.5+X_{2}), OPY(X)=\exp(-X_{2}). \alpha=(0.1,0.5)
```

### 213 iv-wang-2018-average-wald-v1 5

```math
\beta=(0,-0.5)
```

### 214 iv-wang-2018-average-wald-v1 6

```math
\gamma=(0.1,-0.5)
```

### 215 iv-wang-2018-average-wald-v1 7

```math
\eta=(-0.5,1)
```

### 216 iv-wang-2018-average-wald-v1 8

```math
\zeta=(0,-1)
```

### 217 iv-wang-2018-average-wald-v1 9

```math
\kappa=0.1.
```

### 218 iv-wang-2018-average-wald-v1 10

```math
\mathrm{Let} B=q(2-d)+d. F(d,q)=[B-\sqrt{B^{2}+4q(1-d)(1-q)}]/[2(q-1)]=2q(1-d)/[B+\sqrt{B^{2}+4q(1-d)(1-q)}]
```

### 219 iv-wang-2018-average-wald-v1 11

```math
\mathrm{For} q=1, F(d,1)=(1-d)/2. \mathrm{p0D}=F(\mathrm{deltaD},OPD)
```

### 220 iv-wang-2018-average-wald-v1 12

```math
\mathrm{p0Y}=F(\mathrm{deltaD}\cdot \delta,OPY).
```

### 221 iv-wang-2018-average-wald-v1 13

```math
D\mid Z,X,U \sim \mathrm{Bernoulli}(\mathrm{p0D}(X)+Z \mathrm{deltaD}(X)+0.1(2U-1)).
```

### 222 iv-wang-2018-average-wald-v1 14

```math
\mathrm{rD}=\mathrm{p0D}+0.1(2U-1)
```

### 223 iv-wang-2018-average-wald-v1 15

```math
\mathrm{rY}=\mathrm{p0Y}+0.1(2U-1), t=\delta(X)
```

### 224 iv-wang-2018-average-wald-v1 16

```math
\text{ independent } V_{Z},V_{D},V_{Y}\sim \mathrm{Uniform}(0,1)
```

### 225 iv-wang-2018-average-wald-v1 17

```math
g_{a}=\mathrm{rY}-t\cdot \mathrm{rD}+\text{ a }\cdot t, Y(\text{ a })=1\{V_{Y}<g_{a}\}
```

### 226 iv-wang-2018-average-wald-v1 18

```math
\mathrm{Observe} D=D(Z)
```

### 227 iv-wang-2018-average-wald-v1 19

```math
Y=Y(D)
```

### 228 iv-wang-2018-average-wald-v1 20

```math
\mathrm{Then} \mathbb{E}[Y|Z,X,U]=g_{0}+P(D=1|Z,X,U)\cdot (g_{1}-g_{0})=\mathrm{rY}+Z \mathrm{deltaD}\cdot t. \mathbb{E}[Y(1)-Y(0)|X,U]=t.
```

### 229 iv-wang-2018-average-wald-v1 21

```math
\Delta_{W}=\int_{-1}^{-0.5} \tanh(0.1+0.5x) \mathrm{dx} + \int_{0.5}^{1} \tanh(0.1+0.5x) \mathrm{dx}
```

### 230 iv-wang-2021-binary-complier-odds-v1 0

```math
X\sim \mathrm{Uniform}(-1,1)
```

### 231 iv-wang-2021-binary-complier-odds-v1 1

```math
Z\mid X=x\sim \mathrm{Bernoulli}(\mathrm{expit}(0.1-x)).
```

### 232 iv-wang-2021-binary-complier-odds-v1 2

```math
q=\mathrm{expit}(-0.4+0.8\cdot x)
```

### 233 iv-wang-2021-binary-complier-odds-v1 3

```math
P(CO\mid x)=q
```

### 234 iv-wang-2021-binary-complier-odds-v1 4

```math
P(AT\mid x)=(1-q)\cdot q
```

### 235 iv-wang-2021-binary-complier-odds-v1 5

```math
P(NT\mid x)=(1-q)^{2}
```

### 236 iv-wang-2021-binary-complier-odds-v1 6

```math
D=Z \text{ on } CO, D=1 \text{ on } AT, D=0 \text{ on } NT.
```

### 237 iv-wang-2021-binary-complier-odds-v1 7

```math
\delta=\tanh(-x)
```

### 238 iv-wang-2021-binary-complier-odds-v1 8

```math
OP=\exp(-0.4+x)
```

### 239 iv-wang-2021-binary-complier-odds-v1 9

```math
f_{1}=f_{0}+\delta
```

### 240 iv-wang-2021-binary-complier-odds-v1 10

```math
f_{0}\cdot f_{1}/((1-f_{0})\cdot (1-f_{1}))=OP
```

### 241 iv-wang-2021-binary-complier-odds-v1 11

```math
Y\mid CO,D,x\sim \mathrm{Bernoulli}(\mathrm{fD})
```

### 242 iv-wang-2021-binary-complier-odds-v1 12

```math
Y\mid AT,x\sim \mathrm{Bernoulli}(q)
```

### 243 iv-wang-2021-binary-complier-odds-v1 13

```math
Y\mid NT,x\sim \mathrm{Bernoulli}(q)
```

### 244 iv-ye-2024-genius-heteroskedastic-v1-conflict-8dd1770580 0

```math
Z_{j} \text{ independently } \sim \mathrm{Binomial}(2,0.5), j=1,\ldots ,100.
```

### 245 iv-ye-2024-genius-heteroskedastic-v1-conflict-8dd1770580 1

```math
h_{2}=0.2,\kappa=1.
```

### 246 iv-ye-2024-genius-heteroskedastic-v1-conflict-8dd1770580 2

```math
U\sim \mathcal{N}(0,0.6\cdot (1-h_{2}))
```

### 247 iv-ye-2024-genius-heteroskedastic-v1-conflict-8dd1770580 3

```math
\varepsilon_{A},\varepsilon_{Y} \text{ independently } \sim \mathcal{N}(0,0.4\cdot (1-h_{2}))
```

### 248 iv-ye-2024-genius-heteroskedastic-v1-conflict-8dd1770580 4

```math
A=\sum_{j} \gamma_{j} Z_{j} + U + (1+\sum_{j} \delta_{j} Z_{j})\cdot \varepsilon_{A}.
```

### 249 iv-ye-2024-genius-heteroskedastic-v1-conflict-8dd1770580 5

```math
Y=0.4\cdot A+\sum_{j} \alpha_{j} Z_{j}+U+\varepsilon_{Y}.
```

### 250 iv-ye-2024-genius-heteroskedastic-v1-conflict-8dd1770580 6

```math
S_{1}:\alpha_{j}=0
```

### 251 iv-ye-2024-genius-heteroskedastic-v1-conflict-8dd1770580 7

```math
S_{2}:\alpha_{j}\sim \mathcal{N}(\sqrt{\mathrm{tau0}_{\mathrm{squared}}},\mathrm{tau0}_{\mathrm{squared}}) \text{ where } \mathrm{tau0}_{\mathrm{squared}}=h_{2}/(1.5\cdot m)
```

### 252 iv-ye-2024-genius-heteroskedastic-v1-conflict-8dd1770580 8

```math
S_{3}:\alpha_{j}=\gamma_{j}/2.
```

### 253 ate-athey-imbens-wager-2018-arb-v1 0

```math
X_{i} = C_{i} + Z_{i}, \text{ with } C_{i} \in \{0, \delta\}
```

### 254 ate-athey-imbens-wager-2018-arb-v1 1

```math
Z_{i} \sim \mathcal{N}_{p}(0, I_{p})
```

### 255 ate-athey-imbens-wager-2018-arb-v1 2

```math
W_{i} \sim \mathrm{Bernoulli}(0.5)
```

### 256 ate-athey-imbens-wager-2018-arb-v1 3

```math
P(C_{i}=0 | W_{i}=0)=0.8 \text{ and } P(C_{i}=0 | W_{i}=1)=0.2.
```

### 257 ate-athey-imbens-wager-2018-arb-v1 4

```math
P(C_{i}=0)=0.5
```

### 258 ate-athey-imbens-wager-2018-arb-v1 5

```math
P(W_{i}=1 \mid  C_{i}=0)=0.2
```

### 259 ate-athey-imbens-wager-2018-arb-v1 6

```math
P(W_{i}=1 \mid  C_{i}=\delta)=0.8
```

### 260 ate-athey-imbens-wager-2018-arb-v1 7

```math
Y_{i} = X_{i}^{T} \beta+ W_{i} + \varepsilon_{i}
```

### 261 ate-athey-imbens-wager-2018-arb-v1 8

```math
\varepsilon_{i} \sim \mathcal{N}(0,1). Z_{i} \sim \mathcal{N}_{p}(0,I_{p}), \text{ with } \text{ iid } \mathrm{standard}-\mathrm{normal} \text{ coordinates }
```

### 262 ate-athey-imbens-wager-2018-arb-v1 9

```math
\delta= (4 / \sqrt{n}) \cdot  1_{p}.
```

### 263 ate-athey-imbens-wager-2018-arb-v1 10

```math
\delta_{j} = (40 / \sqrt{n}) \cdot  1\{j = 1 \bmod  10\}, \text{ for } j=1,\ldots ,p.
```

### 264 ate-athey-imbens-wager-2018-arb-v1 11

```math
\mathrm{Each} \text{ vector } \text{ is } \mathrm{rescaled} \text{ to } ||\beta||_{2}=2.
```

### 265 ate-athey-imbens-wager-2018-arb-v1 12

```math
Y_{i}(w)=X_{i}^{T} \beta+ w + \varepsilon_{i}, w \in \{0,1\}
```

### 266 ate-athey-imbens-wager-2018-arb-v1 13

```math
\mathrm{ATE}=\mathbb{E}[Y_{i}(1)-Y_{i}(0)]=1.
```

### 267 ate-athey-imbens-wager-2018-arb-v2 0

```math
\mathrm{For} k=1,\ldots ,20, c_{k} \sim \mathcal{N}_{p}(0, I_{p})
```

### 268 ate-athey-imbens-wager-2018-arb-v2 1

```math
K_{i} \sim \mathrm{Uniform}\{1,\ldots ,20\}
```

### 269 ate-athey-imbens-wager-2018-arb-v2 2

```math
C_{i}=c_{K_{i}}
```

### 270 ate-athey-imbens-wager-2018-arb-v2 3

```math
W_{i} \mid  K_{i}=k \sim \mathrm{Bernoulli}(\eta) \text{ for } k=1,\ldots ,10
```

### 271 ate-athey-imbens-wager-2018-arb-v2 4

```math
W_{i} \mid  K_{i}=k \sim \mathrm{Bernoulli}(1-\eta) \text{ for } k=11,\ldots ,20
```

### 272 ate-athey-imbens-wager-2018-arb-v2 5

```math
Z_{i} \sim \mathcal{N}_{p}(0,I_{p})
```

### 273 ate-athey-imbens-wager-2018-arb-v2 6

```math
X_{i}=C_{i}+Z_{i}
```

### 274 ate-athey-imbens-wager-2018-arb-v2 7

```math
\mathrm{The} \text{ source } \mathrm{writes} Z_{i}\sim \mathcal{N}(0,I_{p})
```

### 275 ate-athey-imbens-wager-2018-arb-v2 8

```math
\varepsilon_{i} \sim \mathcal{N}(0,1), \mathrm{so} \text{ variance }=1
```

### 276 ate-athey-imbens-wager-2018-arb-v2 9

```math
Y_{i} = X_{i}^{T} \beta+ W_{i} + \varepsilon_{i}, \mathrm{corresponding} \text{ to } \text{ the } \text{ source } \mathrm{notation} Y_{i}=(C_{i}+Z_{i}) \beta+ W_{i} + \varepsilon_{i}.
```

### 277 ate-athey-imbens-wager-2018-arb-v2 10

```math
\mathrm{Raw} \beta_{j} \mathrm{proportional} \text{ to } j^{-1/2}, j=1,\ldots ,p
```

### 278 ate-athey-imbens-wager-2018-arb-v2 11

```math
\mathrm{rescale} \text{ to } ||\beta||_{2}=3.
```

### 279 ate-athey-imbens-wager-2018-arb-v2 12

```math
\mathrm{Raw} \beta_{j} \mathrm{proportional} \text{ to } 1/(j+9), j=1,\ldots ,p
```

### 280 ate-athey-imbens-wager-2018-arb-v2 13

```math
\mathrm{rescale} \text{ to } ||\beta||_{2}=3.
```

### 281 ate-athey-imbens-wager-2018-arb-v2 14

```math
\mathrm{rescale} \text{ to } ||\beta||_{2}=3.
```

### 282 ate-athey-imbens-wager-2018-arb-v2 15

```math
\mathrm{rescale} \text{ to } ||\beta||_{2}=3.
```

### 283 ate-athey-imbens-wager-2018-arb-v2 16

```math
\mathrm{Structural} \mathrm{interpretation} \text{ for } w \in \{0,1\}: Y_{i}(w)=X_{i}^{T} \beta+w+\varepsilon_{i}, \mathrm{so} \mathrm{ATE}=\mathbb{E}[Y(1)-Y(0)]=1.
```

### 284 ate-athey-imbens-wager-2018-arb-v3 0

```math
X_{i} \sim \mathcal{N}_{p}(0,\Sigma)
```

### 285 ate-athey-imbens-wager-2018-arb-v3 1

```math
\Sigma_{jk}=\rho^{\lvert j-k\rvert}
```

### 286 ate-athey-imbens-wager-2018-arb-v3 2

```math
\mathrm{Table} 3 \mathrm{uses} \rho=0.5, p=2000.
```

### 287 ate-athey-imbens-wager-2018-arb-v3 3

```math
\theta_{i} = X_{i}^{T} \beta_{W} + \varepsilon_{i1}.
```

### 288 ate-athey-imbens-wager-2018-arb-v3 4

```math
W_{i} \mid  \theta_{i} \sim \mathrm{Bernoulli}(1/(1+\exp(\theta_{i}))) = \mathrm{Bernoulli}(\mathrm{expit}(-\theta_{i})).
```

### 289 ate-athey-imbens-wager-2018-arb-v3 5

```math
Y_{i} = X_{i}^{T} \beta_{Y} + 0.5 W_{i} + \varepsilon_{i2}.
```

### 290 ate-athey-imbens-wager-2018-arb-v3 6

```math
\beta_{Y,j} \mathrm{proportional} \text{ to } 1/j^{2} \text{ for } j=1,\ldots ,p
```

### 291 ate-athey-imbens-wager-2018-arb-v3 7

```math
\beta_{W,j} \mathrm{proportional} \text{ to } 1/j^{2} \text{ for } j=1,\ldots ,p
```

### 292 ate-athey-imbens-wager-2018-arb-v3 8

```math
\beta_{W,j} \mathrm{proportional} \text{ to } 1/\sqrt{j} \text{ for } j=1,\ldots ,p
```

### 293 ate-athey-imbens-wager-2018-arb-v3 9

```math
Y_{i}(w)=X_{i}^{T} \beta_{Y}+0.5 w+\varepsilon_{i2}
```

### 294 ate-athey-imbens-wager-2018-arb-v3 10

```math
\mathrm{ATE}=\mathbb{E}[Y_{i}(1)-Y_{i}(0)]=0.5.
```

### 295 ate-athey-imbens-wager-2018-arb-v4 0

```math
X_{i} \sim \mathcal{N}_{p}(0,\Sigma)
```

### 296 ate-athey-imbens-wager-2018-arb-v4 1

```math
\Sigma_{ij}=\rho^{\lvert i-j\rvert}
```

### 297 ate-athey-imbens-wager-2018-arb-v4 2

```math
p=2000.
```

### 298 ate-athey-imbens-wager-2018-arb-v4 3

```math
X_{i1}=Z_{i1}
```

### 299 ate-athey-imbens-wager-2018-arb-v4 4

```math
X_{ij}=\rho\cdot X_{i,j-1} + \sqrt{1-\rho^{2}}\cdot Z_{ij} \text{ for } j=2,\ldots ,p, \text{ where } \mathrm{innovations} Z_{ij} \mathrm{are}\overset{\mathrm{iid}}{\sim} \mathcal{N}(0,1)
```

### 300 ate-athey-imbens-wager-2018-arb-v4 5

```math
k_{j} = (23\cdot (j-1)) \bmod  p
```

### 301 ate-athey-imbens-wager-2018-arb-v4 6

```math
\mathrm{raw}_{j} = 1/\sqrt{1+k_{j}}
```

### 302 ate-athey-imbens-wager-2018-arb-v4 7

```math
k_{j}=(23\cdot (j-1)) \bmod  p.
```

### 303 ate-athey-imbens-wager-2018-arb-v4 8

```math
\mathrm{raw}_{j} = 1/(10+k_{j})
```

### 304 ate-athey-imbens-wager-2018-arb-v4 9

```math
k_{j}=(23\cdot (j-1)) \bmod  p.
```

### 305 ate-athey-imbens-wager-2018-arb-v4 10

```math
\mathrm{raw}_{j}=10 \text{ if } k_{j}<10
```

### 306 ate-athey-imbens-wager-2018-arb-v4 11

```math
\mathrm{raw}_{j}=1 \text{ if } 10\leq k_{j}<100
```

### 307 ate-athey-imbens-wager-2018-arb-v4 12

```math
\mathrm{raw}_{j}=0 \text{ if } k_{j}\geq 100
```

### 308 ate-athey-imbens-wager-2018-arb-v4 13

```math
k_{j}=(23\cdot (j-1)) \bmod  p.
```

### 309 ate-athey-imbens-wager-2018-arb-v4 14

```math
\mathrm{raw}_{j}=1 \text{ if } k_{j}<10, \text{ otherwise } 0
```

### 310 ate-athey-imbens-wager-2018-arb-v4 15

```math
k_{j}=(23\cdot (j-1)) \bmod  p.
```

### 311 ate-athey-imbens-wager-2018-arb-v4 16

```math
W_{i} \mid  X_{i} \sim \mathrm{Bernoulli}(\mathrm{expit}(\sum_{j=1}^{100} X_{ij}/40))
```

### 312 ate-athey-imbens-wager-2018-arb-v4 17

```math
\mathrm{equivalently} P(W_{i}=1\mid X_{i})=1/[1+\exp(-\sum_{j=1}^{100} X_{ij}/40)].
```

### 313 ate-athey-imbens-wager-2018-arb-v4 18

```math
Y_{i} = X_{i}^{T} \beta_{Y} + 0.5 W_{i} + \varepsilon_{i}, \varepsilon_{i} \sim \mathcal{N}(0,1), \text{ independent } \mathrm{under} \text{ the } \mathrm{implementation} \mathrm{convention}.
```

### 314 ate-athey-imbens-wager-2018-arb-v4 19

```math
Y_{i}(w)=X_{i}^{T} \beta_{Y} + 0.5w + \varepsilon_{i}, w \in \{0,1\}
```

### 315 ate-athey-imbens-wager-2018-arb-v4 20

```math
\mathrm{ATE}=\mathbb{E}[Y_{i}(1)-Y_{i}(0)]=0.5.
```

### 316 ate-athey-imbens-wager-2018-arb-v5 0

```math
X_{i} \sim \mathcal{N}_{p}(0,I_{p})
```

### 317 ate-athey-imbens-wager-2018-arb-v5 1

```math
p=1600 \in \text{ the } \mathrm{selected} \mathrm{Table} 5 \mathrm{setting}
```

### 318 ate-athey-imbens-wager-2018-arb-v5 2

```math
\theta_{i} = \log(1 + \exp(-2 - 2 X_{i1})) / 0.915
```

### 319 ate-athey-imbens-wager-2018-arb-v5 3

```math
W_{i} \mid  X_{i} \sim \mathrm{Bernoulli}(1 - \exp(-\theta_{i}))
```

### 320 ate-athey-imbens-wager-2018-arb-v5 4

```math
\mathrm{equivalently} P(W_{i}=1\mid X_{i})= -\mathrm{expm1}(-\theta_{i}) \text{ for } \mathrm{stable} \mathrm{numeric} \mathrm{evaluation}
```

### 321 ate-athey-imbens-wager-2018-arb-v5 5

```math
Y_{i} = \sum_{j=1}^{10} X_{ij} + \theta_{i} (2 W_{i} - 1)/2 + \varepsilon_{i}
```

### 322 ate-athey-imbens-wager-2018-arb-v5 6

```math
\varepsilon_{i} \sim \mathcal{N}(0,1)
```

### 323 ate-athey-imbens-wager-2018-arb-v5 7

```math
Y_{i}(w)=\sum_{j=1}^{10} X_{ij} + \theta_{i}(2w-1)/2 + \varepsilon_{i}, w \in \{0,1\}
```

### 324 ate-athey-imbens-wager-2018-arb-v5 8

```math
Y_{i}(1)-Y_{i}(0)=\theta_{i}
```

### 325 ate-athey-imbens-wager-2018-arb-v5 9

```math
\mathrm{ATE}=\mathbb{E}[\theta(X_{1})]\approx 0.389416787118157.
```

### 326 ate-benkser-carone-vdl-gilbert-2017-dr-v1 0

```math
W_{1} \sim \mathrm{Uniform}(-2, 2)
```

### 327 ate-benkser-carone-vdl-gilbert-2017-dr-v1 1

```math
W_{2} \sim \mathrm{Bernoulli}(1/2)
```

### 328 ate-benkser-carone-vdl-gilbert-2017-dr-v1 2

```math
A \mid  W=(w_{1},w_{2}) \sim \mathrm{Bernoulli}(g_{0}(w_{1},w_{2}))
```

### 329 ate-benkser-carone-vdl-gilbert-2017-dr-v1 3

```math
g_{0}(w_{1},w_{2})=\mathrm{expit}(-w_{1} + 2\cdot w_{1}\cdot w_{2})
```

### 330 ate-benkser-carone-vdl-gilbert-2017-dr-v1 4

```math
Y \mid  A=\text{ a },W=w \sim \mathrm{Bernoulli}(\mathrm{Qbar0}(\text{ a },w))
```

### 331 ate-benkser-carone-vdl-gilbert-2017-dr-v1 5

```math
\mathrm{Qbar0}(\text{ a },w)=\mathrm{expit}(0.2\cdot \text{ a } - w_{1} + 2\cdot w_{1}\cdot w_{2})
```

### 332 ate-ding-dasgupta-2016-binary-rct-v1 0

```math
\mathrm{N}_{11}=\#\{i:Y_{i}(1)=1,Y_{i}(0)=1\}
```

### 333 ate-ding-dasgupta-2016-binary-rct-v1 1

```math
\mathrm{N}_{10}=\#\{i:Y_{i}(1)=1,Y_{i}(0)=0\}
```

### 334 ate-ding-dasgupta-2016-binary-rct-v1 2

```math
\mathrm{N}_{01}=\#\{i:Y_{i}(1)=0,Y_{i}(0)=1\}
```

### 335 ate-ding-dasgupta-2016-binary-rct-v1 3

```math
\mathrm{N}_{00}=\#\{i:Y_{i}(1)=0,Y_{i}(0)=0\}
```

### 336 ate-ding-dasgupta-2016-binary-rct-v1 4

```math
\mathrm{N}=\mathrm{N}_{11}+\mathrm{N}_{10}+\mathrm{N}_{01}+\mathrm{N}_{00}=200.
```

### 337 ate-ding-dasgupta-2016-binary-rct-v1 5

```math
\mathrm{N}_{1}=\mathrm{N}_{0}=100
```

### 338 ate-ding-dasgupta-2016-binary-rct-v1 6

```math
P(A=\text{ a })=1/\mathrm{binom}(\mathrm{N},\mathrm{N}_{1}) \text{ for } \mathrm{every} \mathrm{assignment} \text{ vector } \text{ a } \text{ with } \sum_{i} \text{ a }_{i}=\mathrm{N}_{1}.
```

### 339 ate-ding-dasgupta-2016-binary-rct-v1 7

```math
Y_{i}=A_{i} Y_{i}(1)+(1-A_{i})Y_{i}(0)
```

### 340 ate-ding-dasgupta-2016-binary-rct-v1 8

```math
\tau=\mathrm{N}^{-1} \sum_{i}[Y_{i}(1)-Y_{i}(0)]=(\mathrm{N}_{10}-\mathrm{N}_{01})/\mathrm{N}.
```

### 341 ate-huang-chan-2017-05-19-setting-2-v1 0

```math
Z_{1},\ldots ,Z_{10}\overset{\mathrm{iid}}{\sim} \mathcal{N}(0,1).
```

### 342 ate-huang-chan-2017-05-19-setting-2-v1 1

```math
X_{1}=\exp(Z_{1}/2)
```

### 343 ate-huang-chan-2017-05-19-setting-2-v1 2

```math
X_{2}=Z_{2}/(1+\exp(Z_{1}))
```

### 344 ate-huang-chan-2017-05-19-setting-2-v1 3

```math
X_{3}=(Z_{1}\cdot Z_{3}/25+3/5)^{3}
```

### 345 ate-huang-chan-2017-05-19-setting-2-v1 4

```math
X_{4},\ldots ,X_{10}=Z_{4},\ldots ,Z_{10}.
```

### 346 ate-huang-chan-2017-05-19-setting-2-v1 5

```math
p(X)=\mathrm{expit}(X_{1}-X_{2}+X_{3})
```

### 347 ate-huang-chan-2017-05-19-setting-2-v1 6

```math
A\mid X\sim \mathrm{Bernoulli}(p).
```

### 348 ate-huang-chan-2017-05-19-setting-2-v1 7

```math
Y(1)=1+Z_{1}+\varepsilon_{1}
```

### 349 ate-huang-chan-2017-05-19-setting-2-v1 8

```math
Y(0)=Z_{2}+\varepsilon_{0}
```
