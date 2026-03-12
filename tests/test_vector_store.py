import unittest
from clawretriever.vector_store import VectorStore
import os
import shutil

class TestVectorStore(unittest.TestCase):
    def test_search(self):
        if os.path.exists("test_store"):
            shutil.rmtree("test_store")
            
        vs = VectorStore("test_store/index.faiss")
        class MockDoc:
            def __init__(self, text): self.text = text
            
        vs.add_documents([MockDoc("The capital of France is Paris"), MockDoc("Apples are usually red")])
        results = vs.search("What is the capital of France?", k=1)
        self.assertIn("Paris", results[0].text)
        
        if os.path.exists("test_store"):
            shutil.rmtree("test_store")

if __name__ == "__main__":
    unittest.main()
