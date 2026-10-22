from app.graph import research_graph


def main():
    initial_state = {
        "name": "Mohie",
        "greeting": "",
        "response": "",
        "topic": "Ai agents",
        "research_plan": "",
    }

    result = research_graph.invoke(initial_state)

    print(result["response"])


if __name__ == "__main__":
    main()