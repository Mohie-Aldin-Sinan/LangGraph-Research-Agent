from langgraph.graph import END, START, StateGraph

from app.nodes import (
    greet_user,
    handle_failure,
    plan_research,
    prepare_response,
    retry_research,
    route_research,
)
from app.state import ResearchState


def build_graph():
    builder = StateGraph(ResearchState)

    builder.add_node("greet_user", greet_user)
    builder.add_node("plan_research", plan_research)
    builder.add_node("retry_research", retry_research)
    builder.add_node("handle_failure", handle_failure)
    builder.add_node("prepare_response", prepare_response)

    builder.add_edge(START, "greet_user")
    builder.add_edge("greet_user", "plan_research")

    builder.add_conditional_edges(
        "plan_research",
        route_research,
        {
            "success": "prepare_response",
            "retry": "retry_research",
            "failure": "handle_failure",
        },
    )

    builder.add_edge("retry_research", "plan_research")
    builder.add_edge("handle_failure", END)
    builder.add_edge("prepare_response", END)

    return builder.compile()


research_graph = build_graph()