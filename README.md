# ClawRetriever

A robust RAG (Retrieval-Augmented Generation) framework leveraging OpenClaw agents for intelligent orchestration, semantic vector search, and advanced document processing.

## Overview

ClawRetriever bridges the gap between static knowledge bases and dynamic AI agents. It provides a modular pipeline for:
1.  **Document Ingestion**: Multi-format support with smart chunking strategies.
2.  **Vector Storage**: local FAISS indexing for high-performance similarity search.
3.  **Agentic Orchestration**: Uses OpenClaw to create specialized agents that query, synthesize, and validate retrieved context.

## Core Components

- **Collector**: Recursively scans directories for PDF, Markdown, and Text files.
- **Fragmenter**: Handles recursive character-based splitting to maintain semantic coherence.
- **Search Engine**: Wraps Sentence-Transformers and FAISS for efficient embedding generation and retrieval.
- **ClawAgent**: An OpenClaw-powered agent that acts as the "Brain", deciding how to use retrieved context to answer user queries.

## Architecture

1.  **Ingestion Phase**: Files -> Text -> Chunks -> Embeddings -> Vector Index.
2.  **Query Phase**: User Input -> Query Embedding -> Vector Search -> Top-K Context.
3.  **Generation Phase**: Context + Query -> OpenClaw Agent -> Synthesized Answer.

## Quick Start

### Prerequisites
- Python 3.9+
- OpenClaw installed (`pip install openclaw`)

### Installation

```bash
git clone https://github.com/user/clawretriever.git
cd clawretriever
pip install -r requirements.txt
```

### Usage

```python
from clawretriever.engine import RagPipeline

# Initialize the pipeline
pipeline = RagPipeline(data_dir="./docs")

# Run a query
response = pipeline.ask("How do I configure the OpenClaw agent parameters?")
print(f"Agent Response: {response}")
```

## Contributing
Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License
MIT License - see [LICENSE](LICENSE) for details.
