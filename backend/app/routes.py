#api endpoints
from flask import jsonify

def init_routes(app):
    @app.route('/api', methods=['GET'])
    def home():
        return jsonify({'message': 'YELLO'})