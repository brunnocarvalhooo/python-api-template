import pytest

from .create_user_controller import CreateUserController

class MockUsersRepostory:
    def create(
        self,
        name: str,
        email: str,
        whatsapp: str,
        password: str
    ) -> None:
        pass

def test_create():
    data = {
        "name": "Teste da Silva",
        "email": "teste@gmail.com",
        "whatsapp": "199999999",
        "password": "123456",
    }

    controller = CreateUserController(MockUsersRepostory())
    response = controller.create(data)

    assert response["message"] == "Usuário criado com sucesso"

def test_create_with_error():
    data = {
        "name": "Teste da Silva",
        "whatsapp": "199999999",
        "password": "123456",
    }

    controller = CreateUserController(MockUsersRepostory())

    with pytest.raises(Exception):
        controller.create(data)
