
#Ask the judge one question
"""from langchain_ollama import ChatOllama

judge = ChatOllama(model="llama3.2:3b", temperature=0)

question = "What is ACID?"
answer = "ACID stands for Atomicity, Consistency, Isolation and Durability."

reply = judge.invoke(f"Question: {question}\nAnswer: {answer}\n\nDoes the answer address the question? Say yes or no, and why.")
print(reply.content)"""


#Ask for JSON to read
"""import json
from langchain_ollama import ChatOllama

judge = ChatOllama(model="llama3.2:3b", temperature=0, format="json")

question = "What is ACID?"
answer = "ACID stands for Atomicity, Consistency, Isolation and Durability."

prompt = fQuestion: {question}
Answer: {answer}

Does the answer address the question?
Reply in JSON: {{"reasoning": "...", "pass": true or false}}

result = json.loads(judge.invoke(prompt).content)
print(result["pass"], "-", result["reasoning"])
"""

#ask from rag for answers

"""from rag import ask_rag
import json
from langchain_ollama import ChatOllama
judge = ChatOllama(model="llama3.2:3b", temperature=0,format="json")

question = "What is ACID?"
answer = "ACID stands for Atomicity, Consistency, Isolation and Durability."

answer, hits, _ = ask_rag(question)
print("RAG said:", answer)


facts = "\n\n".join(doc.page_content for doc, _ in hits)

grounded_prompt = fFACTS:
{facts}

ANSWER:
{answer}

Is every claim in the answer supported by the FACTS?
Reply in JSON: {{"reasoning": "...", "pass": true or false}}

g = json.loads(judge.invoke(grounded_prompt).content)
print("Grounded:", g["pass"], "-", g["reasoning"])"""

# --- test the judge: an answer with an invented claim ---

def main:
        from rag import ask_rag
        import json
        from langchain_ollama import ChatOllama
        judge = ChatOllama(model="llama3.1:8b", temperature=0,format="json")


        question = "What is ACID?"
        answer = "ACID stands for Atomicity, Consistency, Isolation and Durability."

        answer, hits, _ = ask_rag(question)
        print("RAG said:", answer)

        print("   -----------------GROUNDEDNESS CHECK--------------------- ")
        facts = "\n\n".join(doc.page_content for doc, _ in hits)

        print("   -----------------CORRECT ANSWER--------------------- ")

        grounded_prompt = f"""FACTS:
        {facts}

        ANSWER:
        {answer}

        Is every claim in the answer supported by the FACTS?
        Reply in JSON: {{"reasoning": "...", "pass": true or false}}"""

        g = json.loads(judge.invoke(grounded_prompt).content)
        print("Grounded:", g["pass"], "-", g["reasoning"])


        print("   -----------------FAKE ANSWER--------------------- ")


        fake_answer = answer + "\n- ACID was invented by Google in 2015 [1]."

        fake_prompt = f"""FACTS:
        {facts}

        ANSWER:
        {fake_answer}

        Go through the answer claim by claim. For each claim, check whether the FACTS state it.
        If even ONE claim is not stated in the FACTS, the answer FAILS (pass = false),
        no matter how many other claims are supported.
        Reply in JSON: {{"reasoning": "...", "pass": true or false}}"""

        f = json.loads(judge.invoke(fake_prompt).content)
        print("Fake answer grounded:", f["pass"], "-", f["reasoning"])


        print("   -------------------RELEVANCE CHECK------------------- ")

        relevance_prompt = f"""QUESTION: {question}

        ANSWER:
        {answer}

        Does the answer directly address the question and help the person who asked it?
        Reply in JSON: {{"reasoning": "...", "pass": true or false}}"""

        r = json.loads(judge.invoke(relevance_prompt).content)
        print("Relevant:", r["pass"], "-", r["reasoning"])

        off_topic = "LEFT JOIN returns all rows from the left table and matching rows from the right."
        b = json.loads(judge.invoke(relevance_prompt.replace(answer, off_topic)).content)
        print("Off-topic relevant:", b["pass"], "-", b["reasoning"])





        print("   -------------------CORRECTNESS AS COMPLETENESS------------------- ")

        required = [
            "Atomicity: a transaction is all-or-nothing",
            "Consistency: moves the database from one valid state to another",
            "Isolation: concurrent transactions don't interfere",
            "Durability: committed changes survive failures",
            "ACID is usually implemented with write-ahead logging",
        ]

        points = "\n".join(f"- {p}" for p in required)

        complete_prompt = f"""QUESTION: {question}

        ANSWER:
        {answer}

        REQUIRED POINTS (a correct answer contains all of them, in any wording):
        {points}

        For each required point, say whether the answer contains it. Same meaning in different words counts.
        Reply in JSON: {{"points": [{{"point": "...", "present": true or false}}]}}"""

        c = json.loads(judge.invoke(complete_prompt).content)
        found = [p for p in c["points"] if p["present"]]
        print(f"Complete: {len(found)}/{len(required)}")
        for p in c["points"]:
            print("  ", "✓" if p["present"] else "✗", p["point"])



        print("   ------------------- RETRIEVAL RELEVANCE ------------------- ")

        useful = 0
        for i, (doc, score) in enumerate(hits, 1):
            chunk_prompt = f"""QUESTION: {question}

        DOCUMENT:
        {doc.page_content}

        Does this document contain information that helps answer the question?
        Reply in JSON: {{"reasoning": "...", "pass": true or false}}"""
            v = json.loads(judge.invoke(chunk_prompt).content)
            useful += v["pass"]
            print(f"  [{i}] {'✓' if v['pass'] else '✗'}  {doc.metadata.get('source_file')}  (rerank {score:.2f})")

        print(f"Retrieval relevance: {useful}/{len(hits)} chunks useful")



