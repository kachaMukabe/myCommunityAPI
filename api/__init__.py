from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
CORS(app)
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "postgresql://xwacjxki:kretN0fBe_SPBkYTawYUxSim1hjuF1gV@flora.db.elephantsql.com/xwacjxki"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


@app.route("/")
def index():
    return "My first console"
