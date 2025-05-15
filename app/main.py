from fastapi import FastAPI
from app.schema import Person
from app.config import settings
import joblib
import numpy as np

app = FastAPI()

scaler, model = joblib.load(settings.MODEL_PATH)

@app.post("/predict")
def predict(data: Person):
    features = np.array([[data.height, data.weight]])
    scaled = scaler.transform(features)
    prediction = model.predict(scaled)[0]
    return {"obese": bool(prediction)}
