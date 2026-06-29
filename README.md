# Code Review Agent

An AST-aware Python code review agent that analyzes code at the function level,
not the text level. Built with **LangChain**, **LangGraph**, and **Gemini 2.5 Flash** to provide targeted, structured reviews of Python codebases.

## Why AST and not naive chunking?

Most code review tools split files by line count or token count. This breaks
functions in half, feeds incomplete code to the LLM, and produces generic,
useless suggestions. This project parses Python files at the AST level so every
chunk is a complete, meaningful unit — a full function or method with its
arguments, body, and docstring intact.

## Project Structure

```
code-review-agent-v2/
├── Chunk/
│   ├── chunker.py        # AST-based Python code chunker using tree-sitter
│   └── test_file.py      # Sample Python file for testing
├── my_agent/
│   ├── agent.py           # LangChain agent with Gemini 2.5 Flash + tool calling
│   ├── .env               # API keys (not committed — add your own)
│   └── utl/
│       └── tools/
│           └── tool.py    # Custom tools decorated with @tool
├── requirements.txt
├── pyproject.toml
└── README.md
```

## Features

- **AST Chunker** — Recursively walks the Python syntax tree using `tree-sitter` to extract every function and method, including those nested inside classes. Returns name, source code, start line, and end line for each chunk.
- **LangChain Agent** — Uses `create_agent` with Gemini 2.5 Flash to review the extracted code chunks and provide structured feedback.
- **Tool Calling** — Custom tools (e.g., `add`) decorated with `@tool` and passed to the agent for function calling.
- **Cross-folder Imports** — Imports the AST chunker from `Chunk/` into `my_agent/` using `sys.path` manipulation.

## Quick Start

### 1. Clone the repo

```bash
git clone https://github.com/Shaurya001-web/code-review-agent-v2.git
cd code-review-agent-v2
```

### 2. Install dependencies

```bash
pip install uv
uv sync
```

Or with pip:

```bash
pip install -r requirements.txt
```

### 3. Set up API keys

Create a `.env` file inside `my_agent/`:

```bash
# my_agent/.env
GOOGLE_API_KEY=YOUR_API_KEY
TAVILY_API_KEY=YOUR_TAVILY_API_KEY
```

### 4. Run the agent

```bash
python my_agent/agent.py
```

The agent will:
1. Parse `Chunk/test_file.py` into function-level chunks using tree-sitter
2. Send the chunks to Gemini 2.5 Flash for code review
3. Print the review result

## Example Output

```
This code is syntactically correct and appears to implement the intended functionality without obvious errors.
```

## What is Coming

- Pydantic output schema with severity, category, suggestion, and line reference
- SQLite persistence layer for review history across multiple runs
- Diff-aware scoping that reviews only changed functions between two file versions