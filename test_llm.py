import os
from crewai.llm import LLM
from dotenv import load_dotenv

load_dotenv(r"c:\MINI_PROJECTS_SEM-2\ai-research-assistant-main\ai-research-assistant-main\.env")

llm = LLM(
    model="groq/llama-3.1-8b-instant",
    max_tokens=50,
)

print(dir(llm))
