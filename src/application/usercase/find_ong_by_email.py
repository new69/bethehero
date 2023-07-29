from src.application.repository.ong_repository_interface import OngRepositoryInterface
from src.domain.entity.ong import Ong


class FindOngByEmail:
    def __init__(self, repository: OngRepositoryInterface):
        self.repository = repository

    def execute(self, *, email: str) -> Ong | None:
        return self.repository.find_by_email(email=email)
