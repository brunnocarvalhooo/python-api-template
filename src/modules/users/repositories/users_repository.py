from sqlite3 import Connection as SQLiteConnection
from sqlalchemy.orm.exc import NoResultFound

from src.config.sql_alchemy.entities.users import UsersTable
from .users_repository_interface import UsersRepositoryInterface


class UsersRepository(UsersRepositoryInterface):
    def __init__(self, db_connection: SQLiteConnection) -> None:
        self.__db_connection = db_connection

    def list_users(self) -> list[UsersTable]:
        with self.__db_connection as database:
            try:
                users = database.session.query(UsersTable).all()
                return users
            except NoResultFound:
                return []
