import os
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
load_dotenv()

database_host = os.getenv("DATABASE_IP")
database_pass = os.getenv("DATABASE_PASS")
database_port = os.getenv("DATABASE_PORT")
database_name = os.getenv("DATABASE_NAME")
database_user = os.getenv("DATABASE_USER")
DATABASE_CONNECTION_URL = f"postgresql://{database_user}:{database_pass}@{database_host}:{database_port}/{database_name}"

print(DATABASE_CONNECTION_URL)
db = SQLAlchemy()

def createData(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_CONNECTION_URL
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

