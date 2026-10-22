from app.state import ResearchState

MAX_RETRIES = 3


def greet_user(state: ResearchState) -> dict:
    return {
        "greeting": f"Hello, {state['name']}!"
    }


def plan_research(state: ResearchState) -> dict:
    topic = state["topic"]

    research_plan = [
        f"Understand the fundamentals of {topic}",
        f"Identify major developments in {topic}",
        f"Evaluate practical applications of {topic}",
        f"Summarize the key findings about {topic}",
    ]

    return {
        "research_plan": research_plan,
        "error": "",
    }


def route_research(state: ResearchState) -> str:
    if state["research_plan"]:
        return "success"

    if state["retry_count"] < MAX_RETRIES:
        return "retry"

    return "failure"


def retry_research(state: ResearchState) -> dict:
    return {
        "retry_count": state["retry_count"] + 1
    }


def handle_failure(state: ResearchState) -> dict:
    return {
        "error": (
            "Unable to generate a valid research plan "
            f"after {MAX_RETRIES} retries."
        )
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
        f"{state['greeting']}\n\n"
        f"Research topic: {state['topic']}\n\n"
        f"Research plan:\n{plan}"
    )

    return {"response": response}