"""The Houseplant Out-of-Office — make.fun entry.

Writes a single original one-line out-of-office auto-reply, as if a
houseplant sent it, to /output/entry.txt. Deterministic, no network.
"""

ENTRY = "Out of office: I'm a cactus. You haven't watered me since 2023 and I'm still alive. Your email can wait."


def main() -> None:
    import os

    # Gate: the entry must be 1-120 characters of non-whitespace text.
    assert 1 <= len(ENTRY) <= 120, f"entry is {len(ENTRY)} chars, gate is 1-120"
    assert ENTRY.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
