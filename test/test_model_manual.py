import json
from model.pessoa import Pessoa


v1 = {
    "apelido" : "josé",
    "nome" : "José Roberto",
    "nascimento" : "2000-10-01",
    "stack" : ["C#", "Node", 1]
}

v2 = '{"apelido" : "ana","nome" : "Ana Barbosa","nascimento" : "1985-09-23"}'

user_dict = json.loads(v2)



p1 = Pessoa(**v1)
p2 = Pessoa(**user_dict)