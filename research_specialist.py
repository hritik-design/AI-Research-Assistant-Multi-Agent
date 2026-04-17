import os
import time
from crewai import Agent, LLM
from crewai_tools import SerperDevTool

def enforce_rolling_window(*args, **kwargs):
    time.sleep(30)

# LLM configurations - Agent specific config
model = os.getenv("RESEARCH_AGENT_LLM", "groq/llama-3.3-70b-versatile")
temperature = float(os.getenv("RESEARCH_AGENT_TEMPERATURE", "0.2"))

llm = LLM(
    model=model,
    temperature=temperature,
    max_tokens=4000
)

research_specialist_agent = Agent(
    role="Research Specialist",
    goal="Gather comprehensive and accurate information on given topics from multiple sources.",
    backstory="You are an expert researcher with a keen eye for details and a passion for uncovering facts.",
    llm=llm,
    tools=[SerperDevTool(n_results=3)],
    verbose=True,
    step_callback=enforce_rolling_window
)
