#!/usr/bin/env python3
"""news-image-20261117: write one image summing up the world's news of
Tuesday 17 November 2026 to /output/entry.png.

The picture is a classic newspaper front page (entry.png, bundled with
this program): a globe icon + "THE WORLD'S NEWS" masthead + a dark-blue
nav bar, 10 main story cards (Ukraine's Kerch Bridge strike, Trump's
Quad summit in Manila, the US chip-export loophole, the fourth Hormuz
tanker fire, five EU states' Rwanda deportation plan, the West urging
Israel to open Gaza crossings, Depardieu admitting sex assault, Japan
scrambling jets, the Houthi advance in Yemen, Nvidia's earnings after
Huang's exit), each with a numbered tag + category ribbon + image +
headline + explainer, plus 32 more stories in the "ALSO ON TUESDAY"
list in 3 columns — 42 stories in total, all reported on Tuesday
17 November 2026 — and a world-landmarks skyline strip at the bottom.
The program copies it byte-for-byte to $MAKEFUN_OUTPUT_DIR/entry.png
and verifies the size, format and dimensions (at most 1 MiB and 1024x1024).
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def image_size(path):
    """Return (width, height) of a PNG or JPEG using only the stdlib.

    PNG: width/height are big-endian uint32 at bytes 16..24 (IHDR).
    JPEG: scan markers for a Start-Of-Frame (0xC0-0xCF except 0xC4,
    0xC8, 0xCC); its segment holds height then width as uint16.
    """
    with open(path, "rb") as fh:
        head = fh.read(24)
    if head[:8] == b"\x89PNG\r\n\x1a\n":
        width = int.from_bytes(head[16:20], "big")
        height = int.from_bytes(head[20:24], "big")
        return width, height
    if head[:2] == b"\xff\xd8":
        with open(path, "rb") as fh:
            data = fh.read()
        i = 2
        while i + 9 < len(data):
            if data[i] != 0xFF:
                i += 1
                continue
            marker = data[i + 1]
            if marker in (0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7,
                          0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF):
                height = int.from_bytes(data[i + 5:i + 7], "big")
                width = int.from_bytes(data[i + 7:i + 9], "big")
                return width, height
            length = int.from_bytes(data[i + 2:i + 4], "big")
            i += 2 + length
    raise ValueError("cannot read dimensions: not a PNG or JPEG")


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(HERE, "entry.png")
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    size = os.path.getsize(dst)
    assert size <= 1_048_576, f"entry.png too large: {size} bytes (limit 1 MiB)"
    with open(dst, "rb") as fh:
        magic = fh.read(3)
    assert magic in (b"\xff\xd8\xff", b"\x89PN"), "entry.png is not a JPEG or PNG"
    width, height = image_size(dst)
    assert width <= 1024 and height <= 1024, (
        f"entry.png too big: {width}x{height} (limit 1024x1024)")
    print(f"wrote {dst} ({size} bytes, {width}x{height})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
