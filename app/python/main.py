from fastapi import FastAPI

app = FastAPI()


@app.get("/helloworld")
async def say_hallo():
    return {"message": "Hello World"}


@app.get("/api/{message}")
async def get_message(message: str):
    return {"message": message}
