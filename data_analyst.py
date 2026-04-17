import os
import time
from crewai import Agent, LLM
from crewai_tools import FileReadTool

def enforce_rolling_window(*args, **kwargs):
    time.sleep(30)

# LLM configurations - Agent specific config
model = os.getenv("ANALYST_AGENT_LLM", "groq/llama-3.3-70b-versatile")
temperature = float(os.getenv("ANALYST_AGENT_TEMPERATURE", "0.2"))

llm = LLM(
    model=model,
    temperature=temperature,
    max_tokens=4000
)

data_analyst_agent = Agent(
    role="Data Analyst",
    goal="Analyze gathered information to extract key insights, patterns, and conclusions",
    backstory = (
                "You are a skilled data analyst with expertise in synthesizing complex "
                "information into actionable insights. You excel at identifying patterns, trends, "
                "and key findings from research data."
            ),
    llm=llm,
    tools=[FileReadTool()],
    verbose=True,
    step_callback=enforce_rolling_window,
)
