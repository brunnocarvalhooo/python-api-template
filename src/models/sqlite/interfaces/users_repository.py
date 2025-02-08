from abc import ABC, abstractmethod

from src.models.sqlite.entities.uses import UsersTable


class UsersRepositoryInterface(ABC):

    @abstractmethod
    def create(
        self,
        name: str,
        email: str,
        whatsapp: str,
        password: str
    ) -> None:
        pass

    @abstractmethod
    def list_users(self) -> list[UsersTable]:
        pass

    @abstractmethod
    def get_by_id(self, id_user: str) -> UsersTable | None:
        pass

    @abstractmethod
    def update(
        self,
        id_user: str,
        name: str = None,
        whatsapp: str = None,
        password: str = None,
    ) -> bool:
        pass

    @abstractmethod
    def delete(self, id_user: str) -> bool:
        pass
