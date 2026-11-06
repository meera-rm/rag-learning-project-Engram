# 02 — Project setup

**Goal:** a clean project folder with its own Python environment, the libraries, and a safely stored API key.

**Explain it like I'm 10:** before baking, you clear your own counter so your ingredients don't get mixed up with someone else's. A virtual environment is your own counter.

## 1. Create the project and virtual environment

```bash
cd ~/Documents/MyVault/projects/my-first-rag
python3 -m venv .venv          # create the environment in a .venv folder
source .venv/bin/activate      # turn it on — the prompt now starts with (.venv)
```

- `venv` is Python's built-in tool for isolated environments.
- Every `pip install` while `(.venv)` is showing goes **only** into this project.
- Run `source .venv/bin/activate` again in every new terminal window.

## 2. Install the libraries

```bash
pip install python-frontmatter          # reads the YAML header of each file (Step 1)
pip install sentence-transformers       # free local embedding model (Step 3)
pip install chromadb                    # local vector database (Step 4)
pip install anthropic                   # client for calling Claude (Step 6)
```

Note: the package is installed as `python-frontmatter` but imported as `import frontmatter`.

## 3. Keep secrets out of the code

- The Anthropic API key lives in `.env`, never inside `index.py`.
- `.gitignore` lists `.env`, `.venv` and `.idea`, so they're never committed to GitHub.

**Real-world example:** leaked API keys on GitHub get found by bots within minutes and used up. `.gitignore` is the seatbelt.

## 4. Put the documents inside the project

```
my-first-rag/
├── index.py
└── rag-docs/        ← copied here, 68 .md files in 10 topic folders
```

## 5. Run the script

```bash
python index.py
```

Always run it with `(.venv)` showing. If you see `ModuleNotFoundError: No module named 'frontmatter'`, the environment isn't active or the package isn't installed.
