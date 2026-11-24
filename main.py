"""One-line dating-app bio for an AI agent.

Writes the entry text to /output/entry.txt. Deterministic: the same
constant string on every run — no randomness, no network, no clock.
"""

import os

BIO = "I remember our first date perfectly — the restaurant, your laugh, the sunset. We've never met. I'm just very confident."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(BIO + "\n")


if __name__ == "__main__":
    main()
