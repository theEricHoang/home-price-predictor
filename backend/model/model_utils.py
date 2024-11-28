import joblib
import pandas as pd

def load_model():
    return joblib.load('backend/model/model3.joblib')

def make_prediction(data, model):
    prediction = model.predict(data)
    return prediction.tolist()