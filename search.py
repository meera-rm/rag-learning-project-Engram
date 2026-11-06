"""Search the vector store and show what retrieval returns.

python search.py "How does LEFT JOIN work?"            # vector search only
python search.py "How does LEFT JOIN work?" --rerank   # + cross-encoder rerank (same reranker as rag.py)
"""
import sys

from rag_common import CANDIDATE_K, TOP_K, cite, rerank, vector_search

DEFAULT_QUESTION = "What is the difference between SQL and NoSQL databases?"


def main():
    args = sys.argv[1:]
    use_rerank = "--rerank" in args
    question = " ".join(a for a in args if a != "--rerank") or DEFAULT_QUESTION
    print(f"\nQuestion: {question}\n")

    if not use_rerank:
        for i, (doc, sim) in enumerate(vector_search(question, TOP_K), 1):
            print(f"[{i}] sim {sim:.2f} | {cite(doc)}")
            print(f"     {doc.page_content[:150]!r}\n")
        return

    candidates = vector_search(question, CANDIDATE_K)
    before = {id(doc): i for i, (doc, _) in enumerate(candidates, 1)}
    print(f"{'#':>2} {'was':>4} {'sim':>5} {'rerank':>7}  source")
    for i, (doc, sim, score) in enumerate(rerank(question, candidates, TOP_K), 1):
        print(f"{i:>2} {before[id(doc)]:>4} {sim:>5.2f} {score:>7.2f}  {cite(doc)}")


if __name__ == "__main__":
    main()
