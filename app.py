from flask import Flask, jsonify, request
from uuid import UUID

app = Flask(__name__)   #instancia Flask app


@app.route("/pessoas",methods=['POST'])
def PostPessoas(): ...



@app.route("/pessoas/<uuid:id>",methods=['GET'])
def GetPessoas(id): ...


@app.route("/pessoas",methods=['GET'])
def GetPessoasTermo():
    search_term = request.args.get('t')
    

def contagemPessas(): ...


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)