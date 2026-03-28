from core.skills.skill_engine import extract_skills, compare_skills


def recommend_jobs(resume_text: str, job_texts: list[str], top_k: int = 5) -> list[dict]:
    """
    Recommend top matching jobs for a resume.
    """

    if not resume_text or not job_texts:
        return []

    # 🔹 Extract resume skills
    resume_skills = extract_skills(resume_text)

    recommendations = []

    for i, job_text in enumerate(job_texts):

        job_skills = extract_skills(job_text)

        comparison = compare_skills(resume_skills, job_skills)

        recommendations.append({
            "job_id": i,
            "matched_skills": comparison["matched"],
            "missing_skills": comparison["missing"],
            "score": comparison["score"]
        })

    # 🔹 Sort by score
    recommendations.sort(key=lambda x: x["score"], reverse=True)

    # 🔹 Return top K results
    return recommendations[:top_k]