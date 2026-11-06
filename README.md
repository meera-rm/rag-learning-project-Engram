# Rag Learning Project

A local study assistant that answers questions from my own notes (SQL, Java, JavaScript, React, Python, DSA, system design, AI), with citations — and says so when the notes don't cover something.

**Stack:** Python · LangChain · Chroma · `BAAI/bge-small-en-v1.5` embeddings · `BAAI/bge-reranker-v2-m3` reranker · Ollama (`qwen2.5:14b`). Everything runs on my Mac.

How it was built, step by step: [docs/README.md](docs/README.md)

## Setup (once)

```bash
cd ~/Documents/MyVault/projects/my-first-rag
python3 -m venv .venv
source .venv/bin/activate

pip install python-frontmatter transformers sentence-transformers \
            langchain-huggingface langchain-chroma langchain-ollama langchain-openai

# local LLM (install Ollama from ollama.com first)
ollama pull qwen2.5:14b
```

Activate the environment in every new terminal: `source .venv/bin/activate`.

## Build the index

Run when the documents or chunking change:

```bash
python index.py        # load + chunk rag-docs/ → all_chunks.json (prints stats)
python embed.py        # embed + store → chroma_db/ (resets the collection first)
```

`embed.py` ends with `Total stored: N` — N should equal the chunk count from `index.py`.

## Ask questions

```bash
python rag.py                                         # interactive (type 'exit' to quit)
python rag.py "How does LEFT JOIN work?"              # one question
python rag.py --dry-run "How does LEFT JOIN work?"    # show retrieved chunks + prompt, no LLM call
python rag.py --no-rerank                             # vector search only, to compare
OLLAMA_MODEL=llama3.2:3b python rag.py                # use a different local model
```

## Check retrieval

```bash
python search.py "How does LEFT JOIN work?"           # top 5 by vector search
python search.py "How does LEFT JOIN work?" --rerank  # + reranker, shows rank before/after
```

## Evaluate

```bash
python eval.py         # 32 test questions → hit rate @5 + refusal rate, appends a row to eval_log.csv
```

When asked for a note, write **what changed, old → new, and why** (e.g. `CANDIDATE_K 20 → 40 for bank transfer miss`). Change one thing per run.

## Settings

All shared settings live in `rag_common.py`: models, paths, `CANDIDATE_K`, `TOP_K`, `MIN_RERANK_SCORE`. Change them there only.

## Filtering by topic

`retrieve()` accepts a `topic` (a folder name in `rag-docs/`: `databases`, `java-spring`, `javascript-web`, `python-data`, `dsa`, `system-design`, `interview-prep`, `ai`, `projects`, `daily-concepts`):

```bash
python -c "from rag import retrieve; [print(round(s,2), d.metadata['source_file']) for d,s in retrieve('What is ACID?', topic='databases')]"
```

## Query rewriting

`retrieve(question, use_rewrite=True)` asks the LLM to rewrite the question in note-style terms and searches with both versions. Off by default in `rag.py` (one extra LLM call per question); currently on in `eval.py`.


## Run order

```bash
source .venv/bin/activate   # check: which python → my-first-rag/.venv/bin/python
python index.py             # only when docs or chunking change
python embed.py             # only after index.py ("Total stored" must match the chunk count)
python rag.py               # ask questions
python eval.py              # fast retrieval check (no LLM)
python my_eval.py           # slow answer check (LLM judge)
```

## Guardrails

`guardrails.py` (imported by `rag.py`): empty/over-long questions, prompt-injection phrases, citation validation. `redact_pii` exists but is off for study notes (it matched dates). Details: `docs/14-guardrails.md`.

## Evaluation

| Script | Checks | Latest |
| --- | --- | --- |
| `eval.py` | Retrieval hit rate @5, refusals | 96%, 100% |
| `my_eval.py` | Grounded, relevant, complete, retrieval relevance, citations, refusals + guardrails | 20/20, 20/20, 95%, 92%, 20/20, 6/6 |

## Not needed to run the RAG

