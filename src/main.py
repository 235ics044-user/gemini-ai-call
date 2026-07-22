import os
from google import genai

def main(context):
    api_key = os.getenv("GEMINI_API_KEY")

    client = genai.Client(api_key=api_key)

    # URL se prompt lo
    prompt = context.req.query.get("prompt", "Hello Gemini!")

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    return context.res.json({
        "prompt": prompt,
        "response": response.text
    })
