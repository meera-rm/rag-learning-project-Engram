"""Step 7b: answer-quality evaluation with an LLM judge.

Based on Class 10 (evaluation) and the LangSmith evaluator types:
  1. Rules first (no LLM): refusal correct? citations valid?
  2. Groundedness, two steps: extract the answer's claims -> check each claim against the chunks.
     Score = supported claims / all claims.          (catches hallucinations)
  3. Completeness: are the required claims for this question in the answer?
     Score = required claims present / required.     (correctness without exact wording)
  4. Judge agreement: compare the judge with your own hand grades (the "human" field).

python eval_answers.py

Start with ONE judge. Later, add more models from different families to JUDGE_MODELS
(Class 10: an ensemble of independently trained judges, keep their disagreements).
"""
import csv
import json
import re
from datetime import datetime
from pathlib import Path

from langchain_ollama import ChatOllama

from rag import ask_rag
from rag_common import cite

# ========== Settings ==========
JUDGE_MODELS = ["llama3.1:8b"]   # different from the answer model (qwen2.5:14b); add e.g. "gemma2:9b" later
REFUSAL = "I couldn't find enough information in my documents."
DISAGREE_GAP = 0.25              # flag a question when judges' scores differ by more than this

BASE_DIR = Path(__file__).resolve().parent
RESULTS_PATH = BASE_DIR / "eval_answers_results.json"
LOG_PATH = BASE_DIR / "eval_answers_log.csv"

# ========== Test set ==========
# required = claims a correct answer must contain (any wording). None = should be refused.
# human    = your own grade after reading the answer (fill in after the first run):
#            {"grounded": True/False, "complete": True/False}
TESTS = [
    {"question": "What is ACID?",
     "required": ["Atomicity: a transaction is all-or-nothing (all changes applied or none)",
                  "Consistency: a transaction moves the database from one valid state to another",
                  "Isolation: concurrent transactions do not interfere with each other",
                  "Durability: once committed, changes are permanent and survive failures"],
     "human": None},
    {"question": "How does LEFT JOIN work?",
     "required": ["Returns all rows from the left table",
                  "Returns the matching rows from the right table",
                  "Where there is no match, the right table's columns are NULL"],
     "human": None},
    {"question": "What is the difference between WHERE and HAVING?",
     "required": ["WHERE filters rows before grouping",
                  "HAVING filters groups after GROUP BY"],
     "human": None},
    {"question": "Explain the difference between @Component and @Bean",
     "required": ["@Component is a class-level annotation",
                  "@Component classes are picked up by component scanning",
                  "@Bean is a method-level annotation inside a @Configuration class",
                  "@Bean gives manual / fine-grained control over how the bean is created"],
     "human": None},
    {"question": "What is a baseline model in machine learning?", "required": None, "human": None},
    {"question": "How do I bake sourdough bread?", "required": None, "human": None},
]

# ========== Judge prompts ==========
EXTRACT_CLAIMS = """Break the ANSWER below into its individual factual claims.
- One claim per item, each a complete sentence that makes sense on its own.
- Keep qualifiers attached (e.g. "only", "before GROUP BY").
- Say which numbered sentence each claim came from.
- Ignore citation markers like [1] and greetings.

ANSWER (sentences numbered):
{numbered_answer}

Reply in JSON: {{"claims": [{{"claim": "...", "sentence": "S1"}}]}}"""

CHECK_CLAIMS = """You are checking whether claims are supported by EVIDENCE.
The claims were extracted automatically from the ORIGINAL ANSWER and may contain extraction mistakes,
so read each claim in the context of the original answer.

EVIDENCE (the only facts the answer was allowed to use):
{context}

ORIGINAL ANSWER:
{answer}

CLAIMS:
{claims}

For each claim, decide if the evidence supports it. A claim not stated in the evidence is unsupported,
even if it is true in general.
Reply in JSON: {{"verdicts": [{{"claim": "...", "reason": "<short>", "supported": true or false}}]}}"""

CHECK_COMPLETENESS = """QUESTION: {question}

ANSWER:
{answer}

REQUIRED POINTS (a complete answer contains all of them, in any wording):
{required}

For each required point, decide if the answer contains it. Same meaning in different words counts.
Reply in JSON: {{"points": [{{"point": "...", "reason": "<short>", "present": true or false}}]}}"""


# ========== Helpers ==========
def number_sentences(text):
    """Split an answer into sentences/lines and label them S1, S2, ..."""
    parts = [p.strip() for p in re.split(r"(?<=[.!?])\s+|\n+", text) if p.strip()]
    return "\n".join(f"S{i}: {p}" for i, p in enumerate(parts, 1))


def ask_judge(judge, prompt, key):
    """Run a judge prompt and return the list under `key`, or None if the output can't be parsed."""
    raw = judge.invoke(prompt).content
    try:
        items = json.loads(raw).get(key)
        return items if isinstance(items, list) else None
    except json.JSONDecodeError:
        return None


def citation_check(answer, n_chunks):
    """Rule check (no LLM): at least one citation, and every [n] is between 1 and n_chunks."""
    cited = [int(n) for n in re.findall(r"\[(\d+)\]", answer)]
    if not cited:
        return False, "no citations"
    bad = sorted({n for n in cited if not 1 <= n <= n_chunks})
    return (not bad), (f"invalid citations {bad} (only {n_chunks} chunks)" if bad else "ok")


