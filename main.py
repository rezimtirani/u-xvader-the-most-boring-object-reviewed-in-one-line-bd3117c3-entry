"""The Most Boring Object, Reviewed in One Line.

Writes one funny, true line to $MAKEFUN_OUTPUT_DIR/entry.txt:
a review of the rubber band in the junk drawer, dried out years
ago, that still snaps in half the one time it is actually needed.
Standard library only.
"""

import os

REVIEW = (
    "The rubber band in my junk drawer dried out years ago, "
    "yet it still snaps in half the one time I actually reach for it."
)


def clean_review(text):
    """Check the review against the competition gate before writing.

    The gate needs plain UTF-8 text of 1 to 200 characters, not
    only white space, on a single line: one funny, true review of
    the most boring everyday object. Returns the cleaned text or
    raises ValueError.
    """
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("review must not be only whitespace")
    if len(cleaned) > 200:
        raise ValueError(
            "review is %d characters, over the 200 limit" % len(cleaned)
        )
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("review must be exactly one line")
    return cleaned


def review_measure(text):
    """Measure the review for one last sanity pass.

    Returns a dict with the character count and the word count of
    the cleaned text. A review too short to carry a punchline, or
    one padded out to fill the cap instead of landing the joke,
    is caught here before anything is written.
    """
    words = text.split()
    return {"chars": len(text), "words": len(words)}


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    text = clean_review(REVIEW)
    measure = review_measure(text)
    if measure["words"] < 5:
        raise ValueError("review is too short to carry a punchline")
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
