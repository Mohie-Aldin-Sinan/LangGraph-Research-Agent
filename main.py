import os

from dotenv import load_dotenv

load_dotenv()

if not os.getenv("TAVILY_API_KEY"):
    raise RuntimeError(
        "TAVILY_API_KEY is missing. "
        "Add it to your .env file."
    )

from app.graph import research_graph


def main():
    initial_state = {
        "name": "Mohie",
        "greeting": "",
        "topic": "AI agents",
        "research_plan": [],
        "search_results": [],
        "findings": [],
        "response": "",
        "retry_count": 0,
        "error": "",
    }

    result = research_graph.invoke(initial_state)

    if result["error"]:
        print(f"Research failed: {result['error']}")
        return

    print(result["response"])


if __name__ == "__main__":
    main()