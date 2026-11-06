# 15 — Chunk-size experiment and final results

**Goal:** decide between `CHUNK_WORDS = 300 / TOKEN_LIMIT = 480` and `200 / 400` with evidence, and record the final, tested state of the RAG.

## 1. The experiment

Changed only the chunk settings in `index.py`, then `index.py` → `embed.py` → `eval.py` → `my_eval.py`.

| Setting | Run A | Run B | Run C (final) |
| --- | --- | --- | --- |
| `CHUNK_WORDS` | 300 | **200** | 300 |
| `TOKEN_LIMIT` | 480 | **400** | 480 |
| Chunks | ~9,250 (earlier code) | **10,642** | **8,473** |
| Max chunk | 349 words / 482 tokens | 250 / 402 | 349 / 482 |

(8,473 vs ~9,250 at the same settings: `index.py` gained merging/splitting changes in between.)

## 2. Results

| Metric | 300 / 480 | 200 / 400 |
| --- | --- | --- |
| Hit rate @5 (`eval.py`) | 96% | 96% |
| Refusals (`eval.py`) | 4/4 | 4/4 |
| Complete (`my_eval.py`) | 95% | 95% |
| Citations | 20/20 | 20/20 |
| **Bank transfer score** | **0.89** | 0.28 |
| **Two pointers score** | **0.45** | 0.37 |
| **Transformer refusal score** (lower = safer) | **0.01** | 0.08 |

**Same pass rates — but 200 words shrank every borderline margin.** Bank transfer dropped to 0.28 (close to the 0.15 cutoff): smaller chunks split the ACID explanation so no single chunk held the whole "all-or-nothing" idea. The off-topic transformer question moved closer to being wrongly answered.

**Decision: keep `CHUNK_WORDS = 300`, `TOKEN_LIMIT = 480`.** 480 leaves a buffer under the model's 512-token limit (`over 512: 0`).

**Lesson (good interview example):** the pass rate didn't change, but the system got more fragile — only the detailed scores showed it.

### The harmless warning

```
Token indices sequence length is longer than the specified maximum sequence length for this model (702 > 512)
```

`split_oversized_chunks` asks the tokenizer to count a long section **so it can split it**; the tokenizer warns. The summary line `over 512: 0` confirms every stored chunk fits.

## 3. An eval fix found along the way

Back at 300 words, bank transfer showed **MISSED at 0.89**. The top chunk was `topmate System Design.pdf › p. 185` — *"CHAPTER 62 ACID … all-or-nothing"* — exactly right, but PDF chunks are labelled by **page number**, so `"ACID"` wasn't in `file › section`.

Fix in `eval.py` (line 97): also match the chunk's opening text, where PDF pages usually have their chapter heading:

```python
sources = [f"{cite(doc)} {doc.page_content[:120]}" for doc, _ in hits]
```

120 characters ≈ one heading line — targeted enough to avoid false passes from words deep in a chunk.

## 4. Run log (`eval_log.csv`)

| Time | Hit rate | Refusals | Note |
| --- | --- | --- | --- |
| 20:11 | 96% | 100% | CHUNK_WORDS 300 → 200 (10,642 chunks); Jane Doe rename; margins shrank |
| 20:29 | 93% | 100% | Back to 300 / 480 (8,473 chunks); margins restored; bank transfer MISSED only because of `p. 185` label |
| 20:33 | **96%** | **100%** | Eval matches cite + first 120 chars; bank transfer FOUND 0.89. **Final settings** |

⚠️ `eval_log.csv` currently starts at the 20:11 run — the earlier rows (runs 1–8) are no longer in the file. They're preserved in `12-evaluation.md`.

## 5. Final state of the RAG

| | Value |
| --- | --- |
| Documents | 68 Markdown files in `rag-docs/` (personal name replaced with Jane Doe) |
| Chunks | 8,473 — `CHUNK_WORDS=300`, `OVERLAP_WORDS=50`, `MIN_WORDS=40`, `TOKEN_LIMIT=480` |
| Embeddings | `BAAI/bge-small-en-v1.5`, 384 dims, normalized; embedding takes ~32 s on `mps` |
| Vector DB | Chroma, `rag_documents` collection, `reset_collection()` on every embed |
| Retrieval | 40 candidates → dedupe → `bge-reranker-v2-m3` → top 5 → drop chunks < 0.15 |
| LLM | `qwen2.5:14b` via Ollama, temperature 0 |
| Guardrails | Input checks, injection block, rule 11, `<context>` tags, citation warning (`redact_pii` off) |

| Evaluation | Result |
| --- | --- |
| `eval.py` hit rate @5 | **96%** (26/27) — only miss: "stop a function firing on every keystroke" (paraphrase; query rewriting didn't fix it) |
| `eval.py` refusals | **100%** (4/4) |
| `my_eval.py` grounded / relevant | **20/20 / 20/20** |
| `my_eval.py` complete | **95%** (COALESCE, groupby gaps) |
| `my_eval.py` retrieval relevance | **92%** |
| `my_eval.py` citations | **20/20** |
| `my_eval.py` refusals + guardrails | **6/6** |

## 6. Files that run the RAG

```bash
python index.py      # rag-docs/ → all_chunks.json         (when docs/chunking change)
python embed.py      # all_chunks.json → chroma_db/         (after index.py)
python search.py "…" --rerank                               # check retrieval (optional)
python rag.py        # the assistant
python eval.py       # fast retrieval check
python my_eval.py    # slow answer check
```

| File | Role |
| --- | --- |
| `rag_common.py` | Shared settings + models — never run directly |
| `guardrails.py` | Input/output checks — imported by `rag.py` |
| `eval.py`, `my_eval.py` | Testing only — not needed to run the RAG |
| `learningsnippets/` | `rag_starter.py`, `rag_backup.py`, `search_original.py`, `test_embeddings.py`, `tryjudge.py` — reference and experiments |
| `eval_answers.py`, `langchainindex.py` | Reference only (advanced judge version; LangChain splitter experiment) |

## 7. Still open

- [ ] Hand-check ~5 answers in `my_eval_results.json` against the judge (Class 10)
- [ ] Decide if the groupby `transform` point is too narrow
- [ ] Debounce paraphrase miss (known limitation)
- [ ] UI (`app.py` with Streamlit)
- [ ] Digital Twin: `twin-docs/`, persona prompt, hosted LLM, lighter setup (reranker ~2.3 GB), deploy
