from .prompts import QA_PROMPT, SUMMARY_PROMPT, COMPARISON_PROMPT
from .schemas import QAResponse, SummaryResponse, ComparisonResponse


def route(query_type: str):
    if query_type == "summary":
        return SUMMARY_PROMPT, SummaryResponse
    if query_type == "comparison":
        return COMPARISON_PROMPT, ComparisonResponse
    return QA_PROMPT, QAResponse
