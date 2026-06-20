"""Command-line interface for the Indian market core snapshot."""

from __future__ import annotations

import argparse
import json
import sys

from indian_market.snapshot import build_snapshot, render_text


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="indian-market-snapshot",
        description="Produce a core snapshot of the Indian stock market.",
    )
    parser.add_argument(
        "--live",
        action="store_true",
        help="Attempt to fetch live quotes (requires yfinance + network); "
        "falls back to bundled data on failure.",
    )
    parser.add_argument(
        "--format",
        choices=("text", "json"),
        default="text",
        help="Output format (default: text).",
    )
    parser.add_argument(
        "-o",
        "--output",
        help="Write output to a file instead of stdout.",
    )
    args = parser.parse_args(argv)

    snapshot = build_snapshot(live=args.live)

    if args.format == "json":
        rendered = json.dumps(snapshot.to_dict(), indent=2)
    else:
        rendered = render_text(snapshot)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as fh:
            fh.write(rendered + "\n")
    else:
        print(rendered)

    return 0


if __name__ == "__main__":
    sys.exit(main())
