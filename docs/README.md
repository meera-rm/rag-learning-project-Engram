# My First RAG — Project Docs

A record of how I built my first RAG (Retrieval-Augmented Generation) system over my own study notes: what I did, the commands I ran, and why each step works the way it does.

## What this project does

It turns 68 Markdown files of study notes (SQL, Java, JavaScript, React, Python, DSA, system design, AI) into ~9,250 searchable chunks, stores them in a local vector database (Chroma), and answers questions with a local LLM (qwen2.5:14b via Ollama) **only from my notes**, with citations — or says the notes don't cover it.

## Progress

| Step | What | Status | Doc |
| --- | --- | --- | --- |
| 0 | Prepare the documents (`rag-docs/`) | ✅ | [01-preparing-rag-docs.md](01-preparing-rag-docs.md) |
| 0 | Project setup and environment | ✅ | [02-project-setup.md](02-project-setup.md) |
| 1 | Load documents + metadata | ✅ | [03-loading-documents.md](03-loading-documents.md) |
| 2 | Chunk the documents | ✅ | [04-chunking.md](04-chunking.md) |
| 2 | Chunker improvements (section labels, token check, `all_chunks.json`) | ✅ | [06-chunking-improvements.md](06-chunking-improvements.md) |
| 3–4 | Embed + store in Chroma | ✅ | [07-embedding.md](07-embedding.md) |
| 5 | Retrieval and reranking | ✅ | [08-retrieval-and-reranking.md](08-retrieval-and-reranking.md) |
| 6 | Generating answers, choosing the LLM | ✅ | [09-generating-answers.md](09-generating-answers.md) |
| — | Shared module (`rag_common.py`) + end-to-end tests | ✅ | [10-shared-module-and-tests.md](10-shared-module-and-tests.md) |
| 5–6 | Dedupe, "not covered" cutoff, OCR warning, answer cleanup | ✅ | [11-retrieval-and-prompt-fixes.md](11-retrieval-and-prompt-fixes.md) |
| 7 | Evaluation + run log | 🟡 Retrieval eval done; answer-quality eval next | [12-evaluation.md](12-evaluation.md) |
| — | Every bug and its fix | ✅ | [05-debugging-log.md](05-debugging-log.md) |

## Project layout

```
my-first-rag/
├── README.md            # how to run the project
├── rag-docs/            # 68 cleaned Markdown files in 10 topic folders
├── rag_common.py        # shared settings + models (one source of truth)
├── index.py             # Steps 1–2: load + chunk → all_chunks.json
├── all_chunks.json      # the chunks (hand-off between index.py and embed.py)
├── embed.py             # Steps 3–4: embed + store → chroma_db/
├── chroma_db/           # the vector database
├── search.py            # check retrieval (with or without reranker)
├── rag.py               # Steps 5–6: the study assistant
├── eval.py              # Step 7: test set + scoring
├── eval_log.csv         # one row per eval run, with notes
├── test_embeddings.py   # quick check the embedding model works
├── docs/                # these notes
├── .env, .gitignore, .venv/
```

## Current numbers

| | Value |
| --- | --- |
| Chunks | 9,251 (max 349 words / 482 tokens, none over 512) |
| Embedding model | BAAI/bge-small-en-v1.5 (384 dims) |
| Reranker | BAAI/bge-reranker-v2-m3 |
| Retrieval | 40 candidates → dedupe → rerank → top 5, refuse below 0.15 |
| LLM | qwen2.5:14b (Ollama, local) |
| Latest eval | Hit rate @5 93%, refusals 100% (32 questions) |

## To-do

- [ ] Delete the duplicate `MIN_RERANK_SCORE` line in `rag.py`
- [ ] Run `eval.py` for `CANDIDATE_K = 40` (already set) and log it
- [ ] Fix the two paraphrase misses (bank transfer, debounce) — hybrid search if needed
- [ ] Answer-quality eval (correctness, groundedness)
- [ ] Add the AI class transcripts as a new source

## Update — 

