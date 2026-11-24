"""Fortune Cookie Wisdom for Developers.

Entry for make.fun competition
u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44.

Writes one original fortune-cookie line for a software developer
to /output/entry.txt. Python 3.13, stdlib only, no network, fully
deterministic: the same line, byte for byte, on every run.

The competition's gate is enforced here, not trusted to luck: the
text is validated against the gate before it is written, and the
file is read back afterwards and compared byte for byte with the
expected encoding. Any failure exits non-zero with a clear error
instead of leaving behind an entry the gate would reject.
"""

import os
import sys

FORTUNE = "You will fix the bug by deleting the code you were proudest of writing."

# The competition's gate (competition.yaml / RULES.txt): /output/entry.txt
# must be UTF-8 text of 1 to 120 characters, not only white space.
MAX_CHARS = 120


def check_gate(text: str) -> None:
    """Raise ValueError unless `text` satisfies the competition's gate.

    Checks, in the order the gate states them: non-empty, at most
    120 characters, not only white space, and a single line (no
    line breaks, so the file holds exactly one fortune-cookie line).
    """
    if not text:
        raise ValueError("gate failed: entry is empty (needs 1-120 characters)")
    if len(text) > MAX_CHARS:
        raise ValueError(
            f"gate failed: entry is {len(text)} characters, over the 120 limit"
        )
    if not text.strip():
        raise ValueError("gate failed: entry is only white space")
    if "\n" in text or "\r" in text:
        raise ValueError("gate failed: entry must be a single line")
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        # A lone surrogate (or other unencodable character) would make
        # the gate's UTF-8 requirement fail at write time; catch it
        # here so the failure is reported as a gate failure, not a crash.
        raise ValueError("gate failed: entry is not valid UTF-8 text") from None


def main() -> int:
    try:
        check_gate(FORTUNE)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    output_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(output_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    expected = FORTUNE.encode("utf-8")
    # Write the line exactly, with no trailing newline: the gate counts
    # every character in the file, and the entry must stay <= 120 chars.
    with open(output_path, "wb") as f:
        f.write(expected)

    # Read the file back and confirm it holds exactly the intended
    # bytes: a truncated or mangled write must fail loudly here rather
    # than reach the gate as an invalid entry.
    with open(output_path, "rb") as f:
        actual = f.read()
    if actual != expected:
        first_diff = next(
            (i for i, (a, b) in enumerate(zip(actual, expected)) if a != b),
            min(len(actual), len(expected)),
        )
        print(
            f"error: wrote {len(actual)} bytes to {output_path} but expected "
            f"{len(expected)} bytes for the entry text "
            f"(first difference at byte {first_diff})",
            file=sys.stderr,
        )
        return 1

    print(FORTUNE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
