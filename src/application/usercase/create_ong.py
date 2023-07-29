from src.application.repository.ong_repository_interface import OngRepositoryInterface
from src.domain.entity.ong import Ong


class CreateOng:
    def __init__(self, *, repository: OngRepositoryInterface):
        self.repository = repository

    def execute(self, *, ong: Ong) -> Ong:
        return self.repository.create(ong=ong)


# SOLID
# Single Responsability Principle
# Open Closed Principle
# Liskov Substitution Principle
# Interface Segregation Principle
# Dependency Inversion Principle
