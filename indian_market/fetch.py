"""Optional live-fetch layer for real Indian market quotes.

Uses ``yfinance`` when it is installed and network access is available. Any
failure (missing dependency, no network, bad response) raises
:class:`FetchUnavailable`, which callers can catch to fall back to the bundled
snapshot.
"""

from __future__ import annotations

from indian_market.data import YF_SYMBOLS
from indian_market.models import IndexQuote, MarketSnapshot


class FetchUnavailable(RuntimeError):
    """Raised when live quotes cannot be retrieved."""


def fetch_quotes() -> list[IndexQuote]:
    """Fetch live quotes for the core indices.

    Raises:
        FetchUnavailable: if ``yfinance`` is missing or the fetch fails.
    """
    try:
        import yfinance  # type: ignore
    except ImportError as exc:  # pragma: no cover - depends on environment
        raise FetchUnavailable(
            "yfinance is not installed; install it for live quotes "
            "(pip install yfinance)"
        ) from exc

    from indian_market.data import _BUNDLED

    category_by_symbol = {s: cat for (s, _n, _l, _p, cat) in _BUNDLED}
    name_by_symbol = {s: n for (s, n, _l, _p, _cat) in _BUNDLED}

    quotes: list[IndexQuote] = []
    for label, yf_symbol in YF_SYMBOLS.items():
        try:
            ticker = yfinance.Ticker(yf_symbol)
            hist = ticker.history(period="2d")
            if hist.empty or len(hist) < 1:
                continue
            last = float(hist["Close"].iloc[-1])
            prev = float(hist["Close"].iloc[-2]) if len(hist) >= 2 else last
        except Exception:  # pragma: no cover - network/library variability
            continue
        quotes.append(
            IndexQuote(
                symbol=label,
                name=name_by_symbol.get(label, label),
                last=round(last, 2),
                previous_close=round(prev, 2),
                category=category_by_symbol.get(label, "broad"),
            )
        )

    if not quotes:
        raise FetchUnavailable("no live quotes could be retrieved")
    return quotes


def fetch_snapshot() -> MarketSnapshot:
    """Build a snapshot from live quotes.

    Raises:
        FetchUnavailable: if live quotes cannot be retrieved.
    """
    return MarketSnapshot.now(source="yfinance", quotes=fetch_quotes())
