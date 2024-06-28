from uuid import UUID
from flask import Flask, jsonify, request
from pydantic_core import ValidationError
from model.pessoa import Pessoa
from settings import createData, db
from sqlalchemy.exc import IntegrityError

# from model.pessoa import Pessoa
from model.PessoaModel import PessoaM

app = Flask(__name__)   #instancia Flask app

createData(app)

@app.route("/pessoas",methods=['POST'])
def PostPessoas():
    try:
        new_user = Pessoa(**request.json)
        db.session.add(PessoaM(**new_user.model_dump()))
        db.session.commit()
    except ValidationError as e:
        return {
            'error': str(e)
        }, 400
    except IntegrityError as e:
        return {
            'error': str(e)
        },402

    return '', 201

@app.route("/pessoas/<uuid:id>",methods=['GET'])
def GetPessoas(id): ...


@app.route("/pessoas",methods=['GET'])
def GetPessoasTermo():
    search_term = request.args.get('t')
    

def contagemPessas(): ...


if __name__ == '__main__':
    app.run(debug=True)