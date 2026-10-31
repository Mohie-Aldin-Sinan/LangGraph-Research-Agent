from urllib.parse import urlsplit, urlunsplit

from app.state import ResearchState
from app.tools import search_web


def get_result_key(result: dict) -> str:
    """Generate a unique identifier for a search result."""

    url = result.get("url", "")

    if isinstance(url, str) and url.strip():
        parsed_url = urlsplit(url.strip())

        normalized_url = urlunsplit((
            parsed_url.scheme.lower(),
            parsed_url.netloc.lower(),
            parsed_url.path.rstrip("/") or "/",
            parsed_url.query,
            "",
        ))

        return normalized_url

    # Fallback when the result has no URL.
    title = " ".join(result.get("title", "").lower().split())
    content = " ".join(result.get("content", "").lower().split())

    return f"{title}|{content}"


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
    """Search using every research query and remove duplicate results."""

    all_results = []
    seen_results = set()

    for query in state["research_plan"]:

        print(f"Searching: {query}")

        results = search_web(query)

        query_results = results.get("results", [])

        for result in query_results:

            if not isinstance(result, dict):
                continue

            result_key = get_result_key(result)

            if result_key in seen_results:
                continue

            seen_results.add(result_key)
            all_results.append(result)

    print(f"Unique results collected: {len(all_results)}")

    return {
        "search_results": all_results
    }


def extract_findings(state: ResearchState) -> dict:
    """Extract and clean useful information from search results."""

    findings = []

    for result in state["search_results"]:

        if not isinstance(result, dict):
            continue

        title = result.get("title", "")
        content = result.get("content", "")
        url = result.get("url", "")

        # Validate content.
        if not isinstance(content, str):
            continue

        content = content.strip()

        if not content:
            continue

        # Clean metadata.
        if not isinstance(title, str):
            title = ""

        if not isinstance(url, str):
            url = ""

        finding = {
            "title": title.strip() or "Untitled source",
            "url": url.strip(),
            "content": content,
        }

        findings.append(finding)

    return {
        "findings": findings
    }


def prepare_response(state: ResearchState) -> dict:
    """Build a structured report from retrieved information."""

    if not state["findings"]:
        return {
            "response": "",
            "error": "No useful findings were retrieved.",
        }

    findings_text = ""

    for index, finding in enumerate(
        state["findings"],
        start=1,
    ):
        findings_text += (
            f"### Finding {index}\n"
            f"Title: {finding['title']}\n"
            f"Source: {finding['url'] or 'URL unavailable'}\n"
            f"Content: {finding['content']}\n\n"
        )

    research_plan = "\n".join(
        f"{index}. {step}"
        for index, step in enumerate(
            state["research_plan"],
            start=1,
        )
    )

    response = (
        f"{state['greeting']}\n\n"
        f"# Research Report: {state['topic']}\n\n"
        f"## Findings\n\n"
        f"{findings_text}\n"
        f"## Research Plan\n\n"
        f"{research_plan}"
    )

    return {
        "response": response,
        "error": "",
    }