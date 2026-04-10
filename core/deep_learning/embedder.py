from sentence_transformers import SentenceTransformer

# 🔥 LOAD MODEL ONLY ONCE (GLOBAL)
_model = SentenceTransformer('all-MiniLM-L6-v2')


class Embedder:
    def encode(self, texts):
        if isinstance(texts, str):
            texts = [texts]
        return _model.encode(texts)