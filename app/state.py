from typing import TypedDict


class ResearchState(TypedDict):
    name: str
    greeting: str
    response: str
    topic: str
    research_plan: list[str]