`learningsnippets/` (starter script, backups, `test_embeddings.py`, `tryjudge.py`), `eval_answers.py` (advanced judge reference), `langchainindex.py` (splitter experiment). Run snippets from the project root: `python learningsnippets/tryjudge.py`.


## UI

```bash
streamlit run app.py      # chat at http://localhost:8501, sources + topic filter
```

## RAGAS (separate environment)

```bash
source .venv/bin/activate && python collect_for_ragas.py && deactivate   # answers → ragas_input.json
source .venv-ragas/bin/activate && python ragas_eval.py && deactivate    # scores → ragas_results.json
```

RAGAS runs in `.venv-ragas` because its dependencies clash with the RAG's (`docs/16-ragas.md`). Latest (3 Qs): relevancy 0.91, precision 0.92, recall 0.92, faithfulness 0.67 — faithfulness underscored by the small judge (checked by hand).

## Command history — RAGAS setup (Nov 5)

The exact commands run to set up RAGAS without breaking the RAG, in order. Details: `docs/16-ragas.md`, debugging log #40–43.

### 1. Clean the main environment (RAGAS had been installed into it)

```bash
source .venv/bin/activate
python -m pip uninstall -y ragas datasets       # remove RAGAS + datasets from the RAG's environment
python -m pip install "huggingface-hub<2"       # datasets had upgraded it to 2.4.0; langchain-huggingface needs <2
python -m pip check                             # should say: No broken requirements found
python collect_for_ragas.py                     # runs ask_rag() → writes ragas_input.json
deactivate
```

### 2. Create a separate RAGAS environment and score

```bash
python3 -m venv .venv-ragas
source .venv-ragas/bin/activate
python -m pip install ragas datasets langchain-ollama langchain-huggingface sentence-transformers "langchain-community>=0.4,<0.4.2"
python ragas_eval.py                            # reads ragas_input.json → prints scores, writes ragas_results.json
deactivate
```

`langchain-community<0.4.2` because ragas 0.4.3 imports `chat_models.vertexai`, which 0.4.2 removed.

### 3. Commands run with no environment active (mistake — no harm done)

```bash
python -m pip uninstall -y ragas datasets       # "Skipping ragas as it is not installed"
python -m pip install "huggingface-hub<2"       # went to ~/.pyenv system Python: "already satisfied"
python -m pip check
python rag.py "What is ACID?"                   # ModuleNotFoundError: No module named 'langchain_ollama'
```

The prompt had no `(.venv)` after `deactivate`, so these used the system Python. Fix:

```bash
source .venv/bin/activate
which python                                    # → my-first-rag/.venv/bin/python
python rag.py "What is ACID?"                   # works again
```

### 4. Running RAGAS from now on (one line per step)

```bash
source .venv/bin/activate && python collect_for_ragas.py && deactivate
source .venv-ragas/bin/activate && python ragas_eval.py && deactivate
```

## Why RAGAS has its own environment (and the one-environment option)

Installing RAGAS into `.venv` caused two clashes: `datasets` upgraded `huggingface-hub` to 2.4.0 (the RAG's `langchain-huggingface` needs < 2), and ragas 0.4.3 needs `langchain-community` ≤ 0.4.1. Keeping RAGAS in `.venv-ragas` leaves the RAG exactly as tested.

### If you really want one environment

It could work with careful pins, because both clashes have versions in common:

```bash
source .venv/bin/activate
python -m pip install ragas datasets "huggingface-hub<2" "langchain-community>=0.4,<0.4.2"
python -m pip check
```

Then re-run `eval.py` and `my_eval.py` to confirm nothing changed. The catch: any later `pip install` might upgrade those packages again and break things silently, as happened before. You'd need to keep those pins in a `requirements.txt` and always install from it (`python -m pip install -r requirements.txt`). Details: `docs/16-ragas.md` §9.

## Third-party files replaced with my own notes
22 files written by other authors were moved unchanged to `rag-docs-excluded/` and replaced by
22 study-notes files in my own words (`*-notes.md`, `note_kind: study-notes`).
Details, mapping and checks: `docs/18-third-party-content-and-study-notes.md`.
After this change, re-run: `python index.py` → `python embed.py` → `python eval.py` → `python my_eval.py`.
