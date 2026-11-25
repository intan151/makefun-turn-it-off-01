"""Have You Tried Turning It Off? -- make.fun one-liner entry.

Writes one funny line (<=200 characters) to /output/entry.txt: the line a
hopeless tech support agent says to a desperate customer.

Stdlib only, no network, no randomness: the output is byte-identical on
every run.
"""

import os

LINE = (
    "Have you tried turning it off and on again? It won't fix your "
    "computer, but it's the only thing in my life I've ever successfully "
    "fixed."
)


def main():
    assert 1 <= len(LINE) <= 199, "entry must be 1-199 characters"
    assert "\n" not in LINE, "entry must be a single line"
    assert "turning it off" in LINE.lower(), "entry must answer the brief"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    # Read back: the file on disk must be exactly the line, nothing else.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        assert f.read() == LINE, "entry.txt does not match the line"


if __name__ == "__main__":
    main()
