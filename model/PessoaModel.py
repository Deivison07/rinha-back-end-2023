import uuid
from sqlalchemy.dialects.postgresql import UUID, JSON
from app import db

class Pessoa(db.Model):
    __tablename__ = 'pessoa'
    id = db.Column(UUID(as_uuid=True))
    nome = db.Column(db.String(100))
    apelido =  db.Column(db.String(32))
    nascimento = db.Column(db.datetime.date())
    stack = db.Column(JSON())
