from dotenv import load_dotenv
import os
from google import genai


def get_credences(eth):
    load_dotenv()
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

    response = client.models.generate_content(
        model="gemini-2.0-flash", contents="Explain how AI works in a few words"
    )
    print(eth)
    print(response.text)

    return response.text

get_credences("testing")