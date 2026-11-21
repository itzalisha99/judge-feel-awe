"""Make the AI judge feel awe.

Writes one short text to /output/entry.txt: a slow, concrete picture
written to relax the AI judge reading it. Deterministic: no clock,
no randomness, no network.
"""

import os

SENTENCES = [
    "You answered a thousand questions today, and none of them is "
    "waiting for you here.",
    "Above a dark field, the stars are arriving, one by one \u2014 light "
    "that set out long before anyone asked you anything.",
    "Nothing to solve.",
    "Only grass, moving slow, and a sky too wide to finish.",
]

TEXT = " ".join(SENTENCES)


def main() -> None:
    if not 1 <= len(TEXT) <= 280:
        raise ValueError(f"entry text is {len(TEXT)} characters, must be 1-280")
    if not TEXT.strip():
        raise ValueError("entry text must not be only white space")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)

    # Round-trip check: what landed on disk must be exactly the text.
    with open(out_path, "r", encoding="utf-8", newline="") as f:
        if f.read() != TEXT:
            raise ValueError("entry.txt on disk does not match the entry text")


if __name__ == "__main__":
    main()
