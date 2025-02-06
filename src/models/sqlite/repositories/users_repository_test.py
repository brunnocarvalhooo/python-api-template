from src.models.sqlite.settings.connection import db_connection_handler

from .users_repository import UsersRepository

db_connection_handler.connect_to_db()


def test_list_users():
    repo = UsersRepository(db_connection_handler)
    reponse = repo.list_users()
    print(reponse)
