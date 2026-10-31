from app.nodes import extract_findings


def test_extract_findings():

    state = {
        "search_results": [
            {
                "title": "AI Agents",
                "url": "https://example.com/agents",
                "content": " AI agents use tools to perform tasks. "
            },
            {
                "title": "Empty Result",
                "url": "https://example.com/empty",
                "content": "   "
            },
            {
                "title": "Missing URL",
                "content": "Agents can execute multi-step workflows."
            },
        ]
    }

    result = extract_findings(state)

    findings = result["findings"]

    assert len(findings) == 2

    assert findings[0]["title"] == "AI Agents"

    assert findings[0]["content"] == (
        "AI agents use tools to perform tasks."
    )

    assert findings[1]["url"] == ""