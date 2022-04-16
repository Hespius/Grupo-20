import asyncio
import sqlalchemy
import json
import sys

sys.path.insert(0, '/home/Storage/Documents/UFABC/' +
                'engenharia-software/Grupo-20/api')

from database import DATABASE_URL, metadata
from models.db_models import Usuario, Commodity, Oferta


async def config_db(database_url=DATABASE_URL):
    engine = sqlalchemy.create_engine(database_url)
    metadata.drop_all(engine)
    metadata.create_all(engine)
    await load_default_data()


async def load_default_data():
    await load_default_commodities()
    # await load_default_users()


async def load_default_commodities():
        with open('scripts/dados/commodities.json') as f:
            commodities = []
            dados = json.load(f)

            for item in dados:

                commodity = Commodity(nome=item['nome'])

                commodities.append(commodity)

            await Commodity.objects.bulk_create(commodities)


async def load_default_users():
        with open('scripts/dados/usuarios.json') as f:
            usuarios = []
            dados = json.load(f)

            for item in dados:

                usuario = Usuario(id=item['id'],
                                  nome=item['nome'],
                                  cep=item['cep'],
                                  cidade=item['cidade'],
                                  cpf_cnpj=item['cpf_cnpj'],
                                  email=item['email'],
                                  estado=item['estado'],
                                  logradouro=item['logradouro'],
                                  numero=item['numero'],
                                  senha=item['senha'],
                                  telefone=item['telefone'],
                                  tipo=item['tipo'])

                usuarios.append(usuario)

            await Commodity.objects.bulk_create(usuarios)

if __name__ == '__main__':
    asyncio.run(config_db())
