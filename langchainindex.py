from pathlib import Path 
import frontmatter
import re
from langchain_text_splitters import (
    MarkdownHeaderTextSplitter,
    RecursiveCharacterTextSplitter,
)

CHUNK_WORDS = 300
OVERLAP_WORDS = 50

SEPARATORS = ["\n\n", "\n", ". ", " ", ""]


def get_header_pattern(source_type):
    if source_type == "interview-questions":
        return r'^(\*\*Q?\d+\.|#{1,6}\s|<!-- page \d+ -->$)'
    elif source_type in ("book", "ocr"):
        return r'^<!-- page \d+ -->$'
    else:
        return r'^#{1,6}\s+.+$'


def split_by_custom_headers(text, source_type):
    """Split text into sections using custom header patterns."""
    header_pattern = get_header_pattern(source_type)
    pattern = re.compile(header_pattern)

    sections = []
    current = []

    for line in text.split("\n"):
        if pattern.match(line) and current:
            section = "\n".join(current).strip()
            if section:
                sections.append(section)
            current = []

        current.append(line)

    if current:
        section = "\n".join(current).strip()
        if section:
            sections.append(section)

    return sections


def chunk_document(text, source_type):
    """Split by headers, then recursively chunk oversized sections."""

    # Step 1: Split into sections
    if source_type in ("interview-questions", "book", "ocr"):
        sections = split_by_custom_headers(text, source_type)
    else:
        markdown_splitter = MarkdownHeaderTextSplitter(
            headers_to_split_on=[
                ("#", "Header 1"),
                ("##", "Header 2"),
                ("###", "Header 3"),
                ("####", "Header 4"),
                ("#####", "Header 5"),
                ("######", "Header 6"),
            ],
            strip_headers=False,
        )
        sections = markdown_splitter.split_text(text)

    # Step 2: Recursive chunking with overlap
    recursive_splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_WORDS,
        chunk_overlap=OVERLAP_WORDS,
        length_function=lambda text: len(text.split()),
        separators=SEPARATORS,
    )

    chunks = []

    for section in sections:
        # Markdown splitter returns Document objects;
        # custom splitter returns strings.
        section_text = (
            section.page_content
            if hasattr(section, "page_content")
            else section
        )

        split_chunks = recursive_splitter.split_text(section_text)
        chunks.extend(split_chunks)

    return chunks


# Example
if __name__ == "__main__":
    text = """
**Q1. What is Python?**
Python is a programming language.

**Q2. What is React?**
React is a JavaScript library.

**Q3. Explain machine learning.**
Machine learning allows computers to learn from data.
"""

    chunks = chunk_document(text, "interview-questions")

    for i, chunk in enumerate(chunks, start=1):
        print(f"\n--- Chunk {i} ---")
        print(chunk)
        print("Words:", len(chunk.split()))
