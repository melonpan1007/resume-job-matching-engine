# ---------------------------------------------
# TEST FILE: Semantic Similarity using BERT
# ---------------------------------------------

# Import embedding model (Deep Learning)
from core.deep_learning.embedder import Embedder

# Import similarity function (Cosine similarity)
from core.matching.similarity import Similarity


# ---------------------------------------------
# STEP 1: Define sample texts
# ---------------------------------------------
# These simulate:
# Resume vs Job Description
texts = [
    "Python developer with machine learning skills",
    "Looking for machine learning engineer"
]


# ---------------------------------------------
# STEP 2: Convert text → embeddings
# ---------------------------------------------
# Embedder uses Sentence-BERT model
embedder = Embedder()

# Convert both texts into vector representations
embeddings = embedder.encode(texts)


# ---------------------------------------------
# STEP 3: Compute similarity
# ---------------------------------------------
# We compare the two vectors using cosine similarity
score = Similarity.compute([embeddings[0]], [embeddings[1]])


# ---------------------------------------------
# STEP 4: Display result
# ---------------------------------------------
print("\n=== Semantic Similarity Test ===")

print(f"Text 1: {texts[0]}")
print(f"Text 2: {texts[1]}")

# Convert score to float (since sklearn returns array)
score_value = float(score)

print(f"Similarity Score: {round(score_value, 3)}")


# ---------------------------------------------
# STEP 5: Interpret result
# ---------------------------------------------
# Simple interpretation based on score
if score_value > 0.7:
    print("Result: HIGH similarity (semantic match)")
elif score_value > 0.4:
    print("Result: MEDIUM similarity")
else:
    print("Result: LOW similarity")