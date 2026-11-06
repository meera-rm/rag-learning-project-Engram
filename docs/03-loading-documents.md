# 03 — Step 1: Loading the documents

**Goal:** turn the 68 files into a Python list where each item has the file's **text** and its **metadata**.


## 1. Build paths from the script's own location

```python
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent   # the my-first-rag folder
DOCS_DIR = BASE_DIR / "rag-docs"
```

- `__file__` is the path of the running script, so `.parent` is the folder it lives in.
- This works no matter which folder I run `python index.py` from. `Path("rag-docs")` would only work when the terminal is already inside `my-first-rag`.
- The `/` operator joins path parts.

## 2. Find every file with `rglob`

```python
for path in sorted(DOCS_DIR.rglob("*.md")):
    if path.name == "README.md":
        continue
```

- `rglob` = **recursive** glob: searches the folder and every folder inside it.
- Plain `glob("*.md")` only checks the top level, so it would find just `README.md`.
- `sorted()` keeps the same order every run, which makes debugging easier.
- `README.md` is skipped because it describes the folder, not study content.

Quick check I used:

```python
files = sorted(p for p in DOCS_DIR.rglob("*.md") if p.name != "README.md")
print(DOCS_DIR, DOCS_DIR.exists(), len(files))   # → .../rag-docs True 68
```

- `False` → the path or folder name is wrong.
- `True` but `0` → the files are one level deeper than expected.

## 3. Split the frontmatter from the text

```python
import frontmatter

post = frontmatter.loads(path.read_text(encoding="utf-8"))
docs.append({"text": post.content, "metadata": post.metadata})
```

- `path.read_text(...)` reads the file **contents**. (Passing `path.name` or `str(path)` would parse the file *name* instead — a common slip.)
- `encoding="utf-8"` avoids errors on characters like "—" and "›".
- `post.metadata` → a dictionary, e.g. `{'title': 'SQL-Complete-Notes', 'topic': 'databases', 'source_type': 'my-notes', ...}`
- `post.content` → everything after the second `---`, the text to chunk.

**Why keep them together:** every chunk later copies its document's metadata, so an answer can say "this came from databases › SQL-Complete-Notes", and searches can filter by `topic` or `source_type`.

## 4. Data types I asked about

| Value | Type | Why |
| --- | --- | --- |
| `doc["metadata"]["source_type"]` → `"my-notes"` | `str` | YAML reads an unquoted word as text |
| `doc["metadata"]["pages"]` → `123` | `int` | YAML reads a bare number as a number |
| `doc["metadata"]` | `dict` | key → value pairs from the frontmatter |
| `docs` | `list` of `dict` | one item per file |

String comparisons are **exact and case-sensitive**: `"my-notes" == "My-Notes"` is `False`, and so is `"my-notes" == "my_notes"`.

## 5. Comparing values: `=` vs `==`

```python
source_type = doc["metadata"]["source_type"]   # = stores a value

if source_type == "my-notes":                    # == compares two values
    ...
elif source_type in ("book", "ocr"):             # shorthand for == "book" or == "ocr"
    ...
else:
    ...
```

`if source_type = "my-notes":` is a `SyntaxError`. The value needs quotes because it's a string; without them Python reads `my - notes` as subtraction.

## Result

```
68 documents loaded
```
