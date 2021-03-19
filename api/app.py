
from fastapi import FastAPI
import joblib as joblib

app = FastAPI()

model = joblib.load('model.joblib')

# define a root `/` endpoint
@app.get("/")
def index():
    return {"ok": True}

@app.get("/predict")
def predict(params):
  return params

# Implement a /predict endpoint
