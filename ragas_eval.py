import json
from datasets import Dataset
from langchain_ollama import ChatOllama
from langchain_huggingface import HuggingFaceEmbeddings
from ragas import evaluate
from ragas.llms import LangchainLLMWrapper
from ragas.embeddings import LangchainEmbeddingsWrapper
from ragas.metrics import faithfulness, answer_relevancy, context_precision, context_recall

rows = json.load(open("ragas_input.json"))
data = {k: [r[k] for r in rows] for k in ("question", "answer", "contexts", "ground_truth")}

judge = LangchainLLMWrapper(ChatOllama(model="llama3.1:8b", temperature=0))
embeddings = LangchainEmbeddingsWrapper(HuggingFaceEmbeddings(
    model_name="BAAI/bge-small-en-v1.5", encode_kwargs={"normalize_embeddings": True}))

result = evaluate(Dataset.from_dict(data),
                  metrics=[faithfulness, answer_relevancy, context_precision, context_recall],
                  llm=judge, embeddings=embeddings)
print(result)
result.to_pandas().to_json("ragas_results.json", orient="records", indent=2)