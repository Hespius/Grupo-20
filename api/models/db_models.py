from dataclasses import dataclass
import ormar
from api.database import database, metadata


class Commodity(ormar.Model):
    class Meta:
        metadata = metadata
        database = database 
        tablename = 'Commodities'

    id: int = ormar.Integer(primary_key=True)
    nome: str = ormar.String(max_length=100)

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

    commodity = ormar.ManyToMany(Commodity,
                                 through_relation_name='id_produtor',
                                 through_reverse_relation_name='id_commodity')

    def __str__(self):
        return 'nome: ' + self.nome + '\nemail: ' + self.email


class Oferta(ormar.Model):
    class Meta:
        metadata = metadata
        database = database
        tablename = 'Ofertas'

    id: int = ormar.Integer(primary_key=True)
    data_cadastro: str = ormar.DateTime(nullable=True)
    data_disponivel: str = ormar.DateTime()
    quantidade: float = ormar.Float()
    preco: float = ormar.Float()

    id_commodity: int = ormar.ForeignKey(Commodity)
    id_produtor: int = ormar.ForeignKey(Usuario)


