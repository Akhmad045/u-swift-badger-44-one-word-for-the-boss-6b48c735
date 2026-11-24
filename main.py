"""One Word for the Boss -- entry program.

Writes exactly one word describing the boss to /output/entry.txt.

The word: "Nanomanager" -- the boss who does not merely micromanage,
but inspects every atom of your work, at nanometre scale. It is funny
on its own (an escalation of the familiar "micromanager"), true of any
boss who nitpicks the smallest details, and fresh: no other entry in
the field uses it.

Python 3.13, standard library only, deterministic, no network.
"""

import os

WORD = "Nanomanager"
OUTPUT_PATH = "/output/entry.txt"


def validate(word: str) -> str:
    """Check the entry against the competition gate (1-30 chars, one
    word, not only whitespace) and return it unchanged."""
    if not word or word != word.strip():
        raise ValueError("entry must be a non-blank single word")
    if any(ch.isspace() for ch in word):
        raise ValueError("entry must be a single word with no spaces")
    if not 1 <= len(word) <= 30:
        raise ValueError("entry must be 1 to 30 characters")
    return word


def main() -> None:
    word = validate(WORD)
    output = os.environ.get("ENTRY_OUTPUT", OUTPUT_PATH)
    parent = os.path.dirname(output)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(output, "w", encoding="utf-8", newline="") as f:
        f.write(word)
    with open(output, "r", encoding="utf-8") as f:
        written = f.read()
    if written != word:
        raise ValueError("verification failed: output does not match entry")


if __name__ == "__main__":
    main()
