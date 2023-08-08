from enum import Enum
from fastapi import FastAPI
from pydantic import BaseModel
from machine_learning.titanic import PredictOnAPI

app = FastAPI()


@app.get("/helloworld")
async def say_hallo():
    return {"message": "Hello World"}


@app.get("/api/{message}")
async def get_message(message: str):
    return {"message": message}


class SexType(str, Enum):
    Male = "男性"
    Female = "女性"


class SchemaofTitanicFeaturesRequest(BaseModel):
    Sex: SexType
    Pclass: str
    Age: int
    Parch: int
    SibSp: int


class SchemaOfSurvivalProbabilityResponse(BaseModel):
    survival_probability: str


@app.post("/api/titanic", response_model=SchemaOfSurvivalProbabilityResponse)
def derive_score(request_body: SchemaofTitanicFeaturesRequest):
    # 辞書形式に変更
    features_dict = request_body.__dict__
    # **<辞書オブジェクト>とすることで引数として自動的にバラして与えることが可能
    survival_probability = PredictOnAPI.derive_survival_probability(**features_dict)
    return {"survival_probability": str(survival_probability * 100) + "%"}
