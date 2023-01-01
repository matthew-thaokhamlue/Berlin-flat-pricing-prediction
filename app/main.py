from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import pickle
from pathlib import Path


app = FastAPI()


class FeatureItem(BaseModel):
    postcode_id: str
    builtin_kitchen: bool
    living_space: float


@app.get("/")
async def root():
    return {"message": "Hello World"}


BASE_DIR = Path(__file__).resolve(strict=True).parent


with open(f"{BASE_DIR}/trained_model.pkl", "rb") as f:
    model = pickle.load(f)


@app.post("/predict")
async def predict(item: FeatureItem):
    df = pd.DataFrame([item.dict().values()], columns=item.dict().keys())
    y_pred = model.predict(df)
    return {"flat_price_predicted_in_EUR": int(y_pred)}
