"""
https://docs.langchain.com/langsmith/evaluate-rag-tutorial

RAG evaluators compare one artifact to another (response, input, retrieved docs, or reference answer):
Correctness (response vs reference answer)
Goal: Score how similar the RAG answer is to a ground-truth answer.
Mode: Requires a reference answer in the dataset.
Evaluator: LLM-as-judge for answer correctness.
Relevance (response vs input)
Goal: Score how well the response addresses the user question.
Mode: No reference answer; compares the answer to the input.
Evaluator: LLM-as-judge for relevance and helpfulness.
Groundedness (response vs retrieved docs)
Goal: Score how well the response agrees with the retrieved context.
Mode: No reference answer; compares the answer to retrieved documents.
Evaluator: LLM-as-judge for faithfulness and hallucinations.
Retrieval relevance (retrieved docs vs input)
Goal: Score how relevant the retrieved documents are to the query.
Mode: No reference answer; compares the question to retrieved documents.
Evaluator: LLM-as-judge for retrieval relevance.
For more on these evaluator types, see Evaluate RAG applications.
Rag eval overview
​

"""
"""

create a spreadsheet, google docs, etc and define some columns, something like:
"eval date, attemptNo, scenario, metric-1, .., metric-N"

prepare your datasets, depends on scenario (question-answering, research, discovery)

repeat and record results and document observations, otherwise after 2 weeks those metrics will be just a number with no value.

"""


import csv
from datetime import datetime
from pathlib import Path

from rag import retrieve
from rag_common import MIN_RERANK_SCORE, cite

# expect = words that should appear in a top-5 source_file (any one counts). None = should be refused.
TESTS = [
    ("What is the difference between WHERE and HAVING?",   ["SQL-Interview", "SQL-Complete"]),
    ("How does LEFT JOIN work?",                            ["SQL-Complete", "SQL-Interview"]),
    ("What does strict turn on in tsconfig?",               ["TS-COMPLETE", "2026-10-08", "typescript-unions"]),
    ("Explain the difference between @Component and @Bean", ["JAVA-INTERVIEW", "JAVA-COMPLETE"]),
    ("What does @Transactional do in Spring?",              ["JAVA-INTERVIEW", "JAVA-COMPLETE", "jhu784"]),
    ("How does a HashMap work internally in Java?",         ["JAVA", "DSA"]),
    ("What is the useEffect hook in React?",                ["REACT"]),
    ("How does the JavaScript event loop work?",            ["JAVASCRIPT", "NODEJS"]),
    ("When should I use the two pointers technique?",       ["DSA", "logic-building"]),
    ("What is consistent hashing?",                         ["SYSTEM-DESIGN", "systemdesign"]),
    ("Explain the CAP theorem",                             ["SYSTEM-DESIGN", "systemdesign", "JAVA"]),
    ("How do I use groupby in pandas?",                     ["pandas"]),
    # --- exact terms (embeddings can blur these) ---
    ("What is the difference between RANK and DENSE_RANK?", ["SQL-Complete", "SQL-Interview", "SQL (1)", "sqlinterviews"]),
    ("What does COALESCE do in SQL?",                       ["SQL-Complete", "SQL-Interview", "concepts/"]),
    ("When should I use ExecutorService in Java?",          ["javamultithreading", "JAVA-"]),
    ("What does the volatile keyword do in Java?",          ["javamultithreading", "JAVA-"]),
    ("How does Promise.all work?",                          ["JAVASCRIPT", "concepts/"]),
    ("How do I fill missing values with fillna in pandas?", ["pandas"]),

    # --- paraphrased: no keyword from the notes in the question ---
    ("How do I find customers who never placed an order?",  ["SQL-Complete", "SQL-Interview"]),
    ("How do I stop a function from firing on every keystroke?", ["debounc"]),#["JAVASCRIPT-INTERVIEW", "REACT-COMPLETE"]
    ("How can React skip recalculating an expensive value on every render?", ["REACT", "JAVASCRIPT-COMPLETE", "TS-COMPLETE"]),
    ("Why should a bank transfer be all-or-nothing in a database?", ["SQL-Complete", "SQL-Interview", "MongoDB", "JAVA-", "ACID"]),

    # --- answers mostly in books or OCR files ---
    ("What are the stages of a MongoDB aggregation pipeline?", ["MongoDB", "SQL-Interview", "topmate"]),
    ("How do I read a CSV file into a PySpark DataFrame?",  ["pyspark"]),
    ("What is XSS and how do you prevent it?",              ["security", "JAVA-", "jhu784", "GoldmanSachs"]),
    ("What is Spring Boot Actuator used for?",              ["tutorialspoint", "JAVA-", "jhu784"]),
    ("How does database sharding work?",                    ["MongoDB", "systemdesign", "JAVA-"]),

    # --- AI notes ---
    ("What is a transformer in AI?",                        None),
    #("What is a transformer in AI?",                        ["learning-guide", "digital-twin"]
    # --- should be refused (not in rag-docs) ---
    ("How does the Rust borrow checker work?",              None),
    ("What is a baseline model in machine learning?",       None),
    ("How do I bake sourdough bread?",                      None),
   
]


def run():
    hits_ok, refusals_ok, n_covered, n_uncovered = 0, 0, 0, 0
    print(f"{'result':<7} {'best':>5}  question")
    for question, expect in TESTS:
        hits = retrieve(question, use_rerank=True, use_rewrite=False)# use_rewrite=True so evals stay fast, and turn it on only when you’re testing rewrite changes.
        best = hits[0][1] if hits else 0.0
        sources = [f"{cite(doc)} {doc.page_content[:120]}" for doc, _ in hits]

        if expect is None:                       # should be refused
            n_uncovered += 1
            ok = best < MIN_RERANK_SCORE
            refusals_ok += ok
        else:                                    # expected file in the top 5?
            n_covered += 1
            found = any(e.lower() in s.lower() for s in sources for e in expect)
            ok = found and best >= MIN_RERANK_SCORE
            hits_ok += ok
            label = "FOUND" if ok else ("LOW SCORE" if found else "MISSED")

        if expect is None:
            label = "REFUSED" if ok else "ANSWERED?!"
        else:
            label = "FOUND" if ok else ("LOW SCORE" if found else "MISSED")
        print(f"{label:<11} {best:>5.2f}  {question}")
        if not ok:
            print("        got:", sources)

    hit_rate = hits_ok / max(1, n_covered)
    refusal_rate = refusals_ok / max(1, n_uncovered)
    print(f"\nHit rate @5:  {hits_ok}/{n_covered} = {hit_rate:.0%}")
    print(f"Refusals:     {refusals_ok}/{n_uncovered} = {refusal_rate:.0%}")

    # your "spreadsheet" idea: one row per run, so results don't become meaningless numbers
    log = Path(__file__).parent / "eval_log.csv"
    new = not log.exists()
    with log.open("a", newline="") as f:
        w = csv.writer(f)
        if new:
            w.writerow(["eval_date", "scenario", "hit_rate_at_5", "refusal_rate", "notes"])
        w.writerow([datetime.now().strftime("%Y-%m-%d %H:%M"), "retrieval+rerank",
                    f"{hit_rate:.2f}", f"{refusal_rate:.2f}", input("Notes for this run: ")])


if __name__ == "__main__":
    run()