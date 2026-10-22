from app.graph import research_graph


def main():
    initial_state = {
        "name": "Mohie",
        "greeting": "",
        "response": "",
        "topic": "AI Agents",
        "research_plan": [],
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