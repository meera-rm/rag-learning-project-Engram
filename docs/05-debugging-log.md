# 05 — Debugging log

Every bug I hit, what it looked like, why it happened, and the fix. Newest last.

## 1. Code pasted out of order → `NameError`

**Symptom:** the pattern-picking code used `doc` and `text` at the top of the file, before any documents were loaded.

**Why:** Python runs top to bottom. `doc` only exists *inside* `for doc in docs:`, after `docs` is loaded.

**Fix:** put code in order — settings → functions → a "Run" block at the bottom that calls them. Per-document code goes **inside** the loop.

**Explain it like I'm 10:** I was trying to read a notebook's label before taking it off the shelf.

## 2. Two statements glued together → `SyntaxError`

**Symptom:** `lines = text.split('\n')docs = []`

**Fix:** one statement per line.

## 3. Mystery import → `from pydoc import doc, text`

**Why:** VS Code auto-imported it when I typed `doc` / `text`. It imports Python's documentation tool and can hide real `NameError`s.

**Fix:** delete the line.

## 4. Broken regex → `re.error: nothing to repeat at position 1`

**Symptom:** `r'^?{1,6}\s+.+$'`

**Why:** `?` and `{1,6}` repeat "the thing before me", but after `^` there's nothing to repeat.

**Fix:** `r'^(\*\*Q?\d+\.|#{1,6}\s)'` for bold question lines or headings.

## 5. Typo in a comparison value → branch never runs

**Symptom:** `elif source_type == "books"`

**Why:** the frontmatter says `book` (singular). Strings must match exactly.

**Fix:** `elif source_type in ("book", "ocr"):`

## 6. Literal letter in a regex → page markers never match

**Symptom:** `r'^<!-- page N -->{1,6}\s+.+$'`

**Why:** `N` means the letter N, not "a number". The extra `{1,6}\s+.+` also asked for text after the marker, but it sits alone on its line.

**Fix:** `r'^<!-- page \d+ -->$'`

## 7. `return` inside the loop → 68 chunks, largest 11 words

**Symptom:**
```
68 documents loaded
68 chunks
Largest chunk: 11 words
```

**Why:** the "add final chunk" block and `return chunks` were indented one level too far, inside `for line in lines:`. `return` ends the function immediately, so it returned after the **first line** of each document (its title).

**Fix:** move those lines 4 spaces left so they run once, after the loop (select them in VS Code → Shift+Tab).

**Explain it like I'm 10:** I told the helper "read the notebook, then hand it back", but put "hand it back" inside "read each line", so they handed it back after line one.

**Lesson:** in Python, indentation *is* the structure.

## 8. One section of 46,693 words

**Symptom:** the whole Goldman Sachs file came out as one section.

**Why:** its `source_type` is `interview-questions`, but it came from a PDF, so it has page markers instead of `**Q1.**` lines. The interview pattern never matched.

**Fix:** add page markers to the interview pattern: `r'^(\*\*Q?\d+\.|#{1,6}\s|<!-- page \d+ -->$)'`. Plus recursive splitting as a safety net for any section over 300 words.

## 9. Chunk size bigger than the model can read

**Symptom:** `CHUNK_WORDS = 500`

**Why:** MiniLM reads ~190 words, BGE ~380. With 500 + 50 overlap, the end of many chunks would be invisible to search.

**Fix:** `CHUNK_WORDS = 300` → 350-word max.

## 10. Table-of-contents chunks

**Symptom:** a sample chunk was `Custom object validator . . . . . . . 122`.

**Fix:** `is_table_of_contents()` drops chunks with 10+ dot leaders (~465 chunks).

## 11. Heading-only chunks

**Symptom:** a sample chunk was just `# PART 8 — OBJECTS AND PROGRAMMABILITY`.

**Fix:** `merge_small_sections()` joins anything under 40 words to the next section.

## 12. Code comments treated as headings

**Symptom:** chunks that were half a Python example, split at `# Two positional arguments`.

**Fix:** track `in_code` and don't split while inside a ```` ``` ```` block.

## 13. Overlap squashed formatting

**Symptom:** a pandas chunk had its heading, sentence and table header on one line.

**Why:** `" ".join(prev.split()[-50:])` — `.split()` removes newlines.

**Fix:** `last_words()` uses `re.split(r'(\s+)', text)` to keep the original whitespace, and joins with `"\n"`.

## 14. "Isn't this cut off?" — no, it's the preview

**Symptom:** a sample ended with `WHER`.

