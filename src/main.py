import os
from google import genai

def main(context):
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        return context.res.json({"error": "GEMINI_API_KEY not found"}, 500)

    try:
        client = genai.Client(api_key=api_key)

        response = client.models.generate_content(
            model="model=gemini-3.6-flash",
            contents="Say only: Hello Yash"
        )

        return context.res.json({
            "text": response.text
        })

    except Exception as e:
        context.error(str(e))  # Log Appwrite me jayega
        return context.res.json({
            "error": str(e)
        }, 500)
