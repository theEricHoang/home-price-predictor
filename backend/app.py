from flask import Flask
from flask_cors import CORS
from api.predict import predict_blueprint
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)

limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=['10 per hour'],
)

app.register_blueprint(predict_blueprint)
CORS(app)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)