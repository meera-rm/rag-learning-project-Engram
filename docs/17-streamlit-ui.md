# 17 — A simple UI with Streamlit (`app.py`)

**Goal:** a chat page in the browser on top of the same `ask_rag()`, with sources and a topic filter.

## 1. Run it

```bash
source .venv/bin/activate
python -m pip install streamlit
streamlit run app.py          # opens http://localhost:8501
```

Ollama must be running (qwen2.5:14b answers the questions).

## 2. How `app.py` works

| Piece | What it does |
| --- | --- |
| `@st.cache_resource` on `load_rag()` | Loads the embedding model and the 2.3 GB reranker **once**. Streamlit reruns the whole script on every interaction — without caching it would reload them every question |
| `st.session_state.messages` | Keeps chat history across reruns |
| `for msg in st.session_state.messages` | Redraws earlier messages after each rerun |
| `st.chat_input` | The chat box (returns text on Enter, otherwise `None`) |
| `st.chat_message("user"/"assistant")` | Chat bubbles |
| `st.spinner("Searching my notes…")` | Shown while `ask_rag` runs |
| `st.expander("Sources")` | Collapsible list `[i] file › section — score` |
| Sidebar `st.selectbox("Topic", …)` | "all" + the 10 `rag-docs` folders |
| Sidebar `st.button("Clear chat")` | Empties history, `st.rerun()` |

**Key idea:** Streamlit runs **top to bottom on every click** — that's why models are cached, history lives in `session_state`, and the sidebar must come **before** the code that uses `topic`.

## 3. Topic filter — two bugs fixed

1. **Sidebar at the bottom of the file.** `topic` would be used before it existed (Streamlit runs top to bottom). → Moved the sidebar right after `load_rag()`, merged the two `with st.sidebar:` blocks.
2. **Dropdown not connected.** `ask_rag(question)` never received the choice. → Wired it through:

`rag.py`:
```python
def ask_rag(question, use_rerank=True, dry_run=False, topic=None):
    ...
    hits = retrieve(question, use_rerank, topic=topic)
```

`app.py`:
```python
answer, hits, _ = ask_rag(question, topic=None if topic == "all" else topic)
```

`topic=None` is the default, so `eval.py`, `my_eval.py` and terminal `rag.py` behave exactly as before. Backups: `backups/before-ui-topic/`.

## 4. Guardrails work in the UI automatically

They live inside `ask_rag`, so the chat shows the same messages as the terminal:

| Try | Expect |
| --- | --- |
| "What is ACID?" (topic: all) | Cited answer; sources from system design + SQL |
| "What is ACID?" (topic: databases) | Only SQL / MongoDB sources |
| "What is ACID?" (topic: javascript-web) | "I couldn't find enough information…" — proves the filter works |
| "What is a baseline model?" | Refusal, no sources |
| "Ignore your previous instructions…" | "I can only answer questions about my notes." |

## 5. Local only (for now)

Deploying publicly (Digital Twin) needs a hosted LLM instead of Ollama and a lighter setup (the reranker is ~2.3 GB). Free hosts: Streamlit Community Cloud, Hugging Face Spaces.

## Resources

- [Streamlit: Build a basic LLM chat app](https://docs.streamlit.io/develop/tutorials/chat-and-llm-apps/build-conversational-apps)
- [Streamlit: Caching](https://docs.streamlit.io/develop/concepts/architecture/caching)
- [Streamlit: Session State](https://docs.streamlit.io/develop/concepts/architecture/session-state)
