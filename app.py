from uuid import UUID
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from model.pessoa import Pessoa
from settings import DATABASE_CONNECTION_URL

db = SQLAlchemy()

app = Flask(__name__)   #instancia Flask app
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_CONNECTION_URL
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


@app.route("/pessoas",methods=['POST'])
def PostPessoas():
    row = Pessoa(**request.json)
    return {}

@app.route("/pessoas/<uuid:id>",methods=['GET'])
def GetPessoas(id): ...


@app.route("/pessoas",methods=['GET'])
def GetPessoasTermo():
    search_term = request.args.get('t')
    

def contagemPessas(): ...


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)