import asyncio
import sqlalchemy
import json
from datetime import datetime

from api.database import DATABASE_URL, metadata
from api.models.db_models import Usuario, Commodity


async def config_db(database_url=DATABASE_URL):
    engine = sqlalchemy.create_engine(database_url)
    metadata.drop_all(engine)
    metadata.create_all(engine)
    await load_default_data()


async def load_default_data():
    await load_default_commodities()
    await load_default_users()
    await load_default_ofertas()


async def load_default_commodities():
    with open('scripts/dados/commodities.json') as f:
        commodities = []
        dados = json.load(f)

        for item in dados:

            commodity = Commodity(nome=item['nome'])

            commodities.append(commodity)

        await Commodity.objects.bulk_create(commodities)

    print('Adicionado commodities')


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

        await Usuario.objects.bulk_create(usuarios)

    print('Adicionado usuários')


def get_unique_ids(arr, propertyName):
    uniques = []

    for item in arr:
        if item[propertyName] not in uniques:
            uniques.append(item[propertyName])

    return uniques


async def load_default_ofertas():
    with open('scripts/dados/ofertas.json') as f:
        dados = json.load(f)
        ids_produtores = get_unique_ids(dados, 'produtorId')
        commodities = await Commodity.objects.all()
        data_cadastro = datetime.now()
        for id in ids_produtores:
            produtor = await Usuario.objects.get_or_none(id=id)

            # print('======= OFERTAS DO PRODUTOR {} ======='.format(id))
            for item in dados:
                if item['produtorId'] == id:
                    commodity = [
                        x for x in commodities if x.id == item['commodityId']][0]

                    await produtor.commodity.add(commodity, data_cadastro=data_cadastro,
                                                 data_disponivel=item['data_disponivel'],
                                                 quantidade=item['quantidade'],
                                                 saldo=item['quantidade'],
                                                 preco=item['preco'])
                    print(
                        "Adicionou a oferta de {} Kgs de {} pelo o produtor {} ao preço de {}".format(item['quantidade'], commodity.nome, produtor.nome, item['preco']))

if __name__ == '__main__':
    asyncio.run(config_db())
