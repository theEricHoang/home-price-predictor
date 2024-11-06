from app import create_app
from app.routes import init_routes

app = create_app()
init_routes(app)

if __name__ == '__main__':
    app.run(debug=True)