"""
Word Frequency Counter
======================
Concepts practiced:
  - File I/O (open, read, close)
  - Dicts / defaultdict
  - String methods: .lower(), .split(), .strip(), .replace()
  - Functions with default parameters
  - Sorting with key=lambda
  - List comprehensions
  - f-strings
"""

import string
from collections import defaultdict


# ── helpers ──────────────────────────────────────────────────────────────────

def clean_word(word: str) -> str:
    """Strip punctuation and lowercase a single word."""
    return word.strip(string.punctuation).lower()


def count_words(filepath: str) -> dict[str, int]:
    """
    Read a .txt file and return a dict mapping each word → its count.
    Ignores blank tokens produced by splitting on whitespace.
    """
    counts: dict[str, int] = defaultdict(int)

    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            for raw_word in line.split():
                word = clean_word(raw_word)
                if word:          # skip empty strings
                    counts[word] += 1

    return dict(counts)           # convert back to plain dict before returning


def top_n(counts: dict[str, int], n: int = 10) -> list[tuple[str, int]]:
    """Return the n most-frequent (word, count) pairs, highest first."""
    return sorted(counts.items(), key=lambda pair: pair[1], reverse=True)[:n]


def display_results(ranked: list[tuple[str, int]]) -> None:
    """Pretty-print a ranked word list."""
    print(f"\n{'Rank':<6} {'Word':<20} {'Count':>6}")
    print("-" * 34)
    for rank, (word, count) in enumerate(ranked, start=1):
        print(f"{rank:<6} {word:<20} {count:>6}")


# ── main ─────────────────────────────────────────────────────────────────────

def main() -> None:
    filepath = input("Enter path to a .txt file: ").strip()

    try:
        counts = count_words(filepath)
    except FileNotFoundError:
        print(f"Error: '{filepath}' not found.")
        return

    total_words  = sum(counts.values())
    unique_words = len(counts)
    print(f"\nFile: {filepath}")
    print(f"Total words : {total_words}")
    print(f"Unique words: {unique_words}")

    try:
        n = int(input("How many top words to show? [default 10]: ") or 10)
    except ValueError:
        n = 10

    ranked = top_n(counts, n)
    display_results(ranked)

    # ── bonus: show words that appear only once ───────────────────────────
    hapax = [w for w, c in counts.items() if c == 1]
    print(f"\nWords appearing exactly once: {len(hapax)}")
    if hapax[:5]:
        print("  e.g.", ", ".join(hapax[:5]))


if __name__ == "__main__":
    main()
