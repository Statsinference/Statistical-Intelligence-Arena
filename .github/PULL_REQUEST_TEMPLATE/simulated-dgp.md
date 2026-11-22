## StatArena data contribution

**Track** · Simulated DGP

**Case file** · [Link the single case Markdown file changed by this PR.]

**Summary** · [State the question, target and what the design tests.]

**Materials** · [Link shareable sources. Name any materials available through the agreed private review channel.]

## Causal design preview

### DAG

<!-- Replace the example with your case's DAG arrows. Use the same arrow directions and IDs as both edge lists in the case. -->

```mermaid
flowchart LR
    X["X (exposure)"] --> Y["Y (outcome)"]
```

### Structural equations

<!-- Replace the example with all display-math blocks from the case's Structural equations subsection. Keep their contents and order. -->

```math
Y = f(X, \varepsilon_Y)
```

## Checklist

- [ ] This PR adds or updates one Markdown proposal under `website/data-submissions/simulated-dgp/submissions/`.
- [ ] The preview DAG shows the same arrows as the case's DAG edges and structural parents.
- [ ] The preview contains every structural equation from the case in the same order.
- [ ] I checked sharing permissions and kept protected values in the agreed review channel.
