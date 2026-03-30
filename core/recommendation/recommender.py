from core.skills.skill_engine import extract_skills, compare_skills
from core.representation.vectorizer import TFIDFVectorizer
from core.deep_learning.embedder import Embedder
from core.matching.similarity import Similarity
from core.ingestion.job_loader import load_jobs


def recommend_jobs(resume_text: str, top_k: int = 5):

    jobs = load_jobs()

    if not resume_text or not jobs:
        return []

    # 🔹 INIT models
    tfidf = TFIDFVectorizer()
    embedder = Embedder()

    documents = [resume_text] + [job["text"] for job in jobs]

    # 🔹 TF-IDF vectors
    tfidf_vectors = tfidf.fit_transform(documents)

    # 🔹 BERT embeddings
    embeddings = embedder.encode(documents)

    resume_skills = extract_skills(resume_text)

    recommendations = []

    for i, job in enumerate(jobs):

        job_text = job["text"]
        job_title = job["title"]

        job_skills = extract_skills(job_text)

        # 🔹 Skill score
        skill_result = compare_skills(resume_skills, job_skills)
        skill_score = skill_result["score"]

        # 🔹 TF-IDF score
        tfidf_score = Similarity.compute(
            tfidf_vectors[0], tfidf_vectors[i + 1]
        )

        # 🔹 BERT score
        bert_score = Similarity.compute(
            [embeddings[0]], [embeddings[i + 1]]
        )

        # 🔹 FINAL SCORE
        final_score = round(
            0.3 * tfidf_score +
            0.5 * bert_score +
            0.2 * skill_score, 3
        )

        recommendations.append({
            "job_title": job_title,
            "tfidf_score": float(tfidf_score),
            "bert_score": float(bert_score),
            "skill_score": float(skill_score),
            "final_score": float(final_score),
            "matched_skills": skill_result["matched"],
            "missing_skills": skill_result["missing"]
        })

    recommendations.sort(key=lambda x: x["final_score"], reverse=True)

    return recommendations[:top_k]