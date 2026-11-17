# GitHub math rendering probe

## Standard dollar raw escaping

$$
N_{10}=\#\{i:Y_i(1)=1\}
$$

## Doubly escaped math punctuation

$$
N_{10}=\\#\\{i:Y_i(1)=1\\}
$$

## Fenced math

```math
N_{10}=\#\{i:Y_i(1)=1\}
```

## Cardinality bars

$$
N_{10}=\left|\{i:Y_i(1)=1\}\right|
$$

## Actual Ding fenced mathematics

```math
\mathrm{N}_{11}=\#\{i:Y_{i}(1)=1,Y_{i}(0)=1\}
```

```math
\mathrm{N}_{10}=\#\{i:Y_{i}(1)=1,Y_{i}(0)=0\}
```

```math
\mathrm{N}_{01}=\#\{i:Y_{i}(1)=0,Y_{i}(0)=1\}
```

```math
\mathrm{N}_{00}=\#\{i:Y_{i}(1)=0,Y_{i}(0)=0\}
```

```math
P(A=\text{ a })=1/\mathrm{binom}(\mathrm{N},\mathrm{N}_{1}) \text{ for } \mathrm{every} \mathrm{assignment} \text{ vector } \text{ a } \text{ with } \sum_{i} \text{ a }_{i}=\mathrm{N}_{1}.
```

## Multiline original

```math
\begin{aligned}
L_{0} &= 1.5\cdot T_{00}+\varepsilon_{1} \\
U_{0} &= 1.5\cdot T_{00}+\varepsilon_{2}.
\end{aligned}
```

## Multiline flattened

```math
\begin{aligned}
L_{0} &= 1.5\cdot T_{00}+\varepsilon_{1} \\ U_{0} &= 1.5\cdot T_{00}+\varepsilon_{2}.
\end{aligned}
```

## Matrix original

```math
\begin{bmatrix}
1 & 0.25 & 0.5\\
0.25 & 1 & 0.5\\
0.5 & 0.5 & 1
\end{bmatrix}
```

## Matrix flattened

```math
\begin{bmatrix}
1 & 0.25 & 0.5\\ 0.25 & 1 & 0.5\\ 0.5 & 0.5 & 1
\end{bmatrix}
```
