import os
import time
from crewai import Agent, LLM
from crewai_tools import FileWriterTool

def enforce_rolling_window(*args, **kwargs):
    time.sleep(40)

# LLM configurations - Agent specific config
model = os.getenv("WRITER_AGENT_LLM", "groq/llama-3.3-70b-versatile")
temperature = float(os.getenv("WRITER_AGENT_TEMPERATURE", "0.3"))

llm = LLM(
    model=model,
    temperature=temperature,
    max_tokens=8000
)

content_writer_agent = Agent(
    role="Content Writer",
    goal="Create comprehensive, well-structured reports and summaries",
    backstory = (
                "You are a professional content writer with expertise in creating "
                "clear, engaging, and well-structured documents. You can transform complex "
                "information into accessible and compelling content."
            ),
    llm=llm,
    tools=[FileWriterTool()],
    verbose=True,
    step_callback=enforce_rolling_window
)
