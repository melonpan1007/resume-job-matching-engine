def generate_explanation(result):
    """
    Generate human-readable explanation for match
    """

    return f"""
    Match Score: {result['final_score']}

    TF-IDF Similarity: {result['tfidf_score']}
    Semantic Similarity (BERT): {result['bert_score']}
    Skill Match Score: {result['skill_score']}

    Matched Skills: {", ".join(result['matched_skills'])}
    Missing Skills: {", ".join(result['missing_skills'])}
    """