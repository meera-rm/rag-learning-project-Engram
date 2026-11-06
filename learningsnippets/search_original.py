
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

embeddings = HuggingFaceEmbeddings(
    model_name="BAAI/bge-small-en-v1.5",
    encode_kwargs={"normalize_embeddings": True}
)

vector_store = Chroma(
    collection_name="rag_documents",
    embedding_function=embeddings,
    persist_directory="./chroma_db"
)

query = "What is the difference between SQL and NoSQL databases?"

results = vector_store.similarity_search(query, k=5)

for i, doc in enumerate(results, 1):
    print(f"\n===== RESULT {i} =====")
    print("Source:", doc.metadata.get("source_file"))
    print("Text:", doc.page_content[:600])
    
print("Total stored chunks:", vector_store._collection.count())