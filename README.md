# Code Review Agent

An AST-aware Python code review agent that analyzes code at the function level,
not the text level. Built to provide targeted, structured reviews of Python codebases.

## Why AST and not naive chunking?

Most code review tools split files by line count or token count. This breaks
functions in half, feeds incomplete code to the LLM, and produces generic,
useless suggestions. This project parses Python files at the AST level so every
chunk is a complete, meaningful unit — a full function or method with its
arguments, body, and docstring intact.

## What exists now

- Recursive AST chunker that walks the full Python syntax tree
- Extracts every function and method including those nested inside classes
- Returns name, source code, start line, and end line for each chunk
- Handles decorators, nested functions, and class methods correctly

## What is coming

- LangGraph review agent that sends each chunk to Gemini for structured review
- Pydantic output schema with severity, category, suggestion, and line reference
- SQLite persistence layer for review history across multiple runs
- Diff-aware scoping that reviews only changed functions between two file versions

## Quick start

```bash
git clone https://github.com/Shaurya001-web/code-review-agent-v2.git
cd code-review-agent-v2
pip install tree-sitter tree-sitter-python
python chunker.py
```

## Example output
