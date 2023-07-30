from src.application.usercase.create_ong import CreateOng
from src.application.usercase.find_ong_by_email import FindOngByEmail
from src.domain.entity.ong import Ong
from src.infra.repository.ong_repository_memory import OngRepositoryMemory


class TestFindOngByEmail:
    def test_should_find_ong(self) -> None:
        ong_repository = OngRepositoryMemory()
        ong = Ong(name='Ong Test', email='test@test.com', whatsapp='+55(11)99999999', document='52.203.101/0001-63')
        CreateOng(repository=ong_repository).execute(ong=ong)

        usercase = FindOngByEmail(repository=ong_repository)
        expected_response = usercase.execute(email=ong.email)

        assert expected_response is not None
        assert expected_response.email == ong.email

    def test_should_not_find_any_ong_with_email_is_wrong(self) -> None:
        ong_repository = OngRepositoryMemory()
        ong = Ong(name='Ong Test', email='test@test.com', whatsapp='+55(11)99999999', document='52.203.101/0001-63')
        CreateOng(repository=ong_repository).execute(ong=ong)

        usercase = FindOngByEmail(repository=ong_repository)
        expected_response = usercase.execute(email='test2@test.comn')

        assert expected_response is None

    def test_should_not_find_ong_with_it_not_exists(self) -> None:
        ong_repository = OngRepositoryMemory()
        usercase = FindOngByEmail(repository=ong_repository)
        expected_response = usercase.execute(email='test2@test.comn')

        assert expected_response is None
