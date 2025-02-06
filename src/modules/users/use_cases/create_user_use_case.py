from src.modules.users.repositories.users_repository_interface import UsersRepositoryInterface
from src.shared.infra.http_types.http_request import HttpRequest
from src.shared.infra.http_types.http_response import HttpResponse

class CreateUserUseCase:
    def __init__(self, users_repository: UsersRepositoryInterface):
        self.users_repository = users_repository

    def execute(self, http_request: HttpRequest) -> HttpResponse:
        pass
