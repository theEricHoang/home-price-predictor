import joblib

def load_model():
    return joblib.load('model/model.pkl')

def make_prediction(data, model):
    prediction = model.predict(data)
    return prediction.tolist()