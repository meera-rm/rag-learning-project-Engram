# 07 — Step 3–4: Embedding the chunks and storing them in Chroma (`embed.py`)

**Goal:** turn each of the 9,251 chunks into a vector ("meaning fingerprint") and store them in a Chroma vector database on disk.

## 1. How `embed.py` works

| | My `embed.py` |
| --- | --- |
| Input | `all_chunks.json` (9,251 chunks) |
| Model | `BAAI/bge-small-en-v1.5`, 384 numbers, local via LangChain |
| Normalization | `normalize_embeddings=True` |
| Batching | Loop of 500 with progress |
| Storage | Chroma in `./chroma_db` |
| IDs | `sha256("source_file:position")` |
| Search later | Chroma's HNSW index |

**Why these choices fit me:**
- **bge-small** was trained for search (question → passage). MiniLM is general-purpose. Both are 384 numbers.
- **Normalization** makes every vector length 1, so comparing them = cosine similarity (the angle between them). bge recommends it.
- **Why Chroma:** 9,251 × 384 numbers as JSON would be ~70 MB and every question would loop over all of them. Chroma stores them efficiently, indexes them, and can filter by metadata.
- **Batches of 500:** keeps memory steady and stays under Chroma's insert limit.
- **The same model must be used in `search.py` and `rag.py`.** It is.

## 2. Changes made today

1. **Load from `all_chunks.json`** instead of calling `build_chunks()` — no re-chunking or tokenizer load just to re-embed.
2. **Removed `from index import build_chunks`.** Importing a module runs its top-level code, so it loaded the tokenizer for nothing.
3. **`vector_store.reset_collection()` before adding.** My IDs come from *position*. When the chunk count dropped from 9,296 to 9,251, the last 45 old IDs would never be overwritten and stale damaged chunks would stay in Chroma.
4. **Paths relative to the script** (`BASE_DIR`), a `main()` function with an `if __name__ == "__main__":` guard, timing, and a sample vector print.

Still to tidy: `persist_directory` is defined at the top but `Chroma(...)` still uses the literal `"./chroma_db"`.

## 3. Commands

```bash
rm -rf chroma_db       # delete the old vector store (only needed before reset_collection was added)
python embed.py        # embed all chunks and store them
```

## 4. Result

```
Embedded 9251 chunks in 34.4 s
Each embedding has 384 numbers. First 8: [-0.081, -0.054, 0.022, 0.027, 0.045, -0.018, -0.078, 0.003]
Total stored: 9251
```

- **9,251 out of `index.py` = 9,251 in Chroma** → no stale chunks, no ID collisions.
- **34.4 s** ≈ 270 chunks per second, so re-embedding after a chunking change is cheap.
- **Small numbers** like -0.081 are expected: the vector has length 1, spread over 384 numbers. No single number means anything; meaning is in the direction of all 384 together.

## Resources

- BAAI `bge-small-en-v1.5` model card (Hugging Face) — why normalize, benchmark results.
- LangChain Chroma docs — `add_texts`, `reset_collection`, metadata filtering.
- [Pinecone — What is a Vector Database?](https://www.pinecone.io/learn/vector-database/) — why an index beats a JSON file at thousands of vectors.