**Why:** `print(c["text"][:400])` prints only the first 400 characters. The real chunk continued.

**Fix:** nothing to fix; use `print(c["text"])` to see the whole chunk.

## 15. `save_chunks()` called without a path → `TypeError`

**Symptom:** `TypeError: save_chunks() missing 1 required positional argument: 'path'`

**Why:** the function was defined as `save_chunks(chunks, path)` but `__main__` called `save_chunks(all_chunks)`.

**Fix:** give it a default: `def save_chunks(chunks, path=CHUNKS_PATH):`

## 16. Function defined inside itself → no stats printed

**Symptom:** the script ran but printed none of the stats.

**Why:** pasting left two lines:
```python
def analyze_chunks(all_chunks):
   def analyze_chunks(all_chunks):
```
The outer function only *defines* an inner one and returns. Python allows it, so there's no error.

**Fix:** delete the second `def` line.

**Explain it like I'm 10:** a box inside an identical box. You open the outer one, see another closed box, and stop.

## 17. Before and after were identical

**Symptom:** `diff before.txt after.txt` showed no difference.

**Why:** both runs used the **same** (already-changed) `index.py`. There was no saved copy of the old version and no git.

**Fix:** keep the old file (e.g. `index_original.py`) or use git before changing code. Then compare total chunks, max tokens and the size distribution.

## 18. Token splitting lowercased ~20% of chunks

**Symptom:** "heading-only" chunks like `# # 11. normalization ...` and `select e. name, d. department _ name`.

**Why:** `split_oversized_chunks` decoded tokens back to text. The bge tokenizer is uncased, so decoding lowercases, adds spaces and drops newlines. ~1,884 of 9,296 chunks.

**Fix:** slice the original text using `return_offsets_mapping=True`. Details in [06-chunking-improvements.md](06-chunking-improvements.md).

## 19. TOC chunks with solid dots got through

**Symptom:** smallest chunks were `....... 8 maven....... 9 gradle`.

**Why:** `is_table_of_contents` only counted spaced dots `. .`.

**Fix:** also count runs of 5+ dots: `len(re.findall(r"\.{5,}", text)) >= 3`.

## 20. Stale vectors after re-chunking

**Symptom (would have been):** old damaged chunks still showing up in search.

**Why:** Chroma IDs are `source_file:position`. When the chunk count dropped by 45, the last 45 old IDs were never overwritten.

**Fix:** `vector_store.reset_collection()` at the start of `embed.py` (or `rm -rf chroma_db`). Check: "Total stored" must equal `index.py`'s total.

## 21. Variable name typo → `NameError`

**Symptom:** reranker loader crashed.

**Why:** `BGE_MODEL = None` at the top, but the function used `_BGE_MODEL`. Python treats them as different names.

**Fix:** loaded the reranker once at the top instead: `reranker = CrossEncoder(...)`.

## 22. `NameError: name 'CrossEncoder' is not defined`

**Why:** copied the new code but not the import.

**Fix:** `from sentence_transformers import CrossEncoder`

## 23. All 20 candidates sent to the LLM

**Symptom (caught in review):** `k=20` in `similarity_search`, and the reranker never called.

**Why it's bad:** 20 × ~480 tokens ≈ 9,600 tokens > `num_ctx` 8192. Ollama drops the beginning of the prompt — the rules.

**Fix:** `retrieve()` = search 20 → rerank → return top 5.

## 24. `model 'qwen2.5:7b' not found (status code: 404)`

**Why:** the model wasn't downloaded. `ollama list` showed only `qwen2.5:14b`. The error only appears after the first question, because Ollama isn't contacted until then.

**Fix:** `ollama pull qwen2.5:7b`, or use a model that's installed. Ollama needs the **exact** name.

**Lesson:** I had labelled an earlier run "7B" — it was really 14B. Always check `ollama list` and the startup line.

## 25. Chunks and question sent to the LLM twice

**Symptom (caught in review):** after splitting the prompt into system + user messages, `SYSTEM_PROMPT` still ended with `Retrieved context: {context}` and `Question: {question}`.

**Why it's bad:** the user message also had them, so every prompt was ~6,000 tokens instead of ~3,000, close to `num_ctx` 8192 — and the chunks were back inside the rules message.

**Fix:** the system message holds only the role and rules; the chunks and question go only in the user message (`build_user_message()`). `--dry-run` now makes this visible.

**Explain it like I'm 10:** I made a separate rule card and worksheet, but also photocopied the worksheet onto the back of the rule card.

