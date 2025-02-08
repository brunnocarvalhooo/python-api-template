from sqlalchemy.orm.exc import NoResultFound

from src.models.sqlite.entities.uses import UsersTable
from src.models.sqlite.interfaces.users_repository import UsersRepositoryInterface


class UsersRepository(UsersRepositoryInterface):
    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection

    def create(
        self,
        name: str,
        email: str,
        whatsapp: str,
        password: str
    ) -> None:
        with self.__db_connection as database:
            try:
                user = UsersTable(
                    name=name,
                    email=email,
                    whatsapp=whatsapp,
                    password=password,
                    status=True,
                )
                database.session.add(user)
                database.session.commit()
            except Exception as e:
                database.session.rollback()
                print(f"Erro ao criar usuário: {e}")

    def list_users(self) -> list[UsersTable]:
        with self.__db_connection as database:
            try:
                return database.session.query(UsersTable).all()
            except NoResultFound:
                return []

    def get_by_id(self, id_user: str) -> UsersTable | None:
        with self.__db_connection as database:
            try:
                user = database.session.query(UsersTable).filter(UsersTable.id == id_user).with_entities(
                    UsersTable.id,
                    UsersTable.name,
                    UsersTable.email,
                    UsersTable.whatsapp,
                ).one_or_none() 
                return user
            except NoResultFound:  
                return None

    def update(
        self,
        id_user: str,
        name: str = None,
        whatsapp: str = None,
        password: str = None,
    ) -> bool:
        with self.__db_connection as database:
            try:
                user = database.session.query(UsersTable).filter_by(id=id_user).one_or_none()
                if not user:
                    return False

                if name:
                    user.name = name
                if whatsapp:
                    user.whatsapp = whatsapp
                if password:
                    user.password = password

                database.session.commit()
                return True
            except Exception as e:
                database.session.rollback()
                print(f"Erro ao atualizar usuário: {e}")
                return False

    def delete(self, id_user: str) -> bool:
        with self.__db_connection as database:
            try:
                user = database.session.query(UsersTable).filter_by(id=id_user).first()
                if not user:
                    return False

                database.session.delete(user)
                database.session.commit()
                return True
            except Exception as e:
                database.session.rollback()
                print(f"Erro ao deletar usuário: {e}")
                return False
