from src.application.repository.ong_repository_interface import OngRepositoryInterface
from src.domain.entity.ong import Ong
from src.infra.db.conn import db_session
from src.infra.db.models import OngModel


class OngRepositoryOrm(OngRepositoryInterface):
    def create(self, *, ong: Ong) -> Ong:
        ong_model = OngModel(
            id=ong.id,
            name=ong.name,
            email=ong.email,
            whatsapp=ong.whatsapp,
            document=ong.document,
        )
        db_session.add(ong_model)

        try:
            db_session.commit()
        except Exception as e:
            db_session.rollback()
            raise e

        return ong

    def find_by_email(self, *, email: str) -> Ong | None:
        ong_model = db_session.query(OngModel).filter(OngModel.email == email).first()
        return (
            Ong(
                id=str(ong_model.id),
                name=str(ong_model.name),
                email=str(ong_model.email),
                whatsapp=str(ong_model.whatsapp),
                document=str(ong_model.document),
            )
            if ong_model
            else None
        )
