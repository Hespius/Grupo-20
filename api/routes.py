# from sys import prefix
from fastapi import APIRouter
from controllers import users_controller as users

routes = APIRouter()

routes.include_router(users.router, prefix="/usuarios")
