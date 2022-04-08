from fastapi import APIRouter
from models.db_models import Commodity

router = APIRouter()

# TODO: permitir null vindo do json ao invés de vazio


@router.post("/cadastrar")
async def add_commoditty(item: Commodity):

    await item.save()
    return item


@router.get("/")
async def get_commodities():
    return await Commodity.objects.all()
