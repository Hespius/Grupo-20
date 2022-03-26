from fastapi import APIRouter
from models.users import Usuario

router = APIRouter()

#TODO: permitir null vindo do json ao invés de vazio
@router.post("/cadastrar/consumidor")
async def add_consumidor(item: Usuario):

    await  item.save()
    return item

@router.get("/consumidores")
async def get_consumidores():
    return await Usuario.objects.filter(produtor = False).all()


@router.post("/cadastrar/produtor")
async def add_produtor(item: Usuario):

    item.produtor = True

    await  item.save()
    return item

@router.get("/produtores")
async def get_produtores():
    return await Usuario.objects.filter(produtor = True).all()

# @router.post('login')
# async def login(login: LoginForm):
    
