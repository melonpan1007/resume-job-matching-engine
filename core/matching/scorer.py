from core.representation.vectorizer import TFIDFVectorizer
from core.deep_learning.embedder import Embedder
from core.matching.similarity import Similarity
from core.skills.skill_engine import extract_skills, compare_skills


def match_resume_job(resume_text: str, job_text: str):
    """
    Full pipeline: Resume vs Job Matching
    """

    # 🔹 INIT models
    tfidf = TFIDFVectorizer()
    embedder = Embedder()

    documents = [resume_text, job_text]

    # 🔹 TF-IDF
    tfidf_vectors = tfidf.fit_transform(documents)
    tfidf_score = Similarity.compute(tfidf_vectors[0], tfidf_vectors[1])

    # 🔹 BERT
    embeddings = embedder.encode(documents)
    bert_score = Similarity.compute([embeddings[0]], [embeddings[1]])

    # 🔹 Skills
    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_text)

    skill_result = compare_skills(resume_skills, job_skills)
    skill_score = skill_result["score"]

    # 🔹 FINAL SCORE
    final_score = round(
        0.4 * tfidf_score +
        0.4 * bert_score +
        0.2 * skill_score, 3
    )

    return {
        "tfidf_score": tfidf_score,
        "bert_score": bert_score,
        "skill_score": skill_score,
        "final_score": final_score,
        "matched_skills": skill_result["matched"],
        "missing_skills": skill_result["missing"]
    }