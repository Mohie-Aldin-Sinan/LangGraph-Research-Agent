from langgraph.graph import END, START, StateGraph

from app.nodes import greet_user, plan_research, prepare_response
from app.state import ResearchState


def build_graph():
    builder = StateGraph(ResearchState)

    builder.add_node("greet_user", greet_user)
    builder.add_node("plan_research", plan_research)
    builder.add_node("prepare_response", prepare_response)

    builder.add_edge(START, "greet_user")
    builder.add_edge("greet_user", "plan_research")
    builder.add_edge("plan_research", "prepare_response")
    builder.add_edge("prepare_response", END)

    return builder.compile()


research_graph = build_graph()