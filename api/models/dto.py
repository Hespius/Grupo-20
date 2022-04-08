from pydantic import BaseModel
from .db_models import Usuario


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
