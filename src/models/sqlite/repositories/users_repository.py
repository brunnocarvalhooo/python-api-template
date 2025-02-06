from sqlalchemy.orm.exc import NoResultFound

from src.models.sqlite.entities.uses import UsersTable


class UsersRepository:
    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection

    def list_users(self) -> list[UsersTable]:
        with self.__db_connection as database:
            try:
                users = database.session.query(UsersTable).all()
                return users
            except NoResultFound:
                return []
