# 12 — Step 7: Evaluation (`eval.py`)

**Goal:** prove with a fixed question set that retrieval finds the right notes and refuses what isn't there — and record every run so changes can be compared.

## 1. What `eval.py` measures

| Metric | Question type | PASS when |
| --- | --- | --- |
| **Hit rate @5** | Covered by my notes (`expect` = list of words) | An expected word appears in a top-5 `file › section` **and** the best score ≥ `MIN_RERANK_SCORE` |
| **Refusal rate** | Not in my notes (`expect = None`) | Best score < `MIN_RERANK_SCORE` (the RAG would say "not covered") |

It calls the real `retrieve()` with the reranker on, but **no LLM**, so a full run is quick. Answer quality (correctness, groundedness — the LangSmith evaluator types noted at the top of `eval.py`) is a later step; retrieval has to be right first.

Labels in the output:

| Label | Meaning |
| --- | --- |
| `FOUND` | Right section in top 5, score high enough |
| `LOW SCORE` | Right section found, but the score is below the cutoff, so `rag.py` would refuse |
| `MISSED` | Right section not in the top 5 (the `got:` line shows what came back) |
| `REFUSED` | Trick question correctly refused |
| `ANSWERED?!` | Trick question scored high enough to be answered — bad |

**PASS on a trick question means the system did the right thing** (refused), not that it found an answer.

## 2. The test set (32 questions)

| Group | Examples | Tests whether… |
| --- | --- | --- |
| Basic | WHERE vs HAVING, LEFT JOIN, @Component vs @Bean, consistent hashing | Easy questions work |
| Exact terms | RANK vs DENSE_RANK, COALESCE, `volatile`, Promise.all, fillna | Exact jargon is still found |
| Paraphrased | "customers who never placed an order", "stop a function firing on every keystroke", "bank transfer all-or-nothing" | Retrieval understands meaning, not just keywords |
| Books / OCR | MongoDB aggregation pipeline, PySpark read CSV, XSS, Actuator, sharding | Content only in big books or scanned PDFs is reachable |
| Refusals | Rust borrow checker, baseline model, transformer, sourdough bread | Uncovered topics are refused |

Each expected file was checked in `rag-docs` before the question was added.

## 3. The run log (`eval_log.csv`)

Every run appends one row; the script asks for a note describing what changed.

| # | Time | Hit rate @5 | Refusals | Note (what changed) |
| --- | --- | --- | --- | --- |
| 1 | 11-05 15:46 | 100% | 100% | Baseline: TOP_K=5, CANDIDATE_K=20, rerank on (bge-reranker-v2-m3), MIN_RERANK_SCORE=0.5, 14 questions |
| 2 | 15:55 | 93% | 100% | Test set v2 (32 Qs). Misses: bank transfer (SQL chunk not retrieved), transformer (bad test). Two pointers 0.45 + debounce 0.20 found but below threshold |
| 3 | 15:58 | 86% | 100% | Eval now requires score ≥ MIN_RERANK_SCORE (0.5) for a pass. 24/28 |
| 4 | 16:01 | 89% | 100% | Transformer test → refusal (notes only mention the `sentence-transformers` library). No pipeline changes |
| 5 | 16:03 | 96% | 100% | MIN_RERANK_SCORE 0.5 → 0.15 (gap between refusals ≤0.01 and weakest real hit 0.20) |
| 6 | 16:10 | 93% | 100% | Eval matches `file › section`; debounce test expects "debounc" (was a false pass at file level) |

### Reading the log

- **Run 1 → 2:** the score dropped because the **test got harder** (14 → 32 questions), not because the system got worse. That's why notes matter.
- **Run 3:** the eval became stricter. "Found the file" isn't enough if `rag.py` would still refuse because of a low score. The honest number went down.
- **Run 4:** a failing test was **wrong**: the expected answer wasn't in my notes. Fixing the answer key, not the code, was correct.
- **Run 5:** reranker scores showed refusals at 0.00–0.05 and the weakest real hits at 0.20–0.45, so 0.5 was refusing real answers. 0.15 sits in the gap.
- **Run 6:** matching only the file name gave a **false pass**: the debounce question "found" `JAVASCRIPT-INTERVIEW-QUESTIONS.md`, but not the debounce section. Matching `file › section` made the score honest again.

