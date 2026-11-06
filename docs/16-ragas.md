# 16 — RAGAS: a standard second opinion on answer quality

**Goal:** score the RAG with **RAGAS**, a standard library of LLM-judge metrics, and compare it with my own `my_eval.py`.

## 1. RAGAS metrics vs `my_eval.py`

| RAGAS metric | Closest `my_eval.py` check | Measures |
| --- | --- | --- |
| `faithfulness` | `check_grounded` | Share of the answer's claims supported by the retrieved chunks (extracts claims first) |
| `answer_relevancy` | `check_relevant` | Does the answer address the question? (uses embeddings) |
| `context_precision` | `check_retrieval` | Are the useful chunks ranked near the top? |
| `context_recall` | — | Do the chunks contain everything in my reference answer? |

**RAGAS does not test** refusals, guardrails or citation format — `my_eval.py` stays the main answer check.

## 2. Setup problems (and why RAGAS has its own environment)

| Problem | Cause | Fix |
| --- | --- | --- |
| `ModuleNotFoundError: No module named 'langchain_community.chat_models.vertexai'` | `ragas 0.4.3` still imports a file that `langchain-community 0.4.2` removed — a known bug (ragas issue #2745) | Use `langchain-community>=0.4,<0.4.2` (0.4.1) |
| `langchain-huggingface … requires huggingface-hub<2.0.0, but you have 2.4.0` | Installing RAGAS pulled in `datasets 5.1.0`, which upgraded `huggingface-hub` to 2.4.0 — breaking my RAG's requirements | Uninstall `ragas datasets` from the main `.venv`, then `pip install "huggingface-hub<2"` |
| Pinning inside the main `.venv` didn't stick, and versions kept clashing | Two tools with different dependency needs in one environment | **A separate `.venv-ragas`** |

**Decision:** keep my RAG's `.venv` exactly as it was when all evals passed, and give RAGAS its own environment. `.venv-ragas` is in `.gitignore`.

## 3. The two-step flow

```
.venv        collect_for_ragas.py  →  ragas_input.json   (runs my real ask_rag)
.venv-ragas  ragas_eval.py         →  ragas_results.json (RAGAS scores, never imports my RAG)
```

### Step 1 — `collect_for_ragas.py` (main `.venv`)

```python
import json
from rag import ask_rag

TESTS = [
    {"question": "How does LEFT JOIN work?",
     "reference": "LEFT JOIN returns all rows from the left table and matching rows from the right; "
                  "where there is no match, the right table's columns are NULL."},
    {"question": "What is the difference between WHERE and HAVING?",
     "reference": "WHERE filters rows before grouping; HAVING filters groups after GROUP BY."},
    {"question": "What does the volatile keyword do in Java?",
     "reference": "volatile marks a variable that can be changed by different threads, and makes "
                  "changes to it immediately visible to other threads."},
]

rows = []
for t in TESTS:
    answer, hits, _ = ask_rag(t["question"])
    rows.append({"question": t["question"], "answer": answer,
                 "contexts": [doc.page_content for doc, _ in hits] or ["(no context retrieved)"],
                 "ground_truth": t["reference"]})
with open("ragas_input.json", "w") as f:
    json.dump(rows, f, indent=2, ensure_ascii=False)
```

Uses the **real** `ask_rag()` — guardrails, reranker and refusal cutoff included — so the scores describe the app I built.

### Step 2 — `ragas_eval.py` (`.venv-ragas`)

```python
rows = json.load(open("ragas_input.json"))
data = {k: [r[k] for r in rows] for k in ("question", "answer", "contexts", "ground_truth")}

judge = LangchainLLMWrapper(ChatOllama(model="llama3.1:8b", temperature=0))
embeddings = LangchainEmbeddingsWrapper(HuggingFaceEmbeddings(
    model_name="BAAI/bge-small-en-v1.5", encode_kwargs={"normalize_embeddings": True}))

result = evaluate(Dataset.from_dict(data),
                  metrics=[faithfulness, answer_relevancy, context_precision, context_recall],
                  llm=judge, embeddings=embeddings)
result.to_pandas().to_json("ragas_results.json", orient="records", indent=2)
```

- `LangchainLLMWrapper` lets RAGAS use my local Ollama judge instead of OpenAI.
- Same embedding model as the RAG (`bge-small`) for `answer_relevancy`.
- Old-style field names (`question`, `answer`, `contexts`, `ground_truth`); newer RAGAS uses `user_input`, `response`, `retrieved_contexts`, `reference`.

## 4. Results

### Run 1 — 3 questions, including a refusal question

| Metric | Score |
| --- | --- |
| faithfulness | 0.83 |
| answer_relevancy | 0.56 |
| context_precision | 0.65 |
| context_recall | 0.67 |

The refusal question ("What is a baseline model?") dragged everything down: RAGAS scores "I couldn't find enough information" as **irrelevant**, and has only the placeholder `"(no context retrieved)"` for the context metrics. RAGAS isn't built to score refusals — `my_eval.py` tests those (6/6). **Removed it.**

### Run 2 — 3 covered questions (judge llama3.1:8b)

| Metric | Score |
| --- | --- |
| answer_relevancy | **0.91** |
| context_precision | **0.92** |
| context_recall | **0.92** |
| faithfulness | **0.67** |

Per question:

| Question | Faithfulness | Relevancy | Precision | Recall |
| --- | --- | --- | --- | --- |
| LEFT JOIN | **0.25** | 0.92 | 0.95 | 1.00 |
| WHERE vs HAVING | 0.75 | 0.85 | 0.80 | 1.00 |
| volatile | 1.00 | 0.97 | 1.00 | 0.75 |

## 5. Faithfulness is a judge error — checked by hand

**RAGAS (3 Qs, judge llama3.1:8b): relevancy 0.91, precision 0.92, recall 0.92, faithfulness 0.67. Faithfulness is a judge error: LEFT JOIN scored 0.25 but every claim is in its chunks (checked by hand); my_eval grounded check agrees it's grounded. Small judges underscore RAGAS faithfulness, especially with code.**

Claims in the LEFT JOIN answer, checked against the 5 chunks it was given:

| Claim | In the chunks? |
| --- | --- |
| Example query `employees e … d.department_id` | ✅ |
| "where no department is assigned … NULL" | ✅ |
| Use LEFT JOIN instead of INNER JOIN "even if there is no match" | ✅ |

WHERE vs HAVING (0.75): "aggregate functions" and `COUNT(*) > 2` are both in its chunks too.

**Why it happens:** RAGAS faithfulness asks the judge to split the answer into claims and verify each one. An 8B model is weak at this, especially with code — it often fails to match a SQL query in the answer to the same query in a chunk.

**Lesson (Class 10):** treat judge scores as evidence; when judges disagree (`my_eval.py` grounded ✓ vs RAGAS 0.25), check the source yourself. Here the disagreement came from the evaluator, not the RAG.

## 6. Warnings

`DeprecationWarning`s for `ragas.metrics`, `LangchainLLMWrapper` and `LangchainEmbeddingsWrapper`: still supported in 0.4.3, removal planned for v1.0. Safe to ignore now; if a RAGAS upgrade breaks the script, switch to `ragas.metrics.collections` and `llm_factory`.

## 7. Next

- [ ] Add "What is ACID?" back (it was deleted along with the refusal question) and grow to 8–10 questions
- [ ] Stronger judge for faithfulness (bigger local model, or a hosted model) — or rely on `my_eval.py` grounded + hand checks
- [ ] Citation format: the LEFT JOIN answer cited `[1, 5]`; `check_citations` only recognises `[1][5]` → prompt rule or regex update

## Commands

```bash
# Step 1 — main environment
source .venv/bin/activate && python collect_for_ragas.py && deactivate
# Step 2 — RAGAS environment
source .venv-ragas/bin/activate && python ragas_eval.py && deactivate

# one-time setup of .venv-ragas
python3 -m venv .venv-ragas
source .venv-ragas/bin/activate
python -m pip install ragas datasets langchain-ollama langchain-huggingface sentence-transformers "langchain-community>=0.4,<0.4.2"
```

## Resources

- [RAGAS: Available metrics](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/) — how each metric is computed.
- [Pinning fix for the vertexai import](https://github.com/decko/raki/pull/337) — same bug in another project.

---

## 9. Why not just use the regular `.venv`? (and how, if you really want to)

Two packages clashed when RAGAS went into the RAG's environment:

| Clash | RAG needs | RAGAS side needs | Common version? |
| --- | --- | --- | --- |
| `huggingface-hub` | `langchain-huggingface`: **< 2.0** | `datasets`: ≥ 1.31, < 3.0 | ✅ e.g. 1.33 — but pip picked the newest (2.4.0) and broke the RAG |
| `langchain-community` | had 0.4.2 | ragas 0.4.3: **≤ 0.4.1** (imports the removed `chat_models/vertexai.py`) | ✅ 0.4.1 |

### Why a separate environment is the safer choice

- The RAG's `.venv` is the one that passed every eval (hit rate 96%, grounded 20/20, refusals 6/6). Changing its packages means re-testing everything.
- RAGAS is only an evaluation tool — it shouldn't change the app's dependencies.
- RAGAS and the RAG can be upgraded independently.

### If you really want one environment

It could work with careful pins, because both clashes have versions in common:

```bash
source .venv/bin/activate
python -m pip install ragas datasets "huggingface-hub<2" "langchain-community>=0.4,<0.4.2"
python -m pip check
```

Then re-run `eval.py` and `my_eval.py` to confirm nothing changed.

**The catch:** any later `pip install` might upgrade those packages again and break things silently, as happened before. You'd need to keep those pins in a `requirements.txt` and always install from it:

```text
# requirements.txt (excerpt)
huggingface-hub<2              # langchain-huggingface requires <2
langchain-community>=0.4,<0.4.2  # ragas 0.4.3 imports chat_models.vertexai (removed in 0.4.2)
```

```bash
python -m pip install -r requirements.txt
```

**Decision:** keep two environments — one extra command, and the RAG stays exactly as tested.
