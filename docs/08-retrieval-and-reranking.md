# 08 — Step 5: Retrieval and reranking (`search.py`)

**Goal:** find the best 5 chunks for a question, see their scores, and test whether a reranker improves them.

## 1. What changed in `search.py`

| | Old `search.py` | Now |
| --- | --- | --- |
| Question | Hardcoded | Command line, with a default |
| Similarity math | Chroma does it | Chroma does it (its index is faster; worth understanding once, not reimplementing) |
| Passes | Top 5 only | Top 20 → cross-encoder reranker → top 5 (tested here, then added to `rag.py`) |
| Scores shown | None | Similarity + reranker relevance |

The old version is kept as `search_original.py`.

## 2. Bi-encoder vs. cross-encoder

- **Bi-encoder (bge-small, my embedding model):** turns the question and each chunk into vectors **separately**, then compares them. Fast enough for all 9,251 chunks, but it never reads the question and chunk together.
- **Cross-encoder (reranker):** reads each `(question, chunk)` pair **together** and scores how well the chunk answers. Much more accurate, too slow for 9,251 chunks.
- **So:** retrieve 20 quickly, rerank those 20 carefully, keep 5.

The rerank code is only ~6 lines — the intelligence is in the trained model (`predict()`); the rest is pair, sort, slice.

## 3. The new `search.py`

```bash
python search.py "How does LEFT JOIN work?"            # vector search only, with scores
python search.py "How does LEFT JOIN work?" --rerank   # top 20 → rerank → top 5
```

- **Similarity:** Chroma returns squared L2 distance; for length-1 vectors, `cosine = 1 - distance / 2`.
- **Reranker used for these tests:** `cross-encoder/ms-marco-MiniLM-L-6-v2` (~90 MB, downloaded on first `--rerank` run). `sentence-transformers` was already installed in `.venv`.
- **Update:** `search.py` now uses the shared reranker from `rag_common.py` (`BAAI/bge-reranker-v2-m3`, the same one `rag.py` uses), which scores 0–1. The results below are from MiniLM; the bge v2-m3 comparison is in [10-shared-module-and-tests.md](10-shared-module-and-tests.md).
- **`was` column** = position before reranking. `was` > 5 means the reranker found a chunk vector search had missed.
- Rerank scores are raw confidence values (higher = better), not 0–1. Compare them with each other only.

Harmless messages: `Redirects are currently not supported in MacOs` (PyTorch), `unauthenticated requests to the HF Hub` (no token needed; `HF_HUB_OFFLINE=1` silences it once models are cached).

## 4. Results

### "How does LEFT JOIN work?" — vector search only

```
[1] sim 0.85 | SQL-Complete-Notes.md › LEFT JOIN (LEFT OUTER JOIN)
[2] sim 0.81 | SQL-Interview-Questions.md › Q26. ... LEFT JOIN instead of an INNER JOIN.
[3] sim 0.80 | SQL-Complete-Notes.md › 34. LATERAL joins and anti-joins
[4] sim 0.80 | SQL-Complete-Notes.md › A.5 — GROUP BY & Joins (page 5)
[5] sim 0.80 | SQL-Complete-Notes.md › FULL JOIN (FULL OUTER JOIN)
```

### Same question with `--rerank`

```
 #  was   sim  rerank  source
 1    6  0.80    5.44  SQL-Interview-Questions.md › Q14. What is LEFT JOIN?
 2    1  0.85    4.10  SQL-Complete-Notes.md › LEFT JOIN (LEFT OUTER JOIN)
 3    2  0.81    3.79  SQL-Interview-Questions.md › Q26. ... LEFT JOIN instead of an INNER JOIN.
 4    7  0.79    3.08  SQL-Complete-Notes.md › LEFT JOIN (LEFT OUTER JOIN)   (2nd piece)
 5    9  0.79    2.55  SQL-Interview-Questions.md › Q16. What is FULL JOIN?
```

LEFT JOIN chunks in the top 5: **2 → 4**. The most direct answer (Q14) was at #6 and never reached the LLM before. All `sim` scores were 0.79–0.85 — basically noise to vector search — while rerank scores spread clearly from 5.44 to 2.55.

### Three more questions with `--rerank`

| Question | Pulled in from outside top 5 | Best answer at #1 |
| --- | --- | --- |
| How do I make a slow SQL query faster? | 3 (from #7, #12, #13: Query Optimization, `Q316. EXPLAIN ANALYZE`, topmate p. 251) | ✅ |
| When should I use useMemo in React? | 0 (vector search was already right; only reordered) | ✅ `04 — useMemo` |
| Difference between a process and a thread? | 1 (from #8) | ✅ `87. ... thread and a process?` (was #3, score 7.38 vs 5.54) |

**Conclusion:** reranking improved or kept quality on all 4 questions and never made it worse → added to `rag.py` (see 09).

## 5. Finding: duplicate sources

For the slow-query question, #1 and #2 were the same page twice:
- `rag-docs/system-design/topmate-system-design.md`, line 14190, `<!-- page 254 -->` (frontmatter `source_file: systemdesign/topmate System Design.pdf`, `source_type: book`)
- `rag-docs/system-design/system-design-interview-book-digest.md`, line 5818, `### 85. Slow Queries   *(p. 254)*`

The digest is my structured rewrite of the topmate book, so most chapters exist twice and can take 2 of 5 slots. The digest is cleaner (the PDF conversion dropped letter pairs, e.g. `signi cantly`). **To decide later:** remove the topmate book from `rag-docs/`, or skip near-duplicates when building the top 5.

Tip: search result names come from each file's **frontmatter** (`source_file`), not its filename. To find a chunk, search the file for `<!-- page N -->` or the heading text.

## Resources

- Sentence-Transformers docs — "Retrieve & Re-Rank" (bi-encoder vs. cross-encoder, the 20 → 5 pattern).
- Pinecone — "Rerankers and Two-Stage Retrieval".
- LangChain Chroma docs — `similarity_search_with_score`.
