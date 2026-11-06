import json
import math
import re

from typing import List
from statistics import mean, median
from collections import Counter

import frontmatter
from transformers import AutoTokenizer

from rag_common import CHUNKS_PATH, DOCS_DIR, EMBEDDING_MODEL




# ========== Settings ==========
# DOCS_DIR and CHUNKS_PATH come from rag_common.py


#MAX_WORDS = 400        # sections longer than this get split
CHUNK_WORDS = 300      # target size for each piece
OVERLAP_WORDS = 50     # words repeated between neighbouring pieces
SEPARATORS = ["\n\n", "\n", ". ", " "]   # paragraph, line, sentence, word
MIN_WORDS = 40 

TOKEN_LIMIT = 480 # Leave room below the model's 512-token limit

# Initialize tokenizer once
# Same model as the embeddings, so token counts match what the embedder sees
tokenizer = AutoTokenizer.from_pretrained(EMBEDDING_MODEL)

#files = sorted(p for p in DOCS_DIR.rglob("*.md") if p.name != "README.md")
#print(DOCS_DIR, DOCS_DIR.exists(), len(files))


#for path in files:
 #   topic = path.parent.name                      # e.g. "databases"
 #   rel = path.relative_to(DOCS_DIR)              # e.g. databases/sql-complete-notes.md
  #  text = path.read_text(encoding="utf-8")
   # print(topic, rel, len(text.split()), "words")


# ========== Step 1: load every document ==========
def load_docs():
    docs = []
    for path in sorted(DOCS_DIR.rglob("*.md")):
        if path.name == "README.md":
            continue
        post = frontmatter.loads(path.read_text(encoding="utf-8"))
        docs.append({"text": post.content, "metadata": post.metadata})

    return docs


# ========== Step 2a: split each document on its structure ==========

# ========== Step 2b:get_header_pattern ==========
def get_header_pattern(source_type):
    if source_type == "interview-questions":
        # bold question lines (**Q1. / **1.) or headings (JS/React files)
        return r'^(\*\*Q?\d+\.|#{1,6}\s|<!-- page \d+ -->$)'
    elif source_type in ("book", "ocr"):
        return r'^<!-- page \d+ -->$'
    else:
        return r'^#{1,6}\s+.+$'   # markdown headings (my-notes)


# ========== Step 2c:markdown_document_chunking ==========


def markdown_document_chunking( text: str, header_pattern: str) -> List[str]:
    # Split by markdown headers (# ## ### etc.)

    #re.compile() prepares that regex for repeated matching.
    #re.MULTILINE allows ^ and $ to match at individual line boundaries.
    #compiled_pattern.findall(text) extracts matching headers from your document.
        
    lines = text.split('\n')
    pattern = re.compile(header_pattern)
    chunks = []
    current_chunk = []
    in_code = False

    for line in lines:
        if line.strip().startswith("```"):
            in_code = not in_code 
        # Check if this line is a header
        if pattern.match(line) and not in_code:
            # If we have a current chunk, save it before starting a new one
            if current_chunk:
                chunk_text = '\n'.join(current_chunk).strip()
                if chunk_text:
                    chunks.append(chunk_text)
                current_chunk = []
        current_chunk.append(line)

    # Add final chunk
    if current_chunk:
        chunk_text = '\n'.join(current_chunk).strip()
        if chunk_text:
            chunks.append(chunk_text)

    return chunks

def section_label(section, header_pattern):
    """First header line of a section, cleaned up for citations."""
    pattern = re.compile(header_pattern)
    for line in section.split("\n"):
        if pattern.match(line):
            page = re.match(r"<!-- page (\d+) -->", line)
            if page:
                return f"p. {page.group(1)}"
            return line.strip("#* ").strip()
    return ""   # text before the first heading (intro paragraph)


# ========== Step 3: merge small sections ==========

