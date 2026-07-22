import os
from google import genai


def main(context):
    try:
        client = genai.Client(
            api_key=os.environ["GEMINI_API_KEY"]
        )

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents="Hello Gemini!"
        )

        return context.res.json({
            "success": True,
            "response": response.text
        })

    except Exception as e:
        return context.res.json({
            "success": False,
            "error": str(e)
        }, 500)
