def main(context):
    return context.res.json(
        {
            "success": True,
            "response": "Hello from Appwrite!"
        },
        200,
        {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET,POST,OPTIONS",
            "Access-Control-Allow-Headers": "*"
        }
    )
