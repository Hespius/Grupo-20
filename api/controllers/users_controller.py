from fastapi import APIRouter
from models.users import Consumidor, Produtor

router = APIRouter()

consumidores = []
produtores = []

@router.post("/cadastrar/consumidor")
async def add_consumidor(item: Consumidor):

    if len([consumidor for consumidor in consumidores if consumidor.email == item.email]) > 0:
        return { "sucesso": False, "mensagem": "email já cadastrado"}

    consumidores.append(item)

    return { "sucesso": True, "mensagem": ""}

@router.get("/consumidores")
async def get_consumidores():
    return consumidores


@router.post("/cadastrar/produtor")
async def add_produtor(item: Produtor):

    if len([produtor for produtor in produtores if produtor.email == item.email]) > 0:
        return { "sucesso": False, "mensagem": "email já cadastrado"}

    produtores.append(item)

    return { "sucesso": True, "mensagem": ""}

@router.get("/produtores")
async def get_produtores():
    return produtores
