# n=1 — health optimizer mockups

Concept mockups for a health app built around n-of-1 experimentation rather than
passive tracking. Six mobile screens, rendered at a true 390×844 viewport.

## Files

| File | What it is |
|---|---|
| `n1-health-optimizer.html` | Source. Ships without `<html>`/`<head>`/`<body>` because the Artifact host supplies them. |
| `n1-health-optimizer.standalone.html` | Generated. **Open this one in a browser** — double-click it, no server needed. |
| `preview/screen-01…06.png` | Each screen on its own. |
| `preview/full-light.png`, `preview/full-dark.png` | The whole page in both themes. |
| `build-standalone.sh` | Regenerates the standalone file from the source. |

After editing `n1-health-optimizer.html`, run `sh build-standalone.sh` so the
standalone copy doesn't drift.

## Screens

1. **Today** — one decision per day; readiness decomposed into the inputs that moved it
2. **Why** — causal ledger as a forest plot: effect size, 95% CI, n; null results kept visible
3. **Trials** — randomized, blinded n-of-1 trials; interim results marked unactionable
4. **Labs** — blood work overlaid on wearable data; personal vs. population reference range
5. **Context** — illness, travel and cycle re-baseline the model instead of breaking a streak
6. **One record** — sources merged with visible conflict arbitration

Not a medical device. All figures are illustrative.