### Note on run 5
Its note says the duplicate `MIN_RERANK_SCORE = 0.5` in `rag.py` was removed, but at that time it was still 0.5 there, so the eval used 0.15 while the real app used 0.5. `rag.py` line 11 now says 0.15, but it is still a **second copy** — delete it so `rag_common.py` is the only source (debugging log #15).

## 4. Open problems

| Question | Status | Likely cause | Next experiment |
| --- | --- | --- | --- |
| "Why should a bank transfer be all-or-nothing?" | MISSED | `SQL-Complete-Notes` has a "bank transfer example" section, but system-design chunks about distributed transactions win the vector search | `CANDIDATE_K` 20 → 40 (already set in `rag_common.py`; **not evaluated yet**), then hybrid keyword search |
| "How do I stop a function from firing on every keystroke?" | MISSED | Matches the literal words "every keystroke" in "Form events", not the debounce Q&A | Same as above |

Both are **paraphrase problems**: the question never uses the notes' key word ("atomicity", "debounce").

## 5. How to run an experiment

1. Change **one** thing (a setting, the chunking, the prompt).
2. If chunking or the embedding model changed: `python index.py` then `python embed.py`.
3. `python eval.py`
4. Note format: **what changed, old → new, why** — e.g. `CANDIDATE_K 20 → 40 for bank transfer miss`.
5. Compare with the previous row before changing anything else.

## Commands

```bash
python eval.py      # run all tests, print results, append a row to eval_log.csv
```

To add a test, add a tuple to `TESTS` — every entry needs a question **and** an expectation, with a trailing comma:

```python
("Your question?", ["word-in-file-or-section"]),   # should be found
("Your question?", None),                           # should be refused
```

## Resources

- [LangSmith: Evaluate a RAG application](https://docs.langchain.com/langsmith/evaluate-rag-tutorial) — the correctness / relevance / groundedness / retrieval-relevance evaluators noted at the top of `eval.py`; the next step after retrieval checks.
- [Pinecone: Evaluation measures in information retrieval](https://www.pinecone.io/learn/offline-evaluation/) — hit rate, recall@k, MRR and other retrieval metrics.

---

# Update — runs 7 and 8

| # | Time | Hit rate @5 | Refusals | Note (what changed) |
| --- | --- | --- | --- | --- |
| 7 | 11-05 16:23 | 93% | 100% | `CANDIDATE_K` 20 → 40 for bank transfer + debounce misses |
| 8 | 16:28 | 96% | 100% | Bank transfer test also accepts the "ACID" section; debounce = known paraphrase limit |

### Reading runs 7–8

- **Run 7 — `CANDIDATE_K` 20 → 40:** same 25/27, but **bank transfer's best score rose 0.55 → 0.89**. With 40 candidates the reranker found `SYSTEM-DESIGN-INTERVIEW.md › 62. ACID` and `› 70. Transactions` — sections that really answer "all-or-nothing" (atomicity). Nothing else changed and all refusals stayed at 0.00–0.02, so 40 is kept.
- **Run 8 — answer key widened:** the expected list for bank transfer gained `"ACID"`. This is different from the transformer case: there nothing correct came back; here the retrieved chunks **are** correct, just from a different file than the key named.

- **Debounce:** still 0.20 with the same 5 chunks ("Form events", `useCallback`, timers) in both runs — the debounce Q&A isn't even in the top 40. More candidates can't fix a phrasing gap → query rewriting (doc 11, §10).

### Updated open problems

| Question | Status | Next |
| --- | --- | --- |
| Bank transfer | ✅ FOUND (0.89) since run 8 | — |
| Stop a function firing on every keystroke | MISSED (0.20) | Eval with `use_rewrite=True` (already set in `eval.py`, not run yet) |

### Step 7 status

| Part | Status |
| --- | --- |
| Retrieval eval (hit rate @5, refusals, run log) | ✅ 96% / 100% |
| Answer-quality eval (correct? grounded? right citations?) | ❌ next — start by grading 10 `rag.py` answers by hand, log as `scenario = answers-manual` |

### Next run

`eval.py` already calls `retrieve(question, use_rerank=True, use_rewrite=True)`. Run it with the note:

```
query rewriting ON (original + rewritten search, rerank on original)
```

Expect: slower; debounce hopefully FOUND; check all 4 refusals still pass.
