from email.policy import default
import ormar

from database import database, metadata

class Usuario(ormar.Model):
    class Meta:
        metadata = metadata
        database = database
        tablename = 'Usuarios'

    id: int = ormar.Integer(primary_key=True)
    nome: str = ormar.String(max_length=200)
    telefone: str = ormar.String(max_length=20)
    email: str = ormar.String(max_length=200)
    logradouro: str = ormar.String(max_length=200)
    numero: int = ormar.Integer()
    complemento: str = ormar.String(max_length=200)
    cep: str = ormar.String(max_length=20)
    cidade: str = ormar.String(max_length=200)
    estado: str = ormar.String(max_length=30)
    cpf: str = ormar.String(max_length=30)
    cnpj: str = ormar.String(max_length=30)
    produtor: bool = ormar.Boolean(default=False)
    senha: str = ormar.String(max_length=50)

# class User(BaseModel):
#     id: int
#     nome = Column(String)
#     telefone = Column(String)
#     email = Column(String)
#     logradouro = Column(String)
#     numero: int
#     complemento = Column(String)
#     cep = Column(String)
#     cidade = Column(String)
#     estado = Column(String)
#     senha = Column(String) 

# class Consumidor(User):
#     cpf= ''

# class Produtor(User):
#     cnpj= ''

# class LoginForm():
#     email = Column(String)
#     senha = Column(String)