def merge_small_sections(sections, min_words=MIN_WORDS):
    merged = []
    carry = ""
    for section in sections:
        carry = carry + "\n\n" + section if carry else section
        if word_count(carry) >= min_words:
            merged.append(carry)
            carry = ""
    if carry:                          # leftover small piece at the very end
        if merged:
            merged[-1] += "\n\n" + carry
        else:
            merged.append(carry)
    return merged

# ========== Step 4: cut long sections + overlap ==========    


# word_count

def word_count(text):
    return len(text.split())

#recursive_split 
def recursive_split(text, separators=SEPARATORS):
    if not text.strip():
        return []

    if word_count(text) <= CHUNK_WORDS:
        return [text]

    if not separators:
        words = text.split()
        return [
            " ".join(words[i:i + CHUNK_WORDS])
            for i in range(0, len(words), CHUNK_WORDS)
        ]

    sep, rest = separators[0], separators[1:]

    parts = text.split(sep)
    pieces = []
    current = ""

    for part in parts:
        candidate = current + sep + part if current else part

        if word_count(candidate) <= CHUNK_WORDS:
            current = candidate
        else:
            if current:
                pieces.append(current)

            if word_count(part) > CHUNK_WORDS:
                pieces.extend(recursive_split(part, rest))
                current = ""
            else:
                current = part

    if current:
        pieces.append(current)

    return pieces



#last_words 
def last_words(text, n):
    """Return the last n words of text, keeping its original spaces and newlines."""
    parts = re.split(r'(\s+)', text)    # the ( ) keeps the whitespace as separate parts
    seen = 0
    for i in range(len(parts) - 1, -1, -1):
        if parts[i].strip():            # a word, not whitespace
            seen += 1
            if seen == n:
                return "".join(parts[i:]).strip()
    return text.strip()

#add_overlap 
def add_overlap(pieces):
    if not pieces:
        return []
    out = [pieces[0]]
    for prev, piece in zip(pieces, pieces[1:]):
        tail = last_words(prev, OVERLAP_WORDS)
        out.append(tail + "\n" + piece)
    return out

#chunk_section
def chunk_section(text):
    return add_overlap(recursive_split(text))


# ========== Step 5: clean up ==========       
  
# is_table_of_contents              
def is_table_of_contents(text):
    # TOC lines use dot leaders: "Summary . . . . 122" or "Summary........122"
    return text.count(". .") >= 10 or len(re.findall(r"\.{5,}", text)) >= 3

#merge_heading_only_chunks 
def merge_heading_only_chunks(chunks):
    merged = []
    pending_heading = None

    for chunk in chunks:
        text = chunk["text"].strip()

        if re.fullmatch(r"#{1,6}\s+.+", text):
            pending_heading = (
                pending_heading + "\n" + text
                if pending_heading
                else text
            )
            continue

        if pending_heading:
            text = pending_heading + "\n\n" + text
            pending_heading = None

        merged.append({
            "text": text,
            "metadata": chunk["metadata"].copy()
        })

    if pending_heading:
        if merged:
            merged[-1]["text"] += "\n\n" + pending_heading
        else:
            # Entire document contains only headings
            merged.append({
                "text": pending_heading,
                "metadata": chunks[-1]["metadata"].copy()
            })

    return merged


# ========== Step 6: enforce token limit ==========     
# split_oversized_chunks       
def split_oversized_chunks(chunks):
    result = []

    for chunk in chunks:
        text = chunk["text"]
        metadata = chunk["metadata"]

        enc = tokenizer(text, add_special_tokens=False, return_offsets_mapping=True)
        offsets = enc["offset_mapping"]          # (start_char, end_char) for each token

        if len(offsets) <= TOKEN_LIMIT:
            result.append(chunk)
            continue

        num_pieces = math.ceil(len(offsets) / TOKEN_LIMIT)
        base_size, remainder = divmod(len(offsets), num_pieces)

        start = 0
        for i in range(num_pieces):
            piece_size = base_size + (1 if i < remainder else 0)
            piece_offsets = offsets[start:start + piece_size]
            start += piece_size

            char_start = piece_offsets[0][0]
            char_end = piece_offsets[-1][1]
            piece_text = text[char_start:char_end].strip()   # slice the ORIGINAL text

            if piece_text:
                result.append({"text": piece_text, "metadata": metadata.copy()})

    return result



