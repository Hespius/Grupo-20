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


@router.get("/commodities")
async def get_commodities():
    return await Commodity.objects.all()


@router.get("/ofertas")
async def get_ofertas(produtorId: int = None, commodityId: int = None, dataDisponibilidade = None, quantidade: float = None):

    ofertas = []

    if dataDisponibilidade != None:
        ofertas = await Oferta.objects.filter(data_disponivel__lte = dataDisponibilidade).all()
    else:
        ofertas = await Oferta.objects.all()

    if produtorId != None:
        ofertas = [oferta for oferta in ofertas if oferta.id_produtor.id == produtorId]

    if commodityId != None:
        ofertas = [oferta for oferta in ofertas if oferta.id_commodity.id == commodityId]

    if quantidade != None:
        ofertas = [oferta for oferta in ofertas if oferta.quantidade >= quantidade]


    return ofertas


@router.post("/criar-oferta")
async def add_oferta(oferta: Oferta):
    produtor = await Usuario.objects.get_or_none(id=oferta.id_produtor)

    if produtor == None:
        return Response(sucesso=False, mensagem='Produtor não encontrado')

    commodity = await Commodity.objects.get_or_none(id=oferta.id_commodity)

    if commodity == None:
        return Response(sucesso=False, mensagem='Commodity não encontrada')

    oferta.data_cadastro = datetime.now()

    await Oferta.save(oferta)

    return oferta