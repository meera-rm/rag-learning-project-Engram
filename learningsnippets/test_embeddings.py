from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(
    model_name="BAAI/bge-small-en-v1.5",
    encode_kwargs={"normalize_embeddings": True}
)

text = "Python is a programming language."

vector = embeddings.embed_query(text)

print("Embedding dimensions:", len(vector))
print("First 5 values:", vector[:5])