# ========== Run ==========
#build_chunks
def build_chunks():

    docs = load_docs()
    all_chunks = []

    for doc in docs:
        source_type = doc["metadata"]["source_type"]
        header_pattern = get_header_pattern(source_type)

        sections = markdown_document_chunking(
            doc["text"], header_pattern
        )

        
        sections = merge_small_sections(sections)

        doc_chunks = []

        for section in sections:
            label = section_label(section, header_pattern)
            chunks = chunk_section(section)

            for chunk in chunks:
                if is_table_of_contents(chunk):
                    continue

                metadata = doc["metadata"].copy()
                metadata["section"] = label
                doc_chunks.append({
                    "text": chunk,
                    "metadata": metadata
                })

        doc_chunks = merge_heading_only_chunks(doc_chunks)
        all_chunks.extend(doc_chunks)

    all_chunks = split_oversized_chunks(all_chunks)


    return all_chunks


#save chunks
def save_chunks(chunks, path=CHUNKS_PATH):

    with open(path, "w", encoding="utf-8") as f:
        #python-frontmatter parses YAML, so a line like date: 2026-10-01 becomes a Python date object,
        #Object of type date is not JSON serializable
        json.dump(chunks, f, ensure_ascii=False, indent=2, default=str)
    print(f"Saved {len(chunks)} chunks -> {path}")   



# ========== Stats ==========                                  
# analyze_chunks
def analyze_chunks(all_chunks):
    if not all_chunks:
        print("No chunks to analyze.")
        return

    sizes = [word_count(c["text"]) for c in all_chunks]
    tokens = [len(tokenizer.encode(c["text"], add_special_tokens=True)) for c in all_chunks]

    print("\n===== SUMMARY =====")
    print("Total chunks:", len(all_chunks))
    print(f"Words  -> min {min(sizes)}, max {max(sizes)}, "
          f"mean {mean(sizes):.1f}, median {median(sizes)}")
    print(f"Tokens -> max {max(tokens)}, over 512: {sum(t > 512 for t in tokens)}")

    print("\n===== SIZE DISTRIBUTION =====")
    ranges = [(0, 40), (40, 100), (100, 200), (200, 300), (300, 350), (350, float("inf"))]
    for low, high in ranges:
        count = sum(low <= s < high for s in sizes)
        print(f"{low:>3} - {str(high):>3} words: {count:>5} chunks ({count / len(sizes) * 100:.1f}%)")

    heading_only = [c for c in all_chunks if re.fullmatch(r"#{1,6}\s+.+", c["text"].strip())]
    print(f"\nHeading-only chunks: {len(heading_only)}")
    for c in heading_only[:20]:
        print("  ", c["metadata"].get("source_file"), "->", repr(c["text"]))

    print("\n===== TOP 10 DOCUMENTS BY CHUNK COUNT =====")
    counts = Counter(c["metadata"].get("source_file", "unknown") for c in all_chunks)
    for filename, count in counts.most_common(10):
        print(f"{count:>5} chunks | {filename}")

    print("\n===== SMALLEST 5 CHUNKS =====")
    for c in sorted(all_chunks, key=lambda c: word_count(c["text"]))[:5]:
        print(f"\n{c['metadata'].get('source_file')} ({word_count(c['text'])} words)")
        print("  ", repr(c["text"][:200]))




if __name__ == "__main__":

    all_chunks = build_chunks()
    save_chunks(all_chunks)
    analyze_chunks(all_chunks)