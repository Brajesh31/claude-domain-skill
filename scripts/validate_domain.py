#!/usr/bin/env python3
"""Check basic DNS hostname syntax; does not verify ownership or DNS."""

from __future__ import annotations
import argparse
import re

LABEL = re.compile(r"^[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?$")

def valid_hostname(value: str) -> bool:
    value = value.rstrip(".")
    if not value or len(value) > 253 or "." not in value:
        return False
    return all(LABEL.fullmatch(label) for label in value.split("."))

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("hostname")
    args = parser.parse_args()
    if not valid_hostname(args.hostname):
        print("Invalid hostname syntax.")
        return 1
    print(f"Hostname syntax looks valid: {args.hostname.rstrip('.')}")
    print("This does not verify ownership, DNS records, TLS, or service health.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
