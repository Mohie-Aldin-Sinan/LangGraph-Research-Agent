from operator import add
from typing import Annotated, TypedDict


class ResearchState(TypedDict):
    name: str
    greeting: str
    topic: str

    research_plan: list[str]

    search_results: Annotated[list[dict], add]

    findings: Annotated[list[dict[str, str]], add]

    pending_search_results: list[dict]

    research_sufficient: bool
    coverage_assessment: str
    missing_aspects: list[str]
    follow_up_queries: list[str]

    retry_count: int
    max_retries: int

    response: str
    error: str