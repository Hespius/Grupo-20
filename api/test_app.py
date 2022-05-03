from urllib import response
from api.main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_get_consumidores():
    response = client.get('usuarios/consumidores')
    assert response.status_code == 200


def test_get_produtores():
    response = client.get('usuarios/produtores')
    assert response.status_code == 200


def test_get_produtos_commodities():
    response = client.get('produtos/commodities')
    assert response.status_code == 200


def test_get_produtos_ofertas():
    response = client.get('produtos/ofertas')
    assert response.status_code == 200


def test_get_produtos_ordem():
    response = client.get('produtos/ordem')
    assert response.status_code == 200