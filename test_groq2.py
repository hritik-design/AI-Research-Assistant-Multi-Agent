import os
import requests
from dotenv import load_dotenv

load_dotenv(r"c:\MINI_PROJECTS_SEM-2\ai-research-assistant-main\ai-research-assistant-main\.env")

url = "https://api.groq.com/openai/v1/models"
headers = {
    "Authorization": f"Bearer {os.environ.get('GROQ_API_KEY')}"
}
response = requests.get(url, headers=headers)
print("Models:", [m['id'] for m in response.json().get('data', [])])
