from collections import Counter

def evaluate_consistency(results):
    consistent = all(r["routed_to"] != "general_support" for r in results if r["urgency"] == "high")
    return "High urgency routing consistency: PASS" if consistent else "FAIL"

def count_by_urgency(results):
    return dict(Counter([r["urgency"] for r in results]))

def routes_summary(results):
    return dict(Counter([r["routed_to"] for r in results]))
