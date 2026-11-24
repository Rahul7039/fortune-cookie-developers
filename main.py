"""Fortune Cookie Wisdom for Developers.

Entry for make.fun competition
u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44.

Writes one original fortune-cookie line for a software developer
to /output/entry.txt. Python 3.13, stdlib only, no network, fully
deterministic: the same line, byte for byte, on every run.
"""

import os

FORTUNE = "You will fix the bug by deleting the code you were proudest of writing."


def main() -> None:
    output_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(output_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    # Write the line exactly, with no trailing newline: the gate counts
    # every character in the file, and the entry must stay <= 120 chars.
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        f.write(FORTUNE)
    print(FORTUNE)


if __name__ == "__main__":
    main()
