import textwrap

from crewai import Task
from agents.data_analyst import data_analyst_agent
def create_analysis_task(research_task_instance):
    return Task(
        agent=data_analyst_agent,
        description=textwrap.dedent("""
                    Analyze the research findings for the topic: {topic}

                    Your tasks:
                    1. Review the research findings from the previous task
                    2. Identify patterns, trends, and key insights
                    3. Analyze the implications and significance
                    4. Provide expert interpretation of the data
                    5. Highlight the most important conclusions

                    Provide (as relevant to the topic):
                    - Key insights, patterns, or straightforward explanations
                    - Trend analysis or broader context
                    - Implications and significance
                    - Expert interpretation
                    - Actionable conclusions or a complete concise summary
                    Adjust the output scale based on whether the topic is a deep research inquiry or a general question.
                    """),
        expected_output="A detailed analysis report with insights, patterns, and conclusions",
        context=[research_task_instance],
        output_file="analysis_report.md"
    )
