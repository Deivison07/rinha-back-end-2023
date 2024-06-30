from uuid import UUID
from flask import Flask, jsonify, request
from pydantic_core import ValidationError
from model.pessoa import Pessoa
from settings import createData, db
from sqlalchemy.exc import IntegrityError
from model.UnprocessableError import UnprocessableError

# from model.pessoa import Pessoa
from model.PessoaModel import PessoaM

app = Flask(__name__)   #instancia Flask app

createData(app)

@app.route("/pessoas",methods=['POST'])
def PostPessoas():
    try:
        row = PessoaM(**Pessoa(**request.json).model_dump())
        db.session.add(row)
        db.session.commit()
    except ValidationError:
        return {}, 400
    
    except (IntegrityError, UnprocessableError):
        return {},422

    response = jsonify()
    response.status_code = 201
    response.headers['Location'] = f'/pessoas/{row.id}'
    return response

@app.route("/pessoas/<uuid:id>",methods=['GET'])
def GetPessoas(id): ...


@app.route("/pessoas",methods=['GET'])
def GetPessoasTermo():
    search_term = request.args.get('t')
    

def contagemPessas(): ...


if __name__ == '__main__':
    app.run(debug=True)