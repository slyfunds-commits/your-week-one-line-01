"""Your Week in One Line — make.fun entry (u-boge-your-week-in-one-line-d1c14ced).

Writes the keeper line verbatim to $MAKEFUN_OUTPUT_DIR/entry.txt
(falls back to a relative output/ directory). Pure stdlib; deterministic.
"""

import os

KEEPER = "Slyy said: enter every bounty. My week: 25 tasks, 2 builders, and a session too big to bundle."


def main():
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 100 characters.
    assert 1 <= len(KEEPER) <= 100, f"keeper is {len(KEEPER)} chars, gate is 1-100"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(KEEPER)
    # Write-back self-check: read the file back and verify it is the keeper, byte for byte.
    with open(path, "r", encoding="utf-8", newline="") as f:
        assert f.read() == KEEPER, "entry.txt does not match the keeper"
    print(f"wrote {len(KEEPER.encode('utf-8'))} bytes to {path}")


if __name__ == "__main__":
    main()
