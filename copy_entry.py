#!/usr/bin/env python3
"""Ship the pre-rendered front page to the grader's output directory.

Stdlib only. The picture itself is rendered at build time by the Pillow
program in the builder's workspace (draw_20261119.py) and committed here as
entry.png; this module only copies that file into the output directory.
It honours MAKEFUN_OUTPUT_DIR when set and falls back to /output otherwise.
No network access, no fonts, no third-party imports: it runs on a stock
python:3.13 image as `python3 main.py`.
"""
import os
import shutil
from pathlib import Path


def main():
    here = Path(__file__).resolve().parent
    src = here / "entry.png"
    if not src.is_file():
        raise SystemExit("entry.png missing next to main.py")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, out_dir / "entry.png")


if __name__ == "__main__":
    main()
