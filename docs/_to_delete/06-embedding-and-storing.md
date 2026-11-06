# 06 — Steps 3–4: Embedding and storing the chunks

**Goal:** turn every chunk into an embedding and save it in Chroma on disk, so questions can be answered without re-processing the notes.

**Explain it like I'm 10:** every index card gets a pin on a giant "meaning map" (the embedding), and all the cards go into a filing cabinet that sorts by meaning (Chroma). Later, a question gets a pin too, and you grab the cards nearest to it.

## The files involved

```
index.py          → builds the chunks and saves them to all_chunks.json
rag_common.py     → shared settings + models (same values in every script)
embed.py          → reads all_chunks.json, embeds, stores in chroma_db/
test_embeddings.py→ quick check that the embedding model works
```

The pipeline now has a hand-off file in the middle:

```
rag-docs/ ──index.py──► all_chunks.json ──embed.py──► chroma_db/
```

`index.py` and `embed.py` are kept separate on purpose: chunking takes seconds and I re-run it often while tuning; embedding takes minutes and only needs re-running when the chunks change. (Engineers call this *separation of concerns*.)

## 1. `rag_common.py` — one place for shared settings

```python
EMBEDDING_MODEL = "BAAI/bge-small-en-v1.5"
RERANKER_MODEL  = "BAAI/bge-reranker-v2-m3"
CHUNKS_PATH     = BASE_DIR / "all_chunks.json"
CHROMA_DIR      = BASE_DIR / "chroma_db"
COLLECTION_NAME = "rag_documents"
CANDIDATE_K = 40   # chunks fetched before reranking (was 20)
TOP_K = 5          # chunks that reach the LLM
MIN_RERANK_SCORE = 0.15   # was 0.5 — see 08-evaluation.md
```

- Anything that **must** match across scripts lives here. The embedding model is the big one: if questions and chunks are embedded with different models, their "map coordinates" don't line up.
- Models load **lazily** (`get_embeddings()`, `get_vector_store()`, `get_reranker()`): the first call creates them, later calls reuse them, and importing the file doesn't load anything heavy.
- `get_device()` picks the fastest hardware: `cuda` (NVIDIA), `mps` (Apple Silicon GPU) or `cpu`. On my Mac it's `mps`.

**Rule I learned:** a setting should be defined in exactly one file. A copy in another file silently overrides it (bug #15 in the debugging log).

## 2. Chunking upgrades in `index.py`

Since `04-chunking.md`, `index.py` gained four things:

**a. A `section` label on every chunk** (`section_label()`): the first heading of the section, or `p. 412` for page-based files. It goes into the metadata, so citations read `STUDYNOTEs/SQL-Complete-Notes.md › LEFT JOIN (LEFT OUTER JOIN)` instead of just a file name.

**b. `merge_heading_only_chunks()`**: a chunk that is only a heading line gets glued to the top of the next chunk, so it isn't a useless search result on its own.

**c. A token-based safety check** (`split_oversized_chunks()`): word counts are only an estimate of what the model reads. This uses the **embedding model's own tokenizer** to count real tokens and splits anything over `TOKEN_LIMIT = 480` (the model's limit is 512):

```python
tokenizer = AutoTokenizer.from_pretrained(EMBEDDING_MODEL)
enc = tokenizer(text, add_special_tokens=False, return_offsets_mapping=True)
```

`return_offsets_mapping=True` gives each token's start/end position in the original text, so the split slices the **original** text and keeps its formatting.

**Explain it like I'm 10:** counting words is guessing how full a lunchbox is by looking. Counting tokens is weighing it on the scale the school actually uses.

**d. Save + statistics**: `save_chunks()` writes `all_chunks.json`; `analyze_chunks()` prints sizes, token counts, heading-only chunks and the biggest documents.

```python
json.dump(chunks, f, ensure_ascii=False, indent=2, default=str)
```

`default=str` is needed because frontmatter turns a line like `date: 2026-10-01` into a Python `date` object, which JSON can't store directly.

**Result** (`python index.py`):

```
Saved 9251 chunks -> all_chunks.json
Words  -> min 8, max 349, mean 139.2, median 129
Tokens -> max 482, over 512: 0
```

Every chunk fits the embedding model.

## 3. `test_embeddings.py` — does the model work?

```bash
python test_embeddings.py
```

Embeds one sentence and prints `Embedding dimensions: 384` plus the first 5 numbers. The first run downloads the model from Hugging Face; after that it works offline.

## 4. `embed.py` — embed and store

```python
vector_store = get_vector_store()
vector_store.reset_collection()        # start fresh: no stale chunks

for i in range(0, len(all_chunks), BATCH_SIZE):      # BATCH_SIZE = 500
    batch = all_chunks[i:i + BATCH_SIZE]
    ids = [hashlib.sha256(f"{c['metadata'].get('source_file','')}:{i + j}".encode()).hexdigest()
           for j, c in enumerate(batch)]
    vector_store.add_texts(texts=[c["text"] for c in batch],
                           metadatas=[c["metadata"] for c in batch],
                           ids=ids)
```

- **`HuggingFaceEmbeddings(..., normalize_embeddings=True)`** scales every vector to length 1, so comparisons are fair and Chroma's distance can be converted to cosine similarity.
- **Batches of 500** keep memory steady and stay under Chroma's per-call limit.
- **IDs** are a SHA-256 fingerprint of the source file + chunk position.
- **`reset_collection()`** empties the collection first. Without it, a change in chunk count shifts every position, creates new IDs, and leaves the old chunks behind as stale duplicates. (Before this fix the store held 9,296 chunks while the chunker produced a different number.)

**Explain it like I'm 10:** before refiling the cabinet, empty it, so old cards don't hide among the new ones.

## 5. Checking the store

`embed.py` ends with `Total stored: N`. **N must equal the number of chunks in `all_chunks.json`.** If not, something stale is left over.

## Commands

```bash
source .venv/bin/activate
pip install python-frontmatter transformers langchain-huggingface langchain-chroma sentence-transformers

python index.py           # chunk → all_chunks.json (+ stats)
python test_embeddings.py # once: model works?
python embed.py           # embed + store → chroma_db/  (re-run whenever chunks change)
```

## Resources

- [LangChain: Chroma integration](https://python.langchain.com/docs/integrations/vectorstores/chroma/) — `add_texts`, `similarity_search_with_score`, `filter`, `reset_collection`.
- [LangChain: HuggingFace embeddings](https://python.langchain.com/docs/integrations/text_embedding/huggingfacehub/) — loading sentence-transformer models and `normalize_embeddings`.
- [BAAI/bge-small-en-v1.5 model card](https://huggingface.co/BAAI/bge-small-en-v1.5) — the embedding model: 384 dimensions, 512-token limit.
