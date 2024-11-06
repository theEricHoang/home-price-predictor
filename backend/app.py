from flask import Flask
from flask_cors import CORS
from api.predict import predict_blueprint

app = Flask(__name__)
app.register_blueprint(predict_blueprint)
CORS(app)

if __name__ == '__main__':
    app.run(debug=True)