- ✅ Duplicate `MIN_RERANK_SCORE` removed from `rag.py` — `rag_common.py` is the only source now
- ✅ `CANDIDATE_K = 40` evaluated (run 7): bank transfer score 0.55 → 0.89; answer key widened (run 8) → **hit rate @5 96%, refusals 100%**
- ✅ `topic=` metadata filter added (doc 11 §8)
- ✅ Weak chunks (< 0.15) dropped before the prompt (doc 11 §9)
- 🟡 Query rewriting added, on in `eval.py`, **not evaluated yet** (doc 11 §10)
- ⚠️ Open bugs: refusal check after filtering (#25), rewrite ignores `topic` (#26) — see `05-debugging-log.md`

Updated to-do:

- [ ] Fix bug #25: `if not hits:` in `ask_rag`
- [ ] Fix bug #26: pass `where` to the rewritten search
- [ ] Run `eval.py` with query rewriting and log it
- [ ] `my-notes` bonus (+0.05, sort only)
- [ ] Answer-quality eval (grade 10 answers by hand first)
- [ ] Add the AI class transcripts as a new source

**Later Nov 5:** ✅ bug #25 fixed (`if not hits:` in `ask_rag`), ✅ #27 fixed (warning in `show_hits`), both verified with "What is a baseline model?" (refused) and "What is ACID?" (answered). Still open: #26 (rewrite ignores `topic`), eval run with query rewriting.


## Update —: answer evaluation, guardrails, final settings

| Doc | What |
| --- | --- |
| [13-answer-evaluation.md](13-answer-evaluation.md) | `my_eval.py`: built step by step with `tryjudge.py`; grounded, relevant, complete, retrieval, citations, refusals; results |
| [14-guardrails.md](14-guardrails.md) | `guardrails.py`, rule 11, `<context>` tags, citation warning, why `redact_pii` is off, personal-data scan + Jane Doe rename |
| [15-chunk-size-experiment-and-final-results.md](15-chunk-size-experiment-and-final-results.md) | 300 vs 200 words (kept 300/480), `eval.py` PDF-label fix, final state, which files run the RAG |
| [05-debugging-log.md](05-debugging-log.md) | Part 3: bugs #28–39 (judge in a comment, misplaced `"""`, lenient judge, `KeyError`, wrong `.venv`, …) |

**Final results:** hit rate @5 **96%**, refusals **100%** (`eval.py`); grounded **20/20**, relevant **20/20**, complete **95%**, citations **20/20**, refusals + guardrails **6/6** (`my_eval.py`).

**Final settings:** `CHUNK_WORDS=300`, `TOKEN_LIMIT=480`, 8,473 chunks, `CANDIDATE_K=40`, `TOP_K=5`, `MIN_RERANK_SCORE=0.15`, qwen2.5:14b answers, llama3.1:8b judges.

To-do:
- [ ] Hand-check ~5 judged answers (Class 10)
- [ ] Decide on the groupby `transform` test point
- [ ] UI (`app.py`, Streamlit)
- [ ] Digital Twin


## Update —: RAGAS + UI

| Doc | What |
| --- | --- |
| [16-ragas.md](16-ragas.md) | RAGAS as a second opinion: why it has its own `.venv-ragas`, the two-step flow, results, and the faithfulness judge error found by hand |
| [17-streamlit-ui.md](17-streamlit-ui.md) | `app.py` chat UI: caching, session state, sources, topic filter |
| [05-debugging-log.md](05-debugging-log.md) | Part 4: bugs #40–46 (RAGAS import bug, dependency clash, no venv active, refusal drag, `[1, 5]` citations, topic dropdown) |

**RAGAS (3 Qs, judge llama3.1:8b):** relevancy 0.91, precision 0.92, recall 0.92, faithfulness 0.67. Faithfulness is a judge error: LEFT JOIN scored 0.25 but every claim is in its chunks (checked by hand); my_eval grounded check agrees it's grounded. Small judges underscore RAGAS faithfulness, especially with code.

To-do:
- [ ] Add "What is ACID?" back to `collect_for_ragas.py`; grow to 8–10 questions
- [ ] Citation format `[1, 5]` (bug #45)
- [ ] Hand-check ~5 `my_eval.py` answers
- [ ] Digital Twin
