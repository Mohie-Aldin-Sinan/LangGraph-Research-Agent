import os
from functools import lru_cache

from langchain_openai import ChatOpenAI


@lru_cache(maxsize=1)
def get_chat_model() -> ChatOpenAI:
    """Initialize and cache the Groq chat model."""

    return ChatOpenAI(
        model=os.getenv(
            "GROQ_MODEL",
            "openai/gpt-oss-120b"
        ),
        api_key=os.getenv("GROQ_API_KEY"),
        base_url="https://api.groq.com/openai/v1",
        temperature=0,
        timeout=30,
        max_retries=2,
    )