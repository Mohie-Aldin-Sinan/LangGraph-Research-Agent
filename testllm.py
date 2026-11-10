from dotenv import load_dotenv
from pydantic import BaseModel, Field

load_dotenv()

from app.llm import get_chat_model


class ResearchEvaluation(BaseModel):

    research_sufficient: bool = Field(
        description="Whether the research is sufficient."
    )

    coverage_assessment: str = Field(
        description="An explanation of research coverage."
    )

    missing_aspects: list[str] = Field(
        description="Important missing research areas."
    )

    follow_up_queries: list[str] = Field(
        description="Additional search queries."
    )


def main():

    model = get_chat_model()

    structured_model = model.with_structured_output(
        ResearchEvaluation,
        method="json_schema",
    )

    response = structured_model.invoke("""
    Evaluate the following research:

    Topic: AI Agents

    Findings:
    - AI agents can use tools.
    - AI agents can execute multi-step tasks.
    - LangGraph supports stateful workflows.

    The research does not cover framework comparisons
    or production deployment challenges.

    Determine whether additional research is necessary.
    """)

    print(response)
    print("\nResearch sufficient:", response.research_sufficient)
    print("Missing aspects:", response.missing_aspects)
    print("Follow-up queries:", response.follow_up_queries)


if __name__ == "__main__":
    main()