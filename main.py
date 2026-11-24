#!/usr/bin/env python3
"""Entry point for the news-image-20261123 bounty.

Reads the bundled newspaper image and writes it to /output/entry.png.
Standard library only, no network access.
Requires Python 3.13.
"""

import hashlib
import os
import sys

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "asset", "entry.png")
DST = "/output/entry.png"
MAX_BYTES = 1024 * 1024
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def fail(message):
    print(f"error: {message}", file=sys.stderr)
    raise SystemExit(1)


def main():
    if not os.path.isfile(SRC):
        fail(f"bundled image missing: {SRC}")
    with open(SRC, "rb") as handle:
        data = handle.read()
    if len(data) == 0:
        fail("bundled image is empty")
    if len(data) > MAX_BYTES:
        fail(f"bundled image is {len(data)} bytes, over the 1 MiB limit")
    if data[:8] != PNG_MAGIC:
        fail("bundled image is not a PNG file")
    if data[16:24] != b"\x00\x00\x04\x00\x00\x00\x04\x00":
        fail("bundled image is not 1024x1024")
    if len(data) < 1000:
        fail("bundled image looks truncated")
    os.makedirs(os.path.dirname(DST), exist_ok=True)
    with open(DST, "wb") as handle:
        handle.write(data)
    with open(DST, "rb") as handle:
        written = handle.read()
    if hashlib.sha256(written).hexdigest() != hashlib.sha256(data).hexdigest():
        fail("output differs from the bundled image")
    print(f"wrote {DST} ({len(written)} bytes)")


if __name__ == "__main__":
    main()
