# GitHub rowspan and math test

## No blanks

<table>
<thead><tr><th>Scenario</th><th>Estimand</th><th>Definition</th><th>Value</th></tr></thead>
<tbody>
<tr><td>case1</td><td rowspan="2">ATE</td><td rowspan="2">$\mathbb{E}[Y(1)-Y(0)]$</td><td>0</td></tr>
<tr><td>case2</td><td>0.2</td></tr>
</tbody>
</table>

## Blank lines

<table>
<thead><tr><th>Scenario</th><th>Estimand</th><th>Definition</th><th>Value</th></tr></thead>
<tbody>
<tr><td>case1</td><td rowspan="2">ATE</td><td rowspan="2">

$`\frac{1}{N}\sum_{i=1}^N Y_i`$

</td><td>0</td></tr>
<tr><td>case2</td><td>0.2</td></tr>
</tbody>
</table>

## MathML

<table>
<tr><th>Scenario</th><th>Estimand</th><th>Definition</th><th>Value</th></tr>
<tr><td>case1</td><td rowspan="2">ATE</td><td rowspan="2"><math><mrow><mi>E</mi><mo>[</mo><mi>Y</mi><mo>]</mo></mrow></math></td><td>0</td></tr>
<tr><td>case2</td><td>0.2</td></tr>
</table>

## Rendered math image

<table>
<tr><th>Scenario</th><th>Estimand</th><th>Definition</th><th>Value</th></tr>
<tr><td>case1</td><td rowspan="2">ATE</td><td rowspan="2"><img alt="E[Y(1)-Y(0)]" src="https://render.githubusercontent.com/render/math?math=%5Cmathbb%7BE%7D%5BY%281%29-Y%280%29%5D"></td><td>0</td></tr>
<tr><td>case2</td><td>0.2</td></tr>
</table>
