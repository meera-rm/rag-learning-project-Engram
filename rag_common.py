"""Settings and models shared by index.py, embed.py, search.py and rag.py.

Anything that MUST be the same in every script lives here, so changing it
once changes it everywhere. Models are loaded lazily: the first time a
get_...() function is called, not when this file is imported.
"""
from pathlib import Path

# ========== Paths ==========
BASE_DIR = Path(__file__).resolve().parent
DOCS_DIR = BASE_DIR / "rag-docs"
CHUNKS_PATH = BASE_DIR / "all_chunks.json"
CHROMA_DIR = BASE_DIR / "chroma_db"
COLLECTION_NAME = "rag_documents"

# ========== Models ==========
#EMBEDDING_MODEL = "BAAI/bge-small-en-v1.5"    # used for chunk sizes (index.py), vectors (embed.py) and questions
EMBEDDING_MODEL = "BAAI/bge-small-en-v1.5"     # change this, e.g. to "BAAI/bge-base-en-v1.5"
RERANKER_MODEL = "BAAI/bge-reranker-v2-m3"    # cross-encoder for reranking

# ========== Retrieval ==========
CANDIDATE_K = 40   # how many chunks vector search fetches before reranking
TOP_K = 5          # how many chunks reach the LLM
MIN_RERANK_SCORE = 0.15  #oriignal was 0.5 # bge-reranker-v2-m3 scores are 0–1; below this, the chunk probably doesn't answer the question

_embeddings = None
_vector_store = None
_reranker = None


def get_device():
    """Fastest available device: NVIDIA GPU, Apple Silicon GPU, or CPU."""
    import torch
    if torch.cuda.is_available():
        return "cuda"
    if torch.backends.mps.is_available():
        return "mps"
    return "cpu"


def get_embeddings():
    """The embedding model, created once."""
    global _embeddings
    if _embeddings is None:
        from langchain_huggingface import HuggingFaceEmbeddings
        _embeddings = HuggingFaceEmbeddings(
            model_name=EMBEDDING_MODEL,
            encode_kwargs={"normalize_embeddings": True},
        )
    return _embeddings


def get_vector_store():
    """The Chroma collection, connected once."""
    global _vector_store
    if _vector_store is None:
        from langchain_chroma import Chroma
        _vector_store = Chroma(
            collection_name=COLLECTION_NAME,
            embedding_function=get_embeddings(),
            persist_directory=str(CHROMA_DIR),
        )
    return _vector_store


def get_reranker():
    """The cross-encoder, loaded only when reranking is actually used (~2.3 GB)."""
    global _reranker
    if _reranker is None:
        from sentence_transformers import CrossEncoder
        _reranker = CrossEncoder(RERANKER_MODEL, device=get_device(), max_length=512)
    return _reranker


def vector_search(question, k, where=None):
    """Return [(doc, cosine_similarity), ...] best first."""
    hits = get_vector_store().similarity_search_with_score(question, k=k,filter=where)
    # Chroma returns squared L2 distance; for length-1 vectors, cosine = 1 - distance / 2
    return [(doc, 1 - dist / 2) for doc, dist in hits]


def rerank(question, hits, top_k):
    """Score each (question, chunk) pair with the cross-encoder; keep the best top_k.

    hits: [(doc, similarity), ...] from vector_search
    returns: [(doc, similarity, rerank_score), ...] best first
    """
    scores = get_reranker().predict([(question, doc.page_content) for doc, _ in hits])
    ranked = sorted(zip(hits, scores), key=lambda p: p[1], reverse=True)
    return [(doc, sim, float(score)) for (doc, sim), score in ranked[:top_k]]


def cite(doc):
    """'source_file › section' — used in prompts, search output and citations."""
    source = doc.metadata.get("source_file", "unknown")
    section = doc.metadata.get("section")
    return f"{source} › {section}" if section else source


def is_near_duplicate(a, b, threshold=0.6):
    """True if two texts share more than 60% of their words."""
    wa, wb = set(a.split()), set(b.split())
    return len(wa & wb) / max(1, len(wa | wb)) > threshold


def dedupe(hits):
    """Keep the first of any near-duplicate chunks. hits: [(doc, score), ...] best first."""
    kept = []
    for doc, score in hits:
        if any(is_near_duplicate(doc.page_content, d.page_content) for d, _ in kept):
            continue
        kept.append((doc, score))
    return kept
