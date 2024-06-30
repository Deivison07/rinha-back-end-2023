import unittest
from model.pessoa import Pessoa
from pydantic_core import ValidationError
from model.UnprocessableError import UnprocessableError
class MainTest(unittest.TestCase):
    def setUp(self):...
        #preencher com dados ou instancias que serão usadas para cada teste individualmente
        # print(' --> Novo teste -->')
    
    def test_model_Pessoa_apelido_null(self):
       v1 = {
            "apelido" : None,
            "nome" : "Ana Barbosa",
            "nascimento" : "1985-01-23",
            "stack" : None
        }
       self.assertRaises(UnprocessableError, Pessoa, **v1)

    def test_model_Pessoa_stack_com_inteiro(self):
        
        v1 = {
            "apelido" : "josé",
            "nome" : "José Roberto",
            "nascimento" : "2000-10-01",
            "stack" : ["C#", "Node", 2]
        }
        self.assertRaises(ValidationError, Pessoa, **v1)

    def test_model_Pessoa_apelido_com_inteiro(self):
        
        v1 = {
            "apelido" : 2,
            "nome" : "José Roberto",
            "nascimento" : "2000-10-01",
            "stack" : ["C#", "Node", "python"]
        }
        self.assertRaises(ValidationError, Pessoa, **v1)
    
    def test_model_Pessoa_sem_nome(self):
        
        v1 = {
            "apelido" : 2,
            # "nome" : "José Roberto",
            "nascimento" : "2000-10-01",
            "stack" : ["C#", "Node", "python"]
        }
        self.assertRaises(ValidationError, Pessoa, **v1)
    def tearDown(self):...
        # print('<-- terminando teste <--')
        
if __name__ == '__main__':
    unittest.main()