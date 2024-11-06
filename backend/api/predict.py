from flask import Blueprint, request, jsonify
from model.model_utils import load_model, make_prediction
import numpy as np

predict_blueprint = Blueprint('predict', __name__)
model = load_model()

@predict_blueprint.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    features = np.array([data['zipCode'], data['beds'], data['baths'], data['sqft'], data['latitude'], data['longitude']]).reshape(1, -1)
    prediction = make_prediction(features, model)
    return jsonify({'predictedPrice': prediction[0]})