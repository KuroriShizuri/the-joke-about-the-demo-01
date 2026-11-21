"""The joke about the demo — make.fun entry.

Writes one one-line joke about working beside an AI coding agent to
/output/entry.txt (or $ENTRY_OUTPUT). Deterministic, stdlib-only, no network.
"""

import os

JOKE = "During the demo, my AI agent found the bug, fixed it, then apologized to the audience for my code."


def main() -> None:
    path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
