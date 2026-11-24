"""Fortune in a Pot — make.fun entry.

Verified: ENTRY is 108 characters / 108 bytes, written to entry.txt
with no trailing newline, UTF-8.
entry.txt sha256: 152c3bd9d00f879e82d393e4d9eebe403150daf3d809dda6193eb0082f2305c6
Competition: u-golden-heron-44-fortune-in-a-pot-ded981e9
"""

import os

ENTRY = "You will grow one perfect new leaf this week, and your keeper will photograph it 214 times before breakfast."

def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
