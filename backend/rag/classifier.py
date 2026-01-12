def classify(question: str) -> str:
    q = question.lower()
    if "compare" in q or "difference" in q:
        return "comparison"
    if "summary" in q or "summarize" in q:
        return "summary"
    return "qa"
