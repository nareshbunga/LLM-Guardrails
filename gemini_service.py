from google import genai
from config import(
    GEMINI_API_KEY,
    GEMINI_MODEL
)


Client = genai.Client(
    api_key=GEMINI_API_KEY
)

def generate_response(prompt:str) -> str:
    response = Client.models.generate_content(
        model=GEMINI_MODEL,
        contents=prompt
    )
    return response.text or ""

print(generate_response("Happy Gemini?"))

