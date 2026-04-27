import faiss
import numpy as np

class VectorStore:
    def __init__(self, embeddings, chunks):
        self.chunks = chunks
        self.embeddings = np.array(embeddings).astype("float32")
        dimension = self.embeddings.shape[1]
        self.index = faiss.IndexFlatL2(dimension)
        self.index.add(self.embeddings)

    def search(self, query_embedding, k=3):
        query_embedding = np.array([query_embedding]).astype("float32")
        distances, indices = self.index.search(query_embedding, k)
        results = [self.chunks[i] for i in indices[0]]
        return results