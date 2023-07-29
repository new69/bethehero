from src.application.usercase.create_ong import CreateOng
from src.domain.entity.ong import Ong
from src.infra.repository.ong_repository_memory import OngRepositoryMemory


class TestUsercaseCreateOng:
    def test_create_ong(self) -> None:
        ong_repository = OngRepositoryMemory()
        usercase = CreateOng(repository=ong_repository)
        ong = Ong(name='Ong Test', email='test@test.com', whatsapp='+551199999999', document='123.456.789/0001-10')
        expected_response = usercase.execute(ong=ong)

        assert isinstance(expected_response, Ong)
        assert expected_response.name == ong.name
        assert expected_response.email == ong.email
        assert expected_response.whatsapp == ong.whatsapp
        assert expected_response.document == ong.document
