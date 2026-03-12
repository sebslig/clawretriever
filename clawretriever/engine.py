import os
import logging
from typing import List, Optional
from clawretriever.processor import DocumentProcessor
from clawretriever.vector_store import VectorStore
from clawretriever.agent import RetrievalAgent

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class RagPipeline:
    """
    The main entry point for the ClawRetriever RAG system.
    """
    def __init__(self, data_dir: str, index_path: str = "storage/index.faiss"):
        self.processor = DocumentProcessor()
        self.vector_store = VectorStore(index_path)
        self.agent = RetrievalAgent()
        
        if os.path.exists(data_dir):
            self.ingest(data_dir)

    def ingest(self, directory: str):
        """Processes and indexes documents from a directory."""
        logger.info(f"Ingesting documents from {directory}")
        documents = self.processor.load_directory(directory)
        chunks = self.processor.chunk_documents(documents)
        self.vector_store.add_documents(chunks)
        self.vector_store.save()

    def ask(self, query: str) -> str:
        """Retrieves context and generates a response via the OpenClaw agent."""
        context_chunks = self.vector_store.search(query, k=4)
        context_text = "\n---\n".join([c.text for c in context_chunks])
        
        response = self.agent.generate_response(query, context_text)
        return response
