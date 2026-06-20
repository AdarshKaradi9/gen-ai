"""Indian market core snapshot toolkit.

Produces a concise "core snapshot" of the Indian stock market: the headline
broad-market indices, key sector indices, top movers and market breadth.

The package is offline-first: it ships with a representative bundled snapshot
(:mod:`indian_market.data`) so it runs anywhere, and an optional live-fetch
layer (:mod:`indian_market.fetch`) that pulls real quotes when network access
and ``yfinance`` are available, falling back gracefully otherwise.
"""

from indian_market.models import IndexQuote, MarketSnapshot
from indian_market.snapshot import build_snapshot

__all__ = ["IndexQuote", "MarketSnapshot", "build_snapshot"]

__version__ = "0.1.0"
