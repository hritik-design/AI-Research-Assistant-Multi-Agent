import os
from litellm import completion
from dotenv import load_dotenv

load_dotenv(r"c:\MINI_PROJECTS_SEM-2\ai-research-assistant-main\ai-research-assistant-main\.env")

try:
    response = completion(
        model="groq/gemma2-9b-it",
        messages=[{"role": "user", "content": "Hello, how are you?"}]
    )
    print("Success Gemma:", response.choices[0].message.content)
except Exception as e:
    print("Error Gemma:", e)

try:
    response = completion(
        model="groq/mixtral-8x7b-32768",
        messages=[{"role": "user", "content": "Hello, how are you?"}]
    )
    print("Success Mixtral:", response.choices[0].message.content)
except Exception as e:
    print("Error Mixtral:", e)
