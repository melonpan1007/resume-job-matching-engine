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

    documents = [resume_text] + job_texts

    # -----------------------------
    # VECTOR REPRESENTATION
    # -----------------------------
    tfidf_vectors = tfidf.fit_transform(documents)
    embeddings = embedder.encode(documents)

    # -----------------------------
    # EXTRACT SKILLS
    # -----------------------------
    resume_skills = extract_skills(resume_text)

    recommendations = []

    # -----------------------------
    # PROCESS EACH JOB
    # -----------------------------
    for i, job_text in enumerate(job_texts):

        job_skills = extract_skills(job_text)

        # Skill score
        skill_result = compare_skills(resume_skills, job_skills)
        skill_score = float(skill_result["score"])

        # TF-IDF
        tfidf_score = float(
            Similarity.compute(tfidf_vectors[0], tfidf_vectors[i + 1])
        )

        # BERT
        bert_score = float(
            Similarity.compute([embeddings[0]], [embeddings[i + 1]])
        )

        # Final Score
        final_score = round(
            0.3 * tfidf_score +
            0.5 * bert_score +
            0.2 * skill_score,
            3
        )

        # 🔥 NEW FEATURES
        missing_skills = skill_result["missing"]

        recommendation = {
            "job_title": job_titles[i],
            "job_description": job_text[:150],

            "tfidf_score": round(tfidf_score, 3),
            "bert_score": round(bert_score, 3),
            "skill_score": round(skill_score, 3),

            "final_score": final_score,
            "matched_skills": skill_result["matched"],
            "missing_skills": missing_skills,

            # 🔥 Skill Gap Suggestion
            "suggestion": (
                f"Improve skills: {', '.join(missing_skills)}"
                if missing_skills else "Strong match"
            ),

            # 🔥 Explainability
            "explanation": (
                f"Matched using TF-IDF ({round(tfidf_score,2)}), "
                f"BERT ({round(bert_score,2)}), "
                f"Skill match ({round(skill_score,2)})"
            )
        }

        recommendations.append(recommendation)

    # -----------------------------
    # SORT
    # -----------------------------
    recommendations.sort(
        key=lambda x: x["final_score"],
        reverse=True
    )

    # -----------------------------
    # OVERALL SCORE (🔥 BIG FEATURE)
    # -----------------------------
    if recommendations:
        overall = sum(r["final_score"] for r in recommendations[:top_k]) / top_k
    else:
        overall = 0

    return {
        "overall_score": round(overall * 100, 2),
        "recommendations": recommendations[:top_k]
    }