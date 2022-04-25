from curses import meta
import ormar
from typing import Optional

from api.database import database, metadata


class Commodity(ormar.Model):
    class Meta:
        metadata = metadata
        database = database
        tablename = 'Commodities'

    id: int = ormar.Integer(primary_key=True)
    nome: str = ormar.String(max_length=100)


class Oferta(ormar.Model):
    class Meta:
        metadata = metadata
        database = database
        tablename = 'Ofertas'

    id: int = ormar.Integer(primary_key=True)
    data_cadastro: str = ormar.DateTime(nullable=True)
    data_disponivel: str = ormar.DateTime()
    quantidade: float = ormar.Float()
    saldo: float = ormar.Float()
    preco: float = ormar.Float()


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

    commodity = ormar.ManyToMany(Commodity, through=Oferta)

    def __str__(self):
        return 'nome: ' + self.nome + '\nemail: ' + self.email


class Ordem(ormar.Model):
    class Meta:
        metadata = metadata
        database = database
        tablename = 'Ordens'

    id: int = ormar.Integer(primary_key=True)
    quantidade: float = ormar.Float()
    data_requisitada: str = ormar.DateTime()

    oferta: Optional[Oferta] = ormar.ForeignKey(Oferta)
    comprador: Optional[Usuario] = ormar.ForeignKey(Usuario)
