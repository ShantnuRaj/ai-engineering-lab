import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(
    api_key=api_key,
    http_options=types.HttpOptions(
        timeout=30000
    )
)

try:
    print("Sending request...")

    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents="Reply with only HELLO"
    )

    print("Gemini:", response.text)

except Exception as e:
    print("Error:", repr(e))

finally:
    client.close()