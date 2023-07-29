from abc import ABC, abstractmethod

from src.domain.entity.ong import Ong


class OngRepositoryInterface(ABC):
    @abstractmethod
    def create(self, *, ong: Ong) -> Ong:
        raise NotImplementedError

    @abstractmethod
    def find_by_email(self, *, email: str) -> Ong | None:
        raise NotImplementedError
