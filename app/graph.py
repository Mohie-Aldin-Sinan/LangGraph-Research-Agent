from langgraph.graph import END, START, StateGraph

from app.state import ResearchState
from app.nodes import (
    greet_user,
    plan_research,
    search_research,
    extract_findings,
    prepare_response,
)


def build_graph():
    builder = StateGraph(ResearchState)

    builder.add_node("greet_user", greet_user)
    builder.add_node("plan_research", plan_research)
    builder.add_node("search_research", search_research)
    builder.add_node("extract_findings", extract_findings)
    builder.add_node("prepare_response", prepare_response)

    builder.add_edge(START, "greet_user")
    builder.add_edge("greet_user", "plan_research")
    builder.add_edge("plan_research", "search_research")
    builder.add_edge("search_research", "extract_findings")
    builder.add_edge("extract_findings", "prepare_response")
    builder.add_edge("prepare_response", END)

    return builder.compile()


research_graph = build_graph()