import string
from pydantic import BaseModel

class User(BaseModel):
    id: int
    nome = ''
    telefone = ''
    email = ''
    logradouro = ''
    numero: int
    complemento = ''
    cep = ''
    cidade = ''
    estado = ''
    senha = ''

    

class Consumidor(User):
    cpf= ''

class Produtor(User):
    cnpj= ''