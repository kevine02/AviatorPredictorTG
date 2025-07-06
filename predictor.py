# from scraper_real import scrape_last_multipliers  # Réel
from scraper import scrape_last_multipliers  # Simulation
import numpy as np
import joblib
from tensorflow.keras.models import load_model

def predict_next():
    data = scrape_last_multipliers()
    scaler = joblib.load("scaler.save")
    model = load_model("model.h5")
    scaled = scaler.transform(np.array(data[-5:]).reshape(-1, 1))
    X = np.array([scaled])
    pred = model.predict(X)[0][0]
    return data, pred > 0.5
