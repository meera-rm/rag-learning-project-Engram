# 01 — Preparing the documents (`rag-docs/`)

**Goal:** turn a messy folder of study material into clean, text-only Markdown files that a RAG pipeline can read.

**Explain it like I'm 10:** before studying, you empty your backpack, throw out the wrappers, photocopy the pages that are only pictures, and put the notebooks into labeled folders by subject.

## 1. What I started with

My `lstemp` folder had **14,289 files**, but most weren't notes:

| What | Count | Usable? |
| --- | --- | --- |
| Python library files inside `pandsfolder/.venv/` | ~13,000 | ❌ Installed code, not notes |
| Markdown notes (`.md`) | ~85 | ✅ Best source: clean text with headings |
| PDFs | 24 | 🟡 Half have real text, half are only images |
| Screenshots (`.png`) | ~100 | ❌ Not used this time |
| Notebooks, HTML, CSV, code | a few dozen | 🟡 Some converted, the rest skipped |

**Lesson:** always look at what's actually in a folder before feeding it to a RAG. Junk in = junk answers out.

## 2. Checking which PDFs have real text

A PDF can hold real text, or it can just be **pictures of pages** (scans, exported handwriting). A RAG can only read real text.

```bash
pdfinfo "file.pdf"            # how many pages
pdftotext "file.pdf" - | wc -w   # how many words of extractable text
```

- **Lots of words** → text PDF, can be converted directly.
- **0 words** → image-only PDF, needs OCR (text recognition).

Result: 10 text PDFs (books, interview questions) and 12 image-only PDFs.

**Explain it like I'm 10:** a text PDF is a typed page. An image PDF is a photo of a page. The computer can read typing, but for a photo it needs glasses (OCR) first.

## 3. Finding duplicates

Identical files make the same chunk show up twice in search results and push out other useful ones. I compared file *contents* using checksums (a fingerprint of the file):

```bash
md5sum *.pdf *.md | sort      # identical fingerprints = identical files
```

Found 3 exact duplicate pairs (e.g. `system design.pdf` and `system design (1).pdf`) and kept one of each.

## 4. Converting everything to Markdown

Every output file went into `rag-docs/<topic>/<name>.md`.

| Source | How it was converted |
| --- | --- |
| Markdown notes | Copied as-is |
| Text PDFs | `pdftotext`, splitting on page breaks and adding `<!-- page N -->` markers |
| Image-only PDFs | Each page rendered with `pdftoppm`, then read with `tesseract` OCR |
| `.ipynb` notebooks | Read the JSON, kept markdown cells, wrapped code cells in ```` ```python ```` |
| `.html` pages | `pandoc` to Markdown; flashcards pulled out of the page's JavaScript data |

The OCR commands, per page:

```bash
pdftoppm -r 250 -gray -png -f 5 -l 5 file.pdf page    # render page 5 as an image
tesseract page.png - --psm 3                          # read the text from the image
```

OCR was slow (~17 s per page), so it ran 4 pages at a time in parallel. OCR text has typical errors, for example `print()` read as `printO`.

**Why page markers?** `<!-- page 12 -->` is an HTML comment, so it's invisible when the Markdown is displayed, but my code can use it to split books by page and cite page numbers.

## 5. Adding frontmatter (labels) to every file

Each file starts with a **YAML frontmatter** header between two `---` lines:

```markdown
---
title: SQL-Complete-Notes
topic: databases
source_type: my-notes
source_file: STUDYNOTEs/SQL-Complete-Notes.md
---
```

- `topic` = the folder (`databases`, `java-spring`, `system-design`, …)
- `source_type` = one of `my-notes`, `interview-questions`, `book`, `ocr`
- `source_file` = where the original lives
- `pages` = page count (PDF-based files only)

This becomes each chunk's **metadata**, so answers can say where they came from and searches can be filtered.

## 6. What I left out on purpose

| Left out | Why |
| --- | --- |
| `.venv/` library files | Code, not notes |
| `plans/` daily schedules | To-do lists would show up instead of real explanations |
| Resume and about-me files | Personal, not study material |
| Duplicates, notebook copy of a `.md`, blank question test | Same content twice, or questions with no answers |
| Screenshots | Images; not selected for this build |

## Result

**68 files, 10 topic folders, ~1.37 million words.**

| `source_type` | Words |
| --- | --- |
| `book` | ~715k |
| `my-notes` | ~465k |
| `interview-questions` | ~126k |
| `ocr` | ~63k |

The two big books (Java/Spring notes, topmate System Design) are larger than all my own notes together. That matters later: searches may lean toward book text unless I rank `my-notes` higher.

The full file list is in `rag-docs/README.md`.
