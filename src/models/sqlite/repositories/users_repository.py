from sqlalchemy.orm.exc import NoResultFound

from src.models.sqlite.entities.uses import UsersTable


class UsersRepository:
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
                    active=False
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
                print(f"Buscando usuário com ID: {id_user}")  # Imprimir o ID que está sendo buscado
                user = database.session.query(UsersTable).filter(str(UsersTable.id) == str(id_user)).first()
                print(f"Usuário encontrado: {user}")  # Imprimir o usuário encontrado
                return user
            except NoResultFound:
                return None

    def update(
        self,
        id_user: str,
        name: str = None,
        whatsapp: str = None,
        password: str = None,
        active: bool = None
    ) -> bool:
        with self.__db_connection as database:
            try:
                user = database.session.query(
                    UsersTable).filter_by(id=id_user).first()
                if not user:
                    return False

                if name:
                    user.name = name
                if whatsapp:
                    user.whatsapp = whatsapp
                if password:
                    user.password = password
                if active is not None:
                    user.active = active

                database.session.commit()
                return True
            except Exception as e:
                database.session.rollback()
                print(f"Erro ao atualizar usuário: {e}")
                return False

    def delete(self, id_user: str) -> bool:
        with self.__db_connection as database:
            try:
                user = database.session.query(
                    UsersTable).filter_by(id=id_user).first()
                if not user:
                    return False

                database.session.delete(user)
                database.session.commit()
                return True
            except Exception as e:
                database.session.rollback()
                print(f"Erro ao deletar usuário: {e}")
                return False
