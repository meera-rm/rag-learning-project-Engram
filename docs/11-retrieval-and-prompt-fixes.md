# 11 — Retrieval and prompt fixes (after `rag_common.py`)

**Goal:** finish the Step 5 checklist and tighten Step 6: dedupe on every path, a "not covered" cutoff that really stops the LLM, an OCR warning in the prompt, and clean answer endings.

**Explain it like I'm 10:** the librarian now throws out photocopied cards, the helper refuses to answer when no card is good enough, blurry photocopies get a warning sticker, and the helper stops signing every answer with a list of all the cards.

## 1. Step 5 checklist — where it stands

| # | Step 5 item | Status |
| --- | --- | --- |
| 1 | Same embedding model for questions | ✅ `rag_common.get_embeddings()` |
| 2 | Top k | ✅ `CANDIDATE_K` candidates → `TOP_K = 5` |
| 3 | Read the scores | ✅ cosine similarity + rerank score printed by `show_hits` |
| 4 | Metadata filters (`topic`, `source_type`) | ❌ not yet |
| 5 | Stop books crowding out notes | 🟡 reranker handles relevance; no explicit `my-notes` bonus |
| 6 | Remove near-duplicates | ✅ `dedupe()` on both paths |
| — | Next level: reranking | ✅ `bge-reranker-v2-m3` |

## 2. Dedupe on both paths (`rag.py`)

```python
def retrieve(question, use_rerank=True):
    candidates = dedupe(vector_search(question, CANDIDATE_K))
    if not use_rerank:
        return candidates[:TOP_K]
    return [(doc, score) for doc, _, score in rerank(question, candidates, TOP_K)]
```

- Fetch many, **then** dedupe, **then** keep 5 — deduping only 5 results could leave 4.
- `dedupe` comes from `rag_common.py`, so it must be imported: `from rag_common import ..., dedupe, ...`.
- `[:TOP_K]` is a slice: the first 5, already best-first.

## 3. The "not covered" cutoff now stops the LLM (`ask_rag`)

```python
hits = retrieve(question, use_rerank)
docs = [doc for doc, _ in hits]
user_message = build_user_message(question, docs)

if dry_run:
    return None, hits, user_message

if use_rerank and hits and hits[0][1] < MIN_RERANK_SCORE:
    return "I couldn't find enough information in my documents.", hits, user_message

response = llm.invoke([("system", SYSTEM_PROMPT), ("human", user_message)])
```

- Before, `show_hits` only **printed** a warning and the LLM still answered from weak chunks.
- The check sits **after** `dry_run`, so `--dry-run` still shows the full prompt even for weak matches.
- The real `user_message` is returned (not `""`) so anything that logs it still works.

Tested:

| Question | Best score | Result |
| --- | --- | --- |
| "What is a baseline model?" | 0.05 | Refused instantly, no LLM call |
| "How does LEFT JOIN work?" | 0.98 | Answered from SQL notes, cited |

## 4. OCR warning in the prompt

Two changes, both needed:

**Rule 10 in `SYSTEM_PROMPT`:**

```text
10. Each excerpt is labelled with its type. Excerpts marked
    source_type=ocr were read from scanned images and may contain
    OCR typos (for example "printO" for "print()"). Correct obvious
    typos in your answer, and prefer a non-OCR excerpt when two
    excerpts disagree.
```

**`source_type` in every chunk label (`build_user_message`):**

```python
f"[{i}] Source: {cite(doc)} (source_type={doc.metadata.get('source_type', 'unknown')})\n{doc.page_content}"
```

The rule is useless unless the model can see which excerpts are OCR. `.get(..., 'unknown')` avoids a crash if a chunk is missing the field.

**Explain it like I'm 10:** you tell the helper "be careful with blurry photocopies" *and* put a sticker on each blurry one.

## 5. Removing a trailing citation line

qwen2.5:14b sometimes ended answers with `[1] [2] [5]` on its own line, despite rule 9. Fixed in code:

```python
answer = re.sub(r'\n\s*(\[\d+\]\s*)+\s*$', '', response.content).strip()
```

