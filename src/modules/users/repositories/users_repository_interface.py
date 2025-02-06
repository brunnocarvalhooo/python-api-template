from abc import abstractmethod, ABC

from src.config.sql_alchemy.entities.users import UsersTable


class UsersRepositoryInterface(ABC):
    @abstractmethod
    def list_users(self) -> list[UsersTable]:
        pass
