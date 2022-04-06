import ormar

from database import database, metadata
from pydantic import BaseModel


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
    complemento: str = ormar.String(max_length=200, nullable=True)
    cep: str = ormar.String(max_length=20)
    cidade: str = ormar.String(max_length=200)
    estado: str = ormar.String(max_length=30)
    cpf_cnpj: str = ormar.String(max_length=30)
    tipo: str = ormar.String(max_length=20)
    senha: str = ormar.String(max_length=50)

    def __str__(self):
        return 'nome: ' + self.nome + '\nemail: ' + self.email


class LoginForm(BaseModel):
    email: str
    senha: str


class Response():
    sucesso: bool
    mensagem: str


class ResponseLogin(Response):
    nome: str
    email: str
    cidade: str
    estado: str
    cpf: str
    cnpj: str
    tipo: str

    def __init__(self, usuario: Usuario):

        self.sucesso = True
        self.mensagem = ''

        self.nome = usuario.nome
        self.email = usuario.email
        self.cidade = usuario.cidade
        self.estado = usuario.estado
        self.tipo = usuario.tipo

        if usuario.tipo == 'produtor':
            self.cnpj = usuario.cpf_cnpj
        else:
            self.cpf = usuario.cpf_cnpj
