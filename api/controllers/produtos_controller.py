from datetime import datetime
from fastapi import APIRouter

from api.models.db_models import Commodity, Oferta, Usuario, Ordem
from api.models.dto import OfertaDto, Response, OfertaDto2

router = APIRouter()

# TODO: permitir null vindo do json ao invés de vazio


@router.post("/cadastrar")
async def add_commoditty(item: Commodity):

    await item.save()
    return item


@router.get("/commodities")
async def get_commodities():
    commodities = await Commodity.objects.all()

    commoditiesDTO = [{"commodity": item.nome} for item in commodities]

    return commoditiesDTO


@router.get("/ofertas")
async def get_ofertas(produtorId: int = None, commodityName: str = None,
                      dataDisponibilidade=None, quantidade: float = None):

    ofertas = []
    ofertasDto = []

    if dataDisponibilidade is not None:
        ofertas = await Oferta.objects.select_all().filter(
            data_disponivel__lte=dataDisponibilidade).all()
    else:
        ofertas = await Oferta.objects.select_all().all()

    if produtorId is not None:
        ofertas = [oferta for oferta in ofertas if
                   oferta.usuario.id == produtorId]

    if commodityName is not None:
        ofertas = [oferta for oferta in ofertas if
                   oferta.commodity.nome == commodityName]

    if quantidade is not None:
        ofertas = [oferta for oferta in ofertas if
                   oferta.quantidade >= quantidade]

    ofertasDto = [OfertaDto(oferta) for oferta in ofertas]

    return ofertasDto


@router.post("/criar-oferta")
async def add_oferta(oferta: OfertaDto2):
    produtor = await Usuario.objects.get_or_none(id=oferta.usuario)

    if produtor is None:
        return Response(sucesso=False, mensagem='Produtor não encontrado')

    commodity = await Commodity.objects.get_or_none(nome=oferta.commodity)

    if commodity is None:
        return Response(sucesso=False, mensagem='Commodity não encontrada')

    data_cadastro = datetime.now()
    oferta.saldo = oferta.quantidade

    await produtor.commodity.add(commodity, data_cadastro=data_cadastro,
                                 data_disponivel=oferta.data_disponivel,
                                 quantidade=oferta.quantidade,
                                 preco=oferta.preco,
                                 saldo=oferta.saldo)

    return oferta


@router.post('/ordem')
async def add_ordem(ordem: Ordem):

    ofertaDB = await Oferta.objects.get_or_none(id=ordem.oferta)

    if ofertaDB is None:
        return Response(sucesso=False, mensagem='Oferta não existe')

    if ordem.quantidade > ofertaDB.saldo:
        return Response(sucesso=False,
                        mensagem='Quantidade requirida maior que o estoque')

    await ofertaDB.update(saldo=ofertaDB.saldo - ordem.quantidade)

    ordemDB = await Ordem.save(ordem)

    return ordemDB


@router.get('/ordem')
async def get_ordens(consumidorId: int = None, produtorId: int = None):

    ordens = await Ordem.objects.select_related(
        [Ordem.oferta.usuario, Ordem.comprador]).all()

    if consumidorId is not None:
        ordens = [ordem for ordem in ordens if ordem.comprador.id ==
                  consumidorId]

    if produtorId is not None:
        ordens = [ordem for ordem in ordens if ordem.oferta.usuario.id ==
                  produtorId]

    return ordens
