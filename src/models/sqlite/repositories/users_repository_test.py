import pytest
from src.models.sqlite.settings.connection import db_connection_handler
from .users_repository import UsersRepository

db_connection_handler.connect_to_db()


@pytest.fixture(scope="function")
def repo():
    return UsersRepository(db_connection_handler)


@pytest.mark.skip(reason="db interaction test")
def test_create_user(repo):
    repo.create(name="Teste", email="teste@email.com",
                whatsapp="123456789", password="senha123")

    users = repo.list_users()
    assert any(user.email == "teste@email.com" for user in users)


@pytest.mark.skip(reason="db interaction test")
def test_list_users(repo):
    users = repo.list_users()
    assert len(users) > 0


@pytest.mark.skip(reason="db interaction test")
def test_get_by_id(repo):
    users = repo.list_users()
    if users:
        user = users[0]
        finded_user = repo.get_by_id(user.id)
        assert finded_user is not None
        assert finded_user.id == user.id


@pytest.mark.skip(reason="db interaction test")
def test_update_user(repo):
    users = repo.list_users()
    if users:
        user = users[0]
        success = repo.update(id_user=user.id, name="UpdatedName")
        updated_user = repo.get_by_id(user.id)

        assert success is True
        assert updated_user.name == "UpdatedName"


@pytest.mark.skip(reason="db interaction test")
def test_delete_user(repo):
    users = repo.list_users()
    if users:
        user = users[0]
        success = repo.delete(user.id)
        deleted_user = repo.get_by_id(user.id)

        assert success is True
        assert deleted_user is None
