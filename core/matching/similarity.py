from sklearn.metrics.pairwise import cosine_similarity

class Similarity:
    @staticmethod
    def compute(vec1, vec2):
        return cosine_similarity(vec1, vec2)