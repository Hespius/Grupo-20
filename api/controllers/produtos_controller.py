from datetime import datetime
from fastapi import APIRouter

from models.db_models import Commodity, Oferta, Usuario
from models.dto import Response

router = APIRouter()

# TODO: permitir null vindo do json ao invés de vazio


@router.post("/cadastrar")
async def add_commoditty(item: Commodity):

    await item.save()
    return item


@router.get("/")
async def get_commodities():
    return await Commodity.objects.all()


@router.post("/criar-oferta")
async def add_oferta(id_produtor: int, id_commodity: int, oferta: Oferta):
    produtor = await Usuario.objects.get_or_none(id=id_produtor)

    oferta.data_cadastro = datetime.now()

    if produtor == None:
        return Response(sucesso=False, mensagem='Produtor não encontrado')

    commodity = await Commodity.objects.get_or_none(id=id_commodity)

    if commodity == None:
        return Response(sucesso=False, mensagem='Commodity não encontrada')

    oferta.id_commodity = id_commodity
    oferta.id_produtor = id_produtor

    await Oferta.save(oferta)

    return oferta