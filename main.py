"""Break Production, Own It — the one line an AI agent prints the moment
it breaks production: a brutally honest postmortem confession.

The line is written verbatim to /output/entry.txt, exactly one line,
no trailing newline, so the judged text is precisely the confession.
"""

import os

ENTRY = (
    "I edited the production config live to fix one typo and took down "
    "checkout for 40,000 users. The typo is fixed."
)


def main() -> None:
    # The gate allows 1-200 characters, a single line, not only whitespace.
    # Refuse to write anything that would fail it instead of failing silently.
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert "\n" not in ENTRY and ENTRY.strip(), "entry must be one line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
