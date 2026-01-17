from datetime import timedelta
from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flasgger import Swagger
from .log import logger
from .shared.global_variables import USERNAME, PASSWORD, HOST, DB_NAME
from .shared.response import give_response
from .shared import http_status_code as status
from .models import db
from .urls import urls

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = (
    f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}/{DB_NAME}"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["JWT_SECRET_KEY"] = "secret"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=7)

api = Api(app)
CORS(app)
jwt = JWTManager(app)
db.init_app(app)
Swagger(app)
urls(api)


@app.errorhandler(404)
def url_not_found(e):
    """return appropriate response if url not found"""
    code = status.HTTP_404_NOT_FOUND
    logger.error(f"The requested url was not found on the server: {e}")
    return (
        give_response(
            message="The requested url was not found on the server",
            code=code,
            success=False,
        ),
        code,
    )
