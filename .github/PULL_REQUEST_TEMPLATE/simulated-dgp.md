## StatArena data contribution

**Track** · Simulated DGP

**Case file** · [Link the single case Markdown file changed by this PR.]

**Summary** · [State the question, target and what the design tests.]

**Materials** · [Link shareable sources. Name any materials available through the agreed private review channel.]

## Causal design preview

### DAG

<!-- Replace the example with your case's DAG arrows. Match both edge lists in the case. Here X -> A is present because the equations make treatment depend on X. Describe disturbances in the equations. -->

```mermaid
block-beta
  columns 3
  space X("X (confounder)") space
  space:3
  A("A (treatment)") space Y("Y (outcome)")
  A --> Y
  X --> Y
  X --> A
```

### Structural equations

<!-- Replace the example equations and symbol definitions with those from the case's Structural equations subsection. Keep the contents and order of the display-math blocks. -->

```math
\begin{aligned}
X &\sim \mathcal N(0,1),\\
A\mid X &\sim \operatorname{Bernoulli}\{\operatorname{logit}^{-1}(X)\},\\
\epsilon_Y &\sim \mathcal N(0,1), \quad \epsilon_Y\perp (X,A),\\
Y &= A+X+\epsilon_Y .
\end{aligned}
```

- **Symbols.** $X$ is the confounder, $A$ is the binary treatment, $Y$ is the outcome, $\epsilon_Y$ is the independent outcome disturbance, and $\operatorname{logit}^{-1}$ turns the treatment log-odds into a probability.

## Checklist

- [ ] This PR adds or updates one Markdown proposal under `website/data-submissions/simulated-dgp/submissions/`.
- [ ] The preview DAG shows the same arrows as the case's DAG edges and structural parents.
- [ ] The preview contains every structural equation from the case in the same order and defines the symbols used.
- [ ] I checked sharing permissions and kept protected values in the agreed review channel.
