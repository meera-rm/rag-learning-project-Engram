"""
My first RAG: ask questions about the AI Engineering class slides + transcripts.

Setup (once):
    pip install pypdf chromadb anthropic
    export ANTHROPIC_API_KEY=...

Run:
    python rag_starter.py ingest "/path/to/Slides with Transcript"
    python rag_starter.py ask "What is a baseline model and why build one?"
"""
import re
import sys
from pathlib import Path

import chromadb
from pypdf import PdfReader

DB_DIR = "rag_db"            # where the vector database is saved on disk
COLLECTION = "class_notes"
MIN_WORDS = 60               # tiny slides get merged into the next one
MAX_WORDS = 250              # long slides get cut into pieces this size...
OVERLAP = 40                 # ...sharing 40 words so no idea gets cut in half
TOP_K = 5                    # how many chunks to hand to the LLM

SLIDE_SPLIT = re.compile(r"SLIDE (\d+) OF \d+")


def pdf_to_chunks(pdf_path: Path):
    """One chunk per slide's transcript, tagged with class + slide number."""
    class_num = int(re.search(r"Class (\d+)", pdf_path.name).group(1))
    text = "\n".join(page.extract_text() or "" for page in PdfReader(pdf_path).pages)

    # re.split with a capture group gives: [intro, "1", body1, "2", body2, ...]
    parts = SLIDE_SPLIT.split(text)
    chunks, carry, carry_start = [], "", None
    for i in range(1, len(parts) - 1, 2):
        slide = int(parts[i])
        body = parts[i + 1].replace("TRANSCRIPT", "").strip()
        body = re.sub(r"\s+", " ", body)
        if carry_start is None:
            carry_start = slide
        carry = f"{carry} {body}".strip()
        if len(carry.split()) >= MIN_WORDS:
            chunks.append((class_num, carry_start, slide, carry))
            carry, carry_start = "", None
    if carry:
        chunks.append((class_num, carry_start, slide, carry))

    # Some slides (Q&A sections) have thousands of words. Embedding models only
    # "read" the first ~250 words, so cut long ones into overlapping windows.
    final = []
    for c, s1, s2, t in chunks:
        words = t.split()
        for n, start in enumerate(range(0, len(words), MAX_WORDS - OVERLAP)):
            piece = " ".join(words[start:start + MAX_WORDS])
            final.append((c, s1, s2, n, piece))
            if start + MAX_WORDS >= len(words):
                break
    return final


def ingest(folder: str):
    client = chromadb.PersistentClient(path=DB_DIR)
    # Start fresh each time so re-running doesn't duplicate chunks
    if COLLECTION in [c.name for c in client.list_collections()]:
        client.delete_collection(COLLECTION)
    col = client.create_collection(COLLECTION)  # uses Chroma's default local embedding model

    total = 0
    for pdf in sorted(Path(folder).glob("Class *.pdf")):
        chunks = pdf_to_chunks(pdf)
        col.add(
            ids=[f"c{c}_s{s1}-{s2}_p{n}" for c, s1, s2, n, _ in chunks],
            documents=[t for *_, t in chunks],
            metadatas=[{"class": c, "slide_start": s1, "slide_end": s2} for c, s1, s2, _, _ in chunks],
        )
        total += len(chunks)
        print(f"{pdf.name}: {len(chunks)} chunks")
    print(f"Done. {total} chunks stored in ./{DB_DIR}")


def ask(question: str):
    import anthropic

    col = chromadb.PersistentClient(path=DB_DIR).get_collection(COLLECTION)
    hits = col.query(query_texts=[question], n_results=TOP_K)

    context = ""
    for doc, meta in zip(hits["documents"][0], hits["metadatas"][0]):
        context += f"\n[Class {meta['class']}, slides {meta['slide_start']}-{meta['slide_end']}]\n{doc}\n"

    prompt = (
        "Answer the question using ONLY the class transcript excerpts below. "
        "Cite the class and slide numbers you used. If the excerpts don't cover it, say so.\n"
        f"<excerpts>{context}</excerpts>\n\nQuestion: {question}"
    )
    reply = anthropic.Anthropic().messages.create(
        model="claude-sonnet-5-5",
        max_tokens=800,
        messages=[{"role": "user", "content": prompt}],
    )
    print(reply.content[0].text)
    print("\n--- retrieved from ---")
    for meta in hits["metadatas"][0]:
        print(f"Class {meta['class']}, slides {meta['slide_start']}-{meta['slide_end']}")


if __name__ == "__main__":
    if len(sys.argv) < 3 or sys.argv[1] not in ("ingest", "ask"):
        sys.exit(__doc__)
    ingest(sys.argv[2]) if sys.argv[1] == "ingest" else ask(" ".join(sys.argv[2:]))
