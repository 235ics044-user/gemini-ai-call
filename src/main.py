import os
import json
from google import genai

MODELS = [
    "gemini-3.6-flash",
    "gemini-flash-latest",
    "gemini-3.5-flash-lite",
    "gemini-3.1-flash-lite",
    "gemini-flash-lite-latest"
]

CORS_HEADERS = {
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
    "Access-Control-Allow-Headers": "*"
}


def main(context):

    if context.req.method == "OPTIONS":
      return context.res.json({})
    
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        return context.res.json(
            {
                "success": False,
                "error": "GEMINI_API_KEY not found"
            },
            500,
            CORS_HEADERS
        )

    client = genai.Client(api_key=api_key)

    # GET request support
    if context.req.method == "GET":

        prompt = context.req.query.get("prompt", "Hello Gemini!")

        history = [
            {
                "role": "user",
                "text": prompt
            }
        ]

    else:

        body = json.loads(context.req.body)

        history = body.get("history", [])

    last_error = None

    for model in MODELS:

        try:

            chat = client.chats.create(model=model)

            reply = None

            for msg in history:

                if msg["role"] == "user":
                    reply = chat.send_message(msg["text"])

            return context.res.json(
                {
                    "success": True,
                    "response": reply.text,
                    "model": model
                },
                200,
                CORS_HEADERS
            )

        except Exception as e:

            last_error = str(e)

    return context.res.json(
        {
            "success": False,
            "error": last_error
        },
        500,
        CORS_HEADERS
    )
