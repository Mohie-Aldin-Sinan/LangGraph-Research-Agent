from app.nodes import search_research


def test_search_research_removes_duplicate_urls(monkeypatch):

    mock_results = {
        "query 1": {
            "results": [
                {
                    "title": "AI Agents",
                    "url": "https://example.com/agents",
                    "content": "Information about agents."
                },
                {
                    "title": "LLM Agents",
                    "url": "https://example.com/llm",
                    "content": "Information about LLM agents."
                }
            ]
        },
        "query 2": {
            "results": [
                {
                    "title": "AI Agents Duplicate",
                    "url": "https://example.com/agents/",
                    "content": "Duplicate information."
                },
                {
                    "title": "Agent Frameworks",
                    "url": "https://example.com/frameworks",
                    "content": "Information about frameworks."
                }
            ]
        }
    }

    def mock_search_web(query):
        return mock_results[query]

    monkeypatch.setattr(
        "app.nodes.search_web",
        mock_search_web
    )

    state = {
        "research_plan": ["query 1", "query 2"]
    }

    result = search_research(state)

    assert len(result["search_results"]) == 3