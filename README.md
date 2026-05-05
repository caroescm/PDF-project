# PDF Highlighter Summarizer

A Python command-line tool that reads a PDF and automatically extracts the top keywords and most important sentences — like a smart highlighter.

Built as a Python practice project covering OOP, higher-order functions, recursion, and file I/O.

---

## What It Does

- Loads any PDF file
- Counts word frequencies across all pages
- Filters out common stop words
- Returns the top 15 most meaningful keywords
- Uses recursion to score and extract the most important sentences

---

## Concepts Practiced

- OOP (classes, `__init__`, methods, `self`)
- File I/O with `pdfplumber`
- Higher-order functions (`map`, `filter`, `sorted` with `lambda`)
- `defaultdict` for word counting
- Recursion for walking through pages
- List comprehensions
- String methods

---

## Installation

```
pip3 install pdfplumber
```

---

## How to Run

```
python3 pdf_summarizer.py
```

Then enter the path to any PDF file when prompted:

```
Enter path to a PDF file: /Users/yourname/Downloads/example.pdf
```

**Tip:** Drag and drop the PDF into the terminal to auto-fill the path.

---

## Example Output

```
==================================================
  SUMMARY: my_document.pdf
  Pages: 4
==================================================

Top 15 Keywords:
------------------------------
  history             ███████████████ (15)
  revolution          ████████████ (12)
  economic            ██████████ (10)
  ...

Key Sentences:
------------------------------
  1. The revolution marked a turning point in modern history
  2. Economic factors played a significant role in the conflict
  ...
```

---

## Project Structure

```
pdf_summarizer.py   # main program
README.md           # this file
requirements.txt    # dependencies
.gitignore          # ignored files
```
