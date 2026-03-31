#Configuration settings for Talent Match 

MODEL_NAME = "all-MiniLM-L6-v2"

TFIDF_MAX_FEATURES = 5000

SCORING_WEIGHTS = {
    "tfidf" : 0.4,
    "bert": 0.4,
    "skills": 0.2
}

#centralized hyperparameters using config management