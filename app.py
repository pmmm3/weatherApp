from flask import Flask
from api.routes.city import city
from api.routes.main import main


def create_app():
    app = Flask(__name__)
    app.register_blueprint(main)
    app.register_blueprint(city)
    return app


if __name__ == '__main__':
    weather_app = create_app()
    weather_app.run(debug=True)
