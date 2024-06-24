from datetime import date
from pydantic import BaseModel, StringConstraints, field_validator
from typing_extensions import Annotated
from typing import List, Optional

class Pessoa(BaseModel):
    apelido: Annotated[str, StringConstraints(max_length=32)]
    nome: Annotated[str, StringConstraints(max_length=100)]
    nascimento: date
    stack: Optional[List[Annotated[str, StringConstraints(max_length=32)]]] = None

    @field_validator('nascimento', mode='before')
    def parse_date(cls, v):
        if isinstance(v, str):
            return date.fromisoformat(v)
        return v

