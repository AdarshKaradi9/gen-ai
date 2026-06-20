"""High-level snapshot builder and text rendering."""

from __future__ import annotations

from indian_market.data import bundled_snapshot
from indian_market.fetch import FetchUnavailable, fetch_snapshot
from indian_market.models import MarketSnapshot


def build_snapshot(live: bool = False) -> MarketSnapshot:
    """Build a core market snapshot.

    Args:
        live: If ``True``, attempt to fetch live quotes and fall back to the
            bundled snapshot on failure. If ``False`` (default), use the
            bundled snapshot directly.
    """
    if not live:
        return bundled_snapshot()
    try:
        return fetch_snapshot()
    except FetchUnavailable:
        return bundled_snapshot()


def _fmt_quote_line(symbol: str, last: float, change: float, pct: float) -> str:
    arrow = "▲" if pct > 0 else ("▼" if pct < 0 else "■")
    return f"  {symbol:<16} {last:>12,.2f}  {arrow} {change:>+9.2f} ({pct:>+6.2f}%)"


def render_text(snapshot: MarketSnapshot) -> str:
    """Render a snapshot as a human-readable terminal report."""
    lines: list[str] = []
    lines.append("=" * 56)
    lines.append("  INDIAN MARKET — CORE SNAPSHOT")
    lines.append(f"  as of {snapshot.as_of}  |  source: {snapshot.source}  |  {snapshot.currency}")
    lines.append("=" * 56)

    lines.append("\n  Broad market")
    for q in snapshot.broad():
        lines.append(_fmt_quote_line(q.symbol, q.last, q.change, q.change_pct))

    lines.append("\n  Sectors")
    for q in snapshot.sectors():
        lines.append(_fmt_quote_line(q.symbol, q.last, q.change, q.change_pct))

    breadth = snapshot.breadth()
    lines.append(
        f"\n  Breadth: {breadth['advances']} advancing / "
        f"{breadth['declines']} declining / {breadth['unchanged']} flat"
    )

    gainers = ", ".join(f"{q.symbol} ({q.change_pct:+.2f}%)" for q in snapshot.top_gainers())
    losers = ", ".join(f"{q.symbol} ({q.change_pct:+.2f}%)" for q in snapshot.top_losers())
    lines.append(f"  Top gainers: {gainers}")
    lines.append(f"  Top losers:  {losers}")
    lines.append("=" * 56)
    return "\n".join(lines)
