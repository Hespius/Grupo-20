# from sys import prefix
from math import prod
from fastapi import APIRouter

from api.controllers import users_controller as users
from api.controllers import produtos_controller as produtos

routes = APIRouter()

routes.include_router(users.router, prefix="/usuarios")
routes.include_router(produtos.router, prefix="/produtos")
