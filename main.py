from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import pickle

app = FastAPI()


class FeatureItem(BaseModel):
    postcode_id: str
    builtin_kitchen: bool
    living_space: float


model = pickle.load(open('model.pickle', 'rb'))


@app.post("/predict")
async def pred(item: FeatureItem):
    df = pd.DataFrame([item.dict().values()], columns=item.dict().keys())
    y_pred = model.predict(df)
    return {"flat_price_predicted_in_EUR": int(y_pred)}
