from app.state import ResearchState
from app.tools import search_web


def greet_user(state: ResearchState) -> dict:
    return {
        "greeting": f"Hello, {state['name']}!"
    }


def plan_research(state: ResearchState) -> dict:
    topic = state["topic"]

    return {
        "research_plan": [
            f"Find reliable information about {topic}",
            f"Identify important facts about {topic}",
            f"Summarize the findings about {topic}",
        ]
    }


def search_research(state: ResearchState) -> dict:
    """Search the web using the research topic."""

    results = search_web(state["topic"])

    return {
        "search_results": results.get("results", [])
    }


def extract_findings(state: ResearchState) -> dict:
    """Extract useful text from the search results."""

    findings = []

    for result in state["search_results"]:
        title = result.get("title", "")
        content = result.get("content", "")
        url = result.get("url", "")

        if content.strip():
            findings.append(
                f"Title: {title}\n"
                f"Source: {url}\n"
                f"Finding: {content}"
            )

    return {"findings": findings}


def prepare_response(state: ResearchState) -> dict:
    """Build a structured report from retrieved information."""

    if not state["findings"]:
        return {
            "response": "",
            "error": "No useful findings were retrieved.",
        }

    findings_text = "\n\n".join(
        f"{index}. {finding}"
        for index, finding in enumerate(
            state["findings"],
            start=1,
        )
    )

    response = (
        f"{state['greeting']}\n\n"
        f"# Research Report: {state['topic']}\n\n"
        f"## Findings\n\n"
        f"{findings_text}\n\n"
        f"## Research Plan\n\n"
        + "\n".join(
            f"{index}. {step}"
            for index, step in enumerate(
                state["research_plan"],
                start=1,
            )
        )
    )

    return {
        "response": response,
        "error": "",
    }