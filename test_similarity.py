from core.deep_learning.embedder import Embedder
from core.matching.similarity import Similarity

texts = [
    "Python developer with ML skills",
    "Looking for machine learning engineer"
]

embedder = Embedder()
embeddings = embedder.encode(texts)

score = Similarity.compute([embeddings[0]], [embeddings[1]])

print(score)