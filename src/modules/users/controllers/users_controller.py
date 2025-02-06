from src.modules.users.repositories.users_repository_interface \
    import UsersRepositoryInterface

class CreateUser:
    def __init__(self, users_repository: UsersRepositoryInterface) -> None:
        self.__users_repository = users_repository

    def create(self, data: dict) -> dict:
        print(data)
        # name = data["name"]
        # email = data["email"]
        # whatsapp = data["whatsapp"]
        # avatar = data["avatar"]
        # password = data["password"]
        return self.__users_repository
