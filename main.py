#!/usr/bin/env python3
"""Famous Last Words at 1 Percent — make.fun entry.

Writes one line of text: the last words a phone says as its battery
hits 1 percent, to entry.txt in the output directory.
"""

import os

TEXT = "Goodbye. My last act is deleting your search history, because some secrets should die with me."
MAX_CHARS = 199


def validated_text() -> str:
    """Return the entry text, checking it against the competition gate:
    UTF-8 text of 1 to 199 characters, not only white space, one line."""
    encoded = TEXT.encode("utf-8")
    decoded = encoded.decode("utf-8")
    if decoded != TEXT:
        raise ValueError("entry text does not round-trip through UTF-8")
    if not (1 <= len(TEXT) <= MAX_CHARS):
        raise ValueError(f"entry text must be 1-{MAX_CHARS} characters, got {len(TEXT)}")
    if not TEXT.strip():
        raise ValueError("entry text must not be only white space")
    if "\n" in TEXT or "\r" in TEXT:
        raise ValueError("entry text must be a single line")
    return TEXT


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    payload = (validated_text() + "\n").encode("utf-8")
    with open(path, "wb") as f:
        f.write(payload)
    # Read back to prove the bytes on disk are exactly the intended bytes.
    with open(path, "rb") as f:
        if f.read() != payload:
            raise IOError("written entry.txt does not match the intended bytes")


if __name__ == "__main__":
    main()
