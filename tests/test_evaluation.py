from evaluation.evaluator import compare_models
from evaluation.analytics import analyze_results

# Sample multiple results
results = [
    compare_models("Python developer", "Looking for Python engineer"),
    compare_models("Data analyst with SQL", "Need data scientist with Python"),
    compare_models("Frontend React developer", "Looking for backend Java dev")
]

analysis = analyze_results(results)

print("\n=== Analytics Result ===")
print(analysis)