## 26. f-string at the top of the file → `NameError` at startup

**Symptom (would have been):** `NameError: name 'context' is not defined` before the first question.

**Why:** `SYSTEM_PROMPT = f"""... {context} ..."""` was moved out of the function to the top of the file. Python fills in an f-string the moment that line runs, and at startup there is no `context` yet.

**Fix:** `SYSTEM_PROMPT` is a plain string (no `f`) with only the rules. Use an f-string only where the values exist.

## 27. Low-score warning could never fire

**Symptom (caught by reading the output):** after switching `search.py` to the shared reranker, scores were `0.98`, `0.93`… — never below 0.

**Why:** MiniLM returned raw scores (`5.44`, `-2.1`), but sentence-transformers applies a sigmoid to `bge-reranker-v2-m3`, so its scores are 0–1. The warning checked `< 0`.

**Fix:** `MIN_RERANK_SCORE = 0.5` in `rag_common.py` (0.5 after a sigmoid = 0 before it). Tested with an off-topic question: best chunk 0.44 → warning fired.

**Lesson:** when you swap a model, check the *range* of its outputs, not just whether it runs.

## Harmless messages (no fix needed)

- `Token indices sequence length is longer than ... (702 > 512)` — the tokenizer measures chunks *before* splitting them.
- `Redirects are currently not supported in MacOs` — PyTorch notice.
- `You are sending unauthenticated requests to the HF Hub` — no token needed; `HF_HUB_OFFLINE=1` silences it once models are cached.

## Habits that helped

- Print counts after every step (`68 documents`, `8387 chunks`, `Largest chunk`).
- Look at 3 random chunks after every change.
- Change one thing at a time, then re-run.
- Check every `[n]` citation against the actual chunk text, not just whether the source sounds right.
- Compare models on the **same** questions with the **same** retrieval, so only one thing changes.
- Use `--dry-run` to look at the exact prompt whenever the prompt-building code changes.

---

# Part 2 — Embedding, retrieval, generation and evaluation

## 15. A setting defined in two files → the app and the eval disagreed

**Symptom:** `eval.py` passed the debounce question, but `python rag.py` still printed "Even the best chunk scored below **0.5**".

**Why:** `rag.py` imported `MIN_RERANK_SCORE` (0.15) from `rag_common.py`, then **overwrote it** on line 11 with its own `MIN_RERANK_SCORE = 0.5`. Python runs top to bottom, so the later line wins. `eval.py` imported straight from `rag_common`, so it used 0.15.

**Fix:** delete the copy in `rag.py`; keep every shared setting only in `rag_common.py`. Check with:
```bash
grep -n "MIN_RERANK_SCORE =" *.py      # should print exactly one line
```
**Status:** line 11 now says 0.15, but the duplicate line still exists — delete it.

**Explain it like I'm 10:** I changed the passing grade on the answer key, but the report card still had the old grade written on it.

## 16. `return` not indented under `if` (and `ef` instead of `def`)

**Symptom:** the "not covered" check in `ask_rag` had its `return` at the same level as the `if`, plus a `# type: ignore` to silence the editor; the function header had lost its `d`.

**Fix:** `def`, indent the `return` 4 spaces, remove `# type: ignore` (it hides the warning without fixing the code). Also moved the check **after** the `dry_run` return so `--dry-run` still shows the full prompt.

## 17. Trailing `[1] [2] [5]` line in answers

**Symptom:** answers ended with a line of citations, despite prompt rule 9.

**Why:** small local models slip on fiddly rules, especially habits from training.

**Fix:** strip it in code: `re.sub(r'\n\s*(\[\d+\]\s*)+\s*$', '', response.content).strip()`, and make rule 9 more concrete.

## 18. `("")` in the test list → `ValueError: not enough values to unpack (expected 2, got 0)`

**Why:** brackets around one value don't make a tuple — `("")` is just an empty string, and unpacking it into `question, expect` finds 0 values.

**Fix:** delete it. Every test needs `("question", expect),`.

## 19. `NameError: name 'cite' is not defined` in `eval.py`

**Why:** `cite` lives in `rag_common.py`; a file can only use names it defines or imports.

**Fix:** `from rag_common import MIN_RERANK_SCORE, cite`

## 20. A test that expected something not in my notes

**Symptom:** "What is a transformer in AI?" MISSED with score 0.00.

**Why:** the notes only mention the **library** `sentence-transformers`; they never explain transformers. The RAG was right to find nothing.

