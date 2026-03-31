from core.data_loader import load_jobs
from core.representation.vectorizer import TFIDFVectorizer
from core.skills.skill_engine import extract_skills, compare_skills
from core.deep_learning.embedder import Embedder
from core.matching.similarity import Similarity


def recommend_jobs(resume_text: str, top_k: int = 5):

    # -----------------------------
    # LOAD DATASET
    # -----------------------------
    df = load_jobs()

    job_texts = df["Job Description"].tolist()
    job_titles = df["Job Title"].tolist()

    # -----------------------------
    # INIT MODELS
    # -----------------------------
    tfidf = TFIDFVectorizer()
    embedder = Embedder()

    # Combine resume + jobs
    documents = [resume_text] + job_texts

    # -----------------------------
    # VECTOR REPRESENTATION
    # -----------------------------
    tfidf_vectors = tfidf.fit_transform(documents)
    embeddings = embedder.encode(documents)

    # -----------------------------
    # EXTRACT RESUME SKILLS
    # -----------------------------
    resume_skills = extract_skills(resume_text)

    recommendations = []

    # -----------------------------
    # LOOP THROUGH JOBS
    # -----------------------------
    for i, job_text in enumerate(job_texts):

        job_skills = extract_skills(job_text)

        # 🔹 Skill Matching Score
        skill_result = compare_skills(resume_skills, job_skills)
        skill_score = skill_result["score"]

        # 🔹 TF-IDF Similarity
        tfidf_score = float(
            Similarity.compute(tfidf_vectors[0], tfidf_vectors[i + 1])
        )

        # 🔹 BERT Similarity
        bert_score = float(
            Similarity.compute([embeddings[0]], [embeddings[i + 1]])
        )

        # 🔹 FINAL SCORE (weighted)
        final_score = round(
            0.3 * tfidf_score +
            0.5 * bert_score +
            0.2 * skill_score,
            3
        )

        # -----------------------------
        # STORE RESULT (🔥 FIXED PART)
        # -----------------------------
        recommendations.append({
            "job_title": job_titles[i],
            "job_description": job_text[:150],

            # 🔥 THESE WERE MISSING (CRITICAL FIX)
            "tfidf_score": tfidf_score,
            "bert_score": bert_score,
            "skill_score": skill_score,

            "final_score": final_score,
            "matched_skills": skill_result["matched"],
            "missing_skills": skill_result["missing"]
        })

    # -----------------------------
    # SORT BY BEST MATCH
    # -----------------------------
    recommendations.sort(
        key=lambda x: x["final_score"],
        reverse=True
    )

    # ----------------------------- 
    # RETURN TOP K
    # -----------------------------
    return recommendations[:top_k]