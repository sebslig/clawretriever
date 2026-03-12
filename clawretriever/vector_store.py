import faiss
import numpy as np
import pickle
import os
from sentence_transformers import SentenceTransformer
from typing import List

class VectorStore:
    """Wrapper around FAISS and Sentence-Transformers for vector operations."""
    
    def __init__(self, index_path: str, model_name: str = "all-MiniLM-L6-v2"):
        self.index_path = index_path
        self.model = SentenceTransformer(model_name)
        self.dimension = self.model.get_sentence_embedding_dimensions()
        self.index = faiss.IndexFlatL2(self.dimension)
        self.documents = []

    def add_documents(self, documents: List):
        if not documents:
            return
        texts = [doc.text for doc in documents]
        embeddings = self.model.encode(texts)
        self.index.add(np.array(embeddings).astype("float32"))
        self.documents.extend(documents)

    def search(self, query: str, k: int = 5):
        query_vec = self.model.encode([query]).astype("float32")
        distances, indices = self.index.search(query_vec, k)
        
        results = []
        for idx in indices[0]:
            if idx != -1 and idx < len(self.documents):
                results.append(self.documents[idx])
        return results

    def save(self):
        os.makedirs(os.path.dirname(self.index_path), exist_ok=True)
        faiss.write_index(self.index, self.index_path)
        with open(self.index_path + ".docs", "wb") as f:
            pickle.dump(self.documents, f)
