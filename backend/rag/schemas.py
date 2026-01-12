from pydantic import BaseModel
from typing import List


class QAResponse(BaseModel):
    answer: str
    sources: List[str]


class SummaryResponse(BaseModel):
    summary: str
    key_points: List[str]


class ComparisonResponse(BaseModel):
    similarities: List[str]
    differences: List[str]
