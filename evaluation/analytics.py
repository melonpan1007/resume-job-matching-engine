def analyze_results(results):
    avg_tfidf = sum(r["TF-IDF"] for r in results) / len(results)
    avg_bert = sum(r["BERT"] for r in results) / len(results)

    return {
        "avg_tfidf": avg_tfidf,
        "avg_bert": avg_bert,
        "better_model": "BERT" if avg_bert > avg_tfidf else "TF-IDF"
    }