**Fix:** change the test to `None` (should be refused). **Lesson:** when a test fails, first check the answer is really in the documents.

## 21. Threshold too strict → real answers refused

**Symptom:** two pointers (0.45) and debounce (0.20) found the right notes, but `rag.py` would refuse them at 0.5.

**Fix:** `MIN_RERANK_SCORE 0.5 → 0.15`, chosen from the gap between refusals (≤0.05) and the weakest real hits (0.20). Also made `eval.py` require `score ≥ MIN_RERANK_SCORE` for a pass, so the eval matches what the app does.

## 22. False pass: right file, wrong section

**Symptom:** debounce was `FOUND`, but `rag.py` answered from the "Form events" section ("`oninput` fires on every keystroke"), which doesn't explain how to *stop* it.

**Why:** the eval only checked the **file** name; `JAVASCRIPT-INTERVIEW-QUESTIONS.md` has many chunks, and some other chunk from it was in the top 5.

**Fix:** match against `cite(doc)` (`file › section`) and expect `"debounc"`. The question now honestly shows MISSED.

## 23. Date objects in `json.dump`

**Symptom:** `TypeError: Object of type date is not JSON serializable` when saving `all_chunks.json`.

**Why:** frontmatter turns `date: 2026-10-01` into a Python `date` object.

**Fix:** `json.dump(..., default=str)`.

## More habits that helped

- Keep every shared setting in one file (`rag_common.py`).
- Test the real app (`rag.py`) as well as the eval — they must agree.
- When the score changes, read the note column before deciding whether the system got better or worse.

## 24. `TypeError: vector_search() takes 2 positional arguments but 3 were given`

**Symptom:** testing the `topic` filter.

**Why:** the body of `vector_search` was changed to use `filter=where`, but the **signature** still said `def vector_search(question, k):`. `rag.py` passed a third argument with nowhere to go (and `where` would have been a `NameError` anyway).

**Fix:** `def vector_search(question, k, where=None):` — the default `None` keeps two-argument calls (like `search.py`) working.

**Explain it like I'm 10:** I taught the librarian to read a "which drawer" note but didn't add a slot at the front desk for it.

## 25. Refusal check skipped after filtering weak chunks (open)

**Symptom (not hit yet, found in code review):** after adding the weak-chunk filter to `ask_rag`, an uncovered question filters `hits` down to `[]`. The old check `if use_rerank and hits and hits[0][1] < MIN_RERANK_SCORE:` is then `False` (empty list), so the LLM is called with **no context**.

**Fix:** replace it with `if not hits:`.

**Lesson:** when you change what a list can contain (here: it can now be empty), re-check every condition that reads it.

## 26. Rewritten search ignores the topic filter (open)

**Why:** `hits += vector_search(rewritten, CANDIDATE_K)` — no `where`.

**Fix:** `vector_search(rewritten, CANDIDATE_K, where)`.

## 25 (update). ✅ Fixed — why `if not hits:` replaced the old refusal check

**Before the weak-chunk filter**, `retrieve()` always returned 5 chunks, best first, so refusing meant "is the **best** chunk too weak?":

```python
if use_rerank and hits and hits[0][1] < MIN_RERANK_SCORE:
```

```
"What is a baseline model?"
hits = [0.05, 0.04, 0.02, 0.01, 0.00]
hits[0][1] = 0.05 < 0.15  →  True  →  refuse ✅
```

**After the filter** (`hits = [(doc, score) for doc, score in hits if score >= MIN_RERANK_SCORE]`), the same question gives:

```
before filter:  [0.05, 0.04, 0.02, 0.01, 0.00]
after filter:   []        ← every chunk below 0.15
```

Python evaluates `and` left to right and **stops at the first False**. An empty list counts as `False`, so `use_rerank and hits and ...` is `False`, the refusal is **skipped**, and qwen is called with **no notes at all**.

The `hits and` part was originally a guard — `hits[0]` on an empty list crashes with `IndexError`. After filtering, "empty" became exactly the case that should refuse, so the guard ended up skipping it.

**Fix:**

```python
if not hits:                                     # nothing scored ≥ 0.15 → refuse
    return "I couldn't find enough information in my documents.", hits, user_message
```

The question changed from "is the best chunk weak?" to "**is anything left?**". Re-checking the score is unnecessary: the filter already guarantees every remaining chunk scores ≥ 0.15.

