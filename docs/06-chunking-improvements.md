# 06 — Improving the chunker (`index.py`)

**Goal:** compare my chunker with the tutorial's, clean up `index.py`, add section labels for citations, save the chunks to a file, and fix two data-quality bugs the stats revealed.

**Explain it like I'm 10:** I already had scissors that cut my notebook into cards along the chapter lines. Today I tidied the scissors, wrote the chapter name on every card, put the cards in a box, and found that some cards had been photocopied by a broken copier.

## 1. My chunker vs. the tutorial's `step1_extract_and_chunk.py`

Tutorial: [niharika2309/basic_RAG — step1_extract_and_chunk.py](https://github.com/niharika2309/basic_RAG/blob/main/step1_extract_and_chunk.py)

| | Tutorial step 1 | My `index.py` |
| --- | --- | --- |
| Input | 1 PDF read with `pypdf` | 68 `.md` files read with `python-frontmatter` |
| First split | Per page | Per section, with a different header pattern per `source_type` |
| Code-block aware | No | Yes (`in_code` stops `# comments` counting as headings) |
| Size unit | ~600 characters (~100 words) | 300 words, then a 480-token check |
| How long text is cut | Sliding window at word boundaries | `recursive_split`: paragraph → line → sentence → word |
| Overlap | 10 words | 50 words |
| Newlines | Lost (joined with spaces) | Kept (`last_words`) |
| Clean-up passes | None | Merge tiny sections, drop TOC, merge heading-only, token limit |
| Metadata | `{"page": N}` | All frontmatter + `section` |
| Output | Writes `chunks.json` | Writes `all_chunks.json` (added today) |

**Which is better for me?** Mine. My notes are Markdown with headings, code blocks and three kinds of sources (notes, interview Q&A, OCR'd books). A fixed-size cutter would slice explanations away from their examples and flatten code onto one line.

**What I borrowed from the tutorial:** saving chunks to a file, and precise citations (the tutorial has page numbers; I added section labels).

**Explain it like I'm 10:** the tutorial is a cookie cutter for one kind of dough. My notes are a box of mixed shapes, so I need scissors that follow each shape's outline.

## 2. Cleanup

| Change | Why |
| --- | --- |
| Removed duplicate `from statistics import mean, median` and unused `random` | Less clutter; imports grouped standard library → third-party (PEP 8) |
| Removed `print(len(docs), docs[0]["metadata"])` from `load_docs()` | Duplicated output, and crashes with `IndexError` on an empty folder |
| Renumbered the section comments (there were two "Step 2b") | The file reads in the order the pipeline runs |
| Moved `split_oversized_chunks` above `build_chunks` | Top-to-bottom = order of execution |
| Replaced the empty `analyze_chunks` stub with every stat **once** | `__main__` printed "Total chunks" 4×, "Largest chunk" 3× |
| `__main__` is now 3 lines | `build_chunks()` → `save_chunks()` → `analyze_chunks()` |

```python
if __name__ == "__main__":
    all_chunks = build_chunks()
    save_chunks(all_chunks)
    analyze_chunks(all_chunks)
```

## 3. Saving chunks to a file

```python
CHUNKS_PATH = BASE_DIR / "all_chunks.json"

def save_chunks(chunks, path=CHUNKS_PATH):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(chunks, f, ensure_ascii=False, indent=2, default=str)
    print(f"Saved {len(chunks)} chunks -> {path}")
```

- **Saved in `__main__`, not inside `build_chunks()`.** A function that builds chunks shouldn't also decide where they go on disk. (Explain it like I'm 10: the baker bakes; whoever holds the cookies decides box or plate.)
- `ensure_ascii=False` keeps `é`, `→`, `’` readable.
- `default=str` handles YAML dates in frontmatter (`date: 2026-10-01` becomes a Python `date`, which JSON can't store).
- The file name must match what `embed.py` reads: `all_chunks.json`.

## 4. Section labels for citations

Before, citations said only `STUDYNOTEs/SQL-Complete-Notes.md`. Now they say `STUDYNOTEs/SQL-Complete-Notes.md › LEFT JOIN (LEFT OUTER JOIN)`.

```python
def section_label(section, header_pattern):
    """First header line of a section, cleaned up for citations."""
    pattern = re.compile(header_pattern)
    for line in section.split("\n"):
        if pattern.match(line):
            page = re.match(r"<!-- page (\d+) -->", line)
            if page:
                return f"p. {page.group(1)}"
            return line.strip("#* ").strip()
    return ""   # text before the first heading (intro paragraph)
```

- Lives right after `markdown_document_chunking`, because both use the same `header_pattern`.
- Called in `build_chunks()` **before** `chunk_section()`, because the 50-word overlap pushes the heading away from the top of later pieces:

```python
for section in sections:
    label = section_label(section, header_pattern)   # read the title first
    chunks = chunk_section(section)                  # then cut + add overlap
    for chunk in chunks:
        ...
        metadata = doc["metadata"].copy()
        metadata["section"] = label                  # every piece inherits it
```

Labels look like `LEFT JOIN`, `Q12. What is a CTE?` (interview files) and `p. 7` (books). Only 6 of 9,251 chunks have an empty label.

**Explain it like I'm 10:** one function cuts the notebook into chapters; `section_label` reads the title off each chapter so every card says which chapter it came from.

## 5. Bug found by the stats: token splitting damaged ~20% of chunks

**Symptom:** 295 "heading-only" chunks that weren't heading-only at all:

```
'# # 11. normalization and denormalization # # # normalization * * normalization is ...'
'select e. name, d. department _ name from employees e left join departments d ...'
```

**Why:** `split_oversized_chunks` encoded chunks to tokens, cut them, then **decoded** the tokens back to text. The bge tokenizer is uncased, so decoding lowercases everything, adds spaces around punctuation and drops newlines. About **1,884 of 9,296 chunks (~20%)** came out like this — mostly Spring Boot, the system-design digest and Java notes.

**Fix:** use the tokenizer only to find *where* to cut, then slice the **original** text with `return_offsets_mapping=True`:

```python
enc = tokenizer(text, add_special_tokens=False, return_offsets_mapping=True)
offsets = enc["offset_mapping"]          # (start_char, end_char) for each token
...
char_start = piece_offsets[0][0]
char_end = piece_offsets[-1][1]
piece_text = text[char_start:char_end].strip()   # slice the ORIGINAL text
```

**Explain it like I'm 10:** I translated my notes into a secret code to measure them, then translated back with a decoder that only knows lowercase and puts spaces everywhere. Now I just use the code to mark where to cut, and cut the original page.

## 6. Bug found by the stats: TOC pages with solid dots

**Symptom:** smallest chunks were `....... 8 maven....... 9 gradle....` from the tutorialspoint PDF.

**Why:** `is_table_of_contents` only caught **spaced** dot leaders (`. . . .`).

**Fix:**

```python
def is_table_of_contents(text):
    # TOC lines use dot leaders: "Summary . . . . 122" or "Summary........122"
    return text.count(". .") >= 10 or len(re.findall(r"\.{5,}", text)) >= 3
```

## 7. Commands I ran

```bash
python index.py > before.txt     # save the stats output to a file
python index.py > after.txt      # run again after the change
diff before.txt after.txt        # line-by-line comparison
```

- `>` redirects printed output into a file instead of the screen.
- **Lesson:** my first "before" and "after" were identical because both ran the **same** file. A real before/after needs the old code saved first (no git in this folder yet).
- The warning `Token indices sequence length is longer than the specified maximum sequence length (702 > 512)` is harmless: the tokenizer measures chunks *before* splitting them.

## 8. Results — before vs. after the fixes

| | Before | After | Why |
| --- | --- | --- | --- |
| Total chunks | 9,296 | **9,251** | exactly 45 TOC chunks removed |
| Lowercased / mangled chunks | ~1,884 (20%) | **0** | slice original text |
| Dot-leader TOC chunks | 45 | **0** | new `\.{5,}` rule |
| "Heading-only" chunks | 295 | **0** | they were decoded chunks squashed onto one line |
| Largest chunk | 393 words | 349 words | decoding had inflated counts (`department _ name` = 3 words) |
| Mean / median | 156.2 / 156 | 139.2 / 129 | same reason |
| Max tokens / over 512 | 482 / 0 | 482 / 0 | still under bge's limit |

Size distribution after:

```
  0 -  40 words:    51 chunks (0.6%)
 40 - 100 words:  3315 chunks (35.8%)
100 - 200 words:  3876 chunks (41.9%)
200 - 300 words:  1913 chunks (20.7%)
300 - 350 words:    96 chunks (1.0%)
350 - inf words:     0 chunks (0.0%)
```

Top documents by chunk count: Spring Boot notes PDF (1,526), topmate System Design PDF (1,409), System Design digest (779), Java complete notes (503), SQL interview questions (372).

Remaining small junk (optional to fix later): ~51 chunks under 40 words, e.g. a sentence fragment plus page number, Docker hash lists, a title page.

## Resources

- [Pinecone — Chunking Strategies for LLM Applications](https://www.pinecone.io/learn/chunking-strategies/) — fixed-size vs. structure-aware vs. recursive.
- Greg Kamradt — "5 Levels of Text Splitting" (FullStackRetrieval RetrievalTutorials on GitHub) — the path from step 1 to my `index.py`.
- Hugging Face LLM Course, ch. 6 "Fast tokenizers' special powers" — `return_offsets_mapping`, the fix in section 5.
- PEP 8 "Imports" — import order used in the cleanup.
