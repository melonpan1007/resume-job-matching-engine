def analyze_results(results):
    if not results:
        return {}

    avg_tfidf = sum(r.get("tfidf_score", 0) for r in results) / len(results)
    avg_bert = sum(r.get("bert_score", 0) for r in results) / len(results)

    return {
        "avg_tfidf": round(avg_tfidf, 3),
        "avg_bert": round(avg_bert, 3),
        "better_model": "BERT" if avg_bert > avg_tfidf else "TF-IDF"
    }