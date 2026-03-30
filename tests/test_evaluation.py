# --------------------------------------------------
# FIX IMPORT PATH ISSUE (IMPORTANT)
# --------------------------------------------------
import sys
import os

# Add project root to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


# --------------------------------------------------
# IMPORT MODULES
# --------------------------------------------------
from evaluation.evaluator import compare_models
from evaluation.analytics import analyze_results


# --------------------------------------------------
# STEP 1: DEFINE TEST CASES
# --------------------------------------------------
# Each tuple = (resume_text, job_text)
test_cases = [
    ("Python developer with machine learning", "Looking for ML engineer"),
    ("Data analyst with SQL and Excel", "Hiring data scientist with Python"),
    ("Frontend React developer", "Looking for backend Java developer")
]


# --------------------------------------------------
# STEP 2: RUN MODEL COMPARISON
# --------------------------------------------------
results = []

print("\n==============================")
print("🚀 MODEL EVALUATION TEST")
print("==============================")

for i, (resume, job) in enumerate(test_cases, 1):

    # Run comparison (TF-IDF + BERT)
    result = compare_models(resume, job)

    results.append(result)

    print(f"\n--- Test Case {i} ---")
    print(f"Resume: {resume}")
    print(f"Job: {job}")

    print(f"TF-IDF Score : {round(result['TF-IDF'], 3)}")
    print(f"BERT Score   : {round(result['BERT'], 3)}")

    # Quick interpretation
    if result['BERT'] > result['TF-IDF']:
        print("👉 BERT captured better semantic meaning")
    else:
        print("👉 TF-IDF performed better (keyword match)")


# --------------------------------------------------
# STEP 3: ANALYZE OVERALL PERFORMANCE
# --------------------------------------------------
analysis = analyze_results(results)


# --------------------------------------------------
# STEP 4: FINAL SUMMARY
# --------------------------------------------------
print("\n==============================")
print("📊 FINAL ANALYSIS")
print("==============================")

print(f"Average TF-IDF Score : {round(analysis['avg_tfidf'], 3)}")
print(f"Average BERT Score   : {round(analysis['avg_bert'], 3)}")
print(f"Better Model         : {analysis['better_model']}")


# --------------------------------------------------
# STEP 5: FINAL INSIGHT (FOR VIVA)
# --------------------------------------------------
if analysis['better_model'] == "BERT":
    print("\n✅ Insight: BERT performs better for semantic understanding.")
else:
    print("\n✅ Insight: TF-IDF performs better for keyword matching.")