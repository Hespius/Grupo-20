from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_get_consumidores():
    response = client.get('usuarios/consumidores')
    print(response)
    assert response.status_code == 200
