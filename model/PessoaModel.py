import uuid
from sqlalchemy.dialects.postgresql import UUID, JSON
from sqlalchemy import DateTime

from settings import db

class PessoaM(db.Model):
    __tablename__ = 'pessoas'
    __table_args__ = {"schema": "public"}
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nome = db.Column(db.String(100))
    apelido =  db.Column(db.String(32))
    nascimento = db.Column(DateTime())
    stack = db.Column(JSON())