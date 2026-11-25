#!/usr/bin/env python3
"""The Most Boring Object, Reviewed in One Line.

Writes the one-line review to /output/entry.txt and prints it.
Revision 2 (final): doorstop review. The joke is the object's own
dullness - it holds one door open for years, asks for nothing, and
its only reward is being kicked daily. True, specific, lands fast.
"""

import os

ENTRY = "Five stars for the doorstop: it has held the same door open since 2019, asks for nothing, and gets kicked for it every single day."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
