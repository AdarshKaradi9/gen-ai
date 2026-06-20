"""Bundled, representative snapshot of the Indian market.

This data ships with the package so the toolkit runs fully offline. The levels
are representative reference values for the core Indian indices, not a live
feed; use :mod:`indian_market.fetch` for real-time quotes. The ``as_of`` label
makes clear this is bundled sample data.
"""

from __future__ import annotations

from indian_market.models import IndexQuote, MarketSnapshot

BUNDLED_AS_OF = "2026-06-19"

# Yahoo Finance ticker symbols, used by the optional live-fetch layer.
YF_SYMBOLS: dict[str, str] = {
    "NIFTY 50": "^NSEI",
    "BSE SENSEX": "^BSESN",
    "NIFTY NEXT 50": "^NSMIDCP",
    "NIFTY BANK": "^NSEBANK",
    "NIFTY IT": "^CNXIT",
    "NIFTY AUTO": "^CNXAUTO",
    "NIFTY FMCG": "^CNXFMCG",
    "NIFTY PHARMA": "^CNXPHARMA",
    "NIFTY METAL": "^CNXMETAL",
    "NIFTY ENERGY": "^CNXENERGY",
}

# (symbol, name, last, previous_close, category)
_BUNDLED: list[tuple[str, str, float, float, str]] = [
    ("NIFTY 50", "Nifty 50", 24850.10, 24710.30, "broad"),
    ("BSE SENSEX", "BSE Sensex", 81450.60, 81005.20, "broad"),
    ("NIFTY NEXT 50", "Nifty Next 50", 71200.40, 71550.10, "broad"),
    ("NIFTY BANK", "Nifty Bank", 55320.75, 55010.45, "sector"),
    ("NIFTY IT", "Nifty IT", 38900.20, 39410.80, "sector"),
    ("NIFTY AUTO", "Nifty Auto", 25140.55, 24890.10, "sector"),
    ("NIFTY FMCG", "Nifty FMCG", 56720.30, 56680.90, "sector"),
    ("NIFTY PHARMA", "Nifty Pharma", 22310.85, 22150.40, "sector"),
    ("NIFTY METAL", "Nifty Metal", 9840.15, 10020.60, "sector"),
    ("NIFTY ENERGY", "Nifty Energy", 41250.70, 41180.25, "sector"),
]


def bundled_quotes() -> list[IndexQuote]:
    """Return the bundled core index quotes."""
    return [
        IndexQuote(symbol=s, name=n, last=last, previous_close=prev, category=cat)
        for (s, n, last, prev, cat) in _BUNDLED
    ]


def bundled_snapshot() -> MarketSnapshot:
    """Return the bundled snapshot, labelled with its reference date."""
    return MarketSnapshot(
        as_of=BUNDLED_AS_OF,
        source="bundled-sample",
        currency="INR",
        quotes=bundled_quotes(),
    )
