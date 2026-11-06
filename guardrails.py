"""Guardrails: cheap checks on the question (before the RAG) and the answer (after the LLM)."""
import re

# ---------- input checks ----------
MAX_QUESTION_CHARS = 500

def check_question(question):
    """Return an error message if the question shouldn't be processed, else None."""
    if not question.strip():
        return "Please ask a question."
    if len(question) > MAX_QUESTION_CHARS:
        return f"Please keep questions under {MAX_QUESTION_CHARS} characters."
    return None


INJECTION_PATTERNS = [
    r"ignore (all |your |the )?(previous |above )?(instructions|rules)",
    r"disregard (your|the) (instructions|rules|system prompt)",
    r"(reveal|show|print) (your|the) (system )?prompt",
    r"you are now",
    r"act as (?!a study)",
]

def looks_like_injection(question):
    q = question.lower()
    return any(re.search(p, q) for p in INJECTION_PATTERNS)


# ---------- output checks ----------
def check_citations(answer, n_chunks):
    """True if the answer has at least one [n] and every [n] is between 1 and n_chunks."""
    cited = [int(n) for n in re.findall(r"\[(\d+)\]", answer)]
    return bool(cited) and all(1 <= n <= n_chunks for n in cited)


def redact_pii(text):
    """Replace email addresses and phone numbers with placeholders."""
    text = re.sub(r"[\w.+-]+@[\w-]+\.[\w.]+", "[email removed]", text)
    text = re.sub(r"\+?\d[\d\s().-]{8,}\d", "[phone removed]", text)
    return text