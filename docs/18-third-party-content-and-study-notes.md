# 18 — Replacing third-party files with my own study notes

## Why
22 files in `rag-docs/` were written by other people (course notes, tutorials, handbooks, cheat sheets).
Before deploying the RAG publicly they should not be served from my app, and their author
attribution should not be stripped. So:

1. The 22 files were **moved unchanged** to `rag-docs-excluded/` (attribution intact, see its README).
2. **22 new study-notes files** were written in my own words covering the same topics,
   saved into `rag-docs/<topic>/` with `source_type: my-notes` and `note_kind: study-notes`.

## Mapping (original topic → new notes file)

| Topic folder | New notes file | Replaces (in rag-docs-excluded/) |
| --- | --- | --- |
| databases | mongodb-notes.md | mongodb.md |
| databases | sql-query-patterns-notes.md | sql-1.md |
| databases | sql-interview-queries-notes.md | sqlinterviews.md |
| interview-prep | ai-assisted-coding-interview-notes.md | AI-assisted interview playbook |
| interview-prep | big-bank-coding-interview-notes.md | bank interview questions file |
| java-spring | spring-boot-rest-api-guide-notes.md | 2018 Spring Boot API guide |
| java-spring | java-developer-handbook-notes.md | java.md |
| java-spring | spring-boot-project-structure-notes.md | javabasicspringbootstructureproject.md |
| java-spring | java-multithreading-notes.md | javamultithreading.md |
| java-spring | spring-boot-course-notes.md | jhu784 course notes |
| java-spring | spring-boot-features-tutorial-notes.md | Spring Boot tutorial |
| javascript-web | web-security-notes.md | web-development-security-concepts.md |
| python-data | pandas-dataset-preparation-notes.md | array-methods… file (its content was pandas homework, so the notes live in python-data) |
| python-data | python-core-notes.md | completepythonnotes.md |
| python-data | pandas-essentials-notes.md | pandas-cheatsheet.md + pandas-notes.md |
| python-data | pandas-feature-engineering-notes.md | pandasfeaturenegineering.md |
| python-data | pyspark-notes.md | pyspark-cheatsheet.md |
| system-design | system-design-learning-path-notes.md | system-design.md |
| system-design | low-level-design-notes.md | systemdesignpattern.md |
| system-design | system-design-building-blocks-notes.md | systemdesignpatterns.md |
| system-design | system-design-handbook-part1-notes.md + part2 | system design handbook (241 chapters) |

## Checks run
- Frontmatter parses for all 22 files (`title`, `topic`, `source_type`).
- 10-word overlap check against the originals: 0 for most files; the few hits are generic
  phrases (OWASP category names, a standard ReentrantLock/try/finally idiom, "max-heap for the lower half").
- SQL example tables renamed (`staff`, `teams`, `boss_id`, `pay`) so examples don't mirror the originals.

## What to do next
```bash
python index.py      # chunks are stale: 22 files moved out, 22 notes added
python embed.py      # rebuild the Chroma collection
python eval.py       # retrieval: some expected sources pointed at moved files
python my_eval.py    # answers
```
In `eval.py`, update expected-source strings that pointed at moved files
(e.g. `pyspark`, `MongoDB`, `topmate`, `security`, `tutorialspoint`, `jhu784`, `sqlinterviews`,
`javamultithreading`) to the new notes file names, e.g. `pyspark-notes`, `mongodb-notes`,
`system-design-handbook`, `web-security-notes`, `spring-boot-course-notes`, `java-multithreading-notes`.

Before deploying, add `rag-docs-excluded/` to `.gitignore` so those files are never pushed.
