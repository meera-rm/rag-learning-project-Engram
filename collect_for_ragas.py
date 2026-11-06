import json
from rag import ask_rag

TESTS = [
  
    {"question": "How does LEFT JOIN work?",
     "reference": "LEFT JOIN returns all rows from the left table and matching rows from the right; "
                  "where there is no match, the right table's columns are NULL."},
    {"question": "What is the difference between WHERE and HAVING?",
     "reference": "WHERE filters rows before grouping; HAVING filters groups after GROUP BY."},
    {"question": "What does the volatile keyword do in Java?",
     "reference": "volatile marks a variable that can be changed by different threads, and makes "
                  "changes to it immediately visible to other threads."},
   
]

rows = []
for t in TESTS:
    answer, hits, _ = ask_rag(t["question"])
    rows.append({"question": t["question"], "answer": answer,
                 "contexts": [doc.page_content for doc, _ in hits] or ["(no context retrieved)"],
                 "ground_truth": t["reference"]})
    print("✓", t["question"])

with open("ragas_input.json", "w") as f:
    json.dump(rows, f, indent=2, ensure_ascii=False)
print("Saved ragas_input.json")