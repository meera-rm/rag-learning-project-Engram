import streamlit as st

st.set_page_config(page_title="Study Notes Assistant", page_icon="📚")


# ---------- load the RAG once ----------
@st.cache_resource(show_spinner="Loading models…")
def load_rag():
    from rag_common import get_embeddings, get_reranker
    get_embeddings()                # embedding model
    get_reranker()                  # reranker
    from rag import ask_rag
    from rag_common import cite
    return ask_rag, cite

ask_rag, cite = load_rag()


# ---------- sidebar (must come before it's used below) ----------
TOPICS = ["all", "databases", "java-spring", "javascript-web", "python-data", "dsa",
          "system-design", "interview-prep", "ai", "projects", "daily-concepts"]

with st.sidebar:
    topic = st.selectbox("Topic", TOPICS)
    if st.button("Clear chat"):
        st.session_state.messages = []
        st.rerun()


# ---------- page ----------
st.title("📚 Ask my study notes")
st.caption("Answers come only from my notes, with sources. "
           "If my notes don't cover it, it says so.")

if "messages" not in st.session_state:
    st.session_state.messages = []          # chat history

# show earlier messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
        if msg.get("sources"):
            with st.expander("Sources"):
                for line in msg["sources"]:
                    st.write(line)

# new question
question = st.chat_input("Ask about SQL, Java, React, system design…")
if question:
    st.session_state.messages.append({"role": "user", "content": question})
    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):
        with st.spinner("Searching my notes…"):
            answer, hits, _ = ask_rag(question, topic=None if topic == "all" else topic)
        st.markdown(answer)

        sources = [f"[{i}] {cite(doc)} — score {score:.2f}"
                   for i, (doc, score) in enumerate(hits, 1)]
        if sources:
            with st.expander("Sources"):
                for line in sources:
                    st.write(line)

    st.session_state.messages.append(
        {"role": "assistant", "content": answer, "sources": sources})
