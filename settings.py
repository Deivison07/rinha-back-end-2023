import os
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
load_dotenv()

pool_size = int(os.getenv("POOL_SIZE"))
database_host = os.getenv("DATABASE_IP")
database_pass = os.getenv("DATABASE_PASS")
database_port = os.getenv("DATABASE_PORT")
database_name = os.getenv("DATABASE_NAME")
database_user = os.getenv("DATABASE_USER")
DATABASE_CONNECTION_URL = f"postgresql://{database_user}:{database_pass}@{database_host}:{database_port}/{database_name}"

db = SQLAlchemy()

def createData(app:Flask):
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_CONNECTION_URL
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
        'pool_size': pool_size,
    }   

    db.init_app(app)

