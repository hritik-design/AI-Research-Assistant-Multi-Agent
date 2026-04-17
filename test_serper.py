from crewai_tools import SerperDevTool
from dotenv import load_dotenv

load_dotenv(r"c:\MINI_PROJECTS_SEM-2\ai-research-assistant-main\ai-research-assistant-main\.env")

tool = SerperDevTool(n_results=2)
try:
    res = tool.run(search_query="AI Models")
    print("Success. Length:", len(res))
    print(res)
except Exception as e:
    print("Error:", e)

tool2 = SerperDevTool(search_url="https://google.serper.dev/search", n=2)
try:
    res2 = tool2.run(search_query="AI Models")
    print("Success 2. Length:", len(res2))
except Exception as e:
    print("Error 2:", e)
