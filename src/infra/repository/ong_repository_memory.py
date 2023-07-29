from src.application.repository.ong_repository_interface import OngRepositoryInterface
from src.domain.entity.ong import Ong


class OngRepositoryMemory(OngRepositoryInterface):
    def __init__(self) -> None:
        self.ONGS: list[Ong] = []

    def create(self, *, ong: Ong) -> Ong:
        self.ONGS.append(ong)
        return ong

    def find_by_email(self, *, email: str) -> Ong | None:
        ong = [x for x in self.ONGS if x.email == email]

        return ong[0] if len(ong) > 0 else None
