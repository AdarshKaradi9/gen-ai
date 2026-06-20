# Indian Market — Core Snapshot

A small, **offline-first** Python toolkit that produces a concise *core snapshot*
of the Indian stock market: the headline broad-market indices, the key sector
indices, top movers, and overall market breadth.

It ships with a representative bundled snapshot so it runs anywhere with zero
dependencies, and an optional live-fetch layer (`yfinance`) that pulls real
quotes when network access is available — falling back to the bundled data
gracefully if not.

> Part of the *Generative AI Collabs* repository.

## What's in a snapshot

- **Broad market:** Nifty 50, BSE Sensex, Nifty Next 50
- **Sectors:** Bank, IT, Auto, FMCG, Pharma, Metal, Energy
- **Derived views:** absolute & % change per index, market breadth
  (advances/declines), top gainers and top losers

## Quick start

No installation required — the core toolkit uses only the standard library.

```bash
# Text report (uses bundled snapshot)
python3 -m indian_market.cli

# JSON output
python3 -m indian_market.cli --format json

# Try live quotes (falls back to bundled data if unavailable)
python3 -m indian_market.cli --live

# Write to a file
python3 -m indian_market.cli --format json -o snapshot.json
```

### Install (optional)

```bash
pip install -e .          # installs the `indian-market-snapshot` command
pip install -e ".[live]"  # also installs yfinance for live quotes
```

## Library usage

```python
from indian_market import build_snapshot

snap = build_snapshot(live=False)   # set live=True to attempt a real fetch
print(snap.breadth())               # {'advances': 7, 'declines': 3, 'unchanged': 0}
for q in snap.top_gainers():
    print(q.symbol, q.change_pct)
print(snap.to_dict())               # JSON-ready dict
```

## Live data

The `--live` flag (and `build_snapshot(live=True)`) attempts to fetch real
quotes via [`yfinance`](https://pypi.org/project/yfinance/) for the indices
listed in `indian_market/data.py` (`YF_SYMBOLS`). If `yfinance` is missing or
the network is unavailable, a `FetchUnavailable` is raised internally and the
toolkit transparently falls back to the bundled snapshot.

> The bundled levels are representative reference values for documentation and
> offline use — **not** a live feed. Use `--live` for real-time data.

## Project layout

```
indian_market/
  __init__.py    # public API: IndexQuote, MarketSnapshot, build_snapshot
  models.py      # dataclasses + derived metrics (change, breadth, movers)
  data.py        # bundled snapshot + Yahoo Finance symbol map
  fetch.py       # optional live-fetch layer (yfinance), graceful fallback
  snapshot.py    # build_snapshot() + text rendering
  cli.py         # command-line interface
tests/
  test_snapshot.py
```

## Tests

```bash
pip install pytest
pytest
```
