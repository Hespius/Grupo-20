from pydantic import BaseModel

from api.models.db_models import Oferta, Usuario


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


class OfertaDto ():

    def __init__(self, oferta: Oferta):
        self.id = oferta.id
        self.data_disponivel = oferta.data_disponivel
        self.quantidade = oferta.quantidade
        self.preco = oferta.preco
        self.commodity = oferta.commodity.nome
        self.usuario = oferta.usuario.nome
        self.saldo = oferta.saldo

    id: int
    data_disponivel: str
    quantidade: float
    saldo: float
    preco: float
    commodity: str
    usuario: str


class OfertaDto2 (BaseModel):

    data_disponivel: str
    quantidade: float
    saldo: float
    preco: float
    commodity: str
    usuario: int
