from app.state import ResearchState


def greet_user(state: ResearchState) -> dict:
    return {
        "greeting": f"Hello, {state['name']}!"
    }

def plan_research(state: ResearchState) -> dict:
    topic = state["topic"]

    return {
        "research_plan": [
            f"Understand the fundamentals of {topic}",
            f"Identify major developments in {topic}",
            f"Summarize key findings about {topic}",
        ]
    }

def prepare_response(state: ResearchState) -> dict:
    plan = "\n".join(
        f"{index}. {step}"
        for index, step in enumerate(
            state["research_plan"],
            start=1,
        )
    )

    response = (
        f"{state['greeting']}\n"
        "Welcome to your Research Agent.\n\n"
        f"Research topic: {state['topic']}\n\n"
        f"Research plan:\n{plan}\n\n"
        "Thank you!"
    )

    return {"response": response}
