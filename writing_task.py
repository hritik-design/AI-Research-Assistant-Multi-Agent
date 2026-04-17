import textwrap

from crewai import Task
from agents.content_writer import content_writer_agent
def create_writing_task(research_task_instance, analysis_task_instance):
    return Task(
        agent=content_writer_agent,
        description=textwrap.dedent("""
                    Create a comprehensive report on the topic: {topic}

                    Your tasks:
                    1. Review both research findings and analysis results
                    2. Write a well-structured, comprehensive report
                    3. Ensure clarity and readability for the target audience
                    4. Include executive summary, main content, and conclusions
                    5. Cite all sources appropriately

                    The report should include (scale complexity based on topic length):
                    - Executive Summary or Direct Answer
                    - Introduction or Context
                    - Main Findings or Explanations
                    - Analysis and Insights
                    - Conclusions and Recommendations
                    - Sources and References
                    """),
        expected_output="A comprehensive, well-structured report with executive summary and conclusions",
        context=[analysis_task_instance],
        output_file="final_report.md"
    )
