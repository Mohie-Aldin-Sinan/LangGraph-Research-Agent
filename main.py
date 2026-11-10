import os

from dotenv import load_dotenv

load_dotenv()

if not os.getenv("TAVILY_API_KEY"):
    raise RuntimeError(
        "TAVILY_API_KEY is missing. "
        "Add it to your .env file."
    )

if not os.getenv("GROQ_API_KEY"):
    raise RuntimeError("GROQ_API_KEY is missing.")

from app.graph import research_graph


def main():
    initial_state = {
    "name": "Mohie",
    "greeting": "",
    "topic": "AI Agents",

    "research_plan": [],

    "search_results": [],
    "findings": [],
    "pending_search_results": [],

    "research_sufficient": False,
    "coverage_assessment": "",
    "missing_aspects": [],
    "follow_up_queries": [],

    "retry_count": 0,
    "max_retries": 2,

    "response": "",
    "error": "",
    }

    result = research_graph.invoke(initial_state)

    if result["error"]:
        print(f"Research failed: {result['error']}")
        return

    print(result["response"])


if __name__ == "__main__":
    main()