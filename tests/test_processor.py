import unittest
from clawretriever.processor import DocumentProcessor, Document

class TestProcessor(unittest.TestCase):
    def setUp(self):
        self.processor = DocumentProcessor()

    def test_chunking(self):
        doc = Document("This is a long sentence for testing chunking logic.", {"source": "test"})
        chunks = self.processor.chunk_documents([doc], size=10, overlap=2)
        self.assertGreater(len(chunks), 1)
        self.assertEqual(chunks[0].metadata["source"], "test")

if __name__ == "__main__":
    unittest.main()
