from datetime import date
from pydantic import BaseModel, StringConstraints, field_validator, ConfigDict
from typing_extensions import Annotated
from typing import List, Optional
from .unprocessableError import UnprocessableError

class Pessoa(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    apelido: Annotated[str, StringConstraints(max_length=32)]
    nome: Annotated[str, StringConstraints(max_length=100)]
    nascimento: date
    stack: Optional[List[Annotated[str, StringConstraints(max_length=32)]]] = None


    @field_validator('apelido','nome','nascimento', mode='before')
    def Unprocessable_entity(cls, arg) -> None:
        if arg is None:
            raise UnprocessableError()
        return arg


    # @field_validator('apelido, nascimento', mode='before')
    # def parse_date(cls, v):
    #     if isinstance(v, str):
    #         return date.fromisoformat(v)
    #     return v

