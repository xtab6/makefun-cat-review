#!/usr/bin/env python3
"""Write the entry: one funny one-star cat review, one line, <200 chars."""

import os
import shutil

ENTRY = (
    'One star. He moved my sunny spot three inches to the left and '
    'called it "redecorating". I have filed a formal complaint with '
    "the sun."
)


def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    # Clean only the contents of /output; never remove the folder itself.
    for name in os.listdir(out_dir):
        path = os.path.join(out_dir, name)
        if os.path.isdir(path) and not os.path.islink(path):
            shutil.rmtree(path)
        else:
            os.unlink(path)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
