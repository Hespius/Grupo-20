from ormar import exceptions
from fastapi import APIRouter, HTTPException

from api.models.dto import LoginForm, ResponseLogin
from api.models.db_models import Usuario

router = APIRouter()

# TODO: permitir null vindo do json ao invés de vazio


@router.post("/cadastrar")
async def add_usuario(item: Usuario):

    usuario_repetido = await Usuario.objects.all(email=item.email)
    print(usuario_repetido)

    if len(usuario_repetido) > 0:
        raise HTTPException(status_code=404, detail='e-mail já cadastrado')

    await item.save()
    return item


@router.get("/consumidores")
async def get_consumidores():
    return await Usuario.objects.filter(tipo='Consumidor').all()


@router.get("/produtores")
async def get_produtores():
    return await Usuario.objects.filter(tipo='Produtor').all()


@router.post('/login')
async def login(login: LoginForm):

    user: Usuario = {}

    try:
        user = await Usuario.objects.get(email=login.email, senha=login.senha)

    except exceptions.NoMatch:
        raise HTTPException(status_code=404,
                            detail='Login ou senha incorretos')

    responseObj = ResponseLogin(user)

    return responseObj
