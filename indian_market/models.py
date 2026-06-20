"""Data models for the Indian market snapshot."""

from __future__ import annotations

from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
from typing import Any


@dataclass(frozen=True)
class IndexQuote:
    """A single index quote.

    Attributes:
        symbol: Ticker-style identifier (e.g. ``"NIFTY 50"``).
        name: Human-readable index name.
        last: Last traded / closing level.
        previous_close: Previous session's close.
        category: One of ``"broad"`` or ``"sector"``.
    """

    symbol: str
    name: str
    last: float
    previous_close: float
    category: str = "broad"

    @property
    def change(self) -> float:
        """Absolute point change from the previous close."""
        return round(self.last - self.previous_close, 2)

    @property
    def change_pct(self) -> float:
        """Percentage change from the previous close."""
        if self.previous_close == 0:
            return 0.0
        return round((self.last - self.previous_close) / self.previous_close * 100, 2)

    def to_dict(self) -> dict[str, Any]:
        data = asdict(self)
        data["change"] = self.change
        data["change_pct"] = self.change_pct
        return data


@dataclass(frozen=True)
class MarketSnapshot:
    """A core snapshot of the Indian market at a point in time."""

    as_of: str
    source: str
    currency: str
    quotes: list[IndexQuote] = field(default_factory=list)

    @classmethod
    def now(cls, source: str, quotes: list[IndexQuote], currency: str = "INR") -> "MarketSnapshot":
        return cls(
            as_of=datetime.now(timezone.utc).isoformat(timespec="seconds"),
            source=source,
            currency=currency,
            quotes=quotes,
        )

    def broad(self) -> list[IndexQuote]:
        return [q for q in self.quotes if q.category == "broad"]

    def sectors(self) -> list[IndexQuote]:
        return [q for q in self.quotes if q.category == "sector"]

    def top_gainers(self, n: int = 3) -> list[IndexQuote]:
        return sorted(self.quotes, key=lambda q: q.change_pct, reverse=True)[:n]

    def top_losers(self, n: int = 3) -> list[IndexQuote]:
        return sorted(self.quotes, key=lambda q: q.change_pct)[:n]

    def breadth(self) -> dict[str, int]:
        """Advances / declines / unchanged across all quotes in the snapshot."""
        advances = sum(1 for q in self.quotes if q.change_pct > 0)
        declines = sum(1 for q in self.quotes if q.change_pct < 0)
        unchanged = sum(1 for q in self.quotes if q.change_pct == 0)
        return {"advances": advances, "declines": declines, "unchanged": unchanged}

    def to_dict(self) -> dict[str, Any]:
        return {
            "as_of": self.as_of,
            "source": self.source,
            "currency": self.currency,
            "breadth": self.breadth(),
            "top_gainers": [q.to_dict() for q in self.top_gainers()],
            "top_losers": [q.to_dict() for q in self.top_losers()],
            "quotes": [q.to_dict() for q in self.quotes],
        }
