"""Tests for the Indian market core snapshot toolkit."""

import json

from indian_market.data import bundled_snapshot
from indian_market.fetch import FetchUnavailable
from indian_market.models import IndexQuote, MarketSnapshot
from indian_market.snapshot import build_snapshot, render_text


def test_index_quote_change_math():
    q = IndexQuote("NIFTY 50", "Nifty 50", 24850.10, 24710.30)
    assert q.change == 139.80
    assert q.change_pct == 0.57


def test_index_quote_zero_previous_close_is_safe():
    q = IndexQuote("X", "X", 100.0, 0.0)
    assert q.change_pct == 0.0


def test_bundled_snapshot_has_broad_and_sectors():
    snap = bundled_snapshot()
    assert len(snap.broad()) >= 1
    assert len(snap.sectors()) >= 1
    assert snap.currency == "INR"
    assert snap.source == "bundled-sample"


def test_breadth_counts_sum_to_total():
    snap = bundled_snapshot()
    b = snap.breadth()
    assert b["advances"] + b["declines"] + b["unchanged"] == len(snap.quotes)


def test_top_gainers_are_sorted_descending():
    snap = bundled_snapshot()
    pct = [q.change_pct for q in snap.top_gainers(3)]
    assert pct == sorted(pct, reverse=True)
    assert len(pct) == 3


def test_top_losers_are_sorted_ascending():
    snap = bundled_snapshot()
    pct = [q.change_pct for q in snap.top_losers(3)]
    assert pct == sorted(pct)


def test_build_snapshot_offline_uses_bundled():
    snap = build_snapshot(live=False)
    assert snap.source == "bundled-sample"


def test_build_snapshot_live_falls_back(monkeypatch):
    import indian_market.snapshot as snapshot_mod

    def boom():
        raise FetchUnavailable("no network in test")

    monkeypatch.setattr(snapshot_mod, "fetch_snapshot", boom)
    snap = build_snapshot(live=True)
    assert snap.source == "bundled-sample"


def test_to_dict_is_json_serializable():
    snap = bundled_snapshot()
    payload = json.dumps(snap.to_dict())
    data = json.loads(payload)
    assert "quotes" in data
    assert "breadth" in data
    assert data["quotes"][0]["change_pct"] == snap.quotes[0].change_pct


def test_render_text_contains_header_and_indices():
    snap = bundled_snapshot()
    out = render_text(snap)
    assert "INDIAN MARKET — CORE SNAPSHOT" in out
    assert "NIFTY 50" in out
    assert "Breadth:" in out


def test_snapshot_now_factory():
    snap = MarketSnapshot.now("test", bundled_snapshot().quotes)
    assert snap.source == "test"
    assert "T" in snap.as_of  # ISO timestamp
