from math import prod
from ormar import exceptions
from fastapi import APIRouter
from models.produtos import Produto
from models.users import Response, Usuario

router = APIRouter()

# TODO: permitir null vindo do json ao invés de vazio
@router.post("/cadastrar")
async def add_consumidor(item: Produto):

    await item.save()
    return item

@router.get("/")
async def get_produtos():
    return await Produto.objects.all()