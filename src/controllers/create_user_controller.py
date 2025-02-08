from src.models.sqlite.interfaces.users_repository import UsersRepositoryInterface


class CreateUserController:
    def __init__(self, users_repository: UsersRepositoryInterface) -> None:
        self.users_repository = users_repository

    def create(self, data: dict) -> dict:
        self.__validate_data(data)

        name = data["name"]
        email = data["email"]
        whatsapp = data["whatsapp"]
        password = data["password"]

        self.__db_interaction(name, email, whatsapp, password)

        return self.__format_response()

    def __validate_data(self, data: dict) -> None:
        missing_fields = []

        if isinstance(data, dict):
            if not data.get("name"):
                missing_fields.append("name")
            if not data.get("email"):
                missing_fields.append("email")
            if not data.get("password"):
                missing_fields.append("password")
        else:
            raise TypeError({"message": "Requisição mal formatada"})

        if missing_fields:
            raise Exception({"message": f"Campos obrigatórios ausentes: {', '.join(missing_fields)}"})

    def __db_interaction(self, name: str = None, email: str = None, whatsapp: str = None, password: str = None) -> None:
        self.users_repository.create(name, email, whatsapp, password)

    def __format_response(self):
        return {"message": "Usuário criado com sucesso"}
