# Lazybot - An attempt of using tool use, local vector RAG multi-modal agent
### Agnostic API approach to being lazy with AI! 


A local-first AI agent with tool use, RAG over large PDF collections, vision/OCR, and web browsing.

## Quick Start

```bash
# 1. Clone and enter project
cd lazybot-agent

# 2. Create virtual environment
python -m venv .venv
.venv\Scripts\activate   # Windows
# source .venv/bin/activate  # macOS/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure
copy .env.example .env
# Edit .env with your API key and allowed directories

# 5. (Optional) Index PDFs for RAG
python -m agent.rag.ingest --dir "C:\path\to\pdfs"

# 6. Run the agent
python -m agent.main
# OPTIONAL PDF INDEX:
python -m agent.main --index PATH

```



## Features

**Tool use**: scoped filesystem read/search, web search/fetch
**RAG**: incremental PDF ingestion with checksums, chunked embeddings, metadata filters
**Vision**: image understanding via multimodal models, OCR for scanned PDFs
**Safety**: confirmation prompts for risky actions, audit logging, directory allowlists
**agnostic**: OpenRouter, OpenAI, Anthropic, or local Ollama models
