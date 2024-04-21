from fastapi import FastAPI

async def on_fetch(request, env):
    import asgi

    return await asgi.fetch(app, request, env)


app = FastAPI()

@app.post("/send_message/")
async def send_message(message: str):
    return {"message": message}
