import re

# You can expand this list later
COMMON_SKILLS = [
    "python",
    "java",
    "c++",
    "machine learning",
    "deep learning",
    "sql",
    "mongodb",
    "docker",
    "kubernetes",
    "react",
    "node",
    "aws",
    "git",
    "data analysis",
]


def extract_skills(text: str) -> list[str]:
    """
    Extract skills from text.

    Args:
        text (str): Input text

    Returns:
        list[str]: List of extracted skills
    """

    text = text.lower()
    found_skills = []

    for skill in COMMON_SKILLS:
        # match full word only
        if re.search(r"\b" + re.escape(skill) + r"\b", text):
            found_skills.append(skill)

    return list(set(found_skills))  # remove duplicates


def compare_skills(resume_skills: list[str], job_skills: list[str]) -> dict:
    """
    Compare resume skills with job skills.

    Returns:
        dict: {
            "matched": [],
            "missing": [],
            "score": float
        }
    """

    resume_set = set(resume_skills)
    job_set = set(job_skills)

    matched = list(resume_set.intersection(job_set))
    missing = list(job_set - resume_set)

    # score = matched / total required job skills
    if len(job_set) == 0:
        score = 0.0
    else:
        score = len(matched) / len(job_set)

    return {
        "matched": matched,
        "missing": missing,
        "score": round(score, 2)
    }