from flask import Flask
from dotenv import load_dotenv
from flask_cors import CORS
from src.models import raffle_database
from src.routes.raffle_router import raffle_router


load_dotenv()

app = Flask(__name__)
raffle_database.init_app(app)

CORS(app)

app.register_blueprint(raffle_router)

# @app.route('/')
# def hello_world():
#     return 'Hello World!'


if __name__ == '__main__':
    app.run()
