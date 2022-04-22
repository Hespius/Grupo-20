from datetime import datetime
from fastapi import APIRouter

from api.models.db_models import Commodity, Oferta, Usuario, Ordem
from api.models.dto import OfertaDto, Response

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
async def add_oferta(produtorId: int, commodityName: str, oferta: Oferta):
    produtor = await Usuario.objects.get_or_none(id=produtorId)

    if produtor is None:
        return Response(sucesso=False, mensagem='Produtor não encontrado')

    commodity = await Commodity.objects.get_or_none(nome=commodityName)

    if commodity is None:
        return Response(sucesso=False, mensagem='Commodity não encontrada')

    oferta.data_cadastro = datetime.now()
    oferta.saldo = oferta.quantidade

    await produtor.commodity.add(commodity, data_cadastro=oferta.data_cadastro,
                                 data_disponivel=oferta.data_disponivel,
                                 quantidade=oferta.quantidade,
                                 preco=oferta.preco)

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

    # ordemDB = await Ordem.objects.select_all().all()

    return ordemDB


@router.get('/ordem')
async def get_ordens(consumidorId: int, produtorId: int):

    ordens = await Ordem.objects.select_all().all()

    # ordemDB = await Ordem.objects.select_all().all()

    return ordens
