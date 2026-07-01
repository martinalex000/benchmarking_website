#!/usr/bin/env python3
"""Obtain an OpenReview bearer token without storing your password in .env.

The token is printed to stdout; add it to ``.env`` as ``OPENREVIEW_TOKEN``.
OpenReview session tokens expire (default login TTL is one hour; this script
requests up to one week).

Usage::

    uv run python scripts/openreview_login.py
    uv run python scripts/openreview_login.py --username you@example.com
    uv run python scripts/openreview_login.py --expires-days 7
"""

from __future__ import annotations

import argparse
import getpass
import sys
from pathlib import Path

_PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))

from backend.openreview_client import OpenReviewClient, OpenReviewError  # noqa: E402

_MAX_EXPIRES_SECONDS = 604_800  # 7 days (OpenReview API limit)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Log in to OpenReview and print a bearer token for OPENREVIEW_TOKEN"
    )
    parser.add_argument(
        "--username",
        help="OpenReview username/email (prompted if omitted)",
    )
    parser.add_argument(
        "--expires-days",
        type=float,
        default=7.0,
        help="Token lifetime in days (max 7; default 7)",
    )
    args = parser.parse_args(argv)

    username = (args.username or "").strip() or input("OpenReview username/email: ").strip()
    if not username:
        print("Username is required.", file=sys.stderr)
        return 1
    password = getpass.getpass("OpenReview password: ")
    if not password:
        print("Password is required.", file=sys.stderr)
        return 1

    expires_in = min(int(args.expires_days * 86_400), _MAX_EXPIRES_SECONDS)
    try:
        token = OpenReviewClient.login_for_token(
            username,
            password,
            expires_in=expires_in,
        )
    except OpenReviewError as exc:
        print(f"Login failed: {exc}", file=sys.stderr)
        return 1

    days = expires_in / 86_400
    print(f"# OpenReview bearer token (expires in ~{days:.1f} day(s))")
    print(f"OPENREVIEW_TOKEN={token}")
    print(
        "\nAdd the line above to your .env file. "
        "Do not commit .env. Re-run this script when the token expires.",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
