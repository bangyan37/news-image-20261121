"""Write the 21 November 2026 world-news image to the output directory.

The repository holds the finished newspaper image as entry.png (JPEG
bytes, as the competition allows: 44 stories, 7 regions, 3 leads, a
UTC timeline and a markets strip for Saturday 21 November 2026).
This program simply copies it, byte for byte, so two runs always
produce identical output.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
IMAGE = HERE / "entry.png"


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.png"
    shutil.copyfile(IMAGE, target)
    if target.stat().st_size != IMAGE.stat().st_size:
        raise RuntimeError("output image size mismatch")


if __name__ == "__main__":
    main()
