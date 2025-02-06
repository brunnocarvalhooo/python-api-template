import pytest

from src.config.sql_alchemy.connection import db_connection_handler
from .users_repository import UsersRepository

db_connection_handler.connect_to_db()


@pytest.mark.skip(reason="db integration test")
def test_list_users():
    repo = UsersRepository(db_connection_handler)
    response = repo.list_users()
    print(response)
