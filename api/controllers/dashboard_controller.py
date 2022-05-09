from fastapi import APIRouter
import json
router = APIRouter()


@router.get('/receita/{produtorId}')
def buscar_receita(produtorId: int):

    produtor = {}

    with open('api/controllers/dados/receita.json') as file:
        dados = json.load(file)

        filtro = [
            produtor['data'] for produtor in dados if
            produtor['produtorId'] == produtorId]

        produtor = filtro[0]

        produtor['receita_total'] = sum(
            produtor['grafico_dados']['receita_mensal'])

    return produtor


@router.get('/distribuicao/{produtorId}')
def buscar_distribuicao(produtorId: int):

    produtor = {}

    with open('api/controllers/dados/distribuicao_vendas.json') as file:
        dados = json.load(file)

        filtro = [
            produtor['data'] for produtor in dados if
            produtor['produtorId'] == produtorId]

        produtor = filtro[0]

    return produtor


@router.get('/vendas-mensais/{produtorId}')
def buscar_vendas_mensais(produtorId: int):

    produtor = {}

    with open('api/controllers/dados/vendas_mensais.json') as file:
        dados = json.load(file)

        filtro = [
            produtor['dados'] for produtor in dados if
            produtor['produtorId'] == produtorId]

        produtor = filtro[0]

    return produtor
