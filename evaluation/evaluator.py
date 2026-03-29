from core.representation.vectorizer import TFIDFVectorizer
from core.deep_learning.embedder import Embedder
from sklearn.metrics.pairwise import cosine_similarity


def compare_models(resume, job_desc):
    # TF-IDF
    tfidf = TFIDFVectorizer()
    tfidf_vectors = tfidf.fit_transform([resume, job_desc]).toarray()
    tfidf_score = cosine_similarity([tfidf_vectors[0]], [tfidf_vectors[1]])[0][0]

    # BERT / Deep Learning
    embedder = Embedder()
    emb1 = embedder.encode(resume)
    emb2 = embedder.encode(job_desc)
    bert_score = cosine_similarity([emb1], [emb2])[0][0]

    return {
        "TF-IDF": float(tfidf_score),
        "BERT": float(bert_score),
        "difference": float(bert_score - tfidf_score)
    }