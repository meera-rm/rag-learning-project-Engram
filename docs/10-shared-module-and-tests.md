# 10 — A shared module (`rag_common.py`) and end-to-end tests

**Goal:** stop repeating the same setup in four scripts, then prove the whole pipeline still works — including on a question my notes **can't** answer.

**Explain it like I'm 10:** four kids each wrote the same phone number on their own sticky note. If the number changes and one kid isn't told, they keep calling the wrong number and never find out. Now there's one notice on the fridge, and everyone reads it from there.

## 1. Why a shared file

The tutorial has [`helpers.py`](https://github.com/niharika2309/basic_RAG/blob/main/helpers.py): one "supply cupboard" that loads the embedder, reranker and LLM client once, with settings from `.env`, and every step script imports from it.

My setup was repeated:

| Setup | `index.py` | `embed.py` | `search.py` | `rag.py` |
| --- | --- | --- | --- | --- |
| Model name `BAAI/bge-small-en-v1.5` | ✅ (tokenizer) | ✅ | ✅ | ✅ |
| `HuggingFaceEmbeddings(..., normalize_embeddings=True)` | | ✅ | ✅ | ✅ |
| `Chroma(collection_name="rag_documents", ...)` | | ✅ | ✅ | ✅ |
| `chroma_db` path | | ✅ | ✅ | ✅ |
| `cite()` | | | ✅ | ✅ |
| Reranker | | | ✅ (MiniLM) | ✅ (bge v2-m3) |

**The dangerous case:** change the embedding model in `embed.py` and forget `rag.py`. Nothing crashes — questions are just embedded differently from the chunks, and retrieval quietly gets worse.

**Rule of thumb:** once the same setup is in 3+ files and a mismatch would break things *silently*, move it into one file. Do it before the eval script, which would be a fifth copy.

I named it `rag_common.py`, not `helpers.py`, so the name says what's in it.

## 2. What's in `rag_common.py`

| Shared item | What it is |
| --- | --- |
| `BASE_DIR`, `DOCS_DIR`, `CHUNKS_PATH`, `CHROMA_DIR`, `COLLECTION_NAME` | All paths, relative to the project folder (fixes the fragile `"./chroma_db"`) |
| `EMBEDDING_MODEL`, `RERANKER_MODEL` | Each model name written once |
| `CANDIDATE_K = 20`, `TOP_K = 5` | Retrieval sizes |
| `MIN_RERANK_SCORE = 0.5` | Below this, the best chunk probably doesn't answer the question (section 5) |
| `get_device()`, `get_embeddings()`, `get_vector_store()`, `get_reranker()` | Each model is created **the first time it's needed** ("lazy loading"), not on import |
| `vector_search()`, `rerank()` | The two retrieval steps, used by `search.py` and `rag.py` |
| `cite()` | The `source › section` label |

**What stays out:** chunking logic (`index.py`), batching (`embed.py`), prompt, rules and LLM settings (`rag.py`) — only one file uses each.

**Why lazy loading:** otherwise `embed.py`, or `rag.py --no-rerank`, would load the 2.3 GB reranker for nothing. `rag.py` still loads the reranker at startup when reranking is on (`get_reranker()` in `__main__`), so the first question isn't slow.

```python
_reranker = None

def get_reranker():
    global _reranker
    if _reranker is None:                     # first call: load it
        from sentence_transformers import CrossEncoder
        _reranker = CrossEncoder(RERANKER_MODEL, device=get_device(), max_length=512)
    return _reranker                          # later calls: reuse it
```

## 3. How each script changed

| Script | Change |
| --- | --- |
| `index.py` | Tokenizer loads `EMBEDDING_MODEL`, so chunk token counts always match the embedder. Paths come from `rag_common`. Chunking unchanged. |
| `embed.py` | ~25 lines shorter: load chunks → `get_vector_store()` → reset → store in batches. |
| `search.py` | ~15 lines instead of ~60. **Now uses the same reranker as `rag.py`** (bge v2-m3, not MiniLM), so `--rerank` shows exactly what the LLM gets. |
| `rag.py` | No more model setup at the top. `retrieve()` is 4 lines built from `vector_search()` + `rerank()`. Prompt, flags, LLM unchanged. |

Old versions are in `backups/before-rag-common/`.

## 4. Check: nothing changed that shouldn't have

```bash
python search.py "How does LEFT JOIN work?"            # vector search only
python search.py "How does LEFT JOIN work?" --rerank   # now bge v2-m3
python rag.py --dry-run "How does LEFT JOIN work?"
python rag.py "explain caching"
```

No need to re-run `index.py` or `embed.py`: same model, paths and data, so `all_chunks.json` and `chroma_db` are still valid.

**Vector search only — identical to before the refactor** (0.85, 0.81, 0.80, 0.80, 0.80, same five chunks). ✅

## 5. Surprise: the new reranker scores 0–1

MiniLM gave raw scores (`5.44`, `2.55`). **bge-reranker-v2-m3 returns 0–1** (`0.98`, `0.93`): sentence-transformers applies a sigmoid for this model automatically — the same squashing the tutorial's `helpers.py` does by hand.

So the warning "best chunk scored **below 0**" could never fire. Fixed with `MIN_RERANK_SCORE = 0.5` in `rag_common.py` (0.5 on the 0–1 scale = 0 on the raw scale, so the intent is the same).

**Explain it like I'm 10:** the old judge gave marks out of whatever they liked; the new judge marks out of 1. "Warn if below zero" never triggers on the new scale, so it became "warn if below half marks".

## 6. MiniLM vs. bge v2-m3 on "How does LEFT JOIN work?"

```
 #  was   sim  rerank  source
 1    1  0.85    0.98  SQL-Complete-Notes.md › LEFT JOIN (LEFT OUTER JOIN)
 2    6  0.80    0.93  SQL-Interview-Questions.md › Q14. What is LEFT JOIN?
 3   16  0.77    0.92  SQL-Complete-Notes.md › LEFT JOIN (LEFT OUTER JOIN)   (2nd piece)
 4    8  0.79    0.92  SQL-Complete-Notes.md › RIGHT JOIN (RIGHT OUTER JOIN)
 5    2  0.81    0.90  SQL-Interview-Questions.md › Q26. ... LEFT JOIN instead of an INNER JOIN.
```

| # | MiniLM (earlier, see 08) | bge v2-m3 (now) |
| --- | --- | --- |
| 1 | Q14. What is LEFT JOIN? (was #6) | LEFT JOIN section (was #1) |
| 2 | LEFT JOIN section | Q14 (was #6) |
| 3 | Q26 LEFT vs INNER | **LEFT JOIN 2nd piece (was #16)** — anti-joins + the "WHERE vs ON in an outer join" tip |
| 4 | LEFT JOIN 2nd piece (was #7) | RIGHT JOIN (was #8) |
| 5 | Q16. What is FULL JOIN? (was #9) | Q26 (was #2) |

Both keep 4 of 5 on LEFT JOIN. bge v2-m3 reached down to **#16** for a valuable tip (a classic mistake); RIGHT JOIN at #4 is weaker but related.

## 7. Dry run — "How does LEFT JOIN work?"

- **5 chunks** ✅, context appears **once** (only in the user message) ✅
- **~1,225 tokens** — less than my ~3,000 guess, because these chunks are shorter than the 480-token maximum. Even 5 maximum-size chunks stay well under 8,192. ✅
- Visible chunking detail: chunk [1] ends mid-code-block and chunk [3] starts with `WHERE o.order_id IS NULL;`. A long section was split at the 300-word limit inside a SQL example, so code examples sometimes arrive in two pieces.

## 8. "Explain caching" — rules 8 and 9 work

```
[1] rerank 0.97 | systemdesign/systemdesignpatterns.pdf › p. 16
[2] rerank 0.92 | STUDYNOTEs/JAVA-INTERVIEW-QUESTIONS.md › 7. What is caching and why does it improve performance?
[3] rerank 0.90 | STUDYNOTEs/JAVA-COMPLETE-NOTES.md › 24.8 Caching and performance
[4] rerank 0.83 | systemdesign/topmate System Design.pdf › p. 309
[5] rerank 0.80 | systemdesign/topmate System Design.pdf › p. 300
```

| | Before rules 8–9 (see 09) | Now |
| --- | --- | --- |
| LRU / LFU / FIFO / TTL list | Only the last item cited | **Every item cites [3]** |
| Strategies list | Mixed `[1][3]` | Every item cited |
| Ending | — | No summary citing several sources at once |

Citations are also more precise: Cache-Aside now points to [4], the chunk that explains it in depth. The last sentence ("does not grow indefinitely [3]") is a slight paraphrase beyond [3] — minor.

## 9. Off-topic control: "What is the capital of France?"

The same idea as the tutorial's "capital of Japan" question in `ragas_results.json`: a question my notes can't answer, to check the system says so instead of guessing.

```bash
python rag.py --dry-run "what is the capital of France?"   # what the LLM would get
python rag.py "what is the capital of France?"             # what it actually does
```

```
===== RETRIEVED (reranked) =====
[1] rerank   0.44 | STUDYNOTEs/NODEJS-COMPLETE-NOTES.md › GET Method Example 3 — a bigger form
[2] rerank   0.00 | STUDYNOTEs/jhu784-notes-javaspringbootnotes.pdf › p. 1276
[3] rerank   0.00 | STUDYNOTEs/DSA_Patterns_JavaScript_Study_Notes.md › 11. Graph DFS & BFS
[4] rerank   0.00 | STUDYNOTEs/jhu784-notes-javaspringbootnotes.pdf › p. 1328
[5] rerank   0.00 | STUDYNOTEs/jhu784-notes-javaspringbootnotes.pdf › p. 507
⚠️  Even the best chunk scored below 0.5 — my notes may not cover this question.

===== ANSWER =====
I couldn't find enough information in my documents.
```

- **Vector search can't say "nothing matches".** It always returns the 5 *least distant* chunks, however far away.
- **The reranker can.** Four chunks got 0.00. The Node.js chunk got 0.44 because its sample output says *"I live in the beautiful city of **Paris**"* — it mentions Paris but never says it's the capital.
- **The LLM refused** with exactly the rule 2 sentence — even though it knows "Paris" from training **and** chunk [1] contained the word. A weaker model might write "Paris [1]": outside knowledge plus a citation that doesn't support it.

**Two independent safety layers agreed:**

| Layer | Said |
| --- | --- |
| Reranker (retrieval) | best chunk 0.44 → ⚠️ warning |
| LLM (generation) | "I couldn't find enough information in my documents." |

**Explain it like I'm 10:** the student knew the answer from home, and one page even mentioned Paris. But the rule was "only use these pages", and no page says Paris is the capital — so they wrote "I can't find it in my pages". That's the honest answer.

### Is 0.5 the right threshold?

| Question | Best rerank score |
| --- | --- |
| How does LEFT JOIN work? | 0.98 |
| Explain caching | 0.97 |
| Capital of France *(off-topic)* | **0.44** |

0.5 sits in the gap, but the margin below it is small (a passing word earns partial credit). Keep 0.5 for now; check where **vague on-topic** questions land, and let the eval set decide.

**Optional later:** when the best score is below the threshold, skip the LLM and answer "I couldn't find enough information" directly (faster), and/or drop chunks scoring near 0 before they reach the LLM. Not needed for safety — 14B already refuses on its own.

## 10. Summary of today's end-to-end tests

| Test | Result |
| --- | --- |
| Specific question (LEFT JOIN) | ✅ Right chunks, accurate answer |
| Broad question (caching) | ✅ 5 complementary sources, every list item cited |
| Off-topic control (France) | ✅ Warning fired, model refused |
| Refactor (`rag_common.py`) | ✅ Vector-only results identical to before |

These four questions are the start of the eval set: I already know the right answer for each, and they cover specific, broad and off-topic.

## 11. Next: evaluation with RAGAS (step 7)

The tutorial's [`ragas_results.json`](https://github.com/niharika2309/basic_RAG/blob/main/ragas_results.json) is the output of an evaluation run: 5 questions, each with the question, retrieved chunks, answer, a human-written **reference** answer, and four scores from a "judge" LLM:

| Metric | Question it answers | Grades | Needs a reference? |
| --- | --- | --- | --- |
| **faithfulness** | Is every claim supported by the retrieved chunks? | Generation | No |
| **answer_relevancy** | Does the answer address the question? | Generation | No |
| **context_precision** | Are the useful chunks ranked near the top? | Retrieval | Yes |
| **context_recall** | Did retrieval find everything needed? | Retrieval | Yes |

Tutorial averages: faithfulness **0.73**, answer_relevancy **0.58**, context_precision **1.0**, context_recall **1.0** — retrieval perfect, generation the weak spot. Its off-topic control ("capital of Japan") scored 1.0 faithfulness but 0.22 relevancy: a low score there is the *good* outcome.

I already did faithfulness **by hand** (e.g. "null pointer exceptions [2]" in 09). RAGAS automates it.

**Plan for my notes:**
1. 10–15 questions with short reference answers from my notes — easy, vague, and 1–2 off-topic controls (start with the four above).
2. An eval script that imports `ask_rag()` / `retrieve()` and saves question, answer, chunks and reference.
3. Score with RAGAS (judge: local `qwen2.5:14b`, or a cloud model).
4. Re-run after every change (rerank on/off, model, prompt, `MIN_RERANK_SCORE`) and compare averages.

Watch out if copying the tutorial: its `get_llm_eval()` stores the same `_llm_client` as `get_llm()`, so the judge can silently reuse the main LLM client with the wrong key and URL.

## Resources

- [Tutorial `helpers.py`](https://github.com/niharika2309/basic_RAG/blob/main/helpers.py) — the shared-toolbox idea, lazy loading, sigmoid on rerank scores.
- RAGAS docs — "Metrics" (definitions and required inputs) and "Customize models" (local Ollama judge).
- Hamel Husain — "Your AI Product Needs Evals".