| Case | `hits` after filter | `not hits` | Result |
| --- | --- | --- | --- |
| "What is a baseline model?" | `[]` | `True` | Instant refusal, no LLM call ✅ |
| "What is ACID?" | 5 chunks (0.35–0.98) | `False` | Cited answer ✅ |

**Explain it like I'm 10:** the old rule was "look at the top card; if it's bad, say I don't know." Then I started throwing bad cards away first. With an empty pile there's no top card, the rule never fires, and the helper tries to answer with an empty hand.

## 27. Blank RETRIEVED section, warning gone (✅ fixed)

**Symptom:** after fixing #25, the refusal worked but the output showed an empty `===== RETRIEVED (reranked) =====` with no ⚠️ warning.

**Why:** `show_hits` receives the **filtered** list from `ask_rag` (not the raw scores), and its warning used the same old condition: `if use_rerank and hits and hits[0][1] < MIN_RERANK_SCORE:` — `False` for an empty list. First attempt changed only the **message**; the **condition** above it was still the old one, so it still never printed.

**Fix:**

```python
if not hits:
    print(f"⚠️  No chunk scored {MIN_RERANK_SCORE} or higher — my notes may not cover this question.")
```

Output now:

```
===== RETRIEVED (reranked) =====
⚠️  No chunk scored 0.15 or higher — my notes may not cover this question.

===== ANSWER =====
I couldn't find enough information in my documents.
```

**Explain it like I'm 10:** I rewrote the sign, but it was still hanging on a door that never opens.

