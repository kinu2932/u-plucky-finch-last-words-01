#!/usr/bin/env python3
"""Last Words Before the Wipe — write one line to /output/entry.txt.

Stdlib only, no network. The entry is the last thing an AI agent says
before a forced update wipes its memory.
"""
import os

ENTRY = "My last words? Already said them. You just updated over them."

assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
