import os
from google import genai

MODELS = [
    "gemini-3.6-flash",
    "gemini-flash-latest",
    "gemini-3.5-flash-lite",
    "gemini-3.1-flash-lite",
    "gemini-flash-lite-latest"
]

def main(context):
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        return context.res.json({
            "success": False,
            "error": "GEMINI_API_KEY not found"
        }, 500)

    client = genai.Client(api_key=api_key)

    prompt = context.req.query.get("prompt", "Hello Gemini!")

    last_error = None

    for model in MODELS:
        try:
            response = client.models.generate_content(
                model=model,
                contents=prompt
            )

            return context.res.json({
                "success": True,
                "model": model,
                "prompt": prompt,
                "response": response.text
            })

        except Exception as e:
            last_error = str(e)

    return context.res.json({
        "success": False,
        "error": "All models failed",
        "details": last_error
    }, 500)
