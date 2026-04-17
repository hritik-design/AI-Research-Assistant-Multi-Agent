import textwrap

from crewai import Task
from agents.research_specialist import research_specialist_agent


def create_research_task():
    return Task(
        agent=research_specialist_agent,
        description=textwrap.dedent("""
                    Conduct comprehensive research on the topic: {topic}

                    Your tasks:
                    1. Search for the most current and relevant information
                    2. Gather data from multiple reliable sources
                    3. Identify key facts, statistics, and expert opinions
                    4. Organize findings in a structured format
                    5. Ensure information is accurate and up-to-date

                    Provide a detailed research summary with (if applicable to the question type):
                    - Key findings or direct answers
                    - Important statistics, facts, or contextual details
                    - Expert opinions (if relevant)
                    - Recent developments (if relevant)
                    - Reliable sources used
                    Adjust the depth, structure, and format based on the complexity of the topic.
                    """),
        expected_output="A comprehensive research summary with key findings, statistics, expert opinions, recent developments, and sources",
        output_file="research_findings.md"
    )
