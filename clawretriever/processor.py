import os
from typing import List, Dict

class Document:
    def __init__(self, text: str, metadata: Dict):
        self.text = text
        self.metadata = metadata

class DocumentProcessor:
    """Handles text extraction and semantic chunking."""
    
    def load_directory(self, path: str) -> List[Document]:
        docs = []
        for root, _, files in os.walk(path):
            for file in files:
                if file.endswith((".txt", ".md")):
                    full_path = os.path.join(root, file)
                    with open(full_path, "r", encoding="utf-8") as f:
                        docs.append(Document(f.read(), {"source": file}))
        return docs

    def chunk_documents(self, documents: List[Document], size: int = 500, overlap: int = 50) -> List[Document]:
        chunks = []
        for doc in documents:
            text = doc.text
            start = 0
            while start < len(text):
                end = start + size
                chunk_text = text[start:end]
                chunks.append(Document(chunk_text, doc.metadata))
                start += (size - overlap)
        return chunks
