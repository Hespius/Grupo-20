import ormar

from api.database import database, metadata


class Produto(ormar.Model):
    class Meta:
        metadata = metadata
        database = database
        tablename = 'Produtos'

    id: int = ormar.Integer(primary_key=True)
    commodity: str = ormar.String(max_length=200)
    data_disponivel: str = ormar.DateTime(timezone= False)
    quantidade: int = ormar.Integer()
    preco: float = ormar.Float()