
from api.models.db_models import Usuario
from api.controllers import users_controller

from mock import patch

@patch('api.controllers.users_controller.add_usuario', return_value=1)
def test_main(mock_test):

    x = Usuario(
        id = 1,
        nome = 'teste',
        telefone = '999999999',
        email = 'teste@teste.com',
        logradouro = 'rua teste',
        numero = 123,
        cep = '99999999',
        cidade = 'sao paulo',
        estado = 'sp',
        cpf_cnpj = '11111111111',
        tipo = 'consumidor',
        senha = '1234'
    )

    y = users_controller.add_usuario(x)

    mock_test.assert_called_once()
