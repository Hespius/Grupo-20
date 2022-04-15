from re import S
from pydantic import BaseModel

from api.models.db_models import Usuario

class LoginForm(BaseModel):
    email: str
    senha: str


class Response():
    sucesso: bool
    mensagem: str

    def __init__(self, sucesso: bool, mensagem: str):
        self.sucesso = sucesso
        self.mensagem = mensagem


class ResponseLogin(Response):
    id_usuario: int
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

        self.id_usuario = usuario.id
        self.nome = usuario.nome
        self.email = usuario.email
        self.cidade = usuario.cidade
        self.estado = usuario.estado
        self.tipo = usuario.tipo

        if usuario.tipo == 'produtor':
            self.cnpj = usuario.cpf_cnpj
        else:
            self.cpf = usuario.cpf_cnpj
