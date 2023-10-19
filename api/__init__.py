from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager


app = Flask(__name__)
CORS(app)
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "postgresql://xwacjxki:kretN0fBe_SPBkYTawYUxSim1hjuF1gV@flora.db.elephantsql.com/xwacjxki"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["JWT_SECRET_KEY"] = "super-secret"
db = SQLAlchemy(app)
jwt = JWTManager(app)


@app.route("/")
def index():
    return "My first console"
