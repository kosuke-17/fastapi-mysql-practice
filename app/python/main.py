from enum import Enum
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/helloworld")
async def say_hallo():
    return {"message": "Hello World"}


@app.get("/api/{message}")
async def get_message(message: str):
    return {"message": message}


class SexType(str, Enum):
    Male = "男"
    Female = "女"


class SchemaofTitanicFeaturesRequest(BaseModel):
    Sex: SexType
    Pclass: str
    Age: int
    Parch: int
    SibSp: int


@app.post("/api/titanic", response_model=SchemaofTitanicFeaturesRequest)
def derive_score(body: SchemaofTitanicFeaturesRequest):
    return body