Reads as: a newline, then one or more `[number]` groups, at the very end (`$`) → removed. Tested: removes `\n\n[1] [2] [5]` and `\n[1][2]`; leaves `Uses arr[0] and list [1] here.` alone. Needs `import re` at the top of `rag.py`.

Code is more reliable than hoping a small model follows a fiddly rule.

## 6. Example after the fixes

`python rag.py "Explain the difference between @Component and @Bean"` — 5 chunks from my own Java notes (rerank 0.86–0.99); the answer explained class-level `@Component` + component scanning vs. method-level `@Bean` in a `@Configuration` class, citing `[1][2][5]` on the list item (rule 8 working).

## 7. Settings changed since `10-shared-module-and-tests.md`

| Setting (`rag_common.py`) | Before | Now | Why |
| --- | --- | --- | --- |
| `MIN_RERANK_SCORE` | 0.5 | 0.15 | 0.5 refused real answers (scores 0.20–0.45); refusals score ≤0.05 — see `12-evaluation.md` |
| `CANDIDATE_K` | 20 | 40 | Give the reranker more candidates for paraphrased questions — **not evaluated yet** |

⚠️ `rag.py` still has its own `MIN_RERANK_SCORE` line (now 0.15). Delete it so `rag_common.py` is the only source (debugging log #15).

## Commands

```bash
python rag.py --dry-run "How does print work in Python?"   # check (source_type=...) appears in labels
python rag.py "What is a baseline model?"                  # should refuse without calling the LLM
grep -n "MIN_RERANK_SCORE =" *.py                          # should print exactly one line
```

---

# Update — filters, weak-chunk filter, query rewriting

## 8. Metadata filter: `topic=`

**What:** limit a search to one topic folder.

**Explain it like I'm 10:** instead of searching the whole library, tell the librarian "only look in the blue drawer."

`rag_common.py`:

```python
def vector_search(question, k, where=None):
    hits = get_vector_store().similarity_search_with_score(question, k=k, filter=where)
    return [(doc, 1 - dist / 2) for doc, dist in hits]
```

`where=None` is a **default value**: callers that pass two arguments (like `search.py`) still work, with no filter.

`rag.py`:

```python
def retrieve(question, use_rerank=True, use_rewrite=False, topic=None):
    where = {"topic": topic} if topic else None
    hits = vector_search(question, CANDIDATE_K, where)
    ...
```

**Test:**

```bash
python -c "from rag import retrieve; [print(round(s,2), d.metadata['source_file']) for d,s in retrieve('What is ACID?', topic='databases')]"
```

```
0.97 STUDYNOTEs/SQL-Interview-Questions.md
0.35 STUDYNOTEs/SQL-Complete-Notes.md
0.08 MongoDB.pdf
0.03 STUDYNOTEs/SQL-Interview-Questions.md
0.02 STUDYNOTEs/SQL-Complete-Notes.md
```

All 5 from `databases`; without the filter the same question pulls system design chunks.

Filter syntax for later:

| Want | `where` |
| --- | --- |
| One topic | `{"topic": "databases"}` |
| Only my notes + interview files | `{"source_type": {"$in": ["my-notes", "interview-questions"]}}` |
| Both | `{"$and": [{"topic": "databases"}, {"source_type": "my-notes"}]}` |

`eval.py` doesn't pass a topic, so the eval score is unaffected.

## 9. Dropping weak chunks before the prompt (`ask_rag`)

The ACID test showed 3 of 5 chunks scoring 0.02–0.08 still reached the LLM. Now:

```python
hits = retrieve(question, use_rerank)
if use_rerank:                                   # only rerank scores use the 0–1 cutoff
    hits = [(doc, score) for doc, score in hits if score >= MIN_RERANK_SCORE]
```

- This is a **list comprehension**: keep each `(doc, score)` pair whose score is at least 0.15. Same as a `for` loop with an `if` and `append`.
- Only for reranked results: with `--no-rerank` the scores are cosine similarity, a different scale where 0.15 means nothing.
- For ACID it turns `0.97, 0.35, 0.08, 0.03, 0.02` into `0.97, 0.35`.

**Explain it like I'm 10:** hand the helper only the cards that are actually about the question, so they don't get distracted.

⚠️ **Open bug:** the old refusal check `if use_rerank and hits and hits[0][1] < MIN_RERANK_SCORE:` is still there. After filtering, a "not covered" question leaves `hits` **empty**, so `hits and ...` is `False`, the check is skipped, and the LLM is called with no context. Replace it with:

```python
if not hits:                                     # nothing good enough → refuse
    return "I couldn't find enough information in my documents.", hits, user_message
```

## 10. Query rewriting (for paraphrased questions)

**Problem:** "How do I stop a function from firing on every keystroke?" never uses the word *debounce*, so the debounce Q&A isn't in the top 40 vector results.

**Fix:** ask the LLM to rewrite the question into the terms my notes would use, search with **both** the original and the rewrite, dedupe, then rerank against the **original** question.

```python
REWRITE_PROMPT = """Rewrite the question below as a short search query
using the technical terms a programmer's study notes would use.
Return only the query, no explanation.

Question: {question}
Search query:"""

def rewrite_query(question):
    response = llm.invoke(REWRITE_PROMPT.format(question=question))
    return response.content.strip().strip('"')

# in retrieve():
if use_rewrite:
    rewritten = rewrite_query(question)
    hits += vector_search(rewritten, CANDIDATE_K)    # merge both result lists
```

- Rerank uses the **original** question, so a bad rewrite can't push wrong chunks to the top.
- `dedupe` drops chunks both searches returned.
- Cost: one extra LLM call per question (slow with qwen2.5:14b).
- Risk: an off-topic question rewritten into jargon might match something; the refusal tests check this.

**Explain it like I'm 10:** you ask for "the thing that stops a doorbell ringing too often"; a helper translates it to "doorbell timer", and now the librarian knows which shelf to check.

**Status:** `rag.py` has it (off by default, `use_rewrite=False`); `eval.py` now calls `retrieve(..., use_rewrite=True)`. **No eval row yet.**

⚠️ The rewritten search doesn't pass `where`, so `topic=` is ignored for that half. Fix: `vector_search(rewritten, CANDIDATE_K, where)`.

## 11. Not done yet: `my-notes` bonus

Planned: rerank **all** candidates, sort with `+0.05` for `my-notes` / `interview-questions`, keep 5 — bonus for **order only**, so the 0.15 cutoff still uses the real rerank score.

## 12. Update — weak-chunk filter: both refusal checks fixed

The open bug in §9 is fixed: `ask_rag` and `show_hits` both use `if not hits:` (debugging log #25, #27).

Verified:

```bash
python rag.py "What is a baseline model?"
```
```
===== RETRIEVED (reranked) =====
⚠️  No chunk scored 0.15 or higher — my notes may not cover this question.

===== ANSWER =====
I couldn't find enough information in my documents.
```

```bash
python rag.py "What is ACID?"
```
```
[1] rerank 0.98 | systemdesign/SYSTEM-DESIGN-INTERVIEW-BOOK-DIGEST.md › 62. ACID *(p. 185)
[2] rerank 0.97 | systemdesign/topmate System Design.pdf › p. 185
[3] rerank 0.97 | STUDYNOTEs/SQL-Interview-Questions.md › Q14. What is ACID in the context of database transactions?
[4] rerank 0.44 | STUDYNOTEs/JAVA-COMPLETE-NOTES.md › 38.7 Glossary
[5] rerank 0.35 | STUDYNOTEs/SQL-Complete-Notes.md › The ACID Properties
```

All 5 scored ≥ 0.15, so none were filtered (the earlier `topic='databases'` test had 0.02–0.08 chunks because the filter limited it to one folder). The answer listed all four properties, each cited; [4] wasn't cited (rule 6 working).

**Observation for the answer-quality eval:** every bullet cited `[1][2][3][5]`. Not wrong — all four agree — but noisy. A stronger model or a rule like "cite the one or two sources that best support each claim" would tighten it.
