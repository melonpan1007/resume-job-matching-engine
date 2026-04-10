from sklearn.metrics.pairwise import cosine_similarity

class Similarity:
    @staticmethod
    def compute(vec1, vec2):
        return float(cosine_similarity(vec1, vec2)[0][0])