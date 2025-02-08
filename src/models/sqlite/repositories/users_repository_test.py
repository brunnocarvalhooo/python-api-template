import pytest
from src.models.sqlite.settings.connection import db_connection_handler
from .users_repository import UsersRepository

# Conectar ao banco antes dos testes
db_connection_handler.connect_to_db()

# Criar uma fixture apenas para fornecer o repositório
@pytest.fixture(scope="function")
def repo():
    return UsersRepository(db_connection_handler)


# @pytest.mark.skip(reason="db interaction test")
def test_create_user(repo):
    """Testa se um usuário é criado corretamente."""
    repo.create(name="Teste", email="teste@email.com", whatsapp="123456789", password="senha123")
    
    users = repo.list_users()
    assert any(user.email == "teste@email.com" for user in users)


# @pytest.mark.skip(reason="db interaction test")
def test_list_users(repo):
    """Testa se a listagem de usuários retorna pelo menos um usuário."""
    users = repo.list_users()
    assert len(users) > 0  # Apenas verificamos se há usuários no banco


# @pytest.mark.skip(reason="db interaction test")
def test_get_by_id(repo):
    """Testa se conseguimos buscar um usuário pelo ID."""
    users = repo.list_users()
      # Pegando o primeiro usuário da lista
    if users:
        first_user = users[0]
        print(type(first_user.id))
        user = repo.get_by_id(first_user.id)
        assert user is not None
        assert user.id == users[0].id


@pytest.mark.skip(reason="db interaction test")
def test_update_user(repo):
    """Testa se um usuário pode ser atualizado corretamente."""
    users = repo.list_users()
    if users:
        user = users[0]
        success = repo.update(id_user=user.id, name="UpdatedName", active=True)
        updated_user = repo.get_by_id(user.id)

        assert success is True
        assert updated_user.name == "UpdatedName"
        assert updated_user.active is True


@pytest.mark.skip(reason="db interaction test")
def test_delete_user(repo):
    """Testa se um usuário pode ser removido do banco."""
    users = repo.list_users()
    if users:
        user = users[0]
        success = repo.delete(user.id)
        deleted_user = repo.get_by_id(user.id)

        assert success is True
        assert deleted_user is None
