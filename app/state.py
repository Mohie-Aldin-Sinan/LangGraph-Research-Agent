from typing import TypedDict


class ResearchState(TypedDict):
    name: str
    greeting: str
    topic: str
    research_plan: list[str]
    search_results: list[dict]
    findings: list[str]
    response: str
    retry_count: int
    error: str