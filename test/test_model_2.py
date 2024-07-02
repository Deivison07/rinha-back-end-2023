import unittest
from model.pessoaValidation import Pessoa
from pydantic_core import ValidationError

class MainTest2(unittest.TestCase):
    def setUp(self):...
        #preencher com dados ou instancias que serão usadas para cada teste individualmente
        # print(' --> Novo teste -->')
    
    def test_model_Pessoa_stack_com_mais_de_32_caracteres(self):
        
        v1 = {
            "apelido" : "josé",
            "nome" : "José Roberto",
            "nascimento" : "2000-10-01",
            "stack" : ["C#", "Node", f"a"*33]
        }
        self.assertRaises(ValidationError, Pessoa, **v1)

    def tearDown(self):...
        # print('<-- terminando teste <--')
        
if __name__ == '__main__':
    unittest.main()