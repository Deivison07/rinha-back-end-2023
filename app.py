from flask import Flask, jsonify, request
from pydantic_core import ValidationError
from model.pessoa import Pessoa
from settings import createData, db
from sqlalchemy.exc import IntegrityError
from model.UnprocessableError import UnprocessableError
from sqlalchemy.sql import text
 
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
        return {}, 422

    response = jsonify()
    response.status_code = 201
    response.headers['Location'] = f'/pessoas/{row.id}'
    return response

@app.route("/pessoas/<uuid:id>",methods=['GET'])
def GetPessoas(id):
    query = db.session.query(PessoaM).filter_by(id=id).first()
    return Pessoa.model_validate(query).model_dump()
    

@app.route("/pessoas",methods=['GET'])
def GetPessoasTermo():
    search_term = request.args.get('t')

    if search_term in [None, '']:
        return {'error': "query string obrigatória"}, 400

    query = text(f"SELECT * FROM pessoas WHERE BUSCA_TRGM LIKE :value limit 50")
    rows = db.session.execute(query, {'value': f"%{search_term}%"}).fetchall()
    if rows == []:
        return [], 200
    
    pessoas_model = [Pessoa.model_validate(row).model_dump() for row in rows]
    return pessoas_model


@app.route("/contagem-pessoas",methods=['GET'])
def contagemPessas():
    cont = db.session.query(PessoaM).count()
    return f'{cont}', 200



if __name__ == '__main__':
    app.run(debug=True)