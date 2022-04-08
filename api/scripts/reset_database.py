import asyncio
import sqlalchemy
import json

from database import DATABASE_URL, metadata
from models.db_models import Usuario, Commodity, Oferta


async def config_db(database_url=DATABASE_URL):
    engine = sqlalchemy.create_engine(database_url)
    metadata.drop_all(engine)
    metadata.create_all(engine)
    await load_default_data()


async def load_default_data():
    with open('scripts/dados/commodities.json') as f:
        commodities = []
        dados = json.load(f)

        for item in dados:

            commodity = Commodity(id=item['id'], nome=item['nome'])
            # commodity.id = item['id']
            # commodity.nome = item['nome']

            commodities.append(commodity)

        await Commodity.objects.bulk_create(commodities)


if __name__ == '__main__':
    asyncio.run(config_db())
