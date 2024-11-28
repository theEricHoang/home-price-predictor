from flask import Blueprint, request, jsonify
from model.model_utils import load_model, make_prediction
from model.preprocessing import preprocess_data

predict_blueprint = Blueprint('predict-house-price', __name__)
model = load_model()

@predict_blueprint.route('/api/predict-house-price', methods=['POST'])
def predict():
    data = request.get_json()
    features = preprocess_data(data)

    if features.empty:
        return jsonify({'error': 'Invalid data or unable to fetch coordinates'}), 400

    prediction = make_prediction(features, model)
    return jsonify({'predictedPrice': int(prediction[0]*100)/100})