# 04 — Step 2: Chunking the documents

**Goal:** cut every document into pieces of about 40–350 words, each holding one idea, using the document's own structure.

**Explain it like I'm 10:** you're cutting a giant textbook into index cards. A card with one word is useless, a card with a whole chapter is too much to scan. One idea per card, with the chapter name on top.

**Why chunk at all?** Search compares my question with each chunk as a whole. A 60,000-word file matches everything a little and nothing well. Small embedding models also only "read" the first ~190 words (MiniLM) or ~380 words (BGE) of a chunk and ignore the rest.

## 1. Choosing the strategy

I compared the methods in [Weaviate's chunking guide](https://weaviate.io/blog/chunking-strategies-for-rag):

| Method | Fit for my files | Why |
| --- | --- | --- |
| **Document-based (Markdown headings)** | ✅ Main method | My files are clean Markdown with lots of headings |
| **Recursive** | ✅ Backup | Cuts sections that are still too long; handles page-only books |
| Fixed-size | 🟡 Baseline only | Ignores headings, cuts mid-idea |
| Hierarchical | 🟡 Later upgrade | Could help with the 1,300-page books |
| Semantic, late, LLM-based, agentic | ❌ Not now | Built for unstructured text, or too costly and complex for a first RAG |

**Decision: split on structure first, then recursively split anything still too long.**

## 2. Settings

```python
CHUNK_WORDS = 300      # target size for each piece
OVERLAP_WORDS = 50     # words repeated between neighbouring pieces
SEPARATORS = ["\n\n", "\n", ". ", " "]   # paragraph, line, sentence, word
MIN_WORDS = 40         # sections shorter than this get merged into the next
```

300 + 50 overlap = 350 words max, which fits the BGE embedding model fully. (I first tried 500, but the end of many chunks would have been ignored by the model.)

## 3. A different split pattern per `source_type`

```python
def get_header_pattern(source_type):
    if source_type == "interview-questions":
        # bold questions (**Q1. / **1.), headings, or PDF page markers
        return r'^(\*\*Q?\d+\.|#{1,6}\s|<!-- page \d+ -->$)'
    elif source_type in ("book", "ocr"):
        return r'^<!-- page \d+ -->$'
    else:
        return r'^#{1,6}\s+.+$'   # markdown headings (my-notes)
```

Reading the regex patterns:

| Piece | Means |
| --- | --- |
| `^` / `$` | start / end of the line |
| `#{1,6}\s` | 1 to 6 `#` characters, then a space (a Markdown heading) |
| `\*\*` | two literal asterisks (`*` is special, so it's escaped with `\`) |
| `Q?` | an optional `Q`, so it matches `**Q1.` and `**1.` |
| `\d+\.` | one or more digits, then a literal dot |
| `|` | OR |
| `<!-- page \d+ -->` | a page marker with any page number |

Why three patterns:
- **my-notes** use headings.
- **interview files** mark questions as bold lines (`**Q1. What is SQL?**`) or headings (JS/React), and the Goldman Sachs file came from a PDF, so it only has page markers.
- **books and OCR** only have page markers.

**Explain it like I'm 10:** regex is a stencil. `N` is a stencil of the letter N; `\d+` fits any number, so it matches page 1, page 12 and page 412.

## 4. Split on structure (and never inside code)

```python
def markdown_document_chunking(text, header_pattern):
    lines = text.split('\n')
    pattern = re.compile(header_pattern)
    chunks = []
    current_chunk = []
    in_code = False

    for line in lines:
        if line.strip().startswith("```"):
            in_code = not in_code            # entering or leaving a code block
        if pattern.match(line) and not in_code:
            if current_chunk:                # save the section we were building
                chunk_text = '\n'.join(current_chunk).strip()
                if chunk_text:
                    chunks.append(chunk_text)
                current_chunk = []
        current_chunk.append(line)

    if current_chunk:                        # don't forget the last section
        chunk_text = '\n'.join(current_chunk).strip()
        if chunk_text:
            chunks.append(chunk_text)

    return chunks
```

- Walks line by line. A matching line means "a new section starts here".
- `re.match` checks from the **start** of the line.
- `in_code` stops a Python comment like `# Two positional arguments` inside a code block from being treated as a heading.
- The "last section" block and `return` sit **after** the loop (see the debugging log for what happened when they didn't).

## 5. Merge tiny sections

```python
def merge_small_sections(sections, min_words=MIN_WORDS):
    merged = []
    carry = ""
    for section in sections:
        carry = carry + "\n\n" + section if carry else section
        if word_count(carry) >= min_words:
            merged.append(carry)
            carry = ""
    if carry:                          # leftover small piece at the very end
        if merged:
            merged[-1] += "\n\n" + carry
        else:
            merged.append(carry)
    return merged
```

A heading-only section like `# PART 8 — OBJECTS AND PROGRAMMABILITY` is carried forward and joined to the section after it, so that chunk knows which part of the notes it belongs to. Cover pages get attached to the next page the same way.

**Explain it like I'm 10:** a sticky note that only says "Chapter 8" is useless alone. Stick it on top of chapter 8's first page.

## 6. Recursive splitting for long sections

```python
def recursive_split(text, separators=SEPARATORS):
    if not text.strip():
        return []
    if word_count(text) <= CHUNK_WORDS:          # small enough: keep it
        return [text]
    if not separators:                           # nothing left: hard cut by words
        words = text.split()
        return [" ".join(words[i:i + CHUNK_WORDS]) for i in range(0, len(words), CHUNK_WORDS)]
    sep, rest = separators[0], separators[1:]
    parts = text.split(sep)
    pieces, current = [], ""
    for part in parts:
        candidate = current + sep + part if current else part
        if word_count(candidate) <= CHUNK_WORDS:
            current = candidate                  # keep packing parts together
        else:
            if current:
                pieces.append(current)
            if word_count(part) > CHUNK_WORDS:
                pieces.extend(recursive_split(part, rest))   # still too big: smaller separator
                current = ""
            else:
                current = part
    if current:
        pieces.append(current)
    return pieces
```

1. Small enough? Keep it unchanged.
2. Too big? Split on paragraphs (`\n\n`) and pack them back together up to 300 words.
3. One paragraph alone too big? The function **calls itself** with the next separator: lines, then sentences, then words. That's the "recursive" part.

**Explain it like I'm 10:** to fit a cake into lunchboxes, cut along the layers first. If a layer is too big, cut slices. If a slice is too big, cut bites. Only use the smaller knife when you have to.

## 7. Overlap that keeps formatting

```python
def last_words(text, n):
    """Return the last n words of text, keeping its original spaces and newlines."""
    parts = re.split(r'(\s+)', text)    # the ( ) keeps the whitespace as separate parts
    seen = 0
    for i in range(len(parts) - 1, -1, -1):
        if parts[i].strip():            # a word, not whitespace
            seen += 1
            if seen == n:
                return "".join(parts[i:]).strip()
    return text.strip()


def add_overlap(pieces):
    if not pieces:
        return []
    out = [pieces[0]]
    for prev, piece in zip(pieces, pieces[1:]):
        tail = last_words(prev, OVERLAP_WORDS)
        out.append(tail + "\n" + piece)
    return out


def chunk_section(text):
    return add_overlap(recursive_split(text))
```

- Each piece starts with the last 50 words of the piece before it, so an idea cut at a boundary still appears whole in one chunk.
- My first version used `" ".join(prev.split()[-50:])`, which lost every newline and squashed headings and tables onto one line. `re.split(r'(\s+)', ...)` keeps the whitespace, so Markdown stays intact.

## 8. Drop table-of-contents chunks

```python
def is_table_of_contents(text):
    # TOC lines use dot leaders: "Summary . . . . . . . 122"
    return text.count(". .") >= 10
```

The big PDFs had ~465 contents-page chunks. They contain no knowledge, but their keywords can match questions and push useful chunks out of the results.

## 9. Putting it together

```python
docs = load_docs()
all_chunks = []
for doc in docs:
    source_type = doc["metadata"]["source_type"]
    header_pattern = get_header_pattern(source_type)
    sections = markdown_document_chunking(doc["text"], header_pattern)
    sections = merge_small_sections(sections)          # merge first...
    for section in sections:
        for chunk in chunk_section(section):           # ...then cut to size
            if is_table_of_contents(chunk):
                continue
            all_chunks.append({"text": chunk, "metadata": doc["metadata"]})
```

Order matters: merge first, then recursively split, so a merged section that's too long still gets cut.

## 10. Checking quality with random samples

```python
import random
for c in random.sample(all_chunks, 3):
    print("\n---", c["metadata"]["topic"], "|", c["metadata"]["title"])
    print(c["text"][:450])
```

Each sample should read as one complete idea. **Note:** `[:450]` only prints the first 450 characters, so endings like `WHER` are cut in the *printout*, not in the chunk. Use `print(c["text"])` to see a whole chunk.

## How the numbers changed

| Change | Chunks | Largest |
| --- | --- | --- |
| Structure split only (first working run) | 9,083 sections | 46,693 words |
| + recursive split, overlap | 10,516 | 350 |
| + drop table-of-contents chunks | 9,704 | 350 |
| + merge sections under 40 words, skip code blocks | **8,387** | **350** |

## Resources

- [Weaviate: Chunking Strategies for RAG](https://weaviate.io/blog/chunking-strategies-for-rag) — compares every method; the source of the strategy decision.
- [LangChain: Recursive text splitter](https://python.langchain.com/docs/how_to/recursive_text_splitter/) — the library version of the recursive idea.
- [regex101.com](https://regex101.com/) — test regex patterns against real lines (set the flavor to Python).
- [Python Regular Expression HOWTO](https://docs.python.org/3/howto/regex.html) — official beginner guide to regex.
