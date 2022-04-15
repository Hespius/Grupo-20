from datetime import datetime
from fastapi import APIRouter

from api.models.db_models import Commodity, Oferta, Usuario
from api.models.dto import Response

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

    if dataDisponibilidade is not None:
        ofertas = await Oferta.objects.select_all().filter(data_disponivel__lte=dataDisponibilidade).all()
    else:
        ofertas = await Oferta.objects.select_all().all()

    if produtorId is not None:
        ofertas = [oferta for oferta in ofertas if oferta.usuario.id == produtorId]

    if commodityId is not None:
        ofertas = [oferta for oferta in ofertas if oferta.commodity.id == commodityId]

    if quantidade is not None:
        ofertas = [oferta for oferta in ofertas if oferta.quantidade >= quantidade]

    return ofertas


@router.post("/criar-oferta")
async def add_oferta(produtorId: int, commodityId: int, oferta: Oferta):
    produtor = await Usuario.objects.get_or_none(id=produtorId)

    if produtor == None:
        return Response(sucesso=False, mensagem='Produtor não encontrado')

    commodity = await Commodity.objects.get_or_none(id=commodityId)

    if commodity == None:
        return Response(sucesso=False, mensagem='Commodity não encontrada')

    oferta.data_cadastro = datetime.now()

    await produtor.commodity.add(commodity, data_cadastro=oferta.data_cadastro,
                                 data_disponivel=oferta.data_disponivel, quantidade=oferta.quantidade,
                                 preco=oferta.preco)

    return oferta