"""Step 3–4: embed every chunk in all_chunks.json and store it in Chroma.

python embed.py
"""
import hashlib
import json
import time

from rag_common import CHUNKS_PATH, get_embeddings, get_vector_store

BATCH_SIZE = 500   # chunks per insert; keeps memory steady and under Chroma's limit


def main():
    with open(CHUNKS_PATH, encoding="utf-8") as f:
        all_chunks = json.load(f)
    print(f"Loaded {len(all_chunks)} chunks from {CHUNKS_PATH.name}")

    vector_store = get_vector_store()
    vector_store.reset_collection()   # no stale chunks from earlier runs

    start = time.time()
    for i in range(0, len(all_chunks), BATCH_SIZE):
        batch = all_chunks[i:i + BATCH_SIZE]

        ids = [
            hashlib.sha256(
                f"{c['metadata'].get('source_file', '')}:{i + j}".encode()
            ).hexdigest()
            for j, c in enumerate(batch)
        ]

        vector_store.add_texts(
            texts=[c["text"] for c in batch],
            metadatas=[c["metadata"] for c in batch],
            ids=ids,
        )
        print(f"Stored {min(i + BATCH_SIZE, len(all_chunks))}/{len(all_chunks)} chunks")

    print(f"\nEmbedded {len(all_chunks)} chunks in {time.time() - start:.1f} s")
    sample = get_embeddings().embed_query(all_chunks[0]["text"])
    print(f"Each embedding has {len(sample)} numbers. First 8: {[round(x, 3) for x in sample[:8]]}")
    print("Total stored:", vector_store._collection.count())


if __name__ == "__main__":
    main()