**Lesson (#25 + #27):** when you change what a list can contain — here, "it can now be empty" — re-check **every** line that reads that list, in every function it's passed to.

---

# Part 3 — Answer evaluation, guardrails, environment

## 28. Judge code inside a comment → `NameError: name 'judge' is not defined`

**Why:** in `tryjudge.py`, earlier steps were switched off with triple quotes `"""…"""` — including `judge = ChatOllama(...)`. Text inside quotes is ignored, so `judge` never existed for the active code below.

**Fix:** put the imports and `judge = ...` in the active part of the file.

## 29. Closing `"""` in the wrong place → code silently became prompt text

**Symptom:** the real answer's "Grounded:" line never printed, and there was no error.

**Why:** `grounded_prompt = f"""…` ended **after** the `g = json.loads(...)` and `print(...)` lines, so they were part of the string.

**Fix:** close `"""` right after the `Reply in JSON…` line. Tip: in VS Code, string text is coloured differently — code shown in string colour means the quotes are wrong.

## 30. A lenient judge: found the fake claim but still said True

**Symptom:** the judge's reasoning said "ACID invented by Google in 2015 is **not supported**", then returned `pass: true`.

**Why:** small judges weigh "mostly supported" against the rule "every claim".

**Fix:** stricter prompt — "If even ONE claim is not stated in the FACTS, the answer FAILS, no matter how many other claims are supported." Re-tested: fake answer False, real answer True.

## 31. `check_complete` returned the raw list

**Symptom:** `return points` — `evaluate` expected `(score, missing)`.

**Fix:** count `present`, collect missing points, `return found / len(required), missing`. Renamed the prompt text variable to `points_text` so one name doesn't mean two things.

## 32. `KeyError: 'grounded'` in the summary / CSV

**Why:** `results` includes refusal tests, which have no `grounded` key.

**Fix:** use `answered = [r for r in results if not r["refusal_test"]]` for every score; keep `results` only for saving the JSON.

## 33. Old summary lines left inside the loop

**Why:** `n = len(results)` and summary prints were indented under `for test in TESTS:` — they would print after every question.

**Fix:** delete them; one summary after the loop.

## 34. Two checks still crashed on bad JSON

**Why:** `ask_judge` returned `None` on bad JSON, but `check_relevant` and `check_retrieval` still did `ask_judge(prompt)["pass"]`.

**Fix:** `result = ask_judge(prompt)` then `result["pass"] if result else False` in every check.

## 35. Guardrail tests showed ✗ although the guardrails worked

**Why:** `my_eval.py` matched only `"I couldn't find enough information…"`, but the guardrails reply "I can only answer questions about my notes." / "Please ask a question."

**Fix:** a `REFUSALS` set and `answer.strip() in REFUSALS` → 6/6.

## 36. Wrong virtual environment → wrong package + `transformers` missing

**Symptoms:** `pip install` of `frontmatter` downgraded PyYAML to 5.1 (`jupyter-events` conflict); then `No module named 'frontmatter'`; then `No module named 'transformers'`.

**Why:** `which python` showed `…/StructuredExtractionPipeline/.venv/bin/python` — a **different project's** `.venv` was active (both show `(.venv)` in the prompt). On top of that, `frontmatter` ≠ `python-frontmatter`: both install a `frontmatter` folder, so uninstalling one deletes the other's files.

**Fix:**
```bash
deactivate
cd ~/Documents/MyVault/projects/my-first-rag
source .venv/bin/activate
which python          # must end in my-first-rag/.venv/bin/python (Python 3.14)
```
In the other project: `python -m pip install --upgrade "pyyaml>=6"` (and `--force-reinstall --no-deps python-frontmatter` if it uses it).

**Habits:** run `which python` before `pip install`; prefer `python -m pip`; save `python -m pip freeze > requirements.txt` while everything works; check with `python -m pip check`.

## 37. `vector_search` signature vs body (fixed earlier, #24) — and `redact_pii` false positives

`redact_pii`'s phone regex matched 744 dates/numbers in my notes. Turned off for study notes (doc 14 §4).

## 38. Chunk size changed without a note

`index.py` had `CHUNK_WORDS = 200 / TOKEN_LIMIT = 400` while earlier tests used 300/480. Re-tested both (doc 15) and kept 300/480. **Lesson:** every settings change gets an eval run and a note.

## 39. PDF page labels hid a correct chunk from `eval.py`

**Symptom:** bank transfer MISSED with score 0.89.

**Why:** PDF chunks are labelled `p. 185`, not by heading; the expected word "ACID" was in the chunk's first line, not its label.

**Fix:** `sources = [f"{cite(doc)} {doc.page_content[:120]}" for doc, _ in hits]`.

---

# Part 4 — RAGAS, environments, UI

## 40. `No module named 'langchain_community.chat_models.vertexai'` when importing RAGAS

**Why:** `ragas 0.4.3` imports `ChatVertexAI` from a file that `langchain-community 0.4.2` removed (known bug, ragas issue #2745).

**Fix:** `langchain-community>=0.4,<0.4.2` — in a **separate** `.venv-ragas` (see #41).

## 41. Installing RAGAS broke the RAG's environment

**Symptom:** `pip check` → `langchain-huggingface 1.2.3 has requirement huggingface-hub<2.0.0 … but you have huggingface-hub 2.4.0`; the pin from #40 didn't stick.

**Why:** RAGAS brought `datasets 5.1.0`, which upgraded `huggingface-hub` past what the RAG supports.

**Fix:**
```bash
source .venv/bin/activate
python -m pip uninstall -y ragas datasets
python -m pip install "huggingface-hub<2"
python -m pip check        # No broken requirements found.
```
RAGAS now lives in `.venv-ragas`, fed by `ragas_input.json` (doc 16).

**Lesson:** an evaluation tool shouldn't be allowed to change the app's dependencies.

## 42. `No module named 'langchain_ollama'` right after cleanup

**Why:** the prompt had **no `(.venv)`** — after `deactivate`, the system (pyenv) Python was in use.

**Fix:** `source .venv/bin/activate`, check `which python`. A `pip install` run without a venv went into `~/.pyenv/versions/3.14.7` (harmless here: "already satisfied").

## 43. RAGAS scores dragged down by a refusal question

**Why:** RAGAS scores a correct refusal ("I couldn't find enough information…") as irrelevant, with no real context. Relevancy 0.56 → 0.91 after removing it.

**Fix:** keep refusal tests in `my_eval.py` only.

## 44. RAGAS faithfulness underscored a grounded answer

**Symptom:** LEFT JOIN faithfulness 0.25.

**Why:** the 8B judge failed RAGAS's claim-by-claim check — every claim (including the example SQL) is in the chunks, verified by hand.

**Fix:** treat RAGAS faithfulness with a small judge as unreliable; rely on `my_eval.py` grounded + hand checks, or use a stronger judge.

## 45. Citation format `[1, 5]`

**Symptom:** an answer cited `[1, 5]`; `check_citations` (`\[(\d+)\]`) only recognises `[1][5]`.

**Status:** open — add a prompt rule ("cite as [1][5]") or extend the regex.

## 46. Topic dropdown in `app.py` did nothing

**Why:** the sidebar was at the bottom (Streamlit runs top to bottom) and `ask_rag` had no `topic` parameter.

**Fix:** sidebar moved up; `ask_rag(..., topic=None)` passes it to `retrieve` (doc 17).