# ========== Judging one answer ==========
def groundedness(judge, answer, docs):
    claims = ask_judge(judge, EXTRACT_CLAIMS.format(numbered_answer=number_sentences(answer)), "claims")
    if not claims:
        return None, [], "claim extraction failed"
    context = "\n\n---\n\n".join(f"[{i}] {d.page_content}" for i, d in enumerate(docs, 1))
    claim_list = "\n".join(f"- {c.get('claim', '')} ({c.get('sentence', '?')})" for c in claims)
    verdicts = ask_judge(judge, CHECK_CLAIMS.format(context=context, answer=answer, claims=claim_list), "verdicts")
    if not verdicts:
        return None, claims, "claim check failed"
    score = sum(bool(v.get("supported")) for v in verdicts) / len(verdicts)
    return score, verdicts, ""


def completeness(judge, question, answer, required):
    req = "\n".join(f"- {r}" for r in required)
    points = ask_judge(judge, CHECK_COMPLETENESS.format(question=question, answer=answer, required=req), "points")
    if not points:
        return None, [], "completeness check failed"
    score = sum(bool(p.get("present")) for p in points) / len(required)
    return score, points, ""


def evaluate_one(test, judges):
    question, required = test["question"], test["required"]
    answer, hits, _ = ask_rag(question)
    docs = [doc for doc, _ in hits]
    refused = answer.strip() == REFUSAL
    should_refuse = required is None

    result = {"question": question, "answer": answer, "sources": [cite(d) for d in docs],
              "human": test.get("human"), "refusal_ok": refused == should_refuse}

    # Refusal cases, or a wrong refusal: nothing else to judge
    if should_refuse or refused:
        result["note"] = ("refused correctly" if result["refusal_ok"]
                          else "answered a question it should refuse" if should_refuse
                          else "refused a question my notes cover")
        return result

    ok, why = citation_check(answer, len(docs))
    result["citations_ok"], result["citations_note"] = ok, why

    result["judges"] = {}
    for name, judge in judges.items():
        g, verdicts, g_err = groundedness(judge, answer, docs)
        c, points, c_err = completeness(judge, question, answer, required)
        result["judges"][name] = {"groundedness": g, "completeness": c,
                                  "unsupported": [v.get("claim") for v in verdicts if not v.get("supported")],
                                  "missing": [p.get("point") for p in points if not p.get("present")],
                                  "errors": [e for e in (g_err, c_err) if e]}

    for metric in ("groundedness", "completeness"):
        scores = [j[metric] for j in result["judges"].values() if j[metric] is not None]
        result[metric] = sum(scores) / len(scores) if scores else None
        result[f"{metric}_disagree"] = len(scores) > 1 and max(scores) - min(scores) > DISAGREE_GAP
    return result


# ========== Run ==========
def fmt(x):
    return "  - " if x is None else f"{x:4.2f}"


def judge_agreement(results):
    """Share of hand-graded answers where the judge's pass/fail matches yours."""
    pairs = []
    for r in results:
        h = r.get("human")
        if not h or r.get("groundedness") is None:
            continue
        if "grounded" in h:
            pairs.append((r["groundedness"] == 1.0) == h["grounded"])
        if "complete" in h:
            pairs.append((r["completeness"] == 1.0) == h["complete"])
    return (sum(pairs) / len(pairs), len(pairs)) if pairs else (None, 0)


def run():
    judges = {m: ChatOllama(model=m, temperature=0, format="json", num_ctx=8192) for m in JUDGE_MODELS}
    results = []

    print(f"{'ground':>6} {'compl':>6} {'cites':>5}  question")
    for test in TESTS:
        r = evaluate_one(test, judges)
        results.append(r)
        if "judges" not in r:                                  # refusal case
            print(f"{'':>6} {'':>6} {'':>5}  {'✓' if r['refusal_ok'] else '✗'} {r['question']}  ({r['note']})")
            continue
        flag = " ⚠ judges disagree" if r["groundedness_disagree"] or r["completeness_disagree"] else ""
        print(f"{fmt(r['groundedness']):>6} {fmt(r['completeness']):>6} "
              f"{'✓' if r['citations_ok'] else '✗':>5}  {r['question']}{flag}")
        for name, j in r["judges"].items():
            for claim in j["unsupported"]:
                print(f"         unsupported ({name}): {claim}")
            for point in j["missing"]:
                print(f"         missing ({name}): {point}")
            for err in j["errors"]:
                print(f"         error ({name}): {err}")
        if not r["citations_ok"]:
            print(f"         citations: {r['citations_note']}")

    judged = [r for r in results if "judges" in r]
    avg = lambda key: (lambda xs: sum(xs) / len(xs) if xs else None)([r[key] for r in judged if r[key] is not None])
    summary = {
        "groundedness": avg("groundedness"),
        "completeness": avg("completeness"),
        "citations_ok": sum(r["citations_ok"] for r in judged) / len(judged) if judged else None,
        "refusals_ok": sum(r["refusal_ok"] for r in results) / len(results),
    }
    agreement, n_pairs = judge_agreement(results)

    print("\n" + "  ".join(f"{k}: {'-' if v is None else f'{v:.0%}'}" for k, v in summary.items()))
    print(f"judge vs. you: {'no hand grades yet' if agreement is None else f'{agreement:.0%} of {n_pairs} checks agree'}")

    RESULTS_PATH.write_text(json.dumps(results, indent=2, ensure_ascii=False, default=str))
    print(f"Details → {RESULTS_PATH.name}")

    new = not LOG_PATH.exists()
    with LOG_PATH.open("a", newline="") as f:
        w = csv.writer(f)
        if new:
            w.writerow(["eval_date", "judges", "n_questions", "groundedness", "completeness",
                        "citations_ok", "refusals_ok", "judge_agreement", "notes"])
        w.writerow([datetime.now().strftime("%Y-%m-%d %H:%M"), "+".join(JUDGE_MODELS), len(results),
                    *("" if v is None else f"{v:.2f}" for v in summary.values()),
                    "" if agreement is None else f"{agreement:.2f}",
                    input("Notes for this run: ")])


if __name__ == "__main__":
    run()
