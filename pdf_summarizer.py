"""
PDF Highlighter Summarizer
==========================
Give it a PDF path → get a keyword summary back.

Concepts to practice:
  - OOP (classes, __init__, self, methods)
  - File I/O
  - Higher-order functions (map, filter, sorted with key=lambda)
  - defaultdict
  - Recursion
  - String methods
  - List comprehensions

Install the PDF library first:
  pip install pdfplumber
"""

import string
from collections import defaultdict
import pdfplumber


class Page:
    """Represents one page of a PDF."""

    def __init__(self, page_number: int, raw_text: str):
        self.page_number = page_number
        self.raw_text    = raw_text

    def get_sentences(self) -> list[str]:
        """Split raw_text into a list of sentences (split on '.')."""
        return [s.strip() for s in self.raw_text.split(".") if s.strip() != ""]

    def get_words(self) -> list[str]:
        """Return every word on this page, lowercased, punctuation removed."""
        word = self.raw_text.split()
        turn_lower = filter(lambda x: x != "", map(lambda x: x.lower().strip(string.punctuation), word))
        return list(turn_lower)


class Document:
    """Represents a full PDF as a list of Page objects."""

    def __init__(self, filepath: str):
        self.filepath = filepath
        self.pages: list[Page] = []

    def load(self) -> None:
        """Open the PDF and populate self.pages."""
        with pdfplumber.open(self.filepath) as pdf:
            for i, page in enumerate(pdf.pages):
                text = page.extract_text()
                if text is None:
                    text = ""
                self.pages.append(Page(i, text))

    def all_words(self) -> list[str]:
        """Return every word from every page as one flat list."""
        return [word for page in self.pages for word in page.get_words()]


class Summary:
    """Builds and displays a summary from a Document."""

    def __init__(self, document: Document, top_n: int = 15):
        self.document = document
        self.top_n    = top_n

    def word_counts(self) -> dict[str, int]:
        """Count how often each word appears across the whole document."""
        counts: dict[str, int] = defaultdict(int)
        total_words = self.document.all_words()
        for word in total_words:
            counts[word] += 1
        return dict(counts)

    def top_keywords(self) -> list[tuple[str, int]]:
        """Return the self.top_n most frequent words, excluding stop words."""
        STOP_WORDS = {
            "the", "a", "an", "is", "it", "in", "on", "at", "to", "of",
            "and", "or", "for", "with", "this", "that", "be", "as", "are",
            "was", "by", "from", "but", "not", "have", "had", "has", "we",
            "you", "i", "if", "so", "do", "its", "can", "will", "all", "—",
        }
        counts = self.word_counts()
        filtered = filter(lambda x: x[0] not in STOP_WORDS, counts.items())
        by_count = sorted(filtered, key = lambda x: x[1], reverse = True)
        return by_count[:self.top_n]

    def important_sentences(self, keywords: set[str]) -> list[str]:
        """
        Recursively score sentences and return the top 5.

        Use recursion to walk through the pages:
          base case  → no pages left, return []
          recursive  → score sentences on current page, combine with rest
        """
        def score_sentence(sentence: str) -> int:
            """Count how many keywords appear in this sentence."""
            words = [w.lower().strip(string.punctuation) for w in sentence.split()]
            return len([w for w in words if w in keywords])

        def recurse(pages: list[Page]) -> list[str]:
            # TODO: base case — if pages is empty, return []
            if not pages:
                return []
            sentences = pages[0].get_sentences()
            long_sentences = filter(lambda x: len(x.split()) >= 5, sentences)
            by_score = sorted(long_sentences, key = lambda x: score_sentence(x), reverse = True)
            top_two = by_score[:2]
            return top_two + recurse(pages[1:])

        all_sentences = recurse(self.document.pages)
        return sorted(all_sentences, key= lambda x: score_sentence(x), reverse= True)[:5]

    def display(self) -> None:
        """Print the final summary to the terminal."""
        keywords_ranked = self.top_keywords()

        if not keywords_ranked:
            print("No content found — did the PDF load correctly?")
            return

        keyword_set = {word for word, _ in keywords_ranked}

        print(f"\n{'=' * 50}")
        print(f"  SUMMARY: {self.document.filepath}")
        print(f"  Pages: {len(self.document.pages)}")
        print(f"{'=' * 50}")

        print(f"\nTop {self.top_n} Keywords:")
        print("-" * 30)
        for word, count in keywords_ranked:
            bar = "█" * min(count, 30)
            print(f"  {word:<20} {bar} ({count})")

        print(f"\nKey Sentences:")
        print("-" * 30)
        sentences = self.important_sentences(keyword_set)
        for i, sentence in enumerate(sentences, 1):
            print(f"  {i}. {sentence.strip()}")

        print()


def main() -> None:
    filepath = input("Enter path to a PDF file: ").strip()

    doc = Document(filepath)

    doc.load()
    if not doc.pages:
        print("Error: no pages found — did the PDF load correctly?")
        return

    summary = Summary(doc, top_n=15)
    summary.display()


if __name__ == "__main__":
    main()
