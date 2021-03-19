
from fastapi import FastAPI
import joblib as joblib

app = FastAPI()

model = joblib.load('../model.pickle')

# define a root `/` endpoint
@app.get("/")
def index():
    return {"ok": True}

@app.get("/predict")
def predict(acousticness,
            danceability,
            duration_ms,
            energy,
            explicit,
            id,
            instrumentalness,
            key,
            liveness,
            loudness,
            mode,
            name,
            release_date,
            speechiness,
            tempo,
            valence,
            artis):
  return model.predict(acousticness,
            danceability,
            duration_ms,
            energy,
            explicit,
            id,
            instrumentalness,
            key,
            liveness,
            loudness,
            mode,
            name,
            release_date,
            speechiness,
            tempo,
            valence,
            artis)

# Implement a /predict endpoint
